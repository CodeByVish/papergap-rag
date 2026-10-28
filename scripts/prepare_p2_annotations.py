"""Export P2's proposed blind batches from an approved, complete annotation pool."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from src.evaluation.retrieval import read_jsonl


def export_batch(rows, path, first, last):
    if first < 1 or last < first or last > len(rows):
        raise ValueError("Annotation range is outside pool")
    with path.open("x", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(
            out,
            fieldnames=[
                "record_number",
                "record_id",
                "question_id",
                "paper_id",
                "question",
                "passage_id",
                "section",
                "text",
                "relevance",
                "notes",
            ],
        )
        writer.writeheader()
        for number in range(first, last + 1):
            row = rows[number - 1]
            p = row["passage"]
            writer.writerow(
                {
                    "record_number": number,
                    "record_id": row["record_id"],
                    "question_id": row["question_id"],
                    "paper_id": row["paper_id"],
                    "question": row["question"],
                    "passage_id": p["passage_id"],
                    "section": p["section"],
                    "text": p["text"],
                    "relevance": "",
                    "notes": "",
                }
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--assignment-manifest",
        type=Path,
        required=True,
        help="P6 approval: approved_by, pool_sha256, p2_first:[start,end], p2_second:[start,end]",
    )
    args = parser.parse_args()
    try:
        manifest = json.loads((args.pool_dir / "pool_manifest.json").read_text())
        blinded = args.pool_dir / "blinded.jsonl"
        digest = hashlib.sha256(blinded.read_bytes()).hexdigest()
        approval = json.loads(args.assignment_manifest.read_text())
        if (
            manifest.get("role") != "held_out"
            or manifest.get("status") != "complete"
            or manifest.get("blinded_sha256") != digest
            or approval.get("pool_sha256") != digest
            or not approval.get("approved_by")
        ):
            raise ValueError(
                "Requires complete held-out pool and matching P6 assignment approval"
            )
        rows = read_jsonl(blinded)
        if (
            len(rows) != 1000
            or len({(r["question_id"], r["passage"]["passage_id"]) for r in rows})
            != 1000
        ):
            raise ValueError("Final annotation pool must contain 1,000 unique pairs")
        counts = Counter(r["question_id"] for r in rows)
        if len(counts) != 100 or set(counts.values()) != {10}:
            raise ValueError(
                "Final pool must contain 100 questions with ten pairs each"
            )
        ranges = [approval["p2_first"], approval["p2_second"]]
        assigned = [set(range(first, last + 1)) for first, last in ranges]
        if assigned[0] & assigned[1] or any(
            not indices or min(indices) < 1 or max(indices) > len(rows)
            for indices in assigned
        ):
            raise ValueError("P2 ranges must be valid and disjoint")
        args.output_dir.mkdir(parents=True, exist_ok=False)
        for name, (first, last) in zip(["first", "second"], ranges, strict=True):
            export_batch(rows, args.output_dir / f"p2-{name}.csv", first, last)
        with (args.output_dir / "assignment.json").open("x") as out:
            json.dump(
                {"pool_sha256": digest, "approval": approval, "labels_filled": False},
                out,
                indent=2,
            )
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
