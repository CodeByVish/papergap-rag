"""Development question items with gold passages from P3's evidence mapping.

    python -m scripts.make_dev_items \
        --mapping gold_evidence_mapping_all_splits.jsonl \
        --passages passages.jsonl --qa qa.jsonl \
        --split train --answerable 32 --unanswerable 8 --out items.jsonl

The output feeds `scripts/run_agent_experiment.py --items`. Gold passage IDs come from
P3's `gold-evidence-to-passage-v0-proposed` mapping; they only mean something on the
passages file the mapping was built against (the 365/40-word corpus), so a mapping
that matches no passage in `--passages` stops the script. Questions without a mapping
row (unanswerable, or evidence that did not match whole paragraphs) get no gold.
The test split is refused.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts.run_agent_experiment import ALLOWED_SPLITS


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as source:
        for line in source:
            if line.strip():
                yield json.loads(line)


def spread(rows: list[dict[str, Any]], count: int) -> list[dict[str, Any]]:
    """`count` rows, one per paper, evenly spaced over the papers in sorted order."""
    first_per_paper: dict[str, dict[str, Any]] = {}
    for row in sorted(rows, key=lambda r: (r["paper_id"], r["question_id"])):
        first_per_paper.setdefault(row["paper_id"], row)
    papers = list(first_per_paper.values())
    if count > len(papers):
        raise ValueError(f"asked for {count} questions but only {len(papers)} papers qualify")
    step = len(papers) / count if count else 0
    return [papers[int(i * step)] for i in range(count)]


def build_items(mapping: Path, passages: Path, qa: Path, split: str,
                answerable: int, unanswerable: int) -> list[dict[str, Any]]:
    if split not in ALLOWED_SPLITS:
        raise ValueError(f"split must be one of {ALLOWED_SPLITS}; the test split is refused")
    passage_ids, papers = set(), set()
    for row in read_jsonl(passages):
        passage_ids.add(row["passage_id"])
        papers.add(row["paper_id"])

    mapped = [r for r in read_jsonl(mapping)
              if r["source_split"] == split and r["paper_id"] in papers and r["gold_passage_ids"]]
    usable = [r for r in mapped if set(r["gold_passage_ids"]) <= passage_ids]
    if mapped and not usable:
        raise ValueError(
            "none of the mapping's gold passage IDs occur in --passages; the mapping was "
            "built on a different chunking (P3's is 365/40 words)"
        )
    items = [
        {"question_id": r["question_id"], "question": r["question"], "paper_id": r["paper_id"],
         "answerable": True, "gold_passage_ids": sorted(set(r["gold_passage_ids"]))}
        for r in spread(usable, answerable)
    ]
    cannot_answer = [
        {"question_id": r["question_id"], "question": r["question"], "paper_id": r["paper_id"],
         "answerable": False}
        for r in read_jsonl(qa)
        if r["source_split"] == split and r["paper_id"] in papers
        and all(a["answer"]["unanswerable"] for a in r["answers"])
    ]
    return items + spread(cannot_answer, unanswerable)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mapping", type=Path, required=True)
    p.add_argument("--passages", type=Path, required=True)
    p.add_argument("--qa", type=Path, required=True)
    p.add_argument("--split", default="train", choices=ALLOWED_SPLITS)
    p.add_argument("--answerable", type=int, default=32)
    p.add_argument("--unanswerable", type=int, default=8)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    try:
        items = build_items(args.mapping, args.passages, args.qa, args.split,
                            args.answerable, args.unanswerable)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as sink:
        for item in items:
            sink.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"wrote {len(items)} items ({sum(i['answerable'] for i in items)} answerable) to {args.out}")


if __name__ == "__main__":
    main()
