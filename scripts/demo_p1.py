"""Query the independent P1 retrievers: python -m scripts.demo_p1 --help."""

import argparse
import json
import time
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION, load_passages, revision_sha
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.schemas import Passage, RetrievalHit


def _check_same_passages(directory: Path, passages: list[Passage]) -> None:
    """Keep the two independently queried retrievers on the same corpus."""
    metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
    saved = {}
    for paper in metadata["papers"]:
        for raw in paper["passages"]:
            passage = Passage.model_validate(raw)
            saved[passage.passage_id] = passage
    if saved != {passage.passage_id: passage for passage in passages}:
        raise ValueError(
            "Dense index passages do not match the input JSONL; rebuild the index"
        )


def _print_results(name: str, results: list[RetrievalHit], elapsed_ms: float) -> None:
    print(f"\n{name} results:")
    if not results:
        print("(no passages for this paper)")
    for hit in results:
        preview = " ".join(hit.passage.text.split())
        if len(preview) > 140:
            preview = preview[:137] + "..."
        print(
            f"rank={hit.rank} passage_id={hit.passage.passage_id} "
            f"score={hit.score:.6f} section={hit.passage.section!r} "
            f"text={preview!r}"
        )
    print(f"{name} retrieval latency: {elapsed_ms:.3f} ms")


def run_demo(
    passages_path: str | Path,
    paper_id: str,
    query: str,
    top_k: int = 3,
    *,
    dense_index_dir: str | Path | None = None,
    revision: str = PINNED_REVISION,
    device: str = "cpu",
    cache_folder: str | Path | None = None,
    local_files_only: bool = False,
) -> None:
    """Print one query per retriever after an untimed warm-up of each backend."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a nonempty string")
    if not isinstance(paper_id, str) or not paper_id.strip():
        raise ValueError("paper_id must be a nonempty string")
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
        raise ValueError("top_k must be a positive integer")
    passages = load_passages(passages_path)
    bm25 = BM25Retriever(passages)
    if dense_index_dir is None:
        dense = DenseRetriever(
            passages,
            revision=revision,
            device=device,
            cache_folder=cache_folder,
            local_files_only=local_files_only,
        )
    else:
        dense_index_dir = Path(dense_index_dir)
        dense = DenseRetriever.load(
            dense_index_dir,
            model_name=DEFAULT_MODEL_NAME,
            revision=revision,
            device=device,
            cache_folder=cache_folder,
            local_files_only=local_files_only,
        )
        _check_same_passages(dense_index_dir, passages)

    # Query warm-up also loads a lazy SentenceTransformer after index reload.
    # Neither construction/loading nor these warm-ups enter the measured calls.
    bm25.retrieve(query, paper_id, top_k)
    dense.retrieve(query, paper_id, top_k)
    started = time.perf_counter()
    sparse_hits = bm25.retrieve(query, paper_id, top_k)
    sparse_ms = (time.perf_counter() - started) * 1000
    started = time.perf_counter()
    dense_hits = dense.retrieve(query, paper_id, top_k)
    dense_ms = (time.perf_counter() - started) * 1000

    fixture = Path(__file__).resolve().parents[1] / "tests/fixtures/mock_passages.jsonl"
    synthetic = Path(passages_path).resolve() == fixture
    corpus_label = "synthetic passages" if synthetic else "input passages"
    print(
        f"Corpus: {len(passages)} {corpus_label}, "
        f"{len({passage.paper_id for passage in passages})} papers"
    )
    print(f"Paper: {paper_id}\nQuery: {query}")
    print(
        f"Timing: one retrieve() call per backend after one warm-up each; "
        f"device={device}. Model loading and index construction are excluded."
    )
    if synthetic:
        print("Synthetic-data timing only; not representative of the real P3 corpus.")
    else:
        print("A single timing sample, not a corpus performance benchmark.")
    _print_results("BM25", sparse_hits, sparse_ms)
    _print_results("Dense", dense_hits, dense_ms)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--dense-index-dir", type=Path)
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--cache-folder", type=Path)
    parser.add_argument("--local-files-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        run_demo(
            args.passages,
            args.paper_id,
            args.query,
            args.top_k,
            dense_index_dir=args.dense_index_dir,
            revision=args.revision,
            device=args.device,
            cache_folder=args.cache_folder,
            local_files_only=args.local_files_only,
        )
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
