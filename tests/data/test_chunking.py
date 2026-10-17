from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import pytest

from src.data.chunking import (
    CHUNKING_VERSION,
    NORMALIZATION_VERSION,
    ChunkingConfig,
    SourceFormatError,
    build_passages_from_record,
    build_passages_from_records,
    chunk_source_container,
    validate_built_passages,
)
from src.data.passage_ids import PassageIdContext


def _context(**changes: object) -> PassageIdContext:
    values: dict[str, object] = {
        "dataset_id": "allenai/qasper",
        "resolved_revision": "a" * 40,
        "local_parser_version": 1,
        "normalization_version": NORMALIZATION_VERSION,
        "chunking_version": CHUNKING_VERSION,
        "chunk_size_words": 4,
        "chunk_overlap_words": 1,
    }
    values.update(changes)
    return PassageIdContext(**values)  # type: ignore[arg-type]


def _config(**changes: object) -> ChunkingConfig:
    values: dict[str, object] = {
        "chunk_size_words": 4,
        "chunk_overlap_words": 1,
        "normalization_version": NORMALIZATION_VERSION,
        "chunking_version": CHUNKING_VERSION,
    }
    values.update(changes)
    return ChunkingConfig(**values)  # type: ignore[arg-type]


def _record(
    paper_id: str = "paper-a",
    *,
    sections: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    return {
        "id": paper_id,
        "title": "A synthetic paper",
        "abstract": "must not enter a passage",
        "full_text": sections
        if sections is not None
        else [
            {
                "section_name": "Section A",
                "paragraphs": ["one two three four five six"],
            }
        ],
        "qas": [{"question": "must not enter a passage"}],
        "figures_and_tables": [{"caption": "must not enter a passage"}],
    }


def test_word_rule_preserves_internal_text_and_records_conservative_changes() -> None:
    passages, report = chunk_source_container(
        context=_context(),
        config=_config(),
        title="A synthetic paper",
        section="Section A",
        paper_id="paper-a",
        source_kind="full_text",
        section_index=0,
        paragraphs=["  one  two\r\nthree  ", "", "four"],
    )

    assert [item.passage.text for item in passages] == [
        "one  two\nthree\n\nfour"
    ]
    assert [len(item.passage.text.split()) for item in passages] == [4]
    assert report.paragraphs_seen == 3
    assert report.paragraphs_emitted == 2
    assert report.blank_paragraphs_dropped == 1
    assert report.line_ending_replacements == 1
    assert report.outer_whitespace_trims == 1
    assert passages[0].paragraph_indices == (0, 2)


def test_chunking_uses_word_overlap_without_crossing_source_container() -> None:
    result = build_passages_from_record(
        _record(
            sections=[
                {
                    "section_name": "Repeated",
                    "paragraphs": ["one two three four five six seven"],
                },
                {
                    "section_name": "Repeated",
                    "paragraphs": ["eight nine ten eleven"],
                },
            ]
        ),
        context=_context(),
        config=_config(),
    )

    assert [item.passage.chunk_number for item in result.passages] == [0, 1, 0]
    assert result.passages[0].passage.text == "one two three four"
    assert result.passages[1].passage.text == "four five six seven"
    assert result.passages[2].passage.text == "eight nine ten eleven"
    assert result.passages[0].passage.next_passage_id == result.passages[1].passage.passage_id
    assert result.passages[1].passage.next_passage_id is None
    assert result.passages[1].coordinate.section_index == 0
    assert result.passages[2].coordinate.section_index == 1
    validate_built_passages(result.passages)


def test_fixture_preserves_paper_and_repeated_section_boundaries() -> None:
    fixture_path = Path(__file__).parents[1] / "fixtures" / "chunking_records.json"
    records = json.loads(fixture_path.read_text(encoding="utf-8"))
    result = build_passages_from_records(
        records,
        context=_context(chunk_size_words=3, chunk_overlap_words=1),
        config=_config(chunk_size_words=3, chunk_overlap_words=1),
    )

    assert len(result.passages) == 3
    assert [item.coordinate.paper_id for item in result.passages] == [
        "fixture-paper-a",
        "fixture-paper-a",
        "fixture-paper-b",
    ]
    assert [item.coordinate.section_index for item in result.passages] == [0, 1, 0]
    assert all(
        "must not enter a passage" not in item.passage.text
        for item in result.passages
    )
    validate_built_passages(result.passages)


def test_first_middle_last_and_single_chunk_adjacency() -> None:
    multi_result = build_passages_from_record(
        _record(
            sections=[
                {
                    "section_name": "Long",
                    "paragraphs": [
                        "one two three four five six seven eight nine ten"
                    ],
                }
            ]
        ),
        context=_context(chunk_size_words=3, chunk_overlap_words=1),
        config=_config(chunk_size_words=3, chunk_overlap_words=1),
    )
    multi = multi_result.passages
    assert len(multi) == 5
    assert multi[0].passage.previous_passage_id is None
    assert multi[0].passage.next_passage_id == multi[1].passage.passage_id
    assert multi[2].passage.previous_passage_id == multi[1].passage.passage_id
    assert multi[2].passage.next_passage_id == multi[3].passage.passage_id
    assert multi[-1].passage.previous_passage_id == multi[-2].passage.passage_id
    assert multi[-1].passage.next_passage_id is None

    single, _ = chunk_source_container(
        context=_context(),
        config=_config(),
        title="A synthetic paper",
        section="Single",
        paper_id="paper-single",
        source_kind="full_text",
        section_index=0,
        paragraphs=["one two"],
    )
    assert len(single) == 1
    assert single[0].passage.previous_passage_id is None
    assert single[0].passage.next_passage_id is None


def test_empty_section_keeps_original_section_index() -> None:
    result = build_passages_from_record(
        _record(
            sections=[
                {"section_name": "Empty", "paragraphs": ["", "  "]},
                {"section_name": "Kept", "paragraphs": ["one two"]},
            ]
        ),
        context=_context(),
        config=_config(),
    )

    assert len(result.passages) == 1
    assert result.passages[0].coordinate.section_index == 1
    assert result.report.empty_sections_dropped == 1


def test_blank_section_name_is_dropped_without_guessing_a_replacement() -> None:
    result = build_passages_from_record(
        _record(
            sections=[
                {"section_name": "", "paragraphs": ["one two"]},
                {"section_name": "Kept", "paragraphs": ["three four"]},
            ]
        ),
        context=_context(),
        config=_config(),
    )

    assert len(result.passages) == 1
    assert result.passages[0].passage.section == "Kept"
    assert result.report.blank_sections_dropped == 1


def test_null_section_name_is_dropped_without_guessing_a_replacement() -> None:
    result = build_passages_from_record(
        _record(
            sections=[
                {"section_name": None, "paragraphs": ["one two"]},
                {"section_name": "Kept", "paragraphs": ["three four"]},
            ]
        ),
        context=_context(),
        config=_config(),
    )

    assert len(result.passages) == 1
    assert result.passages[0].passage.section == "Kept"
    assert result.report.null_sections_dropped == 1


def test_builder_does_not_read_supervision_or_figure_fields() -> None:
    record = _record()
    result = build_passages_from_record(
        record,
        context=_context(),
        config=_config(),
    )

    text = " ".join(item.passage.text for item in result.passages)
    assert "must not enter a passage" not in text


def test_building_same_records_twice_is_byte_stable() -> None:
    records = [_record("paper-b"), _record("paper-a")]
    first = build_passages_from_records(records, context=_context(), config=_config())
    second = build_passages_from_records(records, context=_context(), config=_config())

    first_json = [item.passage.model_dump(mode="json") for item in first.passages]
    second_json = [item.passage.model_dump(mode="json") for item in second.passages]
    assert first_json == second_json
    assert [item.coordinate.paper_id for item in first.passages] == [
        "paper-a",
        "paper-a",
        "paper-b",
        "paper-b",
    ]


def test_duplicate_paper_ids_and_malformed_sections_fail_closed() -> None:
    with pytest.raises(SourceFormatError, match="duplicate paper ID"):
        build_passages_from_records(
            [_record(), _record()], context=_context(), config=_config()
        )

    with pytest.raises(SourceFormatError, match="missing paragraphs"):
        build_passages_from_record(
            _record(sections=[{"section_name": "Section A"}]),
            context=_context(),
            config=_config(),
        )


def test_invalid_context_or_config_is_rejected() -> None:
    with pytest.raises(ValueError, match="chunk_size_words"):
        build_passages_from_record(
            _record(),
            context=_context(chunk_size_words=5),
            config=_config(),
        )

    with pytest.raises(ValueError, match="chunk_overlap_words"):
        ChunkingConfig(chunk_size_words=4, chunk_overlap_words=4)


def test_validate_built_passages_detects_broken_adjacency() -> None:
    result = build_passages_from_record(
        _record(), context=_context(), config=_config()
    )
    broken = tuple(
        replace(
            item,
            passage=item.passage.model_copy(update={"next_passage_id": "bad"}),
        )
        for item in result.passages
    )
    with pytest.raises(ValueError, match="invalid next link"):
        validate_built_passages(broken)


def test_validate_built_passages_detects_duplicate_ids_and_empty_text() -> None:
    result = build_passages_from_record(
        _record(), context=_context(), config=_config()
    )
    with pytest.raises(ValueError, match="duplicate passage ID"):
        validate_built_passages(result.passages + (result.passages[0],))

    empty = tuple(
        replace(
            item,
            passage=item.passage.model_copy(update={"text": "   "}),
        )
        for item in result.passages
    )
    with pytest.raises(ValueError, match="empty passage text"):
        validate_built_passages(empty)
