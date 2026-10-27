import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from src.retrieval.fusion import reciprocal_rank_fusion
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import rerank
from src.retrieval.schemas import RetrievalHit


@pytest.fixture
def rankings():
    raw = json.loads(
        (Path(__file__).parent / "fixtures/mock_retrieval_results.json").read_text()
    )
    return {
        name: [RetrievalHit.model_validate(x) for x in raw[name]]
        for name in ("bm25", "dense")
    }


def test_rrf_math_and_raw_score_preservation(rankings):
    results = reciprocal_rank_fusion(rankings)
    assert results[0].passage.section == "results"
    assert results[0].rrf_score == pytest.approx(1 / 62 + 1 / 61)
    assert results[0].source_scores["bm25"].score == 9
    assert [r.rank for r in results] == [1, 2, 3]


def test_duplicate_only_contributes_once(rankings):
    expected = reciprocal_rank_fusion(rankings)
    rankings["bm25"].append(rankings["bm25"][0].model_copy(update={"rank": 4}))
    assert reciprocal_rank_fusion(rankings) == expected


def test_deterministic_ties(rankings):
    a, b = rankings["bm25"][:2]
    results = reciprocal_rank_fusion(
        {"x": [a], "y": [b.model_copy(update={"rank": 1})]}
    )
    assert [r.passage.passage_id for r in results] == sorted(
        [a.passage.passage_id, b.passage.passage_id]
    )


def test_conflicting_passage_rejected(rankings):
    hit = rankings["dense"][0]
    rankings["dense"][0] = hit.model_copy(
        update={"passage": hit.passage.model_copy(update={"text": "conflict"})}
    )
    with pytest.raises(ValueError, match="Conflicting content"):
        reciprocal_rank_fusion(rankings)


def test_duplicate_rank_rejected(rankings):
    rankings["bm25"][1] = rankings["bm25"][1].model_copy(update={"rank": 1})
    with pytest.raises(ValueError, match="Duplicate rank"):
        reciprocal_rank_fusion(rankings)


class FixedScorer:
    def __init__(self, scores):
        self.scores = scores

    def score(self, query, texts):
        return self.scores


def test_rerank_preserves_provenance_and_does_not_mutate(rankings):
    fused = reciprocal_rank_fusion(rankings)
    result = rerank("question", fused, FixedScorer([-2, 5, 1]), top_k=2)
    assert result[0].passage == fused[1].passage
    assert result[0].source_scores == fused[1].source_scores
    assert result[0].rrf_score == fused[1].rrf_score
    assert result[0].rank == 1
    assert result[0].reranker_score == 5
    assert all(r.reranker_score is None for r in fused)


@pytest.mark.parametrize("scores", [[1], [1, 2, float("nan")], [1, 2, float("inf")]])
def test_bad_scorer_rejected(rankings, scores):
    with pytest.raises(ValueError, match="finite score"):
        rerank("question", reciprocal_rank_fusion(rankings), FixedScorer(scores))


def test_empty_does_not_call_model():
    assert rerank("question", [], None) == []
    assert reciprocal_rank_fusion({}) == []


def test_hybrid_callback_and_serialization(rankings):
    calls = []

    def source(name):
        def callback(query, paper_id, top_k):
            calls.append((query, paper_id, top_k))
            return rankings[name]

        return callback

    hybrid = HybridRetriever(
        source("bm25"), source("dense"), scorer=FixedScorer([1, 2, 3])
    )
    results = hybrid.retrieve("question", "mock-paper", top_k=20)
    assert len(results) == 3
    assert calls == [("question", "mock-paper", 20)] * 2
    assert json.loads(results[0].model_dump_json())["rank"] == 1


def test_cross_paper_results_fail_closed(rankings):
    hybrid = HybridRetriever(lambda *args: rankings["bm25"], lambda *args: [])
    with pytest.raises(ValueError, match="another paper"):
        hybrid.retrieve("question", "other-paper")


@pytest.mark.parametrize("value", [0, -1, True, 1.5])
def test_invalid_top_k(rankings, value):
    with pytest.raises(ValueError):
        rerank(
            "question", reciprocal_rank_fusion(rankings), FixedScorer([]), top_k=value
        )


def test_schema_rejects_nonfinite_scores_and_invalid_ranks(rankings):
    data = rankings["bm25"][0].model_dump()
    for patch in [{"rank": 0}, {"score": float("inf")}, {"unexpected": 1}]:
        with pytest.raises(ValidationError):
            RetrievalHit.model_validate(data | patch)
