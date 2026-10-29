"""BM25 retrieval over the passages of one selected paper."""

import json
import math
import re
from collections.abc import Iterable
from importlib.metadata import version
from pathlib import Path

from rank_bm25 import BM25Okapi

from .schemas import Passage, RetrievalHit

_INDEX_SETTINGS = {
    "format_version": 1,
    "index_type": "BM25Okapi",
    "tokenization": "unicode-word-regex-casefold-v1",
    "token_pattern": r"\w+",
    "k1": 1.5,
    "b": 0.75,
    "epsilon": 0.25,
}


def _tokenize(text: str) -> list[str]:
    """Use the same case-insensitive word tokens for passages and queries."""
    return re.findall(_INDEX_SETTINGS["token_pattern"], text.casefold())


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
            self._indexes[paper_id] = (
                BM25Okapi(
                    tokens,
                    k1=_INDEX_SETTINGS["k1"],
                    b=_INDEX_SETTINGS["b"],
                    epsilon=_INDEX_SETTINGS["epsilon"],
                )
                if any(tokens)
                else None
            )

    def retrieve(
        self, query: str, paper_id: str, top_k: int, *, section: str | None = None
    ) -> list[RetrievalHit]:
        """Return at most top_k passages from paper_id, with one-based ranks.

        Raw BM25 scores may be zero or negative. All available passages remain
        eligible, including those with no matching terms. Ties use passage ID.
        An optional exact section match restricts candidates before top-k; BM25
        statistics still come from the selected whole paper. Unknown papers or
        sections return []; invalid arguments raise ValueError. A caller may
        supply a rewritten query directly; no query rewriting occurs here.
        """
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be a nonempty string")
        if not isinstance(paper_id, str) or not paper_id.strip():
            raise ValueError("paper_id must be a nonempty string")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer")
        if section is not None and (
            not isinstance(section, str) or not section.strip()
        ):
            raise ValueError("section must be a nonempty string or None")

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
            (
                (passage, score)
                for passage, score in zip(paper_passages, scores)
                if section is None or passage.section == section
            ),
            key=lambda item: (-item[1], item[0].passage_id),
        )
        return [
            RetrievalHit(passage=passage, rank=rank, score=score)
            for rank, (passage, score) in enumerate(ordered[:top_k], start=1)
        ]

    def save(self, directory: str | Path) -> None:
        """Save complete passages and reproducible BM25 settings as JSON.

        Only new or empty directories are accepted. No pickle or private
        rank_bm25 state is persisted; load() rebuilds the in-memory term index.
        """
        directory = Path(directory)
        if directory.exists() and (not directory.is_dir() or any(directory.iterdir())):
            raise ValueError("Save directory must be new or empty")
        directory.mkdir(parents=True, exist_ok=True)
        metadata = {
            **_INDEX_SETTINGS,
            "rank_bm25_version": version("rank-bm25"),
            "papers": [
                {
                    "paper_id": paper_id,
                    "passages": [p.model_dump() for p in self._passages[paper_id]],
                }
                for paper_id in sorted(self._passages)
            ],
        }
        (directory / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    @classmethod
    def load(cls, directory: str | Path) -> "BM25Retriever":
        """Validate saved settings and passages, then rebuild the BM25 index.

        This intentionally tokenizes the saved text again. It is a portable JSON
        snapshot, not a serialized rank_bm25 object or a zero-rebuild cache.
        """
        metadata = json.loads(
            (Path(directory) / "metadata.json").read_text(encoding="utf-8")
        )
        if not isinstance(metadata, dict):
            raise ValueError("BM25 metadata must be an object")  # noqa: TRY004
        expected_settings = {
            **_INDEX_SETTINGS,
            "rank_bm25_version": version("rank-bm25"),
        }
        for key, expected in expected_settings.items():
            if (
                type(metadata.get(key)) is not type(expected)
                or metadata[key] != expected
            ):
                raise ValueError(f"Incompatible BM25 metadata: {key}")
        papers = metadata.get("papers")
        if not isinstance(papers, list):
            raise ValueError("Missing or invalid BM25 papers metadata")  # noqa: TRY004
        passages = []
        seen_papers: set[str] = set()
        seen_ids: set[str] = set()
        for paper in papers:
            if not isinstance(paper, dict):
                raise ValueError("Invalid BM25 paper mapping")  # noqa: TRY004
            paper_id = paper.get("paper_id")
            if not isinstance(paper_id, str) or not paper_id.strip():
                raise ValueError("Invalid paper_id in BM25 mapping")
            if paper_id in seen_papers:
                raise ValueError("Duplicate paper_id in BM25 mapping")
            seen_papers.add(paper_id)
            raw_passages = paper.get("passages")
            if not isinstance(raw_passages, list) or not raw_passages:
                raise ValueError("Each BM25 paper requires a nonempty Passage mapping")
            paper_passages = [Passage.model_validate(raw) for raw in raw_passages]
            for passage in paper_passages:
                if passage.paper_id != paper_id:
                    raise ValueError("Passage belongs to another paper in BM25 mapping")
                if passage.passage_id in seen_ids:
                    raise ValueError("Duplicate passage_id in BM25 mapping")
                seen_ids.add(passage.passage_id)
            if paper_passages != sorted(
                paper_passages, key=lambda passage: passage.passage_id
            ):
                raise ValueError("BM25 Passage mapping is not in canonical row order")
            passages.extend(paper_passages)
        return cls(passages)
