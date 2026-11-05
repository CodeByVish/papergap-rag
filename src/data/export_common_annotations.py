"""Export and verify independent Markdown views of the frozen common pool.

Run ``python -m src.data.export_common_annotations run`` from the repository root.
This projection reuses saved records and never invokes retrieval or reads gold.
The separate output directory preserves the original pool's byte-bound manifest.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.data.build_annotation_pool import (
    read_jsonl,
    snapshot,
    verify_snapshot,
    write_json,
)
from src.data.build_common_pool import DEFAULT_OUTPUT as POOL
from src.data.build_common_pool import verify as verify_pool
from src.data.build_multi_retriever_pilot import (
    FOUR_METHODS,
    METHODS,
    render_multi_batches,
)

OUTPUT = POOL.with_name("annotation_common_v2_markdown")
IDENTITY_INSTRUCTION = "Enter your name or agreed identifier after `Annotator:`."


def validate_views(
    rows: list[dict], output: Path, methods: tuple[str, ...] = METHODS
) -> list[dict]:
    """Check every persisted view against source fields and independent ordering.

    Args:
        rows: Canonical pool records in saved question order.
        output: Export directory containing both annotator slots.
        methods: Frozen algorithm order used by this pool version.

    Returns:
        Per-batch coverage counts shared by both slots.

    Raises:
        ValueError: A file has missing, duplicate, reordered or altered content.
    """
    questions = {}
    for row in rows:
        questions.setdefault(row["question_id"], []).append(row)
    groups = list(questions.values())
    batches = []
    expected_paths = {
        output / f"annotator_{slot}/batch_{i:02d}.md"
        for slot in ("A", "B")
        for i in range(1, (len(groups) + 19) // 20 + 1)
    }
    if set(output.rglob("*.md")) != expected_paths:
        raise ValueError("missing or unexpected Markdown batches")
    for start in range(0, len(groups), 20):
        batch = start // 20 + 1
        selected = groups[start : start + 20]
        batches.append(
            {
                "batch": batch,
                "question_count": len(selected),
                "pair_count": sum(map(len, selected)),
            }
        )
        for slot in ("A", "B"):
            text = (output / f"annotator_{slot}/batch_{batch:02d}.md").read_text(
                encoding="utf-8"
            )
            header, *sections = text.split("\n## Question ")
            if (
                "\nAnnotator: \n" not in header
                or IDENTITY_INSTRUCTION not in header
                or "0 — Not relevant" not in header
                or "1 — Relevant" not in header
                or "`Label: 0` or `Label: 1`" not in header
                or len(sections) != len(selected)
            ):
                raise ValueError("invalid instructions or question coverage")
            for number, (section, records) in enumerate(
                zip(sections, selected), start + 1
            ):
                first = records[0]
                title = " ".join(first["paper_title"].splitlines())
                quoted_question = "\n".join(
                    "> " + line for line in first["question"].splitlines()
                )
                introduction, *parts = section.split("\n### ")
                if (
                    introduction
                    != f"{number:04d}\n\nPaper: {title}\n\n{quoted_question}\n"
                ):
                    raise ValueError("question number, title or text changed")
                if len(parts) != len(methods) + 1:
                    raise ValueError("missing or extra display groups")
                for group, part in zip(("Common Retrieved Chunks", *methods), parts):
                    # Derive membership from sources, independently of display_group.
                    members = [
                        r
                        for r in records
                        if (
                            len(r["retrieved_by"]) >= 2
                            if group == "Common Retrieved Chunks"
                            else r["retrieved_by"] == [group]
                        )
                    ]
                    members.sort(
                        key=lambda r: (
                            r["record_number"]
                            if group == "Common Retrieved Chunks"
                            else next(
                                h["rank"]
                                for h in r["retrievals"]
                                if h["method"] == group
                            )
                        )
                    )
                    group_name, body = part.split("\n\n", 1)
                    if group_name != group:
                        raise ValueError("incorrect group order")
                    if not members:
                        if body.rstrip("\n") != "None":
                            raise ValueError("empty group must show None")
                        continue
                    blocks = ("\n" + body).split("\n#### Passage ")
                    if blocks[0] or len(blocks) - 1 != len(members):
                        raise ValueError("duplicate or missing passages")
                    for block, row in zip(blocks[1:], members):
                        record = row["record_number"]
                        passage = "\n".join(
                            "> " + line for line in row["passage"].splitlines()
                        )
                        expected = (
                            f"{record}\n\nRetrieved by: "
                            + ", ".join(row["retrieved_by"])
                            + f"\n\n{passage}\n\n#### Relevance {record}\n\nLabel: "
                        )
                        if block.rstrip("\n") != expected:
                            raise ValueError(
                                "passage, attribution, order, record or blank label changed"
                            )
    return batches


def export(output: Path, pool: Path = POOL) -> dict:
    """Validate the frozen pool, create new views and save reproducibility hashes.

    Args:
        output: Unused directory; existing exports and human edits are refused.
        pool: Verified historical or four-method pool directory.

    Returns:
        Verified counts, after source and output bytes have been checked.
    """
    if output.exists():
        raise FileExistsError(output)
    counts, methods = source_pool(pool)
    inputs = snapshot(
        [
            pool / name
            for name in (
                "manifest.json",
                "pairs.jsonl",
                "questions.jsonl",
                "rankings.jsonl",
            )
        ]
    )
    rows = read_jsonl(pool / "pairs.jsonl")
    output.mkdir(parents=True)
    render_multi_batches(rows, output, methods)
    for path in sorted(output.rglob("*.md")):
        text = path.read_text(encoding="utf-8").replace(
            "Annotator: \n\n", f"Annotator: \n\n{IDENTITY_INSTRUCTION}\n\n", 1
        )
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
    batches = validate_views(rows, output, methods)
    verify_snapshot(inputs)
    write_json(
        output / "manifest.json",
        {
            "schema_version": "v0-proposed",
            "purpose": "blank source-disclosed held-out annotation views; human judgments pending",
            "inputs": inputs,
            "source_sha256": snapshot(
                [
                    Path(__file__).resolve().relative_to(Path.cwd()),
                    Path("src/data/build_multi_retriever_pilot.py"),
                ]
            ),
            "question_count": counts["question_count"],
            "pair_count_per_annotator": counts["pair_count"],
            "slots": ["A", "B"],
            "batches": batches,
            "outputs": snapshot(sorted(output.rglob("*.md"))),
            "policy": "two independent blank copies; assign distinct people in Step 4; no gold, scores, native ranks or internal IDs in views; use saved rankings for metrics",
        },
    )
    return verify(output, pool)


def source_pool(pool: Path) -> tuple[dict, tuple[str, ...]]:
    """Select the strict verifier from the source manifest's method contract.

    Args:
        pool: Complete source directory; never inferred from annotation text.

    Returns:
        Verified counts and the ordered display methods.
    """
    manifest = json.loads((pool / "manifest.json").read_text(encoding="utf-8"))
    if manifest["settings"].get("methods") == list(FOUR_METHODS):
        from src.data.build_four_method_pool import verify as verify_four

        return verify_four(pool), FOUR_METHODS
    return verify_pool(pool), METHODS


def verify(output: Path, pool: Path = POOL) -> dict:
    """Verify pristine templates and all frozen input/history hashes read-only.

    Args:
        output: Completed export; collect human-edited copies separately.
        pool: Source version whose full pair coverage is required.

    Returns:
        Counts without exposing question, passage or evidence content.
    """
    counts, methods = source_pool(pool)
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    verify_snapshot(manifest["inputs"])
    verify_snapshot(manifest["outputs"])
    batches = validate_views(read_jsonl(pool / "pairs.jsonl"), output, methods)
    if (
        manifest["batches"] != batches
        or manifest["question_count"] != counts["question_count"]
        or manifest["pair_count_per_annotator"] != counts["pair_count"]
        or manifest["slots"] != ["A", "B"]
    ):
        raise ValueError("export manifest counts differ from source")
    return {
        "question_count": counts["question_count"],
        "pair_count_per_annotator": counts["pair_count"],
        "batches_per_annotator": len(batches),
        "annotator_slots": 2,
        "initial_judgments_required": 2 * counts["pair_count"],
    }


def main() -> None:
    """Expose generation and read-only verification from the repository root.

    Neither action loads a retrieval model, samples questions or assigns labels.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("run", "verify"))
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--pool", type=Path, default=POOL)
    args = parser.parse_args()
    print(
        json.dumps(
            export(args.output, args.pool)
            if args.action == "run"
            else verify(args.output, args.pool)
        )
    )


if __name__ == "__main__":
    main()
