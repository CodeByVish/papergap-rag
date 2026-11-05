"""System-blinded annotation views with separate provenance."""

import hashlib


def pool_candidates(rankings, questions, *, per_question=10, gold=None):
    if (
        isinstance(per_question, bool)
        or not isinstance(per_question, int)
        or per_question < 1
    ):
        raise ValueError("per_question must be a positive integer")
    gold = gold or {}
    indices = {}
    for method, rows in rankings.items():
        index = {r["question_id"]: r for r in rows}
        if len(index) != len(rows) or set(index) != {
            q["question_id"] for q in questions
        }:
            raise ValueError("Pool methods must cover identical unique questions")
        indices[method] = index
    blinded, provenance, shortfalls = [], [], []
    for question in questions:
        qid = question["question_id"]
        candidates = {}
        # Round-robin by rank across methods, with fixed method order.
        for method in sorted(indices):
            row = indices[method][qid]
            if any(row.get(k) != question[k] for k in ("paper_id", "question")):
                raise ValueError("Pool query mismatch")
            seen = set()
            for position, hit in enumerate(row["retrieved_passages"], 1):
                p = hit["passage"]
                pid = p["passage_id"]
                if (
                    p["paper_id"] != question["paper_id"]
                    or pid in seen
                    or hit["rank"] != position
                ):
                    raise ValueError("Invalid pool passage/ranking")
                seen.add(pid)
                candidate = candidates.setdefault(pid, {"passage": p, "sources": {}})
                if candidate["passage"] != p:
                    raise ValueError("Conflicting passage metadata")
                candidate["sources"][method] = {
                    "rank": hit["rank"],
                    "score": hit.get("score"),
                    "rrf_score": hit.get("rrf_score"),
                    "reranker_score": hit.get("reranker_score"),
                }
        selected = []
        for p in gold.get(qid, []):
            if p.paper_id != question["paper_id"]:
                raise ValueError("Gold pool passage belongs to another paper")
            candidates.setdefault(
                p.passage_id, {"passage": p.model_dump(mode="json"), "sources": {}}
            )
            if p.passage_id not in selected:
                selected.append(p.passage_id)
        if len(selected) > per_question:
            raise ValueError("More gold passages than pool capacity; review protocol")
        method_order = sorted(indices)
        max_rank = max(
            (s["rank"] for c in candidates.values() for s in c["sources"].values()),
            default=0,
        )
        for rank in range(1, max_rank + 1):
            for method in method_order:
                for pid, candidate in candidates.items():
                    if (
                        len(selected) < per_question
                        and pid not in selected
                        and candidate["sources"].get(method, {}).get("rank") == rank
                    ):
                        selected.append(pid)
        if len(selected) < per_question:
            shortfalls.append(
                {
                    "question_id": qid,
                    "available": len(selected),
                    "requested": per_question,
                }
            )
        for pid in sorted(
            selected,
            key=lambda pid: hashlib.sha256((qid + "\0" + pid).encode()).hexdigest(),
        ):
            record_id = hashlib.sha256((qid + "\0" + pid).encode()).hexdigest()
            blinded.append(
                {
                    "record_id": record_id,
                    **question,
                    "passage": candidates[pid]["passage"],
                }
            )
            provenance.append(
                {
                    "record_id": record_id,
                    "sources": candidates[pid]["sources"],
                    "included_as_gold": pid
                    in {p.passage_id for p in gold.get(qid, [])},
                }
            )
    return {"blinded": blinded, "provenance": provenance, "shortfalls": shortfalls}
