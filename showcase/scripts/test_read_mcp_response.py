import json
import unittest
from read_mcp_response import decode_records, render, page


class ResponseReaderTests(unittest.TestCase):
    def test_multiple_records(self):
        for separator in ('\n\n', '\n', ''):
            text = '{"a":1}' + separator + '{"results":[{"title":"Native feature","canonical_url":"https://example.test","excerpt":"full example"}]}'
            records = decode_records(text)
            self.assertEqual(len(records), 2)
            self.assertIn('Native feature', render(records))
            self.assertIn('full example', render(records, 1, 0))

    def test_plain_and_mixed_text_are_preserved(self):
        for text in ('plain text', '{"a":1}\nnon-json tail'):
            self.assertEqual(render(decode_records(text), 0), text)

    def test_pages_reassemble_unicode_without_loss(self):
        original = 'α🙂你好' * 2000
        offset = 0
        parts = []
        while offset < len(original.encode()):
            header, content = page(original, offset, 4000).split('\n', 1)
            self.assertLessEqual(len(content.encode()), 4000)
            self.assertTrue(content)
            parts.append(content)
            offset += len(content.encode())
        self.assertEqual(''.join(parts), original)

    def test_invalid_selection(self):
        with self.assertRaises(ValueError):
            render([{}], 0, 0)
        with self.assertRaises(ValueError):
            render([{}], -1)


if __name__ == '__main__':
    unittest.main()
