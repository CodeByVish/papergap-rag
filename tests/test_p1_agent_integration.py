"""Controlled interface tests of real HybridRetriever and P4 graph wiring.

Synthetic P1-shaped candidates exercise control flow and provenance only. These
tests are not real-corpus retrieval or keyword-critic quality evidence.
"""

from functools import partial

from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState, GapLabel
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import Passage, RetrievalHit, RetrievedPassage

QUESTION = "Which result and method are reported?"
QUERIES = [
    QUESTION,
    f"{QUESTION} results experimental findings",
    f"{QUESTION} method approach architecture",
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
            section="Background",
            chunk_number=number,
            text=text,
        )
        for number, (name, paper_id, text) in enumerate(
            [
                ("shared", "paper-a", "Introductory background."),
                ("early", "paper-a", "Additional background."),
                ("unused", "paper-a", "Lower ranked background."),
                ("result", "paper-a", "A result is described here."),
                ("method", "paper-a", "A method is described here."),
                ("other", "paper-b", "A separate method is described here."),
            ]
        )
    }
    candidates = {
        ("paper-a", QUERIES[0]): ["shared", "early", "unused"],
        ("paper-a", QUERIES[1]): ["result", "shared", "unused"],
        ("paper-a", QUERIES[2]): ["method", "shared", "unused"],
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
    result = graph.invoke(AgentState(question=QUESTION, paper_id="paper-a"))

    assert result["sufficient"] is True
    assert result["retrieval_round"] == 3
    assert result["retrieval_round"] - 1 == 2
    assert [entry["query"] for entry in result["retrieval_log"]] == QUERIES
    assert [entry["triggered_by"] for entry in result["retrieval_log"]] == [
        "NONE",
        "MISSING_RESULT",
        "MISSING_METHOD",
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
    original = graph.invoke(AgentState(question=QUESTION, paper_id="paper-a"))
    other = graph.invoke(AgentState(question=OTHER_QUESTION, paper_id="paper-b"))

    assert other["retrieval_round"] == 1
    assert other["required_components"] == ["method"]
    assert other["sufficient"] is True
    assert other["gap_label"] == GapLabel.NONE
    assert other.get("rewritten_query") is None
    assert len(other["retrieved_passages"]) == 1 < rounds[3][2]
    assert other["retrieved_passages"][0].passage.paper_id == "paper-b"
    assert other["retrieval_log"] == [
        {
            "round": 1,
            "query": OTHER_QUESTION,
            "triggered_by": "NONE",
            "passage_ids": ["opaque:paper-b:other"],
        }
    ]

    empty = graph.invoke(AgentState(question=EMPTY_QUESTION, paper_id="empty-paper"))
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
        f"{EMPTY_QUESTION} baseline comparison outperform",
        f"{EMPTY_QUESTION} baseline comparison outperform",
    ]
    assert all(
        paper_id == "empty-paper" and not hits for _, paper_id, _, hits in rounds[4:]
    )
    assert all(not call[4] for call in source_calls[8:])

    repeated = graph.invoke(AgentState(question=QUESTION, paper_id="paper-a"))
    assert repeated == original
    assert rounds[7:] == rounds[:3]
    assert source_calls[14:] == source_calls[:6]
