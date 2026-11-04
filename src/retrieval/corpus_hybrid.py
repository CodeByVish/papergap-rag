"""Hybrid corpus search with an optional paper filter (v0-proposed)."""

from src.retrieval.fusion import reciprocal_rank_fusion
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import rerank


class CorpusHybridRetriever:
    """None selects all papers; a string retains P1/P2's paper-filter behavior."""

    def __init__(self, sparse, dense, *, scorer=None, candidate_k=20, rrf_k=60):
        self.sparse, self.dense, self.scorer = sparse, dense, scorer
        self.paper = HybridRetriever(
            sparse.retrieve,
            dense.retrieve,
            scorer=scorer,
            candidate_k=candidate_k,
            rrf_k=rrf_k,
        )
        self.candidate_k, self.rrf_k = candidate_k, rrf_k

    def retrieve(self, query, paper_id=None, top_k=5, *, section=None):
        if paper_id is not None:
            return self.paper.retrieve(query, paper_id, top_k, section=section)
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be positive")
        sources = {
            "bm25": self.sparse.retrieve_corpus(
                query, self.candidate_k, section=section
            ),
            "dense": self.dense.retrieve_corpus(
                query, self.candidate_k, section=section
            ),
        }
        fused = reciprocal_rank_fusion(sources, rrf_k=self.rrf_k)
        return (
            rerank(query, fused, self.scorer, top_k=top_k)
            if self.scorer
            else fused[:top_k]
        )
