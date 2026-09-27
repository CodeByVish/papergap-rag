"""Tests for deterministic passage identity generation."""

from __future__ import annotations

import hashlib
import inspect
import json

import pytest
from pydantic import ValidationError

from src.data.passage_ids import (
    PASSAGE_ID_SCHEME_VERSION,
    PassageIdContext,
    make_passage_id,
)
from src.data.schemas import Passage

REVISION = "a" * 40


def _context(**updates: object) -> PassageIdContext:
    """Return a valid synthetic context without using QASPER text."""

    data: dict[str, object] = {
        "dataset_id": "allenai/qasper",
        "resolved_revision": REVISION,
        "local_parser_version": 1,
        "normalization_version": "normalization-v1",
        "chunking_version": "chunking-v1",
        "chunk_size_words": 200,
        "chunk_overlap_words": 40,
    }
    data.update(updates)
    return PassageIdContext(**data)


def _base_id(**updates: object) -> str:
    """Return an ID for a stable synthetic coordinate."""

    data: dict[str, object] = {
        "context": _context(),
        "paper_id": "paper-a",
        "source_kind": "full_text",
        "section_index": 2,
        "chunk_index": 3,
    }
    data.update(updates)
    return make_passage_id(**data)


def test_golden_vector_and_canonical_payload_are_exact() -> None:
    context = _context()
    payload = {
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
            "paper_id": "paper-a",
            "source_kind": "full_text",
            "section_index": 2,
            "chunk_index": 3,
        },
    }
    canonical_json = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    assert canonical_json == (
        '{"coordinate":{"chunk_index":3,"paper_id":"paper-a",'
        '"section_index":2,"source_kind":"full_text"},'
        '"dataset":{"dataset_id":"allenai/qasper",'
        '"local_parser_version":1,"resolved_revision":"'
        + REVISION
        + '"},"scheme":"qasper-passage-v1",'
        '"transform":{"chunk_overlap_words":40,"chunk_size_words":200,'
        '"chunking_version":"chunking-v1",'
        '"normalization_version":"normalization-v1"}}'
    )
    assert _base_id() == (
        "qasper-passage-v1-"
        "fe1214d2ab869911e267500cd9b8903dc8e3d4d1e66bde218d0bcc938da8c6ee"
    )
    assert hashlib.sha256(canonical_json.encode("utf-8")).hexdigest() == (
        _base_id().removeprefix(f"{PASSAGE_ID_SCHEME_VERSION}-")
    )


def test_repeated_calls_have_the_same_format_and_value() -> None:
    passage_id = _base_id()

    assert passage_id == _base_id()
    assert passage_id.startswith(f"{PASSAGE_ID_SCHEME_VERSION}-")
    assert len(passage_id) == len(PASSAGE_ID_SCHEME_VERSION) + 1 + 64
    assert all(character in "0123456789abcdef" for character in passage_id[-64:])


@pytest.mark.parametrize(
    ("change", "expected_argument"),
    [
        ("dataset_id", {"context": _context(dataset_id="other/dataset")}),
        ("resolved_revision", {"context": _context(resolved_revision="b" * 40)}),
        (
            "local_parser_version",
            {"context": _context(local_parser_version=2)},
        ),
        (
            "normalization_version",
            {"context": _context(normalization_version="normalization-v2")},
        ),
        (
            "chunking_version",
            {"context": _context(chunking_version="chunking-v2")},
        ),
        (
            "chunk_size_words",
            {"context": _context(chunk_size_words=250, chunk_overlap_words=40)},
        ),
        (
            "chunk_overlap_words",
            {"context": _context(chunk_size_words=200, chunk_overlap_words=50)},
        ),
        ("paper_id", {"paper_id": "paper-b"}),
        ("source_kind", {"source_kind": "abstract"}),
        ("section_index", {"section_index": 3}),
        ("chunk_index", {"chunk_index": 4}),
    ],
)
def test_each_identity_input_changes_the_id(
    change: str,
    expected_argument: dict[str, object],
) -> None:
    del change

    assert _base_id(**expected_argument) != _base_id()


def test_titles_sections_and_text_are_not_function_inputs() -> None:
    parameter_names = list(inspect.signature(make_passage_id).parameters)

    assert parameter_names == [
        "context",
        "paper_id",
        "source_kind",
        "section_index",
        "chunk_index",
    ]
    assert not {"title", "section", "text"}.intersection(parameter_names)


def test_utf8_canonical_encoding_does_not_escape_unicode() -> None:
    paper_id = "paper-\u6d4b\u8bd5"
    passage_id = _base_id(paper_id=paper_id)
    payload = {
        "scheme": PASSAGE_ID_SCHEME_VERSION,
        "dataset": {
            "dataset_id": "allenai/qasper",
            "resolved_revision": REVISION,
            "local_parser_version": 1,
        },
        "transform": {
            "normalization_version": "normalization-v1",
            "chunking_version": "chunking-v1",
            "chunk_size_words": 200,
            "chunk_overlap_words": 40,
        },
        "coordinate": {
            "paper_id": paper_id,
            "source_kind": "full_text",
            "section_index": 2,
            "chunk_index": 3,
        },
    }
    canonical_json = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )

    assert "\\u6d4b" not in canonical_json
    expected_digest = hashlib.sha256(canonical_json.encode("utf-8")).hexdigest()
    assert passage_id == f"{PASSAGE_ID_SCHEME_VERSION}-{expected_digest}"


def test_ten_thousand_synthetic_coordinates_have_unique_ids() -> None:
    passage_ids = {
        _base_id(chunk_index=chunk_index) for chunk_index in range(10_000)
    }

    assert len(passage_ids) == 10_000


def test_generated_ids_are_accepted_as_passage_and_neighbor_ids() -> None:
    first_id = _base_id(chunk_index=0)
    second_id = _base_id(chunk_index=1)

    passage = Passage.model_validate(
        {
            "passage_id": first_id,
            "paper_id": "paper-a",
            "title": "Synthetic paper title",
            "section": "Synthetic section",
            "chunk_number": 0,
            "text": "Synthetic passage text.",
            "previous_passage_id": None,
            "next_passage_id": second_id,
        }
    )

    assert passage.passage_id == first_id
    assert passage.next_passage_id == second_id


def test_chunk_index_matches_passage_chunk_number() -> None:
    chunk_index = 3
    passage_id = _base_id(chunk_index=chunk_index)

    passage = Passage.model_validate(
        {
            "passage_id": passage_id,
            "paper_id": "paper-a",
            "title": "Synthetic paper title",
            "section": "Synthetic section",
            "chunk_number": chunk_index,
            "text": "Synthetic passage text.",
            "previous_passage_id": None,
            "next_passage_id": None,
        }
    )

    assert passage.chunk_number == chunk_index


def test_missing_context_is_rejected() -> None:
    with pytest.raises(TypeError, match="context must be a PassageIdContext"):
        make_passage_id(
            context=None,
            paper_id="paper-a",
            source_kind="full_text",
            section_index=0,
            chunk_index=0,
        )


@pytest.mark.parametrize(
    "field_name",
    [
        "dataset_id",
        "resolved_revision",
        "local_parser_version",
        "normalization_version",
        "chunking_version",
        "chunk_size_words",
        "chunk_overlap_words",
    ],
)
def test_missing_context_fields_are_rejected(field_name: str) -> None:
    with pytest.raises(TypeError, match=field_name):
        PassageIdContext(**_context_data_without(field_name))


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("dataset_id", 1),
        ("resolved_revision", False),
        ("normalization_version", ["normalization-v1"]),
        ("chunking_version", None),
        ("local_parser_version", True),
        ("chunk_size_words", 200.0),
        ("chunk_overlap_words", False),
    ],
)
def test_context_rejects_wrong_types(field_name: str, value: object) -> None:
    with pytest.raises((TypeError, ValueError), match=field_name):
        PassageIdContext(**{field_name: value, **_context_data_without(field_name)})


def _context_data_without(field_name: str) -> dict[str, object]:
    data: dict[str, object] = {
        "dataset_id": "allenai/qasper",
        "resolved_revision": REVISION,
        "local_parser_version": 1,
        "normalization_version": "normalization-v1",
        "chunking_version": "chunking-v1",
        "chunk_size_words": 200,
        "chunk_overlap_words": 40,
    }
    del data[field_name]
    return data


@pytest.mark.parametrize(
    "field_name",
    ["dataset_id", "resolved_revision", "normalization_version", "chunking_version"],
)
@pytest.mark.parametrize("value", ["", " ", " leading", "trailing "])
def test_context_rejects_empty_or_edge_whitespace_strings(
    field_name: str,
    value: str,
) -> None:
    with pytest.raises(ValueError, match=field_name):
        PassageIdContext(**{field_name: value, **_context_data_without(field_name)})


@pytest.mark.parametrize("revision", ["A" * 40, "a" * 39, "a" * 41, "g" * 40])
def test_context_rejects_invalid_revisions(revision: str) -> None:
    with pytest.raises(ValueError, match="resolved_revision"):
        _context(resolved_revision=revision)


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("local_parser_version", 0),
        ("local_parser_version", -1),
        ("chunk_size_words", 0),
        ("chunk_size_words", -1),
        ("chunk_overlap_words", -1),
    ],
)
def test_context_rejects_invalid_integer_ranges(
    field_name: str,
    value: int,
) -> None:
    with pytest.raises(ValueError, match=field_name):
        _context(**{field_name: value})


@pytest.mark.parametrize(
    ("chunk_size_words", "chunk_overlap_words"),
    [(200, 200), (200, 201)],
)
def test_context_rejects_overlap_at_or_above_chunk_size(
    chunk_size_words: int,
    chunk_overlap_words: int,
) -> None:
    with pytest.raises(ValueError, match="chunk_overlap_words"):
        _context(
            chunk_size_words=chunk_size_words,
            chunk_overlap_words=chunk_overlap_words,
        )


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("section_index", True),
        ("section_index", 1.0),
        ("section_index", -1),
        ("chunk_index", False),
        ("chunk_index", 1.0),
        ("chunk_index", -1),
    ],
)
def test_coordinates_require_non_negative_strict_integers(
    field_name: str,
    value: object,
) -> None:
    with pytest.raises((TypeError, ValueError), match=field_name):
        _base_id(**{field_name: value})


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("paper_id", 1),
        ("paper_id", ""),
        ("paper_id", " "),
        ("paper_id", " leading"),
        ("source_kind", "unknown"),
        ("source_kind", ""),
        ("source_kind", " trailing"),
    ],
)
def test_coordinates_reject_invalid_strings(field_name: str, value: object) -> None:
    with pytest.raises((TypeError, ValueError), match=field_name):
        _base_id(**{field_name: value})


def test_context_is_frozen() -> None:
    context = _context()

    with pytest.raises(AttributeError):
        context.chunk_size_words = 250  # type: ignore[misc]


def test_validation_errors_are_raised_before_passage_use() -> None:
    with pytest.raises(ValidationError):
        Passage.model_validate(
            {
                "passage_id": _base_id(),
                "paper_id": "paper-a",
                "title": "Synthetic paper title",
                "section": "Synthetic section",
                "chunk_number": 0,
                "text": "Synthetic passage text.",
                "previous_passage_id": _base_id(chunk_index=1),
                "next_passage_id": _base_id(chunk_index=1),
            }
        )
