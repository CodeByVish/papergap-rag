"""Held-out protocol for P4's end-to-end run: the freeze record and what depends on it.

`docs/EVALUATION.md`: before any held-out question is read, the final commit and the
configuration are recorded and frozen; held-out answers and labels are read only afterwards,
for scoring. This module makes that order hard to break by accident.

- `configs/p4_freeze.json` is the record. It is a draft (`status: "draft"`) until the team
  freezes it; `freeze_problems` lists what is still missing.
- `held_out_items` writes the run's input from P3's frozen question list and refuses to read
  it unless the record is frozen and the list matches the hash recorded in it. The output
  holds only `question_id`, `question` and `paper_id`: no answers, no gold.
- `gold_items_for` builds the scoring items (gold passages, answerability) from P3's mapping
  and the QA file. It is for scoring after the run, never for the run itself.
- `check_run` compares a finished run's manifest with the record.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable, Iterable, Mapping, Sequence
from pathlib import Path
from typing import Any

_COMMIT = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# Dotted paths that must hold a value before the record can be called frozen.
REQUIRED_VALUES = (
    "frozen_at",
    "code.commit",
    "corpus.all_paper_text.sha256",
    "dense_index.path",
    "dense_index.metadata_sha256",
    "questions.sha256",
    "questions.count",
)
ITEM_KEYS = ("question_id", "question", "paper_id")


class FreezeError(ValueError):
    """The freeze record is not ready, or a file does not match it."""


def _get(record: Mapping[str, Any], dotted: str) -> Any:
    value: Any = record
    for part in dotted.split("."):
        if not isinstance(value, Mapping) or part not in value:
            return None
        value = value[part]
    return value


def load_freeze(path: Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def freeze_problems(freeze: Mapping[str, Any]) -> list[str]:
    """What still stops this record from being frozen; empty when it is ready."""
    problems = []
    if freeze.get("status") != "frozen":
        problems.append(f'status is {freeze.get("status")!r}, not "frozen"')
    for dotted in REQUIRED_VALUES:
        value = _get(freeze, dotted)
        if value in (None, "", [], {}):
            problems.append(f"{dotted} is not set")
    commit = _get(freeze, "code.commit")
    if commit and not _COMMIT.match(str(commit)):
        problems.append("code.commit must be a full 40-character commit hash")
    for dotted in ("corpus.all_paper_text.sha256", "dense_index.metadata_sha256", "questions.sha256"):
        value = _get(freeze, dotted)
        if value and not _SHA256.match(str(value)):
            problems.append(f"{dotted} must be a 64-character SHA-256")
    return problems


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with Path(path).open(encoding="utf-8") as source:
        return [json.loads(line) for line in source if line.strip()]


def held_out_items(
    questions_path: Path,
    freeze: Mapping[str, Any],
    *,
    commit_exists: Callable[[str], bool],
) -> list[dict[str, str]]:
    """The run's input: P3's frozen question list reduced to question, id and paper.

    Refuses unless the record is frozen, its commit exists in the repository and the list on
    disk is byte-identical to the one the record names. Nothing but `ITEM_KEYS` is copied,
    so no answer, label or split provenance reaches the run.
    """
    problems = freeze_problems(freeze)
    if problems:
        raise FreezeError(
            "the freeze record is not frozen, so held-out questions will not be read: "
            + "; ".join(problems)
        )
    commit = str(_get(freeze, "code.commit"))
    if not commit_exists(commit):
        raise FreezeError(f"frozen commit {commit} does not exist in this repository")
    actual = sha256_of(questions_path)
    if actual != _get(freeze, "questions.sha256"):
        raise FreezeError(
            f"{questions_path} has SHA-256 {actual}, but the freeze record names "
            f"{_get(freeze, 'questions.sha256')}"
        )
    rows = read_jsonl(questions_path)
    items = []
    for number, row in enumerate(rows, 1):
        for key in ITEM_KEYS:
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise FreezeError(f"{questions_path}:{number}: {key} must be a nonempty string")
        items.append({key: row[key] for key in ITEM_KEYS})
    ids = [item["question_id"] for item in items]
    if len(set(ids)) != len(ids):
        raise FreezeError(f"{questions_path} has duplicate question ids")
    expected = _get(freeze, "questions.count")
    if len(items) != expected:
        raise FreezeError(f"{questions_path} has {len(items)} questions, the record says {expected}")
    papers = _get(freeze, "questions.papers")
    if papers is not None and len({item["paper_id"] for item in items}) != papers:
        raise FreezeError(f"{questions_path} does not cover {papers} papers, as the record says")
    return items


def gold_items_for(
    questions: Iterable[Mapping[str, Any]],
    mapping_rows: Iterable[Mapping[str, Any]],
    qa_rows: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Scoring items for `questions`: gold passages from P3's mapping, answerability from QA.

    A question with mapped gold is answerable; one whose every annotator marked it unanswerable
    is not; an answerable question whose evidence did not map to whole passages keeps
    `answerable` unset and is left out of recall (as in `scripts/make_dev_items.py`).
    """
    gold = {r["question_id"]: sorted(set(r["gold_passage_ids"]))
            for r in mapping_rows if r.get("gold_passage_ids")}
    cannot_answer = {
        r["question_id"] for r in qa_rows
        if r.get("answers") and all(a["answer"]["unanswerable"] for a in r["answers"])
    }
    items = []
    for question in questions:
        qid = question["question_id"]
        item: dict[str, Any] = {key: question[key] for key in ITEM_KEYS}
        if qid in gold:
            item.update(answerable=True, gold_passage_ids=gold[qid])
        elif qid in cannot_answer:
            item["answerable"] = False
        items.append(item)
    return items


def check_run(manifest: Mapping[str, Any], freeze: Mapping[str, Any]) -> list[str]:
    """How a finished run's `run_manifest.json` differs from the freeze record."""
    mismatches = []

    def expect(label: str, actual: Any, wanted: Any) -> None:
        if wanted is not None and actual != wanted:
            mismatches.append(f"{label}: run has {actual!r}, record says {wanted!r}")

    args = manifest.get("args") or {}
    expect("git commit", _get(manifest, "environment.git_commit"), _get(freeze, "code.commit"))
    expect("corpus sha256", manifest.get("passages_sha256"),
           _get(freeze, "corpus.all_paper_text.sha256"))
    expect("critic view", manifest.get("critic_view"), _get(freeze, "agent.critic_view"))
    expect("prompt budget", manifest.get("prompt_budget"), _get(freeze, "agent.prompt_budget"))
    expect("top_k", args.get("top_k"), _get(freeze, "retrieval.top_k"))
    expect("candidate_k", args.get("candidate_k"), _get(freeze, "retrieval.candidate_k"))
    expect("max_retries", args.get("max_retries"), _get(freeze, "agent.max_retries"))
    expect("section-scoped retries", bool(args.get("scoped")), _get(freeze, "retrieval.scoped"))
    expect("reranker", bool(args.get("bge")), _get(freeze, "retrieval.reranker"))
    arms = _get(freeze, "arms")
    if arms is not None and set(args.get("arms") or ()) != set(arms):
        mismatches.append(f"arms: run has {sorted(args.get('arms') or ())!r}, record says {sorted(arms)!r}")
    return mismatches


def check_coverage(arm_ids: Mapping[str, Sequence[str]], expected: Iterable[str]) -> list[str]:
    """Each arm must hold exactly the expected questions."""
    wanted = set(expected)
    problems = []
    for arm, ids in arm_ids.items():
        found = set(ids)
        if found != wanted:
            problems.append(
                f"arm {arm}: {len(wanted - found)} questions missing, {len(found - wanted)} unexpected"
            )
    return problems
