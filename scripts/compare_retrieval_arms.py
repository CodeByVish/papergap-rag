#!/usr/bin/env python
"""Explain outcome changes between two retrieval arms, record by record.

``compare_runs.py`` says *what* moved. ``week5_diagnose.py`` says *why* the
generator or validator moved. This script answers the retrieval question those
two cannot: **was the passage the old answer cited still retrieved by the new
arm?**

The distinction matters for R3 vs R4. A reranker is allowed to change the top-k;
what it is not allowed to do silently is drop the only passage that carried the
answer. When an answered -> refused flip happens:

* ``evidence_dropped`` - none of the old citations are in the new arm's context.
  The reranker removed the evidence; the refusal is a retrieval result.
* ``evidence_partly_dropped`` - some old citations survived. Part of the gap is
  retrieval, part is the model's judgement on a changed context.
* ``same_evidence`` - every old citation is still there. The refusal is the
  model/validator reacting to different *surrounding* passages, not to missing
  evidence.

And for a refused -> answered flip, ``new_evidence`` means the new arm surfaced
something the old arm never retrieved; ``same_evidence`` means the model changed
its mind on the same passages.

    python scripts/compare_retrieval_arms.py \\
        --baseline-answers runs/week5/answers-vllm-v7-cluster.jsonl \\
        --candidate-answers runs/week6/answers-vllm-bge-reranked-cluster.jsonl \\
        --baseline-retrieval data/p1_hybrid.jsonl \\
        --candidate-retrieval data/bge/retrieval.jsonl \\
        --out runs/week6/retrieval-arm-diff.json

Reads files only: no model, no GPU. It imports the adapter, so run it with the
same interpreter as the generation scripts (pydantic is required).
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from generate_from_retrieval import load_payloads  # noqa: E402
from src.generation.adapters import build_request  # noqa: E402


def load_answers(path: str | Path) -> dict[str, dict[str, Any]]:
    records = [
        json.loads(line)
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return {str(record["request_id"]): record for record in records}


def load_contexts(path: str | Path) -> dict[str, set[str]]:
    """``question_id -> passage ids the arm actually supplied``.

    Built through the same adapter the generator used, so a nested P2 hit and a
    flat P1 hit are read identically. A payload that cannot be adapted is
    skipped: this is a diagnostic, and one malformed line must not hide the
    other 99.
    """
    contexts: dict[str, set[str]] = {}
    for payload in load_payloads(path):
        try:
            adapted = build_request(payload)
        except (ValueError, TypeError):
            continue
        request = adapted.request
        if request.request_id is None:
            continue
        contexts[str(request.request_id)] = set(request.passage_ids)
    return contexts


def outcome(record: dict[str, Any]) -> str:
    result = record["result"]
    if result["evidence_status"] != "SUFFICIENT":
        return "refused"
    if not result["citations"]:
        return "no-cite"
    return "answered"


def classify(
    before: str,
    after: str,
    old_citations: list[str],
    new_citations: list[str],
    old_context: set[str],
    new_context: set[str],
) -> str:
    """One label for why the outcome changed, retrieval-first."""
    if after == "answered":
        if any(citation not in old_context for citation in new_citations):
            return "new_evidence"
        return "same_evidence"

    if before == "answered" and after == "refused":
        if not old_citations:
            return "same_evidence"  # nothing was cited before; not a retrieval gap
        dropped = [c for c in old_citations if c not in new_context]
        if len(dropped) == len(old_citations):
            return "evidence_dropped"
        if dropped:
            return "evidence_partly_dropped"
        return "same_evidence"

    return "other"


def compare(
    baseline_answers: dict[str, dict[str, Any]],
    candidate_answers: dict[str, dict[str, Any]],
    baseline_contexts: dict[str, set[str]],
    candidate_contexts: dict[str, set[str]],
) -> dict[str, Any]:
    changes: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()

    for request_id, record in candidate_answers.items():
        previous = baseline_answers.get(request_id)
        if previous is None:
            continue
        before, after = outcome(previous), outcome(record)
        if before == after:
            continue

        old_citations = list(previous["result"]["citations"])
        new_citations = list(record["result"]["citations"])
        old_context = baseline_contexts.get(request_id, set())
        new_context = candidate_contexts.get(request_id, set())
        label = classify(
            before, after, old_citations, new_citations, old_context, new_context
        )
        counts[label] += 1
        changes.append(
            {
                "request_id": request_id,
                "index": record.get("index"),
                "question": record["question"],
                "from": before,
                "to": after,
                "label": label,
                "downgraded": record["validation"]["downgraded"],
                "downgrade_reason": record["validation"].get("downgrade_reason"),
                "old_citations": old_citations,
                "new_citations": new_citations,
                "old_citations_surviving": [
                    c for c in old_citations if c in new_context
                ],
                "old_citations_dropped": [
                    c for c in old_citations if c not in new_context
                ],
                "new_citations_not_previously_retrieved": [
                    c for c in new_citations if c not in old_context
                ],
                "context_overlap": (
                    len(old_context & new_context) / len(old_context | new_context)
                    if old_context | new_context
                    else None
                ),
            }
        )

    return {
        "changes": changes,
        "counts": dict(counts),
        "baseline_only": sorted(set(baseline_answers) - set(candidate_answers)),
        "candidate_only": sorted(set(candidate_answers) - set(baseline_answers)),
    }


def _cut(text: str, limit: int = 90) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-answers", type=Path, required=True)
    parser.add_argument("--candidate-answers", type=Path, required=True)
    parser.add_argument("--baseline-retrieval", type=Path, required=True)
    parser.add_argument("--candidate-retrieval", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args(argv)

    report = compare(
        load_answers(args.baseline_answers),
        load_answers(args.candidate_answers),
        load_contexts(args.baseline_retrieval),
        load_contexts(args.candidate_retrieval),
    )

    print("| change | count |")
    print("| --- | ---: |")
    for label, count in sorted(report["counts"].items()):
        print(f"| {label} | {count} |")

    for item in report["changes"]:
        print()
        print(
            f"[{item['index']}] {item['from']} -> {item['to']} "
            f"| {item['label']} | {_cut(item['question'])}"
        )
        print(
            f"  downgraded: {item['downgraded']} "
            f"reason: {item['downgrade_reason']} "
            f"| context overlap: {item['context_overlap']}"
        )
        print(f"  old citations surviving: {item['old_citations_surviving']}")
        print(f"  old citations dropped  : {item['old_citations_dropped']}")
        print(
            "  new citations not previously retrieved: "
            f"{item['new_citations_not_previously_retrieved']}"
        )

    if report["baseline_only"] or report["candidate_only"]:
        print()
        print("ids only in baseline:", report["baseline_only"][:5])
        print("ids only in candidate:", report["candidate_only"][:5])

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
