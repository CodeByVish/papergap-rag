"""Tests for the published corpus size gate and independent recount."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from scripts import check_corpus


def _write_fixture(tmp_path: Path) -> tuple[Path, Path]:
    corpus = tmp_path / "passages.jsonl"
    record = {
        "passage_id": "synthetic-1",
        "paper_id": "paper-1",
        "title": "Synthetic paper",
        "section": "Methods",
        "chunk_number": 0,
        "text": "Two distinct words",
        "previous_passage_id": None,
        "next_passage_id": None,
    }
    payload = (json.dumps(record, sort_keys=True) + "\n").encode("utf-8")
    corpus.write_bytes(payload)
    manifest = tmp_path / "passages.manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "output": {
                    "file": corpus.name,
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "indexed_paper_count": 1,
                    "passage_count": 1,
                    "unique_passage_count": 1,
                    "source_word_count": 3,
                    "passage_word_count": 3,
                    "passage_word_type_count": 3,
                    "rubric_minimum_met": True,
                }
            }
        ),
        encoding="utf-8",
    )
    return corpus, manifest


def test_recount_rejects_an_undersized_corpus(tmp_path: Path) -> None:
    corpus, manifest = _write_fixture(tmp_path)
    with pytest.raises(ValueError, match="below rubric minimum"):
        check_corpus.check_corpus(corpus, manifest)


def test_recount_detects_modified_bytes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    corpus, manifest = _write_fixture(tmp_path)
    monkeypatch.setattr(check_corpus, "MIN_PASSAGES", 1)
    monkeypatch.setattr(check_corpus, "MIN_WORDS", 1)
    assert check_corpus.check_corpus(corpus, manifest)["passage_count"] == 1
    corpus.write_bytes(corpus.read_bytes().replace(b"Two", b"One"))
    with pytest.raises(ValueError, match="sha256 mismatch"):
        check_corpus.check_corpus(corpus, manifest)
