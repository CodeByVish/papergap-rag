"""Load local P5-exported inputs; never treat answer captures as inputs."""
import json
from pathlib import Path


def load_records(path):
    file = Path(path)
    try:
        text = file.read_text(encoding='utf-8')
        if file.suffix.lower() == '.jsonl':
            rows = []
            for line_number, line in enumerate(text.splitlines(), 1):
                if line.strip():
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        raise ValueError(f'Invalid JSONL at line {line_number}.') from None
        else:
            rows = json.loads(text)
    except OSError:
        raise ValueError('Cannot read P5_RECORDS_PATH. Check the local file.') from None
    except (json.JSONDecodeError, UnicodeError):
        raise ValueError('Invalid JSON record file.') from None
    if not isinstance(rows, list) or not rows:
        raise ValueError('Expected a nonempty JSON array or JSONL file of exported states.')
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict) or not row or 'result' in row:
            raise ValueError(f'Invalid exported state at record {index}; answer captures are not inputs.')
    return rows


def record_label(record, index):
    return f"{index + 1}: {str(record.get('question', record.get('request_id', 'Exported state')))[:120]}"
