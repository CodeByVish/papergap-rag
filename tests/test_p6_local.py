"""Contract checks for local generation, agent HTTP execution and saved config."""

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from src.generation.generators.mock import MockGenerator
from src.generation.generators.ollama_backend import OllamaGenerator
from src.generation.pipeline import GroundedQAPipeline
from src.generation.server import WARMUP_RECORD, create_app


def test_agent_hook_runs_only_for_fresh_question():
    calls = []

    def record_fn(question, paper_id, top_k, request_id):
        calls.append((question, paper_id, top_k, request_id))
        return {
            **WARMUP_RECORD,
            "question": question,
            "paper_id": paper_id,
            "critic_log": [{"round": 1, "source": "llm"}],
        }

    client = TestClient(
        create_app(GroundedQAPipeline(MockGenerator()), record_fn=record_fn)
    )
    assert client.get("/health").json()["agent"] is True
    assert client.get("/health").json()["retrieval"] is True
    response = client.post(
        "/answer", json={"question": "A question?", "paper_id": "paper-A"}
    )
    assert response.status_code == 200
    assert response.json()["agent"]["critic_log"] == [{"round": 1, "source": "llm"}]
    assert len(calls) == 1
    assert client.post("/answer", json={"record": WARMUP_RECORD}).status_code == 200
    assert len(calls) == 1


def test_hook_is_exclusive_and_protected():
    pipeline = GroundedQAPipeline(MockGenerator())
    with pytest.raises(ValueError, match="alternatives"):
        create_app(pipeline, retriever=lambda *a: [], record_fn=lambda *a: {})
    calls = []
    client = TestClient(
        create_app(pipeline, record_fn=lambda *a: calls.append(a), token="secret")
    )
    assert (
        client.post("/answer", json={"question": "Why?", "paper_id": "p"}).status_code
        == 401
    )
    assert calls == []


def test_ollama_uses_nonstreaming_and_no_thinking(monkeypatch):
    generator = OllamaGenerator("test-model")
    requests = []

    def post(endpoint, payload):
        requests.append((endpoint, payload))
        return {
            "message": {"content": '{"ok": true}'},
            "eval_count": 4,
            "prompt_eval_count": 12,
            "total_duration": 2_000_000_000,
        }

    generator._loaded = True
    monkeypatch.setattr(generator, "_post", post)
    result = generator.chat([{"role": "user", "content": "check"}])
    assert json.loads(result) == {"ok": True}
    assert requests[0][1]["think"] is False
    assert requests[0][1]["stream"] is False
    assert requests[0][1]["options"]["num_ctx"] == 8192
    assert generator.last_generation_stats.completion_tokens == 4
    assert generator.last_generation_stats.batch_seconds == 2


def test_saved_config_resolves_paths_and_clears_old_auth(monkeypatch, tmp_path):
    from scripts import p6_local

    override = tmp_path / "overrides.env"
    override.write_text("")
    monkeypatch.setenv("P6_CONFIG_FILE", str(override))
    monkeypatch.setenv("P5_API_TOKEN", "stale-secret")
    # Track mutations so pytest restores the process environment afterwards.
    for key in p6_local.dotenv_keys():
        monkeypatch.setenv(key, "")
    p6_local.configure()
    assert (
        Path(__file__).resolve().parents[1]
        == Path(p6_local.os.environ["PAPERGAP_CORPUS"]).parents[2]
    )
    assert p6_local.os.environ["P5_API_TOKEN"] == ""
    assert p6_local.os.environ["DEMO_AGENT_BGE"] == "1"


def test_truncated_critic_can_escalate_but_answer_cannot_succeed(monkeypatch):
    from src.generation.adapters.retrieval import build_request

    generator = OllamaGenerator("test-model")
    generator._loaded = True
    monkeypatch.setattr(
        generator,
        "_post",
        lambda *args: {
            "message": {"content": '{"answer": "cut off'},
            "done_reason": "length",
            "total_duration": 1,
        },
    )
    # P4 receives raw text so GeneratorChatClient can detect unbalanced braces.
    assert generator.chat([{"role": "user", "content": "critic"}]).startswith("{")
    with pytest.raises(RuntimeError, match="completion limit"):
        generator.generate(build_request(WARMUP_RECORD).request)


def test_model_transport_failure_is_not_a_valid_refusal(monkeypatch):
    import requests

    from src.generation.generators.base import BackendNotAvailable

    def unavailable(*args, **kwargs):
        raise requests.ConnectionError("service down")

    monkeypatch.setattr(requests, "post", unavailable)
    with pytest.raises(BackendNotAvailable, match="service down"):
        OllamaGenerator("test-model").load()
