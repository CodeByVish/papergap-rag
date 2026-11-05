"""Check the rule-based planner against QASPER gold evidence (train/validation only).

Usage:
    python scripts/evaluate_planner.py train
    python scripts/evaluate_planner.py validation
    python scripts/evaluate_planner.py train --passages passages_p3.jsonl     # chunk level

For every answerable question, reports how often the plan's requirements are
satisfied by (a) the annotated evidence, (b) the five non-evidence units of the same
paper with the most question-term overlap and (c) as many of those as there are
evidence units, since "any of five" is easier to satisfy than "any of one or two". A useful
critic accepts (a) far more often than (b) or (c). The test split is refused.

By default the units are the paper's paragraphs. With `--passages` they are the corpus
chunks the agent actually maps evidence onto (the 365/40-word chunks), and a chunk is
gold if it contains a whole evidence paragraph or that paragraph's first or last
EDGE_WORDS words. On the 32 development items that rule reproduces P3's
`gold-evidence-to-passage-v0-proposed` ids exactly (45 of 45, none extra).
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agent.nodes import _satisfies
from src.agent.planner import _stem, build_plan, key_terms

HARD_NEGATIVES = 5
EDGE_WORDS = 12


def _passage(section: str | None, text: str) -> SimpleNamespace:
    return SimpleNamespace(passage=SimpleNamespace(section=section or "", text=text))


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def gold_chunks(chunks: list[tuple[str, str]], evidence: set[str], edge_words: int = EDGE_WORDS) -> set[int]:
    """Indexes of the chunks holding a whole evidence paragraph or its first or last words.

    `chunks` are (section, text); `evidence` are whitespace-normalised paragraphs. A
    paragraph that straddles two chunks marks both, as P3's mapping does.
    """
    found: set[int] = set()
    for index, (_, text) in enumerate(chunks):
        flat = _norm(text)
        for paragraph in evidence:
            words = paragraph.split()
            if (paragraph in flat or " ".join(words[:edge_words]) in flat
                    or " ".join(words[-edge_words:]) in flat):
                found.add(index)
                break
    return found


def load_chunks(path: Path) -> dict[str, list[tuple[str, str]]]:
    """Corpus chunks per paper id, in reading order, as (section, text)."""
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_paper: dict[str, list[tuple[int, str, str]]] = collections.defaultdict(list)
    for row in rows:
        by_paper[row["paper_id"]].append((row["chunk_number"], row["section"], row["text"]))
    return {paper: [(s, t) for _, s, t in sorted(chunks)] for paper, chunks in by_paper.items()}


def evaluate(
    papers: list[dict],
    chunks_by_paper: dict[str, list[tuple[str, str]]] | None = None,
    exclude: frozenset[str] = frozenset(),
):
    """(questions, type counts, per-type [questions, gold, 5 lookalikes, size-matched lookalikes]).

    Questions whose id is in `exclude` (e.g. a frozen held-out list) are skipped entirely.
    """
    types: collections.Counter = collections.Counter()
    by_type = collections.defaultdict(lambda: [0, 0, 0, 0])
    total = 0
    for paper in papers:
        paragraphs = [
            (section["section_name"], text)
            for section in paper["full_text"]
            for text in section["paragraphs"]
        ]
        section_of = {text.strip(): name for name, text in paragraphs}
        if chunks_by_paper is None:
            units = paragraphs
        elif paper["id"] in chunks_by_paper:
            units = chunks_by_paper[paper["id"]]
        else:
            units = []
        for qa in paper["qas"]:
            if qa.get("question_id") in exclude:
                continue
            total += 1
            question = qa["question"]
            plan = build_plan(question)
            types[plan.question_type.value] += 1
            evidence = {
                ev.strip()
                for answer in qa["answers"]
                if not answer["answer"]["unanswerable"]
                for ev in answer["answer"]["evidence"]
                if ev.strip() in section_of
            }
            if not evidence or not units:
                continue
            if chunks_by_paper is None:
                gold_index = {i for i, (_, text) in enumerate(units) if text.strip() in evidence}
            else:
                gold_index = gold_chunks(units, {_norm(e) for e in evidence})
            if not gold_index:
                continue
            gold = [_passage(units[i][0], units[i][1]) for i in sorted(gold_index)]
            stems = {_stem(term) for term in key_terms(question)}
            ranked = sorted(
                (
                    (sum(stem in text.lower() for stem in stems), name, text)
                    for i, (name, text) in enumerate(units)
                    if i not in gold_index
                ),
                key=lambda item: -item[0],
            )
            hard = [_passage(n, t) for _, n, t in ranked[:HARD_NEGATIVES]]
            matched = hard[: len(gold)]  # as many lookalikes as gold units: the fair comparison
            row = by_type[plan.question_type.value]
            row[0] += 1
            row[1] += all(any(_satisfies(r, p) for p in gold) for r in plan.requirements)
            row[2] += all(any(_satisfies(r, p) for p in hard) for r in plan.requirements)
            row[3] += all(any(_satisfies(r, p) for p in matched) for r in plan.requirements)
    return total, types, by_type


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("split", choices=["train", "validation"])
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data/raw/qasper")
    parser.add_argument("--passages", type=Path,
                        help="corpus JSONL (365/40 chunks): evaluate on chunks, not paragraphs")
    parser.add_argument("--exclude-ids", type=Path,
                        help="JSONL with a question_id per line (e.g. the frozen held-out list) to leave out")
    args = parser.parse_args()

    papers = [
        json.loads(line)
        for line in (args.data_dir / f"{args.split}.jsonl").read_text().splitlines()
    ]
    chunks = load_chunks(args.passages) if args.passages else None
    exclude = frozenset(
        json.loads(line)["question_id"]
        for line in args.exclude_ids.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ) if args.exclude_ids else frozenset()
    total, types, by_type = evaluate(papers, chunks, exclude)

    unit = "chunks" if chunks is not None else "paragraphs"
    print(f"[{args.split}] questions={total}  units={unit}"
          + (f"  excluded={len(exclude)} ids" if exclude else ""))
    print("type distribution:", {k: f"{v / total:.1%}" for k, v in types.most_common()})
    print("plan accepted by gold evidence | by top-5 lexical hard negatives | by as many "
          "hard negatives as gold units")
    for name, (n, gold, hard, matched) in sorted(by_type.items()):
        print(f"  {name:11s} n={n:5d}  {gold / n:6.1%} | {hard / n:6.1%} | {matched / n:6.1%}")
    n, gold, hard, matched = (sum(row[i] for row in by_type.values()) for i in range(4))
    print(f"  {'OVERALL':11s} n={n:5d}  {gold / n:6.1%} | {hard / n:6.1%} | {matched / n:6.1%}")


if __name__ == "__main__":
    main()
