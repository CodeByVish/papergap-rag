"""Exercise expanded validation plans with verified synthetic exports.

The small pool deliberately forces a new-question shortage while retaining
exact regression rankings, separate denominators and replayable group results.
"""

from __future__ import annotations

import copy
import json
import random
from pathlib import Path

import pytest
from test_chunk_size import exported_inputs as exported_inputs  # noqa: PLC0414

from src.evaluation.chunk_size_artifacts import generate_reports
from src.evaluation.chunk_size_validation import add_validation_summary, freeze_plan
from src.evaluation.run_chunk_size import load_config, run_comparison


def test_frozen_expansion_and_replay(exported_inputs: tuple, tmp_path: Path) -> None:
    """Freeze, reuse and replay a plan without changing old results.

    An available pool smaller than requested retains all new questions, records
    the shortage and never imports the synthetic held-out test question.
    """
    papers, qa, export, config_path = exported_inputs
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config["question_sample_count"] = 1
    config_path.write_text(json.dumps(config), encoding="utf-8")
    args = {
        "config_path": config_path,
        "papers_path": papers,
        "qa_path": qa,
        "export_manifest": export,
        "output_root": tmp_path / "tmp_results",
    }
    reference = run_comparison(**args, run_id="reference")
    config.update(
        question_sample_count=201,
        validation={
            "reference_run": str(reference),
            "additional_question_count": 200,
            "primary_word_budget": 1000,
        },
    )
    config_path.write_text(json.dumps(config), encoding="utf-8")
    plan_path = tmp_path / "tmp_plan.json"
    run_comparison(**args, run_id="expanded", prepare_plan=plan_path)
    assert not (args["output_root"] / "expanded").exists()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    old = plan["groups"]["regression"]["question_ids"]
    new = plan["groups"]["new"]["question_ids"]
    assert len(old) == len(new) == 1 and not set(old) & set(new)
    assert set(old + new) == {"question-train", "question-validation"}
    assert plan["unused_eligible_count"] == 1
    run_dir = run_comparison(**args, run_id="expanded", question_plan=plan_path)
    assert (
        json.loads((run_dir / "question_plan.json").read_text(encoding="utf-8")) == plan
    )
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["regression_verified"] is True
    summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
    saved = (run_dir / "summary.json").read_bytes()
    replayed = generate_reports(run_dir)
    assert summary == json.loads(json.dumps(replayed))
    assert (run_dir / "summary.json").read_bytes() == saved
    for group, denominator in (("regression", 1), ("new", 1), ("combined", 2)):
        for value in summary["validation"]["groups"][group]["sizes"].values():
            assert value["evidence_hit_at_5"]["denominator"] == denominator
    assert "new: 1000 words" in (run_dir / "summary.html").read_text(encoding="utf-8")
    assert (run_dir / "report.md").is_file()
    plan["groups"]["new"]["question_ids"] = old
    plan_path.write_text(json.dumps(plan), encoding="utf-8")
    with pytest.raises(ValueError, match="frozen question plan"):
        run_comparison(**args, run_id="tampered", question_plan=plan_path)
    assert not (args["output_root"] / "tampered").exists()
    original = (run_dir / "summary.json").read_bytes()
    (run_dir / "question_plan.json").write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="plan hash mismatch"):
        generate_reports(run_dir)
    assert (run_dir / "summary.json").read_bytes() == original


def test_paired_gains_and_losses() -> None:
    """Retain question identities even when aggregate success counts tie.

    Equal rates can hide disjoint successes; gains and losses must distinguish
    those cases at both top-five and fixed-budget views.
    """
    rows = []
    for qid, success in (("old", True), ("a", True), ("b", False)):
        rows.append(
            {
                "question_id": qid,
                "evidence_hit_at_5": success,
                "complete_evidence_at_5": success,
                "total_retrieved_words": 4,
                "budgets": {
                    "10": {
                        "evidence_hit": success,
                        "complete_evidence": success,
                        "actual_words": 4,
                        "corpus_exhausted": True,
                    }
                },
            }
        )
    other = copy.deepcopy(rows)
    for row in other[1:]:
        row["evidence_hit_at_5"] = not row["evidence_hit_at_5"]
        row["complete_evidence_at_5"] = not row["complete_evidence_at_5"]
        row["budgets"]["10"]["evidence_hit"] = row["evidence_hit_at_5"]
        row["budgets"]["10"]["complete_evidence"] = row["complete_evidence_at_5"]
    summary = {"sizes": {"4": {"questions": rows}, "6": {"questions": other}}}
    plan = {
        "primary_word_budget": 10,
        "primary_metric": "complete_evidence_rate",
        "groups": {"new": {"question_ids": ["a", "b"]}},
    }
    add_validation_summary(summary, plan, [10])
    for pair in summary["validation"]["paired_comparisons"]["new"]:
        assert pair["left_only_question_ids"] == ["a"]
        assert pair["right_only_question_ids"] == ["b"]


def test_plan_sampling_and_input_drift(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Sort unused IDs before sampling and reject a changed input hash.

    A shuffled eligible pool must yield the identical seeded question sequence.
    Reference loading is stubbed here to isolate selection from ranking replay.
    """
    manifest = {
        "config": {"candidates": [325]},
        "question_ids": ["old"],
        "inputs": {
            name: {"sha256": name} for name in ("papers", "qa", "export_manifest")
        },
        "readability_samples": [],
    }
    config = {
        "candidates": [325],
        "seed": 42,
        "overlap_words": 40,
        "top_k": 5,
        "word_budgets": [1000],
        "retrieval": {"mode": "bm25"},
        "n_paper": 5,
        "n_paragraph": 2,
        "validation": {
            "reference_run": str(tmp_path),
            "additional_question_count": 2,
            "primary_word_budget": 1000,
        },
    }
    manifest["config"].update(
        {key: value for key, value in config.items() if key != "validation"}
    )
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    (tmp_path / "summary.json").write_text("{}", encoding="utf-8")
    (tmp_path / "questions.jsonl").write_text("", encoding="utf-8")

    def load_reference(*args: object) -> tuple[list, dict]:
        """Bypass ranking replay in this isolated sample-selection test.

        File integrity and replay are exercised by the end-to-end test above.
        """
        return [], {}

    monkeypatch.setattr(
        "src.evaluation.chunk_size_validation.load_inputs", load_reference
    )
    eligible = [
        {"question_id": qid, "paper_id": "p", "source_split": "train"}
        for qid in ("c", "old", "a", "b")
    ]
    first, _ = freeze_plan(eligible, config, manifest["inputs"])
    second, _ = freeze_plan(list(reversed(eligible)), config, manifest["inputs"])
    assert first == second
    assert first["groups"]["new"]["question_ids"] == random.Random(42).sample(
        ["a", "b", "c"], 2
    )
    assert first["overlapping_paper_ids"] == ["p"]
    changed = copy.deepcopy(manifest["inputs"])
    changed["qa"]["sha256"] = "different"
    with pytest.raises(ValueError, match="input hash changed"):
        freeze_plan(eligible, config, changed)


@pytest.mark.parametrize(
    "settings",
    [
        None,
        {},
        {
            "reference_run": "x",
            "additional_question_count": True,
            "primary_word_budget": 1000,
        },
        {
            "reference_run": "x",
            "additional_question_count": 2,
            "primary_word_budget": 123,
        },
    ],
)
def test_invalid_validation_configuration(tmp_path: Path, settings: object) -> None:
    """Reject invalid validation keys and values before building any corpus.

    Booleans cannot masquerade as sample counts and primary budgets must belong
    to the experiment's explicit list of fixed word budgets.
    """
    path = tmp_path / "tmp_config.json"
    path.write_text(
        json.dumps({"candidates": [325], "validation": settings}), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        load_config(path)
