"""Freeze question-isolated annotation pools using the existing BM25 adapter.

Run prepare, pilot, freeze and export in order through the companion CLI.
Eligibility checks expose only identifiers and corpus metadata before sampling.
Gold references are joined only after retrieval and never enter blind views.
"""

from __future__ import annotations

import hashlib
import json
import platform
import random
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

from src.data.export_evidence_mapping import file_hash
from src.evaluation.chunk_size_retrieval import (
    make_retriever_factory,
    retriever_metadata,
)

DATA = Path("data/processed")
HISTORY = Path("results/chunk_size/round4_bm25_20261028_01")
QUESTION_FIELDS = ("question_id", "paper_id", "question", "source_split")
SEED = 20261028
SETTINGS = {"chunk_size_words": 365, "chunk_overlap_words": 40, "top_k": 5}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read structured records without printing their potentially private text.

    Args:
        path: UTF-8 JSONL artifact; retired annotation data may live in Git.

    Returns:
        Parsed rows in persisted order.
    """
    return [json.loads(line) for line in artifact_bytes(path).decode("utf-8").splitlines()]


def write_json(path: Path, value: Any) -> None:
    """Create a new JSON artifact and refuse replacement of an earlier freeze.

    Args:
        path: Unused output location.
        value: JSON-compatible metadata.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        )


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """Create an ordered JSONL source, keeping labels explicitly null.

    Args:
        path: New output path.
        rows: Records whose order defines stable record numbering.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def unique_rows(rows: list[dict], key: str) -> dict[str, dict]:
    """Index records and reject repeated or empty identifiers.

    Args:
        rows: Parsed source records.
        key: Identifier field shared by all rows.

    Returns:
        Identifier-to-record mapping.
    """
    indexed = {row[key]: row for row in rows}
    if len(indexed) != len(rows) or any(not key for key in indexed):
        raise ValueError("duplicate or empty identifiers")
    return indexed


def code_identity() -> dict:
    """Record HEAD, dirty status and exact implementation hashes.

    Returns:
        A fingerprint that also distinguishes uncommitted source revisions.
    """
    paths = sorted([*Path("src").rglob("*.py"), *Path("scripts").glob("*.py")])
    return {
        "python": platform.python_version(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "working_tree_status": subprocess.check_output(
            ["git", "status", "--short"], text=True, encoding="utf-8"
        ).splitlines(),
        "source_sha256": {p.as_posix(): file_hash(p) for p in paths},
    }


def snapshot(paths: list[Path]) -> dict[str, str]:
    """Hash exact inputs without exposing their contents.

    Args:
        paths: Existing files required for reproduction.

    Returns:
        Repository-relative paths mapped to SHA-256 values.
    """
    return {p.as_posix(): artifact_hash(p) for p in paths}


def artifact_bytes(path: Path) -> bytes:
    """Read current bytes or a deliberately removed legacy data blob from Git.

    Args:
        path: Repository-relative data artifact. Git fallback is restricted to
            explicitly retired annotation directories removed from the checkout.

    Returns:
        Exact current bytes, or the last added/modified Git blob for a missing
        legacy artifact. Callers still check its pre-existing manifest hash.

    Raises:
        FileNotFoundError: A current input or an unarchived artifact is absent.
    """
    if path.is_file():
        return path.read_bytes()
    legacy = {
        "annotation_held_out",
        "annotation_pilot",
        "annotation_pilot_multi_v1",
        "annotation_pilot_multi_v2",
        "annotation_common_v2",
        "annotation_common_v2_markdown",
    }
    if (
        path.is_absolute()
        or path.parts[:2] != ("data", "processed")
        or len(path.parts) < 4
        or path.parts[2] not in legacy
    ):
        raise FileNotFoundError(path)
    commit = subprocess.check_output(
        ["git", "log", "-1", "--diff-filter=AM", "--format=%H", "--", path.as_posix()],
        text=True,
    ).strip()
    if not commit:
        raise FileNotFoundError(path)
    return subprocess.check_output(["git", "show", f"{commit}:{path.as_posix()}"])


def artifact_hash(path: Path) -> str:
    """Hash current or archived legacy bytes without restoring deleted files.

    Args:
        path: Artifact accepted by artifact_bytes; existing files take priority.

    Returns:
        SHA-256 digest compared against immutable generation-time manifests.
    """
    return (
        file_hash(path)
        if path.is_file()
        else hashlib.sha256(artifact_bytes(path)).hexdigest()
    )


def verify_snapshot(hashes: dict[str, str]) -> None:
    """Reject input replacement between preparation, freeze and export.

    Args:
        hashes: Persisted path-to-SHA-256 mapping.
    """
    for name, expected in hashes.items():
        if artifact_hash(Path(name)) != expected:
            raise ValueError(f"frozen file changed: {name}")


def load_corpus(data: Path) -> list[dict]:
    """Verify the fixed all-paper corpus and mapping companion hashes.

    Args:
        data: Processed data directory.

    Returns:
        Unique, nonempty passage records with original IDs.
    """
    path = data / "passages_all_paper_text.jsonl"
    manifest = json.loads(
        (data / "passages_all_paper_text.manifest.json").read_text(encoding="utf-8")
    )
    gold_path = data / "gold_evidence_mapping_all_splits.jsonl"
    gold_manifest = json.loads(
        (data / "gold_evidence_mapping_all_splits.manifest.json").read_text(
            encoding="utf-8"
        )
    )
    if any(
        manifest["chunking"][key] != SETTINGS[key]
        for key in ("chunk_size_words", "chunk_overlap_words")
    ):
        raise ValueError("annotation requires the fixed 365/40 corpus")
    if manifest["scope"] != "all-paper-text" or manifest["output"][
        "sha256"
    ] != file_hash(path):
        raise ValueError("invalid corpus scope or hash")
    if gold_manifest["output"]["sha256"] != file_hash(gold_path):
        raise ValueError("gold mapping hash mismatch")
    if gold_manifest["inputs"]["passages"]["sha256"] != file_hash(path):
        raise ValueError("gold mapping uses a different corpus")
    for name in ("papers", "qa", "export_manifest", "passages_manifest"):
        item = gold_manifest["inputs"][name]
        if file_hash(data / item["file"]) != item["sha256"]:
            raise ValueError(f"gold mapping input changed: {name}")
    rows = read_jsonl(path)
    unique_rows(rows, "passage_id")
    if len(rows) != manifest["output"]["passage_count"] or any(
        not row["text"].strip() for row in rows
    ):
        raise ValueError("invalid corpus rows")
    return rows


def prepare(data: Path = DATA, history: Path = HISTORY) -> None:
    """Extract the actual historical questions and audit all local run IDs.

    Args:
        data: Processed inputs and new question-list output directory.
        history: Saved fourth-round run, never a seed-based reconstruction.
    """
    targets = [
        data / "qa_for_choosing_chunk_size.jsonl",
        data / "annotation_preparation.manifest.json",
    ]
    if any(path.exists() for path in targets):
        raise FileExistsError("preparation outputs already exist")
    load_corpus(data)
    qa = unique_rows(read_jsonl(data / "qa.jsonl"), "question_id")
    saved = read_jsonl(history / "questions.jsonl")
    ids = list(unique_rows(saved, "question_id"))
    manifest = json.loads((history / "manifest.json").read_text(encoding="utf-8"))
    if len(ids) != 250 or set(ids) != set(manifest["question_ids"]):
        raise ValueError("round four must contain the saved 250 questions")
    for row in saved:
        if any(
            row[key] != qa[row["question_id"]][key] for key in ("paper_id", "question")
        ):
            raise ValueError("historical query differs from original QA export")
    audit = []
    used = set(ids)
    # Invalidated and smoke runs still count as exposure; never waive their IDs.
    for path in sorted(Path("results").rglob("manifest.json")):
        run = json.loads(path.read_text(encoding="utf-8"))
        if "question_ids" not in run:
            raise ValueError(f"run has no auditable question list: {path}")
        used.update(run["question_ids"])
        audit.append(
            {
                "file": path.as_posix(),
                "sha256": file_hash(path),
                "question_ids": run["question_ids"],
            }
        )
    for path in sorted(Path("results").rglob("questions.jsonl")):
        run_ids = list(unique_rows(read_jsonl(path), "question_id"))
        used.update(run_ids)
        audit.append(
            {
                "file": path.as_posix(),
                "sha256": file_hash(path),
                "question_ids": run_ids,
            }
        )
    write_jsonl(
        targets[0], [{key: qa[qid][key] for key in QUESTION_FIELDS} for qid in ids]
    )
    inputs = [
        history / "questions.jsonl",
        history / "manifest.json",
        *[
            data / name
            for name in (
                "qa.jsonl",
                "papers.jsonl",
                "qasper_export.manifest.json",
                "passages_all_paper_text.jsonl",
                "passages_all_paper_text.manifest.json",
                "gold_evidence_mapping_all_splits.jsonl",
                "gold_evidence_mapping_all_splits.manifest.json",
            )
        ],
        targets[0],
    ]
    write_json(
        targets[1],
        {
            "schema_version": "v0-proposed",
            "inputs": snapshot(inputs),
            "usage_audit": audit,
            "excluded_question_ids": sorted(used),
            "audit_scope": "all persisted local results manifests and question lists, including invalidated runs; no claim about unrecorded external experiments",
            "settings": SETTINGS,
            "seed": SEED,
            "sampling_rule": "sort eligible question_id ascending, Python Random(seed).sample without replacement, preserve draw order",
            "scope": ["train", "validation", "test"],
            "isolation": "question-level; shared papers allowed",
        },
    )


def render_batches(rows: list[dict], output: Path) -> None:
    """Write two independent English views with global, stable record numbers.

    Args:
        rows: Ordered blind JSONL rows, five adjacent pairs per question.
        output: New annotation run directory.
    """
    for slot in ("A", "B"):
        directory = output / f"annotator_{slot}"
        directory.mkdir()
        for start in range(0, len(rows), 100):
            lines = [
                "# Passage relevance annotation",
                "",
                "Annotator: ",
                "",
                "Judge whether the passage provides information that helps answer the question, including useful partial evidence. Topic overlap alone is not sufficient. Judge only the supplied question and passage.",
                "",
                "0 — Not relevant",
                "",
                "1 — Relevant",
                "",
                "Fill in only `Label: 0` or `Label: 1`. Do not change record numbers, questions or passages. Work independently without consulting another annotator or reference answers.",
                "",
            ]
            for row in rows[start : start + 100]:
                # Quoting prevents source text from creating fake Markdown sections.
                question = "\n".join(
                    "> " + line for line in row["question"].splitlines()
                )
                passage = "\n".join("> " + line for line in row["passage"].splitlines())
                title = " ".join(row["paper_title"].splitlines())
                lines.extend(
                    [
                        f"## Record {row['record_number']:04d}",
                        "",
                        f"Paper: {title}",
                        "",
                        "### Question",
                        "",
                        question,
                        "",
                        "### Passage",
                        "",
                        passage,
                        "",
                        "### Relevance",
                        "",
                        "Label: ",
                        "",
                    ]
                )
            path = directory / f"batch_{start // 100 + 1:02d}.md"
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write("\n".join(lines))


def generate_pairs(
    questions: list[dict], corpus: list[dict], gold: dict, titles: dict
) -> tuple[list, list]:
    """Retrieve without gold, then build separate blind and verification rows.

    Args:
        questions: Saved queries in frozen order.
        corpus: Verified fixed corpus.
        gold: Reference mappings, used only after each retrieval completes.
        titles: Real source titles keyed by paper ID.

    Returns:
        Blind records and separate gold-linked verification records.
    """
    retrieve = make_retriever_factory({"mode": "bm25"})(corpus)
    passages = unique_rows(corpus, "passage_id")
    blind, verification = [], []
    seen = set()
    for question in questions:
        qid, paper_id = question["question_id"], question["paper_id"]
        hits = retrieve(question["question"], paper_id, 5)
        # Preserve ranking while removing repeated backend IDs; never pad a pool.
        hits = list(dict(hits).items())
        if len(hits) != 5:
            raise ValueError("retrieval must return five different passages")
        reference = gold[qid]
        if (
            reference["paper_id"] != paper_id
            or reference["question"] != question["question"]
        ):
            raise ValueError("query and gold reference disagree")
        for rank, (pid, score) in enumerate(hits, 1):
            passage = passages[pid]
            if passage["paper_id"] != paper_id or (qid, pid) in seen:
                raise ValueError("invalid or duplicate question-passage pair")
            seen.add((qid, pid))
            title = titles[paper_id]
            if not isinstance(title, str) or not title.strip():
                raise ValueError("a real paper title is required")
            row = {
                "record_number": len(blind) + 1,
                "question_id": qid,
                "paper_id": paper_id,
                "passage_id": pid,
                "paper_title": title,
                "question": question["question"],
                "passage": passage["text"],
                "label": None,
            }
            blind.append(row)
            verification.append(
                {
                    **row,
                    "retrieval_method": "bm25",
                    "rank": rank,
                    "score": score,
                    "gold_passage_ids": reference["gold_passage_ids"],
                    "gold_evidence_match": pid in reference["gold_passage_ids"],
                    "evidence_paragraphs": reference["evidence_paragraphs"],
                }
            )
    return blind, verification


def export_pool(data: Path, output: Path, *, pilot: bool = False) -> None:
    """Export a development pilot or the saved frozen held-out pool.

    Args:
        data: Processed artifacts with preparation/freeze manifests.
        output: New run directory; existing directories are rejected.
        pilot: Use the first five historical development questions only.
    """
    if not pilot and (data / "historical_bm25_retirement.manifest.json").exists():
        raise ValueError("BM25-only pool retired; use the new frozen list in Step 2.6")
    if output.exists():
        raise FileExistsError(output)
    preparation = json.loads(
        (data / "annotation_preparation.manifest.json").read_text(encoding="utf-8")
    )
    verify_snapshot(preparation["inputs"])
    if pilot:
        questions = read_jsonl(data / "qa_for_choosing_chunk_size.jsonl")[:5]
        freeze_hash = None
    else:
        frozen_path = data / "qa_for_held_out.manifest.json"
        frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
        verify_snapshot(frozen["inputs"])
        verify_snapshot(frozen["code"]["source_sha256"])
        if code_identity()["commit"] != frozen["code"]["commit"]:
            raise ValueError("code commit changed after freeze")
        questions = read_jsonl(data / "qa_for_held_out.jsonl")
        if (
            len(questions) != 200
            or [q["question_id"] for q in questions] != frozen["question_ids"]
        ):
            raise ValueError("held-out list differs from frozen 200-question draw")
        if set(unique_rows(questions, "question_id")) & set(
            preparation["excluded_question_ids"]
        ):
            raise ValueError("held-out questions overlap prior use")
        freeze_hash = file_hash(frozen_path)
    corpus = load_corpus(data)
    gold = unique_rows(
        read_jsonl(data / "gold_evidence_mapping_all_splits.jsonl"), "question_id"
    )
    titles = {row["id"]: row["title"] for row in read_jsonl(data / "papers.jsonl")}
    blind, verification = generate_pairs(questions, corpus, gold, titles)
    output.mkdir(parents=True)
    write_jsonl(output / "pairs.jsonl", blind)
    write_jsonl(output / "verification.jsonl", verification)
    render_batches(blind, output)
    hashes = snapshot(sorted(output.rglob("*.*")))
    write_json(
        output / "manifest.json",
        {
            "schema_version": "v0-proposed",
            "purpose": "development pilot" if pilot else "held-out annotation pool",
            "question_count": len(questions),
            "pair_count": len(blind),
            "question_ids": [q["question_id"] for q in questions],
            "settings": SETTINGS,
            "retriever": retriever_metadata({"mode": "bm25"}),
            "code": code_identity(),
            "inputs": preparation["inputs"],
            "freeze_manifest_sha256": freeze_hash,
            "outputs": hashes,
            "validation": "unique questions; five distinct same-paper passages each; unique pairs; gold joined after retrieval; null labels; blind field projection",
        },
    )


def freeze(data: Path, pilot: Path) -> None:
    """Draw 200 eligible IDs after validating the completed development pilot.

    Args:
        data: Processed input directory and new frozen question-list outputs.
        pilot: Successfully completed pilot run directory.
    """
    if (data / "historical_bm25_retirement.manifest.json").exists():
        raise ValueError(
            "legacy freeze retired; use python -m src.data.freeze_held_out"
        )
    targets = [data / "qa_for_held_out.jsonl", data / "qa_for_held_out.manifest.json"]
    if any(path.exists() for path in targets):
        raise FileExistsError("held-out outputs already exist; never resample")
    preparation_path = data / "annotation_preparation.manifest.json"
    preparation = json.loads(preparation_path.read_text(encoding="utf-8"))
    verify_snapshot(preparation["inputs"])
    for item in preparation["usage_audit"]:
        verify_snapshot({item["file"]: item["sha256"]})
    completed = json.loads((pilot / "manifest.json").read_text(encoding="utf-8"))
    if (
        completed["inputs"] != preparation["inputs"]
        or completed["settings"] != SETTINGS
    ):
        raise ValueError("pilot used different inputs or settings")
    verify_snapshot(completed["outputs"])
    verify_snapshot(completed["code"]["source_sha256"])
    expected_pilot = [
        row["question_id"]
        for row in read_jsonl(data / "qa_for_choosing_chunk_size.jsonl")[:5]
    ]
    if (
        completed["purpose"] != "development pilot"
        or completed["pair_count"] != 25
        or completed["question_ids"] != expected_pilot
    ):
        raise ValueError("a successful five-question development pilot is required")
    corpus = load_corpus(data)
    counts = Counter(row["paper_id"] for row in corpus)
    # Mechanically project identifiers only: no query, answer or evidence is
    # previewed, scored or used to select the eligible question IDs.
    metadata = [
        {key: row[key] for key in ("question_id", "paper_id", "source_split")}
        for row in read_jsonl(data / "gold_evidence_mapping_all_splits.jsonl")
    ]
    unique_rows(metadata, "question_id")
    excluded = set(preparation["excluded_question_ids"])
    reasons = {
        row["question_id"]: "prior experimental use"
        if row["question_id"] in excluded
        else "fewer than five passages"
        for row in metadata
        if row["question_id"] in excluded or counts[row["paper_id"]] < 5
    }
    eligible = sorted(
        row["question_id"] for row in metadata if row["question_id"] not in reasons
    )
    selected = random.Random(preparation["seed"]).sample(eligible, 200)
    qa = unique_rows(read_jsonl(data / "qa.jsonl"), "question_id")
    chosen = [{key: qa[qid][key] for key in QUESTION_FIELDS} for qid in selected]
    inputs = {
        **preparation["inputs"],
        **snapshot([preparation_path, pilot / "manifest.json"]),
    }
    write_jsonl(targets[0], chosen)
    inputs.update(snapshot([targets[0]]))
    write_json(
        targets[1],
        {
            "schema_version": "v0-proposed",
            "purpose": "held-out question list",
            "inputs": inputs,
            "code": code_identity(),
            "seed": preparation["seed"],
            "settings": SETTINGS,
            "retriever": retriever_metadata({"mode": "bm25"}),
            "sampling_rule": preparation["sampling_rule"],
            "scope": preparation["scope"],
            "isolation": preparation["isolation"],
            "eligible_question_ids": eligible,
            "excluded": reasons,
            "prior_usage_excluded_question_ids": sorted(excluded),
            "question_ids": selected,
            "source_split_counts": dict(Counter(q["source_split"] for q in chosen)),
            "usage_boundary": "No tuning, development, prompt selection or system changes based on these queries, answers, evidence, judgments or results. Retrieval pool configuration is frozen; this does not freeze unimplemented downstream systems.",
        },
    )
