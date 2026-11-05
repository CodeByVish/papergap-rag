"""Score saved agent records against gold, after the run.

The held-out run is made on questions only (`scripts/make_held_out_items.py`), so it never sees
gold. This script then compares the records it wrote with the gold and computes the same metrics
as a development run (the code is `scripts/run_agent_experiment.py:summarise`), plus the critic
audit. Development, with gold items:

    python -m scripts.score_agent_records --run-dir runs/p4/critic-fourth-40 \\
        --gold-items items.jsonl --out-dir scores/dev

Held-out, after the run, from P3's gold mapping (read only now):

    python -m scripts.score_agent_records --role held-out --freeze configs/p4_freeze.json \\
        --run-dir runs/p4/held-out --questions held_out_items.jsonl \\
        --mapping gold_evidence_mapping_all_splits.jsonl --qa data/processed/qa.jsonl \\
        --out-dir scores/held-out-all

A held-out score is refused unless the freeze record is frozen, the run's manifest matches it
(commit, corpus hash, critic view, prompt budget, retrieval settings, arms) and every arm holds
exactly the frozen questions. Run it again with `--exclude-ids` (for example the questions P4 annotated)
and a different `--out-dir` and `--label` for a subset table.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.run_agent_experiment import ARMS, WIDE_ARM, load_items_jsonl, summarise  # noqa: E402
from src.agent.experiments import (  # noqa: E402
    ExperimentItem,
    audit_critic,
    format_audit,
    format_baseline_section,
    format_table,
)
from src.agent.protocol import (  # noqa: E402
    check_coverage,
    check_run,
    freeze_problems,
    gold_items_for,
    load_freeze,
    read_jsonl,
    sha256_of,
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run-dir", type=Path, required=True, help="folder with <arm>.jsonl and run_manifest.json")
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--role", choices=["development", "held-out"], default="development")
    p.add_argument("--freeze", type=Path, help="configs/p4_freeze.json (required for --role held-out)")
    gold = p.add_argument_group("gold (one of the two)")
    gold.add_argument("--gold-items", type=Path, help="items JSONL that already carries gold")
    gold.add_argument("--questions", type=Path, help="the questions JSONL the run used")
    gold.add_argument("--mapping", type=Path, help="P3's gold_evidence_mapping_all_splits.jsonl")
    gold.add_argument("--qa", type=Path, help="data/processed/qa.jsonl (answerability)")
    p.add_argument("--only-ids", type=Path, help="JSONL with question_id: score just these")
    p.add_argument("--exclude-ids", type=Path, help="JSONL with question_id: leave these out")
    p.add_argument("--label", default="all questions", help="name of this subset in the output")
    args = p.parse_args(argv)
    if bool(args.gold_items) == bool(args.questions):
        p.error("give either --gold-items, or --questions with --mapping and --qa")
    if args.questions and not (args.mapping and args.qa):
        p.error("--questions needs --mapping and --qa")
    if args.role == "held-out" and not args.freeze:
        p.error("--role held-out needs --freeze")
    return args


def ids_in(path: Path) -> set[str]:
    return {row["question_id"] for row in read_jsonl(path)}


def load_items(args: argparse.Namespace) -> list[ExperimentItem]:
    if args.gold_items:
        return load_items_jsonl(args.gold_items)
    rows = gold_items_for(read_jsonl(args.questions), read_jsonl(args.mapping), read_jsonl(args.qa))
    return [
        ExperimentItem(
            question_id=row["question_id"], question=row["question"], paper_id=row["paper_id"],
            gold_passage_ids=frozenset(row["gold_passage_ids"]) if row.get("gold_passage_ids") else None,
            answerable=row.get("answerable"),
        )
        for row in rows
    ]


def read_arms(run_dir: Path) -> dict[str, list[dict[str, Any]]]:
    arms = {}
    for name in (*ARMS, WIDE_ARM):
        path = run_dir / f"{name}.jsonl"
        if path.exists():
            arms[name] = read_jsonl(path)
    if not arms:
        raise SystemExit(f"no <arm>.jsonl records in {run_dir}")
    return arms


def held_out_checks(args: argparse.Namespace, arms: dict[str, list[dict[str, Any]]],
                    items: Sequence[ExperimentItem]) -> list[str]:
    """Everything a held-out score must satisfy first; empty when it may proceed."""
    freeze = load_freeze(args.freeze)
    problems = [f"freeze record: {line}" for line in freeze_problems(freeze)]
    manifest_path = args.run_dir / "run_manifest.json"
    if manifest_path.exists():
        problems += [f"run: {line}" for line in check_run(json.loads(manifest_path.read_text()), freeze)]
    else:
        problems.append(f"{manifest_path} is missing")
    problems += check_coverage({n: [r["question_id"] for r in rs] for n, rs in arms.items()},
                               [item.question_id for item in items])
    return problems


def git_commit() -> str | None:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    arms = read_arms(args.run_dir)
    items = load_items(args)

    if args.role == "held-out":
        problems = held_out_checks(args, arms, items)
        if problems:
            raise SystemExit("held-out scoring refused:\n  " + "\n  ".join(problems))

    keep = {item.question_id for item in items}
    if args.only_ids:
        keep &= ids_in(args.only_ids)
    if args.exclude_ids:
        keep -= ids_in(args.exclude_ids)
    items = [item for item in items if item.question_id in keep]
    arms = {name: [r for r in rs if r["question_id"] in keep] for name, rs in arms.items()}
    if not items:
        raise SystemExit("no questions left to score")

    summary = summarise(arms, items)
    scored = len({r["question_id"] for records in arms.values() for r in records})
    report = [f"Scored: {args.label} ({scored} questions, {args.role})", "",
              format_table(summary["metrics"]) + format_baseline_section(summary)]
    if "adaptive" in arms:
        audit = audit_critic(arms["adaptive"], items)
        summary["critic_audit"] = audit
        report += ["", "Critic audit (adaptive arm):", "", format_audit(audit)]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "metrics.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (args.out_dir / "metrics.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    manifest = {
        "role": args.role, "label": args.label, "questions": scored, "run_dir": str(args.run_dir),
        "scored_with_commit": git_commit(),
        "freeze": str(args.freeze) if args.freeze else None,
        "inputs": {name: sha256_of(path) for name, path in (
            ("gold_items", args.gold_items), ("questions", args.questions), ("mapping", args.mapping),
            ("qa", args.qa), ("freeze", args.freeze)) if path},
    }
    (args.out_dir / "score_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("\n".join(report))
    print(f"\nwrote {args.out_dir}")


if __name__ == "__main__":
    main()
