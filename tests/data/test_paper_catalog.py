"""Exercise catalog eligibility, source order, missing metadata and validation.

Synthetic files deliberately shuffle passages and repeat section labels so the
tests can distinguish source ordering from incidental corpus row order.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

from src.data.build_paper_catalog import build_paper_catalog


def _write(path: Path, records: list[dict]) -> Path:
    """Write synthetic JSONL input and return its path.

    Args:
        path: Temporary test file destination.
        records: JSON objects to serialize in supplied order.

    Returns:
        The populated file path.
    """
    path.write_text("".join(json.dumps(row) + "\n" for row in records), encoding="utf-8")
    return path


@pytest.fixture
def inputs(tmp_path: Path) -> tuple[Path, Path]:
    """Provide source metadata and an intentionally unordered corpus.

    Args:
        tmp_path: Isolated pytest directory.

    Returns:
        Paper and passage input paths, including a paper with no passages.
    """
    papers = _write(tmp_path / "tmp_papers.jsonl", [
        {"id": "a", "title": " Title ", "authors": [" Author ", None],
         "full_text": [{"section_name": name} for name in
                       [" Intro ", "Unused", "Results", "Intro"]]},
        {"id": "b", "full_text": [{"section_name": None}]},
        {"id": "empty", "full_text": [{"section_name": "Intro"}]},
    ])
    passages = _write(tmp_path / "tmp_passages.jsonl", [
        {"passage_id": "p1", "paper_id": "a", "section": "Results", "text": "result"},
        {"passage_id": "p2", "paper_id": "a", "section": "Intro", "text": "first"},
        {"passage_id": "p3", "paper_id": "a", "section": "Intro", "text": "second"},
        {"passage_id": "p4", "paper_id": "b", "section": None, "text": "body"},
    ])
    return papers, passages


def test_catalog_source_order_and_missing_metadata(inputs: tuple[Path, Path]) -> None:
    """Check exact counts, name aggregation and eligibility with sparse metadata.

    Args:
        inputs: Synthetic source and corpus paths.
    """
    papers, passages = inputs
    catalog = build_paper_catalog(papers=papers, passages=passages)
    assert catalog == {
        "schema_version": "v0-proposed",
        "passages_file": passages.as_posix(),
        "papers": [
            {"paper_id": "a", "title": "Title", "authors": ["Author", None],
             "passage_count": 3, "sections": [
                 {"name": "Intro", "passage_count": 2},
                 {"name": "Results", "passage_count": 1}]},
            {"paper_id": "b", "title": None, "authors": [],
             "passage_count": 1, "sections": [{"name": None, "passage_count": 1}]},
        ],
    }


@pytest.mark.parametrize(("target", "replacement", "message"), [
    ("papers", {"id": "a"}, "duplicate paper ID"),
    ("passages", {"passage_id": "p1", "paper_id": "a"}, "duplicate passage ID"),
    ("passages", {"passage_id": "new", "paper_id": "unknown"}, "unknown passage paper"),
    ("passages", {"passage_id": "new", "paper_id": "a", "text": " "}, "no retrievable text"),
    ("passages", {"passage_id": "new", "paper_id": "a", "text": "x", "section": "Other"},
     "unknown passage section"),
    ("passages", {"passage_id": "new", "paper_id": "a", "text": "x", "section": " Intro "},
     "not normalized"),
])
def test_catalog_rejects_inconsistent_inputs(
    inputs: tuple[Path, Path], target: str, replacement: dict, message: str,
) -> None:
    """Reject broken links and counts instead of silently omitting bad records.

    Args:
        inputs: Synthetic source and corpus paths.
        target: Input file receiving the invalid record.
        replacement: Row appended to that input.
        message: Expected validation error substring.
    """
    papers, passages = inputs
    path = papers if target == "papers" else passages
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(replacement) + "\n")
    with pytest.raises(ValueError, match=message):
        build_paper_catalog(papers=papers, passages=passages)


def test_empty_corpus(inputs: tuple[Path, Path]) -> None:
    """Return an empty selectable list when the corpus contains no passages.

    Args:
        inputs: Synthetic source and corpus paths.
    """
    papers, passages = inputs
    passages.write_text("", encoding="utf-8")
    assert build_paper_catalog(papers=papers, passages=passages)["papers"] == []


def test_cli_preserves_existing_output(inputs: tuple[Path, Path], tmp_path: Path) -> None:
    """Verify the maintained CLI writes JSON once and refuses replacement.

    Args:
        inputs: Synthetic source and corpus paths.
        tmp_path: Isolated output directory.
    """
    papers, passages = inputs
    output = tmp_path / "tmp_catalog.json"
    command = [sys.executable, "-m", "scripts.build_paper_catalog", "--papers", str(papers),
               "--passages", str(passages), "--output", str(output)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    original = output.read_bytes()
    assert json.loads(original) == build_paper_catalog(papers=papers, passages=passages)
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert "output already exists" in result.stderr
    assert output.read_bytes() == original
