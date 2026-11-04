"""Meaningful contract and edge-case checks for the P6 offline scoring path."""

import csv
import json

import pytest

from scripts.run_p6_evaluation import main
from src.evaluation.agreement import agreement, finalize_gold
from src.evaluation.common import read_jsonl, sha256
from src.evaluation.comparison import compare
from src.evaluation.p3_rankings import score_p3
from src.evaluation.performance import summarize_performance, usage_cost
from src.evaluation.qa import evaluate_qa, pair_scores, prediction, references
from src.evaluation.ragas_runner import prepare_samples, score_samples

Q = [{"question_id": "q1", "paper_id": "p1", "question": "Which model?"}]
G = [
    {
        "question_id": "q1",
        "paper_id": "p1",
        "references": ["BERT base model"],
        "unanswerable": False,
    }
]
P = [
    {
        "question_id": "q1",
        "paper_id": "p1",
        "prediction": "BERT model",
        "status": "answered",
        "elapsed_s": 2.0,
        "answer_s": 3.0,
    }
]


def dump(path, rows):
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))
    return path


def test_qa_hand_calculation_multiset_and_reference_selection():
    assert pair_scores("BERT model", "BERT base model") == {"em": 0.0, "f1": 0.8}
    assert pair_scores("x x", "x")["f1"] == pytest.approx(2 / 3)
    assert pair_scores("The BERT.", "bert")["em"] == 1
    rows, summary = evaluate_qa(Q, P, G)
    assert rows[0]["f1"] == 0.8
    assert summary["answerable_f1"] == 0.8
    assert pair_scores("4 samples", "5 samples")["f1"] == 0.5


def test_qasper_types_and_invalid_references():
    row = {
        "answers": [
            {"answer": {"unanswerable": True}},
            {"answer": {"unanswerable": False, "yes_no": False}},
        ]
    }
    assert references(row) == (["no"], False)
    assert references(
        {
            "answers": [
                {"answer": {"unanswerable": False, "extractive_spans": ["x", "y"]}}
            ]
        }
    ) == (["x y"], False)
    with pytest.raises(ValueError):
        references({"answers": [{"answer": {"unanswerable": False}}]})


def test_failures_count_zero_and_unanswerable_refusal_is_separate():
    rows, summary = evaluate_qa(Q, [], G)
    assert rows[0]["f1"] == 0 and summary["failures"] == 1
    gold = [{**G[0], "references": [], "unanswerable": True}]
    rows, _ = evaluate_qa(Q, [{**P[0], "status": "refused"}], gold)
    assert rows[0]["unanswerable_correctness"] == 1 and rows[0]["f1"] is None
    with pytest.raises(ValueError):
        evaluate_qa(Q, P + P, G)
    with pytest.raises(ValueError):
        evaluate_qa(Q, [{**P[0], "paper_id": "wrong"}], G)


def test_p5_safe_generation_error_is_not_refusal():
    row = {
        "answer": {
            "result": {"answer": "x"},
            "validation": {"violations": [{"code": "GENERATION_ERROR"}]},
        }
    }
    assert prediction(row)[1] == "error"


def test_agreement_and_degenerate_kappa():
    assert agreement([(0, 0)] * 45 + [(1, 1)] * 45 + [(0, 1)] * 5 + [(1, 0)] * 5)[
        "kappa"
    ] == pytest.approx(0.8)
    assert agreement([(1, 1)] * 3)["kappa"] is None


def test_pool_scores_do_not_claim_exhaustive_recall():
    pairs = [
        {
            "question_id": "q1",
            "paper_id": "p1",
            "question": "Which model?",
            "passage_id": pid,
            "record_number": i,
        }
        for i, pid in enumerate(["a", "b", "c"], 1)
    ]
    labels = [
        {
            "question_id": "q1",
            "paper_id": "p1",
            "status": "mapped",
            "relevance_complete": False,
            "judged_passage_ids": ["a", "b", "c"],
            "relevant_passage_ids": ["a", "c"],
        }
    ]
    ranking = [
        {
            "question_id": "q1",
            "method": "bm25",
            "hits": [
                {"passage_id": "a", "rank": 1, "record_number": 1},
                {"passage_id": "b", "rank": 2, "record_number": 2},
            ],
        }
    ]
    rows, _summary = score_p3(Q, pairs, ranking, labels, [1, 2])
    assert rows[1]["precision_at_k"] == 0.5 and rows[1]["pool_recall_at_k"] == 0.5
    assert "recall_at_k" not in rows[1]
    with pytest.raises(ValueError):
        score_p3(Q, pairs, ranking, labels, [3])
    ranking[0]["hits"][0]["record_number"] = 3
    with pytest.raises(ValueError):
        score_p3(Q, pairs, ranking, labels, [1])


def test_performance_separates_pipeline_time_and_wall_throughput():
    summary = summarize_performance(
        P + [{**P[0], "question_id": "q2", "status": "error"}], 10
    )
    assert summary["p50_seconds"] == 5
    assert summary["successful_requests_per_second"] == 0.1
    assert summary["technical_errors"] == 1
    assert summarize_performance(P)["successful_requests_per_second"] is None
    assert summarize_performance(P, latency_field="client_elapsed_s")["latency_n"] == 0
    cost = usage_cost(
        [
            {
                "component": "judge",
                "model": "m",
                "input_tokens": 1000,
                "output_tokens": 100,
            }
        ],
        {
            "m": {
                "input_per_million": 2,
                "output_per_million": 5,
                "currency": "USD",
                "date": "2026-11-05",
                "source": "test",
            }
        },
    )
    assert cost[0]["cost"] == 0.0025


def test_ragas_validation_does_not_call_a_model_and_missing_context_is_explicit():
    contexts = [
        {
            "question_id": "q1",
            "paper_id": "p1",
            "exact_rendered": True,
            "provenance": "test",
            "contexts": ["BERT"],
        }
    ]
    samples = prepare_samples(Q, P, G, contexts)
    rows, _ = score_samples(samples)
    assert rows[0]["faithfulness"] is None
    assert rows[0]["faithfulness_status"] == "ready_not_scored"
    rows, _ = score_samples(samples, lambda metric, sample: 0.75)
    assert rows[0]["faithfulness"] == 0.75
    rows, _ = score_samples(samples, lambda metric, sample: float("nan"))
    assert rows[0]["faithfulness_status"] == "invalid_judge_score"
    rows, _ = score_samples(prepare_samples(Q, P, G, []))
    assert rows[0]["faithfulness_status"] == "missing_context"
    with pytest.raises(ValueError):
        prepare_samples(Q, P, G, [{**contexts[0], "exact_rendered": False}])


def test_paired_bootstrap_uses_question_matches_and_paper_identity():
    left = [
        {"question_id": "q1", "paper_id": "p", "f1": 0.2},
        {"question_id": "q2", "paper_id": "p", "f1": 0.4},
    ]
    right = [
        {"question_id": "q2", "paper_id": "p", "f1": 0.6},
        {"question_id": "q1", "paper_id": "p", "f1": 0.4},
    ]
    result = compare(left, right, ["f1"], 20)[0]
    assert result["mean_right_minus_left"] == pytest.approx(0.2)
    assert result["papers"] == 1 and result["paired_questions"] == 2


def test_cli_outputs_hashes_no_overwrite_and_final_scope_guard(tmp_path):
    q, p, g = (
        dump(tmp_path / name, rows)
        for name, rows in [("q.jsonl", Q), ("p.jsonl", P), ("g.jsonl", G)]
    )
    out = tmp_path / "qa"
    args = [
        "qa",
        "--questions",
        str(q),
        "--predictions",
        str(p),
        "--references",
        str(g),
        "--arm",
        "static",
        "--role",
        "development",
        "--output",
        str(out),
    ]
    main(args)
    assert json.loads((out / "summary.json").read_text())["answerable_f1"] == 0.8
    manifest = json.loads((out / "run_manifest.json").read_text())
    assert manifest["inputs"]["predictions"]["sha256"] == sha256(p)
    with pytest.raises(SystemExit):
        main(args)
    args[args.index("development")] = "held_out"
    args[-1] = str(tmp_path / "heldout")
    with pytest.raises(SystemExit):
        main(args)
    assert not (tmp_path / "heldout").exists()


def test_gold_export_requires_real_review_and_third_party(tmp_path):
    report = {"commit": "abc", "threshold_pass": True}
    with pytest.raises(ValueError, match="Human"):
        finalize_gold(
            tmp_path, report, [], {}, [], tmp_path / "missing", {}, tmp_path / "missing"
        )
    # Validation must reject an original annotator acting as adjudicator.
    original = {
        "record_number": 1,
        "question_id": "q",
        "passage_id": "a",
        "question": "Q",
        "passage": "A",
        "annotator_A": "Alice",
        "label_A": 0,
        "annotator_B": "Bob",
        "label_B": 1,
        "adjudicator": "",
        "final_label": "",
        "reason": "",
    }
    path = tmp_path / "adjudication.csv"
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(original))
        w.writeheader()
        w.writerow(
            {**original, "adjudicator": "Alice", "final_label": "1", "reason": "test"}
        )
    review = {
        "source_commit": "abc",
        "independence_confirmed": True,
        "usage_and_freeze_reviewed": True,
        "review_note": "test only",
        "project_role": "development",
    }
    with pytest.raises(ValueError, match="third person"):
        finalize_gold(
            tmp_path, report, [], {}, [original], path, review, tmp_path / "missing"
        )


def test_duplicate_json_keys_rejected(tmp_path):
    p = tmp_path / "bad.jsonl"
    p.write_text('{"question_id":"a","question_id":"b"}\n')
    with pytest.raises(ValueError):
        read_jsonl(p)


def test_rendered_context_reconstruction_uses_real_p5_selection():
    from src.evaluation.contexts import reconstruct_contexts
    from src.generation.prompts.grounded_qa import PROMPT_VERSION, PromptConfig

    with open("tests/fixtures/retrieval_sample.jsonl") as fixture:
        row = json.loads(fixture.readline())
    row["paper_id"] = row["hits"][0]["paper_id"]
    row["answer"] = {
        "result": {"answer": "58.4 F1"},
        "generation": {"prompt_version": PROMPT_VERSION},
    }
    rows = reconstruct_contexts(
        [row],
        PromptConfig(max_passages=1, max_chars_per_passage=20).model_dump(),
        PROMPT_VERSION,
        "synthetic test",
    )
    assert len(rows[0]["contexts"]) == 1
    assert rows[0]["passage_ids"] == [row["hits"][0]["passage_id"]]
    assert row["hits"][0]["text"] not in rows[0]["contexts"][0]
    with pytest.raises(ValueError):
        reconstruct_contexts([row], {}, "wrong-version", "reviewed")


def test_complete_gold_export_and_retrieval_cli(tmp_path):
    pairs = [
        {
            "record_number": i,
            "question_id": "q1",
            "paper_id": "p1",
            "question": "Which model?",
            "passage_id": f"p{i}",
            "passage": f"Text {i}",
        }
        for i in range(1, 6)
    ]
    judgments = {
        (s, i): {"annotator": s, "label": int(i < 3)} for s in "AB" for i in range(1, 6)
    }
    corpus = dump(
        tmp_path / "corpus.jsonl",
        [
            {"passage_id": p["passage_id"], "paper_id": "p1", "text": p["passage"]}
            for p in pairs
        ],
    )
    qpath = dump(tmp_path / "questions.jsonl", Q)
    pairs_path = dump(tmp_path / "pairs.jsonl", pairs)
    rankings_path = dump(
        tmp_path / "rankings.jsonl",
        [
            {
                "question_id": "q1",
                "method": "bm25",
                "hits": [
                    {"passage_id": p["passage_id"], "rank": i, "record_number": i}
                    for i, p in enumerate(pairs, 1)
                ],
            }
        ],
    )
    report = {
        "commit": "synthetic",
        "threshold_pass": True,
        "pool_output_sha256": {
            "data/processed/annotation_common_v3/" + k + ".jsonl": sha256(v)
            for k, v in [
                ("questions", qpath),
                ("pairs", pairs_path),
                ("rankings", rankings_path),
            ]
        },
    }
    adj = tmp_path / "adj.csv"
    adj.write_text("record_number,adjudicator,final_label,reason\n")
    review = {
        "source_commit": "synthetic",
        "independence_confirmed": True,
        "usage_and_freeze_reviewed": True,
        "review_note": "synthetic fixture only",
        "project_role": "development",
    }
    gold_dir = tmp_path / "gold"
    gold_dir.mkdir()
    finalize_gold(gold_dir, report, pairs, judgments, [], adj, review, corpus)
    labels = read_jsonl(gold_dir / "final_labels.jsonl")
    assert labels[0]["relevant_passage_ids"] == ["p1", "p2"]
    assert labels[0]["relevance_complete"] is False
    out = tmp_path / "retrieval"
    main(
        [
            "retrieval",
            "--questions",
            str(qpath),
            "--pairs",
            str(pairs_path),
            "--rankings",
            str(rankings_path),
            "--corpus",
            str(corpus),
            "--labels",
            str(gold_dir / "final_labels.jsonl"),
            "--labels-manifest",
            str(gold_dir / "final_labels_manifest.json"),
            "--role",
            "development",
            "--output",
            str(out),
        ]
    )
    assert json.loads((out / "summary.json").read_text())[0]["precision_at_k"] == 1
    # A ranking file with changed scores must fail byte-level frozen-run validation.
    data = read_jsonl(rankings_path)
    data[0]["hits"][0]["score"] = 999
    dump(rankings_path, data)
    with pytest.raises(SystemExit):
        main(
            [
                "retrieval",
                "--questions",
                str(qpath),
                "--pairs",
                str(pairs_path),
                "--rankings",
                str(rankings_path),
                "--corpus",
                str(corpus),
                "--labels",
                str(gold_dir / "final_labels.jsonl"),
                "--labels-manifest",
                str(gold_dir / "final_labels_manifest.json"),
                "--role",
                "development",
                "--output",
                str(tmp_path / "tampered"),
            ]
        )


def test_cli_performance_ragas_and_comparison_use_real_fixture_contracts(tmp_path):
    from pathlib import Path

    fix = Path("tests/fixtures/p6")
    for arm in ("static", "adaptive"):
        main(
            [
                "qa",
                "--questions",
                str(fix / "questions.jsonl"),
                "--predictions",
                str(fix / (arm + ".jsonl")),
                "--references",
                str(fix / "references.jsonl"),
                "--arm",
                arm,
                "--role",
                "development",
                "--output",
                str(tmp_path / arm),
            ]
        )
    main(
        [
            "performance",
            "--predictions",
            str(fix / "static.jsonl"),
            "--arm",
            "static",
            "--latency-field",
            "client_elapsed_s",
            "--batch-seconds",
            "6.5",
            "--hardware",
            "synthetic",
            "--cache-policy",
            "none",
            "--usage",
            str(fix / "usage.jsonl"),
            "--pricing",
            str(fix / "pricing.json"),
            "--output",
            str(tmp_path / "performance"),
        ]
    )
    assert (tmp_path / "performance/usage_cost.csv").exists()
    main(
        [
            "ragas",
            "--questions",
            str(fix / "questions.jsonl"),
            "--predictions",
            str(fix / "static.jsonl"),
            "--references",
            str(fix / "references.jsonl"),
            "--contexts",
            str(fix / "contexts.jsonl"),
            "--arm",
            "static",
            "--role",
            "development",
            "--output",
            str(tmp_path / "ragas"),
        ]
    )
    scores = read_jsonl(tmp_path / "ragas/scores.jsonl")
    assert scores[0]["faithfulness_status"] == "ready_not_scored"
    main(
        [
            "compare",
            "--left",
            str(tmp_path / "static/scores.jsonl"),
            "--right",
            str(tmp_path / "adaptive/scores.jsonl"),
            "--metrics",
            "f1",
            "task_score",
            "--output",
            str(tmp_path / "compare"),
        ]
    )
    summary = json.loads((tmp_path / "compare/summary.json").read_text())
    assert summary[0]["mean_right_minus_left"] == pytest.approx(0.2)


def test_evidence_static_depths_and_adaptive_match_p4_definition():
    from src.evaluation.evidence import score_evidence

    corpus = [{"passage_id": str(i), "paper_id": "p1"} for i in range(1, 11)]
    gold = [
        {
            "question_id": "q1",
            "paper_id": "p1",
            "gold_passage_ids": ["1", "8", "10"],
            "answerable": True,
        }
    ]
    record = {
        "question_id": "q1",
        "paper_id": "p1",
        "retrieval_log": [{"round": 1, "passage_ids": [str(i) for i in range(1, 11)]}],
    }
    rows, _ = score_evidence(
        Q, [record], gold, corpus, "static", "static", [5, 8, 10], 10
    )
    assert [r["mapped_recall"] for r in rows] == [1 / 3, 2 / 3, 1]
    assert rows[0]["mapped_recall_first_round"] == 1 / 3
    with pytest.raises(ValueError):
        score_evidence(Q, [record], gold, corpus, "static", "static", [10], 5)
    adaptive = {
        **record,
        "answer_error": "generation failed, retrieval still succeeded",
        "retrieval_log": [
            {"round": 1, "passage_ids": ["1", "2"]},
            {"round": 2, "passage_ids": ["2", "8"]},
            {"round": 3, "passage_ids": ["10"]},
        ],
    }
    rows, summary = score_evidence(Q, [adaptive], gold, corpus, "adaptive", "adaptive")
    assert (
        rows[0]["mapped_recall"] == 1 and rows[0]["mapped_recall_first_round"] == 1 / 3
    )
    assert rows[0]["retrieved_count"] == 4
    assert summary[0]["retrieval_failures"] == 0
    rows, summary = score_evidence(Q, [], gold, corpus, "adaptive", "adaptive")
    assert rows[0]["mapped_recall"] == 0
    assert summary[0]["successful_only_mapped_recall"] is None
    rows, _ = score_evidence(
        Q,
        [adaptive],
        [{**gold[0], "gold_passage_ids": []}],
        corpus,
        "adaptive",
        "adaptive",
    )
    assert rows[0]["mapped_recall"] is None and rows[0]["answerable"] is True
    with pytest.raises(ValueError):
        score_evidence(Q, [adaptive], gold, corpus, "static", "static", [5], 5)
    with pytest.raises(ValueError):
        score_evidence(
            Q,
            [adaptive],
            [{**gold[0], "gold_passage_ids": ["unknown"]}],
            corpus,
            "adaptive",
            "adaptive",
        )


def test_evidence_cli_hash_guards_and_static_adaptive_comparison(tmp_path):
    from src.evaluation.common import write_json

    q = dump(tmp_path / "q.jsonl", Q)
    corpus = dump(
        tmp_path / "corpus.jsonl",
        [{"passage_id": str(i), "paper_id": "p1"} for i in range(1, 11)],
    )
    gold = dump(
        tmp_path / "gold.jsonl",
        [{"question_id": "q1", "paper_id": "p1", "gold_passage_ids": ["1", "10"]}],
    )
    manifest = tmp_path / "gold.manifest.json"
    write_json(
        manifest,
        {
            "output": {"sha256": sha256(gold)},
            "inputs": {"passages": {"sha256": sha256(corpus)}},
        },
    )
    static = dump(
        tmp_path / "static.jsonl",
        [
            {
                "question_id": "q1",
                "retrieved_passage_ids": [str(i) for i in range(1, 11)],
            }
        ],
    )
    adaptive = dump(
        tmp_path / "adaptive.jsonl",
        [
            {
                "question_id": "q1",
                "retrieval_log": [
                    {"round": 1, "passage_ids": ["1"]},
                    {"round": 2, "passage_ids": ["10"]},
                ],
            }
        ],
    )
    common = [
        "--questions",
        str(q),
        "--gold",
        str(gold),
        "--gold-manifest",
        str(manifest),
        "--corpus",
        str(corpus),
        "--role",
        "development",
    ]
    main(
        [
            "evidence",
            *common,
            "--records",
            str(static),
            "--mode",
            "static",
            "--arm",
            "static",
            "--saved-depth",
            "10",
            "--ks",
            "5",
            "8",
            "10",
            "--output",
            str(tmp_path / "static"),
        ]
    )
    main(
        [
            "evidence",
            *common,
            "--records",
            str(adaptive),
            "--mode",
            "adaptive",
            "--arm",
            "adaptive",
            "--output",
            str(tmp_path / "adaptive"),
        ]
    )
    main(
        [
            "compare",
            "--left",
            str(tmp_path / "static/scores.jsonl"),
            "--left-k",
            "5",
            "--right",
            str(tmp_path / "adaptive/scores.jsonl"),
            "--metrics",
            "mapped_recall",
            "--output",
            str(tmp_path / "comparison"),
        ]
    )
    result = json.loads((tmp_path / "comparison/summary.json").read_text())[0]
    assert result["mean_right_minus_left"] == 0.5 and result["left_k"] == 5
    gold.write_text(gold.read_text() + "\n")
    with pytest.raises(SystemExit):
        main(
            [
                "evidence",
                *common,
                "--records",
                str(adaptive),
                "--mode",
                "adaptive",
                "--arm",
                "adaptive",
                "--output",
                str(tmp_path / "tampered"),
            ]
        )
