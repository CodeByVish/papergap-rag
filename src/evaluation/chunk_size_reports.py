"""Write reviewable chunk-size reports and import manual readability labels.

Evidence and retrieved text share one report. Readability labels are validated
against the run manifest before changing the machine-readable summary.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.evaluation.chunk_size_metrics import uncovered_spans
from src.evaluation.render_chunk_size_summary import write_summary_html


def write_json(path: Path, value: Any) -> None:
    """Write deterministic UTF-8 JSON with a final newline.

    NaN values are rejected so a saved metric cannot silently be invalid JSON.
    """
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )


def quoted_text(text: str) -> str:
    """Wrap source text in a fence longer than any embedded backtick run.

    Original paper text cannot accidentally create report headings or label rows.
    """
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}text\n{text}\n{fence}"


def evidence_section(
    question: dict[str, Any],
    annotations: list[dict[str, Any]],
    paragraphs: dict[str, dict[str, Any]],
    retrieved: list[dict[str, Any]],
    metrics: dict[str, Any],
) -> str:
    """Render one question with grouped answers, full chunks and coverage details.

    Source splits and eligibility flags are deliberately absent from this report.
    """
    lines = [
        f"## Question: {question['question_id']}",
        "### Question ID and text",
        f"Question ID: `{question['question_id']}`; paper ID: `{question['paper_id']}`.",
        quoted_text(question["question"]),
        "### Answers",
    ]
    for annotation in annotations:
        lines.extend(
            [
                f"#### Answer: {annotation['annotation_id']}",
                quoted_text(json.dumps(annotation["answer"], ensure_ascii=False)),
            ]
        )
        for loc in annotation["locations"]:
            lines.extend(
                [f"Evidence location: `{loc}`", quoted_text(paragraphs[loc]["text"])]
            )
        if not annotation["usable"]:
            lines.append(
                "Limitation: no usable complete text evidence set for this annotation."
            )
        if annotation["unresolved"]:
            lines.append(
                "Unresolved evidence:\n\n"
                + quoted_text(json.dumps(annotation["unresolved"], ensure_ascii=False))
            )
    lines.append("### Retrieved chunks")
    locations = {loc for annotation in annotations for loc in annotation["locations"]}
    for rank, item in enumerate(retrieved, 1):
        lines.extend(
            [
                f"#### Rank {rank}: {item['passage_id']}",
                f"Passage ID: `{item['passage_id']}`; retrieval score: {item['score']}.",
                f"Word count: {len(item['text'].split())}.",
                quoted_text(item["text"]),
            ]
        )
        rows = []
        for loc in sorted(locations & item["spans"].keys()):
            span = item["spans"][loc]
            label = (
                "partial"
                if uncovered_spans(paragraphs[loc]["text"], [span])
                else "full"
            )
            rows.append(f"| `{loc}` | {label} | {span[0]}:{span[1]} |")
        lines.append(
            "| Evidence location | Coverage | Character span within paragraph |\n"
            "| --- | --- | --- |\n" + "\n".join(rows)
            if rows
            else "Evidence coverage: none."
        )
    lines.extend(
        [
            "### Evaluation results",
            f"Evidence Hit@5: {str(metrics['evidence_hit_at_5']).lower()}",
            f"Complete evidence rate@5: {str(metrics['complete_evidence_at_5']).lower()}",
            f"Total retrieved words: {metrics['total_retrieved_words']}.",
            "Fully covered answer annotations: "
            + (", ".join(metrics["fully_covered_annotations"]) or "none")
            + ".",
            "Missing evidence by answer annotation:\n\n"
            + quoted_text(
                json.dumps(
                    {
                        annotation_id: {
                            key: value
                            for key, value in missing.items()
                            if key != "usable"
                        }
                        for annotation_id, missing in metrics[
                            "missing_by_annotation"
                        ].items()
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            ),
        ]
    )
    return "\n\n".join(lines) + "\n"


def readability_report(
    samples: list[dict[str, Any]],
    papers: dict[str, dict[str, Any]],
    passages: list[dict[str, Any]],
) -> tuple[str, list[str]]:
    """Render all chunks touching sampled paragraphs, with one row per unique ID.

    The full original section supplies context. The recorded character span is
    within the sampled paragraph, in original pre-normalization coordinates.
    """
    lines = ["# Readability Review"]
    seen: set[str] = set()
    for number, sample in enumerate(samples, 1):
        loc = sample["location"]
        paper = papers[sample["paper_id"]]
        context = paper["full_text"][sample["section_index"]]["paragraphs"]
        chosen = [item for item in passages if loc in item["spans"]]
        lines.extend(
            [
                f"## Source sample: {number}",
                "### Source text",
                (
                    f"Paper: {sample['paper_id']}; section: {sample['section_index']}; "
                    f"paragraphs: [{sample['paragraph_index']}]; character span: "
                    f"0:{len(sample['text'])} (within sampled paragraph)."
                ),
                "Original section context:\n\n" + quoted_text("\n\n".join(context)),
                "### Chunks (ID and text)",
            ]
        )
        for item in chosen:
            lines.extend(
                [f"Passage ID: `{item['passage_id']}`", quoted_text(item["text"])]
            )
        lines.append("### Evaluation results")
        rows = ["| Passage ID | Result | Reason |", "| --- | --- | --- |"]
        for item in chosen:
            passage_id = item["passage_id"]
            if passage_id not in seen:
                rows.append(f"| `{passage_id}` | pending | |")
                seen.add(passage_id)
        lines.append("\n".join(rows))
    return "\n\n".join(lines) + "\n", sorted(seen)


def read_readability(path: Path, expected_ids: list[str]) -> dict[str, Any]:
    """Validate manual result tables and calculate a unique-passage pass rate.

    Pending labels keep the rate null. Missing IDs, duplicate rows, unknown IDs
    and unknown labels raise ValueError instead of being counted as failures.
    Fenced source text is ignored when parsing result tables.
    """
    labels = {}
    fence = None
    in_results = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            run = len(stripped) - len(stripped.lstrip("`"))
            if fence is None:
                fence = run
            elif stripped == "`" * fence:
                fence = None
            continue
        if fence is not None:
            continue
        if line.startswith("#"):
            in_results = line == "### Evaluation results"
        if not in_results or not line.startswith("| `"):
            continue
        columns = line.split("|")
        if len(columns) < 5:
            raise ValueError(f"malformed readability result row in {path}")
        passage_id = columns[1].strip().strip("`")
        label = columns[2].strip()
        if passage_id not in expected_ids or passage_id in labels:
            raise ValueError(f"unknown or duplicate readability ID: {passage_id}")
        if label not in {"pass", "fail", "pending"}:
            raise ValueError(f"unknown readability label: {label}")
        labels[passage_id] = label
    if set(labels) != set(expected_ids):
        raise ValueError(f"missing readability result rows in {path}")
    total = len(labels)
    pending = sum(label == "pending" for label in labels.values())
    passed = sum(label == "pass" for label in labels.values())
    return {
        "value": passed / total if total and not pending else None,
        "numerator": passed,
        "denominator": total,
        "pending": pending,
    }


def summarize_readability(run_dir: Path) -> dict[str, Any]:
    """Update readability metrics only after every size's report validates.

    Evidence results remain those computed during retrieval. A malformed report
    aborts the operation before the existing summary is written.
    """
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
    for size in manifest["config"]["candidates"]:
        key = str(size)
        summary["sizes"][key]["readability_pass_rate"] = read_readability(
            run_dir / f"chunk_size_{size}" / "readability.md",
            manifest["readability_passage_ids"][key],
        )
    write_json(run_dir / "summary.json", summary)
    write_summary_html(run_dir, summary)
    return summary
