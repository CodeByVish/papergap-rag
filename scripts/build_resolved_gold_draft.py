"""Build a draft 200-question gold set from the reviewed 188 disagreements.

Reads the completed review workbook, validates it, writes one audit row per
disagreement, and adds the final labels to the agreed-only draft gold.
Requires openpyxl.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook

FOLDER = Path("data/processed/annotation_common_v3_markdown")
MUST = "Must review (102)"
SPOT = "Spot-check (86)"
HUMAN_REVIEWED = "human_reviewed"
HUMAN_CHECKED = "human_spot_checked"
AI_UNCHECKED = "ai_suggestion_unchecked"
DISCLOSURE = (
    "Changyan Xu accepted these labels with disclosure instead of third-person "
    "adjudication; team sign-off is pending. Disclose in any report that the "
    "reviewer annotated some of these pairs, that unchecked AI suggestions are "
    "included, that AI suggestions may have been visible during review, and that "
    "most records have no written reason."
)
FIELDS = [
    "record_number",
    "batch",
    "question_id",
    "passage_id",
    "annotator_A",
    "label_A",
    "annotator_B",
    "label_B",
    "final_label",
    "label_source",
    "reviewer",
    "reviewer_note",
    "reviewer_is_annotator",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]


def read_sheet(sheet) -> list[dict]:
    rows = sheet.iter_rows(values_only=True)
    header = next(rows)
    return [dict(zip(header, row)) for row in rows]


def read_batches() -> dict[int, dict]:
    """Return record_number -> labels from both annotators' batch files."""
    records: dict[int, dict] = {}
    for slot in "AB":
        for path in sorted((FOLDER / f"annotator_{slot}").glob("batch_*.md")):
            body = path.read_text(encoding="utf-8")
            name = re.search(r"(?m)^Annotator:[ \t]*(.*?)\s*$", body).group(1)
            batch = int(path.stem.split("_")[1])
            for number, label in re.findall(
                r"(?m)^#### Relevance (\d+)\s*\n+Label:[ \t]*([01])\s*$", body
            ):
                entry = records.setdefault(int(number), {"batch": batch})
                entry[f"annotator_{slot}"] = name
                entry[f"label_{slot}"] = int(label)
    return records


def read_reviews(workbook: Path) -> list[dict]:
    book = load_workbook(workbook, data_only=True)
    reviews = []
    for row in read_sheet(book[MUST]):
        reviews.append({**row, "label_source": HUMAN_REVIEWED})
    for row in read_sheet(book[SPOT]):
        source = HUMAN_CHECKED if row["Must check?"] == "Yes" else AI_UNCHECKED
        reviews.append({**row, "label_source": source})
    return reviews


def resolve(reviews: list[dict], pairs: dict[int, dict]) -> list[dict]:
    batches = read_batches()
    disputed = {n for n, r in batches.items() if r["label_A"] != r["label_B"]}
    numbers = [row["Relevance #"] for row in reviews]
    if len(numbers) != len(set(numbers)) or set(numbers) != disputed:
        raise ValueError("Workbook must cover each disagreement exactly once")
    output = []
    for row in sorted(reviews, key=lambda r: r["Relevance #"]):
        number = row["Relevance #"]
        pair, votes = pairs[number], batches[number]
        final = row["Final label (0/1)"]
        reviewer = (row["Reviewer"] or "").strip()
        if final not in (0, 1) or not reviewer:
            raise ValueError(f"Record {number}: missing final label or reviewer")
        if (row["question_id"], row["passage_id"]) != (
            pair["question_id"],
            pair["passage_id"],
        ):
            raise ValueError(f"Record {number}: workbook IDs differ from the pool")
        first = reviewer.casefold().split()[0]
        names = (votes["annotator_A"].casefold(), votes["annotator_B"].casefold())
        output.append(
            {
                "record_number": number,
                **{k: votes[k] for k in ("batch", "annotator_A", "label_A")},
                **{k: votes[k] for k in ("annotator_B", "label_B")},
                "question_id": pair["question_id"],
                "passage_id": pair["passage_id"],
                "final_label": final,
                "label_source": row["label_source"],
                "reviewer": reviewer,
                "reviewer_note": (row["Reviewer note"] or "").strip(),
                "reviewer_is_annotator": any(first in n.split() for n in names),
            }
        )
    return output


def add_to_gold(base: list[dict], resolved: list[dict], pairs: dict[int, dict]):
    final = {(r["question_id"], r["passage_id"]): r["final_label"] for r in resolved}
    ordered: dict[str, list[str]] = {}
    for _, pair in sorted(pairs.items()):
        ordered.setdefault(pair["question_id"], []).append(pair["passage_id"])
    labels = []
    for row in base:
        qid = row["question_id"]
        agreed = set(row["judged_passage_ids"])
        relevant = set(row["relevant_passage_ids"])
        extra = {p for q, p in final if q == qid}
        if agreed & extra or agreed | extra != set(ordered[qid]):
            raise ValueError(f"Judged passages do not match the pool: {qid}")
        relevant |= {p for p in extra if final[qid, p] == 1}
        labels.append(
            {
                **row,
                "relevant_passage_ids": [p for p in ordered[qid] if p in relevant],
                "judged_passage_ids": ordered[qid],
            }
        )
    return labels


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--pairs", type=Path, required=True)
    parser.add_argument("--base-gold", type=Path, required=True)
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--audit-csv", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    pairs = {p["record_number"]: p for p in read_jsonl(args.pairs)}
    resolved = resolve(read_reviews(args.workbook), pairs)
    with args.audit_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(resolved)

    labels = add_to_gold(read_jsonl(args.base_gold), resolved, pairs)
    args.output.mkdir(parents=True, exist_ok=True)
    gold = args.output / "final_labels.jsonl"
    gold.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in labels),
        encoding="utf-8",
    )
    manifest = json.loads(args.base_manifest.read_text(encoding="utf-8"))
    manifest.update(
        {
            "draft_status": "DRAFT - NOT team-confirmed; not third-person adjudication",
            "labels_sha256": sha256(gold),
            "annotation_coverage": "complete",
            "disagreement_policy": "reviewed-draft",
            "dropped_disagreement_pairs": 0,
            "dropped_questions": 0,
            "questions_without_relevant": sum(
                not r["relevant_passage_ids"] for r in labels
            ),
            "resolution": {
                "decision": DISCLOSURE,
                "disagreements": len(resolved),
                "final_label_counts": dict(
                    sorted(Counter(r["final_label"] for r in resolved).items())
                ),
                "label_sources": dict(
                    sorted(Counter(r["label_source"] for r in resolved).items())
                ),
                "reviewer_is_annotator": sum(
                    r["reviewer_is_annotator"] for r in resolved
                ),
                "workbook_sha256": sha256(args.workbook),
                "audit_csv_sha256": sha256(args.audit_csv),
                "base_gold_sha256": sha256(args.base_gold),
            },
        }
    )
    (args.output / "final_labels_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest["resolution"], indent=2))
    print("questions without relevant:", manifest["questions_without_relevant"])


if __name__ == "__main__":
    main()
