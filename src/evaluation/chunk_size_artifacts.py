"""Persist and replay independent chunk-size retrieval inputs.

JSONL is the calculation source; Markdown and summary JSON are derived views.
Exact source segments preserve CRLF normalization without offset interpolation.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any

from src.evaluation.chunk_size_metrics import evaluate_question, normalized_paragraph
from src.evaluation.chunk_size_reports import evidence_section, quoted_text, write_json
from src.evaluation.render_chunk_size_summary import write_summary_html

SCHEMA = "chunk-size-inputs-v0-proposed"
DEFAULT_BUDGETS = [500, 1000, 2000]


def validate_budgets(budgets: list[int]) -> list[int]:
    """Validate and order positive word budgets before computation.

    Args:
        budgets: Nonempty list of unique integer word limits.

    Returns:
        The budgets in ascending order.
    """
    if (
        not isinstance(budgets, list)
        or not budgets
        or any(type(value) is not int or value <= 0 for value in budgets)
        or len(set(budgets)) != len(budgets)
    ):
        raise ValueError("word_budgets must be unique positive integers")
    return sorted(budgets)


def sha256(path: Path) -> str:
    """Identify exact artifact bytes for replay validation.

    Args:
        path: Local structured input file.

    Returns:
        Hexadecimal SHA-256 of the file contents.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> dict[str, str]:
    """Save ordered UTF-8 objects and return a relative file descriptor.

    Args:
        path: Destination whose parent already exists.
        rows: Records in question order and then rank order.

    Returns:
        File hash; the caller supplies its run-relative path.
    """
    path.write_text(
        "".join(
            json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n" for row in rows
        ),
        encoding="utf-8",
    )
    return {"sha256": sha256(path)}


def question_record(question: dict, annotations: list[dict], paragraphs: dict) -> dict:
    """Remove upstream split fields while retaining complete grouped evidence.

    Args:
        question: Selected upstream QA record.
        annotations: Fully located answer groups from eligibility filtering.
        paragraphs: Original paragraphs indexed by location.

    Returns:
        One independent shared question record.
    """
    locations = sorted({loc for answer in annotations for loc in answer["locations"]})
    return {
        **{key: question[key] for key in ("question_id", "paper_id", "question")},
        "annotations": [
            {
                "annotation_id": answer["annotation_id"],
                "answer": answer["answer"],
                "evidence_locations": answer["locations"],
            }
            for answer in annotations
        ],
        "evidence_paragraphs": [
            {
                key: paragraphs[loc][key]
                for key in ("location", "section_index", "paragraph_index", "text")
            }
            for loc in locations
        ],
    }


def ranked_record(question: dict, item: dict, rank: int, paragraphs: dict) -> dict:
    """Map every original character segment into an untruncated ranked chunk.

    CRLF characters form individual unequal-length segments; all other adjacent
    characters are coalesced. Source text permits independent mapping checks
    even for paragraphs that are not evidence for the current question.

    Args:
        question: Selected question identifying the paper scope.
        item: Retrieved chunk with private paragraph spans and finite score.
        rank: One-based retrieval position.
        paragraphs: All original paragraphs of the paper.

    Returns:
        Serializable ranking record with exact source segments.
    """
    segments = []
    cursor = 0
    for location, (start, end) in item["spans"].items():
        original = paragraphs[location]["text"]
        normalized, boundaries = normalized_paragraph(original)
        left, right = boundaries.index(start), boundaries.index(end)
        fragment = normalized[left:right]
        chunk_start = item["text"].find(fragment, cursor)
        if chunk_start < 0 or item["text"][cursor:chunk_start].strip():
            raise ValueError("cannot reconstruct exact chunk source mapping")
        for offset in range(left, right):
            segment = {
                "chunk_start": chunk_start + offset - left,
                "chunk_end": chunk_start + offset - left + 1,
                "location": location,
                "source_start": boundaries[offset],
                "source_end": boundaries[offset + 1],
                "source_text": original[boundaries[offset] : boundaries[offset + 1]],
            }
            if (
                segments
                and segment["source_end"] - segment["source_start"] == 1
                and segments[-1]["chunk_end"] == segment["chunk_start"]
                and segments[-1]["location"] == location
                and segments[-1]["source_end"] == segment["source_start"]
                and segments[-1]["source_end"] - segments[-1]["source_start"]
                == segments[-1]["chunk_end"] - segments[-1]["chunk_start"]
            ):
                segments[-1]["chunk_end"] = segment["chunk_end"]
                segments[-1]["source_end"] = segment["source_end"]
                segments[-1]["source_text"] += segment["source_text"]
            else:
                segments.append(segment)
        cursor = chunk_start + len(fragment)
    return {
        "question_id": question["question_id"],
        "paper_id": question["paper_id"],
        "rank": rank,
        "score": item["score"],
        "passage_id": item["passage_id"],
        "text": item["text"],
        "word_count": len(re.findall(r"\S+", item["text"])),
        "source_spans": segments,
    }


def retained_ranking(
    rows: list[dict], available: int, maximum: int
) -> tuple[list, dict]:
    """Select the shortest prefix supporting top-five and the maximum budget.

    Args:
        rows: Complete ordered ranking returned for the paper.
        available: Independently counted paper corpus size.
        maximum: Largest word budget required by the run.

    Returns:
        Retained rows and explicit completeness/retention state.
    """
    kept = []
    words = 0
    for row in rows:
        kept.append(row)
        words += row["word_count"]
        if len(kept) >= 5 and words >= maximum:
            break
    complete = len(kept) == available
    return kept, {
        "saved_count": len(kept),
        "available_count": available,
        "saved_word_count": words,
        "ranking_complete": complete,
        "retention_satisfied": complete or (len(kept) >= 5 and words >= maximum),
    }


def project_chunk(row: dict, end: int) -> dict:
    """Project a retained chunk prefix back to original paragraph coordinates.

    Args:
        row: Validated full ranking record.
        end: Exclusive chunk character boundary retained by the budget.

    Returns:
        A record accepted by the shared coverage and report implementations.
    """
    spans = {}
    for segment in row["source_spans"]:
        left, right = segment["chunk_start"], min(end, segment["chunk_end"])
        if left >= right:
            continue
        source_end = (
            segment["source_end"]
            if right == segment["chunk_end"]
            else segment["source_start"] + right - left
        )
        location = segment["location"]
        previous = spans.get(location, (segment["source_start"], source_end))
        spans[location] = (previous[0], source_end)
    return {**row, "text": row["text"][:end], "spans": spans}


def validate_mapping(row: dict, evidence: dict) -> None:
    """Reject invalid, overlapping or text-inconsistent source mappings.

    Args:
        row: One ranking record with a complete source mapping.
        evidence: Original evidence paragraphs indexed by location.

    Raises:
        ValueError: Coordinates or mapped source text cannot support exact replay.
    """
    cursor = 0
    seen = set()
    previous = None
    for span in row["source_spans"]:
        left, right, start, end = (
            span[key]
            for key in ("chunk_start", "chunk_end", "source_start", "source_end")
        )
        location = span["location"]
        parts = location.rsplit(":", 2)
        if (
            len(parts) != 3
            or parts[0] != row["paper_id"]
            or any(not value.isdigit() for value in parts[1:])
            or any(type(value) is not int for value in (left, right, start, end))
            or not 0 <= cursor <= left < right <= len(row["text"])
            or not 0 <= start < end
            or row["text"][cursor:left].strip()
        ):
            raise ValueError("invalid source mapping coordinates")
        raw = span["source_text"]
        normalized = raw.replace("\r\n", "\n").replace("\r", "\n")
        if (
            len(raw) != end - start
            or normalized != row["text"][left:right]
            or (
                end - start != right - left
                and not (raw == "\r\n" and right - left == 1)
            )
        ):
            raise ValueError("source mapping text mismatch")
        if location in evidence and evidence[location]["text"][start:end] != raw:
            raise ValueError("source mapping differs from evidence text")
        if previous and previous["location"] == location:
            if previous["source_end"] != start or previous["chunk_end"] != left:
                raise ValueError("noncontiguous source mapping")
        elif location in seen:
            raise ValueError("repeated source location within chunk")
        seen.add(location)
        cursor, previous = right, span
    if row["text"][cursor:].strip():
        raise ValueError("unmapped chunk text")


def load_inputs(run_dir: Path, manifest: dict) -> tuple[list, dict]:
    """Validate hashes, question identities, rankings and completeness states.

    Args:
        run_dir: Existing completed structured run directory.
        manifest: Provenance and expected artifact state.

    Returns:
        Ordered question records and rankings indexed by size and question ID.
    """
    if "structured_inputs" not in manifest:
        raise ValueError(
            "run has no structured inputs; reconstruct and verify under a new run ID"
        )
    storage = manifest["structured_inputs"]
    if storage["schema_version"] != SCHEMA:
        raise ValueError("unsupported structured input schema")
    files = {}
    for name, descriptor in storage["files"].items():
        path = run_dir / name
        if not path.resolve().is_relative_to(run_dir.resolve()):
            raise ValueError("artifact path escapes run directory")
        if sha256(path) != descriptor["sha256"]:
            raise ValueError(f"artifact hash mismatch: {name}")
        files[name] = [
            json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
        ]
    questions = files["questions.jsonl"]
    ids = [question["question_id"] for question in questions]
    if not ids or ids != manifest["question_ids"] or len(set(ids)) != len(ids):
        raise ValueError("question IDs/order differ from manifest")
    by_question = {question["question_id"]: question for question in questions}
    for question in questions:
        evidence = {item["location"]: item for item in question["evidence_paragraphs"]}
        referenced = set()
        annotations = question["annotations"]
        if (
            not annotations
            or len(evidence) != len(question["evidence_paragraphs"])
            or len({answer["annotation_id"] for answer in annotations})
            != len(annotations)
        ):
            raise ValueError("invalid evidence or annotation identities")
        for item in evidence.values():
            if (
                any(
                    type(item[key]) is not int or item[key] < 0
                    for key in ("section_index", "paragraph_index")
                )
                or item["location"]
                != f"{question['paper_id']}:{item['section_index']}:{item['paragraph_index']}"
                or not item["text"].strip()
            ):
                raise ValueError("invalid evidence paragraph")
        for answer in annotations:
            locations = answer["evidence_locations"]
            if (
                not locations
                or len(set(locations)) != len(locations)
                or set(locations) - evidence.keys()
            ):
                raise ValueError("answer lacks complete evidence")
            referenced.update(locations)
        if referenced != evidence.keys():
            raise ValueError("unreferenced evidence paragraph")
    rankings = {}
    for size in manifest["config"]["candidates"]:
        key = str(size)
        grouped = {qid: [] for qid in ids}
        order = []
        for row in files[f"chunk_size_{size}/ranked_chunks.jsonl"]:
            qid = row["question_id"]
            if qid not in grouped or row["paper_id"] != by_question[qid]["paper_id"]:
                raise ValueError("unknown question or wrong-paper ranking")
            grouped[qid].append(row)
            order.append(ids.index(qid))
        if order != sorted(order):
            raise ValueError("ranking question order differs from shared questions")
        states = storage["ranking_states"][key]
        if set(states) != set(ids):
            raise ValueError("ranking state question set mismatch")
        for qid, rows in grouped.items():
            evidence = {
                item["location"]: item
                for item in by_question[qid]["evidence_paragraphs"]
            }
            previous = None
            seen = set()
            for rank, row in enumerate(rows, 1):
                if (
                    type(row["rank"]) is not int
                    or row["rank"] != rank
                    or not isinstance(row["score"], (int, float))
                    or isinstance(row["score"], bool)
                    or not math.isfinite(row["score"])
                    or row["passage_id"] in seen
                    or not isinstance(row["passage_id"], str)
                    or not row["passage_id"]
                    or type(row["word_count"]) is not int
                    or row["word_count"] <= 0
                    or row["word_count"] != len(re.findall(r"\S+", row["text"]))
                ):
                    raise ValueError("invalid rank, score, passage ID or word count")
                current = (-row["score"], row["passage_id"])
                if previous is not None and current < previous:
                    raise ValueError("ranking is not score-descending / ID-ascending")
                previous = current
                seen.add(row["passage_id"])
                validate_mapping(row, evidence)
            state = states[qid]
            words = sum(row["word_count"] for row in rows)
            available = state["available_count"]
            complete = len(rows) == available
            satisfied = complete or (
                len(rows) >= 5 and words >= max(manifest["config"]["word_budgets"])
            )
            if (
                type(available) is not int
                or available < len(rows)
                or state["saved_count"] != len(rows)
                or state["saved_word_count"] != words
                or state["ranking_complete"] is not complete
                or state["retention_satisfied"] is not satisfied
            ):
                raise ValueError("inconsistent ranking completeness state")
        rankings[key] = grouped
    return questions, rankings


def calculate_question(
    question: dict, rows: list[dict], state: dict, budgets: list[int]
) -> tuple[dict, str]:
    """Compute top-five and all budget views once for JSON and Markdown.

    Args:
        question: Validated standalone evidence record.
        rows: Validated full chunks in retrieval order.
        state: Independently verified saved/available counts.
        budgets: Ordered word limits requested for replay.

    Returns:
        Per-question metrics and the matching Markdown section.
    """
    if not state["ranking_complete"] and (
        len(rows) < 5 or sum(row["word_count"] for row in rows) < max(budgets)
    ):
        raise ValueError(
            "insufficient saved ranking; extend retrieval under a new run ID"
        )
    paragraphs = {item["location"]: item for item in question["evidence_paragraphs"]}
    annotations = [
        {
            **answer,
            "locations": answer["evidence_locations"],
            "usable": True,
            "unresolved": [],
        }
        for answer in question["annotations"]
    ]
    full = [project_chunk(row, len(row["text"])) for row in rows]
    top = evaluate_question(annotations, paragraphs, full[:5])
    result = {
        "question_id": question["question_id"],
        **top,
        "retrieved": [
            {"passage_id": row["passage_id"], "score": row["score"]} for row in rows[:5]
        ],
        "budgets": {},
    }
    report = evidence_section(question, annotations, paragraphs, full, top)
    for budget in budgets:
        remaining = budget
        retained = []
        selections = []
        for row in rows:
            if remaining == 0:
                break
            count = min(remaining, row["word_count"])
            end = (
                len(row["text"])
                if count == row["word_count"]
                else list(re.finditer(r"\S+", row["text"]))[count - 1].end()
            )
            chunk = project_chunk(row, end)
            retained.append(chunk)
            selections.append(
                {
                    "passage_id": row["passage_id"],
                    "rank": row["rank"],
                    "retained_words": count,
                    "chunk_character_span": [0, end],
                    "evidence_spans": {
                        loc: span
                        for loc, span in chunk["spans"].items()
                        if loc in paragraphs
                    },
                }
            )
            remaining -= count
        metrics = evaluate_question(annotations, paragraphs, retained)
        value = {
            "budget_words": budget,
            "actual_words": budget - remaining,
            "unused_words": remaining,
            "corpus_exhausted": state["ranking_complete"] and remaining > 0,
            "evidence_hit": metrics["evidence_hit_at_5"],
            "complete_evidence": metrics["complete_evidence_at_5"],
            "fully_covered_annotations": metrics["fully_covered_annotations"],
            "missing_by_annotation": metrics["missing_by_annotation"],
            "retained_chunks": selections,
        }
        result["budgets"][str(budget)] = value
        report += f"\n#### Word budget: {budget}\n\n"
        report += "| Budget words | Actual words | Unused words | Evidence hit | Complete evidence | Corpus exhausted |\n| --- | --- | --- | --- | --- | --- |\n"
        report += f"| {budget} | {value['actual_words']} | {remaining} | {str(value['evidence_hit']).lower()} | {str(value['complete_evidence']).lower()} | {str(value['corpus_exhausted']).lower()} |\n\n"
        report += quoted_text(json.dumps(value, ensure_ascii=False, indent=2)) + "\n"
    return result, report


def generate_reports(
    run_dir: Path, budgets: list[int] | None = None, *, manifest: dict | None = None
) -> dict:
    """Regenerate derived reports without loading raw data or a retriever.

    All inputs and requested budgets validate before any derived file is written.
    Existing readability labels and run timing/corpus metadata are preserved.

    Args:
        run_dir: Completed run with structured input manifest.
        budgets: Optional replacement budgets supported by saved rankings.
        manifest: In-memory manifest used before the runner's completion marker.

    Returns:
        The regenerated machine-readable summary.
    """
    if manifest is None:
        manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    validate_budgets(manifest["config"]["word_budgets"])
    questions, rankings = load_inputs(run_dir, manifest)
    budgets = validate_budgets(
        manifest["config"]["word_budgets"] if budgets is None else budgets
    )
    summary_path = run_dir / "summary.json"
    summary = (
        json.loads(summary_path.read_text(encoding="utf-8"))
        if summary_path.exists()
        else {
            "schema_version": "v0-proposed",
            "run_id": manifest["run_id"],
            "sizes": {},
        }
    )
    summary["word_budgets"] = budgets
    reports = {}
    for size, grouped in rankings.items():
        results, sections = [], ["# Evidence Review\n"]
        old = summary["sizes"].get(size, {})
        timings = {
            row["question_id"]: row.get("retrieval_seconds")
            for row in old.get("questions", [])
        }
        for question in questions:
            qid = question["question_id"]
            result, section = calculate_question(
                question,
                grouped[qid],
                manifest["structured_inputs"]["ranking_states"][size][qid],
                budgets,
            )
            if timings.get(qid) is not None:
                result["retrieval_seconds"] = timings[qid]
            results.append(result)
            sections.append(section)
        count = len(results)
        value = {**old, "questions": results}
        if "readability_pass_rate" not in value:
            pending = len(manifest.get("readability_passage_ids", {}).get(size, []))
            value["readability_pass_rate"] = {
                "value": None,
                "numerator": 0,
                "denominator": pending,
                "pending": pending,
            }
        for name, field in (
            ("evidence_hit_at_5", "evidence_hit_at_5"),
            ("complete_evidence_rate_at_5", "complete_evidence_at_5"),
            ("retrieved_word_count", "total_retrieved_words"),
        ):
            total = sum(row[field] for row in results)
            value[name] = {
                "value": total / count,
                "numerator": total,
                "denominator": count,
            }
        value["budgets"] = {}
        for budget in budgets:
            items = [row["budgets"][str(budget)] for row in results]
            aggregate = {
                "question_count": count,
                "corpus_exhausted_count": sum(row["corpus_exhausted"] for row in items),
            }
            for name, field in (
                ("evidence_hit", "evidence_hit"),
                ("complete_evidence_rate", "complete_evidence"),
                ("actual_word_count", "actual_words"),
            ):
                total = sum(row[field] for row in items)
                aggregate[name] = {
                    "value": total / count,
                    "numerator": total,
                    "denominator": count,
                }
            value["budgets"][str(budget)] = aggregate
        summary["sizes"][size] = value
        reports[size] = "\n".join(sections)
    if "validation_plan" in manifest:
        from src.evaluation.chunk_size_validation import (
            add_validation_summary,
            write_validation_report,
        )

        plan = manifest["validation_plan"]
        if sha256(run_dir / "question_plan.json") != manifest["question_plan_sha256"]:
            raise ValueError("frozen question plan hash mismatch")
        if json.loads((run_dir / "question_plan.json").read_text(encoding="utf-8")) != plan:
            raise ValueError("question plan differs from manifest")
        add_validation_summary(summary, plan, budgets)
        write_validation_report(run_dir, summary)
    for size, report in reports.items():
        (run_dir / f"chunk_size_{size}" / "evidence_review.md").write_text(
            report, encoding="utf-8"
        )
    write_json(summary_path, summary)
    write_summary_html(run_dir, summary)
    return summary
