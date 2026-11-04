"""Read pinned P3 sheets, preserve original labels, and prepare audited gold exports."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

from src.evaluation.common import sha256, write_csv, write_json, write_jsonl

BASE = "data/processed/annotation_common_v3"
VIEWS = BASE + "_markdown"


def agreement(rows):
    n = len(rows)
    if not n:
        raise ValueError("No double-labeled records")
    counts = Counter(rows)
    observed = sum(a == b for a, b in rows) / n
    pa, pb = (sum(row[i] for row in rows) / n for i in (0, 1))
    expected = pa * pb + (1 - pa) * (1 - pb)
    return {
        "n": n,
        "agreement": observed,
        "kappa": (observed - expected) / (1 - expected) if expected != 1 else None,
        "positive_rate_left": pa,
        "positive_rate_right": pb,
        "confusion_00_01_10_11": [counts[x] for x in ((0, 0), (0, 1), (1, 0), (1, 1))],
    }


def masked(text):
    text = re.sub(r"(?m)^Annotator:[^\n]*$", "Annotator:", text)
    text = re.sub(r"(?m)^Label:[^\n]*$", "Label:", text)
    text = re.sub(r"(?m)(^Label:\n)(?:>[^\n]*\n)+", r"\1", text)
    text = text.replace("Enter your name or agreed identifier after `Annotator:`.", "")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def audit_p3(repo, ref):
    def git(*args):
        return subprocess.check_output(["git", "-C", str(repo), *args])

    commit = git("rev-parse", "--verify", ref + "^{commit}").decode().strip()

    def read(path, revision=commit):
        return git("show", f"{revision}:{path}")

    pairs = [
        json.loads(x) for x in read(BASE + "/pairs.jsonl").decode().splitlines() if x
    ]
    view = json.loads(read(VIEWS + "/manifest.json"))
    pool_manifest = json.loads(read(BASE + "/manifest.json"))
    for path, expected in pool_manifest["outputs"].items():
        if hashlib.sha256(read(path)).hexdigest() != expected:
            raise ValueError(f"Frozen ranking/pool hash mismatch: {path}")
    for path, expected in view["inputs"].items():
        if hashlib.sha256(read(path)).hexdigest() != expected:
            raise ValueError(f"Frozen pool hash mismatch: {path}")
    by_record = {p["record_number"]: p for p in pairs}
    if len(by_record) != len(pairs) or len(
        {(p["question_id"], p["passage_id"]) for p in pairs}
    ) != len(pairs):
        raise ValueError("Duplicate pool identity")
    paths = git("ls-tree", "-r", "--name-only", commit, VIEWS).decode().splitlines()
    sheets = sorted(p for p in paths if re.search(r"/annotator_[AB]/.*\.md$", p))
    if set(sheets) != {
        p for p in view["outputs"] if re.search(r"/annotator_[AB]/.*\.md$", p)
    }:
        raise ValueError("Annotation sheet inventory differs from export manifest")
    judgments = {}
    for path in sheets:
        body = read(path).decode()
        template = None
        for revision in (
            git("log", "--format=%H", commit, "--", path).decode().splitlines()
        ):
            raw = read(path, revision)
            if hashlib.sha256(raw).hexdigest() == view["outputs"][path]:
                template = raw.decode()
                break
        if template is None or masked(body) != masked(template):
            raise ValueError(f"Original template unavailable or body changed: {path}")
        names = re.findall(r"(?m)^Annotator:[ \t]*(.*?)\s*$", body)
        if len(names) != 1 or not names[0].strip():
            raise ValueError(f"Missing human identity: {path}")
        name = names[0].strip()
        slot = re.search(r"/annotator_([AB])/", path).group(1)
        records = re.findall(
            r"(?m)^#### Relevance (\d+)\s*\n+Label:[ \t]*([^\n]*)", body
        )
        passage_numbers = [
            int(x) for x in re.findall(r"(?m)^#### Passage (\d+)$", body)
        ]
        if not records or [int(n) for n, _ in records] != passage_numbers:
            raise ValueError(f"Record alignment mismatch: {path}")
        for number, label in records:
            number = int(number)
            if (
                label.strip() not in {"0", "1"}
                or number not in by_record
                or (slot, number) in judgments
            ):
                raise ValueError(
                    f"Missing/invalid/duplicate label: {path} record {number}"
                )
            judgments[slot, number] = {
                "annotator": name,
                "label": int(label.strip()),
                "source": path,
            }
    if set(judgments) != {(slot, n) for slot in "AB" for n in by_record}:
        raise ValueError("Every pool pair must have two completed labels")
    by_people, all_rows = defaultdict(list), []
    disputes = []
    for n, p in sorted(by_record.items()):
        a, b = judgments["A", n], judgments["B", n]
        if a["annotator"].casefold() == b["annotator"].casefold():
            raise ValueError(f"Same human labeled both slots: {n}")
        people = sorted((a, b), key=lambda x: x["annotator"].casefold())
        by_people[tuple(x["annotator"] for x in people)].append(
            tuple(x["label"] for x in people)
        )
        all_rows.append((a["label"], b["label"]))
        if a["label"] != b["label"]:
            disputes.append(
                {
                    "record_number": n,
                    "question_id": p["question_id"],
                    "passage_id": p["passage_id"],
                    "question": p["question"],
                    "passage": p["passage"],
                    "annotator_A": a["annotator"],
                    "label_A": a["label"],
                    "annotator_B": b["annotator"],
                    "label_B": b["label"],
                    "adjudicator": "",
                    "final_label": "",
                    "reason": "",
                }
            )
    observed = agreement(all_rows)
    observed.pop("kappa")  # Changing human pairs do not define one pooled Cohen kappa.
    report = {
        "schema_version": "v0-proposed",
        "commit": commit,
        "pairs": len(pairs),
        "questions": len({p["question_id"] for p in pairs}),
        "overall": observed,
        "threshold_pass": observed["agreement"] >= 0.8,
        "disagreements": len(disputes),
        "source_split_pair_counts": dict(Counter(p["source_split"] for p in pairs)),
        "by_human_pair": [
            {"annotators": list(names), **agreement(rows)}
            for names, rows in sorted(by_people.items())
        ],
        "input_sha256": {
            p: hashlib.sha256(read(p)).hexdigest()
            for p in sheets + [BASE + "/pairs.jsonl", BASE + "/manifest.json"]
        },
        "pool_output_sha256": pool_manifest["outputs"],
        "limitation": "Method identities were visible; distinct names do not prove independence.",
    }
    return report, pairs, judgments, disputes


def save_audit(output, report, disputes):
    write_json(output / "agreement.json", report)
    fields = [
        "record_number",
        "question_id",
        "passage_id",
        "question",
        "passage",
        "annotator_A",
        "label_A",
        "annotator_B",
        "label_B",
        "adjudicator",
        "final_label",
        "reason",
    ]
    with (output / "adjudication.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(disputes)
    write_csv(
        output / "agreement_by_pair.csv",
        [
            {
                "annotators": " / ".join(r["annotators"]),
                **{k: v for k, v in r.items() if k != "annotators"},
            }
            for r in report["by_human_pair"]
        ],
    )


def finalize_gold(
    output,
    report,
    pairs,
    judgments,
    disputes,
    adjudication_path,
    review,
    corpus,
    disagreements="adjudicate",
):
    """Export gold labels. `disagreements="drop"` keeps only agreed pairs.

    Dropped pairs are left unjudged, not relabelled; initial agreement is unchanged.
    """
    if disagreements not in {"adjudicate", "drop"}:
        raise ValueError("Disagreement policy must be adjudicate or drop")
    if (disagreements == "drop") != (adjudication_path is None):
        raise ValueError(
            "Supply an adjudication file only when disagreements are adjudicated"
        )
    required = ("independence_confirmed", "usage_and_freeze_reviewed")
    if (
        not all(review.get(k) is True for k in required)
        or not review.get("review_note", "").strip()
    ):
        raise ValueError("Human independence/usage review and review_note are required")
    if (
        review.get("project_role") not in {"development", "held_out"}
        or review.get("source_commit") != report["commit"]
    ):
        raise ValueError(
            "Review must identify actual project role and exact source commit"
        )
    if not report["threshold_pass"]:
        raise ValueError(
            "Raw agreement below 80%; preserve this round and review the protocol"
        )
    expected = {int(r["record_number"]): r for r in disputes}
    if disagreements == "drop":
        rows = []
    else:
        with Path(adjudication_path).open(newline="") as f:
            rows = list(csv.DictReader(f))
    if disagreements == "adjudicate" and (
        len(rows) != len(expected)
        or {int(r["record_number"]) for r in rows} != set(expected)
    ):
        raise ValueError("Adjudication must cover each disagreement exactly once")
    final = {}
    for row in rows:
        number = int(row["record_number"])
        original = expected[number]
        if any(
            row.get(k) != str(v)
            for k, v in original.items()
            if k not in {"adjudicator", "final_label", "reason"}
        ):
            raise ValueError("Adjudication altered original identity, text or labels")
        if row["final_label"] not in {"0", "1"} or not row["reason"].strip():
            raise ValueError("Every disagreement needs final_label and reason")
        if not row["adjudicator"].strip() or row["adjudicator"].strip().casefold() in {
            original["annotator_A"].casefold(),
            original["annotator_B"].casefold(),
        }:
            raise ValueError("Adjudicator must be a third person")
        final[number] = int(row["final_label"])
    # Verify the actual corpus agrees with all pooled text/IDs, not just an arbitrary supplied hash.
    from src.evaluation.common import index_rows, read_jsonl

    catalog = index_rows(read_jsonl(corpus), "passage_id")
    grouped, provenance = defaultdict(list), []
    for p in pairs:
        n = p["record_number"]
        c = catalog.get(p["passage_id"])
        if not c or c["paper_id"] != p["paper_id"] or c["text"] != p["passage"]:
            raise ValueError("Corpus identity/text differs from the frozen pool")
        dropped = disagreements == "drop" and n in expected
        label = None if dropped else final.get(n, judgments["A", n]["label"])
        grouped[p["question_id"]].append((p, label))
        provenance.append(
            {
                "record_number": n,
                "question_id": p["question_id"],
                "passage_id": p["passage_id"],
                "A": judgments["A", n],
                "B": judgments["B", n],
                "final_label": label,
                "dropped_disagreement": dropped,
                "adjudication": next(
                    (r for r in rows if int(r["record_number"]) == n), None
                ),
            }
        )
    labels = []
    for qid, records in sorted(grouped.items()):
        labels.append(
            {
                "question_id": qid,
                "paper_id": records[0][0]["paper_id"],
                "status": "mapped",
                "relevance_complete": False,
                "relevant_passage_ids": [p["passage_id"] for p, l in records if l],
                "judged_passage_ids": [
                    p["passage_id"] for p, l in records if l is not None
                ],
            }
        )
    write_jsonl(output / "final_labels.jsonl", labels)
    write_jsonl(output / "original_and_final_judgments.jsonl", provenance)
    write_json(
        output / "final_labels_manifest.json",
        {
            "schema_version": "v0-proposed",
            "labels_sha256": sha256(output / "final_labels.jsonl"),
            "corpus_sha256": sha256(corpus),
            "annotation_coverage": "complete"
            if disagreements == "adjudicate"
            else "agreed_only",
            "disagreement_policy": disagreements,
            "dropped_disagreement_pairs": len(expected)
            if disagreements == "drop"
            else 0,
            "questions_without_relevant": sum(
                not row["relevant_passage_ids"] for row in labels
            ),
            "relevance_complete": False,
            "source": {"commit": report["commit"], "review": review},
            "mapping": "record_number -> frozen pool -> question_id/passage_id",
            "question_scope": {
                "question_ids": sorted(grouped),
                "project_role": review["project_role"],
            },
            "pool_output_sha256": report["pool_output_sha256"],
            "agreement": report,
        },
    )
