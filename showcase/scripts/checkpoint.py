"""Small, atomic resume state; no transcripts, diagnostics, or build artifacts."""
import json
import os
from pathlib import Path
import tempfile


def compact(value):
    if isinstance(value, list):
        return [compact(item) for item in value]
    if isinstance(value, dict):
        omitted = {'tools', 'warnings', 'discovered_agent_ids', 'diagnostics', 'session_name'}
        return {key: compact({k: v for k, v in item.items() if k != 'recorded_answer_markdown'}
                             if key == 'repair' and isinstance(item, dict) else item)
                for key, item in value.items() if key not in omitted}
    return value


def atomic_write(path, text):
    path = Path(path)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix='.'+path.name, delete=False) as stream:
            name = stream.name
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def save(path, state):
    atomic_write(path, json.dumps(compact(state), ensure_ascii=False, indent=2)+'\n')


def load(path, config, cases):
    state = json.loads(path.read_text(encoding='utf-8'))
    if state.get('version') != 1 or state.get('config') != config or state.get('cases') != cases:
        raise ValueError('Run configuration or selected questions changed; use the original options or a new run name.')
    records = state['records']
    ids = [r['query_id'] for r in records]
    if len(ids) != len(set(ids)) or not set(ids) <= {c['query_id'] for c in cases}:
        raise ValueError('Invalid checkpoint records.')
    return state


def completed(record, verify):
    return record.get('status') == 'completed' and bool(record.get('recorded_answer_markdown')) and (
        not verify or record.get('compilation_status') in {'passed', 'no_code'})
