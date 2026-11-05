#!/usr/bin/env python3
"""P5-side load check for P1's live-retrieval package (2026-10-31).

P5 promised P2 an on-cluster integration test after P1's corpus, indexes and
pinned embedding model arrived. This script is that test: it loads the corpus,
checks P1's saved BM25 snapshot and the from-passages rebuild the demo uses,
restores P1's per-paper FAISS indexes through ``DenseRetriever.load``, runs one
hybrid query, and feeds the hits through the same adapter the demo server uses.

It is deliberately **not** the demo's retriever factory. ``src/retrieval/demo.py``
belongs to P2/P4; nothing here should be imported by the server.

Run it from the P5 checkout while the importable shared code lives elsewhere::

    python scripts/check_p1_retrieval.py --repo ~/papergap-rag

or from the shared checkout itself (``--repo`` defaults to the current working
directory). Use the interpreter that will host the demo server - the vLLM venv -
because a missing ``faiss`` / ``sentence-transformers`` / ``rank-bm25`` there is
the finding, not a reason to switch interpreters.

Exit codes: 0 = loaded and retrieved; 1 = a check failed (traceback printed);
2 = the interpreter is missing a package the demo process would need.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import traceback
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

# P1's manifest (2026-10-31) records the environment it verified on. These are
# reported, not enforced: the cluster venv is a different lock, and only exact
# mismatches that change load behaviour (rank-bm25) are called out as a failure.
P1_VERSIONS = {
    "numpy": "2.4.6",
    "rank-bm25": "0.2.2",
    "faiss-cpu": "1.15.1",
    "sentence-transformers": "5.7.0",
    "transformers": "4.57.6",
    "torch": "2.14.0",
}

P1_CORPUS_SHA256 = (
    "abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790"
)
P1_PASSAGES = 32_073
P1_PAPERS = 1_168
P1_DENSE_FILES = 1_168
P1_MODEL = "BAAI/bge-small-en-v1.5"
P1_REVISION = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"

# The question P1's README uses, on a paper whose index is nonempty.
DEFAULT_QUESTION = "How are discourse relations used to learn affective events?"
DEFAULT_PAPER = "1909.00694"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_versions() -> dict[str, str]:
    found: dict[str, str] = {}
    for name in P1_VERSIONS:
        try:
            found[name] = version(name)
        except PackageNotFoundError:
            found[name] = "missing"
    return found


def load_passages(path: Path, passage_model: Any) -> list[Any]:
    """Read P1's UTF-8 JSONL with the shared Passage model.

    The model is ``extra="forbid"``, so this also proves the corpus carries
    exactly the fields P2's retriever declares and nothing P1 forgot to mention.
    """
    passages: list[Any] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                passage = passage_model.model_validate_json(line)
            except Exception as exc:  # pydantic ValidationError, JSONDecodeError
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
            if passage.passage_id in seen:
                raise ValueError(f"{path}:{line_number}: duplicate passage_id")
            seen.add(passage.passage_id)
            passages.append(passage)
    return passages


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    root = Path(os.environ.get("P5_ROOT", Path.home() / "p5"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path.cwd(),
        help="checkout whose src/retrieval and src/generation are imported",
    )
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path(os.environ.get("PAPERGAP_CORPUS", root / "data/corpus/passages.jsonl")),
    )
    parser.add_argument(
        "--dense",
        type=Path,
        default=Path(
            os.environ.get(
                "PAPERGAP_DENSE_INDEX", root / "data/indexes/dense-bge-small"
            )
        ),
    )
    parser.add_argument(
        "--bm25",
        type=Path,
        default=Path(
            os.environ.get("PAPERGAP_BM25_INDEX", root / "data/indexes/bm25")
        ),
    )
    parser.add_argument(
        "--hf-home",
        type=Path,
        default=Path(os.environ.get("HF_HOME", root / "hf")),
        help="HF cache root; must contain models--BAAI--bge-small-en-v1.5",
    )
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument("--paper", default=DEFAULT_PAPER)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--candidate-k", type=int, default=20)
    parser.add_argument("--rrf-k", type=int, default=60)
    parser.add_argument(
        "--allow-download",
        action="store_true",
        help="do not set HF_HUB_OFFLINE/TRANSFORMERS_OFFLINE (default: offline)",
    )
    parser.add_argument(
        "--expect-corpus-sha256",
        default=P1_CORPUS_SHA256,
        help="empty string disables the corpus hash check",
    )
    parser.add_argument(
        "--expect-passages",
        type=int,
        default=P1_PASSAGES,
        help="expected passage count (default: the 200/40 package, 32073)",
    )
    parser.add_argument(
        "--expect-papers",
        type=int,
        default=P1_PAPERS,
        help="expected paper count (default: the 200/40 package, 1168)",
    )
    parser.add_argument(
        "--expect-dense-files",
        type=int,
        default=P1_DENSE_FILES,
        help="expected per-paper FAISS files (default: 1168)",
    )
    return parser.parse_args(argv)


def configure_hf(args: argparse.Namespace) -> None:
    """Set HF_HOME before transformers is imported; it is read at import time."""
    os.environ["HF_HOME"] = str(args.hf_home)
    if not args.allow_download:
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"


def check_paths(args: argparse.Namespace) -> dict[str, Any]:
    facts: dict[str, Any] = {}
    for label, path in (
        ("corpus", args.corpus),
        ("dense", args.dense / "metadata.json"),
        ("hf_home", args.hf_home),
    ):
        if not path.exists():
            raise FileNotFoundError(f"{label} missing: {path}")
    # The 2026-10-31 package shipped a saved BM25 snapshot; the 2026-11-02
    # 365/40 package does not, because the demo rebuilds BM25 from the corpus.
    # A missing snapshot is reported below, never fatal.
    faiss_files = sorted(args.dense.glob("paper-*.faiss"))
    facts["dense_faiss_files"] = len(faiss_files)
    if len(faiss_files) != args.expect_dense_files:
        raise ValueError(
            f"{args.dense}: expected {args.expect_dense_files} per-paper FAISS "
            f"files, found {len(faiss_files)}"
        )
    if args.expect_corpus_sha256:
        digest = sha256_file(args.corpus)
        if digest != args.expect_corpus_sha256:
            raise ValueError(
                f"{args.corpus}: sha256 {digest} != {args.expect_corpus_sha256}"
            )
        facts["corpus_sha256"] = digest
    return facts


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    configure_hf(args)

    repo = args.repo.resolve()
    if not (repo / "src" / "retrieval").is_dir():
        print(
            f"error: {repo} has no src/retrieval; pass --repo <papergap-rag checkout>",
            file=sys.stderr,
        )
        return 2
    sys.path.insert(0, str(repo))

    versions = package_versions()
    print("versions:", json.dumps(versions, sort_keys=True), file=sys.stderr)
    missing = [name for name, value in versions.items() if value == "missing"]
    if missing:
        print(
            "error: the interpreter that will host the demo server is missing "
            + ", ".join(missing)
            + ". Install P2's retrieval dependencies into that venv; do not "
            "switch interpreters, because the demo process imports the factory "
            "in-process.",
            file=sys.stderr,
        )
        return 2

    try:
        from src.retrieval.bm25_retriever import BM25Retriever
        from src.retrieval.dense_retriever import DenseRetriever
        from src.retrieval.hybrid_retriever import HybridRetriever
        from src.retrieval.schemas import Passage
    except ImportError:
        traceback.print_exc()
        return 2

    report: dict[str, Any] = {
        "repo": str(repo),
        "corpus": str(args.corpus),
        "dense": str(args.dense),
        "bm25": str(args.bm25),
        "hf_home": str(args.hf_home),
        "versions": versions,
        "expectations": {
            "passages": args.expect_passages,
            "papers": args.expect_papers,
            "dense_faiss_files": args.expect_dense_files,
            "corpus_sha256": args.expect_corpus_sha256 or "(not checked)",
        },
        "version_mismatches": {
            name: {"expected": expected, "found": versions[name]}
            for name, expected in P1_VERSIONS.items()
            if versions[name] != expected
        },
    }

    try:
        report.update(check_paths(args))

        started = time.perf_counter()
        passages = load_passages(args.corpus, Passage)
        report["timings_s"] = {"load_passages": round(time.perf_counter() - started, 3)}
        papers = {passage.paper_id for passage in passages}
        report["corpus_counts"] = {"passages": len(passages), "papers": len(papers)}
        if len(passages) != args.expect_passages or len(papers) != args.expect_papers:
            raise ValueError(
                f"corpus counts {len(passages)}/{len(papers)} != "
                f"{args.expect_passages}/{args.expect_papers}"
            )
        if args.paper not in papers:
            raise ValueError(f"paper {args.paper!r} has no passages in the corpus")

        # The demo's agent path (scripts/demo_agent_factory.py ->
        # run_agent_experiment.build_retriever) rebuilds BM25 from passages.
        # P1 also shipped a saved BM25 snapshot; ``main``'s BM25Retriever.load()
        # reads it. Do both, and compare their top-k, so the report says whether
        # the snapshot is usable rather than only that rebuilding works.
        started = time.perf_counter()
        bm25 = BM25Retriever(passages)
        report["timings_s"]["build_bm25"] = round(time.perf_counter() - started, 3)
        bm25_report: dict[str, Any] = {
            "demo_path": "build-from-passages",
            "saved_metadata_present": (args.bm25 / "metadata.json").is_file(),
        }
        load_method = getattr(BM25Retriever, "load", None)
        if load_method is None:
            bm25_report["load"] = (
                "unavailable: this checkout has no BM25Retriever.load(); "
                "origin/main has it"
            )
        elif not bm25_report["saved_metadata_present"]:
            bm25_report["load"] = "skipped: metadata.json is missing"
        else:
            try:
                started = time.perf_counter()
                loaded = load_method(args.bm25)
                bm25_report["load"] = "passed"
                bm25_report["load_seconds"] = round(
                    time.perf_counter() - started, 3
                )
                built_ids = [
                    hit.passage.passage_id
                    for hit in bm25.retrieve(args.question, args.paper, args.top_k)
                ]
                loaded_ids = [
                    hit.passage.passage_id
                    for hit in loaded.retrieve(args.question, args.paper, args.top_k)
                ]
                bm25_report["load_matches_rebuild"] = built_ids == loaded_ids
            except Exception as exc:  # report, then keep testing the demo path
                bm25_report["load"] = f"failed: {type(exc).__name__}: {exc}"
        report["bm25_loader"] = bm25_report

        started = time.perf_counter()
        dense = DenseRetriever.load(
            args.dense,
            model_name=P1_MODEL,
            revision=P1_REVISION,
            device="cpu",
            cache_folder=args.hf_home,
            local_files_only=not args.allow_download,
        )
        report["timings_s"]["load_dense"] = round(time.perf_counter() - started, 3)

        hybrid = HybridRetriever(
            bm25.retrieve,
            dense.retrieve,
            candidate_k=args.candidate_k,
            rrf_k=args.rrf_k,
        )
        started = time.perf_counter()
        hits = hybrid.retrieve(args.question, args.paper, args.top_k)
        report["timings_s"]["hybrid_query"] = round(time.perf_counter() - started, 3)
        if not hits:
            raise ValueError(
                f"hybrid retrieval returned no hits for {args.paper!r}; "
                "the question/paper pair or the fusion config is wrong"
            )
        report["query"] = {
            "question": args.question,
            "paper_id": args.paper,
            "top_k": args.top_k,
            "hits": [
                {
                    "rank": hit.rank,
                    "passage_id": hit.passage.passage_id,
                    "rrf_score": round(hit.rrf_score, 6),
                    "text_chars": len(hit.passage.text),
                }
                for hit in hits
            ],
        }

        # The demo server wraps plain hits into a one-round record with this
        # adapter, so exercise P5's side of the contract on the same payload.
        from src.generation.adapters.retrieval import build_request

        adapted = build_request(
            {
                "question": args.question,
                "paper_id": args.paper,
                "retrieval_rounds": 1,
                "retrieved_passages": hits,
            }
        )
        report["adapter"] = {
            "passages": len(adapted.request.passages),
            "notes": adapted.notes,
        }
        if len(adapted.request.passages) != len(hits):
            raise ValueError(
                f"adapter kept {len(adapted.request.passages)} of {len(hits)} hits"
            )
        report["status"] = "passed"
    except Exception:
        traceback.print_exc()
        report["status"] = "failed"
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 1

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
