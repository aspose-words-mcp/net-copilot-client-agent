"""Offline integration coverage: no model requests or SDK required."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import run_copilot


class RunnerTests(unittest.TestCase):
    def run_fixture(self, interrupt=False):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        source = run_copilot.ROOT
        for relative in ['.github/agents/aspose-words-mcp.agent.md', '.github/copilot-instructions.md',
                         'examples/error-correction.md', 'examples/csharp-build-rules.instructions.md',
                         'showcase/scripts/read_mcp_response.py', 'showcase/inputs/questions.json', '.vscode/mcp.json']:
            target = root/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text((source/relative).read_text())
        (root/'.vscode/mcp.json').write_text(json.dumps({'servers': {
            'words-net': {'type': 'http', 'url': 'https://mcp.example.test/endpoint'}}}))
        workspaces = []
        def invoke(command, cwd, stdout, stderr, timeout):
            workspaces.append(cwd)
            if interrupt:
                raise KeyboardInterrupt
            stdout.write_text(json.dumps({'type': 'assistant.message', 'data': {'content': 'Final answer.', 'model': 'test-model'}}))
            stderr.write_text('')
            return {'status': 'completed', 'exit_code': 0}
        with patch.object(run_copilot, 'ROOT', root), patch('sys.argv', ['runner', '--run', 'test']), \
             patch('run_copilot.shutil.which', return_value='/fake/copilot'), \
             patch('run_copilot.subprocess.check_output', return_value='test-version'), \
             patch('run_copilot.run_logged', side_effect=invoke), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            if interrupt:
                with self.assertRaises(SystemExit):
                    run_copilot.main()
            else:
                run_copilot.main()
            with self.assertRaises(SystemExit):
                run_copilot.main()
            if not interrupt:
                with patch('sys.argv', ['runner', '--run', 'test', '--resume']), \
                     patch('run_copilot.run_logged') as resumed:
                    run_copilot.main()
                    resumed.assert_not_called()
                checkpoint = (root/'showcase/runs/test/checkpoint.json').read_bytes()
                with patch('sys.argv', ['runner', '--run', 'test', '--resume', '--model', 'changed']):
                    with self.assertRaises(SystemExit):
                        run_copilot.main()
                self.assertEqual((root/'showcase/runs/test/checkpoint.json').read_bytes(), checkpoint)
        output = root/'showcase/runs/test'
        self.assertEqual(sorted(p.name for p in output.iterdir()), ['checkpoint.json', 'metrics.md', 'showcase.md'])
        self.assertTrue(all(not p.exists() for p in workspaces))
        return output

    def test_success_and_cleanup(self):
        output = self.run_fixture()
        showcase = (output/'showcase.md').read_text()
        self.assertIn('## Questions\n', showcase)
        self.assertIn('## Answers\n', showcase)
        self.assertIn('Answer generated on first attempt.  \nGeneration model: test-model', showcase)
        analysis = (output/'metrics.md').read_text()
        self.assertIn('| Completed answers | 1 |', analysis)
        self.assertIn('| Compilation passed on first attempt | 0 |', analysis)

    def test_interruption_preserves_attempt_and_cleans(self):
        analysis = (self.run_fixture(True)/'metrics.md').read_text()
        self.assertIn('| Attempted questions | 1 |', analysis)
        self.assertIn('| Failed/incomplete generations | 1 |', analysis)
        self.assertIn('Run interrupted: yes.', analysis)

    def test_reflection_switch_rejected(self):
        with patch('sys.argv', ['runner', '--local-reflection']), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                run_copilot.main()
        self.assertEqual(error.exception.code, 2)

class AnalysisTests(unittest.TestCase):
    def test_repair_model_counts_and_compilation_are_separate(self):
        from copilot_results import report
        records = [
            {'query_id': 'a', 'question': 'A?', 'status': 'completed', 'resolved_models': ['one'],
             'recorded_answer_markdown': 'Original', 'verified_answer_markdown': 'Fixed',
             'compilation_status': 'passed', 'verification': {'attempts': [
                 {'compilation': {'status': 'failed'}, 'repair': None},
                 {'compilation': {'status': 'failed'}, 'repair': {'resolved_models': ['two']}},
                 {'compilation': {'status': 'passed'}, 'repair': {'resolved_models': ['two']}}]}},
            {'query_id': 'b', 'question': 'B?', 'status': 'completed', 'resolved_models': [],
             'recorded_answer_markdown': 'Conceptual', 'compilation_status': 'no_code'},
            {'query_id': 'c', 'question': 'C?', 'status': 'timeout', 'recorded_answer_markdown': ''}]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            report(root, records, 4, {'verification': {'package_version': '26.10.0', 'target_framework': 'net10.0'}}, 3)
            analysis = (root/'metrics.md').read_text()
            self.assertIn('| Distinct known models | 2 |', analysis)
            self.assertIn('| two | 0 | 1 |', analysis)
            self.assertIn('| Repair requests | 2 |', analysis)
            self.assertIn('| Compilation passed on first attempt | 0 |', analysis)
            self.assertIn('| Compilation passed after repair | 1 |', analysis)
            self.assertIn('| Remaining questions | 1 |', analysis)
            showcase = (root/'showcase.md').read_text()
            self.assertIn('Answer refined after a compilation repair.  \nGeneration model: one · Repair model: two', showcase)
            self.assertIn('Fixed', showcase)
            self.assertNotIn('Original', showcase)
