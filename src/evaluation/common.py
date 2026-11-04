"""Small, strict local-file helpers for P6 offline evaluation."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path


def read_jsonl(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    rows = []
    for number, line in enumerate(Path(path).read_text().splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line, object_pairs_hook=unique)
        if not isinstance(row, dict):
            raise TypeError(f"{path}:{number}: expected an object")
        rows.append(row)
    if not rows:
        raise ValueError(f"{path}: no records")
    return rows


def index_rows(rows, key="question_id"):
    result = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value.strip() or value in result:
            raise ValueError(f"Missing/duplicate {key}: {value!r}")
        result[value] = row
    return result


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")


def write_jsonl(path, rows):
    Path(path).write_text("".join(json.dumps(r, allow_nan=False) + "\n" for r in rows))


def write_csv(path, rows):
    rows = list(rows)
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with Path(path).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def mean(values):
    values = [v for v in values if finite(v)]
    return sum(values) / len(values) if values else None
