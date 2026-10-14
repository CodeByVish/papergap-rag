"""Deterministic, content-independent identifiers for QASPER passages."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Final, Literal

PASSAGE_ID_SCHEME_VERSION: Final = "qasper-passage-v1"
QASPER_DATASET_ID: Final = "allenai/qasper"
SourceKind = Literal["full_text", "abstract", "figure_table"]

_COMMIT_SHA_RE: Final = re.compile(r"[0-9a-f]{40}")
_SOURCE_KINDS: Final = frozenset({"full_text", "abstract", "figure_table"})


def _validate_string(field_name: str, value: object) -> str:
    """Validate an identity string without silently changing it."""

    if type(value) is not str:
        raise TypeError(f"{field_name} must be a string")
    if value == "":
        raise ValueError(f"{field_name} must not be empty")
    if value != value.strip():
        raise ValueError(
            f"{field_name} must not have leading or trailing whitespace"
        )
    return value


def _validate_integer(field_name: str, value: object, *, minimum: int) -> int:
    """Validate a strict integer and its lower bound."""

    if type(value) is not int:
        raise TypeError(f"{field_name} must be an integer")
    if value < minimum:
        raise ValueError(f"{field_name} must be at least {minimum}")
    return value


@dataclass(frozen=True, slots=True)
class PassageIdContext:
    """Immutable dataset and transformation context used by passage IDs."""

    dataset_id: str
    resolved_revision: str
    local_parser_version: int
    normalization_version: str
    chunking_version: str
    chunk_size_words: int
    chunk_overlap_words: int

    def __post_init__(self) -> None:
        """Reject ambiguous or non-canonical identity context values."""

        _validate_string("dataset_id", self.dataset_id)
        resolved_revision = _validate_string(
            "resolved_revision", self.resolved_revision
        )
        if _COMMIT_SHA_RE.fullmatch(resolved_revision) is None:
            raise ValueError(
                "resolved_revision must be a full lowercase 40-character commit SHA"
            )
        _validate_integer(
            "local_parser_version", self.local_parser_version, minimum=1
        )
        _validate_string("normalization_version", self.normalization_version)
        _validate_string("chunking_version", self.chunking_version)
        chunk_size_words = _validate_integer(
            "chunk_size_words", self.chunk_size_words, minimum=1
        )
        chunk_overlap_words = _validate_integer(
            "chunk_overlap_words", self.chunk_overlap_words, minimum=0
        )
        if chunk_overlap_words >= chunk_size_words:
            raise ValueError(
                "chunk_overlap_words must be less than chunk_size_words"
            )


def _canonical_payload(
    *,
    context: PassageIdContext,
    paper_id: str,
    source_kind: str,
    section_index: int,
    chunk_index: int,
) -> dict[str, object]:
    """Build the fixed payload whose canonical bytes define the ID."""

    paper_id = _validate_string("paper_id", paper_id)
    source_kind = _validate_string("source_kind", source_kind)
    if source_kind not in _SOURCE_KINDS:
        allowed = ", ".join(sorted(_SOURCE_KINDS))
        raise ValueError(f"source_kind must be one of: {allowed}")
    section_index = _validate_integer("section_index", section_index, minimum=0)
    chunk_index = _validate_integer("chunk_index", chunk_index, minimum=0)

    return {
        "scheme": PASSAGE_ID_SCHEME_VERSION,
        "dataset": {
            "dataset_id": context.dataset_id,
            "resolved_revision": context.resolved_revision,
            "local_parser_version": context.local_parser_version,
        },
        "transform": {
            "normalization_version": context.normalization_version,
            "chunking_version": context.chunking_version,
            "chunk_size_words": context.chunk_size_words,
            "chunk_overlap_words": context.chunk_overlap_words,
        },
        "coordinate": {
            "paper_id": paper_id,
            "source_kind": source_kind,
            "section_index": section_index,
            "chunk_index": chunk_index,
        },
    }


def make_passage_id(
    *,
    context: PassageIdContext,
    paper_id: str,
    source_kind: SourceKind,
    section_index: int,
    chunk_index: int,
) -> str:
    """Return a stable opaque ID for one source coordinate and configuration."""

    if not isinstance(context, PassageIdContext):
        raise TypeError("context must be a PassageIdContext")

    payload = _canonical_payload(
        context=context,
        paper_id=paper_id,
        source_kind=source_kind,
        section_index=section_index,
        chunk_index=chunk_index,
    )
    canonical_json = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    digest = hashlib.sha256(canonical_json.encode("utf-8")).hexdigest()
    return f"{PASSAGE_ID_SCHEME_VERSION}-{digest}"


__all__ = [
    "PASSAGE_ID_SCHEME_VERSION",
    "QASPER_DATASET_ID",
    "PassageIdContext",
    "SourceKind",
    "make_passage_id",
]
