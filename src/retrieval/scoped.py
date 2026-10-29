"""Exact section scope for existing three-argument P1 callbacks."""

from collections import Counter

from .schemas import RetrievalHit


class SectionScopedRetriever:
    """Filter the complete paper ranking before selecting section candidates.

    The corpus must match the underlying retriever's indexed passages. This
    adapter works with the merged P1 callbacks without requiring their pending
    native section-filter PR. It retains whole-paper BM25 statistics.
    """

    def __init__(self, retrieve, passages):
        self.retrieve = retrieve
        self.counts = Counter(p.paper_id for p in passages)

    def __call__(self, query, paper_id, top_k, *, section=None):
        if section is None:
            return self.retrieve(query, paper_id, top_k)
        if not isinstance(section, str) or not section.strip():
            raise ValueError("section must be a nonempty string or None")
        hits = self.retrieve(query, paper_id, max(1, self.counts.get(paper_id, 0)))
        eligible = [h for h in hits if h.passage.section == section]
        return [
            RetrievalHit(passage=h.passage, score=h.score, rank=i)
            for i, h in enumerate(eligible[:top_k], 1)
        ]
