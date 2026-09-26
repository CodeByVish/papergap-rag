"""BM25 retrieval over the passages of one selected paper."""

import math
import re
from collections.abc import Iterable

from rank_bm25 import BM25Okapi

from .schemas import Passage, RetrievalHit


def _tokenize(text: str) -> list[str]:
    """Use the same case-insensitive word tokens for passages and queries."""
    return re.findall(r"\w+", text.casefold())


class BM25Retriever:
    """Build independent in-memory BM25 indexes for each paper.

    Passages retain their original IDs and metadata. Duplicate IDs are rejected
    across the entire input. Pass ``retriever.retrieve`` as P2's sparse callback.
    """

    def __init__(self, passages: Iterable[Passage]) -> None:
        self._passages: dict[str, list[Passage]] = {}
        self._indexes: dict[str, BM25Okapi | None] = {}
        seen_ids: set[str] = set()
        for passage in passages:
            if passage.passage_id in seen_ids:
                raise ValueError(f"Duplicate passage_id: {passage.passage_id}")
            seen_ids.add(passage.passage_id)
            self._passages.setdefault(passage.paper_id, []).append(passage)

        for paper_id, paper_passages in self._passages.items():
            paper_passages.sort(key=lambda passage: passage.passage_id)
            tokens = [_tokenize(passage.text) for passage in paper_passages]
            # BM25Okapi divides by zero when the entire vocabulary is empty.
            # Such a paper has no lexical evidence, so all its scores are zero.
            self._indexes[paper_id] = BM25Okapi(tokens) if any(tokens) else None

    def retrieve(
        self, query: str, paper_id: str, top_k: int
    ) -> list[RetrievalHit]:
        """Return at most top_k passages from paper_id, with one-based ranks.

        Raw BM25 scores may be zero or negative. All available passages remain
        eligible, including those with no matching terms. Ties use passage ID.
        Unknown papers return []; invalid arguments raise ValueError.
        """
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a nonempty string")
        if not isinstance(paper_id, str) or not paper_id.strip():
            raise ValueError("paper_id must be a nonempty string")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer")

        paper_passages = self._passages.get(paper_id)
        if not paper_passages:
            return []

        index = self._indexes[paper_id]
        scores = (
            [float(score) for score in index.get_scores(_tokenize(query))]
            if index is not None
            else [0.0] * len(paper_passages)
        )
        if not all(math.isfinite(score) for score in scores):
            raise ValueError("BM25 must return finite scores")

        ordered = sorted(
            zip(paper_passages, scores),
            key=lambda item: (-item[1], item[0].passage_id),
        )
        return [
            RetrievalHit(passage=passage, rank=rank, score=score)
            for rank, (passage, score) in enumerate(ordered[:top_k], start=1)
        ]
