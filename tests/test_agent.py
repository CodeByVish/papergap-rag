"""Unit tests for the P4 LangGraph agent, driven by P2-shaped retrieval results."""

import json
from pathlib import Path

import pytest

from src.agent.graph import build_agent_graph
from src.agent.nodes import MAX_ROUNDS
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import RetrievalHit, RetrievedPassage

FIXTURES = Path(__file__).parent / "fixtures"
QUESTION = "What accuracy did the model achieve?"
PAPER_ID = "mock-paper"
RESULTS_ID = "mock-paper_results_0"


@pytest.fixture(scope="module")
def all_hits() -> list[RetrievedPassage]:
    raw = json.loads((FIXTURES / "mock_reranked_results.json").read_text())
    return [RetrievedPassage.model_validate(item) for item in raw["results"]]


@pytest.fixture
def without_results(all_hits):
    return [h for h in all_hits if h.passage.section != "results"]


def initial_state() -> AgentState:
    return AgentState(question=QUESTION, paper_id=PAPER_ID)


def test_agent_state_defaults():
    state = initial_state()
    assert state.retrieval_round == 0
    assert state.sufficient is False
    assert state.gap_label == GapLabel.NONE
    assert state.retrieved_passages == []
    assert state.retrieval_log == []


def test_gap_label_includes_week4_labels():
    expected = {
        "MISSING_METHOD",
        "MISSING_EXPERIMENT_CONTEXT",
        "MISSING_RESULT",
        "MISSING_COMPARISON",
        "TERMINOLOGY_MISMATCH",
        "WEAK_EVIDENCE",
        "INSUFFICIENT_INFORMATION",
    }
    assert expected.issubset({label.value for label in GapLabel})


def test_sufficient_on_first_round(all_hits):
    app = build_agent_graph(lambda query, paper_id, top_k: all_hits)
    result = app.invoke(initial_state())

    assert result["sufficient"] is True
    assert result["retrieval_round"] == 1
    assert result["gap_label"] == GapLabel.NONE
    assert RESULTS_ID in result["evidence_map"]["result"]


def test_recovers_after_one_retry_with_rewritten_query(all_hits, without_results):
    calls = []

    def retriever(query, paper_id, top_k):
        calls.append(query)
        return all_hits if "results" in query.lower() else without_results

    result = build_agent_graph(retriever).invoke(initial_state())

    assert result["sufficient"] is True
    assert result["retrieval_round"] == 2
    assert RESULTS_ID in result["evidence_map"]["result"]
    assert calls[0] == QUESTION
    assert calls[1].startswith(QUESTION) and "results" in calls[1]
    assert [e["round"] for e in result["retrieval_log"]] == [1, 2]
    assert result["retrieval_log"][0]["triggered_by"] == "NONE"
    assert result["retrieval_log"][1]["triggered_by"] == "MISSING_RESULT"


def test_exhausts_retries_and_hands_off_insufficient(without_results):
    app = build_agent_graph(lambda query, paper_id, top_k: without_results)
    result = app.invoke(initial_state())

    assert result["sufficient"] is False
    assert result["retrieval_round"] == MAX_ROUNDS
    assert result["evidence_map"]["result"] == []
    assert result["gap_label"] == GapLabel.MISSING_RESULT
    assert len(result["retrieval_log"]) == MAX_ROUNDS


def test_empty_retrieval_retries_then_stops():
    calls = []

    def empty(query, paper_id, top_k):
        calls.append(query)
        return []

    result = build_agent_graph(empty).invoke(initial_state())

    assert len(calls) == MAX_ROUNDS
    assert result["sufficient"] is False
    assert result["retrieved_passages"] == []
    assert all(not ids for ids in result["evidence_map"].values())


def test_passages_deduplicated_across_rounds(all_hits, without_results):
    def retriever(query, paper_id, top_k):
        return all_hits if "results" in query.lower() else without_results

    result = build_agent_graph(retriever).invoke(initial_state())

    ids = [h.passage.passage_id for h in result["retrieved_passages"]]
    assert len(ids) == len(set(ids)) == len(all_hits)


def test_max_retries_zero_runs_single_round(without_results):
    calls = []

    def retriever(query, paper_id, top_k):
        calls.append(query)
        return without_results

    result = build_agent_graph(retriever, max_retries=0).invoke(initial_state())

    assert len(calls) == 1
    assert result["retrieval_round"] == 1
    assert result["sufficient"] is False


def test_negative_max_retries_rejected():
    with pytest.raises(ValueError):
        build_agent_graph(lambda query, paper_id, top_k: [], max_retries=-1)


def test_top_k_is_forwarded(all_hits):
    seen = []

    def retriever(query, paper_id, top_k):
        seen.append((paper_id, top_k))
        return all_hits

    build_agent_graph(retriever, top_k=3).invoke(initial_state())
    assert seen == [(PAPER_ID, 3)]


def test_works_with_real_hybrid_retriever():
    raw = json.loads((FIXTURES / "mock_retrieval_results.json").read_text())
    rankings = {
        name: [RetrievalHit.model_validate(x) for x in raw[name]]
        for name in ("bm25", "dense")
    }
    hybrid = HybridRetriever(
        lambda query, paper_id, top_k: rankings["bm25"][:top_k],
        lambda query, paper_id, top_k: rankings["dense"][:top_k],
    )

    result = build_agent_graph(hybrid.retrieve).invoke(initial_state())

    assert result["sufficient"] is True
    assert result["retrieval_round"] == 1
    assert all(isinstance(h, RetrievedPassage) for h in result["retrieved_passages"])
    assert set(result["retrieved_passages"][0].source_scores) == {"bm25", "dense"}
