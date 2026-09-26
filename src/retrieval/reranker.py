"""BGE cross-encoder scoring; model loading happens only on first use."""

import math
from collections.abc import Sequence
from typing import Protocol

from .schemas import RetrievedPassage


class PairScorer(Protocol):
    def score(self, query: str, texts: Sequence[str]) -> Sequence[float]: ...


class BGEReranker:
    def __init__(
        self,
        *,
        model_name: str = "BAAI/bge-reranker-base",
        revision: str | None = None,
        device: str = "cpu",
        batch_size: int = 8,
        max_length: int = 512,
    ):
        if batch_size < 1 or not 1 <= max_length <= 512:
            raise ValueError("batch_size must be positive; max_length must be 1..512")
        self.model_name, self.revision, self.device = model_name, revision, device
        self.batch_size, self.max_length = batch_size, max_length
        self._tokenizer = self._model = None

    def score(self, query: str, texts: Sequence[str]) -> list[float]:
        if not texts:
            return []
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer

        if self._model is None:
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_name, revision=self.revision
            )
            self._model = AutoModelForSequenceClassification.from_pretrained(
                self.model_name, revision=self.revision
            ).to(self.device)
            self._model.eval()
        scores = []
        with torch.inference_mode():
            for start in range(0, len(texts), self.batch_size):
                pairs = [
                    [query, text] for text in texts[start : start + self.batch_size]
                ]
                tokens = self._tokenizer(
                    pairs,
                    padding=True,
                    truncation=True,
                    max_length=self.max_length,
                    return_tensors="pt",
                )
                tokens = {key: value.to(self.device) for key, value in tokens.items()}
                logits = self._model(**tokens).logits
                if logits.shape != (len(pairs), 1):
                    raise ValueError(
                        "Expected one relevance logit per query–passage pair"
                    )
                scores.extend(logits[:, 0].float().cpu().tolist())
        return scores


def rerank(
    query: str,
    candidates: Sequence[RetrievedPassage],
    scorer: PairScorer,
    *,
    top_k: int = 5,
) -> list[RetrievedPassage]:
    if not query.strip():
        raise ValueError("query must be nonempty")
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    if not candidates:
        return []
    if len({c.passage.passage_id for c in candidates}) != len(candidates):
        raise ValueError("Reranker candidates must have unique passage IDs")
    scores = list(scorer.score(query, [c.passage.text for c in candidates]))
    if len(scores) != len(candidates) or not all(math.isfinite(s) for s in scores):
        raise ValueError("Scorer must return one finite score per candidate")
    ordered = sorted(
        zip(candidates, scores),
        key=lambda item: (-item[1], -item[0].rrf_score, item[0].passage.passage_id),
    )
    return [
        candidate.model_copy(update={"rank": rank, "reranker_score": float(score)})
        for rank, (candidate, score) in enumerate(ordered[:top_k], 1)
    ]
