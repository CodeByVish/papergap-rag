"""Verify standalone retrieval replay, truncation and integrity failures.

Synthetic records exercise evidence boundaries without reopening raw QASPER
data or invoking BM25 during report regeneration.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from test_chunk_size import chunk_paper, synthetic_paper, synthetic_question
from test_chunk_size import exported_inputs as exported_inputs  # noqa: PLC0414

from src.evaluation.chunk_size_artifacts import (
    SCHEMA,
    calculate_question,
    generate_reports,
    load_inputs,
    project_chunk,
    question_record,
    ranked_record,
    retained_ranking,
    validate_budgets,
    write_jsonl,
)
from src.evaluation.chunk_size_metrics import locate_annotations, source_paragraphs
from src.evaluation.run_chunk_size import run_comparison


@pytest.fixture
def structured_run(tmp_path: Path) -> tuple[Path, dict, list, dict]:
    """Persist a complete small ranking with CRLF and two answer groups.

    The first evidence paragraph spans chunks, so small word budgets cannot
    inherit the full-ranking hit or complete-annotation decisions.
    """
    paper = synthetic_paper()
    paragraphs = source_paragraphs(paper)
    question = synthetic_question()
    record = question_record(
        question, locate_annotations(question, paragraphs), paragraphs
    )
    rows = [
        ranked_record(question, {**chunk, "score": float(-rank)}, rank, paragraphs)
        for rank, chunk in enumerate(chunk_paper(paper, 4, 0), 1)
    ]
    kept, state = retained_ranking(rows, len(rows), 20)
    (tmp_path / "chunk_size_4").mkdir()
    manifest = {
        "run_id": "synthetic",
        "config": {"candidates": [4], "word_budgets": [3, 6, 20]},
        "question_ids": [question["question_id"]],
        "structured_inputs": {
            "schema_version": SCHEMA,
            "files": {
                "questions.jsonl": write_jsonl(tmp_path / "questions.jsonl", [record]),
                "chunk_size_4/ranked_chunks.jsonl": write_jsonl(
                    tmp_path / "chunk_size_4/ranked_chunks.jsonl", kept
                ),
            },
            "ranking_states": {"4": {question["question_id"]: state}},
        },
    }
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return tmp_path, record, rows, manifest


def test_budget_cut_and_normalized_source_mapping(structured_run: tuple) -> None:
    """Budgeted coverage uses only retained words and exact CRLF coordinates.

    Larger budgets monotonically add evidence; an exactly filled budget is
    not reported exhausted, whereas a budget beyond all words is exhausted.
    """
    directory, question, rows, manifest = structured_run
    state = manifest["structured_inputs"]["ranking_states"]["4"][
        question["question_id"]
    ]
    result, report = calculate_question(question, rows, state, [3, 6, 10, 20])
    assert result["evidence_hit_at_5"]
    assert not result["budgets"]["3"]["evidence_hit"]
    assert result["budgets"]["6"]["evidence_hit"]
    assert result["budgets"]["6"]["fully_covered_annotations"] == ["first"]
    assert not result["budgets"]["10"]["corpus_exhausted"]
    assert result["budgets"]["20"]["corpus_exhausted"]
    assert result["budgets"]["20"]["unused_words"] == 10
    assert "#### Word budget: 6" in report
    assert "#### Rank 3:" in report
    first = project_chunk(rows[0], rows[0]["text"].index("gamma") + len("gamma"))
    assert first["spans"]["paper-train:0:0"] == (2, 19)
    summary = generate_reports(directory)
    assert summary["sizes"]["4"]["budgets"]["20"]["actual_word_count"]["value"] == 10


def test_retention_and_insufficient_saved_prefix(structured_run: tuple) -> None:
    """Retain five even for small budgets, and reject unproven exhaustion.

    Partial rankings support smaller budgets but cannot silently supply missing
    words or fewer than five results for the top-five comparison.
    """
    _, question, rows, _ = structured_run
    repeated = [copy.deepcopy(rows[0]) for _ in range(8)]
    kept, state = retained_ranking(repeated, 8, 3)
    assert len(kept) == 5
    assert not state["ranking_complete"] and state["retention_satisfied"]
    kept, state = retained_ranking(repeated, 8, 21)
    assert len(kept) == 6
    with pytest.raises(ValueError, match="insufficient saved ranking"):
        calculate_question(question, kept, state, [25])
    empty_state = retained_ranking([], 0, 20)[1]
    result, _ = calculate_question(question, [], empty_state, [20])
    assert result["budgets"]["20"]["corpus_exhausted"]
    assert not result["evidence_hit_at_5"]


@pytest.mark.parametrize(
    "mutation",
    [
        "rank",
        "score",
        "tie",
        "duplicate",
        "words",
        "mapping",
        "paper",
        "state",
        "questions",
    ],
)
def test_invalid_artifacts_rejected(structured_run: tuple, mutation: str) -> None:
    """Reject inconsistent records even when their hashes were updated.

    Each mutation violates a separate semantic invariant beyond file integrity.
    """
    directory, _, rows, manifest = structured_run
    path = directory / "chunk_size_4/ranked_chunks.jsonl"
    if mutation == "rank":
        rows[0]["rank"] = 2
    elif mutation == "score":
        rows[1]["score"] = 10
    elif mutation == "tie":
        rows[1]["score"] = rows[0]["score"]
        rows[0]["passage_id"], rows[1]["passage_id"] = "z", "a"
    elif mutation == "duplicate":
        rows[1]["passage_id"] = rows[0]["passage_id"]
    elif mutation == "words":
        rows[0]["word_count"] += 1
    elif mutation == "mapping":
        rows[0]["source_spans"][0]["source_start"] += 1
    elif mutation == "paper":
        rows[0]["paper_id"] = "other"
    elif mutation == "state":
        manifest["structured_inputs"]["ranking_states"]["4"]["question-train"][
            "ranking_complete"
        ] = False
    else:
        manifest["question_ids"] = ["other"]
    manifest["structured_inputs"]["files"]["chunk_size_4/ranked_chunks.jsonl"] = (
        write_jsonl(path, rows)
    )
    with pytest.raises(ValueError):
        load_inputs(directory, manifest)


def test_hash_validation_and_no_partial_output(structured_run: tuple) -> None:
    """Fail before writing derived outputs when source bytes change.

    Original reports survive failed regeneration unchanged for inspection.
    """
    directory, _, _, _ = structured_run
    generate_reports(directory)
    original = (directory / "summary.json").read_bytes()
    path = directory / "questions.jsonl"
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="hash mismatch"):
        generate_reports(directory)
    assert (directory / "summary.json").read_bytes() == original


def test_saved_prefix_supports_changed_budgets(tmp_path: Path) -> None:
    """Save beyond five chunks and reject larger unsupported budgets atomically.

    A short retained prefix is not corpus exhaustion. Successful replay also
    works after deleting derived outputs, using only structured input files.
    """
    paper = synthetic_paper()
    paper["full_text"][0]["paragraphs"] = [" ".join(f"word{i}" for i in range(80))]
    question = synthetic_question()
    question["answers"] = [
        {
            "annotation_id": "all",
            "answer": {"evidence": paper["full_text"][0]["paragraphs"]},
        }
    ]
    paragraphs = source_paragraphs(paper)
    record = question_record(
        question, locate_annotations(question, paragraphs), paragraphs
    )
    rows = [
        ranked_record(question, {**chunk, "score": -rank}, rank, paragraphs)
        for rank, chunk in enumerate(chunk_paper(paper, 4, 0), 1)
    ]
    kept, state = retained_ranking(rows, len(rows), 23)
    assert len(kept) == 6
    assert state["saved_word_count"] == 24
    assert not state["ranking_complete"]
    directory = tmp_path / "chunk_size_4"
    directory.mkdir()
    manifest = {
        "run_id": "prefix",
        "config": {"candidates": [4], "word_budgets": [23]},
        "question_ids": [question["question_id"]],
        "readability_passage_ids": {"4": ["review-only"]},
        "structured_inputs": {
            "schema_version": SCHEMA,
            "files": {
                "questions.jsonl": write_jsonl(tmp_path / "questions.jsonl", [record]),
                "chunk_size_4/ranked_chunks.jsonl": write_jsonl(
                    directory / "ranked_chunks.jsonl", kept
                ),
            },
            "ranking_states": {"4": {question["question_id"]: state}},
        },
    }
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    summary = generate_reports(tmp_path, [12, 24])
    assert summary["sizes"]["4"]["readability_pass_rate"]["pending"] == 1
    assert not summary["sizes"]["4"]["questions"][0]["budgets"]["24"][
        "corpus_exhausted"
    ]
    before = (tmp_path / "summary.json").read_bytes()
    report = (directory / "evidence_review.md").read_bytes()
    with pytest.raises(ValueError, match="insufficient saved ranking"):
        generate_reports(tmp_path, [25])
    assert (tmp_path / "summary.json").read_bytes() == before
    assert (directory / "evidence_review.md").read_bytes() == report
    (tmp_path / "summary.json").unlink()
    (directory / "evidence_review.md").unlink()
    generate_reports(tmp_path, [12, 24])
    assert (tmp_path / "summary.json").read_bytes() == before


@pytest.mark.parametrize("budgets", [[], [0], [True], [1, 1], [-3], [2.5], None])
def test_invalid_budgets(budgets: list) -> None:
    """Reject ambiguous budget settings rather than silently rounding them.

    Booleans and non-integers must never become word limits.
    """
    with pytest.raises(ValueError):
        validate_budgets(budgets)


def test_runner_replay_without_raw_inputs(
    exported_inputs: tuple, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Regenerate a real BM25 run after removing every upstream input.

    JSONL alone must reproduce evidence decisions and preserve readability
    metrics, even if the prior derived question metrics have been altered.
    """
    papers, qa, export, config = exported_inputs
    run = run_comparison(
        config_path=config,
        papers_path=papers,
        qa_path=qa,
        export_manifest=export,
        output_root=tmp_path / "tmp_runs",
        run_id="replay",
    )
    original = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    for path in (papers, qa, export, config):
        path.unlink()
    stale = copy.deepcopy(original)
    stale["sizes"]["4"]["questions"][0]["evidence_hit_at_5"] = "stale"
    stale["sizes"]["4"]["readability_pass_rate"]["pending"] = 1
    (run / "summary.json").write_text(json.dumps(stale), encoding="utf-8")
    replay = generate_reports(run)
    assert (
        json.loads(json.dumps(replay))["sizes"]["4"]["questions"]
        == original["sizes"]["4"]["questions"]
    )
    assert replay["sizes"]["4"]["readability_pass_rate"]["pending"] == 1
    from scripts.evaluate_chunk_size import main

    monkeypatch.setattr(
        "sys.argv",
        [
            "evaluate_chunk_size",
            "regenerate",
            "--run-dir",
            str(run),
            "--word-budgets",
            "3",
            "6",
        ],
    )
    assert main() == 0
    changed = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    assert changed["word_budgets"] == [3, 6]
