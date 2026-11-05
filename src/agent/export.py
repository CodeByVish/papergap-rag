"""Handoff record from the agent to generation and evaluation (P5/P6).

One JSON object per question, holding the full terminal `AgentState` including
`retrieved_passages` with their text. `graph.invoke` returns a dict of Python
objects, so it is revalidated as `AgentState` before serialising.
"""

from __future__ import annotations

import json
from typing import Any

from src.agent.schemas import AgentState


def export_record(result: AgentState | dict[str, Any]) -> dict[str, Any]:
    """JSON-safe dict of the terminal agent state (enums become their values)."""
    state = result if isinstance(result, AgentState) else AgentState.model_validate(result)
    return state.model_dump(mode="json")


def to_jsonl_line(result: AgentState | dict[str, Any]) -> str:
    """One JSONL line (no trailing newline) for `export_record(result)`."""
    return json.dumps(export_record(result), ensure_ascii=False)
