#!/usr/bin/env python3
"""Read bounded slices of saved MCP JSON, JSONL, concatenated JSON, or text."""
import argparse
import json
from pathlib import Path
import sys


def decode_records(text):
    decoder = json.JSONDecoder()
    records = []
    offset = 0
    while offset < len(text):
        while offset < len(text) and text[offset].isspace():
            offset += 1
        if offset == len(text):
            break
        try:
            value, offset = decoder.raw_decode(text, offset)
        except json.JSONDecodeError:
            # Never silently discard a non-JSON tail or a mixed-format response.
            return [text]
        records.append(value)
    return records


def render(records, record=None, result=None):
    if record is None:
        summary = []
        for i, value in enumerate(records):
            entry = {'record': i, 'type': type(value).__name__}
            if isinstance(value, dict):
                entry['keys'] = list(value)
                if isinstance(value.get('results'), list):
                    entry['results'] = [
                        dict(index=j, **{k: r[k] for k in ('title', 'canonical_url', 'member_fqn') if k in r})
                        if isinstance(r, dict) else {'index': j, 'type': type(r).__name__}
                        for j, r in enumerate(value['results'])]
            summary.append(entry)
        return json.dumps(summary, ensure_ascii=False, indent=2)
    if record < 0 or record >= len(records):
        raise ValueError('Record index out of range.')
    value = records[record]
    if result is not None:
        if not isinstance(value, dict) or not isinstance(value.get('results'), list):
            raise ValueError('Selected record has no results array.')
        if result < 0 or result >= len(value['results']):
            raise ValueError('Result index out of range.')
        value = value['results'][result]
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2)


def page(text, offset, limit):
    raw = text.encode('utf-8')
    if offset < 0 or offset > len(raw):
        raise ValueError('Offset outside rendered content.')
    end = min(offset + limit, len(raw))
    # Keep a page boundary between UTF-8 code points.
    while end < len(raw) and raw[end] & 0xC0 == 0x80:
        end -= 1
    content = raw[offset:end].decode('utf-8')
    return f'bytes {offset}:{end}/{len(raw)}; next_offset={end if end < len(raw) else "END"}\n' + content


def main():
    # Saved MCP documentation is UTF-8; never fail on a console in another codepage.
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('path', type=Path)
    p.add_argument('--record', type=int)
    p.add_argument('--result', type=int)
    p.add_argument('--offset', type=int, default=0, help='Byte offset in rendered selection; use next_offset')
    p.add_argument('--limit', type=int, default=4000, help='Maximum output bytes excluding short header (4–8000)')
    a = p.parse_args()
    if not 4 <= a.limit <= 8000 or (a.result is not None and a.record is None):
        p.error('Use --limit 4–8000; --result requires --record.')
    try:
        text = a.path.read_text(encoding='utf-8')
        print(page(render(decode_records(text), a.record, a.result), a.offset, a.limit))
    except (OSError, ValueError, UnicodeError) as error:
        p.exit(1, str(error)+'\n')


if __name__ == '__main__':
    main()
