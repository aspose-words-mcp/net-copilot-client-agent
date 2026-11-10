"""Normalize Copilot CLI event logs and render per-run Q&A reports."""
import json
from pathlib import Path
from checkpoint import atomic_write


def extract(path):
    events = []
    warnings = []
    for index, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            warnings.append(f'Non-JSON output at line {index}; inspect events.jsonl.')
    messages = []
    models = set()
    calls = {}
    agent_names = []
    for event in events:
        kind, data = event.get('type'), event.get('data', {})
        if kind == 'session.custom_agents_updated':
            agent_names = [a.get('id') for a in data.get('agents', [])]
        if kind == 'session.auto_mode_resolved' and data.get('chosenModel'):
            models.add(data['chosenModel'])
        if kind == 'assistant.message':
            if data.get('model'):
                models.add(data['model'])
            if data.get('content') and not data.get('toolRequests'):
                messages.append(data['content'])
        if kind == 'tool.execution_start':
            # A new tool call makes previous prose intermediate, not the final answer.
            messages = []
            calls[data['toolCallId']] = {'name': data.get('toolName'),
                                         'server': data.get('mcpServerName'), 'completed': False}
        if kind == 'tool.execution_complete':
            call = calls.setdefault(data['toolCallId'], {'name': None, 'server': None})
            exit_code = data.get('shellExecution', {}).get('exitCode')
            call.update(completed=True, success=data.get('success'), exit_code=exit_code,
                        failed=data.get('success') is False or exit_code not in (None, 0))
            if 'Saved to:' in json.dumps(data.get('result', {})):
                warnings.append('Tool evidence includes a temporary-file reference; the trace may not contain full documentation.')
        if kind == 'session.error':
            warnings.append('CLI session reported an error; inspect the event log.')
    answer = '\n\n'.join(messages)
    if not answer:
        warnings.append('No final assistant answer found.')
    if not any(c.get('server') == 'words-net' for c in calls.values()):
        warnings.append('No words-net call recorded.')
    if any(c.get('failed') for c in calls.values()):
        warnings.append('One or more tool executions failed; review the trace.')
    return {'recorded_answer_markdown': answer, 'resolved_models': sorted(models),
            'discovered_agent_ids': agent_names, 'tools': list(calls.values()),
            'warnings': list(dict.fromkeys(warnings))}


GROUP_TITLES = {
    'word-to-pdf': 'Word to PDF', 'word-to-html': 'Word to HTML',
    'word-to-excel': 'Word to Excel', 'word-to-markdown': 'Word to Markdown',
    'word-to-image': 'Word to Image', 'pdf-to-other': 'PDF to Other Formats',
    'linq-reporting': 'LINQ Reporting', 'mail-merge': 'Mail Merge',
    'compare': 'Compare Documents', 'split': 'Split Documents',
    'merge': 'Merge Documents', 'find-replace': 'Find and Replace',
    'digital-signatures': 'Digital Signatures', 'watermark': 'Watermarks',
    'ai': 'AI Features',
}


def question_index(records):
    groups = {}
    for record in records:
        groups.setdefault(record.get('group') or 'other', []).append(record)
    lines = []
    for group in list(GROUP_TITLES) + sorted(set(groups) - set(GROUP_TITLES)):
        if group not in groups:
            continue
        title = GROUP_TITLES.get(group, group.replace('-', ' ').title())
        lines += [f'### {title}', '']
        for record in sorted(groups[group], key=lambda r: r['query_id']):
            lines.append(f"- [{record['question']}](#{record['query_id']})")
        lines.append('')
    return lines


def report(run, records, selected, config, elapsed, interrupted=False):
    """Publish only the presentation and aggregate metrics; never raw traces."""
    from collections import Counter

    records = sorted(records, key=lambda r: r['query_id'])
    complete = [r for r in records if r['status'] == 'completed']
    verification = config.get('verification')
    intro = (f'{len(complete)} questions and answers generated with GitHub Copilot CLI and the '
             'Aspose.Words for .NET MCP server, using '
             '`csharp-build-rules.instructions.md` and `error-correction.md`. ')
    if verification:
        intro += (f"C# examples were checked for compilation using Aspose.Words for .NET {verification['package_version']} "
                  f"with target framework {verification['target_framework']}; see [metrics](metrics.md) for outcomes. ")
    else:
        intro += 'C# examples were not checked for compilation. '
    intro += 'Initial generations use fresh sessions.'
    if any(r.get('answer_source') for r in records):
        intro += ' Saved-answer replays are labeled below.'
    lines = ['# Aspose.Words for .NET — Copilot Showcase', '', intro, '',
             '[Client setup](../../../README.md#quick-start)', '', '## Questions', '']
    lines += question_index(records)
    lines += ['', '## Answers', '']
    generation_models, repair_models = Counter(), Counter()
    compilation = Counter()
    first_pass = repaired = repair_requests = no_repair = 0
    exceptions = []
    for r in records:
        attempts = r.get('verification', {}).get('attempts', [])
        repairs = [a['repair'] for a in attempts if a.get('repair') is not None]
        repair_requests += len(repairs)
        gm = r.get('resolved_models') or ['unknown']
        rm = sorted({m for a in repairs for m in (a.get('resolved_models') or ['unknown'])})
        if not r.get('answer_source'):
            generation_models.update(set(gm))
        repair_models.update(rm)
        status = r.get('compilation_status', 'not_run')
        if verification and r['status'] == 'completed' and 'compilation_status' not in r:
            status = 'incomplete'
        compilation[status] += 1
        passed_after_repair = status == 'passed' and bool(repairs)
        repaired += passed_after_repair
        first_pass += status == 'passed' and not repairs
        no_repair += r['status'] == 'completed' and not repairs and not r.get('answer_source')
        if r.get('answer_source'):
            note = 'Answer loaded from a saved answer.'
        elif passed_after_repair:
            note = 'Answer refined after a compilation repair.'
        elif r['status'] != 'completed':
            note = f"Answer generation {r['status']}."
        elif r.get('generation_attempts', 1) > 1:
            note = 'Answer generated after resuming the run.'
        else:
            note = 'Answer generated on first attempt.'
        models = 'Generation model: ' + ('not applicable (saved answer)' if r.get('answer_source') else ', '.join(gm))
        if rm:
            models += ' · Repair model: ' + ', '.join(rm)
        answer = r.get('verified_answer_markdown') or r.get('recorded_answer_markdown') or '*No final answer captured.*'
        lines += [f"<a id=\"{r['query_id']}\"></a>", '', f"### {r['question']}", '', note+'  ', models, '', answer, '']
        if r['status'] != 'completed' or status not in {'passed', 'no_code', 'not_run'}:
            reasons = sorted({c for a in attempts for b in a.get('compilation', {}).get('results', []) for c in b.get('diagnostic_codes', [])})
            detail = ', '.join(reasons) or next((a['compilation']['reason'] for a in attempts if a.get('compilation', {}).get('reason')), '')
            exceptions.append(f"| {r['query_id']} | {r['status']} | {status} | {detail or 'See status; detailed logs are not retained.'} |")
    atomic_write(run/'showcase.md', '\n'.join(lines))
    known = (set(generation_models) | set(repair_models)) - {'unknown'}
    summary = ['# Showcase run metrics', '',
               '| Check | Status |', '| --- | --- |', '| Runtime behavior | Not checked |', '',
               '| Metric | Count |', '| --- | ---: |',
               f'| Selected questions | {selected} |', f'| Attempted questions | {len(records)} |',
               f'| Completed answers | {len(complete)} |', f'| Failed/incomplete generations | {len(records)-len(complete)} |',
               f'| Remaining questions | {selected-len(records)} |',
               f'| Generated answers completed without repair | {no_repair} |',
               f'| Compilation passed on first attempt | {first_pass} |',
               f'| Compilation passed after repair | {repaired} |',
               f'| Repair requests | {repair_requests} |',
               f'| Generation retries | {sum(max(0, r.get("generation_attempts", 1)-1) for r in records)} |',
               f'| Saved-answer replays | {sum(bool(r.get("answer_source")) for r in records)} |',
               f'| Distinct known models | {len(known)} |', '',
               'Question outcomes, model counts, and repair counts describe the latest attempt per question; duration includes all saved sessions.', '',
               f'Run interrupted: {"yes" if interrupted else "no"}.',
               f'Total duration: {elapsed:.2f} seconds. Average per attempted question: {elapsed/len(records) if records else 0:.2f} seconds.', '',
               '## Compilation', '', '| Status | Questions |', '| --- | ---: |']
    for status in ['passed', 'failed', 'no_code', 'not_run', 'unavailable', 'timeout', 'incomplete']:
        summary.append(f'| {status} | {compilation[status]} |')
    summary += ['', 'No-code and unchecked answers are not compilation successes.', '', '## Models', '',
                'Counts are distinct questions per model and role; one question can use multiple models. Unknown identities are not counted as known models.', '',
                '| Model | Generation questions | Repair questions |', '| --- | ---: | ---: |']
    for model in sorted(set(generation_models) | set(repair_models)):
        summary.append(f'| {model} | {generation_models[model]} | {repair_models[model]} |')
    summary += ['', '## Exceptions', '']
    summary += (['| Question | Generation | Compilation | Reason |', '| --- | --- | --- | --- |'] + exceptions) if exceptions else ['None.']
    atomic_write(run/'metrics.md', '\n'.join(summary)+'\n')
