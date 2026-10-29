"""Provisional retrieval metrics that distinguish unknown from negative labels."""

import json
import math
from collections import defaultdict
from pathlib import Path

from src.retrieval.schemas import RetrievalHit, RetrievedPassage


def read_jsonl(path):
    def unique_keys(pairs):
        row = {}
        for key, value in pairs:
            if key in row:
                raise ValueError(f"Duplicate JSON key: {key}")
            row[key] = value
        return row

    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        row = json.loads(line, object_pairs_hook=unique_keys)
        if not isinstance(row, dict):
            raise ValueError("JSONL rows must be objects")  # noqa: TRY004
        rows.append(row)
    return rows


def question_inputs(path):
    rows = read_jsonl(path)
    result, seen = [], set()
    for row in rows:
        projected = {k: row.get(k) for k in ("question_id", "paper_id", "question")}
        if any(not isinstance(v, str) or not v.strip() for v in projected.values()):
            raise ValueError("Question IDs, paper IDs and questions must be nonempty")
        if projected["question_id"] in seen:
            raise ValueError("Duplicate question ID")
        seen.add(projected["question_id"])
        result.append(projected)
    if not result:
        raise ValueError("No questions")
    return result


def binary_metrics(ids, relevant, k):
    top = ids[:k]
    matches = [int(pid in relevant) for pid in top]
    dcg = sum(rel / math.log2(i + 2) for i, rel in enumerate(matches))
    ideal = sum(1 / math.log2(i + 2) for i in range(min(k, len(relevant))))
    return {
        "precision_at_k": sum(matches) / k,
        "recall_at_k": sum(matches) / len(relevant) if relevant else None,
        "mrr_at_k": next((1 / (i + 1) for i, rel in enumerate(matches) if rel), 0.0),
        "ndcg_at_k": dcg / ideal if ideal else None,
    }


def evaluate_rankings(rankings, questions, labels, catalog, ks):
    """Binary judgments; incomplete relevance yields pool-relative recall only.

    Unknown returned passages suppress full-ranking metrics rather than being
    silently counted as negatives. A separate compressed judged-only ranking
    is always explicitly labelled as such. Missing label rows are exclusions.
    """
    if not ks or any(
        isinstance(k, bool) or not isinstance(k, int) or k < 1 for k in ks
    ):
        raise ValueError("K values must be positive integers")
    by_question = {q["question_id"]: q for q in questions}
    label_map = {}
    for row in labels:
        qid = row["question_id"]
        if qid in label_map or qid not in by_question:
            raise ValueError("Duplicate or unknown label question")
        if row.get("paper_id") != by_question[qid]["paper_id"]:
            raise ValueError("Label paper mismatch")
        if type(row.get("relevance_complete")) is not bool:
            raise ValueError("Labels must declare relevance_complete")
        relevant = row.get("relevant_passage_ids", [])
        judged = row.get("judged_passage_ids", relevant)
        if any(
            not isinstance(values, list)
            or any(not isinstance(pid, str) or not pid for pid in values)
            for values in (relevant, judged)
        ):
            raise ValueError("Label passage IDs must be lists of nonempty strings")
        if len(set(relevant)) != len(relevant) or len(set(judged)) != len(judged):
            raise ValueError("Duplicate labelled passage")
        if not set(relevant) <= set(judged):
            raise ValueError("Relevant passages must be judged")
        for pid in judged:
            if pid not in catalog or catalog[pid].paper_id != row["paper_id"]:
                raise ValueError("Unknown or cross-paper labelled passage")
        if row.get("status") not in {"mapped", "unmapped"}:
            raise ValueError("Label status must be mapped or unmapped")
        label_map[qid] = row
    report = {}
    for method, records in rankings.items():
        index = {r["question_id"]: r for r in records}
        if len(index) != len(records) or set(index) != set(by_question):
            raise ValueError("Every method must contain each question exactly once")
        per_query, exclusions = [], []
        for qid, question in by_question.items():
            record = index[qid]
            if any(record.get(k) != question[k] for k in ("paper_id", "question")):
                raise ValueError("Ranking query identity mismatch")
            ids = [h["passage"]["passage_id"] for h in record["retrieved_passages"]]
            if len(set(ids)) != len(ids):
                raise ValueError("Duplicate retrieved passage")
            for hit in record["retrieved_passages"]:
                schema = RetrievedPassage if "rrf_score" in hit else RetrievalHit
                schema.model_validate(hit)
                pid = hit["passage"]["passage_id"]
                if (
                    pid not in catalog
                    or catalog[pid].model_dump(mode="json") != hit["passage"]
                    or catalog[pid].paper_id != question["paper_id"]
                ):
                    raise ValueError("Ranking passage differs from corpus or paper")
            if [h["rank"] for h in record["retrieved_passages"]] != list(
                range(1, len(ids) + 1)
            ):
                raise ValueError("Ranking ranks must be contiguous")
            label = label_map.get(qid)
            if not label or label["status"] != "mapped":
                exclusions.append(
                    {"question_id": qid, "reason": "missing_or_unmapped_labels"}
                )
                continue
            relevant = set(label["relevant_passage_ids"])
            judged = set(label.get("judged_passage_ids", relevant))
            complete = label["relevance_complete"]
            for k in ks:
                top = ids[:k]
                known = sum(pid in judged for pid in top)
                fully_judged = complete or known == len(top)
                full = binary_metrics(ids, relevant, k) if fully_judged else None
                if full and not complete:
                    full["pool_recall_at_k"] = full.pop("recall_at_k")
                    full["pool_ndcg_at_k"] = full.pop("ndcg_at_k")
                per_query.append(
                    {
                        "question_id": qid,
                        "k": k,
                        "judged_coverage_at_k": known / len(top) if top else 1.0,
                        "returned_count": len(top),
                        "error_category": (
                            "no_passages"
                            if not top
                            else "unjudged_top_k"
                            if not fully_judged
                            else "no_relevant_judgments"
                            if not relevant
                            else "no_known_positive_at_k"
                            if not set(top) & relevant
                            else "known_positive_hit"
                        ),
                        "known_relevant_missing_at_k": sorted(relevant - set(top)),
                        "relevance_complete": complete,
                        "full_ranking": full,
                        "judged_only_compressed": binary_metrics(
                            [pid for pid in ids if pid in judged], relevant, k
                        ),
                    }
                )
        macro = []
        for k in ks:
            values = defaultdict(list)
            for row in per_query:
                if row["k"] == k and row["full_ranking"] is not None:
                    for metric, value in row["full_ranking"].items():
                        if value is not None:
                            values[metric].append(value)
            macro.append(
                {
                    "k": k,
                    "metrics": {
                        key: {"mean": sum(v) / len(v), "questions": len(v)}
                        for key, v in values.items()
                    },
                }
            )
        report[method] = {
            "macro": macro,
            "per_query": per_query,
            "exclusions": exclusions,
        }
    paired = []
    for before, after in (("bm25", "rrf"), ("dense", "rrf"), ("rrf", "rrf_bge")):
        if before not in report or after not in report:
            continue
        left = {
            (r["question_id"], r["k"]): r["full_ranking"]
            for r in report[before]["per_query"]
        }
        deltas = defaultdict(list)
        for row in report[after]["per_query"]:
            old = left.get((row["question_id"], row["k"]))
            new = row["full_ranking"]
            if old is None or new is None:
                continue
            for metric in old.keys() & new.keys():
                if old[metric] is not None and new[metric] is not None:
                    deltas[(row["k"], metric)].append(new[metric] - old[metric])
        paired.append(
            {
                "before": before,
                "after": after,
                "deltas": [
                    {
                        "k": k,
                        "metric": metric,
                        "mean_delta": sum(values) / len(values),
                        "paired_questions": len(values),
                    }
                    for (k, metric), values in sorted(deltas.items())
                ],
            }
        )
    return {
        "paired_contributions": paired,
        "protocol": "v0-proposed; binary relevance; macro over available question scores; P@K denominator K; MRR truncated at K; zero-relevant recall/nDCG null",
        "coverage_warning": "Incomplete labels yield pool-relative recall/nDCG, not exhaustive paper relevance. Compressed judged-only rankings are separate.",
        "methods": report,
    }
