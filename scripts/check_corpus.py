"""Independently verify a generated passage corpus and its size manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from src.data.schemas import Passage

MIN_PASSAGES = 10_000
MIN_WORDS = 100_000


def check_corpus(corpus: Path, manifest_path: Path) -> dict[str, int | str | bool]:
    """Recount actual JSONL records and reject mismatched or undersized output."""

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = manifest["output"]
    if corpus.name != expected["file"]:
        raise ValueError("corpus filename differs from manifest")
    digest = hashlib.sha256()
    ids: set[str] = set()
    papers: set[str] = set()
    word_types: set[str] = set()
    passage_count = passage_word_count = 0
    with corpus.open("rb") as handle:
        for line_number, line in enumerate(handle, start=1):
            digest.update(line)
            if not line.strip():
                raise ValueError(f"blank corpus line: {line_number}")
            passage = Passage.model_validate_json(line)
            if passage.passage_id in ids:
                raise ValueError(f"duplicate passage ID at line {line_number}")
            ids.add(passage.passage_id)
            papers.add(passage.paper_id)
            tokens = passage.text.split()
            passage_word_count += len(tokens)
            word_types.update(token.casefold() for token in tokens)
            passage_count += 1
    actual = {
        "sha256": digest.hexdigest(),
        "indexed_paper_count": len(papers),
        "passage_count": passage_count,
        "unique_passage_count": len(ids),
        "passage_word_count": passage_word_count,
        "passage_word_type_count": len(word_types),
    }
    for key, value in actual.items():
        if expected.get(key) != value:
            raise ValueError(f"manifest {key} mismatch: {expected.get(key)!r} != {value!r}")
    source_words = expected.get("source_word_count")
    if type(source_words) is not int or source_words < MIN_WORDS:
        raise ValueError("source word count is below rubric minimum")
    if passage_count < MIN_PASSAGES or passage_word_count < MIN_WORDS:
        raise ValueError("corpus is below rubric minimum")
    if expected.get("rubric_minimum_met") is not True:
        raise ValueError("manifest does not mark rubric minimum met")
    return {**actual, "source_word_count": source_words, "rubric_minimum_met": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = check_corpus(args.corpus, args.manifest)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
