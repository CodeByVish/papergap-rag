"""Audit committed P3 A/B labels; never adjudicate or generate judgments."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


def audit(ref):
    commit = subprocess.check_output(["git", "rev-parse", ref], text=True).strip()
    hashes = {}

    def read(path):
        data = subprocess.check_output(["git", "show", f"{commit}:{path}"])
        hashes[path] = hashlib.sha256(data).hexdigest()
        return data.decode("utf-8")

    pool = "data/processed/annotation_common_v3"
    pairs = [json.loads(line) for line in read(f"{pool}/pairs.jsonl").splitlines()]
    expected = {p["record_number"]: p for p in pairs}
    if len(expected) != len(pairs):
        raise ValueError("Duplicate pool record numbers")
    slots, batches = {}, []
    for slot in ("A", "B"):
        labels = {}
        for batch in range(1, 11):
            path = f"{pool}_markdown/annotator_{slot}/batch_{batch:02}.md"
            text = read(path)
            entries = re.findall(
                r"^#### Relevance (\d+)\s*\n\s*Label:[ \t]*([^\n]*)", text, re.MULTILINE
            )
            if len(entries) != len(re.findall(r"^#### Relevance ", text, re.MULTILINE)):
                raise ValueError(f"Malformed label field: {path}")
            filled = 0
            for number, value in entries:
                number, value = int(number), value.strip()
                if (
                    number in labels
                    or number not in expected
                    or value not in ("", "0", "1")
                ):
                    raise ValueError(
                        f"Duplicate/unknown record or invalid label: {path}:{number}"
                    )
                labels[number] = int(value) if value else None
                filled += bool(value)
            batches.append(
                {"slot": slot, "batch": batch, "filled": filled, "total": len(entries)}
            )
        if set(labels) != set(expected):
            raise ValueError(f"Slot {slot} does not cover the exact pool")
        slots[slot] = labels
    paired = [i for i in expected if all(slots[s][i] is not None for s in slots)]
    conflicts = [
        {
            "record_number": i,
            "question_id": expected[i]["question_id"],
            "passage_id": expected[i]["passage_id"],
            "A": slots["A"][i],
            "B": slots["B"][i],
        }
        for i in paired
        if slots["A"][i] != slots["B"][i]
    ]
    agreement = (len(paired) - len(conflicts)) / len(paired) if paired else None
    complete = len(paired) == len(expected)
    return {
        "source_commit": commit,
        "input_sha256": hashes,
        "batches": batches,
        "pool_pairs": len(expected),
        "paired_records": len(paired),
        "missing_judgments": sum(
            v is None for labels in slots.values() for v in labels.values()
        ),
        "observed_label_agreement": agreement,
        "disagreements": conflicts,
        "all_labels_present": complete,
        "ready_for_final_scoring": False,
        "limitations": [
            "Presence/agreement checks do not certify independent human authorship.",
            "A08–10 originated as Codex labels and were subsequently confirmed by P2.",
            "P3/P6 must approve provenance, adjudication and final scoring labels.",
            "No disagreements are automatically resolved; no retrieval quality scores are claimed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="origin/p3-qasper-foundation")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.ref)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k not in ("input_sha256", "disagreements", "batches")
            },
            indent=2,
        )
    )
    print(f"Disagreements: {len(result['disagreements'])}")


if __name__ == "__main__":
    main()
