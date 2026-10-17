import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from streamlit.testing.v1 import AppTest

from src.generation.prompting import build_messages, citation_warnings
from src.retrieval.indexed_retriever import load_chunks

APP = Path(__file__).resolve().parents[1] / "src/ui/app.py"
PASSAGES = [
    {
        "chunk_id": "paper__1",
        "paper_id": "paper",
        "title": "Test paper",
        "section_path": ["Results"],
        "page_start": 2,
        "text": "The method improved recall.",
        "source_url": "https://aclanthology.org/",
        "rrf_score": 0.03,
    }
]


def configured_app(monkeypatch, passages=None, answer="Recall improved [E1].", provider="qwen"):
    retriever = Mock()
    retriever.retrieve.return_value = PASSAGES if passages is None else passages
    generate = Mock(return_value=answer)
    monkeypatch.setattr("src.ui.services.missing_artifacts", lambda cfg: [])
    monkeypatch.setattr("src.ui.services.get_retriever", lambda cfg: retriever)
    monkeypatch.setattr("src.generation.llm_client.generate", generate)
    app = AppTest.from_file(str(APP))
    app.secrets["llm"] = {
        provider: {
            "api_key": "test-secret",
            "base_url": "https://example.com/v1",
            "model": "test",
        }
    }
    app.run()
    if provider != "qwen":
        app.selectbox[0].select(provider).run()
    assert not app.exception
    return app, retriever, generate


def test_missing_configuration_opens_without_loading_models():
    app = AppTest.from_file(str(APP))
    app.secrets["llm"] = {}
    app.run()
    assert not app.exception
    assert not app.chat_input[0].disabled
    assert any("setup" in item.value.lower() for item in app.info)


def test_answer_sources_survive_rerun_without_second_api_call(monkeypatch):
    app, retriever, generate = configured_app(monkeypatch)
    app.chat_input[0].set_value("What improved?").run()
    assert not app.exception
    assert any("Recall improved [E1]" in item.value for item in app.markdown)
    assert any("Test paper" in item.value for item in app.subheader)
    app.toggle[0].set_value(True).run()
    assert not app.exception
    assert app.json
    generate.assert_called_once()
    retriever.retrieve.assert_called_once_with("What improved?", top_k=5)
    app.button[0].click().run()
    assert not app.chat_message


def test_empty_retrieval_skips_provider(monkeypatch):
    app, _, generate = configured_app(monkeypatch, passages=[])
    app.chat_input[0].set_value("Unknown?").run()
    assert not app.exception
    assert "No evidence" in app.error[0].value
    generate.assert_not_called()


def test_api_failure_is_redacted_and_evidence_retained(monkeypatch):
    app, _, generate = configured_app(monkeypatch)
    generate.side_effect = RuntimeError("test-secret private stack trace")
    app.chat_input[0].set_value("What improved?").run()
    assert not app.exception
    assert "test-secret" not in app.error[0].value
    assert app.subheader


def test_invalid_citation_and_empty_response(monkeypatch):
    app, _, generate = configured_app(monkeypatch, answer="Claim [E99].")
    app.chat_input[0].set_value("Question").run()
    assert "[E99]" in app.warning[0].value
    generate.return_value = ""
    app.chat_input[0].set_value("Again").run()
    assert "empty answer" in app.error[0].value


def test_prompt_does_not_mutate_passages():
    system, user, evidence = build_messages("Question", PASSAGES)
    assert "evidence_id" not in PASSAGES[0]
    assert evidence[0]["evidence_id"] == "E1"
    assert "untrusted" in system and "The method improved recall" in user
    assert not citation_warnings("Claim [E1].", evidence)
    assert citation_warnings("No citations.", evidence)


def test_duplicate_chunk_ids_fail(tmp_path):
    path = tmp_path / "chunks.jsonl"
    path.write_text("\n".join(json.dumps(PASSAGES[0]) for _ in range(2)))
    with pytest.raises(ValueError, match="unique"):
        load_chunks(path)


def test_index_adapter_fuses_real_scores_and_preserves_metadata():
    from threading import Lock

    import numpy as np

    from src.retrieval.indexed_retriever import IndexedRetriever

    retriever = IndexedRetriever.__new__(IndexedRetriever)
    first = PASSAGES[0]
    second = dict(first, chunk_id="paper__2", text="A second passage.")
    retriever.chunks = {row["chunk_id"]: row for row in (first, second)}
    retriever.row_ids = [first["chunk_id"], second["chunk_id"]]
    retriever.lock = Lock()
    retriever.sparse = Mock()
    retriever.sparse.search.return_value = [
        SimpleNamespace(docid="paper__2", score=7.0)
    ]
    retriever.encoder = Mock()
    retriever.encoder.encode.return_value = np.array([[1.0, 0.0]])
    retriever.dense = Mock()
    retriever.dense.search.return_value = (np.array([[0.9, 0.8]]), np.array([[0, 1]]))
    result = retriever.retrieve("question", top_k=2)
    assert result[0]["chunk_id"] == "paper__2"
    assert result[0]["rrf_score"] == pytest.approx(1 / 61 + 1 / 62)
    assert result[0]["page_start"] == 2
    assert result[0]["source_url"] == first["source_url"]


def test_missing_artifacts_disable_submission(monkeypatch):
    app, _, generate = configured_app(monkeypatch)
    monkeypatch.setattr(
        "src.ui.services.missing_artifacts", lambda cfg: ["indexes/dense/chunks.faiss"]
    )
    app.run()
    assert not app.chat_input[0].disabled
    app.radio[0].set_value("Paper RAG").run()
    assert "indexes/dense/chunks.faiss" in app.code[0].value
    app.chat_input[0].set_value("Question").run()
    assert "requires the missing artifacts" in app.error[0].value
    generate.assert_not_called()


@pytest.mark.parametrize("provider", ["qwen", "grok", "groq"])
def test_provider_adapter_routes_requests(monkeypatch, provider):
    from src.generation.llm_client import generate

    client = Mock()
    client.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="answer"))]
    )
    client.responses.create.return_value = SimpleNamespace(output_text="answer")
    monkeypatch.setattr("src.generation.llm_client.OpenAI", Mock(return_value=client))
    assert (
        generate(
            provider,
            {"api_key": "test", "base_url": "https://example.com", "model": "test"},
            "system",
            "question",
        )
        == "answer"
    )
    method = (
        client.chat.completions.create
        if provider in ("qwen", "groq")
        else client.responses.create
    )
    method.assert_called_once()


def test_groq_selection_sends_configured_provider(monkeypatch):
    app, _, generate = configured_app(monkeypatch, provider="groq")
    assert not app.chat_input[0].disabled
    app.chat_input[0].set_value("What improved?").run()
    assert not app.exception
    generate.assert_called_once()
    assert generate.call_args.args[0] == "groq"
    assert generate.call_args.args[1]["api_key"] == "test-secret"
    assert any("Recall improved [E1]" in item.value for item in app.markdown)


def test_direct_chat_without_indexes(monkeypatch):
    app, retriever, generate = configured_app(monkeypatch, provider="groq")
    monkeypatch.setattr("src.ui.services.missing_artifacts", lambda cfg: ["data/chunks.jsonl"])
    app.run()
    app.radio[0].set_value("Direct chat").run()
    app.chat_input[0].set_value("Explain attention").run()
    assert not app.exception
    generate.assert_called_once()
    retriever.retrieve.assert_not_called()
    assert generate.call_args.args[0] == "groq"
    assert not app.warning


def test_missing_credentials_submission_is_actionable(monkeypatch):
    app, _, generate = configured_app(monkeypatch)
    app.selectbox[0].select("grok").run()
    app.chat_input[0].set_value("Hello").run()
    assert not app.exception
    assert "Configure the API key" in app.error[0].value
    generate.assert_not_called()
