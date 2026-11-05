"""Write the held-out run's input: P3's frozen question list, reduced to question, id and paper.

    python -m scripts.make_held_out_items \
        --questions data/processed/qa_for_held_out_v2.jsonl \
        --freeze configs/p4_freeze.json --out runs/p4/held_out_items.jsonl

The protocol (docs/EVALUATION.md) says to record the final commit and configuration before any
held-out question is read. This script is where that is enforced: it does not open the list unless
`configs/p4_freeze.json` is frozen (status, time, commit, hashes), the frozen commit exists
in this repository and the list is byte-identical to the one the record names. The output carries only
`question_id`, `question` and `paper_id`: no answer, no gold, no split. Existing outputs are refused.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.protocol import FreezeError, held_out_items, load_freeze  # noqa: E402


def commit_exists(commit: str) -> bool:
    result = subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=ROOT,
                            capture_output=True)
    return result.returncode == 0


def main(argv: Sequence[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--questions", type=Path, required=True, help="P3's qa_for_held_out_v2.jsonl")
    p.add_argument("--freeze", type=Path, default=ROOT / "configs/p4_freeze.json")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args(argv)
    if args.out.exists():
        raise SystemExit(f"{args.out} exists; choose a new --out")
    try:
        # The freeze record is read first and checked before the question file is opened.
        items = held_out_items(args.questions, load_freeze(args.freeze), commit_exists=commit_exists)
    except FreezeError as error:
        raise SystemExit(str(error)) from error
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as sink:
        for item in items:
            sink.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"wrote {len(items)} questions to {args.out}")


if __name__ == "__main__":
    main()
