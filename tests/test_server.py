"""The Option-C demo service: one answer at a time, same path as the batch.

These tests use the mock backend, so they run on a CPU-only box. FastAPI and
httpx are optional dependencies, not P5 runtime requirements, so the module
skips when they are absent - importing ``src.generation.server`` itself never needs
them, which is the property the skip protects.

What is pinned here is the HTTP contract P6's UI codes against:

* ``POST /answer`` returns the canonical answer record unchanged (the five-key
  ``result`` plus ``validation`` and ``generation``);
* a refusal is ``200``, not an error status - the UI distinguishes them by
  ``result.evidence_status``, exactly as it reads a JSONL file;
* a malformed payload is ``400`` and a missing retriever is ``503``; neither is
  allowed to look like a model refusal;
* free-form input is paper-scoped, because QASPER retrieval is.
"""

from __future__ import annotations

import json
import threading
import time

import pytest

pytest.importorskip("fastapi")
pytest.importorskip("httpx")

from fastapi.testclient import TestClient  # noqa: E402

from src.generation.generators import MockGenerator, MockScenario  # noqa: E402
from src.generation.pipeline import GroundedQAPipeline  # noqa: E402
from src.generation.server import (  # noqa: E402
    WARMUP_RECORD,
    create_app,
    first_record,
    load_passage_index,
    load_record_fn,
    paper_ids_from,
    warm_up,
)

HASHED = "qasper-passage-v1-" + "a" * 64


def hit(text: str = "The model sets a new state of the art.") -> dict:
    """One P2-shaped nested hit, the same shape the batch path consumes."""
    return {
        "passage": {
            "passage_id": HASHED,
            "paper_id": "paper-1",
            "title": "Synthetic paper",
            "section": "results",
            "chunk_number": 0,
            "text": text,
        },
        "rank": 1,
        "rrf_score": 0.9,
        "reranker_score": None,
    }


def exported_record(**overrides) -> dict:
    record = {
        "question_id": "q-001",
        "question": "What result is reported?",
        "paper_id": "paper-1",
        "retrieval_round": 1,
        "retrieved_passages": [hit()],
        "sufficient": True,
        "gap_label": "NONE",
        "required_components": ["result"],
        "evidence_map": {"result": [HASHED]},
    }
    record.update(overrides)
    return record


def pipeline() -> GroundedQAPipeline:
    return GroundedQAPipeline(MockGenerator(MockScenario.GROUNDED))


def client(**kwargs) -> TestClient:
    return TestClient(create_app(pipeline(), **kwargs))


def agent_record_factory(pipe: GroundedQAPipeline):
    """A module-level factory, for the ``load_record_fn`` import-path test."""
    return lambda question, paper_id: exported_record(
        question=question, paper_id=paper_id
    )


# --------------------------------------------------------------------------- #
# The answer contract
# --------------------------------------------------------------------------- #


def test_health_reports_what_the_ui_needs():
    response = client(papers=["paper-1"]).get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["backend"] == "mock"
    assert body["papers"] == 1
    assert body["retrieval"] is False
    assert body["agent"] is False


def test_an_exported_record_is_answered_and_returned_unchanged():
    response = client().post("/answer", json={"record": exported_record()})

    assert response.status_code == 200
    body = response.json()
    assert body["request_id"] == "q-001"
    assert set(body["result"]) == {
        "answer", "citations", "evidence_status", "retrieval_rounds", "provenance"
    }
    assert body["result"]["evidence_status"] == "SUFFICIENT"
    assert body["agent"]["sufficient"] is True
    assert "raw_text_excerpt" in body["generation"]


def test_a_refusal_is_a_200_not_an_error():
    """The UI must read refusals the same way it reads them from a JSONL file."""
    response = client().post(
        "/answer", json={"record": exported_record(retrieved_passages=[])}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["result"]["evidence_status"] == "INSUFFICIENT"
    assert body["validation"]["downgraded"] is False  # a terminal refusal, not a downgrade


def test_the_agent_insufficient_label_refuses_without_a_model_call():
    response = client().post(
        "/answer",
        json={"record": exported_record(gap_label="INSUFFICIENT_INFORMATION")},
    )

    assert response.status_code == 200
    codes = [v["code"] for v in response.json()["validation"]["violations"]]
    assert "AGENT_INSUFFICIENT" in codes


# --------------------------------------------------------------------------- #
# Free-form input
# --------------------------------------------------------------------------- #


def test_free_form_questions_go_through_the_injected_retriever():
    calls: list[tuple[str, str, int]] = []

    def retriever(question: str, paper_id: str, top_k: int) -> list[dict]:
        calls.append((question, paper_id, top_k))
        return [hit()]

    response = client(retriever=retriever, top_k=3).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 200
    assert calls == [("What result is reported?", "paper-1", 3)]
    assert response.json()["result"]["evidence_status"] == "SUFFICIENT"


def test_free_form_without_a_retriever_is_503_not_a_refusal():
    response = client().post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 503
    assert "--retriever" in response.json()["detail"]


def test_free_form_requires_a_paper_id():
    response = client(retriever=lambda q, p, k: [hit()]).post(
        "/answer", json={"question": "What result is reported?"}
    )

    assert response.status_code == 400
    assert "paper_id" in response.json()["detail"]


def test_a_retriever_returning_a_non_list_is_a_server_error():
    response = client(retriever=lambda q, p, k: {"not": "a list"}).post(
        "/answer", json={"question": "Why?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "retriever" in response.json()["detail"]


# --------------------------------------------------------------------------- #
# Free-form through the agent hook
# --------------------------------------------------------------------------- #


def test_record_fn_runs_retrieval_and_the_server_answers_once():
    calls: list[tuple[str, str]] = []

    def record_fn(question: str, paper_id: str) -> dict:
        calls.append((question, paper_id))
        return exported_record(question=question, paper_id=paper_id)

    response = client(record_fn=record_fn).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 200
    assert calls == [("What result is reported?", "paper-1")]
    assert response.json()["result"]["evidence_status"] == "SUFFICIENT"
    assert response.json()["agent"]["sufficient"] is True


def test_health_reports_the_agent_hook():
    body = client(record_fn=lambda q, p: exported_record()).get("/health").json()

    assert body["agent"] is True
    assert body["retrieval"] is True


def test_record_fn_returning_an_answer_is_500_not_a_second_generation():
    def record_fn(question: str, paper_id: str) -> dict:
        return {**exported_record(question=question, paper_id=paper_id), "answer": {}}

    response = client(record_fn=record_fn).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "answer_fn=None" in response.json()["detail"]


def test_create_app_rejects_two_free_form_hooks():
    with pytest.raises(ValueError, match="either retriever or record_fn"):
        create_app(
            pipeline(),
            retriever=lambda q, p, k: [hit()],
            record_fn=lambda q, p: exported_record(),
        )


def test_a_record_fn_error_record_is_500_not_a_refusal():
    response = client(
        record_fn=lambda q, p: {"question_id": "ui-1", "error": "agent failed"}
    ).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "agent failed" in response.json()["detail"]


def test_a_record_fn_exception_is_500_not_a_refusal():
    def record_fn(question: str, paper_id: str) -> dict:
        raise RuntimeError("the agent exploded")

    response = client(record_fn=record_fn).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "the agent exploded" in response.json()["detail"]


def test_a_record_fn_returning_a_non_object_is_500():
    response = client(record_fn=lambda q, p: ["not a record"]).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "expected the exported AgentState" in response.json()["detail"]


def test_a_malformed_record_from_the_hook_is_500_not_400():
    response = client(record_fn=lambda q, p: {"paper_id": "paper-1"}).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 500
    assert "cannot answer" in response.json()["detail"]


def test_record_fn_assigns_a_request_id_when_the_export_has_none():
    def record_fn(question: str, paper_id: str) -> dict:
        record = exported_record(question=question, paper_id=paper_id)
        record.pop("question_id")
        return record

    response = client(record_fn=record_fn).post(
        "/answer", json={"question": "What result is reported?", "paper_id": "paper-1"}
    )

    assert response.status_code == 200
    assert response.json()["request_id"].startswith("ui-")


def test_load_record_fn_binds_the_pipeline():
    bound = load_record_fn(f"{__name__}:agent_record_factory", pipeline())

    record = bound("What result is reported?", "paper-1")

    assert record["question"] == "What result is reported?"
    assert record["paper_id"] == "paper-1"


# --------------------------------------------------------------------------- #
# Client errors are not refusals
# --------------------------------------------------------------------------- #


def test_an_empty_body_is_400():
    response = client().post("/answer", json={})
    assert response.status_code == 400


def test_record_and_question_together_are_400():
    response = client().post(
        "/answer", json={"record": exported_record(), "question": "Which one?"}
    )
    assert response.status_code == 400


def test_a_record_that_is_not_an_object_is_400():
    response = client().post("/answer", json={"record": "not-an-object"})
    assert response.status_code == 400


def test_a_record_without_a_question_is_400_not_a_refusal():
    response = client().post("/answer", json={"record": {"paper_id": "paper-1"}})
    assert response.status_code == 400


def test_a_bearer_token_is_enforced_when_configured():
    app = client(token="s3cret")

    assert app.post("/answer", json={"record": exported_record()}).status_code == 401
    assert (
        app.post(
            "/answer",
            json={"record": exported_record()},
            headers={"Authorization": "Bearer wrong"},
        ).status_code
        == 401
    )
    assert (
        app.post(
            "/answer",
            json={"record": exported_record()},
            headers={"Authorization": "Bearer s3cret"},
        ).status_code
        == 200
    )


# --------------------------------------------------------------------------- #
# One at a time
# --------------------------------------------------------------------------- #


def test_a_second_question_is_429_while_one_is_in_flight():
    """The engine is not thread-safe, so the lock must answer 429, not queue.

    Two clients over one app: the lock lives on the app, and separate clients
    avoid sharing an httpx client across threads.
    """
    entered = threading.Event()

    def slow_retriever(question: str, paper_id: str, top_k: int) -> list[dict]:
        entered.set()
        time.sleep(0.5)
        return [hit()]

    app = create_app(pipeline(), retriever=slow_retriever)
    first = TestClient(app)
    second = TestClient(app)
    results: list[int] = []
    body = {"question": "What result is reported?", "paper_id": "paper-1"}

    def ask() -> None:
        results.append(first.post("/answer", json=body).status_code)

    worker = threading.Thread(target=ask)
    worker.start()
    assert entered.wait(timeout=2), "the first request never reached the retriever"
    busy = second.post("/answer", json=body)
    worker.join(timeout=5)

    assert results == [200]
    assert busy.status_code == 429
    assert "one question at a time" in busy.json()["detail"]


# --------------------------------------------------------------------------- #
# Citation text lookup
# --------------------------------------------------------------------------- #


def test_passage_index_accepts_flat_and_nested_records(tmp_path):
    dump = tmp_path / "passages.jsonl"
    dump.write_text(
        "\n".join(
            [
                json.dumps({"passage_id": "flat", "text": "Flat text.", "paper_id": "p"}),
                json.dumps(
                    {
                        "passage": {
                            "passage_id": "nested",
                            "text": "Nested text.",
                            "paper_id": "p",
                            "section": "results",
                        }
                    }
                ),
                "not json",
                json.dumps({"passage_id": "no-text"}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    index = load_passage_index(dump)

    assert set(index) == {"flat", "nested"}
    assert index["nested"]["text"] == "Nested text."
    assert index["nested"]["section"] == "results"


def test_passage_index_reads_a_retrieval_envelope(tmp_path):
    """The only dump P5 has on the cluster is a retrieval dump, not the corpus.

    Its lines are ``{question, retrieved_passages: [...]}``; an indexer that
    looked only at the top level came out empty even though every passage was
    right there.
    """
    dump = tmp_path / "retrieval.jsonl"
    dump.write_text(
        json.dumps(
            {
                "question": "Q?",
                "question_id": "q1",
                "paper_id": "p",
                "retrieved_passages": [
                    hit(),
                    {"passage": {"passage_id": "other", "text": "Other text."}},
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    index = load_passage_index(dump)

    assert set(index) == {HASHED, "other"}
    assert index[HASHED]["text"].startswith("The model")


def test_citation_ids_resolve_to_passage_text():
    passages = {"id-1": {"text": "The cited sentence.", "paper_id": "p"}}
    response = client(passages=passages).post("/passages", json={"ids": ["id-1", "nope"]})

    assert response.status_code == 200
    body = response.json()
    assert body["passages"]["id-1"]["text"] == "The cited sentence."
    assert body["missing"] == ["nope"]


def test_citation_lookup_without_an_index_is_503():
    response = client().post("/passages", json={"ids": ["id-1"]})

    assert response.status_code == 503
    assert "--passages-from" in response.json()["detail"]


def test_citation_lookup_rejects_a_non_list():
    response = client(passages={}).post("/passages", json={"ids": "id-1"})
    assert response.status_code == 400


# --------------------------------------------------------------------------- #
# Startup inputs
# --------------------------------------------------------------------------- #


def test_paper_ids_are_unique_sorted_and_tolerant_of_bad_lines(tmp_path):
    dump = tmp_path / "retrieval.jsonl"
    dump.write_text(
        "\n".join(
            [
                json.dumps({"paper_id": "b"}),
                "not json",
                json.dumps({"paper_id": "a"}),
                json.dumps({"paper_id": "b"}),
                json.dumps({"question": "no paper"}),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    assert paper_ids_from(dump) == ["a", "b"]


def test_first_record_skips_empty_lines(tmp_path):
    dump = tmp_path / "answers.jsonl"
    dump.write_text("\n\n" + json.dumps({"question": "First?"}) + "\n", encoding="utf-8")

    assert first_record(dump) == {"question": "First?"}


def test_warm_up_runs_the_real_path_and_returns_seconds():
    messages: list[str] = []

    seconds = warm_up(pipeline(), WARMUP_RECORD, echo=messages.append)

    assert seconds > 0
    assert messages and messages[0].startswith("[warmup]")
