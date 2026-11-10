"""Tests for bounded repair and preservation of failed answers."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from compile_copilot import verify_and_repair, compile_answer, tool_urls

ORIGINAL = 'Example [docs](https://example.com/api)\n```csharp\nbroken\n```'
FIXED = ORIGINAL.replace('broken', 'fixed')

class RepairTests(unittest.TestCase):
    def check_flow(self, states, candidates, budget=2):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        calls = []
        def repair(prompt, folder):
            calls.append(prompt)
            return {'execution_status': 'completed', 'recorded_answer_markdown': candidates[len(calls)-1]}
        with patch('compile_copilot.compile_answer', side_effect=[{'status': s} for s in states]):
            answer, record = verify_and_repair('question', ORIGINAL, root, '26.10.0', 'net10.0', 120, budget, repair)
        return answer, record, calls

    def test_repair_passes(self):
        answer, record, calls = self.check_flow(['failed', 'passed'], [FIXED])
        self.assertEqual(answer, FIXED)
        self.assertTrue(record['accepted'])
        self.assertEqual(len(calls), 1)

    def test_exhausted_retains_original(self):
        answer, record, calls = self.check_flow(['failed', 'failed', 'failed'], [FIXED, FIXED+'\nChanged'])
        self.assertEqual(answer, ORIGINAL)
        self.assertFalse(record['accepted'])
        self.assertEqual(len(calls), 2)

    def test_unchanged_stops(self):
        _, record, calls = self.check_flow(['failed'], [ORIGINAL])
        self.assertEqual(record['attempts'][-1]['disposition'], 'unchanged_answer')
        self.assertEqual(len(calls), 1)

    def test_citations_and_removed_code_rejected(self):
        _, record, calls = self.check_flow(['failed'], [FIXED+' https://invented.example/api', 'https://example.com/api'])
        self.assertEqual([a['disposition'] for a in record['attempts']], ['initial', 'citation_rejected', 'code_removed'])
        self.assertEqual(len(calls), 2)

    def test_infrastructure_and_no_code_do_not_repair(self):
        for state in ['unavailable', 'timeout', 'no_code', 'passed']:
            _, record, calls = self.check_flow([state], [])
            self.assertEqual(calls, [])
            self.assertEqual(record['status'], state)

    def test_zero_budget(self):
        _, record, calls = self.check_flow(['failed'], [], budget=0)
        self.assertEqual(calls, [])
        self.assertEqual(record['status'], 'failed')

    def test_no_code(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(compile_answer('Explanation only', Path(folder))['status'], 'no_code')

    def test_only_words_net_urls(self):
        events = []
        for server in ['words-net', 'shell']:
            events += [{'type': 'tool.execution_start', 'data': {'toolCallId': server, 'mcpServerName': server}},
                       {'type': 'tool.execution_complete', 'data': {'toolCallId': server, 'success': True, 'result': 'https://example.com/'+server}}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'events.jsonl'
            path.write_text('\n'.join(json.dumps(e) for e in events), encoding='utf-8')
            self.assertEqual(tool_urls(path), {'https://example.com/words-net'})

if __name__ == '__main__':
    unittest.main()

class SdkPolicyTests(unittest.TestCase):
    def test_build_inherits_exact_repository_policy(self):
        from compile_copilot import SDK_POLICY
        def build(command, cwd, stdout, stderr, timeout):
            self.assertEqual((cwd.parent/'global.json').read_bytes(), SDK_POLICY.read_bytes())
            stdout.write_text('Build succeeded.')
            stderr.write_text('')
            return {'status': 'completed', 'exit_code': 0}
        with tempfile.TemporaryDirectory() as folder, \
             patch('compile_copilot.shutil.which', return_value='/fake/dotnet'), \
             patch('compile_copilot.run_logged', side_effect=build):
            result = compile_answer(FIXED, Path(folder))
            self.assertEqual(result['status'], 'passed')

    def test_missing_policy_prevents_build(self):
        with tempfile.TemporaryDirectory() as folder, \
             patch('compile_copilot.SDK_POLICY', Path(folder)/'missing.json'), \
             patch('compile_copilot.run_logged') as build:
            result = compile_answer(FIXED, Path(folder)/'build')
            self.assertEqual(result['status'], 'unavailable')
            self.assertIn('global.json', result['reason'])
            build.assert_not_called()

    def test_unavailable_sdk_does_not_trigger_repair(self):
        def build(command, cwd, stdout, stderr, timeout):
            stdout.write_text('')
            stderr.write_text('A compatible .NET SDK was not found.')
            return {'status': 'failed', 'exit_code': 145}
        with tempfile.TemporaryDirectory() as folder, \
             patch('compile_copilot.shutil.which', return_value='/fake/dotnet'), \
             patch('compile_copilot.run_logged', side_effect=build), \
             patch('builtins.print'):
            def repair(*args):
                self.fail('SDK selection failure must not request model repair')
            _, result = verify_and_repair('Question', FIXED, Path(folder), '26.10.0', 'net10.0', 120, 2, repair)
            self.assertEqual(result['status'], 'unavailable')
