"""Query P1 indexes through P2 fusion: python -m scripts.demo_hybrid --help."""

import argparse
import json
import time
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION, load_passages, revision_sha
from scripts.demo_p1 import _check_same_passages
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker

RERANKER_REVISION = "2cfc18c9415c912f9d8155881c133215df768a70"


def run_hybrid(
    passages_path: Path,
    dense_index_dir: Path,
    query: str,
    paper_id: str,
    *,
    top_k: int = 5,
    candidate_k: int = 20,
    rrf_k: int = 60,
    bge: bool = False,
    revision: str = PINNED_REVISION,
    reranker_revision: str = RERANKER_REVISION,
    device: str = "cpu",
    cache_folder: Path | None = None,
    local_files_only: bool = False,
) -> dict:
    """Warm up once, then record one full retrieval call and source counts.

    Construction and warm-up are excluded from timing. This is a wiring and
    latency smoke check, not a quality evaluation or a latency distribution.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a nonempty string")
    if not isinstance(paper_id, str) or not paper_id.strip():
        raise ValueError("paper_id must be a nonempty string")
    for name, value in (
        ("top_k", top_k),
        ("candidate_k", candidate_k),
        ("rrf_k", rrf_k),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    passages = load_passages(passages_path)
    sparse = BM25Retriever(passages)
    dense = DenseRetriever.load(
        dense_index_dir,
        model_name=DEFAULT_MODEL_NAME,
        revision=revision,
        device=device,
        cache_folder=cache_folder,
        local_files_only=local_files_only,
    )
    _check_same_passages(dense_index_dir, passages)
    source_ids = {}

    def counted(name, retrieve):
        def callback(query, paper_id, top_k):
            hits = retrieve(query, paper_id, top_k)
            source_ids[name] = {hit.passage.passage_id for hit in hits}
            return hits

        return callback

    scorer = (
        BGEReranker(
            revision=reranker_revision,
            device=device,
            cache_folder=str(cache_folder) if cache_folder is not None else None,
            local_files_only=local_files_only,
        )
        if bge
        else None
    )
    backend = HybridRetriever(
        counted("bm25", sparse.retrieve),
        counted("dense", dense.retrieve),
        scorer=scorer,
        candidate_k=candidate_k,
        rrf_k=rrf_k,
    )
    backend.retrieve(query, paper_id, top_k)
    started = time.perf_counter()
    hits = backend.retrieve(query, paper_id, top_k)
    elapsed_ms = (time.perf_counter() - started) * 1000
    return {
        "query": query,
        "paper_id": paper_id,
        "passages_path": str(Path(passages_path).resolve()),
        "dense_index_dir": str(Path(dense_index_dir).resolve()),
        "dense_model": DEFAULT_MODEL_NAME,
        "dense_revision": revision,
        "reranker_model": "BAAI/bge-reranker-base" if bge else None,
        "reranker_revision": reranker_revision if bge else None,
        "device": device,
        "candidate_k_per_source": candidate_k,
        "candidate_counts": {name: len(ids) for name, ids in source_ids.items()},
        "unique_candidates": len(set().union(*source_ids.values())),
        "rrf_k": rrf_k,
        "top_k": top_k,
        "retrieval_ms": elapsed_ms,
        "timing_policy": "One call after one warm-up; excludes index/model loading.",
        "results": [hit.model_dump() for hit in hits],
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--dense-index-dir", type=Path, required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--candidate-k", type=int, default=20)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument("--bge", action="store_true")
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument(
        "--reranker-revision", type=revision_sha, default=RERANKER_REVISION
    )
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--cache-folder", type=Path)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--output", type=Path)
    args = vars(parser.parse_args(argv))
    output = args.pop("output")
    args["passages_path"] = args.pop("passages")
    try:
        rendered = json.dumps(run_hybrid(**args), indent=2) + "\n"
        if output is not None:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered, encoding="utf-8")
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    print(rendered)


if __name__ == "__main__":
    main()
