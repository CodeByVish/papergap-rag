"""Validate P3's frozen common-pool ranking format and reuse binary metric arithmetic."""

from __future__ import annotations

from collections import defaultdict

from src.evaluation.common import index_rows, mean
from src.evaluation.retrieval import binary_metrics


def score_p3(questions, pairs, rankings, labels, ks, coverage="complete"):
    """Score saved rankings against pool labels.

    With `coverage="agreed_only"` (dropped disagreements), unjudged passages are
    removed from each ranking before cutting at K (condensed list), and P@K is
    over the judged passages in that condensed top K.
    """
    if coverage not in {"complete", "agreed_only"}:
        raise ValueError("Coverage must be complete or agreed_only")
    qmap, gold = index_rows(questions), index_rows(labels)
    if not ks or any(type(k) is not int or k < 1 for k in ks):
        raise ValueError("K must be positive integers")
    if set(gold) != set(qmap):
        raise ValueError("Gold question scope differs from frozen questions")
    pool, records = defaultdict(dict), {}
    for p in pairs:
        qid, pid = p["question_id"], p["passage_id"]
        if (
            qid not in qmap
            or p["paper_id"] != qmap[qid]["paper_id"]
            or p["question"] != qmap[qid]["question"]
        ):
            raise ValueError("Pool question identity mismatch")
        if pid in pool[qid] or p["record_number"] in records:
            raise ValueError("Duplicate pair/record identity")
        pool[qid][pid] = p["record_number"]
        records[p["record_number"]] = (qid, pid)
    for qid, g in gold.items():
        judged, relevant = g["judged_passage_ids"], g["relevant_passage_ids"]
        if (
            g.get("status") != "mapped"
            or g.get("relevance_complete") is not False
            or g["paper_id"] != qmap[qid]["paper_id"]
            or len(judged) != len(set(judged))
            or len(relevant) != len(set(relevant))
            or not set(relevant) <= set(judged)
            or not set(judged) <= set(pool[qid])
            or (coverage == "complete" and set(judged) != set(pool[qid]))
        ):
            raise ValueError(
                "Gold must cover exactly the frozen common pool, without claiming exhaustive relevance"
            )
    by_method, seen = defaultdict(list), set()
    for r in rankings:
        qid, method = r["question_id"], r["method"]
        if (
            qid not in qmap
            or not isinstance(method, str)
            or not method
            or (method, qid) in seen
        ):
            raise ValueError("Unknown/duplicate ranking identity")
        seen.add((method, qid))
        hits = r["hits"]
        if [h["rank"] for h in hits] != list(range(1, len(hits) + 1)):
            raise ValueError("Ranks must be contiguous in saved order")
        ids = [h["passage_id"] for h in hits]
        if len(ids) != len(set(ids)) or any(
            records.get(h["record_number"]) != (qid, h["passage_id"]) for h in hits
        ):
            raise ValueError("Ranking passage/record identity mismatch")
        if max(ks) > len(hits):
            raise ValueError("Requested K exceeds saved ranking depth")
        by_method[method].append((qid, ids))
    per_question, summaries = [], []
    for method, rows in sorted(by_method.items()):
        if {qid for qid, _ in rows} != set(qmap):
            raise ValueError("Every method must contain every frozen question")
        for qid, ids in rows:
            relevant = set(gold[qid]["relevant_passage_ids"])
            judged = set(gold[qid]["judged_passage_ids"])
            condensed = [pid for pid in ids if pid in judged]
            for k in ks:
                values = binary_metrics(condensed, relevant, k)
                shown = len(condensed[:k])
                if coverage == "agreed_only":
                    values["precision_at_k"] = (
                        values["precision_at_k"] * k / shown if shown else None
                    )
                coverage_at_k = sum(pid in judged for pid in ids[:k]) / k
                values["pool_recall_at_k"] = values.pop("recall_at_k")
                values["pool_ndcg_at_k"] = values.pop("ndcg_at_k")
                per_question.append(
                    {
                        "question_id": qid,
                        "paper_id": qmap[qid]["paper_id"],
                        "arm": method,
                        "k": k,
                        "judged_coverage": coverage_at_k,
                        **values,
                    }
                )
        for k in ks:
            selected = [r for r in per_question if r["arm"] == method and r["k"] == k]
            summary = {
                "arm": method,
                "k": k,
                "questions": len(selected),
                "judged_coverage": mean(r["judged_coverage"] for r in selected),
            }
            for metric in (
                "precision_at_k",
                "pool_recall_at_k",
                "mrr_at_k",
                "pool_ndcg_at_k",
            ):
                summary[metric] = mean(r[metric] for r in selected)
                summary[metric + "_n"] = sum(r[metric] is not None for r in selected)
            summaries.append(summary)
    return per_question, summaries
