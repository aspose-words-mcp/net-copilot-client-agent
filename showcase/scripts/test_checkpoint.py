import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from checkpoint import save, load, completed
from run_copilot import run_cases


class ResumeTests(unittest.TestCase):
    def test_atomic_failure_preserves_previous_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'checkpoint.json'
            save(p, {'old': True})
            with patch('checkpoint.os.replace', side_effect=OSError('failure')):
                with self.assertRaises(OSError):
                    save(p, {'old': False})
            self.assertEqual(json.loads(p.read_text()), {'old': True})
            self.assertEqual(list(p.parent.iterdir()), [p])

    def test_compatibility_and_compaction(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'checkpoint.json'
            save(p, dict(version=1, config={'model': 'one'}, cases=[], records=[], elapsed=0,
                         diagnostics='large', tools=['large']))
            self.assertNotIn('diagnostics', p.read_text())
            self.assertEqual(load(p, {'model': 'one'}, [])['records'], [])
            with self.assertRaises(ValueError):
                load(p, {'model': 'two'}, [])
            with self.assertRaises(ValueError):
                load(p, {'model': 'one'}, [{'query_id': 'new'}])

    def test_verified_skip_policy(self):
        for status in ['passed', 'no_code', 'failed', 'timeout', 'unavailable', 'not_run']:
            r = dict(status='completed', recorded_answer_markdown='Answer', compilation_status=status)
            self.assertEqual(completed(r, True), status in {'passed', 'no_code'})
            self.assertTrue(completed(r, False))

    def test_resume_skips_success_and_retries_timeout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            destination = root/'saved'
            destination.mkdir()
            cases = [dict(query_id=q, question=q+'?') for q in ['a', 'b', 'c']]
            state = dict(version=1, config={}, cases=cases, records=[], elapsed=0)
            args = SimpleNamespace(model='auto', timeout=30, verify_code=False)
            called = []
            def invoke(command, cwd, stdout, stderr, timeout):
                question = command[-1]
                called.append(question)
                stdout.write_text(json.dumps({'type':'assistant.message','data':{'content':'Answer','model':'model'}}))
                stderr.write_text('')
                return dict(status='timeout' if question == 'b?' and called.count('b?') == 1 else 'completed', exit_code=0)
            with patch('run_copilot.run_logged', side_effect=invoke), patch('builtins.print'):
                first = root/'first'; first.mkdir()
                with self.assertRaises(SystemExit):
                    run_cases(args, cases, 'fake', {}, None, first, first, destination, {}, state)
                state = load(destination/'checkpoint.json', {}, cases)
                second = root/'second'; second.mkdir()
                run_cases(args, cases, 'fake', {}, None, second, second, destination, {}, state)
            self.assertEqual(called, ['a?', 'b?', 'b?', 'c?'])
            state = load(destination/'checkpoint.json', {}, cases)
            self.assertEqual(len(state['records']), 3)
            self.assertTrue(all(completed(r, False) for r in state['records']))
            metrics = (destination/'metrics.md').read_text()
            self.assertIn('| Completed answers | 3 |', metrics)
            self.assertIn('| Runtime behavior | Not checked |', metrics)
            self.assertNotIn('do not establish runtime correctness', metrics)
            self.assertFalse((destination/'analysis.md').exists())
