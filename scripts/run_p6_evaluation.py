"""P6 offline evaluation. Run `python -m scripts.run_p6_evaluation --help`."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
import tempfile
from importlib import metadata
from pathlib import Path

from src.evaluation.common import (
    index_rows,
    read_jsonl,
    sha256,
    write_csv,
    write_json,
    write_jsonl,
)

ROOT = Path(__file__).resolve().parents[1]


def validate_questions(rows):
    index_rows(rows)
    for row in rows:
        if any(
            not isinstance(row.get(k), str) or not row[k].strip()
            for k in ("question_id", "paper_id", "question")
        ):
            raise ValueError(
                "Questions require nonempty question_id, paper_id and question"
            )
    return rows


def check_role(args, questions):
    if args.role == "held_out":
        if not args.review:
            raise ValueError(
                "Held-out scoring requires --review with real freeze/use approval"
            )
        review = json.loads(args.review.read_text())
        if (
            review.get("usage_and_freeze_reviewed") is not True
            or not review.get("review_note", "").strip()
            or set(review.get("question_ids", []))
            != {q["question_id"] for q in questions}
        ):
            raise ValueError(
                "Review must confirm freeze/use and match exact selected question IDs"
            )


def run(args, output):
    if args.command == "export-p3":
        from src.evaluation.agreement import BASE, audit_p3

        report, _, _, _ = audit_p3(ROOT, args.ref)
        for name in (
            "questions.jsonl",
            "pairs.jsonl",
            "rankings.jsonl",
            "manifest.json",
            "frozen_config.json",
        ):
            raw = subprocess.check_output(
                [
                    "git",
                    "-C",
                    str(ROOT),
                    "show",
                    report["commit"] + ":" + BASE + "/" + name,
                ]
            )
            (output / name).write_bytes(raw)
        return {"source_commit": report["commit"]}
    if args.command in {"audit-labels", "finalize-labels"}:
        from src.evaluation.agreement import audit_p3, finalize_gold, save_audit

        report, pairs, judgments, disputes = audit_p3(ROOT, args.ref)
        if args.command == "audit-labels":
            save_audit(output, report, disputes)
        else:
            review = json.loads(args.review.read_text())
            finalize_gold(
                output,
                report,
                pairs,
                judgments,
                disputes,
                args.adjudication,
                review,
                args.corpus,
                args.disagreements,
            )
            write_json(output / "agreement.json", report)
        return {
            "source_commit": report["commit"],
            "pairs": report["pairs"],
            "agreement": report["overall"]["agreement"],
        }
    if args.command == "evidence":
        from src.evaluation.evidence import score_evidence

        questions = validate_questions(read_jsonl(args.questions))
        check_role(args, questions)
        manifest = json.loads(args.gold_manifest.read_text())
        if manifest.get("output", {}).get("sha256") != sha256(
            args.gold
        ) or manifest.get("inputs", {}).get("passages", {}).get("sha256") != sha256(
            args.corpus
        ):
            raise ValueError("P3 gold-mapping or corpus hash mismatch")
        rows, summary = score_evidence(
            questions,
            read_jsonl(args.records),
            read_jsonl(args.gold),
            read_jsonl(args.corpus),
            args.mode,
            args.arm,
            args.ks,
            args.saved_depth,
        )
        write_jsonl(output / "scores.jsonl", rows)
        write_csv(output / "evidence_recall.csv", summary)
        write_json(output / "summary.json", summary)
        return {
            "role": args.role,
            "arm": args.arm,
            "gold_mapping_manifest": str(args.gold_manifest),
        }
    if args.command == "retrieval":
        from src.evaluation.p3_rankings import score_p3

        questions = validate_questions(read_jsonl(args.questions))
        check_role(args, questions)
        labels = read_jsonl(args.labels)
        manifest = json.loads(args.labels_manifest.read_text())
        scope = set(manifest.get("question_scope", {}).get("question_ids", []))
        question_ids = {q["question_id"] for q in questions}
        if (
            manifest.get("labels_sha256") != sha256(args.labels)
            or manifest.get("corpus_sha256") != sha256(args.corpus)
            or manifest.get("annotation_coverage") != "complete"
            or manifest.get("question_scope", {}).get("project_role") != args.role
            or scope != question_ids
            or not manifest.get("source")
            or not manifest.get("mapping")
        ):
            raise ValueError("Label manifest hash, scope, role or provenance mismatch")
        for field in ("questions", "pairs", "rankings"):
            path = getattr(args, field)
            expected = manifest.get("pool_output_sha256", {}).get(
                "data/processed/annotation_common_v3/" + field + ".jsonl"
            )
            if not expected or sha256(path) != expected:
                raise ValueError("Input differs from pinned frozen P3 " + field)
        pairs, rankings = read_jsonl(args.pairs), read_jsonl(args.rankings)
        # Verify supplied corpus IDs/text; the gold export must refer to the same actual corpus.
        catalog = index_rows(read_jsonl(args.corpus), "passage_id")
        for p in pairs:
            c = catalog.get(p["passage_id"])
            if not c or c["paper_id"] != p["paper_id"] or c["text"] != p["passage"]:
                raise ValueError("Corpus differs from frozen pool")
        rows, summary = score_p3(questions, pairs, rankings, labels, args.ks)
        write_jsonl(output / "scores.jsonl", rows)
        write_csv(output / "retrieval.csv", summary)
        write_json(output / "summary.json", summary)
        return {"role": args.role, "ranking_rows": len(rankings)}
    if args.command in {"qa", "ragas"}:
        questions = validate_questions(read_jsonl(args.questions))
        check_role(args, questions)
        predictions, gold = read_jsonl(args.predictions), read_jsonl(args.references)
        if args.command == "qa":
            from src.evaluation.qa import evaluate_qa

            rows, summary = evaluate_qa(questions, predictions, gold)
        else:
            from src.evaluation.ragas_runner import (
                RagasJudge,
                prepare_samples,
                score_samples,
            )

            samples = prepare_samples(
                questions, predictions, gold, read_jsonl(args.contexts)
            )
            judge = None
            if args.live:
                if not args.judge_config:
                    raise ValueError("--live requires --judge-config")
                judge = RagasJudge(
                    json.loads(args.judge_config.read_text()), args.cache
                )
            rows, summary = score_samples(samples, judge)
            if judge:
                write_json(output / "judge_trace.json", judge.trace)
                write_json(output / "judge_config.json", judge.config)
                summary["usage_note"] = (
                    "Raw judge usage is in judge_trace.json where provider supplies it; embedding usage may be unavailable. No cost inferred."
                )
        for row in rows:
            row["arm"] = args.arm
        summary["arm"] = args.arm
        write_jsonl(output / "scores.jsonl", rows)
        write_json(output / "summary.json", summary)
        # Flat report table; full status breakdown remains in JSON.
        write_csv(
            output / (args.command + ".csv"),
            [{k: v for k, v in summary.items() if not isinstance(v, (dict, list))}],
        )
        return {"role": args.role, "arm": args.arm}
    if args.command == "contexts":
        from src.evaluation.contexts import reconstruct_contexts

        rows = reconstruct_contexts(
            read_jsonl(args.predictions),
            json.loads(args.prompt_config.read_text()),
            args.expect_prompt_version,
            args.review_note,
        )
        write_jsonl(output / "contexts.jsonl", rows)
        return {"contexts": len(rows)}
    if args.command == "performance":
        from src.evaluation.performance import summarize_performance, usage_cost

        summary = summarize_performance(
            read_jsonl(args.predictions), args.batch_seconds, args.latency_field
        )
        summary.update(
            arm=args.arm,
            hardware=args.hardware,
            concurrency=args.concurrency,
            cache_policy=args.cache_policy,
        )
        write_json(output / "summary.json", summary)
        write_csv(output / "performance.csv", [summary])
        if args.usage:
            cost = usage_cost(
                read_jsonl(args.usage),
                json.loads(args.pricing.read_text()) if args.pricing else None,
            )
            write_csv(output / "usage_cost.csv", cost)
        return {"arm": args.arm}
    if args.command == "compare":
        from src.evaluation.comparison import compare

        left, right = read_jsonl(args.left), read_jsonl(args.right)

        def select(rows, side_k):
            cutoff = side_k if side_k is not None else args.k
            if cutoff is not None:
                rows = [r for r in rows if r.get("k") == cutoff]
            if not rows:
                raise ValueError("No rows after K selection")
            if len({r.get("arm") for r in rows}) != 1:
                raise ValueError(
                    "Comparison inputs must each contain exactly one arm; select it first"
                )
            return rows

        if args.left_arm:
            left = [r for r in left if r.get("arm") == args.left_arm]
        if args.right_arm:
            right = [r for r in right if r.get("arm") == args.right_arm]
        left, right = select(left, args.left_k), select(right, args.right_k)
        summary = compare(left, right, args.metrics, args.resamples, args.seed)
        for row in summary:
            row.update(
                left_arm=left[0].get("arm"),
                right_arm=right[0].get("arm"),
                left_k=left[0].get("k"),
                right_k=right[0].get("k"),
            )
        write_csv(output / "ablation.csv", summary)
        write_json(output / "summary.json", summary)
        return {}
    raise ValueError("Unknown command")


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    subs = p.add_subparsers(dest="command", required=True)
    for name in (
        "export-p3",
        "audit-labels",
        "finalize-labels",
        "retrieval",
        "evidence",
        "qa",
        "ragas",
        "performance",
        "contexts",
        "compare",
    ):
        sub = subs.add_parser(name)
        sub.add_argument(
            "--output",
            type=Path,
            required=True,
            help="New directory; never overwrite previous results",
        )
        if name in {"export-p3", "audit-labels", "finalize-labels"}:
            sub.add_argument(
                "--ref",
                default="origin/p3-qasper-foundation",
                help="Local Git ref; no fetch performed",
            )
        if name == "finalize-labels":
            for field in ("review", "corpus"):
                sub.add_argument("--" + field, type=Path, required=True)
            sub.add_argument(
                "--disagreements",
                choices=["adjudicate", "resolved"],
                default="adjudicate",
                help="adjudicate: third-person decisions; resolved: a disclosed review",
            )
            sub.add_argument(
                "--adjudication",
                type=Path,
                required=True,
                help="Completed CSV with a final label for every disagreement",
            )
        if name in {"retrieval", "evidence", "qa", "ragas"}:
            sub.add_argument("--questions", type=Path, required=True)
            sub.add_argument(
                "--role", choices=["development", "held_out"], required=True
            )
            sub.add_argument("--review", type=Path)
        if name == "evidence":
            for field in ("records", "gold", "gold-manifest", "corpus"):
                sub.add_argument("--" + field, type=Path, required=True)
            sub.add_argument("--mode", choices=["static", "adaptive"], required=True)
            sub.add_argument("--arm", required=True)
            sub.add_argument("--ks", type=int, nargs="+")
            sub.add_argument(
                "--saved-depth",
                type=int,
                help="Actual requested depth in original static run configuration",
            )
        if name == "retrieval":
            for field in ("pairs", "rankings", "labels", "labels-manifest", "corpus"):
                sub.add_argument("--" + field, type=Path, required=True)
            sub.add_argument("--ks", nargs="+", type=int, default=[1, 3, 5])
        if name in {"qa", "ragas"}:
            for field in ("predictions", "references"):
                sub.add_argument("--" + field, type=Path, required=True)
            sub.add_argument("--arm", required=True)
        if name == "ragas":
            sub.add_argument("--contexts", type=Path, required=True)
            sub.add_argument(
                "--live",
                action="store_true",
                help="Actually call configured judge; may incur costs",
            )
            sub.add_argument("--judge-config", type=Path)
            sub.add_argument(
                "--cache", type=Path, default=Path("results/p6/judge-cache")
            )
        if name == "contexts":
            sub.add_argument("--predictions", type=Path, required=True)
            sub.add_argument("--prompt-config", type=Path, required=True)
            sub.add_argument("--expect-prompt-version", required=True)
            sub.add_argument("--review-note", required=True)
        if name == "performance":
            sub.add_argument("--predictions", type=Path, required=True)
            sub.add_argument("--arm", required=True)
            sub.add_argument("--batch-seconds", type=float)
            sub.add_argument(
                "--latency-field",
                choices=["internal_pipeline_s", "client_elapsed_s"],
                default="internal_pipeline_s",
            )
            sub.add_argument("--hardware", required=True)
            sub.add_argument("--concurrency", type=int, default=1)
            sub.add_argument("--cache-policy", required=True)
            sub.add_argument("--usage", type=Path)
            sub.add_argument("--pricing", type=Path)
        if name == "compare":
            sub.add_argument("--left", type=Path, required=True)
            sub.add_argument("--right", type=Path, required=True)
            sub.add_argument("--metrics", nargs="+", required=True)
            sub.add_argument("--k", type=int)
            sub.add_argument("--left-k", type=int)
            sub.add_argument("--right-k", type=int)
            sub.add_argument("--left-arm")
            sub.add_argument("--right-arm")
            sub.add_argument("--resamples", type=int, default=1000)
            sub.add_argument("--seed", type=int, default=42)
    return p


def main(argv=None):
    p = parser()
    args = p.parse_args(argv)
    try:
        if args.output.exists():
            raise ValueError("Output already exists; choose a new directory")
        if getattr(args, "concurrency", 1) < 1:
            raise ValueError("Concurrency must be positive")
        inputs = {
            k: {"path": str(v.resolve()), "sha256": sha256(v)}
            for k, v in vars(args).items()
            if isinstance(v, Path) and v.is_file()
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix=".p6-", dir=args.output.parent
        ) as temporary:
            output = Path(temporary) / "bundle"
            output.mkdir()
            details = run(args, output)
            source = [Path(__file__), *sorted((ROOT / "src").rglob("*.py"))]
            manifest = {
                "schema_version": "v0-proposed",
                "command": args.command,
                "python": platform.python_version(),
                "packages": {
                    name: metadata.version(name)
                    for name in ("pydantic", "ragas", "langchain-openai")
                    if name
                    in {d.metadata["Name"].lower() for d in metadata.distributions()}
                },
                "git_commit": subprocess.check_output(
                    ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
                ).strip(),
                "source_sha256": {str(f.relative_to(ROOT)): sha256(f) for f in source},
                "arguments": {
                    k: str(v) if isinstance(v, Path) else v
                    for k, v in vars(args).items()
                },
                "inputs": inputs,
                "details": details,
                "output_sha256": {
                    str(f.relative_to(output)): sha256(f)
                    for f in output.rglob("*")
                    if f.is_file()
                },
            }
            write_json(output / "run_manifest.json", manifest)
            output.rename(args.output)
        print("Wrote evaluation bundle:", args.output)
    except (
        ValueError,
        KeyError,
        TypeError,
        OSError,
        subprocess.CalledProcessError,
        ImportError,
    ) as error:
        p.exit(2, f"Evaluation stopped: {error}\n")


if __name__ == "__main__":
    main()
