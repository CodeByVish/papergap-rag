"""Controlled interface tests of real HybridRetriever and P4 graph wiring.

Synthetic P1-shaped candidates exercise control flow and provenance only. These
tests are not real-corpus retrieval or keyword-critic quality evidence.
"""

import json
import math
from copy import deepcopy
from functools import partial

import pytest

from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.agent_integration import TracedRequest, _without_retrieval_timing
from src.retrieval.experiment import DevelopmentQuestion
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import Passage, RetrievalHit, RetrievedPassage

QUESTION = "Which result and dataset are reported?"
QUERIES = [
    QUESTION,
    f"{QUESTION} results experimental findings accuracy score",
    f"{QUESTION} experimental setup evaluation metrics",
]
OTHER_QUESTION = "Which method is used?"
EMPTY_QUESTION = "Which baseline is used?"


def controlled_agent():
    """Return one reusable graph and observations at its P1/P2 boundaries."""
    passages = {
        name: Passage(
            passage_id=f"opaque:{paper_id}:{name}",
            paper_id=paper_id,
            title="Controlled interface fixture",
            section={
                "result": "Results",
                "context": "Experimental Setup",
                "other": "Methods",
            }.get(name, "Background"),
            chunk_number=number,
            text=text,
        )
        for number, (name, paper_id, text) in enumerate(
            [
                ("shared", "paper-a", "Introductory background."),
                ("early", "paper-a", "Additional background."),
                ("unused", "paper-a", "Lower ranked background."),
                ("result", "paper-a", "A result is described here."),
                ("context", "paper-a", "A dataset and setup are described here."),
                ("other", "paper-b", "A separate method is described here."),
            ]
        )
    }
    candidates = {
        ("paper-a", QUERIES[0]): ["shared", "early", "unused"],
        ("paper-a", QUERIES[1]): ["result", "shared", "unused"],
        ("paper-a", QUERIES[2]): ["context", "shared", "unused"],
        ("paper-b", OTHER_QUESTION): ["other"],
    }
    source_calls = []
    rounds = []

    def source_retrieve(source, query, paper_id, top_k):
        names = [] if paper_id == "empty-paper" else candidates[(paper_id, query)]
        # A repeated passage changes source rank/score on a retry, allowing the
        # test to distinguish keeping the first result from replacing it.
        offset = 100 if source == "dense" else 0
        hits = [
            RetrievalHit(passage=passages[name], rank=rank, score=offset + 10.0 / rank)
            for rank, name in enumerate(names[:top_k], start=1)
        ]
        source_calls.append((source, query, paper_id, top_k, hits))
        return hits

    hybrid = HybridRetriever(
        partial(source_retrieve, "bm25"),
        partial(source_retrieve, "dense"),
        candidate_k=3,
    )

    def retrieve(query, paper_id, top_k):
        hits = hybrid.retrieve(query, paper_id, top_k)
        rounds.append((query, paper_id, top_k, hits))
        return hits

    # Keep the actual default retry budget; only the per-round output is small.
    return build_agent_graph(retrieve, top_k=2), source_calls, rounds


def test_controlled_hybrid_agent_retries_preserve_queries_ids_and_first_hits():
    graph, source_calls, rounds = controlled_agent()
    result = graph.invoke(
        AgentState(question=QUESTION, paper_id="paper-a", question_id="controlled-main")
    )

    assert result["question_id"] == "controlled-main"
    assert result["required_components"] == ["result", "experiment_context"]
    assert result["sufficient"] is True
    assert result["retrieval_round"] == 3
    assert result["retrieval_round"] - 1 == 2
    assert [entry["query"] for entry in result["retrieval_log"]] == QUERIES
    assert [entry["triggered_by"] for entry in result["retrieval_log"]] == [
        "NONE",
        "MISSING_RESULT",
        "MISSING_EXPERIMENT_CONTEXT",
    ]
    assert [query for query, _, _, _ in rounds] == QUERIES
    assert [call[:4] for call in source_calls] == [
        (source, query, "paper-a", 3)
        for query in QUERIES
        for source in ("bm25", "dense")
    ]

    for index, (_, paper_id, top_k, hits) in enumerate(rounds):
        assert paper_id == "paper-a" and top_k == 2
        assert len(hits) == 2
        assert [hit.rank for hit in hits] == [1, 2]
        assert all(isinstance(hit, RetrievedPassage) for hit in hits)
        log = result["retrieval_log"][index]
        assert log["round"] == index + 1
        assert log["passage_ids"] == [hit.passage.passage_id for hit in hits]
        assert log["section"] is None
        assert math.isfinite(log["retrieval_ms"]) and log["retrieval_ms"] >= 0
        assert [hit.rrf_score for hit in hits] == pytest.approx(
            [2 / (60 + rank) for rank in (1, 2)]
        )
        for source, _, _, _, candidates in source_calls[2 * index : 2 * index + 2]:
            assert len(candidates) == 3
            for hit, candidate in zip(hits, candidates):
                assert hit.passage == candidate.passage
                assert hit.passage.paper_id == paper_id
                assert set(hit.source_scores) == {"bm25", "dense"}
                assert hit.source_scores[source].rank == candidate.rank
                assert hit.source_scores[source].score == candidate.score

    first_shared = rounds[0][3][0]
    repeated_shared = rounds[1][3][1]
    assert first_shared.passage.passage_id == repeated_shared.passage.passage_id
    assert first_shared.source_scores != repeated_shared.source_scores
    assert result["retrieved_passages"] == [
        first_shared,
        rounds[0][3][1],
        rounds[1][3][0],
        rounds[2][3][0],
    ]
    ids = [hit.passage.passage_id for hit in result["retrieved_passages"]]
    assert len(ids) == len(set(ids)) == 4 > rounds[0][2]


def test_controlled_hybrid_agent_reuse_and_empty_retry_budget_are_independent():
    graph, source_calls, rounds = controlled_agent()
    initial = AgentState(
        question=QUESTION, paper_id="paper-a", question_id="controlled-main"
    )
    original = graph.invoke(initial)
    other = graph.invoke(
        AgentState(
            question=OTHER_QUESTION, paper_id="paper-b", question_id="controlled-other"
        )
    )

    assert other["question_id"] == "controlled-other"
    assert other["retrieval_round"] == 1
    assert other["required_components"] == ["method"]
    assert other["sufficient"] is True
    assert other["gap_label"] == GapLabel.NONE
    assert other.get("rewritten_query") is None
    assert len(other["retrieved_passages"]) == 1 < rounds[3][2]
    assert other["retrieved_passages"][0].passage.paper_id == "paper-b"
    assert _without_retrieval_timing(other)["retrieval_log"] == [
        {
            "round": 1,
            "query": OTHER_QUESTION,
            "triggered_by": "NONE",
            "passage_ids": ["opaque:paper-b:other"],
            "section": None,
        }
    ]

    empty = graph.invoke(
        AgentState(
            question=EMPTY_QUESTION,
            paper_id="empty-paper",
            question_id="controlled-empty",
        )
    )
    assert empty["question_id"] == "controlled-empty"
    assert empty["retrieval_round"] == 3
    assert empty["retrieval_round"] - 1 == 2
    assert empty["sufficient"] is False
    assert empty["required_components"] == ["comparison"]
    assert empty["retrieved_passages"] == []
    assert empty["evidence_map"] == {"comparison": []}
    assert [entry["round"] for entry in empty["retrieval_log"]] == [1, 2, 3]
    assert all(entry["passage_ids"] == [] for entry in empty["retrieval_log"])
    assert [query for query, _, _, _ in rounds[4:]] == [
        EMPTY_QUESTION,
        f"{EMPTY_QUESTION} comparison state-of-the-art outperform",
        f"{EMPTY_QUESTION} comparison state-of-the-art outperform",
    ]
    assert all(
        paper_id == "empty-paper" and not hits for _, paper_id, _, hits in rounds[4:]
    )
    assert all(not call[4] for call in source_calls[8:])

    repeated = graph.invoke(initial)
    assert _without_retrieval_timing(repeated) == _without_retrieval_timing(original)
    for state in (original, other, empty, repeated):
        assert all(
            math.isfinite(entry["retrieval_ms"]) and entry["retrieval_ms"] >= 0
            for entry in state["retrieval_log"]
        )
    assert rounds[7:] == rounds[:3]
    assert source_calls[14:] == source_calls[:6]


def synthetic_traced_request():
    """Use the real tracer, fusion and graph without loading models or indexes."""
    passage = Passage(
        passage_id="opaque:paper-a:background",
        paper_id="paper-a",
        title="Synthetic tracer fixture",
        section="Background",
        chunk_number=0,
        text="Introductory background.",
    )
    calls = []

    class Backend:
        def __init__(self, source):
            self.source = source

        def retrieve(self, query, paper_id, top_k, *, section):
            calls.append((self.source, query, paper_id, top_k, section))
            if paper_id != passage.paper_id or section != passage.section:
                return []
            score = 1.0 if self.source == "bm25" else 2.0
            return [RetrievalHit(passage=passage, rank=1, score=score)]

    request = TracedRequest(
        Backend("bm25"),
        Backend("dense"),
        [passage],
        section="Background",
        top_k=2,
        candidate_k=3,
    )
    return request, calls


def test_traced_request_preserves_ids_budget_scope_and_reuse():
    request, calls = synthetic_traced_request()
    question = DevelopmentQuestion("traced-main", "paper-a", QUESTION)
    first = request.invoke(question, "first")
    empty = request.invoke(
        DevelopmentQuestion("traced-empty", "empty-paper", EMPTY_QUESTION), "empty"
    )
    repeated = request.invoke(question, "repeated")

    assert first["retry_count"] == empty["retry_count"] == repeated["retry_count"] == 2
    assert first["agent_state"]["sufficient"] is False
    assert first["agent_state"]["gap_label"] == "MISSING_RESULT"
    assert first["input"]["question_id"] == "traced-main"
    assert first["agent_state"]["question_id"] == "traced-main"
    assert empty["agent_state"]["question_id"] == "traced-empty"
    assert empty["accumulated"] == []
    assert len(first["accumulated"]) == 1
    assert first["accumulated"] == first["rounds"][0]["returned"]
    assert first["accumulated"][0]["rrf_score"] == pytest.approx(2 / 61)
    for case in (first, empty, repeated):
        assert len(case["rounds"]) == 3
        assert case["candidate_k"] == 3 and case["top_k"] == 2
        for trace, log in zip(case["rounds"], case["agent_state"]["retrieval_log"]):
            assert trace["section"] == "Background"
            assert trace["query"] == log["query"]
            assert all(
                source["section"] == "Background" and source["requested_k"] == 3
                for source in trace["sources"].values()
            )
    assert [call[:2] for call in calls[:6]] == [
        (source, trace["query"])
        for trace in first["rounds"]
        for source in ("bm25", "dense")
    ]
    assert calls[12:] == calls[:6]
    assert {
        **first,
        "case": "repeated",
        "agent_state": _without_retrieval_timing(first["agent_state"]),
    } == {
        **repeated,
        "agent_state": _without_retrieval_timing(repeated["agent_state"]),
    }


def test_traced_request_accepts_insufficient_information_early_stop():
    request, calls = synthetic_traced_request()

    class CannotAnswerCritic:
        def complete(self, prompt):
            return json.dumps(
                {
                    "sufficient": False,
                    "gap_label": "INSUFFICIENT_INFORMATION",
                    "missing_components": [],
                    "reason": "The synthetic paper does not answer the question.",
                }
            )

    request.graph = build_agent_graph(
        request.retrieve, top_k=request.top_k, critic_client=CannotAnswerCritic()
    )
    case = request.invoke(
        DevelopmentQuestion("traced-unanswerable", "paper-a", QUESTION), "early-stop"
    )

    assert case["retry_count"] == 0
    assert len(case["rounds"]) == 1 and len(calls) == 2
    assert case["agent_state"]["question_id"] == "traced-unanswerable"
    assert case["agent_state"]["gap_label"] == "INSUFFICIENT_INFORMATION"
    assert case["agent_state"]["sufficient"] is False
    assert case["agent_state"]["rewritten_query"] is None
    assert case["agent_state"]["critic_log"][0]["source"] == "llm"


def test_state_comparison_ignores_only_timing_without_mutating_the_trace():
    request, _ = synthetic_traced_request()
    state = request.invoke(
        DevelopmentQuestion("traced-main", "paper-a", QUESTION), "timing"
    )["agent_state"]
    different_timing = deepcopy(state)
    for entry in different_timing["retrieval_log"]:
        entry["retrieval_ms"] += 10
    expected = deepcopy(state)

    assert _without_retrieval_timing(state) == _without_retrieval_timing(
        different_timing
    )
    assert state == expected
    for field, value in (
        ("query", "changed query"),
        ("section", "changed section"),
        ("passage_ids", ["changed passage"]),
    ):
        changed = deepcopy(state)
        changed["retrieval_log"][0][field] = value
        assert _without_retrieval_timing(state) != _without_retrieval_timing(changed)
    changed = {**state, "question_id": "changed question"}
    assert _without_retrieval_timing(state) != _without_retrieval_timing(changed)
