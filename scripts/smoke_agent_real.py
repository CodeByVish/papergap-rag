"""Smoke test: run the agent on real P1/P2 retrieval over QASPER training papers.

Prerequisites (see docs/P2_WEEK2.md): the corpus subset and its dense index, e.g.

    python -m scripts.prepare_p2_pilot ...
    OMP_NUM_THREADS=1 python -m scripts.build_indexes \
        --passages data/processed/p2-training-pilot-passages.jsonl \
        --output-dir indexes/p2-training-pilot --cache-folder .cache/huggingface/hub

Usage (single thread avoids the duplicate-OpenMP crash on macOS when FAISS and
PyTorch are both loaded):

    OMP_NUM_THREADS=1 python -m scripts.smoke_agent_real

Runs the static and adaptive systems with no LLM (the adaptive critic is
rule-based), prints a trace per question, and saves records under results/.
Only training questions are read. Gold passages are an approximation made for
this smoke test (see `approximate_gold`), not P3's evidence mapping.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_indexes import PINNED_REVISION, load_passages
from scripts.demo_hybrid import RERANKER_REVISION
from scripts.demo_p1 import _check_same_passages
from src.agent.experiments import (
    ExperimentItem,
    compute_metrics,
    format_table,
    paired_recall_gain,
    run_system,
)
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.reranker import BGEReranker
from src.retrieval.schemas import Passage


def _squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def approximate_gold(evidence: list[str], passages: list[Passage]) -> frozenset[str]:
    """Passages that contain an annotated evidence paragraph, or lie inside one.

    Whitespace and case are ignored. Evidence that is a table or figure ("FLOAT
    SELECTED") is skipped, and a paragraph split across chunks may be missed.
    """
    found: set[str] = set()
    squashed = [(p.passage_id, _squash(p.text)) for p in passages]
    for paragraph in evidence:
        if paragraph.startswith("FLOAT SELECTED"):
            continue
        target = _squash(paragraph)
        if len(target) < 40:
            continue
        found.update(pid for pid, text in squashed if target in text or text in target)
    return frozenset(found)


def load_items(qa_path: Path, passages: list[Passage]) -> list[ExperimentItem]:
    by_paper: dict[str, list[Passage]] = {}
    for passage in passages:
        by_paper.setdefault(passage.paper_id, []).append(passage)
    items = []
    with qa_path.open(encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            if row["source_split"] != "train" or row["paper_id"] not in by_paper:
                continue
            answers = [a["answer"] for a in row["answers"]]
            evidence = [e for a in answers for e in a["evidence"]]
            answerable = not all(a["unanswerable"] for a in answers)
            gold = approximate_gold(evidence, by_paper[row["paper_id"]]) if answerable else None
            items.append(
                ExperimentItem(
                    question_id=row["question_id"],
                    question=row["question"],
                    paper_id=row["paper_id"],
                    gold_passage_ids=gold or None,
                    answerable=answerable,
                )
            )
    return sorted(items, key=lambda item: (item.paper_id, item.question_id))


def build_retriever(args: argparse.Namespace, passages: list[Passage]):
    _check_same_passages(args.dense_index_dir, passages)
    sparse = BM25Retriever(passages)
    dense = DenseRetriever.load(
        args.dense_index_dir,
        model_name=DEFAULT_MODEL_NAME,
        revision=PINNED_REVISION,
        device="cpu",
        cache_folder=args.cache_folder,
        local_files_only=args.local_files_only,
    )
    scorer = (
        BGEReranker(
            revision=RERANKER_REVISION,
            cache_folder=str(args.cache_folder),
            local_files_only=args.local_files_only,
        )
        if args.bge
        else None
    )
    return HybridRetriever(
        sparse.retrieve, dense.retrieve, scorer=scorer, candidate_k=args.candidate_k
    ).retrieve


def print_trace(record: dict, item: ExperimentItem) -> None:
    print(f"\n[{record['question_id'][:8]}] {item.question}")
    if "error" in record:
        print("  ERROR:", record["error"])
        return
    for entry, critic in zip(record["retrieval_log"], record["critic_log"], strict=False):
        print(
            f"  round {entry['round']} query={entry['query']!r}\n"
            f"    -> {len(entry['passage_ids'])} passages; critic={critic['source']} "
            f"sufficient={critic['sufficient']} gap={critic['gap_label']}"
        )
    sections = sorted({p["passage"]["section"] for p in record["retrieved_passages"]})
    print(f"  final: sufficient={record['sufficient']} sections={sections}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path,
                        default=ROOT / "data/processed/p2-training-pilot-passages.jsonl")
    parser.add_argument("--qa", type=Path, default=ROOT / "data/processed/qa.jsonl")
    parser.add_argument("--dense-index-dir", type=Path,
                        default=ROOT / "indexes/p2-training-pilot")
    parser.add_argument("--cache-folder", type=Path, default=ROOT / ".cache/huggingface/hub")
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--bge", action="store_true", help="add the BGE reranker")
    parser.add_argument("--candidate-k", type=int, default=20)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--output", type=Path, default=ROOT / "results/p4-smoke-real.json")
    args = parser.parse_args()

    passages = load_passages(args.passages)
    items = load_items(args.qa, passages)
    with_gold = sum(1 for item in items if item.gold_passage_ids)
    print(f"{len(passages)} passages, {len(items)} train questions, "
          f"{with_gold} with approximate gold passages")

    retriever = build_retriever(args, passages)
    retriever(items[0].question, items[0].paper_id, args.top_k)  # warm up models before timing
    static = run_system(items, retriever, adaptive=False, top_k=args.top_k)
    adaptive = run_system(items, retriever, adaptive=True, top_k=args.top_k)

    by_id = {item.question_id: item for item in items}
    for record in adaptive:
        print_trace(record, by_id[record["question_id"]])

    results = {"static": compute_metrics(static, items), "adaptive": compute_metrics(adaptive, items)}
    print("\n" + format_table(results))
    print("\npaired recall gain (adaptive - static):", paired_recall_gain(static, adaptive, items))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps({"static": static, "adaptive": adaptive, "metrics": results}, indent=2),
        encoding="utf-8",
    )
    print(f"\nsaved {args.output}")


if __name__ == "__main__":
    main()
