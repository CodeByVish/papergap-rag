"""Reciprocal Rank Fusion with deterministic passage-ID deduplication."""

from collections.abc import Mapping, Sequence

from .schemas import RetrievalHit, RetrievedPassage, SourceScore


def reciprocal_rank_fusion(
    rankings: Mapping[str, Sequence[RetrievalHit]], *, rrf_k: int = 60
) -> list[RetrievedPassage]:
    """Sum 1/(rrf_k + rank) once per source and passage.

    Duplicate IDs within a source use their best original rank. Conflicting
    content or equal ranks for different passages are invalid upstream data.
    """
    if isinstance(rrf_k, bool) or not isinstance(rrf_k, int) or rrf_k < 1:
        raise ValueError("rrf_k must be a positive integer")
    passages = {}
    scores: dict[str, dict[str, SourceScore]] = {}
    for source in sorted(rankings):
        if not source:
            raise ValueError("source names must be nonempty")
        ranks = {}
        for hit in rankings[source]:
            pid = hit.passage.passage_id
            if pid in passages and passages[pid] != hit.passage:
                raise ValueError(f"Conflicting content for passage {pid}")
            if hit.rank in ranks and ranks[hit.rank] != pid:
                raise ValueError(f"Duplicate rank in {source}: {hit.rank}")
            ranks[hit.rank] = pid
            passages[pid] = hit.passage
            source_scores = scores.setdefault(pid, {})
            old = source_scores.get(source)
            if old is not None and old.rank == hit.rank and old.score != hit.score:
                raise ValueError(f"Conflicting score for {pid} in {source}")
            if old is None or hit.rank < old.rank:
                source_scores[source] = SourceScore(rank=hit.rank, score=hit.score)
    totals = {
        pid: sum(1 / (rrf_k + item.rank) for item in sources.values())
        for pid, sources in scores.items()
    }
    ordered = sorted(totals, key=lambda pid: (-totals[pid], pid))
    return [
        RetrievedPassage(
            passage=passages[pid],
            rank=rank,
            source_scores=scores[pid],
            rrf_score=totals[pid],
        )
        for rank, pid in enumerate(ordered, 1)
    ]
