"""Week-6 generation integration: reranked score provenance and LaTeX escapes.

The shared repo's generation module is a port of P5's standalone package, so the
same two defects the Week-6 BGE run exposed are pinned here:

* a reranked hit must be ordered by its reranker score, and a request that mixes
  reranker logits with RRF scores must not sort across the two scales;
* a raw LaTeX command in a JSON string (``\\extnormal``) is a format deviation,
  not a grounding failure, and must not throw the answer away.
"""

from __future__ import annotations

import hashlib

from src.generation.adapters import (
    SCORE_SOURCE_KEY,
    QasperHitAdapter,
    score_source,
)
from src.generation.generators.base import parse_response


def hashed(seed: str) -> str:
    return "qasper-passage-v1-" + hashlib.sha256(seed.encode()).hexdigest()


def nested(seed: str, *, reranker_score=None, rrf_score=0.03, rank=1) -> dict:
    return {
        "passage": {
            "passage_id": hashed(seed),
            "paper_id": "2405.04434",
            "title": "A paper",
            "section": "results",
            "chunk_number": rank,
            "text": f"Finding {seed}.",
        },
        "rank": rank,
        "source_scores": {},
        "rrf_score": rrf_score,
        "reranker_score": reranker_score,
    }


def test_reranker_score_is_preferred_and_recorded():
    passages, report = QasperHitAdapter().to_passages_reported(
        [nested("a", reranker_score=4.2), nested("b", reranker_score=-1.5)]
    )

    assert [p.score for p in passages] == [4.2, -1.5]
    assert [p.metadata[SCORE_SOURCE_KEY] for p in passages] == [
        "reranker",
        "reranker",
    ]
    assert report.mixed_score_records == 0


def test_a_mixed_score_request_keeps_the_retriever_order():
    passages, report = QasperHitAdapter().to_passages_reported(
        [
            nested("a", reranker_score=3.0, rank=1),
            nested("b", reranker_score=None, rrf_score=0.9, rank=2),
        ]
    )

    assert all(p.score is None for p in passages)
    assert [p.passage_id for p in passages] == [hashed("a"), hashed("b")]
    assert report.mixed_score_records == 1
    assert any("mixed retrieval score sources" in note for note in report.notes())


def test_score_source_names_the_field():
    assert score_source({"reranker_score": 1.0}) == "reranker"
    assert score_source({"rerank_score": 1.0}) == "reranker"
    assert score_source({"rrf_score": 0.03}) == "rrf"
    assert score_source({"score": 0.5}) == "native"
    assert score_source({}) == "unscored"


def test_a_raw_latex_escape_is_repaired_not_rejected():
    text = (
        r'{"answer": "The query $spouse(\extnormal{Angela Merkel}, ?)$ is '
        r'converted.", "citations": [], "evidence_status": "SUFFICIENT", '
        r'"retrieval_rounds": 1, "provenance": []}'
    )

    result, diagnostics = parse_response(text)

    assert r"\extnormal" in result.answer
    assert diagnostics.repaired_invalid_escapes
    assert diagnostics.invalid_escape_repairs == 1


def test_an_already_escaped_backslash_is_not_repaired_twice():
    text = (
        r'{"answer": "A \\extnormal command.", "citations": [], '
        r'"evidence_status": "SUFFICIENT", "retrieval_rounds": 1, '
        r'"provenance": []}'
    )

    result, diagnostics = parse_response(text)

    assert result.answer == r"A \extnormal command."
    assert not diagnostics.repaired_invalid_escapes
