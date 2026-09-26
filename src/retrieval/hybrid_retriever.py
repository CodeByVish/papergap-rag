"""P2's callback-based retrieval API, usable before P1 is implemented."""

from typing import Protocol

from .fusion import reciprocal_rank_fusion
from .reranker import PairScorer, rerank
from .schemas import RetrievalHit, RetrievedPassage


class Retriever(Protocol):
    def __call__(self, query: str, paper_id: str, top_k: int) -> list[RetrievalHit]: ...


class HybridRetriever:
    def __init__(
        self,
        sparse: Retriever,
        dense: Retriever,
        *,
        scorer: PairScorer | None = None,
        candidate_k: int = 20,
        rrf_k: int = 60,
    ):
        for name, value in (("candidate_k", candidate_k), ("rrf_k", rrf_k)):
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        self.sparse, self.dense, self.scorer = sparse, dense, scorer
        self.candidate_k, self.rrf_k = candidate_k, rrf_k

    def retrieve(
        self, query: str, paper_id: str, top_k: int = 5
    ) -> list[RetrievedPassage]:
        if not query.strip() or not paper_id.strip():
            raise ValueError("query and paper_id must be nonempty")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer")
        rankings = {
            "bm25": self.sparse(query, paper_id, self.candidate_k),
            "dense": self.dense(query, paper_id, self.candidate_k),
        }
        for hits in rankings.values():
            if any(hit.passage.paper_id != paper_id for hit in hits):
                raise ValueError(
                    "Upstream retriever returned a passage from another paper"
                )
        fused = reciprocal_rank_fusion(rankings, rrf_k=self.rrf_k)
        if self.scorer is None:
            return fused[:top_k]
        return rerank(query, fused, self.scorer, top_k=top_k)
