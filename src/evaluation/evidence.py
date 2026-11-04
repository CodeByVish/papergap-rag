"""Mapped-passage recall for static ranked depths and adaptive cumulative retrieval.

This uses P3 mapping IDs, not human pool labels or generator-visible context.
The per-question set arithmetic matches P4's recall definition. Failure-inclusive
and successful-only means are both reported to make denominators explicit.
"""

from src.evaluation.common import index_rows, mean


def ids_list(values):
    if (
        not isinstance(values, list)
        or not all(isinstance(x, str) and x.strip() for x in values)
        or len(values) != len(set(values))
    ):
        raise ValueError(
            "Passage IDs must be a unique ordered list of nonempty strings"
        )
    return values


def retrieval_rounds(record):
    if "retrieval_log" in record:
        log = record["retrieval_log"]
        if not isinstance(log, list) or not log:
            raise ValueError(
                "Successful agent record requires a nonempty retrieval_log"
            )
        if [r["round"] for r in log] != list(range(1, len(log) + 1)):
            raise ValueError("Retrieval rounds must be contiguous in original order")
        return [ids_list(r["passage_ids"]) for r in log]
    if "retrieved_passage_ids" in record:
        return [ids_list(record["retrieved_passage_ids"])]
    if "hits" in record:
        hits = record["hits"]
        if [h["rank"] for h in hits] != list(range(1, len(hits) + 1)):
            raise ValueError("Saved ranks must be contiguous")
        return [
            ids_list(
                [
                    h.get("passage_id", h.get("passage", {}).get("passage_id"))
                    for h in hits
                ]
            )
        ]
    raise ValueError(
        "Provide original agent retrieval_log, ranked hits, or retrieved_passage_ids"
    )


def score_evidence(
    questions, records, mapping, corpus, mode, arm, ks=None, saved_depth=None
):
    qmap, rmap, gmap = map(index_rows, (questions, records, mapping))
    catalog = index_rows(corpus, "passage_id")
    if set(rmap) - set(qmap):
        raise ValueError("Retrieval records outside selected scope")
    if mode not in {"static", "adaptive"}:
        raise ValueError("Mode must be static or adaptive")
    if mode == "static":
        if (
            not ks
            or any(type(k) is not int or k < 1 for k in ks)
            or len(set(ks)) != len(ks)
        ):
            raise ValueError("Static scoring requires distinct positive K values")
        if type(saved_depth) is not int or saved_depth < max(ks):
            raise ValueError(
                "Saved retrieval depth from original run configuration must cover every K"
            )
    elif ks or saved_depth is not None:
        raise ValueError(
            "Adaptive scoring is cumulative across rounds, not a top-K ranking"
        )

    def validate_ids(ids, q):
        if any(
            pid not in catalog or catalog[pid]["paper_id"] != q["paper_id"]
            for pid in ids
        ):
            raise ValueError(
                "Unknown or cross-paper passage ID; this scorer is paper-scoped"
            )

    rows = []
    for qid, q in qmap.items():
        g, r = gmap.get(qid), rmap.get(qid)
        base = {"question_id": qid, "paper_id": q["paper_id"], "arm": arm, "mode": mode}
        status = "ok"
        gold = set()
        if g is None:
            status = "missing_mapping"
        else:
            if (
                g.get("paper_id") != q["paper_id"]
                or g.get("question", q["question"]) != q["question"]
            ):
                raise ValueError("Mapping query identity mismatch")
            gold = set(ids_list(g["gold_passage_ids"]))
            validate_ids(gold, q)
            if not gold:
                status = "empty_mapping"
        rounds = []
        if r is not None:
            if (
                r.get("paper_id", q["paper_id"]) != q["paper_id"]
                or r.get("question", q["question"]) != q["question"]
            ):
                raise ValueError("Retrieval query identity mismatch")
            if not r.get("error"):
                rounds = retrieval_rounds(r)
                if mode == "static" and len(rounds) != 1:
                    raise ValueError(
                        "Static scoring requires exactly one retrieval round"
                    )
                for ids in rounds:
                    validate_ids(ids, q)
                if mode == "static" and len(rounds[0]) > saved_depth:
                    raise ValueError("Actual ranking exceeds declared saved depth")
        if status == "ok" and (r is None or r.get("error")):
            status = "missing_prediction" if r is None else "retrieval_error"
        # answer_error is not a retrieval failure: retrieval still earns its actual recall.
        for k in ks if mode == "static" else [None]:
            found = (
                set(rounds[0][:k])
                if rounds and mode == "static"
                else set().union(*map(set, rounds))
                if rounds
                else set()
            )
            first = (found if mode == "static" else set(rounds[0])) if rounds else set()
            valid = bool(gold)
            recall = len(found & gold) / len(gold) if valid else None
            rows.append(
                {
                    **base,
                    "k": k,
                    "status": status,
                    "gold_count": len(gold),
                    "retrieved_count": len(found),
                    "matched_gold_count": len(found & gold),
                    "retrieval_rounds": len(rounds),
                    "retrieval_status": "missing_prediction"
                    if r is None
                    else "retrieval_error"
                    if r.get("error")
                    else "ok",
                    "mapped_recall": recall,
                    "successful_only_mapped_recall": recall if status == "ok" else None,
                    "mapped_recall_first_round": len(first & gold) / len(gold)
                    if valid
                    else None,
                    "answerable": answerable(g) if g else None,
                }
            )
    summary = []
    for k in ks if mode == "static" else [None]:
        selected = [r for r in rows if r["k"] == k]
        summary.append(
            {
                "arm": arm,
                "mode": mode,
                "k": k,
                "questions": len(selected),
                "mapped_recall": mean(r["mapped_recall"] for r in selected),
                "mapped_recall_n": sum(
                    r["mapped_recall"] is not None for r in selected
                ),
                "successful_only_mapped_recall": mean(
                    r["mapped_recall"] for r in selected if r["status"] == "ok"
                ),
                "successful_only_n": sum(r["status"] == "ok" for r in selected),
                "mapping_exclusions": sum(
                    r["status"] in {"missing_mapping", "empty_mapping"}
                    for r in selected
                ),
                "retrieval_failures": sum(
                    r["retrieval_status"] != "ok" for r in selected
                ),
                "mean_retrieved_count": mean(r["retrieved_count"] for r in selected),
                "definition": "mapped gold passage ID overlap; not pool recall or paragraph coverage",
            }
        )
    return rows, summary


def answerable(row):
    if "answerable" in row:
        if type(row["answerable"]) is not bool:
            raise ValueError("answerable must be boolean")
        return row["answerable"]
    annotations = row.get("annotations", [])
    if not annotations:
        return None
    flags = [a.get("answer", {}).get("unanswerable") for a in annotations]
    if not all(type(flag) is bool for flag in flags):
        raise ValueError("Mapping annotations lack valid answerability flags")
    return not all(flags)
