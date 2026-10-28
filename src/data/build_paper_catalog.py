"""Build UI paper metadata from the exact passage corpus used for retrieval.

The catalog contains metadata and counts only. It never loads QA annotations or
infers unavailable authors, and retains source section order rather than corpus
row order. Repeated section labels share one entry because filters use names.
"""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Iterator
from pathlib import Path
from typing import Any


def _records(path: Path) -> Iterator[dict[str, Any]]:
    """Read JSON objects incrementally, rejecting malformed or blank rows.

    Args:
        path: UTF-8 JSONL input file.

    Yields:
        One decoded object per source line.

    Raises:
        ValueError: A row is invalid JSON.
        TypeError: A row is not an object.
    """
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{number}: invalid JSON") from error
            if not isinstance(record, dict):
                raise TypeError(f"{path}:{number}: expected an object")
            yield record


def _optional_string(value: Any) -> str | None:
    """Normalize display text using the passage builder's text rules.

    Args:
        value: A source string or missing/null value.

    Returns:
        Trimmed text with LF line endings, or null for absent/blank strings.

    Raises:
        TypeError: A non-null value is not a string.
    """
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("metadata string must be a string or null")
    return value.replace("\r\n", "\n").replace("\r", "\n").strip() or None


def _identifier(record: dict[str, Any], field: str) -> str:
    """Require an identifier without silently modifying its value.

    Args:
        record: Input JSON object.
        field: Identifier key to validate.

    Returns:
        The original nonempty identifier.

    Raises:
        ValueError: The identifier is missing, blank, or has edge whitespace.
    """
    value = record.get(field)
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError(f"invalid {field}: {value!r}")
    return value


def build_paper_catalog(*, papers: Path, passages: Path) -> dict[str, Any]:
    """Validate source links and summarize only papers with retrievable text.

    Args:
        papers: Paper-only QASPER export with unique IDs and ordered full_text.
        passages: Exact JSONL corpus selected by the retrieval consumer.

    Returns:
        A v0-proposed catalog, in paper export order. The passages_file path is
        recorded as supplied, with forward slashes, relative to the caller's
        working directory when a relative path was supplied.

    Raises:
        TypeError: Metadata types are invalid or a JSONL row is not an object.
        ValueError: IDs repeat, a passage has no
            body, or its paper/normalized section is absent from the export.
    """
    metadata: dict[str, dict[str, Any]] = {}
    for paper in _records(papers):
        paper_id = _identifier(paper, "id")
        if paper_id in metadata:
            raise ValueError(f"duplicate paper ID: {paper_id}")
        authors = paper.get("authors")
        if authors is None:
            authors = []
        if not isinstance(authors, list):
            raise TypeError(f"authors must be an array: {paper_id}")
        sections = paper.get("full_text", [])
        if not isinstance(sections, list) or any(
            not isinstance(section, dict) for section in sections
        ):
            raise TypeError(f"full_text must be an array of objects: {paper_id}")
        metadata[paper_id] = {
            "paper_id": paper_id,
            "title": _optional_string(paper.get("title")),
            "authors": [_optional_string(author) for author in authors],
            "section_names": list(dict.fromkeys(
                _optional_string(section.get("section_name")) for section in sections
            )),
        }

    counts: dict[str, Counter[str | None]] = {}
    seen_passages: set[str] = set()
    for passage in _records(passages):
        passage_id = _identifier(passage, "passage_id")
        if passage_id in seen_passages:
            raise ValueError(f"duplicate passage ID: {passage_id}")
        seen_passages.add(passage_id)
        paper_id = _identifier(passage, "paper_id")
        if paper_id not in metadata:
            raise ValueError(f"unknown passage paper ID: {paper_id}")
        if _optional_string(passage.get("text")) is None:
            raise ValueError(f"passage has no retrievable text: {passage_id}")
        name = _optional_string(passage.get("section"))
        if passage.get("section") != name:
            raise ValueError(f"passage section is not normalized: {passage_id}")
        if name not in metadata[paper_id]["section_names"]:
            raise ValueError(f"unknown passage section: {paper_id}: {name!r}")
        counts.setdefault(paper_id, Counter())[name] += 1

    entries = []
    for paper_id, paper in metadata.items():
        if paper_id not in counts:
            continue
        section_counts = counts[paper_id]
        entries.append({
            "paper_id": paper_id,
            "title": paper["title"],
            "authors": paper["authors"],
            "passage_count": sum(section_counts.values()),
            "sections": [
                {"name": name, "passage_count": section_counts[name]}
                for name in paper["section_names"] if name in section_counts
            ],
        })
    return {
        "schema_version": "v0-proposed",
        "passages_file": passages.as_posix(),
        "papers": entries,
    }
