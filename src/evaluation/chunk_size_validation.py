"""Freeze expanded development samples and compare candidates on paired questions.

Round-four plans preserve the reference questions and readability sources while
holding new questions aside from the earlier search. No test data is introduced.
"""

from __future__ import annotations

import itertools
import json
import random
from collections import Counter
from pathlib import Path

from src.evaluation.chunk_size_artifacts import load_inputs, sha256


def freeze_plan(eligible: list[dict], config: dict, inputs: dict) -> tuple[dict, dict]:
    """Validate the reference experiment and freeze ordered old and new IDs.

    Args:
        eligible: Questions passing the unchanged evidence and corpus filters.
        config: Normalized experiment settings including validation controls.
        inputs: Current input descriptors, including exact SHA-256 hashes.

    Returns:
        A reusable sampling plan and the validated reference manifest.

    Raises:
        ValueError: Inputs, controls, or reference questions have changed.
    """
    settings = config["validation"]
    directory = Path(settings["reference_run"])
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    load_inputs(directory, manifest)
    for name in ("papers", "qa", "export_manifest"):
        if inputs[name]["sha256"] != manifest["inputs"][name]["sha256"]:
            raise ValueError(f"reference input hash changed: {name}")
    for key in (
        "overlap_words",
        "top_k",
        "word_budgets",
        "seed",
        "retrieval",
        "n_paper",
        "n_paragraph",
    ):
        if config[key] != manifest["config"][key]:
            raise ValueError(f"reference control changed: {key}")
    if not set(config["candidates"]) <= set(manifest["config"]["candidates"]):
        raise ValueError("validation candidates must have reference results")
    by_id = {question["question_id"]: question for question in eligible}
    old = manifest["question_ids"]
    if not set(old) <= by_id.keys():
        raise ValueError("reference questions no longer eligible")
    pool = sorted(set(by_id) - set(old))
    new = random.Random(config["seed"]).sample(
        pool, min(settings["additional_question_count"], len(pool))
    )
    if not new:
        raise ValueError("no unused eligible validation questions")
    groups = {"regression": old, "new": new, "combined": old + new}
    descriptions = {}
    for name, ids in groups.items():
        papers = sorted({by_id[qid]["paper_id"] for qid in ids})
        descriptions[name] = {
            "question_ids": ids,
            "question_count": len(ids),
            "paper_ids": papers,
            "paper_count": len(papers),
            "source_split_counts": dict(
                Counter(by_id[qid]["source_split"] for qid in ids)
            ),
        }
    return {
        "schema_version": "chunk-size-validation-v0-proposed",
        "config": config,
        "inputs": inputs,
        "reference_files": {
            name: sha256(directory / name)
            for name in ("manifest.json", "summary.json", "questions.jsonl")
        },
        "seed": config["seed"],
        "eligible_count": len(eligible),
        "unused_eligible_count": len(pool),
        "additional_count_requested": settings["additional_question_count"],
        "primary_word_budget": settings["primary_word_budget"],
        "primary_metric": "complete_evidence_rate",
        "groups": descriptions,
        "overlapping_paper_ids": sorted(
            set(descriptions["regression"]["paper_ids"])
            & set(descriptions["new"]["paper_ids"])
        ),
        "readability_samples": manifest["readability_samples"],
    }, manifest


def verify_regression(run_dir: Path, manifest: dict) -> None:
    """Require exact old-question rankings and metrics before completing a run.

    Args:
        run_dir: New run with complete structured rankings and derived metrics.
        manifest: In-memory manifest containing the frozen validation plan.

    Raises:
        ValueError: Any source sample, corpus, ranking or metric has drifted.
    """
    plan = manifest["validation_plan"]
    reference = Path(plan["config"]["validation"]["reference_run"])
    old_manifest = json.loads((reference / "manifest.json").read_text(encoding="utf-8"))
    old_questions, old_rankings = load_inputs(reference, old_manifest)
    questions, rankings = load_inputs(run_dir, manifest)
    count = len(old_questions)
    if (
        questions[:count] != old_questions
        or manifest["readability_samples"] != old_manifest["readability_samples"]
    ):
        raise ValueError("regression question records or readability sources changed")
    summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
    previous = json.loads((reference / "summary.json").read_text(encoding="utf-8"))
    for size, rows in summary["sizes"].items():
        if rows["corpus_sha256"] != previous["sizes"][size]["corpus_sha256"]:
            raise ValueError(f"regression corpus changed: {size}")
        for current, old in zip(
            rows["questions"][:count], previous["sizes"][size]["questions"], strict=True
        ):
            qid = old["question_id"]
            if rankings[size][qid] != old_rankings[size][qid] or {
                key: value
                for key, value in current.items()
                if key != "retrieval_seconds"
            } != {
                key: value for key, value in old.items() if key != "retrieval_seconds"
            }:
                raise ValueError(f"regression results changed: {size}/{qid}")


def aggregate_group(rows: list[dict], budgets: list[int]) -> dict:
    """Aggregate one nonempty question group without mixing its denominator.

    Args:
        rows: Per-question results from the shared structured calculation.
        budgets: Word budgets supported by those results.

    Returns:
        Top-five and budget metrics with explicit numerators and denominators.
    """
    count = len(rows)
    result = {"question_count": count, "budgets": {}}
    views = [
        (
            result,
            rows,
            (
                ("evidence_hit_at_5", "evidence_hit_at_5"),
                ("complete_evidence_rate_at_5", "complete_evidence_at_5"),
                ("retrieved_word_count", "total_retrieved_words"),
            ),
        )
    ]
    for budget in budgets:
        items = [row["budgets"][str(budget)] for row in rows]
        target = {
            "question_count": count,
            "corpus_exhausted_count": sum(row["corpus_exhausted"] for row in items),
        }
        result["budgets"][str(budget)] = target
        views.append(
            (
                target,
                items,
                (
                    ("evidence_hit", "evidence_hit"),
                    ("complete_evidence_rate", "complete_evidence"),
                    ("actual_word_count", "actual_words"),
                ),
            )
        )
    for target, items, fields in views:
        for name, field in fields:
            total = sum(row[field] for row in items)
            target[name] = {
                "value": total / count,
                "numerator": total,
                "denominator": count,
            }
    return result


def add_validation_summary(summary: dict, plan: dict, budgets: list[int]) -> None:
    """Attach group metrics and directional paired gains/losses to a summary.

    Args:
        summary: Mutable machine-readable comparison with per-question results.
        plan: Frozen group membership and the predeclared primary budget.
        budgets: Budgets used in the current report rendering.
    """
    summary["validation"] = {
        "primary_word_budget": plan["primary_word_budget"],
        "primary_metric": plan["primary_metric"],
        "groups": {},
        "paired_comparisons": {},
    }
    for group, description in plan["groups"].items():
        ids = description["question_ids"]
        grouped = {}
        indexed = {}
        for size, value in summary["sizes"].items():
            indexed[size] = {row["question_id"]: row for row in value["questions"]}
            grouped[size] = aggregate_group(
                [indexed[size][qid] for qid in ids], budgets
            )
        summary["validation"]["groups"][group] = {**description, "sizes": grouped}
        pairs = []
        for left, right in itertools.combinations(sorted(indexed, key=int), 2):
            views = {"top_5": ("evidence_hit_at_5", "complete_evidence_at_5")}
            views.update(
                {
                    str(budget): ("evidence_hit", "complete_evidence")
                    for budget in budgets
                }
            )
            for view, fields in views.items():
                for metric in fields:
                    gains, losses = [], []
                    for qid in ids:
                        a, b = indexed[left][qid], indexed[right][qid]
                        if view != "top_5":
                            a, b = a["budgets"][view], b["budgets"][view]
                        if a[metric] and not b[metric]:
                            gains.append(qid)
                        if b[metric] and not a[metric]:
                            losses.append(qid)
                    pairs.append(
                        {
                            "left": left,
                            "right": right,
                            "view": view,
                            "metric": metric,
                            "left_only_question_ids": gains,
                            "right_only_question_ids": losses,
                            "left_only_count": len(gains),
                            "right_only_count": len(losses),
                        }
                    )
        summary["validation"]["paired_comparisons"][group] = pairs


def write_validation_report(run_dir: Path, summary: dict) -> None:
    """Write the concise validation report from the same computed group metrics.

    Args:
        run_dir: Existing comparison output directory.
        summary: Grouped summary with paired question IDs available in JSON.
    """
    validation = summary["validation"]
    primary = validation["primary_word_budget"]
    lines = [
        "# Round 4 validation",
        "",
        f"Primary: complete evidence rate at ${primary}$ words, declared before retrieval. New questions are the main validation group; regression and combined groups are reported separately.",
        "",
        "| Group | Size (words) | Budget | Evidence hit | Complete evidence | Mean actual words | Exhausted |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for group, description in validation["groups"].items():
        for size, value in description["sizes"].items():
            for budget, row in value["budgets"].items():
                hit, complete = row["evidence_hit"], row["complete_evidence_rate"]
                lines.append(
                    f"| {group} | ${size}$ | ${budget}$ | ${hit['numerator']}/{hit['denominator']}$ | ${complete['numerator']}/{complete['denominator']}$ | ${row['actual_word_count']['value']:.2f}$ | ${row['corpus_exhausted_count']}$ |"
                )
    lines.extend(
        [
            "",
            "| New questions: left / right | View | Metric | Left only | Right only |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in validation["paired_comparisons"]["new"]:
        lines.append(
            f"| {row['left']} / {row['right']} | {row['view']} | `{row['metric']}` | ${row['left_only_count']}$ | ${row['right_only_count']}$ |"
        )
    lines.extend(
        [
            "",
            "Top-5 metrics, exact paired question IDs, group paper IDs and split counts are in `summary.json`; `summary.html` shows all group aggregates. New questions may share papers with regression questions. Small differences do not establish significance or a stable optimum. Do not redraw the sample or continue a dense search on these questions. Readability review and final configuration selection remain pending; conclusions apply to BM25 only. Shared interfaces remain `v0-proposed`.",
            "",
        ]
    )
    (run_dir / "report.md").write_text("\n".join(lines), encoding="utf-8")
