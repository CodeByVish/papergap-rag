"""Adapt fixed P1/P2 retrieval contracts to chunk-size experiments.

Configuration validation and metadata stay lightweight. Heavy dependencies are
imported only inside the selected factory path; provenance spans never enter an
index. Each factory call builds fresh paper-scoped indexes for its own corpus.
"""

from __future__ import annotations

import importlib.metadata
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from src.data.schemas import Passage as DataPassage

ROOT = Path(__file__).resolve().parents[2]
SOURCE_COMMIT = "5ccfb070a00f71dd2f95f69afb31868c296f35c4"
DENSE_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
RERANKER_REVISION = "2cfc18c9415c912f9d8155881c133215df768a70"
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "
PUBLIC_FIELDS = (
    "passage_id",
    "paper_id",
    "title",
    "section",
    "chunk_number",
    "text",
    "previous_passage_id",
    "next_passage_id",
)
Retriever = Callable[[str, str, int], list[tuple[str, float]]]
RetrieverFactory = Callable[[list[dict[str, Any]]], Retriever]


def _object(value: Any, allowed: set[str], label: str) -> dict:
    """Reject null, non-object and unknown configuration fields.

    Returns the original object for validation without mutating supplied values.
    """
    if not isinstance(value, dict) or set(value) - allowed:
        raise ValueError(f"{label} must be an object with known keys")
    return value


def normalize_retrieval(supplied: Any, top_k: int = 5) -> dict[str, Any]:
    """Validate all settings and resolve cache paths against the project root.

    Unused model sections are still checked. Defaults are merged by section,
    and no model is imported, loaded or downloaded during validation.
    """
    supplied = _object(
        supplied, {"mode", "candidate_k", "rrf_k", "dense", "reranker"}, "retrieval"
    )
    config = {"mode": "bm25", "candidate_k": 20, "rrf_k": 60, **supplied}
    if config["mode"] not in ("bm25", "dense", "hybrid", "hybrid_rerank"):
        raise ValueError("retrieval.mode must be bm25, dense, hybrid or hybrid_rerank")
    for key in ("candidate_k", "rrf_k"):
        if type(config[key]) is not int or config[key] < 1:
            raise ValueError(f"retrieval.{key} must be a positive integer")
    if config["mode"] in ("hybrid", "hybrid_rerank") and config["candidate_k"] < top_k:
        raise ValueError(
            "retrieval.candidate_k must be at least top_k for hybrid modes"
        )
    for kind, revision, batch in (
        ("dense", DENSE_REVISION, 32),
        ("reranker", RERANKER_REVISION, 8),
    ):
        defaults = {
            "revision": revision,
            "device": "cpu",
            "batch_size": batch,
            "cache_folder": ".cache/huggingface",
            "local_files_only": True,
        }
        if kind == "reranker":
            defaults["max_length"] = 512
        overrides = _object(supplied.get(kind, {}), set(defaults), f"retrieval.{kind}")
        settings = {**defaults, **overrides}
        if not isinstance(settings["revision"], str) or not re.fullmatch(
            r"[0-9a-f]{40}", settings["revision"]
        ):
            raise ValueError(
                f"retrieval.{kind}.revision must be a 40-character lowercase SHA"
            )
        if type(settings["batch_size"]) is not int or settings["batch_size"] < 1:
            raise ValueError(f"retrieval.{kind}.batch_size must be a positive integer")
        if type(settings["local_files_only"]) is not bool:
            raise ValueError(f"retrieval.{kind}.local_files_only must be boolean")
        for key in ("device", "cache_folder"):
            if not isinstance(settings[key], str) or not settings[key].strip():
                raise ValueError(f"retrieval.{kind}.{key} must be a nonempty string")
        if kind == "reranker" and (
            type(settings["max_length"]) is not int
            or not 1 <= settings["max_length"] <= 512
        ):
            raise ValueError(
                "retrieval.reranker.max_length must be an integer in 1..512"
            )
        settings["cache_folder"] = str((ROOT / settings["cache_folder"]).resolve())
        config[kind] = settings
    return config


def project_passages(records: list[dict[str, Any]]) -> list:
    """Validate eight public fields before constructing retrieval models.

    Private spans and other evaluation fields stay in the caller's records.
    IDs and full text are never normalized or regenerated at this boundary.
    """
    from src.retrieval.schemas import Passage as RetrievalPassage

    return [
        RetrievalPassage(
            **DataPassage.model_validate(
                {key: record[key] for key in PUBLIC_FIELDS}
            ).model_dump()
        )
        for record in records
    ]


def scored_ids(hits: list) -> list[tuple[str, float]]:
    """Convert P1/P2 scores while preserving the upstream ranking.

    Zero and negative reranker logits are valid. Only None falls back to RRF.
    """
    result = []
    for hit in hits:
        if hasattr(hit, "score"):
            score = hit.score
        else:
            score = (
                hit.reranker_score if hit.reranker_score is not None else hit.rrf_score
            )
        result.append((hit.passage.passage_id, float(score)))
    return result


def _runtime_error(mode: str, error: Exception) -> RuntimeError:
    """Explain dependency, model-cache and device failures without fallback.

    The original exception is retained by the caller as the cause for diagnosis.
    """
    return RuntimeError(
        f"{mode} retrieval failed: {error}. Check requirements-dev.txt, the configured "
        "device and the exact model revision in cache_folder. Offline loading is "
        "the default; prepare weights separately or explicitly set local_files_only=false. "
        "No fallback was used."
    )


def make_retriever_factory(settings: dict[str, Any]) -> RetrieverFactory:
    """Create a configured factory without importing optional model libraries.

    The returned factory builds one independent candidate index per invocation.
    Query closures own those indexes and release them when discarded by runner.
    """
    config = normalize_retrieval(settings)
    mode = config["mode"]

    def factory(records: list[dict[str, Any]]) -> Retriever:
        """Project a candidate corpus and construct only active components.

        Model initialization and passage encoding occur within factory timing.
        """
        passages = project_passages(records)
        try:
            if mode != "dense":
                from src.retrieval.bm25_retriever import BM25Retriever

                sparse = BM25Retriever(passages)
            if mode != "bm25":
                from src.retrieval.dense_retriever import DenseRetriever

                dense = DenseRetriever(passages, **config["dense"])
            if mode == "bm25":
                backend = sparse
            elif mode == "dense":
                backend = dense
            else:
                from src.retrieval.hybrid_retriever import HybridRetriever

                scorer = None
                if mode == "hybrid_rerank":
                    from src.retrieval.reranker import BGEReranker

                    scorer = BGEReranker(**config["reranker"])
                backend = HybridRetriever(
                    sparse.retrieve,
                    dense.retrieve,
                    scorer=scorer,
                    candidate_k=config["candidate_k"],
                    rrf_k=config["rrf_k"],
                )
        except (ImportError, OSError, RuntimeError, ValueError) as error:
            raise _runtime_error(mode, error) from error

        def retrieve(query: str, paper_id: str, top_k: int) -> list[tuple[str, float]]:
            """Retrieve ordered IDs using only question text and paper scope.

            Lazy BGE loading is part of the first scoring call, without warm-up.
            """
            try:
                return scored_ids(backend.retrieve(query, paper_id, top_k))
            except (ImportError, OSError, RuntimeError, ValueError) as error:
                raise _runtime_error(mode, error) from error

        return retrieve

    return factory


def retriever_metadata(settings: dict[str, Any]) -> dict[str, Any]:
    """Describe active implementations and effective inference parameters.

    These are configured identities, not a claim that weights or truncation
    have been independently verified. Disabled components are explicitly marked.
    """
    config = normalize_retrieval(settings)
    mode = config["mode"]
    packages = (
        ["rank-bm25"]
        if mode == "bm25"
        else ["numpy", "faiss-cpu", "sentence-transformers", "torch", "transformers"]
    )
    if mode.startswith("hybrid"):
        packages.append("rank-bm25")
    if mode == "hybrid_rerank":
        packages.append("sentencepiece")
    versions = {}
    for package in packages:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    metadata = {
        "id": "p1-p2-static-retrieval",
        "mode": mode,
        "source_commit": SOURCE_COMMIT,
        "packages": versions,
        "scope": "selected paper",
        "persistent_score_cache": False,
        "score": {
            "bm25": "raw BM25",
            "dense": "cosine",
            "hybrid": "RRF",
            "hybrid_rerank": "raw reranker logit",
        }[mode],
        "tie_break": "passage_id ascending; reranker ties first use RRF descending",
        "bm25": {"enabled": mode != "dense"},
        "dense": {"enabled": mode != "bm25"},
        "reranker": {"enabled": mode == "hybrid_rerank"},
    }
    if mode != "dense":
        metadata["bm25"].update(
            tokenizer="casefold + Unicode word runs", k1=1.5, b=0.75, epsilon=0.25
        )
    if mode != "bm25":
        metadata["dense"].update(
            {
                **config["dense"],
                "model_name": "BAAI/bge-small-en-v1.5",
                "tokenizer_revision": config["dense"]["revision"],
                "query_instruction": QUERY_INSTRUCTION,
                "max_seq_length": 512,
                "normalization": "l2",
                "similarity_metric": "cosine",
                "index_type": "IndexFlatIP",
                "truncation": "single text at 512 tokens; full chunk retained for reports",
                "truncation_observation": "not verified with real tokenizer",
            }
        )
    if mode.startswith("hybrid"):
        metadata.update(
            candidate_k_per_source=config["candidate_k"],
            rrf_k=config["rrf_k"],
            final_top_k=5,
            rerank_all_fused_candidates=mode == "hybrid_rerank",
        )
    if mode == "hybrid_rerank":
        metadata["reranker"].update(
            {
                **config["reranker"],
                "model_name": "BAAI/bge-reranker-base",
                "tokenizer_revision": config["reranker"]["revision"],
                "padding": True,
                "truncation": True,
                "raw_logits": True,
                "length_limit": "query-passage pair; full chunk retained for reports",
                "truncation_observation": "not verified with real tokenizer",
            }
        )
    return metadata
