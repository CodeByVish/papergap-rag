"""Cross-paper retrieval, compatibility, and corpus-scope contract checks."""

import numpy as np
import pytest
from fastapi.testclient import TestClient
from rank_bm25 import BM25Okapi

from src.agent.critic import build_critic_messages
from src.agent.demo import make_record_fn
from src.agent.schemas import AgentState
from src.generation.generators.mock import MockGenerator
from src.generation.pipeline import GroundedQAPipeline
from src.generation.server import create_app
from src.retrieval.bm25_retriever import BM25Retriever, _tokenize
from src.retrieval.corpus_hybrid import CorpusHybridRetriever
from src.retrieval.dense_retriever import QUERY_INSTRUCTION, DenseRetriever
from src.retrieval.schemas import Passage


def passages():
    return [
        Passage(
            passage_id=f"qasper-passage-v1-{i:064x}",
            paper_id=paper,
            title="Paper " + paper,
            section="Method",
            chunk_number=i,
            text=text,
        )
        for i, (paper, text) in enumerate(
            [
                ("a", "apples apples shared methods"),
                ("b", "oranges shared methods"),
                ("a", "apples other words"),
                ("b", "oranges other words"),
            ],
            1,
        )
    ]


class Encoder:
    model_name = "synthetic/corpus"
    revision = "v1"

    def __init__(self):
        self.calls = []

    def encode(self, texts):
        self.calls.append(list(texts))
        return np.asarray(
            [
                [1, 0] if t.startswith(QUERY_INSTRUCTION) or "shared" in t else [0, 1]
                for t in texts
            ],
            dtype=np.float32,
        )


def test_bm25_uses_global_statistics():
    rows = passages()
    retriever = BM25Retriever(rows)
    result = retriever.retrieve_corpus("apples", 20)
    canonical = sorted(rows, key=lambda p: p.passage_id)
    reference = BM25Okapi([_tokenize(p.text) for p in canonical]).get_scores(
        _tokenize("apples")
    )
    assert {h.passage.paper_id for h in result} == {"a", "b"}
    for hit in result:
        assert hit.score == pytest.approx(reference[canonical.index(hit.passage)])
    assert {h.passage.paper_id for h in retriever.retrieve("apples", "a", 20)} == {"a"}
    assert retriever.retrieve_corpus("apples", 5, section="unknown") == []


def test_dense_reuses_saved_vectors_and_encodes_query_once(tmp_path):
    encoder = Encoder()
    dense = DenseRetriever(passages(), encoder=encoder)
    dense.save(tmp_path / "dense")
    loaded = DenseRetriever.load(tmp_path / "dense", encoder=encoder)
    encoder.calls.clear()
    hits = loaded.retrieve_corpus("query", 2)
    assert {h.passage.paper_id for h in hits} == {"a", "b"}
    assert encoder.calls == [[QUERY_INSTRUCTION + "query"]]
    assert [h.passage.passage_id for h in hits] == sorted(
        h.passage.passage_id for h in hits
    )
    assert all(h.passage.paper_id == "a" for h in loaded.retrieve("query", "a", 20))


def test_hybrid_reranks_full_global_union_and_preserves_paper_filter():
    rows = passages()
    seen = []

    class Scorer:
        def score(self, query, texts):
            seen.append(list(texts))
            return [1 if "shared" in t else 0 for t in texts]

    hybrid = CorpusHybridRetriever(
        BM25Retriever(rows),
        DenseRetriever(rows, encoder=Encoder()),
        scorer=Scorer(),
        candidate_k=4,
    )
    hits = hybrid.retrieve("query", None, 2)
    assert len(seen[-1]) == 4
    assert {h.passage.paper_id for h in hits} == {"a", "b"}
    assert all(set(h.source_scores) == {"bm25", "dense"} for h in hits)
    assert {h.passage.paper_id for h in hybrid.retrieve("query", "b", 5)} == {"b"}
    assert hybrid.retrieve("query", "unknown", 5) == []


def test_corpus_agent_api_preserves_original_source_ids_and_old_api_rejects_omission():
    rows = passages()
    backend = CorpusHybridRetriever(
        BM25Retriever(rows), DenseRetriever(rows, encoder=Encoder())
    )
    callback = make_record_fn(backend.retrieve, None, max_retries=0)
    app = create_app(
        GroundedQAPipeline(MockGenerator()), record_fn=callback, allow_corpus=True
    )
    response = TestClient(app).post(
        "/answer", json={"question": "What methods use shared representations?"}
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["search"] == {
        "scope": "corpus",
        "paper_id": None,
        "source_papers": ["a", "b"],
    }
    assert payload["agent"]["paper_id"] is None
    assert payload["agent"]["retrieval_log"][0]["paper_ids"] == ["a", "b"]
    assert payload["agent"]["retrieval_log"][0]["search_scope"] == "corpus"
    assert (
        TestClient(app)
        .post("/answer", json={"question": "q", "paper_id": ""})
        .status_code
        == 400
    )
    legacy = create_app(GroundedQAPipeline(MockGenerator()), record_fn=callback)
    assert TestClient(legacy).post("/answer", json={"question": "q"}).status_code == 400


def test_corpus_critic_identifies_sources():
    rows = passages()
    h = CorpusHybridRetriever(
        BM25Retriever(rows), DenseRetriever(rows, encoder=Encoder())
    )
    state = AgentState(
        question="Compare methods",
        paper_id=None,
        retrieved_passages=h.retrieve("query", None, 2),
    )
    from src.agent.schemas import GapLabel
    from src.agent.sections import make_section_selector

    state.gap_label = GapLabel.MISSING_METHOD
    assert make_section_selector(rows)(state) is None
    messages = build_critic_messages(state)
    assert "collection of research papers" in messages[0]["content"]
    assert "paper: a; title: Paper a" in messages[1]["content"]
    assert "paper: b; title: Paper b" in messages[1]["content"]
