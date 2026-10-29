"""Capture one real response per UI state from the demo service.

P6 builds the UI without a GPU, so she needs the actual JSON this server emits
for every state the UI has to render - not a hand-written mock that can drift
from the implementation. This script drives the real FastAPI app with the mock
backend through ``TestClient`` and writes the responses to
``examples/demo_ui_responses.json``.

The responses are *real*: same routing, same ``answer_record`` call, same
validator, same serialisation as the cluster run. Only the generator behind them
is the mock, which is why the file is a UI fixture and not evidence.

Run:

    python scripts/capture_demo_responses.py

Regenerate after any change to the response shape, the status codes or the
violation codes - the UI fixture must never be older than the server.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable

# See smoke_demo_server.py: makes the script runnable from either checkout
# without a PYTHONPATH.
for _candidate in (
    Path(__file__).resolve().parents[1],
    Path(__file__).resolve().parents[1] / "src",
):
    if str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))

from fastapi.testclient import TestClient

from src.generation.generators import MockGenerator, MockScenario
from src.generation.pipeline import GroundedQAPipeline
from src.generation.server import create_app

OUT = Path(__file__).resolve().parents[1] / "examples" / "demo_ui_responses.json"

HASHED = "qasper-passage-v1-" + "a" * 64


def hit(text: str = "The model sets a new state of the art.") -> dict[str, Any]:
    return {
        "passage": {
            "passage_id": HASHED,
            "paper_id": "1706.04115",
            "title": "Zero-Shot Relation Extraction via Reading Comprehension",
            "section": "results",
            "chunk_number": 0,
            "text": text,
        },
        "rank": 1,
        "rrf_score": 0.9,
        "reranker_score": None,
    }


def exported(**overrides: Any) -> dict[str, Any]:
    record: dict[str, Any] = {
        "question_id": "0038b073b7cca847033177024f9719c971692042",
        "question": "What result is reported?",
        "paper_id": "1706.04115",
        "retrieval_round": 1,
        "retrieved_passages": [hit()],
        "sufficient": True,
        "gap_label": "NONE",
        "required_components": ["result"],
        "evidence_map": {"result": [HASHED]},
    }
    record.update(overrides)
    return record


DEMO_PASSAGES = {
    HASHED: {
        "text": "The model sets a new state of the art.",
        "paper_id": "1706.04115",
        "title": "Zero-Shot Relation Extraction via Reading Comprehension",
        "section": "results",
    }
}


def app_for(scenario: MockScenario, **kwargs: Any) -> TestClient:
    return TestClient(
        create_app(
            GroundedQAPipeline(MockGenerator(scenario)),
            papers=["1706.04115"],
            passages=DEMO_PASSAGES,
            **kwargs,
        )
    )


def capture(
    state: str,
    scenario: MockScenario,
    body: dict[str, Any],
    *,
    note: str,
    path: str = "/answer",
    request: Callable[[TestClient], Any] | None = None,
) -> dict[str, Any]:
    client = app_for(scenario)
    send = request or (lambda c: c.post(path, json=body))
    response = send(client)
    return {
        "state": state,
        "note": note,
        "request": {"method": "POST", "path": path, "body": body},
        "status": response.status_code,
        "body": response.json(),
    }


def main() -> int:
    responses = {
        "answered": capture(
            "answered",
            MockScenario.GROUNDED,
            {"record": exported()},
            note=(
                "A normal answer: evidence_status=SUFFICIENT, citations non-empty, "
                "the agent block is present because the input was an AgentState."
            ),
        ),
        "refused_model": capture(
            "refusal (model-declared)",
            MockScenario.REFUSAL,
            {"record": exported()},
            note=(
                "The model itself declared INSUFFICIENT; the answer is the canonical "
                "REFUSAL_ANSWER string and validation.downgraded is false."
            ),
        ),
        "refused_empty_context": capture(
            "refusal (no evidence)",
            MockScenario.GROUNDED,
            {"record": exported(retrieved_passages=[], evidence_map={})},
            note=(
                "No passages were retrieved, so the model was never called. "
                "Violation EMPTY_CONTEXT, raw_text is None in generation."
            ),
        ),
        "refused_agent_insufficient": capture(
            "refusal (critic)",
            MockScenario.GROUNDED,
            {"record": exported(sufficient=False, gap_label="INSUFFICIENT_INFORMATION")},
            note=(
                "P4's critic labelled the gap INSUFFICIENT_INFORMATION; P5 refused "
                "without a model call. Violation AGENT_INSUFFICIENT."
            ),
        ),
        "downgraded": capture(
            "downgraded to refusal",
            MockScenario.HALLUCINATED_CITATION,
            {"record": exported()},
            note=(
                "The model cited a passage it was not given. The validator replaced "
                "the answer with a refusal: downgraded=true and an ERROR-level "
                "violation. The UI should badge this differently from a normal refusal."
            ),
        ),
        "warning_partial": capture(
            "answered with warnings",
            MockScenario.PARTIAL,
            {"record": exported()},
            note=(
                "The answer is kept; the violation is WARNING-level. This is the "
                "state that needs a warnings badge rather than a refusal badge."
            ),
        ),
        "bad_request": capture(
            "client error",
            MockScenario.GROUNDED,
            {"paper_id": "1706.04115"},
            note=(
                "No question and no record: 400. This is a UI bug, not a refusal - "
                "FastAPI's own validation errors use the same {'detail': ...} shape."
            ),
        ),
        "free_form_unconfigured": capture(
            "service unavailable",
            MockScenario.GROUNDED,
            {"question": "What result is reported?", "paper_id": "1706.04115"},
            note=(
                "Free-form input while no retriever is wired: 503. The UI should "
                "disable the input and show the detail, not retry."
            ),
        ),
        "citation_text": capture(
            "citation text lookup",
            MockScenario.GROUNDED,
            {"ids": [HASHED, "qasper-passage-v1-" + "b" * 64]},
            note=(
                "POST /passages resolves cited ids to text. 'missing' lists ids the "
                "corpus dump does not contain; show them as missing, do not crash."
            ),
            path="/passages",
        ),
        "health": {
            "state": "liveness",
            "note": "What GET /health returns; use it for the status badge and the tunnel check.",
            "request": {"method": "GET", "path": "/health", "body": None},
            "status": 200,
            "body": app_for(MockScenario.GROUNDED).get("/health").json(),
        },
        "papers": {
            "state": "paper selector",
            "note": "GET /papers: the paper ids the UI may offer. Empty when --papers-from is unset.",
            "request": {"method": "GET", "path": "/papers", "body": None},
            "status": 200,
            "body": app_for(MockScenario.GROUNDED).get("/papers").json(),
        },
        "busy": {
            "state": "busy",
            "note": (
                "Shape of the 429 body (not captured live: it needs two concurrent "
                "requests). The UI should retry after ~20 s, not treat it as an answer."
            ),
            "request": {"method": "POST", "path": "/answer", "body": {"record": "..."}},
            "status": 429,
            "body": {
                "detail": (
                    "the demo server answers one question at a time; wait for the "
                    "current answer (p90 ~17 s) and retry"
                )
            },
        },
    }

    payload = {
        "generated_by": "scripts/capture_demo_responses.py",
        "server": "src.generation.server.create_app",
        "backend": "mock (same code path as vLLM; the generator is the mock)",
        "answer_keys": ["answer", "citations", "evidence_status", "retrieval_rounds", "provenance"],
        "responses": responses,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(responses)} states)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
