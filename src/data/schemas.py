"""Pydantic contracts for normalized passage records.

The passage contract intentionally contains only fields with a currently
identified downstream consumer.  The provenance-field search produced the
following evidence and deferred decisions:

* ``source_split`` has no current runtime consumer; its source-partition
  definition and missing-value behavior are not established.
* ``section_index`` is read only as a zero-based diagnostic coordinate within
  ``full_text`` by the QASPER inspection code.  Missing coordinates sort as
  ``-1`` in that diagnostic code, but no passage-consumer behavior is defined.
* ``paragraph_indices`` has no current runtime consumer; its source-mapping
  definition and missing-value behavior are not established.
* ``word_start`` and ``word_end`` have no current runtime consumer; their chunk
  boundary definitions and missing-value behavior are not established.

These five candidates remain deferred decisions rather than fields in this
model.
"""

from __future__ import annotations

from typing import Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
    field_validator,
    model_validator,
)

PASSAGE_SCHEMA_VERSION = "v0-proposed"


def _validate_non_blank_string(field_name: str, value: str) -> str:
    """Validate a required or non-null passage string without changing it."""

    if value == "":
        raise ValueError(f"{field_name} must not be empty")
    if value.strip() == "":
        raise ValueError(f"{field_name} must not be blank")
    if value != value.strip():
        raise ValueError(
            f"{field_name} must not have leading or trailing whitespace"
        )
    return value


class Passage(BaseModel):
    """A validated, already-normalized passage record.

    The model validates values produced by a later normalization and chunking
    stage.  It does not normalize source text, generate IDs, or infer links to
    other records.  ``text`` must come from exactly one internal source
    container identified by ``(paper_id, source_kind, section_index)``.  This
    model declares that precondition but cannot validate the source coordinates
    or the text origin because those coordinates are not part of the public
    eight-field model.  ``chunk_number`` is the zero-based, contiguous position
    within the source-container sequence and has the same value as the ID
    coordinate ``chunk_index``.  The neighbor fields identify direct passages
    in that same sequence, or are null at a sequence boundary.
    """

    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    passage_id: StrictStr = Field(
        description="Stable identifier for this passage."
    )
    paper_id: StrictStr = Field(
        description="Stable identifier of the source paper."
    )
    title: StrictStr = Field(description="Normalized source-paper title.")
    section: StrictStr = Field(
        description=(
            "Normalized display source-section name; never used to infer a "
            "source-container boundary."
        )
    )
    chunk_number: StrictInt = Field(
        ge=0,
        description=(
            "Zero-based contiguous position within the source container; "
            "equal to the passage ID chunk_index and reset for each source "
            "container sequence."
        ),
    )
    text: StrictStr = Field(
        description=(
            "Non-empty normalized passage text from exactly one source "
            "container (paper_id, source_kind, section_index)."
        )
    )
    previous_passage_id: StrictStr | None = Field(
        default=None,
        description=(
            "ID of the direct previous passage in the same source-container "
            "sequence, or null at the sequence boundary."
        ),
    )
    next_passage_id: StrictStr | None = Field(
        default=None,
        description=(
            "ID of the direct next passage in the same source-container "
            "sequence, or null at the sequence boundary."
        ),
    )

    @field_validator("passage_id", "paper_id", "title", "section", "text")
    @classmethod
    def validate_required_strings(cls, value: str, info: object) -> str:
        """Reject empty, blank, or edge-whitespace required strings."""

        field_name = getattr(info, "field_name", "string field")
        return _validate_non_blank_string(field_name, value)

    @field_validator("previous_passage_id", "next_passage_id")
    @classmethod
    def validate_optional_ids(cls, value: str | None, info: object) -> str | None:
        """Validate optional neighbor IDs without normalizing them."""

        if value is None:
            return None
        field_name = getattr(info, "field_name", "neighbor ID")
        return _validate_non_blank_string(field_name, value)

    @model_validator(mode="after")
    def validate_neighbor_relationships(self) -> Self:
        """Reject self-links and identical previous and next links."""

        if self.previous_passage_id == self.passage_id:
            raise ValueError("previous_passage_id must not equal passage_id")
        if self.next_passage_id == self.passage_id:
            raise ValueError("next_passage_id must not equal passage_id")
        if (
            self.previous_passage_id is not None
            and self.previous_passage_id == self.next_passage_id
        ):
            raise ValueError(
                "previous_passage_id and next_passage_id must not be equal"
            )
        return self
