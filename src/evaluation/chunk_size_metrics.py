"""Calculate evidence coverage with reusable source mapping helpers.

The imported helpers remain available here for existing experiment callers.
"""

from __future__ import annotations

from typing import Any

from src.data.map_evidence import (
    locate_annotations,
    normalized_paragraph,
    passage_spans,
    source_paragraphs,
    uncovered_spans,
)

__all__ = [
    'evaluate_question',
    'locate_annotations',
    'normalized_paragraph',
    'passage_spans',
    'source_paragraphs',
    'uncovered_spans',
]


def evaluate_question(
    annotations: list[dict[str, Any]],
    paragraphs: dict[str, dict[str, Any]],
    retrieved: list[dict[str, Any]],
) -> dict[str, Any]:
    """Compute both evidence decisions and the repeated-overlap word total.

    Retrieved records carry text and paragraph spans. Every annotation must have
    fully located, nonempty evidence before any evidence can contribute a hit.
    Complete evidence still requires covering only one full annotation's set.

    Raises:
        ValueError: No annotations exist or any annotation is unusable. Such
            questions must be excluded before sampling, rather than scored.
    """
    if not annotations or not all(annotation["usable"] for annotation in annotations):
        raise ValueError("all answer annotations must have fully located text evidence")
    locations = {loc for annotation in annotations for loc in annotation["locations"]}
    missing = {}
    for location in sorted(locations):
        spans = [
            item["spans"][location] for item in retrieved if location in item["spans"]
        ]
        missing[location] = uncovered_spans(paragraphs[location]["text"], spans)
    complete = [
        annotation["annotation_id"]
        for annotation in annotations
        if annotation["usable"]
        and all(not missing[loc] for loc in annotation["locations"])
    ]
    return {
        "evidence_hit_at_5": any(not spans for spans in missing.values()),
        "complete_evidence_at_5": bool(complete),
        "total_retrieved_words": sum(len(item["text"].split()) for item in retrieved),
        "fully_covered_annotations": complete,
        "missing_by_annotation": {
            annotation["annotation_id"]: {
                "usable": annotation["usable"],
                "unresolved_evidence": annotation["unresolved"],
                "paragraphs": {
                    loc: missing[loc] for loc in annotation["locations"] if missing[loc]
                },
            }
            for annotation in annotations
        },
    }
