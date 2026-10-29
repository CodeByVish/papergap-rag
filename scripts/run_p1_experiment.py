"""Run train retrieval, or evaluate saved output with the 'evaluate' subcommand."""

import argparse
import json
import sys
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION, revision_sha
from src.retrieval.experiment import evaluate_saved_experiment, run_experiment


def evaluation_main(argv: list[str]) -> None:
    parser = argparse.ArgumentParser(
        description="Audit/score a saved P1 run without retrieval"
    )
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--evaluation-k", type=int)
    parser.add_argument("--labels", dest="labels_path", type=Path)
    parser.add_argument("--labels-manifest", dest="labels_manifest_path", type=Path)
    for flag in ("passages", "corpus-manifest", "qa", "export-manifest"):
        parser.add_argument(
            f"--{flag}", dest=flag.replace("-", "_") + "_path", type=Path
        )
    args = vars(parser.parse_args(argv))
    try:
        report = evaluate_saved_experiment(**args)
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))
    if report["status"] != "valid":
        raise SystemExit(2)


def main(argv: list[str] | None = None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "evaluate":
        evaluation_main(argv[1:])
        return
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Saved-output audit/scoring: python -m scripts.run_p1_experiment evaluate --help",
    )
    for flag in (
        "passages",
        "corpus-manifest",
        "qa",
        "export-manifest",
        "dense-index-dir",
        "output-dir",
    ):
        parser.add_argument(f"--{flag}", type=Path, required=True)
    parser.add_argument("--p3-commit", type=revision_sha, required=True)
    parser.add_argument("--p1-commit", type=revision_sha)
    parser.add_argument("--bm25-index-dir", type=Path)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--revision", type=revision_sha, default=PINNED_REVISION)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--cache-folder", type=Path)
    parser.add_argument("--local-files-only", action="store_true")
    args = vars(parser.parse_args(argv))
    for key in ("passages", "corpus_manifest", "qa", "export_manifest"):
        args[key + "_path"] = args.pop(key)
    try:
        config = run_experiment(**args)
    except (OSError, ValueError, RuntimeError) as error:
        parser.error(str(error))
    print(
        json.dumps(
            {
                "status": config["status"],
                "question_count": config["question_count"],
                "output_dir": str(Path(args["output_dir"]).resolve()),
                **config["summary"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
