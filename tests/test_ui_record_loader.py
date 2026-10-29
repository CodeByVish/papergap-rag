import json
import pytest
from src.ui.record_loader import load_records


def test_formats_preserve_payload(tmp_path):
    rows = [{'question': 'Synthetic question', 'nested': {'original': [1, 2]}}]
    for name, text in [('states.json', json.dumps(rows)), ('states.jsonl', json.dumps(rows[0]) + '\n')]:
        p = tmp_path / name
        p.write_text(text)
        assert load_records(p) == rows


@pytest.mark.parametrize('text', ['[]', '{}', '[{"result": {}}]', 'broken'])
def test_invalid(tmp_path, text):
    p = tmp_path / 'states.json'
    p.write_text(text)
    with pytest.raises(ValueError):
        load_records(p)


def test_invalid_line_and_missing(tmp_path):
    p = tmp_path / 'states.jsonl'
    p.write_text('{"question":"q"}\nbroken')
    with pytest.raises(ValueError, match='line 2'):
        load_records(p)
    with pytest.raises(ValueError, match='Cannot read'):
        load_records(tmp_path / 'missing')


def test_non_utf8_file_is_actionable(tmp_path):
    p = tmp_path / 'invalid.json'
    p.write_bytes(b'\xff\xfe')
    with pytest.raises(ValueError, match='Invalid JSON'):
        load_records(p)
