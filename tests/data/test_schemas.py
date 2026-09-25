"""Tests for the proposed passage schema."""

from __future__ import annotations

import json

import pytest
from pydantic import ValidationError

from src.data.schemas import PASSAGE_SCHEMA_VERSION, Passage


def _passage_data(**updates: object) -> dict[str, object]:
    """Return synthetic passage data without copying QASPER text."""

    data: dict[str, object] = {
        "passage_id": "paper-a-passage-01",
        "paper_id": "paper-a",
        "title": "Synthetic paper title",
        "section": "Synthetic section",
        "chunk_number": 0,
        "text": "Synthetic passage text.",
        "previous_passage_id": None,
        "next_passage_id": "paper-a-passage-02",
    }
    data.update(updates)
    return data


def test_complete_record_is_valid_and_schema_version_is_proposed() -> None:
    passage = Passage.model_validate(_passage_data())

    assert PASSAGE_SCHEMA_VERSION == "v0-proposed"
    assert passage.passage_id == "paper-a-passage-01"
    assert passage.chunk_number == 0
    assert passage.next_passage_id == "paper-a-passage-02"


def test_zero_is_an_accepted_first_chunk_number() -> None:
    passage = Passage.model_validate(_passage_data(chunk_number=0))

    assert passage.chunk_number == 0


@pytest.mark.parametrize(
    ("previous_passage_id", "next_passage_id"),
    [
        (None, "paper-a-passage-02"),
        ("paper-a-passage-00", None),
        ("paper-a-passage-00", "paper-a-passage-02"),
        (None, None),
    ],
)
def test_all_sequence_boundary_neighbor_combinations_are_valid(
    previous_passage_id: str | None,
    next_passage_id: str | None,
) -> None:
    passage = Passage.model_validate(
        _passage_data(
            previous_passage_id=previous_passage_id,
            next_passage_id=next_passage_id,
        )
    )

    assert passage.previous_passage_id == previous_passage_id
    assert passage.next_passage_id == next_passage_id


@pytest.mark.parametrize(
    (
        "passage_id",
        "chunk_number",
        "previous_passage_id",
        "next_passage_id",
    ),
    [
        ("paper-a-passage-01", 0, None, "paper-a-passage-02"),
        (
            "paper-a-passage-01",
            1,
            "paper-a-passage-00",
            "paper-a-passage-02",
        ),
        ("paper-a-passage-02", 2, "paper-a-passage-01", None),
        ("paper-a-single-passage", 0, None, None),
    ],
)
def test_sequence_positions_and_boundaries_round_trip(
    passage_id: str,
    chunk_number: int,
    previous_passage_id: str | None,
    next_passage_id: str | None,
) -> None:
    original = Passage.model_validate(
        _passage_data(
            passage_id=passage_id,
            chunk_number=chunk_number,
            previous_passage_id=previous_passage_id,
            next_passage_id=next_passage_id,
        )
    )

    dumped = original.model_dump(mode="json")
    assert set(dumped) == {
        "passage_id",
        "paper_id",
        "title",
        "section",
        "chunk_number",
        "text",
        "previous_passage_id",
        "next_passage_id",
    }
    assert dumped["previous_passage_id"] == previous_passage_id
    assert dumped["next_passage_id"] == next_passage_id

    restored = Passage.model_validate_json(json.dumps(dumped))

    assert restored == original


def test_json_round_trip_preserves_values_and_fixed_keys() -> None:
    original = Passage.model_validate(_passage_data())
    dumped = original.model_dump(mode="json")
    restored = Passage.model_validate_json(json.dumps(dumped))

    assert dumped == {
        "passage_id": "paper-a-passage-01",
        "paper_id": "paper-a",
        "title": "Synthetic paper title",
        "section": "Synthetic section",
        "chunk_number": 0,
        "text": "Synthetic passage text.",
        "previous_passage_id": None,
        "next_passage_id": "paper-a-passage-02",
    }
    assert set(dumped) == {
        "passage_id",
        "paper_id",
        "title",
        "section",
        "chunk_number",
        "text",
        "previous_passage_id",
        "next_passage_id",
    }
    assert restored == original


@pytest.mark.parametrize(
    "missing_field",
    [
        "passage_id",
        "paper_id",
        "title",
        "section",
        "chunk_number",
        "text",
    ],
)
def test_missing_required_fields_are_rejected(missing_field: str) -> None:
    data = _passage_data()
    del data[missing_field]

    with pytest.raises(ValidationError):
        Passage.model_validate(data)


def test_unknown_extra_fields_are_rejected() -> None:
    with pytest.raises(ValidationError, match="extra_forbidden"):
        Passage.model_validate(_passage_data(unapproved_field="not allowed"))


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("passage_id", 123),
        ("paper_id", False),
        ("title", ["not", "a", "string"]),
        ("section", {"not": "a string"}),
        ("text", 1.5),
        ("previous_passage_id", 123),
        ("next_passage_id", False),
    ],
)
def test_string_fields_reject_non_strings(field_name: str, value: object) -> None:
    with pytest.raises(ValidationError):
        Passage.model_validate(_passage_data(**{field_name: value}))


@pytest.mark.parametrize(
    "field_name",
    ["passage_id", "paper_id", "title", "section", "text"],
)
@pytest.mark.parametrize("value", ["", "   ", " leading", "trailing ", "\tvalue"])
def test_required_strings_reject_empty_blank_and_edge_whitespace(
    field_name: str,
    value: str,
) -> None:
    with pytest.raises(ValidationError):
        Passage.model_validate(_passage_data(**{field_name: value}))


@pytest.mark.parametrize("field_name", ["previous_passage_id", "next_passage_id"])
@pytest.mark.parametrize("value", ["", "   ", " leading", "trailing ", "\tvalue"])
def test_optional_neighbor_ids_reject_non_null_invalid_strings(
    field_name: str,
    value: str,
) -> None:
    with pytest.raises(ValidationError):
        Passage.model_validate(_passage_data(**{field_name: value}))


@pytest.mark.parametrize("value", [-1, True, 1.0])
def test_chunk_number_requires_a_non_negative_strict_integer(value: object) -> None:
    with pytest.raises(ValidationError):
        Passage.model_validate(_passage_data(chunk_number=value))


def test_self_links_are_rejected() -> None:
    with pytest.raises(ValidationError, match="must not equal passage_id"):
        Passage.model_validate(
            _passage_data(
                previous_passage_id="paper-a-passage-01",
                next_passage_id=None,
            )
        )
    with pytest.raises(ValidationError, match="must not equal passage_id"):
        Passage.model_validate(
            _passage_data(
                previous_passage_id=None,
                next_passage_id="paper-a-passage-01",
            )
        )


def test_identical_neighbor_ids_are_rejected() -> None:
    with pytest.raises(
        ValidationError,
        match="previous_passage_id and next_passage_id must not be equal",
    ):
        Passage.model_validate(
            _passage_data(
                previous_passage_id="paper-a-passage-00",
                next_passage_id="paper-a-passage-00",
            )
        )


def test_assignment_validation_rejects_invalid_updates() -> None:
    passage = Passage.model_validate(_passage_data())

    with pytest.raises(ValidationError):
        passage.text = " changed with an edge space"
    with pytest.raises(ValidationError):
        passage.chunk_number = True
    with pytest.raises(ValidationError):
        passage.unapproved_field = "not allowed"


def test_chunk_number_does_not_generate_or_rewrite_neighbor_ids() -> None:
    passage = Passage.model_validate(
        _passage_data(
            chunk_number=4,
            previous_passage_id="synthetic-previous",
            next_passage_id="synthetic-next",
        )
    )

    passage.chunk_number = 9

    assert passage.chunk_number == 9
    assert passage.previous_passage_id == "synthetic-previous"
    assert passage.next_passage_id == "synthetic-next"


def test_json_schema_exposes_only_the_approved_fields() -> None:
    schema = Passage.model_json_schema()

    assert set(schema["properties"]) == {
        "passage_id",
        "paper_id",
        "title",
        "section",
        "chunk_number",
        "text",
        "previous_passage_id",
        "next_passage_id",
    }
    assert set(schema["required"]) == {
        "passage_id",
        "paper_id",
        "title",
        "section",
        "chunk_number",
        "text",
    }
    assert schema["properties"]["previous_passage_id"]["anyOf"] == [
        {"type": "string"},
        {"type": "null"},
    ]
    assert schema["properties"]["next_passage_id"]["anyOf"] == [
        {"type": "string"},
        {"type": "null"},
    ]
    chunk_description = schema["properties"]["chunk_number"]["description"].lower()
    assert "zero-based" in chunk_description
    assert "source container" in chunk_description
    assert "chunk_index" in chunk_description
    assert "null" in schema["properties"]["previous_passage_id"]["description"]
    assert "null" in schema["properties"]["next_passage_id"]["description"]


def test_chunk_boundary_preconditions_are_documented_without_claiming_runtime_validation() -> None:
    schema = Passage.model_json_schema()
    text_description = schema["properties"]["text"]["description"].lower()
    class_docstring = (Passage.__doc__ or "").lower()

    assert "exactly one source container" in text_description
    assert "paper_id, source_kind, section_index" in text_description
    assert "never used to infer" in schema["properties"]["section"]["description"]
    assert "cannot validate the source coordinates" in class_docstring
    assert "not part of the public" in class_docstring
