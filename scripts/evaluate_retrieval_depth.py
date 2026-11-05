"""Gold recall of plain retrieval at several depths: the static baseline, tuned fairly.

The adaptive loop is only worth its critic calls if it beats a static run that simply
reads as many passages. This reports, on development items with P3 gold passages,
recall@k of the question used as the query (no critic, no retry), and the least any
stopping rule could read (`oracle`). Run it with `--bge` on the cluster to include
P2's reranker; the CPU run needs no GPU:

    python -m scripts.evaluate_retrieval_depth \\
        --passages passages_p3.jsonl --dense-index-dir indexes/dense-bge-small \\
        --items items.jsonl --ks 3 5 8 10 15 --out-json depth.json

Only development questions should be passed; never tune on held-out labels.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.experiments import depth_curve  # noqa: E402


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("--passages", type=Path, required=True)
    p.add_argument("--dense-index-dir", type=Path, required=True)
    p.add_argument("--items", type=Path, required=True, help="JSONL of question items with gold")
    p.add_argument("--ks", type=int, nargs="+", default=[3, 5, 8, 10, 15])
    p.add_argument("--candidate-k", type=int, default=20)
    p.add_argument("--bge", action="store_true", help="add the BGE reranker")
    p.add_argument("--score-cache", type=Path, help="persistent reranker score cache (SQLite)")
    p.add_argument("--device", default="cpu")
    p.add_argument("--cache-folder", type=Path, default=ROOT / ".cache/huggingface/hub")
    p.add_argument("--local-files-only", action="store_true")
    p.add_argument("--out-json", type=Path, help="also write the table as JSON")
    args = p.parse_args(argv)
    if max(args.ks) > args.candidate_k:
        p.error(f"--ks reaches {max(args.ks)} but --candidate-k is {args.candidate_k}")
    args.scoped = False  # the plain question is searched over the whole paper
    return args


def format_curve(curve: dict) -> str:
    rows = ["| depth | mean recall | questions with full recall |", "| ---: | ---: | ---: |"]
    for k, recall in curve["recall_at_k"].items():
        rows.append(f"| {k} | {recall:.3f} | {curve['full_recall_at_k'][k]}/{curve['questions_with_gold']} |")
    oracle = curve["oracle"]
    rows.append(f"\noracle stop: {oracle['mean_passages']:.2f} passages on average, "
                f"recall {oracle['mean_recall']:.3f}")
    return "\n".join(rows)


def main(argv: Sequence[str] | None = None) -> None:
    from scripts.build_indexes import load_passages
    from scripts.run_agent_experiment import build_retriever, load_items_jsonl

    args = parse_args(argv)
    passages = load_passages(args.passages)
    items = load_items_jsonl(args.items)
    curve = depth_curve(items, build_retriever(args, passages), args.ks)
    print(format_curve(curve))
    if args.out_json:
        args.out_json.write_text(json.dumps(curve, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
