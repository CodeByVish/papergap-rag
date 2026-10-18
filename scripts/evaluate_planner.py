"""Check the rule-based planner against QASPER gold evidence (train/validation only).

Usage:
    python scripts/evaluate_planner.py train
    python scripts/evaluate_planner.py validation

For every answerable question, reports how often the plan's requirements are
satisfied by (a) the annotated evidence paragraphs and (b) the five
non-evidence paragraphs of the same paper with the most question-term overlap.
A useful critic accepts (a) far more often than (b). The test split is refused.
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.nodes import _satisfies
from src.agent.planner import _stem, build_plan, key_terms

HARD_NEGATIVES = 5


def _passage(section: str | None, text: str) -> SimpleNamespace:
    return SimpleNamespace(passage=SimpleNamespace(section=section or "", text=text))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("split", choices=["train", "validation"])
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/raw/qasper")
    args = parser.parse_args()

    papers = [
        json.loads(line)
        for line in (args.data_dir / f"{args.split}.jsonl").read_text().splitlines()
    ]
    types: collections.Counter = collections.Counter()
    by_type = collections.defaultdict(lambda: [0, 0, 0])  # questions, gold, hard
    total = 0
    for paper in papers:
        paragraphs = [
            (section["section_name"], text)
            for section in paper["full_text"]
            for text in section["paragraphs"]
        ]
        section_of = {text.strip(): name for name, text in paragraphs}
        for qa in paper["qas"]:
            total += 1
            question = qa["question"]
            plan = build_plan(question)
            types[plan.question_type.value] += 1
            gold_texts = {
                ev.strip()
                for answer in qa["answers"]
                if not answer["answer"]["unanswerable"]
                for ev in answer["answer"]["evidence"]
                if ev.strip() in section_of
            }
            if not gold_texts:
                continue
            gold = [_passage(section_of[t], t) for t in gold_texts]
            stems = {_stem(term) for term in key_terms(question)}
            ranked = sorted(
                (
                    (sum(stem in text.lower() for stem in stems), name, text)
                    for name, text in paragraphs
                    if text.strip() not in gold_texts
                ),
                key=lambda item: -item[0],
            )
            hard = [_passage(n, t) for _, n, t in ranked[:HARD_NEGATIVES]]
            row = by_type[plan.question_type.value]
            row[0] += 1
            row[1] += all(any(_satisfies(r, p) for p in gold) for r in plan.requirements)
            row[2] += all(any(_satisfies(r, p) for p in hard) for r in plan.requirements)

    print(f"[{args.split}] questions={total}")
    print("type distribution:", {k: f"{v / total:.1%}" for k, v in types.most_common()})
    print("plan accepted by gold evidence | by top-5 lexical hard negatives")
    for name, (n, gold, hard) in sorted(by_type.items()):
        print(f"  {name:11s} n={n:5d}  {gold / n:6.1%} | {hard / n:6.1%}")
    n, gold, hard = (sum(row[i] for row in by_type.values()) for i in range(3))
    print(f"  {'OVERALL':11s} n={n:5d}  {gold / n:6.1%} | {hard / n:6.1%}")


if __name__ == "__main__":
    main()
