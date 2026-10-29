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
