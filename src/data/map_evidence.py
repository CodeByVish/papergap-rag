"""Map QASPER evidence and passage windows to original source paragraphs.

These helpers share the chunk-size experiment's strict whole-paragraph matching
and original-character offsets without changing the public Passage schema.
"""

from __future__ import annotations

import re
from typing import Any

from src.data.chunking import BuiltPassage, ChunkingConfig


def normalized_paragraph(text: str) -> tuple[str, list[int]]:
    """Normalize a paragraph while preserving offsets into its original text.

    Returns normalized text and a boundary map one element longer than the
    normalized string. CRLF pairs consume two original characters.
    """
    chars: list[str] = []
    boundaries = [0]
    position = 0
    while position < len(text):
        char = text[position]
        position += 1
        if char == "\r":
            if position < len(text) and text[position] == "\n":
                position += 1
            char = "\n"
        chars.append(char)
        boundaries.append(position)
    joined = "".join(chars)
    left = len(joined) - len(joined.lstrip())
    right = len(joined.rstrip())
    if left >= right:
        return "", [len(text)]
    return joined[left:right], boundaries[left : right + 1]


def source_paragraphs(
    paper: dict[str, Any],
    *,
    with_offsets: bool = False,
) -> dict[str, dict[str, Any]]:
    """Index original full-text paragraphs using stable zero-based coordinates.

    Empty or unnamed sections are excluded consistently with the chunker.
    Original paragraph text is retained for reports and evidence matching.
    Character maps are allocated only when with_offsets is requested for one
    paper's chunk mapping, rather than retaining a map for the entire corpus.
    """
    result = {}
    for section_index, section in enumerate(paper["full_text"]):
        if not section["section_name"] or not section["section_name"].strip():
            continue
        for paragraph_index, text in enumerate(section["paragraphs"]):
            normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
            if normalized:
                location = f"{paper['id']}:{section_index}:{paragraph_index}"
                result[location] = {
                    "location": location,
                    "paper_id": paper["id"],
                    "section_index": section_index,
                    "paragraph_index": paragraph_index,
                    "text": text,
                    "normalized": normalized,
                }
                if with_offsets:
                    result[location]["boundaries"] = normalized_paragraph(text)[1]
    return result


def passage_spans(
    paper: dict[str, Any],
    built: tuple[BuiltPassage, ...],
    config: ChunkingConfig,
) -> dict[str, dict[str, tuple[int, int]]]:
    """Recover each chunk's exact original paragraph spans from word positions.

    Repeated text cannot confuse this mapping: offsets follow the same word
    windows as the chunker, including normalization and removed paragraphs.
    """
    paragraphs = source_paragraphs(paper, with_offsets=True)
    containers: dict[int, list[dict[str, Any]]] = {}
    for paragraph in paragraphs.values():
        containers.setdefault(paragraph["section_index"], []).append(paragraph)
    sections = {}
    for index, items in containers.items():
        offset = 0
        ranges = []
        for item in items:
            end = offset + len(item["normalized"])
            ranges.append((offset, end, item))
            offset = end + 2
        text = "\n\n".join(item["normalized"] for item in items)
        sections[index] = (text, list(re.finditer(r"\S+", text)), ranges)
    result = {}
    for item in built:
        text, words, ranges = sections[item.coordinate.section_index]
        start_word = item.coordinate.chunk_index * (
            config.chunk_size_words - config.chunk_overlap_words
        )
        end_word = min(start_word + config.chunk_size_words, len(words))
        start, end = words[start_word].start(), words[end_word - 1].end()
        if text[start:end] != item.passage.text:
            raise ValueError("source span reconstruction differs from chunk text")
        spans = {}
        for p_start, p_end, paragraph in ranges:
            if p_start < end and p_end > start:
                boundaries = paragraph["boundaries"]
                spans[paragraph["location"]] = (
                    boundaries[max(start, p_start) - p_start],
                    boundaries[min(end, p_end) - p_start],
                )
        result[item.passage.passage_id] = spans
    return result


def locate_annotations(
    question: dict[str, Any],
    paragraphs: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Locate every evidence item of each answer without guessing ambiguous text.

    An annotation is usable only if its nonempty text evidence set maps in full
    to unique paragraphs. Float markers, missing text and duplicates are reported
    as unresolved; an empty evidence set can never count as complete.
    """
    by_text: dict[str, list[str]] = {}
    for location, paragraph in paragraphs.items():
        by_text.setdefault(paragraph["normalized"], []).append(location)
    result = []
    for index, annotation in enumerate(question["answers"]):
        answer = annotation["answer"]
        locations = []
        unresolved = []
        evidence = answer.get("evidence", [])
        for text in evidence:
            normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
            matches = by_text.get(normalized, [])
            if not normalized or text.startswith("FLOAT SELECTED") or len(matches) != 1:
                unresolved.append(text)
            elif matches[0] not in locations:
                locations.append(matches[0])
        result.append(
            {
                "annotation_id": str(annotation.get("annotation_id", index)),
                "answer": answer,
                "locations": locations,
                "unresolved": unresolved,
                "usable": bool(locations) and not unresolved,
            }
        )
    return result


def uncovered_spans(text: str, spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Find non-whitespace gaps left by the union of retrieved source spans.

    Whitespace alone does not make an evidence paragraph incomplete. This allows
    adjacent word windows to cover a paragraph even with zero overlap.
    """
    cursor = 0
    gaps = []
    for start, end in sorted(spans):
        if start > cursor and text[cursor:start].strip():
            gaps.append((cursor, start))
        cursor = max(cursor, end)
    if text[cursor:].strip():
        gaps.append((cursor, len(text)))
    return gaps
