import json
from pathlib import Path

import pytest

from scripts.build_indexes import load_passages
from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.scoped import SectionScopedRetriever
from src.retrieval.score_cache import CachedPairScorer


class Scorer:
    def __init__(self):
        self.calls = []

    def score(self, query, texts):
        self.calls.append((query, list(texts)))
        return [float(len(text)) for text in texts]


IDENTITY = {"model_name": "test", "revision": "a" * 40, "max_length": 512}


def test_persistent_cache_content_config_and_query_keys(tmp_path):
    path = tmp_path / "scores.sqlite"
    scorer = Scorer()
    cache = CachedPairScorer(scorer, path, identity=IDENTITY)
    assert cache.score("q", ["aa", "b", "aa"]) == [2, 1, 2]
    assert scorer.calls == [("q", ["aa", "b"])]
    cache.close()
    cache = CachedPairScorer(scorer, path, identity=IDENTITY)
    assert cache.score("q", ["b", "aa"]) == [1, 2]
    assert len(scorer.calls) == 1
    cache.score("changed question", ["aa"])
    cache.score("q", ["changed text"])
    assert len(scorer.calls) == 3
    cache.close()
    changed = CachedPairScorer(scorer, path, identity={**IDENTITY, "max_length": 256})
    changed.score("q", ["aa"])
    assert len(scorer.calls) == 4
    changed.close()


def test_invalid_scores_are_not_cached(tmp_path):
    scorer = Scorer()
    cache = CachedPairScorer(scorer, tmp_path / "scores.sqlite", identity=IDENTITY)
    scorer.score = lambda query, texts: [float("nan")]
    with pytest.raises(ValueError, match="finite"):
        cache.score("q", ["aa"])
    assert cache.connection.execute("SELECT count(*) FROM scores").fetchone()[0] == 0
    cache.close()
    with pytest.raises(ValueError, match="pinned"):
        CachedPairScorer(
            scorer, tmp_path / "bad.sqlite", identity={**IDENTITY, "revision": "main"}
        )


def test_section_filters_before_candidate_cutoff_and_agent_trace():
    passages = load_passages(Path("tests/fixtures/mock_passages.jsonl"))
    sparse = BM25Retriever(passages)
    wrapped = SectionScopedRetriever(sparse.retrieve, passages)
    section = passages[2].section
    expected = [
        h.passage.passage_id
        for h in sparse.retrieve("lexical", passages[2].paper_id, 100)
        if h.passage.section == section
    ][:1]
    hybrid = HybridRetriever(wrapped, wrapped, candidate_k=1)
    hits = hybrid.retrieve("lexical", passages[2].paper_id, section=section)
    assert [h.passage.passage_id for h in hits] == expected
    assert all(h.passage.section == section for h in hits)
    assert hybrid.retrieve("lexical", passages[2].paper_id, section="absent") == []
    app = build_agent_graph(
        hybrid.retrieve, max_retries=0, section_selector=lambda state: section
    )
    result = app.invoke(AgentState(question="lexical", paper_id=passages[2].paper_id))
    log = result["retrieval_log"][0]
    assert log["section"] == section
    assert log["passage_ids"]
    assert "retrieved_passages" not in log
    json.dumps(log)


def test_hybrid_rejects_source_ignoring_section():
    passages = load_passages(Path("tests/fixtures/mock_passages.jsonl"))
    sparse = BM25Retriever(passages)

    def ignores(query, paper_id, top_k, **kwargs):
        return sparse.retrieve(query, paper_id, top_k)

    with pytest.raises(ValueError, match="outside section"):
        HybridRetriever(ignores, ignores).retrieve(
            "lexical", passages[0].paper_id, section="absent"
        )


def test_agent_cli_writes_serializable_round_provenance(tmp_path, monkeypatch):
    import sys

    from scripts import run_hybrid_agent

    passages = load_passages(Path("tests/fixtures/mock_passages.jsonl"))
    monkeypatch.setattr(
        run_hybrid_agent.DenseRetriever, "load", lambda *a, **k: BM25Retriever(passages)
    )
    monkeypatch.setattr(run_hybrid_agent, "_check_same_passages", lambda *a: None)
    output = tmp_path / "agent.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "agent",
            "--passages",
            "tests/fixtures/mock_passages.jsonl",
            "--dense-index-dir",
            str(tmp_path),
            "--query",
            "lexical",
            "--paper-id",
            passages[0].paper_id,
            "--output",
            str(output),
        ],
    )
    run_hybrid_agent.main()
    result = json.loads(output.read_text())
    assert result["retrieved_passages"]
    assert result["retrieved_passages"][0]["source_scores"]
    assert all("retrieved_passages" not in entry for entry in result["retrieval_log"])
    assert result["retrieval_log"][0]["retrieval_ms"] >= 0


def test_critic_gap_reaches_section_retry_without_classifier_override():
    from src.agent.export import export_record
    from src.agent.schemas import GapLabel

    passages = load_passages(Path("tests/fixtures/mock_passages.jsonl"))
    sparse = BM25Retriever(passages)
    scoped = SectionScopedRetriever(sparse.retrieve, passages)
    hybrid = HybridRetriever(scoped, scoped)
    selected = []

    class Critic:
        def __init__(self):
            self.calls = 0

        def complete(self, prompt):
            self.calls += 1
            if self.calls == 1:
                return json.dumps(
                    {
                        "sufficient": False,
                        "gap_label": "MISSING_EXPERIMENT_CONTEXT",
                        "missing_components": ["dataset setup"],
                        "reason": "Need setup details.",
                    }
                )
            return json.dumps(
                {
                    "sufficient": True,
                    "gap_label": "NONE",
                    "missing_components": [],
                    "reason": "Setup evidence is now present.",
                }
            )

    def selector(state):
        selected.append(state.gap_label)
        return (
            "methods"
            if state.gap_label == GapLabel.MISSING_EXPERIMENT_CONTEXT
            else None
        )

    critic = Critic()
    graph = build_agent_graph(
        hybrid.retrieve, critic_client=critic, section_selector=selector
    )
    assert "gap_classifier" not in graph.get_graph().nodes
    result = graph.invoke(
        AgentState(
            question="What accuracy did the model achieve?", paper_id="synthetic-ir"
        )
    )
    assert result["sufficient"] is True
    assert result["retrieval_round"] == 2
    assert selected == [GapLabel.NONE, GapLabel.MISSING_EXPERIMENT_CONTEXT]
    retry = result["retrieval_log"][1]
    assert retry["triggered_by"] == "MISSING_EXPERIMENT_CONTEXT"
    assert retry["section"] == "methods"
    assert retry["query"] != result["question"]
    assert retry["passage_ids"]
    record = export_record(result)
    assert record["retrieved_passages"][0]["passage"]["text"]
    assert all("retrieved_passages" not in entry for entry in record["retrieval_log"])
