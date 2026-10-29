"""Provisional P1 retrieval metrics with explicit, independently supplied labels.

This module never derives relevance from text overlap, answers, or retrieved hits.
P6 can replace the metric backend while retaining the checked qrels boundary.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

DEFAULT_SPLIT_POLICY = "qasper-official-paper-disjoint-v0-proposed"
_STATUSES = {"mapped", "mapping_failed", "unanswerable", "no_relevant"}
_METRICS = {"precision_at_k", "recall_at_k", "mrr_at_k"}


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _identifier(value, field: str) -> str:
    _check(
        isinstance(value, str) and bool(value.strip()) and value == value.strip(),
        f"{field} must be a clean, nonempty string",
    )
    return value


def _sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def _unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        _check(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _id_list(value, field: str) -> list[str]:
    _check(isinstance(value, list), f"{field} must be a list")
    result = [_identifier(item, field) for item in value]
    _check(len(result) == len(set(result)), f"duplicate ID in {field}")
    return result


@dataclass(frozen=True)
class QuestionJudgment:
    paper_id: str
    status: str
    relevance_complete: bool
    relevant_passage_ids: frozenset[str]
    judged_passage_ids: frozenset[str]

    @property
    def exclusion_reason(self) -> str | None:
        if self.status != "mapped":
            return self.status
        if not self.relevance_complete:
            return "incomplete_relevance"
        return None


@dataclass(frozen=True)
class QrelsBundle:
    questions: Mapping[str, str]
    passages: Mapping[str, str]
    judgments: Mapping[str, QuestionJudgment]
    manifest: dict
    provenance: dict


class MetricsBackend(Protocol):
    """Replacement seam for P6; the caller supplies only eligible questions."""

    name: str

    def score(
        self, retrieved: Sequence[str], relevant: frozenset[str], *, k: int
    ) -> Mapping[str, float]: ...


class ProvisionalMetricsBackend:
    name = "p1-provisional"

    def score(
        self, retrieved: Sequence[str], relevant: frozenset[str], *, k: int
    ) -> dict[str, float]:
        _check(type(k) is int and k > 0, "k must be a positive integer")
        _check(bool(relevant), "metrics require known relevant passages")
        selected = list(retrieved[:k])
        _check(len(selected) == len(set(selected)), "duplicate retrieved passage ID")
        matching = [
            rank
            for rank, passage_id in enumerate(selected, 1)
            if passage_id in relevant
        ]
        return {
            "precision_at_k": len(matching) / k,
            "recall_at_k": len(matching) / len(relevant),
            "mrr_at_k": 1.0 / matching[0] if matching else 0.0,
        }


def _judgment(
    row: dict, *, questions: Mapping[str, str], passages: Mapping[str, str]
) -> tuple[str, QuestionJudgment]:
    question_id = _identifier(row["question_id"], "question_id")
    _check(question_id in questions, f"unknown question_id: {question_id}")
    paper_id = _identifier(row["paper_id"], "paper_id")
    _check(
        questions[question_id] == paper_id, f"question paper mismatch: {question_id}"
    )
    status = row["status"]
    _check(
        isinstance(status, str) and status in _STATUSES,
        f"invalid status: {question_id}",
    )
    complete = row["relevance_complete"]
    _check(type(complete) is bool, "relevance_complete must be boolean")
    relevant = frozenset(_id_list(row["relevant_passage_ids"], "relevant_passage_ids"))
    judged = frozenset(
        _id_list(row.get("judged_passage_ids", list(relevant)), "judged_passage_ids")
    )
    _check(relevant <= judged, "judged_passage_ids must include all relevant passages")
    for passage_id in judged:
        _check(passage_id in passages, f"unknown passage_id: {passage_id}")
        _check(passages[passage_id] == paper_id, f"cross-paper qrel: {passage_id}")
    _check(
        (status == "mapped") == bool(relevant),
        "mapped status requires relevant IDs; excluded statuses must not claim relevance",
    )
    _check(
        status != "no_relevant" or complete,
        "no_relevant requires complete relevance annotation",
    )
    return question_id, QuestionJudgment(paper_id, status, complete, relevant, judged)


def _jsonl_judgments(path: Path, questions, passages) -> dict[str, QuestionJudgment]:
    judgments = {}
    with path.open(encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line, object_pairs_hook=_unique_object)
                _check(isinstance(row, dict), "qrels row must be an object")
                question_id, judgment = _judgment(
                    row, questions=questions, passages=passages
                )
                _check(
                    question_id not in judgments,
                    f"duplicate question_id: {question_id}",
                )
                judgments[question_id] = judgment
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(f"{path}:{number}: invalid qrels ({error})") from error
    return judgments


def _trec_judgments(
    path: Path, manifest: dict, questions, passages
) -> dict[str, QuestionJudgment]:
    assessments = manifest["assessments"]
    _check(isinstance(assessments, dict), "TREC requires an assessments object")
    relevant = {question_id: [] for question_id in assessments}
    judged = {question_id: [] for question_id in assessments}
    seen_pairs = set()
    with path.open(encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            columns = line.split()
            _check(len(columns) == 4, f"{path}:{number}: TREC requires four columns")
            question_id, _, passage_id, raw_grade = columns
            _check(question_id in questions, f"unknown question_id: {question_id}")
            _check(
                question_id in assessments, f"missing TREC assessment: {question_id}"
            )
            _check(passage_id in passages, f"unknown passage_id: {passage_id}")
            _check(
                passages[passage_id] == questions[question_id],
                f"cross-paper qrel: {passage_id}",
            )
            _check(
                bool(re.fullmatch(r"\d+", raw_grade)),
                f"{path}:{number}: grade must be a nonnegative integer",
            )
            pair = (question_id, passage_id)
            _check(pair not in seen_pairs, f"duplicate TREC question/passage: {pair}")
            seen_pairs.add(pair)
            judged[question_id].append(passage_id)
            if int(raw_grade) > 0:
                relevant[question_id].append(passage_id)
    result = {}
    for question_id, state in assessments.items():
        _check(isinstance(state, dict), "TREC assessment must be an object")
        _, result[question_id] = _judgment(
            {
                **state,
                "question_id": question_id,
                "relevant_passage_ids": relevant[question_id],
                "judged_passage_ids": judged[question_id],
            },
            questions=questions,
            passages=passages,
        )
    return result


def load_qrels(
    labels_path: str | Path,
    manifest_path: str | Path,
    *,
    corpus_sha256: str,
    questions: Mapping[str, str],
    passages: Mapping[str, str],
    split_policy_version: str = DEFAULT_SPLIT_POLICY,
) -> QrelsBundle:
    """Load independently produced JSONL/TREC judgments for an exact train scope.

    A complete annotation manifest requires one assessment for every question.
    Partial annotation is allowed, but missing questions are excluded from scores.
    """
    labels_path, manifest_path = Path(labels_path), Path(manifest_path)
    _check(
        isinstance(questions, Mapping) and bool(questions),
        "questions must be a nonempty mapping",
    )
    _check(isinstance(passages, Mapping), "passages must be a mapping")
    for question_id, paper_id in questions.items():
        _identifier(question_id, "question_id")
        _identifier(paper_id, "question paper_id")
    for passage_id, paper_id in passages.items():
        _identifier(passage_id, "passage_id")
        _identifier(paper_id, "passage paper_id")
    _check(
        isinstance(corpus_sha256, str)
        and bool(re.fullmatch(r"[0-9a-f]{64}", corpus_sha256)),
        "corpus_sha256 must be a SHA-256 digest",
    )
    try:
        manifest = json.loads(
            manifest_path.read_text(encoding="utf-8-sig"),
            object_pairs_hook=_unique_object,
        )
        _check(isinstance(manifest, dict), "labels manifest must be an object")
        _check(
            type(manifest["format_version"]) is int and manifest["format_version"] == 1,
            "unsupported labels manifest version",
        )
        _check(
            manifest["corpus_sha256"] == corpus_sha256, "labels corpus SHA-256 mismatch"
        )
        labels_hash = _sha256(labels_path)
        _check(manifest["labels_sha256"] == labels_hash, "labels SHA-256 mismatch")
        _identifier(manifest["source"], "labels source")
        _identifier(manifest["mapping"]["version"], "mapping version")
        _identifier(manifest["mapping"]["description"], "mapping description")
        scope = manifest["question_scope"]
        _check(
            scope["source_split"] == "train" and scope["project_role"] == "development",
            "only train development labels are allowed",
        )
        _check(
            scope["split_policy_version"] == split_policy_version,
            "labels split policy mismatch",
        )
        scoped_ids = _id_list(scope["question_ids"], "question_scope.question_ids")
        _check(
            set(scoped_ids) == set(questions),
            "labels question scope must equal the complete run scope",
        )
        coverage = manifest["annotation_coverage"]
        _check(coverage in ("complete", "partial"), "invalid annotation_coverage")
        labels_format = manifest["labels_format"]
        _check(
            labels_format in ("jsonl", "trec"), "labels_format must be jsonl or trec"
        )
        judgments = (
            _jsonl_judgments(labels_path, questions, passages)
            if labels_format == "jsonl"
            else _trec_judgments(labels_path, manifest, questions, passages)
        )
        if coverage == "complete":
            _check(
                set(judgments) == set(questions),
                "complete annotation is missing question labels",
            )
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"invalid labels or manifest: {error}") from error
    return QrelsBundle(
        dict(questions),
        dict(passages),
        judgments,
        manifest,
        {
            "labels_path": str(labels_path.resolve()),
            "manifest_path": str(manifest_path.resolve()),
            "labels_sha256": labels_hash,
            "manifest_sha256": _sha256(manifest_path),
            "corpus_sha256": corpus_sha256,
            "source": manifest["source"],
            "mapping": manifest["mapping"],
            "question_scope": scope,
            "annotation_coverage": coverage,
            "labels_format": labels_format,
        },
    )


def evaluate_rankings(
    rankings: Mapping[str, Mapping[str, Sequence[str]]],
    qrels: QrelsBundle,
    *,
    k: int,
    backend: MetricsBackend | None = None,
) -> dict:
    """Macro-average only mapped, answerable, complete-relevance questions.

    Missing labels and incomplete pools have coverage reports, never zero scores.
    An eligible query with no retrieved hits does receive zero retrieval scores.
    """
    _check(type(k) is int and k > 0, "k must be a positive integer")
    _check(
        isinstance(rankings, Mapping) and bool(rankings),
        "rankings must contain methods",
    )
    backend = backend if backend is not None else ProvisionalMetricsBackend()
    _identifier(backend.name, "backend name")
    eligible_count = sum(
        judgment.exclusion_reason is None for judgment in qrels.judgments.values()
    )
    scope_kind = (
        "all"
        if eligible_count == len(qrels.questions)
        else "subset"
        if eligible_count
        else "none"
    )
    report = {
        "status": "provisional" if eligible_count else "unavailable",
        "k": k,
        "aggregation": "macro average over eligible questions only",
        "evaluation_scope": {
            "kind": scope_kind,
            "scoped_questions": len(qrels.questions),
            "labeled_questions": len(qrels.judgments),
            "eligible_questions": eligible_count,
            "excluded_questions": len(qrels.questions) - eligible_count,
            "interpretation": "Provisional scores describe only eligible questions in the declared scope",
        },
        "definitions": {
            "precision_at_k": "relevant hits / k, including short returns",
            "recall_at_k": "relevant hits / all known relevant passages",
            "mrr_at_k": "reciprocal first relevant rank at or before k; otherwise zero",
            "judged_coverage_at_k": "judged returned passages / actual returned passages at k; null for no returns",
        },
        "backend": {
            "name": backend.name,
            "status": "P6_pending"
            if isinstance(backend, ProvisionalMetricsBackend)
            else "external",
        },
        "labels": qrels.provenance,
        "methods": {},
    }
    for method, method_rankings in rankings.items():
        _identifier(method, "method")
        _check(
            isinstance(method_rankings, Mapping)
            and set(method_rankings) == set(qrels.questions),
            f"{method}: rankings must include every scoped question (use [] for zero hits)",
        )
        excluded = Counter()
        per_question = []
        scores = []
        total_returned = total_judged = 0
        for question_id in sorted(qrels.questions):
            values = method_rankings[question_id]
            _check(
                isinstance(values, Sequence) and not isinstance(values, (str, bytes)),
                f"{question_id}: ranking must be an ordered sequence",
            )
            ids = [_identifier(value, "retrieved passage_id") for value in values]
            _check(
                len(ids) == len(set(ids)),
                f"{question_id}: duplicate retrieved passage_id",
            )
            for passage_id in ids:
                _check(
                    passage_id in qrels.passages,
                    f"unknown retrieved passage_id: {passage_id}",
                )
                _check(
                    qrels.passages[passage_id] == qrels.questions[question_id],
                    f"cross-paper retrieved passage: {passage_id}",
                )
            selected = ids[:k]
            judgment = qrels.judgments.get(question_id)
            reason = "missing_labels" if judgment is None else judgment.exclusion_reason
            metrics = None
            if reason is None:
                metrics = dict(
                    backend.score(selected, judgment.relevant_passage_ids, k=k)
                )
                _check(
                    set(metrics) == _METRICS
                    and all(
                        isinstance(value, (int, float))
                        and not isinstance(value, bool)
                        and math.isfinite(value)
                        and 0 <= value <= 1
                        for value in metrics.values()
                    ),
                    "metric backend returned invalid scores",
                )
                scores.append(metrics)
            else:
                excluded[reason] += 1
            if judgment is None:
                judged_count = 0
            elif judgment.relevance_complete and judgment.status in (
                "mapped",
                "no_relevant",
            ):
                judged_count = len(selected)
            else:
                judged_count = sum(
                    passage_id in judgment.judged_passage_ids for passage_id in selected
                )
            total_returned += len(selected)
            total_judged += judged_count
            per_question.append(
                {
                    "question_id": question_id,
                    "paper_id": qrels.questions[question_id],
                    "status": "missing_labels" if judgment is None else judgment.status,
                    "exclusion_reason": reason,
                    "metrics": metrics,
                    "returned_at_k": len(selected),
                    "judged_at_k": judged_count,
                    "judged_coverage_at_k": judged_count / len(selected)
                    if selected
                    else None,
                    "known_relevant_count": None
                    if judgment is None
                    else len(judgment.relevant_passage_ids),
                }
            )
        report["methods"][method] = {
            "question_count": len(qrels.questions),
            "labeled_questions": len(qrels.judgments),
            "eligible_questions": len(scores),
            "excluded_questions": dict(sorted(excluded.items())),
            "metrics": {
                name: sum(score[name] for score in scores) / len(scores)
                for name in sorted(_METRICS)
            }
            if scores
            else None,
            "returned_at_k": total_returned,
            "judged_at_k": total_judged,
            "judged_coverage_at_k": total_judged / total_returned
            if total_returned
            else None,
            "per_question": per_question,
        }
    return report
