import json
import tempfile
import unittest
from pathlib import Path
from copilot_results import extract, report


class EventExtractionTests(unittest.TestCase):
    def parse(self, events):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'events.jsonl'
            p.write_text('\n'.join(json.dumps(e) for e in events), encoding='utf-8')
            return extract(p)

    def test_final_answer_and_shell_failure(self):
        result = self.parse([
            {'type': 'assistant.message', 'data': {'content': 'Progress'}},
            {'type': 'tool.execution_start', 'data': {'toolCallId': '1', 'toolName': 'bash'}},
            {'type': 'tool.execution_complete', 'data': {'toolCallId': '1', 'success': True, 'shellExecution': {'exitCode': 1}}},
            {'type': 'assistant.reasoning_delta', 'data': {'deltaContent': 'Do not include'}},
            {'type': 'assistant.message', 'data': {'content': 'Final\n```csharp\ncode\n```', 'model': 'model-a'}},
        ])
        self.assertEqual(result['recorded_answer_markdown'], 'Final\n```csharp\ncode\n```')
        self.assertTrue(result['tools'][0]['failed'])
        self.assertEqual(result['resolved_models'], ['model-a'])

    def test_no_final_after_tool_is_not_answer(self):
        result = self.parse([
            {'type': 'assistant.message', 'data': {'content': 'I will check.'}},
            {'type': 'tool.execution_start', 'data': {'toolCallId': '1', 'toolName': 'words-net-query_docs', 'mcpServerName': 'words-net'}},
        ])
        self.assertEqual(result['recorded_answer_markdown'], '')
        self.assertFalse(result['tools'][0]['completed'])

    def test_report_prefers_verified_answer_and_labels_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            records = [{
                'query_id': 'case', 'question': 'Question', 'status': 'completed',
                'recorded_answer_markdown': 'Original', 'verified_answer_markdown': 'Repaired',
                'compilation_status': 'passed', 'answer_source': '/saved/answer.md',
                'verification': {'attempts': [{'repair': {'resolved_models': ['repair-model']}}]}}]
            report(root, records, 1, {}, 1)
            rendered = (root/'showcase.md').read_text(encoding='utf-8')
            self.assertIn('Answer loaded from a saved answer.', rendered)
            self.assertIn('repair-model', rendered)
            self.assertIn('Repaired', rendered)
            self.assertNotIn('Original', rendered)

    def test_actual_model_from_auto(self):
        result = self.parse([{'type': 'session.auto_mode_resolved', 'data': {'chosenModel': 'actual-model'}}])
        self.assertEqual(result['resolved_models'], ['actual-model'])


if __name__ == '__main__':
    unittest.main()
