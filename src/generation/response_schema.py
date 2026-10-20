"""The frozen P6 response contract, as a JSON Schema.

Why this is written by hand rather than generated with ``model_json_schema()``:

* **It works everywhere.** That call raises ``AttributeError: '_SpecialForm'
  object has no attribute 'replace'`` on Python 3.9 with pydantic 2.12, for *any*
  model - an environment bug, not a P5 one.
* **It is stable.** An artefact P6 diffs and validates against must be
  byte-identical on every machine, and a generator whose output depends on the
  local pydantic version cannot promise that. Hand-writing it also makes the
  contract reviewable as a document rather than as generated boilerplate.

The constants here are pinned to :mod:`src.generation.schema` by ``tests/test_examples.py``:
the key set, the required list and the enum values are all checked against the
Pydantic model, so this file cannot silently drift from the code that produces
the data.
"""

from __future__ import annotations

from typing import Any

from src.generation.schema import ANSWER_KEYS, SCHEMA_VERSION

__all__ = ["FINAL_RESPONSE_SCHEMA"]


FINAL_RESPONSE_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "GenerationResult",
    "description": (
        f"P5 final-answer object ({SCHEMA_VERSION}) consumed by P6. "
        "evidence_status=INSUFFICIENT implies empty citations and provenance, and "
        "answer equal to the canonical refusal text."
    ),
    "type": "object",
    # additionalProperties=False makes the frozen five-key contract enforceable:
    # a consumer that validates against this schema will reject a result that has
    # grown an extra field, which is exactly when we want to hear about it.
    "additionalProperties": False,
    "required": list(ANSWER_KEYS),
    "properties": {
        "answer": {
            "type": "string",
            "description": (
                "The generated answer, or the canonical refusal text. Contains no "
                "citation markers; citations live in the citations field."
            ),
        },
        "citations": {
            "type": "array",
            "items": {"type": "string"},
            "description": (
                "Passage ids. Every id was present in the retrieved context, "
                "de-duplicated, in order of first appearance. Empty for a refusal."
            ),
        },
        "evidence_status": {
            "type": "string",
            "enum": ["SUFFICIENT", "INSUFFICIENT"],
            "description": "Whether the retrieved passages supported an answer.",
        },
        "retrieval_rounds": {
            "type": "integer",
            "minimum": 1,
            "description": (
                "Number of retrieval rounds that produced the context. Preserved "
                "through a downgrade so retrieval cost stays attributable."
            ),
        },
        "provenance": {
            "type": "array",
            "items": {"$ref": "#/$defs/ProvenanceEntry"},
            "description": (
                "Per-claim evidence map. Empty for a refusal. After a downgrade it "
                "is empty too: the model's original claims survive only in the "
                "validation report's raw_result, because a refusal makes no claims."
            ),
        },
    },
    "$defs": {
        "ProvenanceEntry": {
            "type": "object",
            "required": ["claim"],
            "additionalProperties": False,
            "properties": {
                "claim": {"type": "string"},
                "passage_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "support": {
                    "type": "string",
                    "enum": ["direct", "partial", "unsupported"],
                },
            },
        }
    },
}
