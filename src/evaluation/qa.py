"""Deterministic QA scoring; a proposed project policy, not official QASPER scoring."""

from __future__ import annotations

import re
import string
from collections import Counter

from src.evaluation.common import index_rows, mean

POLICY = "p6-qa-v0-proposed"
REFUSAL = "Insufficient evidence in the retrieved passages to answer this question."


def normalize(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return " ".join(re.sub(r"\b(a|an|the)\b", " ", text).split())


def pair_scores(prediction, reference):
    p, r = normalize(prediction), normalize(reference)
    pt, rt = p.split(), r.split()
    overlap = sum((Counter(pt) & Counter(rt)).values())
    f1 = (2 * overlap / (len(pt) + len(rt))) if pt or rt else 1.0
    return {"em": float(p == r), "f1": f1}


def references(row):
    """Extract references from normalized P6 rows or original QASPER answer arrays.

    Mixed answerable/unanswerable annotations use answerable references, explicitly.
    Span arrays are joined in recorded order with a space; no invented reference.
    """
    if "references" in row:
        refs, unanswerable = row["references"], row.get("unanswerable")
        if type(unanswerable) is not bool or not isinstance(refs, list):
            raise ValueError(
                "Normalized references require list and boolean unanswerable"
            )
        if not all(isinstance(x, str) and x.strip() for x in refs):
            raise ValueError("Invalid reference text")
        if unanswerable == bool(refs):
            raise ValueError(
                "Unanswerable requires no references; answerable requires references"
            )
        return refs, unanswerable
    answers = row.get("answers")
    if not isinstance(answers, list) or not answers:
        raise ValueError("Missing reference annotations")
    refs, flags = [], []
    for entry in answers:
        if not isinstance(entry, dict):
            raise TypeError("Malformed QASPER annotation")
        a = entry.get("answer", entry)
        if not isinstance(a, dict):
            raise TypeError("Malformed QASPER answer object")
        flag = a.get("unanswerable")
        if type(flag) is not bool:
            raise ValueError("Missing QASPER unanswerable flag")
        flags.append(flag)
        if flag:
            continue
        if type(a.get("yes_no")) is bool:
            text = "yes" if a["yes_no"] else "no"
        elif a.get("free_form_answer"):
            text = a["free_form_answer"]
        else:
            spans = a.get("extractive_spans", [])
            if not isinstance(spans, list) or not all(
                isinstance(x, str) for x in spans
            ):
                raise ValueError("Invalid extractive spans")
            text = " ".join(spans)
        if not isinstance(text, str) or not normalize(text):
            raise ValueError("Answerable annotation has no valid reference text")
        refs.append(text)
    return list(dict.fromkeys(refs)), all(flags)


def prediction(row):
    """Read an agent output, P5 wire envelope, or explicit P6 prediction row."""
    if row.get("error") or row.get("answer_error"):
        return "", "error"
    if "status" in row:
        status = row["status"]
        if status not in {"answered", "refused", "error"}:
            raise ValueError("Prediction status must be answered/refused/error")
        text = row.get("prediction", "")
        if not isinstance(text, str) or (status == "answered" and not text.strip()):
            raise ValueError("Answered prediction requires text")
        return text, status
    envelope = row.get("answer", row)
    if not isinstance(envelope, dict) or not isinstance(envelope.get("result"), dict):
        raise TypeError(
            "No supported prediction envelope; use an explicit normalized row"
        )
    result = envelope["result"]
    validation = envelope.get("validation", {})
    # Generation/parse errors can be encoded as refusals by P5's safe path.
    codes = [v.get("code", "") for v in validation.get("violations", [])]
    if any(c in {"GENERATION_ERROR", "PARSE_ERROR"} for c in codes):
        return "", "error"
    text = result.get("answer")
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Missing final answer text")
    refused = text == REFUSAL
    return text, "refused" if refused else "answered"


def evaluate_qa(questions, predictions, gold):
    qmap, pmap, gmap = map(index_rows, (questions, predictions, gold))
    if set(pmap) - set(qmap):
        raise ValueError("Predictions contain questions outside selected scope")
    rows = []
    for qid, q in qmap.items():
        g, p = gmap.get(qid), pmap.get(qid)
        for other in (g, p):
            if other and (
                other.get("paper_id", q["paper_id"]) != q["paper_id"]
                or other.get("question", q["question"]) != q["question"]
            ):
                raise ValueError(f"Paper mismatch: {qid}")
        base = {"question_id": qid, "paper_id": q["paper_id"]}
        if g is None:
            rows.append({**base, "status": "missing_reference", "em": None, "f1": None})
            continue
        try:
            refs, unanswerable = references(g)
        except (ValueError, TypeError):
            rows.append({**base, "status": "invalid_reference", "em": None, "f1": None})
            continue
        text, status = prediction(p) if p else ("", "missing_prediction")
        if unanswerable:
            correctness = float(status == "refused")
            scores = {"em": None, "f1": None, "unanswerable_correctness": correctness}
            task = correctness
        else:
            matches = (
                [pair_scores(text, r) for r in refs] if status == "answered" else []
            )
            scores = {
                k: max((x[k] for x in matches), default=0.0) for k in ("em", "f1")
            }
            scores["unanswerable_correctness"] = None
            task = scores["f1"]
        rows.append(
            {
                **base,
                "status": status,
                "unanswerable": unanswerable,
                **scores,
                "task_score": task,
            }
        )
    summary = {
        "policy": POLICY,
        "questions": len(rows),
        "answerable_em": mean(r.get("em") for r in rows),
        "answerable_f1": mean(r.get("f1") for r in rows),
        "unanswerable_correctness": mean(
            r.get("unanswerable_correctness") for r in rows
        ),
        "combined_task_score": mean(r.get("task_score") for r in rows),
        "answered": sum(r["status"] == "answered" for r in rows),
        "refused": sum(r["status"] == "refused" for r in rows),
        "failures": sum(r["status"] in {"error", "missing_prediction"} for r in rows),
        "reference_exclusions": sum(
            r["status"] in {"missing_reference", "invalid_reference"} for r in rows
        ),
    }
    summary["answer_coverage"] = summary["answered"] / len(rows) if rows else None
    for metric in ("em", "f1", "unanswerable_correctness", "task_score"):
        summary[metric + "_n"] = sum(r.get(metric) is not None for r in rows)
    summary["answered_only_f1"] = mean(
        r.get("f1") for r in rows if r["status"] == "answered"
    )
    return rows, summary
