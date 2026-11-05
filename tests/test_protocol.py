"""The held-out protocol: freeze record, guarded items, post-run scoring and the critic audit."""

import copy
import hashlib
import json
from pathlib import Path

import pytest

from scripts import make_held_out_items as items_script
from scripts import run_agent_experiment as runner
from scripts import score_agent_records as score
from src.agent.experiments import ExperimentItem, audit_critic, format_audit
from src.agent.protocol import (
    FreezeError,
    check_coverage,
    check_run,
    freeze_problems,
    gold_items_for,
    held_out_items,
    load_freeze,
)
from src.retrieval.schemas import Passage, RetrievedPassage, SourceScore

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "a" * 40


def write_jsonl(path: Path, rows) -> Path:
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return path


def questions(n=3):
    return [{"question_id": f"q{i}", "question": f"Question {i}?", "paper_id": f"p{i % 2}",
             "source_split": "test", "answers": ["must never be copied"]} for i in range(n)]


def frozen_record(questions_path: Path, count: int = 3) -> dict:
    return {
        "status": "frozen", "frozen_at": "2026-11-05T09:00:00+08:00", "approved_by": ["P4", "P6"],
        "code": {"commit": COMMIT},
        "corpus": {"all_paper_text": {"sha256": "b" * 64}},
        "dense_index": {"path": "indexes/x", "metadata_sha256": "c" * 64},
        "questions": {"sha256": hashlib.sha256(questions_path.read_bytes()).hexdigest(),
                      "count": count, "papers": 2},
        "retrieval": {"top_k": 5, "candidate_k": 20, "scoped": True, "reranker": False},
        "agent": {"max_retries": 2, "critic_view": "generator",
                  "prompt_budget": {"max_passages": 8, "max_chars_per_passage": 1200}},
        "arms": ["static", "adaptive", "static-wide"],
    }


# --- the record in the repository -----------------------------------------

def test_the_shipped_record_is_a_draft_that_says_what_is_missing():
    record = load_freeze(ROOT / "configs/p4_freeze.json")
    problems = freeze_problems(record)
    assert record["status"] == "draft"
    assert any("status" in line for line in problems)
    for missing in ("code.commit", "dense_index.path", "dense_index.metadata_sha256", "approved_by"):
        assert any(missing in line for line in problems)


def test_the_shipped_record_names_checkable_identifiers():
    record = load_freeze(ROOT / "configs/p4_freeze.json")
    assert record["questions"]["count"] == 200 and record["questions"]["papers"] == 174
    assert record["questions"]["sha256"].startswith("d509010b")  # the hash in P3's own manifest
    assert record["corpus"]["all_paper_text"]["sha256"].startswith("8eeef011")
    assert record["corpus"]["development"]["sha256"].startswith("ecb1c601")
    assert record["agent"]["refusal_rule"] == "off" and record["retrieval"]["reranker"] is False
    assert {d["id"] for d in record["disclosures"]} >= {"p4-annotated-40", "p4-dev-no-overlap"}


def test_the_annotated_ids_file_holds_forty_distinct_ids():
    rows = [json.loads(line) for line in
            (ROOT / "configs/p4_annotated_held_out_ids.jsonl").read_text().splitlines() if line]
    assert len(rows) == 40 and len({r["question_id"] for r in rows}) == 40
    assert all(set(r) == {"question_id"} for r in rows)  # ids only, no question text


# --- freeze_problems -------------------------------------------------------

def test_a_complete_record_has_no_problems(tmp_path):
    path = write_jsonl(tmp_path / "q.jsonl", questions())
    assert freeze_problems(frozen_record(path)) == []


@pytest.mark.parametrize(("edit", "expected"), [
    (lambda r: r.update(status="draft"), "not \"frozen\""),
    (lambda r: r.update(approved_by=[]), "approved_by"),
    (lambda r: r.update(frozen_at=None), "frozen_at"),
    (lambda r: r["code"].update(commit="abc123"), "40-character"),
    (lambda r: r["questions"].update(sha256="short"), "64-character"),
    (lambda r: r["dense_index"].update(path=None), "dense_index.path"),
])
def test_each_missing_piece_is_named(tmp_path, edit, expected):
    record = frozen_record(write_jsonl(tmp_path / "q.jsonl", questions()))
    edit(record)
    assert any(expected in line for line in freeze_problems(record))


# --- the guarded items ----------------------------------------------------

def test_a_draft_record_is_refused_before_the_question_file_is_opened(tmp_path):
    record = frozen_record(write_jsonl(tmp_path / "q.jsonl", questions()))
    record["status"] = "draft"
    never_written = tmp_path / "does-not-exist.jsonl"
    with pytest.raises(FreezeError, match="not frozen"):
        held_out_items(never_written, record, commit_exists=lambda c: True)  # no FileNotFoundError


def test_items_hold_only_the_question_the_id_and_the_paper(tmp_path):
    path = write_jsonl(tmp_path / "q.jsonl", questions())
    items = held_out_items(path, frozen_record(path), commit_exists=lambda c: True)
    assert items == [{"question_id": f"q{i}", "question": f"Question {i}?", "paper_id": f"p{i % 2}"}
                     for i in range(3)]


def test_a_commit_that_does_not_exist_is_refused(tmp_path):
    path = write_jsonl(tmp_path / "q.jsonl", questions())
    with pytest.raises(FreezeError, match="does not exist"):
        held_out_items(path, frozen_record(path), commit_exists=lambda c: False)


def test_a_question_list_that_differs_from_the_recorded_hash_is_refused(tmp_path):
    path = write_jsonl(tmp_path / "q.jsonl", questions())
    record = frozen_record(path)
    path.write_text(path.read_text() + "\n")  # any change at all
    with pytest.raises(FreezeError, match="SHA-256"):
        held_out_items(path, record, commit_exists=lambda c: True)


@pytest.mark.parametrize("rows", [
    questions(2),  # the record says 3
    [*questions(2), {**questions(1)[0]}],  # duplicate id (and wrong count)
])
def test_wrong_count_or_duplicates_are_refused(tmp_path, rows):
    path = write_jsonl(tmp_path / "q.jsonl", rows)
    with pytest.raises(FreezeError):
        held_out_items(path, frozen_record(path, count=3), commit_exists=lambda c: True)


def test_the_script_refuses_a_draft_and_never_overwrites(tmp_path, monkeypatch, capsys):
    path = write_jsonl(tmp_path / "q.jsonl", questions())
    draft = tmp_path / "freeze.json"
    draft.write_text(json.dumps({**frozen_record(path), "status": "draft"}))
    out = tmp_path / "items.jsonl"
    with pytest.raises(SystemExit, match="not frozen"):
        items_script.main(["--questions", str(path), "--freeze", str(draft), "--out", str(out)])
    assert not out.exists()

    ready = tmp_path / "ready.json"
    ready.write_text(json.dumps(frozen_record(path)))
    monkeypatch.setattr(items_script, "commit_exists", lambda c: True)
    items_script.main(["--questions", str(path), "--freeze", str(ready), "--out", str(out)])
    assert len(out.read_text().splitlines()) == 3
    with pytest.raises(SystemExit, match="exists"):
        items_script.main(["--questions", str(path), "--freeze", str(ready), "--out", str(out)])


# --- gold for scoring -----------------------------------------------------

def test_gold_items_use_the_mapping_and_the_qa_answerability():
    qs = [{"question_id": f"q{i}", "question": "?", "paper_id": "p"} for i in range(4)]
    mapping = [{"question_id": "q0", "gold_passage_ids": ["b", "a", "a"]},
               {"question_id": "q1", "gold_passage_ids": []}]
    qa = [{"question_id": "q1", "answers": [{"answer": {"unanswerable": True}}]},
          {"question_id": "q2", "answers": [{"answer": {"unanswerable": False}}]}]
    by_id = {i["question_id"]: i for i in gold_items_for(qs, mapping, qa)}
    assert by_id["q0"]["answerable"] is True and by_id["q0"]["gold_passage_ids"] == ["a", "b"]
    assert by_id["q1"]["answerable"] is False and "gold_passage_ids" not in by_id["q1"]
    assert "answerable" not in by_id["q2"]  # answerable, but its evidence did not map to a passage
    assert "answerable" not in by_id["q3"]


# --- checking a finished run against the record ---------------------------

def manifest_for(record: dict) -> dict:
    return {"environment": {"git_commit": COMMIT}, "passages_sha256": "b" * 64,
            "critic_view": "generator", "prompt_budget": {"max_passages": 8, "max_chars_per_passage": 1200},
            "args": {"top_k": 5, "candidate_k": 20, "max_retries": 2, "scoped": True, "bge": False,
                     "arms": ["static", "adaptive", "static-wide"]}}


def test_a_run_that_matches_the_record_has_no_mismatch(tmp_path):
    record = frozen_record(write_jsonl(tmp_path / "q.jsonl", questions()))
    assert check_run(manifest_for(record), record) == []


@pytest.mark.parametrize(("edit", "expected"), [
    (lambda m: m["environment"].update(git_commit="d" * 40), "git commit"),
    (lambda m: m.update(passages_sha256="e" * 64), "corpus sha256"),
    (lambda m: m.update(critic_view="pool"), "critic view"),
    (lambda m: m["prompt_budget"].update(max_passages=10), "prompt budget"),
    (lambda m: m["args"].update(bge=True), "reranker"),
    (lambda m: m["args"].update(top_k=10), "top_k"),
    (lambda m: m["args"].update(arms=["static"]), "arms"),
])
def test_each_deviation_from_the_record_is_named(tmp_path, edit, expected):
    record = frozen_record(write_jsonl(tmp_path / "q.jsonl", questions()))
    manifest = copy.deepcopy(manifest_for(record))
    edit(manifest)
    assert any(expected in line for line in check_run(manifest, record))


def test_coverage_requires_exactly_the_expected_questions():
    assert check_coverage({"static": ["a", "b"], "adaptive": ["b", "a"]}, ["a", "b"]) == []
    problems = check_coverage({"static": ["a"], "adaptive": ["a", "b", "z"]}, ["a", "b"])
    assert "arm static: 1 questions missing, 0 unexpected" in problems
    assert "arm adaptive: 0 questions missing, 1 unexpected" in problems


# --- scoring --------------------------------------------------------------

def passage(pid):
    return Passage(passage_id=pid, paper_id="paper", title="t", section="Results",
                   chunk_number=0, text="Our model achieves 91% accuracy.")


def hit(pid):
    return RetrievedPassage(passage=passage(pid), rank=1,
                            source_scores={"bm25": SourceScore(rank=1, score=1.0)}, rrf_score=0.1)


def make_run(tmp_path: Path, item_rows, record: dict | None = None) -> Path:
    items = [ExperimentItem(r["question_id"], r["question"], r["paper_id"], None, None) for r in item_rows]
    run = tmp_path / "run"
    run.mkdir()
    for name, wide in (("static", 5), ("adaptive", 5), ("static-wide", 15)):
        runner.run_arm(name, items, lambda q, p, k: [hit("g"), hit("x")], run,
                       adaptive=name == "adaptive", top_k=wide)
    manifest = manifest_for(record) if record else {"args": {}}
    (run / "run_manifest.json").write_text(json.dumps(manifest))
    return run


def gold_rows(n=3):
    return [{"question_id": f"q{i}", "question": f"Question {i}?", "paper_id": "paper",
             "answerable": True, "gold_passage_ids": ["g"]} for i in range(n)]


def test_development_scoring_writes_the_metrics_the_run_would_have(tmp_path):
    rows = gold_rows()
    run = make_run(tmp_path, rows)
    gold = write_jsonl(tmp_path / "gold.jsonl", rows)
    out = tmp_path / "out"
    score.main(["--run-dir", str(run), "--gold-items", str(gold), "--out-dir", str(out),
                "--label", "dev"])
    metrics = json.loads((out / "metrics.json").read_text())
    assert metrics["metrics"]["static"]["recall_after_retries"] == 1.0
    text = (out / "metrics.md").read_text()
    assert text.startswith("Scored: dev (3 questions, development)") and "Critic audit" in text
    assert json.loads((out / "score_manifest.json").read_text())["inputs"]["gold_items"]


def test_a_subset_is_scored_on_its_own(tmp_path):
    rows = gold_rows()
    run = make_run(tmp_path, rows)
    gold = write_jsonl(tmp_path / "gold.jsonl", rows)
    leave_out = write_jsonl(tmp_path / "ids.jsonl", [{"question_id": "q0"}])
    out = tmp_path / "out"
    score.main(["--run-dir", str(run), "--gold-items", str(gold), "--out-dir", str(out),
                "--exclude-ids", str(leave_out), "--label", "without q0"])
    assert json.loads((out / "metrics.json").read_text())["metrics"]["static"]["questions"] == 2


def held_out_setup(tmp_path, *, count=3):
    rows = questions(count)
    q_path = write_jsonl(tmp_path / "held_out_items.jsonl",
                         [{k: r[k] for k in ("question_id", "question", "paper_id")} for r in rows])
    record = frozen_record(q_path, count=count)
    freeze = tmp_path / "freeze.json"
    freeze.write_text(json.dumps(record))
    run = make_run(tmp_path, rows, record)
    mapping = write_jsonl(tmp_path / "mapping.jsonl", [
        {"question_id": r["question_id"], "gold_passage_ids": ["g"]} for r in rows])
    qa = write_jsonl(tmp_path / "qa.jsonl", [])
    base = ["--role", "held-out", "--freeze", str(freeze), "--run-dir", str(run),
            "--questions", str(q_path), "--mapping", str(mapping), "--qa", str(qa),
            "--out-dir", str(tmp_path / "out")]
    return base, freeze, run, record


def test_a_held_out_score_needs_the_freeze_record():
    with pytest.raises(SystemExit):
        score.parse_args(["--role", "held-out", "--run-dir", "r", "--out-dir", "o",
                          "--gold-items", "g"])


def test_a_held_out_score_is_made_when_everything_matches(tmp_path):
    base, *_ = held_out_setup(tmp_path)
    score.main(base)
    metrics = json.loads((tmp_path / "out/metrics.json").read_text())
    assert metrics["metrics"]["adaptive"]["questions_with_gold"] == 3


def test_a_held_out_score_is_refused_for_a_draft_a_wrong_commit_or_missing_questions(tmp_path):
    base, freeze, run, record = held_out_setup(tmp_path)
    freeze.write_text(json.dumps({**record, "status": "draft"}))
    with pytest.raises(SystemExit, match="freeze record: status"):
        score.main(base)
    freeze.write_text(json.dumps(record))

    manifest = json.loads((run / "run_manifest.json").read_text())
    manifest["environment"]["git_commit"] = "f" * 40
    (run / "run_manifest.json").write_text(json.dumps(manifest))
    with pytest.raises(SystemExit, match="run: git commit"):
        score.main(base)

    manifest["environment"]["git_commit"] = COMMIT
    (run / "run_manifest.json").write_text(json.dumps(manifest))
    short = [line for line in (run / "adaptive.jsonl").read_text().splitlines()][:-1]
    (run / "adaptive.jsonl").write_text("\n".join(short) + "\n")
    with pytest.raises(SystemExit, match="arm adaptive: 1 questions missing"):
        score.main(base)


# --- the critic audit -----------------------------------------------------

def entry(source="llm", sufficient=True, shown=("a",), cites=None):
    row = {"source": source, "sufficient": sufficient, "passage_ids": list(shown)}
    if cites is not None:
        row["supporting_passage_ids"] = cites
    return row


def record(qid, rounds, critic_log):
    return {"question_id": qid, "retrieval_log": [{"passage_ids": ids} for ids in rounds],
            "critic_log": critic_log}


def test_audit_sorts_verdicts_by_whether_the_gold_was_within_reach():
    items = [ExperimentItem("a", "?", "p", frozenset({"g"}), True),
             ExperimentItem("b", "?", "p", frozenset({"g"}), True),
             ExperimentItem("c", "?", "p", frozenset({"g"}), True),
             ExperimentItem("u", "?", "p", None, False)]
    records = [
        # a: round 1 insufficient with gold missing; round 2 the gold arrives and it is accepted
        record("a", [["x"], ["g"]], [entry(sufficient=False, shown=["x"]),
                                      entry(sufficient=True, shown=["x", "g"], cites=["g"])]),
        # b: over-strict (gold in view, still insufficient), then a reused verdict
        record("b", [["g"], ["g"]], [entry(sufficient=False, shown=["g"]),
                                      entry(source="reused", sufficient=False, shown=["g"])]),
        # c: gold retrieved but outside the critic's view; accepted citing something else
        record("c", [["x", "g"]], [entry(sufficient=True, shown=["x"], cites=["x"])]),
        # u: unanswerable and accepted
        record("u", [["x"]], [entry(sufficient=True, shown=["x"], cites=["x"])]),
    ]
    audit = audit_critic(records, items)
    assert audit["verdicts"] == {
        "insufficient/gold missing": 1, "sufficient/gold complete": 1, "insufficient/gold complete": 1,
        "sufficient/gold hidden": 1, "sufficient/unanswerable": 1}
    assert audit["model_verdicts"] == 5
    assert audit["sources"] == {"llm": 5, "reused": 1}
    assert audit["sufficient_cites"] == {"a gold passage": 1, "no gold passage": 1}
    text = format_audit(audit)
    assert "over-strict" in text and "outside its view" in text and "false accept" in text


def test_audit_falls_back_to_the_retrieved_pool_for_older_logs():
    items = [ExperimentItem("a", "?", "p", frozenset({"g"}), True)]
    old = {"source": "llm", "sufficient": False}  # logged before passage ids were kept
    audit = audit_critic([record("a", [["g"]], [old])], items)
    assert audit["verdicts"] == {"insufficient/gold complete": 1}
    assert audit["sufficient_cites"] == {}
