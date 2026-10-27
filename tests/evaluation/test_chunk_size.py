"""Check chunk-size experiment contracts using small synthetic QASPER exports.

The tests cover source coverage, filtering, report validation and the full runner
without downloading data or calling a language model.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from src.data.chunking import ChunkingConfig, build_passages_from_record
from src.data.passage_ids import PassageIdContext
from src.data.qasper_export import export_qasper
from src.evaluation.chunk_size_metrics import (
    evaluate_question,
    locate_annotations,
    passage_spans,
    source_paragraphs,
)
from src.evaluation.chunk_size_reports import read_readability, summarize_readability
from src.evaluation.run_chunk_size import (
    load_config,
    retrieve_question,
    run_comparison,
    select_questions,
    select_readability_samples,
)


def synthetic_paper(split: str = "train") -> dict:
    """Return a paper with repeated tokens and differently normalized paragraphs.

    The first paragraph crosses small chunk boundaries; the second is required
    by only one of the two alternative answer annotations.
    """
    return {
        "id": f"paper-{split}",
        "title": "Synthetic paper",
        "source_split": split,
        "full_text": [
            {
                "section_name": "Body",
                "paragraphs": [
                    "  alpha beta\r\ngamma delta epsilon zeta  ",
                    "",
                    "eta theta iota kappa",
                ],
            }
        ],
    }


def synthetic_question(split: str = "train") -> dict:
    """Return grouped alternative evidence sets that are all fully locatable.

    One annotation requires two paragraphs; another requires just the first.
    """
    paper = synthetic_paper(split)
    evidence = paper["full_text"][0]["paragraphs"]
    return {
        "question_id": f"question-{split}",
        "paper_id": paper["id"],
        "source_split": split,
        "question": "alpha gamma?",
        "answers": [
            {
                "annotation_id": "both",
                "answer": {"evidence": [evidence[0], evidence[2]]},
            },
            {"annotation_id": "first", "answer": {"evidence": [evidence[0]]}},
        ],
    }


def chunk_paper(paper: dict, size: int, overlap: int) -> list[dict]:
    """Build actual shared chunks and attach private original-character spans.

    This helper exercises the same context validation as the production runner.
    """
    config = ChunkingConfig(chunk_size_words=size, chunk_overlap_words=overlap)
    context = PassageIdContext(
        dataset_id="allenai/qasper",
        resolved_revision="a" * 40,
        local_parser_version=1,
        normalization_version=config.normalization_version,
        chunking_version=config.chunking_version,
        chunk_size_words=size,
        chunk_overlap_words=overlap,
    )
    built = build_passages_from_record(paper, context=context, config=config).passages
    spans = passage_spans(paper, built, config)
    return [
        {**item.passage.model_dump(), "spans": spans[item.passage.passage_id]}
        for item in built
    ]


def test_combined_coverage_and_annotation_groups() -> None:
    """Several partial chunks can cover one paragraph and an alternative answer.

    All answers are usable; retrieved word totals include overlap.
    """
    paper = synthetic_paper()
    paragraphs = source_paragraphs(paper)
    annotations = locate_annotations(synthetic_question(), paragraphs)
    chunks = chunk_paper(paper, 4, 2)
    partial = evaluate_question(annotations, paragraphs, chunks[:1])
    assert not partial["evidence_hit_at_5"]
    assert not partial["complete_evidence_at_5"]
    combined = evaluate_question(annotations, paragraphs, chunks[:2])
    assert combined["evidence_hit_at_5"]
    assert combined["fully_covered_annotations"] == ["first"]
    assert combined["total_retrieved_words"] == 8
    complete = evaluate_question(annotations, paragraphs, chunks)
    assert complete["fully_covered_annotations"] == ["both", "first"]


@pytest.mark.parametrize(
    "evidence",
    [
        [],
        [""],
        ["missing paragraph"],
        ["FLOAT SELECTED: Figure 1"],
        ["eta theta iota kappa", "missing paragraph"],
        None,
    ],
)
def test_invalid_annotation_excludes_whole_question(evidence: list | None) -> None:
    """Reject a question even when another answer has fully located evidence.

    Empty, missing, float-only and partially resolved evidence must contribute
    neither sampled questions nor per-question evidence metrics.
    """
    paper = synthetic_paper()
    paragraphs = source_paragraphs(paper)
    invalid = synthetic_question()
    invalid["question_id"] = "invalid"
    answer = {} if evidence is None else {"evidence": evidence}
    invalid["answers"].append({"annotation_id": "invalid", "answer": answer})
    selected, counts, annotations = select_questions(
        [invalid, synthetic_question()],
        {paper["id"]: paper},
        {paper["id"]: paragraphs},
        {paper["id"]},
        {"seed": 42, "question_sample_count": 50},
    )
    assert [question["question_id"] for question in selected] == ["question-train"]
    assert set(annotations) == {"question-train"}
    assert counts == {"eligible": 1, "invalid_answer_evidence": 1, "total": 2}
    with pytest.raises(ValueError, match="all answer annotations"):
        evaluate_question(
            locate_annotations(invalid, paragraphs), paragraphs, chunk_paper(paper, 4, 2)
        )


def test_empty_answers_and_ambiguous_evidence_exclude_questions() -> None:
    """Exclude absent answers and repeated evidence before seeded sampling.

    An unambiguous alternative answer cannot rescue an ambiguous annotation;
    an empty eligible pool raises instead of producing zero-valued metrics.
    """
    paper = synthetic_paper()
    paper["full_text"][0]["paragraphs"].append("eta theta iota kappa")
    paragraphs = source_paragraphs(paper)
    ambiguous = synthetic_question()
    located = locate_annotations(ambiguous, paragraphs)
    assert [annotation["usable"] for annotation in located] == [False, True]
    empty = {**synthetic_question(), "question_id": "empty", "answers": []}
    for question in (ambiguous, empty):
        with pytest.raises(ValueError, match="no eligible"):
            select_questions(
                [question],
                {paper["id"]: paper},
                {paper["id"]: paragraphs},
                {paper["id"]},
                {"seed": 42, "question_sample_count": 50},
            )
        with pytest.raises(ValueError, match="all answer annotations"):
            evaluate_question(locate_annotations(question, paragraphs), paragraphs, [])


def test_zero_overlap_and_repeated_paragraphs() -> None:
    """Whitespace gaps do not prevent coverage and ambiguous evidence is rejected.

    Coordinate-based mapping remains correct even when source text repeats.
    """
    paper = synthetic_paper()
    paragraphs = source_paragraphs(paper)
    annotations = locate_annotations(synthetic_question(), paragraphs)
    result = evaluate_question(annotations, paragraphs, chunk_paper(paper, 3, 0))
    assert result["complete_evidence_at_5"]
    paper["full_text"][0]["paragraphs"].append(paper["full_text"][0]["paragraphs"][0])
    ambiguous = locate_annotations(synthetic_question(), source_paragraphs(paper))
    assert not any(annotation["usable"] for annotation in ambiguous)
    chunks = chunk_paper(paper, 3, 0)
    assert any("paper-train:0:3" in chunk["spans"] for chunk in chunks)


@pytest.mark.parametrize(
    "patch",
    [
        {"candidates": [True]},
        {"candidates": [4, 4]},
        {"candidates": []},
        {"overlap_words": 4},
        {"top_k": 3},
        {"unknown": 1},
        {"question_sample_count": 0},
        {"n_paper": 0},
        {"n_paragraph": True},
        {"n_paragraph": -1},
        {"seed": "42"},
        {"readability_seed": 43},
        {"question_sampling_method": "with_replacement"},
    ],
)
def test_invalid_configuration(tmp_path: Path, patch: dict) -> None:
    """Reject ambiguous values before any experiment output is published.

    Candidate booleans, overlap errors and accidental metric changes are covered.
    """
    path = tmp_path / "tmp_config.json"
    path.write_text(
        json.dumps({"candidates": [4, 6], "overlap_words": 1, **patch}),
        encoding="utf-8",
    )
    with pytest.raises((ValueError, TypeError)):
        load_config(path)


def test_readability_intervals_and_paper_budget() -> None:
    """Cover disjoint intervals without requiring every eligible paper.

    Reversing input mappings must preserve seeded output, while a different seed
    can change source locations. Length diagnostics describe the selected batch.
    """
    paragraphs = {}
    for paper_index in range(8):
        paper = synthetic_paper()
        paper["id"] = f"paper-{paper_index}"
        paper["full_text"] = [
            {"section_name": "First", "paragraphs": ["short"] * 5},
            {"section_name": "Second", "paragraphs": ["long " * 200] * 6},
        ]
        paragraphs[paper["id"]] = source_paragraphs(paper)
    config = {"n_paper": 3, "n_paragraph": 2, "seed": 42}
    samples, metadata = select_readability_samples(paragraphs, set(paragraphs), config)
    assert len(samples) == len({item["location"] for item in samples}) == 6
    assert metadata["paper_count_actual"] == 3
    assert set(metadata["paragraph_count_by_paper"].values()) == {2}
    for offset in range(0, len(samples), 2):
        assert samples[offset]["section_index"] == 0
        assert samples[offset + 1]["section_index"] == 1
    assert metadata["length_check"] == {
        "threshold_words": 150, "short_count": 3, "long_count": 3
    }
    reversed_paragraphs = {
        key: dict(reversed(list(value.items())))
        for key, value in reversed(list(paragraphs.items()))
    }
    assert select_readability_samples(reversed_paragraphs, set(paragraphs), config) == (
        samples, metadata
    )
    changed, _ = select_readability_samples(
        paragraphs, set(paragraphs), {**config, "seed": 7}
    )
    assert [item["location"] for item in changed] != [item["location"] for item in samples]


def test_readability_small_pool_and_exclusions() -> None:
    """Use every eligible paragraph when budgets exceed available data.

    Empty and unnamed sections are excluded by the shared source index; papers
    absent from the common corpus cannot enter the readability sample.
    """
    paper = synthetic_paper()
    paper["full_text"].append({"section_name": " ", "paragraphs": ["excluded"]})
    paragraphs = {
        "paper-train": source_paragraphs(paper),
        "empty": {},
        "not-common": source_paragraphs(synthetic_paper("test")),
    }
    samples, metadata = select_readability_samples(
        paragraphs, {"paper-train", "empty"},
        {"n_paper": 5, "n_paragraph": 8, "seed": 42},
    )
    assert [item["paragraph_index"] for item in samples] == [0, 2]
    assert metadata["paper_count_actual"] == 1
    assert metadata["paragraph_count_requested"] == 40
    assert metadata["paragraph_count_by_paper"] == {"paper-train": 2}


@pytest.fixture
def exported_inputs(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    """Create verified paper and QA exports containing all three official splits.

    Extra train questions have absent or partially unresolved evidence; neither
    may enter reports or metric denominators despite valid alternative answers.
    """
    source = tmp_path / "tmp_source"
    source.mkdir()
    splits = []
    for split in ("train", "validation", "test"):
        paper = synthetic_paper(split)
        paper.pop("source_split")
        question = synthetic_question(split)
        question.pop("paper_id")
        question.pop("source_split")
        paper["qas"] = [question]
        if split == "train":
            paper["qas"].append(
                {"question_id": "no-evidence", "question": "why?", "answers": []}
            )
            partial = synthetic_question(split)
            partial.pop("paper_id")
            partial.pop("source_split")
            partial["question_id"] = "partial-evidence"
            partial["answers"][0]["answer"]["evidence"].append("missing paragraph")
            paper["qas"].append(partial)
        payload = (json.dumps(paper) + "\n").encode("utf-8")
        (source / f"{split}.jsonl").write_bytes(payload)
        splits.append(
            {
                "name": split,
                "file": f"{split}.jsonl",
                "rows": 1,
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )
    (source / "manifest.json").write_text(
        json.dumps(
            {
                "manifest_schema_version": 1,
                "dataset": {
                    "id": "allenai/qasper",
                    "resolved_revision": "a" * 40,
                    "local_parser_version": 1,
                },
                "splits": splits,
            }
        ),
        encoding="utf-8",
    )
    output = tmp_path / "tmp_export"
    papers, qa, manifest = (
        output / name for name in ("papers.jsonl", "qa.jsonl", "manifest.json")
    )
    export_qasper(
        input_dir=source, papers_output=papers, qa_output=qa, manifest_output=manifest
    )
    config = tmp_path / "tmp_config.json"
    config.write_text(
        json.dumps(
            {
                "candidates": [4, 6],
                "overlap_words": 1,
                "question_sample_count": 10,
                "n_paper": 2,
                "n_paragraph": 2,
            }
        ),
        encoding="utf-8",
    )
    return papers, qa, manifest, config


def test_runner_and_manual_summary(exported_inputs: tuple, tmp_path: Path) -> None:
    """Run both sizes, validate held-out exclusion, and import manual labels.

    Both reports must use the same question IDs. Reusing a run ID must fail.
    """
    papers, qa, export, config = exported_inputs
    args = {
        "config_path": config,
        "papers_path": papers,
        "qa_path": qa,
        "export_manifest": export,
        "output_root": tmp_path / "tmp_results",
        "run_id": "comparison",
    }
    run = run_comparison(**args)
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    assert set(manifest["question_ids"]) == {"question-train", "question-validation"}
    assert manifest["filtering_counts"] == {
        "eligible": 2,
        "held_out": 1,
        "invalid_answer_evidence": 2,
        "total": 5,
    }
    assert manifest["question_sample_count_actual"] == 2
    assert manifest["config"]["overlap_words"] == 1
    assert manifest["readability_sample_count_actual"] == 4
    assert set(manifest["readability_sampling"]["paper_ids"]) == {
        "paper-train", "paper-validation"
    }
    pending = summarize_readability(run)
    assert all(
        value["readability_pass_rate"]["value"] is None
        for value in pending["sizes"].values()
    )
    for size in (4, 6):
        review = run / f"chunk_size_{size}" / "readability.md"
        evidence = (review.parent / "evidence_review.md").read_text(encoding="utf-8")
        assert evidence.count("## Question:") == 2
        assert "partial-evidence" not in evidence
        assert "no-evidence" not in evidence
        assert "source_split" not in evidence
        assert "Word count:" in evidence and "Total retrieved words:" in evidence
        assert not (review.parent / "retrieval.jsonl").exists()
        text = review.read_text(encoding="utf-8")
        review.write_text(text.replace("| pending |", "| pass |"), encoding="utf-8")
    summary = summarize_readability(run)
    counts = manifest["readability_review_chunk_counts"]
    assert manifest["readability_review_chunk_count_total"] == sum(counts.values())
    for size, count in counts.items():
        assert count == len(manifest["readability_passage_ids"][size])
        assert count == summary["sizes"][size]["readability_pass_rate"]["denominator"]
    assert all(
        value["readability_pass_rate"]["value"] == 1
        for value in summary["sizes"].values()
    )
    for value in summary["sizes"].values():
        assert value["evidence_hit_at_5"]["denominator"] == 2
        assert (
            value["retrieved_word_count"]["value"]
            == sum(result["total_retrieved_words"] for result in value["questions"]) / 2
        )
    with pytest.raises(FileExistsError):
        run_comparison(**args)
    repeated = run_comparison(**{**args, "run_id": "repeat"})
    repeated_manifest = json.loads(
        (repeated / "manifest.json").read_text(encoding="utf-8")
    )
    repeated_summary = json.loads(
        (repeated / "summary.json").read_text(encoding="utf-8")
    )
    assert repeated_manifest["question_ids"] == manifest["question_ids"]
    assert repeated_manifest["readability_samples"] == manifest["readability_samples"]
    for size in ("4", "6"):
        assert (
            repeated_summary["sizes"][size]["corpus_sha256"]
            == summary["sizes"][size]["corpus_sha256"]
        )


@pytest.mark.parametrize(
    "matches",
    [
        [("missing", 1.0)],
        [("wrong-paper", 1.0)],
        [("valid", float("nan"))],
        [("valid", 1.0), ("valid", 0.0)],
        [(str(index), 1.0) for index in range(6)],
    ],
)
def test_invalid_retrieval_results(matches: list) -> None:
    """A retriever adapter cannot inject invalid or wrong-paper evidence.

    Bad scores, duplicates and over-limit outputs must fail before scoring.
    """

    def retrieve(query: str, paper_id: str, top_k: int) -> list:
        """Return a fixed invalid ranking for adapter-boundary validation.

        Query and filter arguments are accepted to match the factory contract.
        """
        return matches

    with pytest.raises(ValueError):
        retrieve_question(
            retrieve,
            synthetic_question(),
            {
                "valid": {"paper_id": "paper-train"},
                "wrong-paper": {"paper_id": "paper-test"},
            },
            5,
        )


def test_cli_run_and_summary(
    exported_inputs: tuple, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Exercise the maintained CLI against a verified synthetic export.

    Both subcommands use real files and keep generated reports under tmp_path.
    """
    from scripts.evaluate_chunk_size import main

    papers, qa, export, config = exported_inputs
    root = tmp_path / "tmp_cli_results"
    monkeypatch.setattr(
        "sys.argv",
        [
            "evaluate_chunk_size",
            "run",
            "--config",
            str(config),
            "--papers",
            str(papers),
            "--qa",
            str(qa),
            "--export-manifest",
            str(export),
            "--output-root",
            str(root),
            "--run-id",
            "cli",
        ],
    )
    assert main() == 0
    monkeypatch.setattr(
        "sys.argv",
        [
            "evaluate_chunk_size",
            "summarize",
            "--run-dir",
            str(root / "cli"),
        ],
    )
    assert main() == 0


@pytest.mark.parametrize(
    "rows",
    [
        "| `id` | unknown | |",
        "",
        "| `other` | pass | |",
        "| `id` | pass | |\n| `id` | fail | |",
    ],
)
def test_invalid_manual_labels(tmp_path: Path, rows: str) -> None:
    """Missing, duplicate and unexpected manual rows must raise explicit errors.

    None of these malformed reviews should silently become a zero pass rate.
    """
    path = tmp_path / "tmp_readability.md"
    path.write_text("### Evaluation results\n" + rows, encoding="utf-8")
    with pytest.raises(ValueError):
        read_readability(path, ["id"])


def test_pending_and_fenced_labels(tmp_path: Path) -> None:
    """Pending reviews remain null and source text cannot inject result rows.

    A deliberately forged table inside a source fence is ignored by the parser.
    """
    path = tmp_path / "tmp_readability.md"
    path.write_text(
        "### Evaluation results\n```text\n| `id` | fail | |\n```\n| `id` | pending | |\n",
        encoding="utf-8",
    )
    assert read_readability(path, ["id"]) == {
        "value": None,
        "numerator": 0,
        "denominator": 1,
        "pending": 1,
    }
