#!/usr/bin/env python3
"""Run saved questions in fresh Copilot CLI sessions (one question by default)."""
import argparse
import fcntl
import os
import hashlib
import json
import re
import shutil
import subprocess
import time
import uuid
import tempfile
from pathlib import Path
from urllib.parse import urlsplit
from copilot_results import extract, report
from checkpoint import save, load, completed
from compile_copilot import VERSION, TARGET, run_logged, verify_and_repair

ROOT = Path(__file__).resolve().parents[2]


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT/'showcase/inputs/questions.json')
    parser.add_argument('--run', default='showcase-01')
    parser.add_argument('--model', default='auto')
    parser.add_argument('--limit', type=int, default=1, help='Maximum selected questions; default 1')
    parser.add_argument('--all', action='store_true', help='Select every question matching the filters')
    parser.add_argument('--group', help='Select cases with this exact group name')
    parser.add_argument('--query-id', help='Select one query_id')
    parser.add_argument('--timeout', type=int, default=300)
    parser.add_argument('--verify-code', action='store_true', help='Compile C# and run bounded Copilot repair')
    parser.add_argument('--repair-attempts', type=int, default=2)
    parser.add_argument('--aspose-version', default='26.10.0')
    parser.add_argument('--target-framework', default='net10.0')
    parser.add_argument('--build-timeout', type=int, default=120)
    parser.add_argument('--answer-file', type=Path, help='Verify a saved answer for one selected case; requires --verify-code')
    parser.add_argument('--resume', action='store_true', help='Retry unfinished questions from the saved checkpoint')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.run) or args.limit < 1 or args.timeout < 1:
        parser.error('Use a simple run name and positive limit/timeout.')
    if args.repair_attempts < 0 or args.repair_attempts > 5 or args.build_timeout < 1:
        parser.error('Use 0–5 repair attempts and a positive build timeout.')
    if not VERSION.fullmatch(args.aspose_version) or not TARGET.fullmatch(args.target_framework):
        parser.error('Use an explicit Aspose version and net8.0, net9.0 or net10.0.')
    cases = json.loads(args.input.read_text(encoding='utf-8'))['cases']
    ids = [c['query_id'] for c in cases]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r'[A-Za-z0-9_-]+', i) for i in ids):
        parser.error('Case IDs must be unique simple filenames.')
    if args.group:
        cases = [c for c in cases if c.get('group') == args.group]
    if args.query_id:
        cases = [c for c in cases if c['query_id'] == args.query_id]
    if not args.all:
        cases = cases[:args.limit]
    if not cases:
        parser.error('No matching questions.')
    if args.answer_file and (not args.verify_code or len(cases) != 1):
        parser.error('--answer-file requires --verify-code and exactly one selected case.')
    replay_answer = args.answer_file.read_text(encoding='utf-8') if args.answer_file else None
    binary = shutil.which('copilot')
    if not binary:
        parser.error('copilot not found on PATH.')
    agent = (ROOT/'.github/agents/aspose-words-mcp.agent.md').read_text(encoding='utf-8')
    reader = (ROOT/'showcase/scripts/read_mcp_response.py').read_text(encoding='utf-8')
    instructions = (ROOT/'.github/copilot-instructions.md').read_text(encoding='utf-8')
    rules = (ROOT/'examples/error-correction.md').read_text(encoding='utf-8')
    build_rules = (ROOT/'examples/csharp-build-rules.instructions.md').read_text(encoding='utf-8')
    server = json.loads((ROOT/'.vscode/mcp.json').read_text(encoding='utf-8'))['servers']['words-net']
    endpoint = server.get('url', '')
    parsed_endpoint = urlsplit(endpoint)
    if (parsed_endpoint.scheme not in {'http', 'https'} or not parsed_endpoint.hostname
            or 'YOUR_' in endpoint.upper()):
        parser.error('Configure a real words-net HTTP endpoint in .vscode/mcp.json; '
                     'YOUR_MCP_HOST/YOUR_MCP_ENDPOINT is only a placeholder.')
    server = dict(server, tools=['*'])
    config = {'model': args.model, 'agent_sha256': digest(agent),
              'instructions_sha256': digest(instructions), 'response_reader_sha256': digest(reader),
              'code_rules_sha256': digest(rules), 'build_rules_sha256': digest(build_rules),
              'mcp_sha256': digest(json.dumps(server, sort_keys=True)),
              'runner_sha256': digest(Path(__file__).read_text(encoding='utf-8')),
              'cli_version': subprocess.check_output([binary, '--version'], text=True, encoding='utf-8', errors='replace').strip()}
    if args.verify_code:
        config['verification'] = {'package_version': args.aspose_version, 'target_framework': args.target_framework,
                                  'repair_attempts': args.repair_attempts,
                                  'sdk_policy_sha256': digest((ROOT/'examples/global.json').read_text(encoding='utf-8')),
                                  'compiler_sha256': digest((ROOT/'showcase/scripts/compile_copilot.py').read_text(encoding='utf-8'))}
    if replay_answer is not None:
        config['replay_answer_sha256'] = digest(replay_answer)
    destination = ROOT/'showcase/runs'/args.run
    run = destination
    if args.dry_run:
        print(json.dumps({'run': str(run), 'questions': cases, 'configuration': config}, indent=2))
        return
    if args.resume:
        if not (destination/'checkpoint.json').is_file():
            parser.error('No checkpoint found; start a new run without --resume.')
    else:
        try:
            destination.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            parser.error('Run already exists; use --resume or choose a new --run name.')
    # Lock the directory itself: no persistent lock file and automatic release on exit/crash.
    lock_fd = os.open(destination, os.O_RDONLY)
    try:
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error('This run is already active in another process.')
        if args.resume:
            try:
                state = load(destination/'checkpoint.json', config, cases)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                parser.error(f'Cannot resume: {exc}')
        else:
            state = dict(version=1, config=config, cases=cases, records=[], elapsed=0)
            save(destination/'checkpoint.json', state)
        with tempfile.TemporaryDirectory(prefix='copilot-showcase-') as temporary:
            run = Path(temporary)
            workspace = run/'workspace'
            (workspace/'.github/agents').mkdir(parents=True)
            (workspace/'examples').mkdir()
            # The controller owns compilation and repair; the model only retrieves evidence and answers.
            controller_rule = ('\n# Showcase controller\n'
                'The controller handles optional compilation and bounded repair after your response. '
                'Do not build, restore, edit files, or attempt your own compilation repairs. '
                'Read examples/csharp-build-rules.instructions.md and examples/error-correction.md '
                'for code quality. Return the answer without claiming controller verification.\n')
            agent = agent.split('# Verify C# before presenting the final answer')[0] + controller_rule
            instructions = instructions.split('- Before generating C# examples,')[0] + controller_rule
            (workspace/'.github/agents/aspose-words-mcp.agent.md').write_text(agent, encoding='utf-8')
            (workspace/'.github/copilot-instructions.md').write_text(instructions, encoding='utf-8')
            (workspace/'examples/csharp-build-rules.instructions.md').write_text(build_rules, encoding='utf-8')
            (workspace/'examples/error-correction.md').write_text(rules, encoding='utf-8')
            (workspace/'examples/README.md').write_text(controller_rule, encoding='utf-8')
            (workspace/'showcase/scripts').mkdir(parents=True)
            (workspace/'showcase/scripts/read_mcp_response.py').write_text(reader, encoding='utf-8')
            run_cases(args, cases, binary, server, replay_answer, run, workspace, destination, config, state)
    finally:
        os.close(lock_fd)


def run_cases(args, cases, binary, server, replay_answer, run, workspace, destination, config, state):
    records = state['records']
    previous_elapsed = state['elapsed']
    run_started = time.monotonic()
    interrupted = False
    failed = False
    def persist():
        state.update(records=records, elapsed=previous_elapsed + time.monotonic()-run_started,
                     interrupted=interrupted)
        save(destination/'checkpoint.json', state)
        report(destination, records, len(cases), config, state['elapsed'], interrupted)

    try:
        for case in cases:
            old = next((r for r in records if r['query_id'] == case['query_id']), None)
            if old and completed(old, args.verify_code):
                print('Skipping completed:', case['query_id'], flush=True)
                continue
            output = run/case['query_id']
            output.mkdir(exist_ok=True)
            record_path = output/'result.json'
            session_id = str(uuid.uuid4())
            command = [binary, '-C', str(workspace), '--trust-folder',
                       '--agent', 'aspose-words-mcp', '--model', args.model,
                       '--name', session_id, '--no-ask-user', '--no-auto-update',
                       '--disable-builtin-mcps', '--disable-mcp-server', 'ide',
                       '--additional-mcp-config', json.dumps({'mcpServers': {'words-net': server}}),
                       '--allow-tool=words-net', '--allow-tool=shell(python3:*)',
                       '--allow-tool=shell(jq:*)', '--allow-tool=shell(head:*)',
                       '--allow-tool=shell(tail:*)', '--allow-tool=shell(cat:*)',
                       '--deny-tool=write', '--output-format', 'json',
                       '-p', case['question']]
            def invoke(prompt, folder):
                folder.mkdir(parents=True, exist_ok=True)
                invocation = list(command)
                invocation[invocation.index('--name') + 1] = str(uuid.uuid4())
                invocation[-1] = prompt
                execution = run_logged(invocation, workspace, folder/'events.jsonl', folder/'stderr.log', args.timeout)
                return dict(extract(folder/'events.jsonl'), execution_status=execution['status'],
                            exit_code=execution['exit_code'], session_name=invocation[invocation.index('--name') + 1])

            print('Running:', case['query_id'], flush=True)
            started = time.time()
            record = dict(case, status='incomplete', recorded_answer_markdown='', resolved_models=[],
                          generation_attempts=(old or {}).get('generation_attempts', 0)+1)
            if old is not None:
                records.remove(old)
            records.append(record)
            persist()
            if replay_answer is None:
                initial = invoke(case['question'], output)
            else:
                initial = {'recorded_answer_markdown': replay_answer, 'execution_status': 'completed',
                           'exit_code': None, 'resolved_models': [], 'tools': [], 'warnings': [],
                           'session_name': None, 'answer_source': str(args.answer_file.resolve())}
            status = initial['execution_status']
            record.update(status=status, elapsed_seconds=round(time.time()-started, 3),
                          model=args.model, review_status='unreviewed', **initial)
            if status == 'completed' and not record['recorded_answer_markdown']:
                status = record['status'] = 'incomplete'
            (output/'answer.md').write_text(record['recorded_answer_markdown']+'\n', encoding='utf-8')
            # Temporary working records are removed when the run finishes.
            record_path.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
            persist()
            if args.verify_code and status == 'completed':
                accepted, verification = verify_and_repair(
                    case['question'], record['recorded_answer_markdown'], output,
                    args.aspose_version, args.target_framework, args.build_timeout,
                    args.repair_attempts, invoke)
                record['verification'] = verification
                record['compilation_status'] = verification['status']
                if verification['accepted']:
                    record['verified_answer_markdown'] = accepted
                record['total_elapsed_seconds'] = round(time.time()-started, 3)
                record_path.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
                if verification['status'] not in {'passed', 'no_code'}:
                    failed = True
            persist()
            print(status, 'compilation:', record.get('compilation_status', 'not_run'),
                  flush=True)
            if status != 'completed':
                failed = True
                break
    except KeyboardInterrupt:
        interrupted = True
        failed = True
        print('Interrupted; saving partial reports.', flush=True)
    except Exception as exc:
        interrupted = True
        failed = True
        print(f'Run stopped: {type(exc).__name__}. Partial reports saved.', flush=True)
    finally:
        persist()
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
