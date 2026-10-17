"""Deterministic, section-aware normalization and word-level chunking."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, replace
from typing import Final, Literal, cast

from .passage_ids import PassageIdContext, SourceKind, make_passage_id
from .schemas import Passage

NORMALIZATION_VERSION: Final = "text-normalization-v1"
CHUNKING_VERSION: Final = "word-chunking-v1"
DEFAULT_CHUNK_SIZE_WORDS: Final = 200
DEFAULT_CHUNK_OVERLAP_WORDS: Final = 40
_WORD_PATTERN: Final = re.compile(r"\S+", re.UNICODE)
_FULL_TEXT_SOURCE_KIND: Final = "full_text"


class SourceFormatError(ValueError):
    """Raised when a source record violates the required QASPER shape."""


@dataclass(frozen=True, slots=True)
class ChunkingConfig:
    """Validated configuration for deterministic text normalization and chunking."""

    chunk_size_words: int = DEFAULT_CHUNK_SIZE_WORDS
    chunk_overlap_words: int = DEFAULT_CHUNK_OVERLAP_WORDS
    normalization_version: str = NORMALIZATION_VERSION
    chunking_version: str = CHUNKING_VERSION

    def __post_init__(self) -> None:
        """Reject ambiguous values instead of silently coercing them."""

        if type(self.chunk_size_words) is not int or self.chunk_size_words <= 0:
            raise TypeError("chunk_size_words must be a positive integer")
        if (
            type(self.chunk_overlap_words) is not int
            or self.chunk_overlap_words < 0
        ):
            raise TypeError("chunk_overlap_words must be a non-negative integer")
        if self.chunk_overlap_words >= self.chunk_size_words:
            raise ValueError(
                "chunk_overlap_words must be less than chunk_size_words"
            )
        for field_name in ("normalization_version", "chunking_version"):
            value = getattr(self, field_name)
            if type(value) is not str or not value or value != value.strip():
                raise ValueError(
                    f"{field_name} must be a non-empty string without edge whitespace"
                )


@dataclass(frozen=True, slots=True)
class SourceCoordinate:
    """Internal coordinate identifying one chunk within one source container."""

    paper_id: str
    source_kind: SourceKind
    section_index: int
    chunk_index: int


@dataclass(frozen=True, slots=True)
class NormalizationReport:
    """Counts of every conservative source-text transformation."""

    paragraphs_seen: int = 0
    paragraphs_emitted: int = 0
    blank_paragraphs_dropped: int = 0
    line_ending_replacements: int = 0
    outer_whitespace_trims: int = 0
    sections_seen: int = 0
    sections_emitted: int = 0
    blank_sections_dropped: int = 0
    null_sections_dropped: int = 0
    empty_sections_dropped: int = 0
    invalid_papers_dropped: int = 0

    def merged(self, other: NormalizationReport) -> NormalizationReport:
        """Return the element-wise sum of two reports."""

        fields = (
            "paragraphs_seen",
            "paragraphs_emitted",
            "blank_paragraphs_dropped",
            "line_ending_replacements",
            "outer_whitespace_trims",
            "sections_seen",
            "sections_emitted",
            "blank_sections_dropped",
            "null_sections_dropped",
            "empty_sections_dropped",
            "invalid_papers_dropped",
        )
        return replace(
            self,
            **{field: getattr(self, field) + getattr(other, field) for field in fields},
        )


@dataclass(frozen=True, slots=True)
class BuiltPassage:
    """A public passage plus private source coordinates used for validation."""

    passage: Passage
    coordinate: SourceCoordinate
    paragraph_indices: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class PassageBuildResult:
    """Passages and normalization observations for one or more source records."""

    passages: tuple[BuiltPassage, ...]
    report: NormalizationReport


def _require_clean_string(value: object, *, field_name: str) -> str:
    """Require a non-empty string without changing its value."""

    if type(value) is not str:
        raise SourceFormatError(f"{field_name} must be a string")
    if value == "":
        raise SourceFormatError(f"{field_name} must not be empty")
    if value.strip() == "":
        raise SourceFormatError(f"{field_name} must not be blank")
    if value != value.strip():
        raise SourceFormatError(f"{field_name} must not have edge whitespace")
    return value


def _normalize_text(value: object, *, field_name: str) -> tuple[str, int, bool]:
    """Normalize line endings and outer whitespace while preserving inner bytes."""

    if type(value) is not str:
        raise SourceFormatError(f"{field_name} must be a string")
    crlf_count = value.count("\r\n")
    lone_cr_count = value.count("\r") - crlf_count
    normalized = value.replace("\r\n", "\n").replace("\r", "\n")
    trimmed = normalized.strip()
    return trimmed, crlf_count + lone_cr_count, trimmed != normalized


def _validate_context(context: PassageIdContext, config: ChunkingConfig) -> None:
    """Require the ID context and chunking configuration to describe one run."""

    if not isinstance(context, PassageIdContext):
        raise TypeError("context must be a PassageIdContext")
    if context.chunk_size_words != config.chunk_size_words:
        raise ValueError("context chunk_size_words does not match chunking config")
    if context.chunk_overlap_words != config.chunk_overlap_words:
        raise ValueError("context chunk_overlap_words does not match chunking config")
    if context.normalization_version != config.normalization_version:
        raise ValueError(
            "context normalization_version does not match chunking config"
        )
    if context.chunking_version != config.chunking_version:
        raise ValueError("context chunking_version does not match chunking config")


def _paragraph_ranges(
    paragraphs: Sequence[str],
) -> tuple[str, tuple[tuple[int, int, int], ...]]:
    """Join normalized paragraphs and retain their source-index character ranges."""

    pieces: list[str] = []
    ranges: list[tuple[int, int, int]] = []
    offset = 0
    for paragraph_index, paragraph in enumerate(paragraphs):
        if pieces:
            pieces.append("\n\n")
            offset += 2
        start = offset
        pieces.append(paragraph)
        offset += len(paragraph)
        ranges.append((start, offset, paragraph_index))
    return "".join(pieces), tuple(ranges)


def _paragraph_indices_for_span(
    ranges: Sequence[tuple[int, int, int]],
    start: int,
    end: int,
) -> tuple[int, ...]:
    """Return original paragraph indices touched by a chunk character span."""

    return tuple(
        paragraph_index
        for paragraph_start, paragraph_end, paragraph_index in ranges
        if paragraph_start < end and paragraph_end > start
    )


def _build_container_passages(
    *,
    context: PassageIdContext,
    config: ChunkingConfig,
    title: str,
    section: str,
    paper_id: str,
    source_kind: SourceKind,
    section_index: int,
    normalized_paragraphs: Sequence[tuple[int, str]],
) -> tuple[BuiltPassage, ...]:
    """Chunk one already-normalized source container without crossing its boundary."""

    paragraphs = [value for _, value in normalized_paragraphs]
    original_indices = [index for index, _ in normalized_paragraphs]
    source_text, local_ranges = _paragraph_ranges(paragraphs)
    tokens = tuple(_WORD_PATTERN.finditer(source_text))
    if not tokens:
        return ()

    ranges = tuple(
        (start, end, original_indices[local_index])
        for start, end, local_index in local_ranges
    )
    step = config.chunk_size_words - config.chunk_overlap_words
    built: list[BuiltPassage] = []
    start_word = 0
    while start_word < len(tokens):
        end_word = min(start_word + config.chunk_size_words, len(tokens))
        start_char = tokens[start_word].start()
        end_char = tokens[end_word - 1].end()
        text = source_text[start_char:end_char]
        chunk_index = len(built)
        coordinate = SourceCoordinate(
            paper_id=paper_id,
            source_kind=source_kind,
            section_index=section_index,
            chunk_index=chunk_index,
        )
        passage = Passage(
            passage_id=make_passage_id(
                context=context,
                paper_id=paper_id,
                source_kind=source_kind,
                section_index=section_index,
                chunk_index=chunk_index,
            ),
            paper_id=paper_id,
            title=title,
            section=section,
            chunk_number=chunk_index,
            text=text,
            previous_passage_id=None,
            next_passage_id=None,
        )
        built.append(
            BuiltPassage(
                passage=passage,
                coordinate=coordinate,
                paragraph_indices=_paragraph_indices_for_span(
                    ranges, start_char, end_char
                ),
            )
        )
        if end_word == len(tokens):
            break
        start_word += step
    return tuple(built)


def chunk_source_container(
    *,
    context: PassageIdContext,
    config: ChunkingConfig,
    title: str,
    section: str,
    paper_id: str,
    source_kind: SourceKind,
    section_index: int,
    paragraphs: Sequence[object],
) -> tuple[tuple[BuiltPassage, ...], NormalizationReport]:
    """Normalize and chunk exactly one source container.

    The word rule is the count of Unicode-aware non-whitespace runs. Internal
    whitespace, punctuation, casing, and paragraph order are preserved.
    """

    _validate_context(context, config)
    paper_id = _require_clean_string(paper_id, field_name="paper_id")
    title = _require_clean_string(title, field_name="title")
    section = _require_clean_string(section, field_name="section")
    if type(section_index) is not int or section_index < 0:
        raise TypeError("section_index must be a non-negative integer")

    normalized: list[tuple[int, str]] = []
    report = NormalizationReport()
    for paragraph_index, paragraph in enumerate(paragraphs):
        value, line_ending_count, trimmed = _normalize_text(
            paragraph, field_name=f"paragraphs[{paragraph_index}]"
        )
        report = replace(
            report,
            paragraphs_seen=report.paragraphs_seen + 1,
            line_ending_replacements=(
                report.line_ending_replacements + line_ending_count
            ),
            outer_whitespace_trims=(
                report.outer_whitespace_trims + int(trimmed)
            ),
        )
        if not value:
            report = replace(
                report,
                blank_paragraphs_dropped=report.blank_paragraphs_dropped + 1,
            )
            continue
        normalized.append((paragraph_index, value))

    report = replace(report, paragraphs_emitted=len(normalized))
    built = _build_container_passages(
        context=context,
        config=config,
        title=title,
        section=section,
        paper_id=paper_id,
        source_kind=source_kind,
        section_index=section_index,
        normalized_paragraphs=normalized,
    )
    return built, report


def _section_parts(
    section_value: object,
    *,
    section_index: int,
) -> tuple[str | None, list[object]]:
    """Validate and extract one QASPER full-text section."""

    if not isinstance(section_value, Mapping):
        raise SourceFormatError(f"full_text[{section_index}] must be an object")
    if "section_name" not in section_value:
        raise SourceFormatError(
            f"full_text[{section_index}] is missing section_name"
        )
    if "paragraphs" not in section_value:
        raise SourceFormatError(f"full_text[{section_index}] is missing paragraphs")
    section_name = section_value["section_name"]
    if section_name is not None and type(section_name) is not str:
        raise SourceFormatError(
            f"full_text[{section_index}].section_name must be a string"
        )
    paragraphs = section_value["paragraphs"]
    if not isinstance(paragraphs, list):
        raise SourceFormatError(
            f"full_text[{section_index}].paragraphs must be a list"
        )
    return section_name, paragraphs


def build_passages_from_record(
    record: Mapping[str, object],
    *,
    context: PassageIdContext,
    config: ChunkingConfig,
) -> PassageBuildResult:
    """Build only full-text passages from one paper-level QASPER record.

    The function deliberately reads only ``id``, ``title`` and ``full_text``.
    It never reads questions, answers, evidence, or figure/table metadata.
    Empty paragraphs are dropped, while the original section index remains part
    of the ID coordinate so filtering cannot silently renumber later sections.
    """

    _validate_context(context, config)
    if not isinstance(record, Mapping):
        raise SourceFormatError("record must be an object")
    paper_id = _require_clean_string(record.get("id"), field_name="id")
    title_value = record.get("title")
    if type(title_value) is not str:
        raise SourceFormatError("title must be a string")
    title, title_line_endings, title_trimmed = _normalize_text(
        title_value, field_name="title"
    )
    if not title:
        report = NormalizationReport(
            invalid_papers_dropped=1,
            line_ending_replacements=title_line_endings,
            outer_whitespace_trims=int(title_trimmed),
        )
        return PassageBuildResult(passages=(), report=report)
    if "full_text" not in record:
        raise SourceFormatError("record is missing full_text")
    full_text = record["full_text"]
    if not isinstance(full_text, list):
        raise SourceFormatError("full_text must be a list")

    report = NormalizationReport(
        line_ending_replacements=title_line_endings,
        outer_whitespace_trims=int(title_trimmed),
    )
    built: list[BuiltPassage] = []
    for section_index, section_value in enumerate(full_text):
        section_name, paragraphs = _section_parts(
            section_value, section_index=section_index
        )
        report = replace(report, sections_seen=report.sections_seen + 1)
        if section_name is None:
            normalized_section = ""
            section_line_endings = 0
            section_trimmed = False
        else:
            normalized_section, section_line_endings, section_trimmed = _normalize_text(
                section_name, field_name=f"full_text[{section_index}].section_name"
            )
        report = replace(
            report,
            line_ending_replacements=(
                report.line_ending_replacements + section_line_endings
            ),
            outer_whitespace_trims=(
                report.outer_whitespace_trims + int(section_trimmed)
            ),
        )
        if not normalized_section:
            if section_name is None:
                report = replace(
                    report,
                    null_sections_dropped=report.null_sections_dropped + 1,
                )
            else:
                report = replace(
                    report,
                    blank_sections_dropped=report.blank_sections_dropped + 1,
                )
            continue
        container_passages, container_report = chunk_source_container(
            context=context,
            config=config,
            title=title,
            section=normalized_section,
            paper_id=paper_id,
            source_kind=cast(Literal["full_text"], _FULL_TEXT_SOURCE_KIND),
            section_index=section_index,
            paragraphs=paragraphs,
        )
        report = report.merged(container_report)
        if not container_passages:
            report = replace(
                report,
                empty_sections_dropped=report.empty_sections_dropped + 1,
            )
            continue
        report = replace(report, sections_emitted=report.sections_emitted + 1)
        built.extend(container_passages)

    return PassageBuildResult(
        passages=_fill_adjacency(tuple(built)),
        report=report,
    )


def build_passages_from_records(
    records: Iterable[Mapping[str, object]],
    *,
    context: PassageIdContext,
    config: ChunkingConfig,
) -> PassageBuildResult:
    """Build deterministic passages from records ordered by paper ID."""

    _validate_context(context, config)
    results: list[PassageBuildResult] = []
    seen_paper_ids: set[str] = set()
    for record in records:
        if not isinstance(record, Mapping):
            raise SourceFormatError("record must be an object")
        paper_id = _require_clean_string(record.get("id"), field_name="id")
        if paper_id in seen_paper_ids:
            raise SourceFormatError(f"duplicate paper ID: {paper_id!r}")
        seen_paper_ids.add(paper_id)
        results.append(
            build_passages_from_record(record, context=context, config=config)
        )

    passages = tuple(
        item
        for result in sorted(
            results,
            key=lambda result: (
                result.passages[0].coordinate.paper_id
                if result.passages
                else "",
            ),
        )
        for item in result.passages
    )
    report = NormalizationReport()
    for result in results:
        report = report.merged(result.report)
    return PassageBuildResult(passages=_fill_adjacency(passages), report=report)


def _fill_adjacency(passages: tuple[BuiltPassage, ...]) -> tuple[BuiltPassage, ...]:
    """Fill direct links independently inside each private source coordinate."""

    groups: dict[tuple[str, SourceKind, int], list[BuiltPassage]] = {}
    for item in passages:
        key = (
            item.coordinate.paper_id,
            item.coordinate.source_kind,
            item.coordinate.section_index,
        )
        groups.setdefault(key, []).append(item)

    linked: list[BuiltPassage] = []
    for item in passages:
        key = (
            item.coordinate.paper_id,
            item.coordinate.source_kind,
            item.coordinate.section_index,
        )
        sequence = sorted(groups[key], key=lambda value: value.coordinate.chunk_index)
        position = item.coordinate.chunk_index
        previous_id = (
            sequence[position - 1].passage.passage_id if position > 0 else None
        )
        next_id = (
            sequence[position + 1].passage.passage_id
            if position + 1 < len(sequence)
            else None
        )
        linked.append(
            replace(
                item,
                passage=item.passage.model_copy(
                    update={
                        "previous_passage_id": previous_id,
                        "next_passage_id": next_id,
                    }
                ),
            )
        )
    return tuple(linked)


def validate_built_passages(passages: Sequence[BuiltPassage]) -> None:
    """Validate IDs, chunk continuity, non-empty text, and mutual links."""

    ids: set[str] = set()
    groups: dict[tuple[str, SourceKind, int], list[BuiltPassage]] = {}
    for item in passages:
        passage = item.passage
        if passage.passage_id in ids:
            raise ValueError(f"duplicate passage ID: {passage.passage_id}")
        ids.add(passage.passage_id)
        if not passage.text.strip():
            raise ValueError(f"empty passage text: {passage.passage_id}")
        key = (
            item.coordinate.paper_id,
            item.coordinate.source_kind,
            item.coordinate.section_index,
        )
        groups.setdefault(key, []).append(item)

    for key, sequence in groups.items():
        ordered = sorted(sequence, key=lambda value: value.passage.chunk_number)
        expected = list(range(len(ordered)))
        actual = [item.passage.chunk_number for item in ordered]
        if actual != expected:
            raise ValueError(f"non-contiguous chunk numbers for source container {key}")
        for position, item in enumerate(ordered):
            previous_id = (
                ordered[position - 1].passage.passage_id if position > 0 else None
            )
            next_id = (
                ordered[position + 1].passage.passage_id
                if position + 1 < len(ordered)
                else None
            )
            if item.passage.previous_passage_id != previous_id:
                raise ValueError(
                    f"invalid previous link for {item.passage.passage_id}"
                )
            if item.passage.next_passage_id != next_id:
                raise ValueError(f"invalid next link for {item.passage.passage_id}")
            if previous_id is not None and previous_id not in ids:
                raise ValueError(f"dangling previous link for {item.passage.passage_id}")
            if next_id is not None and next_id not in ids:
                raise ValueError(f"dangling next link for {item.passage.passage_id}")


__all__ = [
    "CHUNKING_VERSION",
    "DEFAULT_CHUNK_OVERLAP_WORDS",
    "DEFAULT_CHUNK_SIZE_WORDS",
    "NORMALIZATION_VERSION",
    "BuiltPassage",
    "ChunkingConfig",
    "NormalizationReport",
    "PassageBuildResult",
    "SourceCoordinate",
    "SourceFormatError",
    "build_passages_from_record",
    "build_passages_from_records",
    "chunk_source_container",
    "validate_built_passages",
]
