"""Bounded real-index checks of the P1 -> P2 -> P4 control-flow boundary.

This is an integration check, not an evaluation of the keyword mock critic.
Run from a checkout containing P4 and the local P1 Week 3/4 increment.
"""

from __future__ import annotations

import json
import math
import platform
import subprocess
import sys
from importlib.metadata import version
from pathlib import Path

from scripts.build_indexes import PINNED_REVISION
from src.agent.graph import build_agent_graph
from src.agent.schemas import AgentState
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DEFAULT_MODEL_NAME, DenseRetriever
from src.retrieval.experiment import (
    DevelopmentQuestion,
    _same_passages,
    file_sha256,
    load_experiment_inputs,
)
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.schemas import RetrievalHit, RetrievedPassage


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _hit_record(hit: RetrievalHit | RetrievedPassage) -> dict:
    record = hit.model_dump(mode="json", exclude={"passage"})
    record.update(
        passage_id=hit.passage.passage_id,
        paper_id=hit.passage.paper_id,
        section=hit.passage.section,
    )
    return record


class TracedRequest:
    """Own one immutable section binding; reuse the underlying P1 indexes."""

    def __init__(self, bm25, dense, passages, *, section, top_k=5, candidate_k=20):
        self.section = section
        self.top_k = top_k
        self.candidate_k = candidate_k
        self.by_id = {p.passage_id: p for p in passages}
        self.rounds: list[dict] = []
        self.hybrid = HybridRetriever(
            self._source("bm25", bm25),
            self._source("dense", dense),
            candidate_k=candidate_k,
        )
        # Leave P4's default retry budget unchanged (two retries).
        self.graph = build_agent_graph(self.retrieve, top_k=top_k)

    def _source(self, name, backend):
        section = self.section

        def retrieve(query, paper_id, top_k):
            current = self.rounds[-1]
            _check(query == current["query"], "P1 query differs from P4 query")
            _check(paper_id == current["paper_id"], "P1 paper scope differs")
            _check(top_k == self.candidate_k, "P2 candidate budget differs")
            hits = backend.retrieve(query, paper_id, top_k, section=section)
            allowed = current["available_candidate_ids"]
            _check(len(hits) == min(top_k, len(allowed)), "P1 candidate count")
            _check(len({h.passage.passage_id for h in hits}) == len(hits), "P1 IDs")
            for rank, hit in enumerate(hits, 1):
                _check(hit.rank == rank, "P1 ranks must be continuous")
                _check(hit.passage.passage_id in allowed, "P1 scope violation")
                _check(self.by_id[hit.passage.passage_id] == hit.passage, "P1 mapping")
                _check(math.isfinite(hit.score), "P1 nonfinite score")
            _check(
                [h.score for h in hits]
                == sorted((h.score for h in hits), reverse=True),
                "P1 score ordering",
            )
            current["sources"][name] = {
                "query": query,
                "paper_id": paper_id,
                "section": section,
                "requested_k": top_k,
                "hits": [_hit_record(hit) for hit in hits],
            }
            return hits

        return retrieve

    def retrieve(self, query, paper_id, top_k):
        _check(top_k == self.top_k, "P4 output budget differs")
        allowed = sorted(
            p.passage_id
            for p in self.by_id.values()
            if p.paper_id == paper_id
            and (self.section is None or p.section == self.section)
        )
        current = {
            "round": len(self.rounds) + 1,
            "query": query,
            "paper_id": paper_id,
            "section": self.section,
            "top_k": top_k,
            "available_candidate_ids": allowed,
            "sources": {},
        }
        self.rounds.append(current)
        hits = self.hybrid.retrieve(query, paper_id, top_k)
        sources = {
            name: {hit["passage_id"]: hit for hit in source["hits"]}
            for name, source in current["sources"].items()
        }
        union = set().union(*(set(source) for source in sources.values()))
        totals = {
            pid: sum(
                1 / (60 + source[pid]["rank"])
                for source in sources.values()
                if pid in source
            )
            for pid in union
        }
        expected = sorted(union, key=lambda pid: (-totals[pid], pid))[:top_k]
        _check(
            [h.passage.passage_id for h in hits] == expected, "Hybrid RRF order/count"
        )
        for rank, hit in enumerate(hits, 1):
            _check(isinstance(hit, RetrievedPassage), "P4 needs RetrievedPassage")
            _check(hit.rank == rank, "Hybrid rank")
            _check(self.by_id[hit.passage.passage_id] == hit.passage, "Hybrid mapping")
            expected_sources = {
                name: {
                    key: source[hit.passage.passage_id][key]
                    for key in ("rank", "score")
                }
                for name, source in sources.items()
                if hit.passage.passage_id in source
            }
            _check(
                {name: score.model_dump() for name, score in hit.source_scores.items()}
                == expected_sources,
                "Hybrid source provenance",
            )
            _check(
                math.isclose(hit.rrf_score, totals[hit.passage.passage_id]), "RRF score"
            )
        current["unique_candidate_ids"] = sorted(union)
        current["returned"] = [_hit_record(hit) for hit in hits]
        return hits

    def invoke(self, question: DevelopmentQuestion, label: str) -> dict:
        self.rounds = []
        # question_id is trace metadata: P4's existing schema has no such field.
        initial = {"question": question.query, "paper_id": question.paper_id}
        result = AgentState.model_validate(self.graph.invoke(initial))
        _check(result.paper_id == question.paper_id, "P4 changed the request paper")
        _check(1 <= result.retrieval_round <= 3, "Default retry limit")
        _check(result.retrieval_round == len(self.rounds), "Round count mismatch")
        _check(self.rounds[0]["query"] == question.query, "Initial query mismatch")
        _check(len(result.retrieval_log) == len(self.rounds), "P4 log length")
        first_seen = {}
        for log, trace in zip(result.retrieval_log, self.rounds, strict=True):
            _check(trace["paper_id"] == question.paper_id, "P4 called another paper")
            _check(log["query"] == trace["query"], "P4/P1 query trace mismatch")
            _check(log["round"] == trace["round"], "P4/P1 round trace mismatch")
            _check(
                log["passage_ids"] == [h["passage_id"] for h in trace["returned"]],
                "P4/P2 passage trace mismatch",
            )
            if trace["round"] > 1:
                _check(trace["query"] != question.query, "Rewrite did not reach P1")
            for hit in trace["returned"]:
                first_seen.setdefault(hit["passage_id"], hit)
        accumulated = [_hit_record(hit) for hit in result.retrieved_passages]
        _check(
            accumulated == list(first_seen.values()),
            "Cross-round dedup/first occurrence",
        )
        if not result.sufficient:
            _check(
                result.retrieval_round == 3, "Insufficient evidence must exhaust budget"
            )
        return {
            "case": label,
            "question_id": question.question_id,
            "input": initial,
            "section": self.section,
            "top_k": self.top_k,
            "candidate_k": self.candidate_k,
            "rounds": self.rounds,
            "retry_count": result.retrieval_round - 1,
            "accumulated": accumulated,
            "agent_state": result.model_dump(
                mode="json", exclude={"retrieved_passages"}
            ),
            "status": "passed",
        }


def run_agent_integration(artifact_root: Path, output_dir: Path) -> dict:
    """Reuse verified artifacts for fixed train questions; never build embeddings."""
    root = artifact_root.resolve()
    _check(
        not output_dir.exists() or not any(output_dir.iterdir()),
        "Output must be new or empty",
    )
    data = root / ".cache/p3-week3-week4/data/processed"
    inputs = load_experiment_inputs(
        data / "passages.jsonl",
        data / "passages.manifest.json",
        data / "qa.jsonl",
        data / "qasper_export.manifest.json",
    )
    index_paths = {
        "bm25": root / "indexes/p1-week3-week4-bm25",
        "dense": root / "indexes/p1-week3-week4-development",
    }
    metadata_hashes = {}
    for name, directory in index_paths.items():
        metadata_path = directory / "metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        _same_passages(
            [p for paper in metadata["papers"] for p in paper["passages"]],
            inputs.passages,
            name,
        )
        metadata_hashes[name] = file_sha256(metadata_path)
        if name == "dense":
            _check(
                metadata["revision"] == PINNED_REVISION, "Dense model revision mismatch"
            )
            _check(metadata["model_name"] == DEFAULT_MODEL_NAME, "Dense model mismatch")
    cache = root / ".cache/huggingface"
    snapshot = cache / "models--BAAI--bge-small-en-v1.5/snapshots" / PINNED_REVISION
    _check(snapshot.is_dir(), "Matching local model snapshot is required")
    bm25 = BM25Retriever.load(index_paths["bm25"])
    dense = DenseRetriever.load(
        index_paths["dense"],
        revision=PINNED_REVISION,
        cache_folder=cache,
        device="cpu",
        local_files_only=True,
    )
    questions = {q.question_id: q for q in inputs.questions}
    q1 = questions["0038b073b7cca847033177024f9719c971692042"]
    q2 = questions["003f884d3893532f8c302431c9f70be6f64d9be8"]
    q3 = questions["0062ad4aed09a57d0ece6aa4b873f4a4bf65d165"]
    empty = questions["2a0f14740ee14224d116d4f51dacde6863bcdc1e"]

    def request(question, section=None, top_k=5):
        if section is not None:
            # Bind the exact name read from the corpus, not a fabricated label.
            section = next(
                p.section
                for p in inputs.passages
                if p.paper_id == question.paper_id and p.section == section
            )
        return TracedRequest(bm25, dense, inputs.passages, section=section, top_k=top_k)

    approach = request(q1, "Approach")
    cases = [approach.invoke(q1, "approach-before")]
    for question, section, top_k, label in (
        (q2, "Acknowledgements", 5, "different-question-paper-section"),
        (q3, "Results", 2, "one-available-passage"),
        (q1, "Model", 3, "same-question-different-section"),
        (empty, None, 5, "known-paper-without-passages"),
        (q1, None, 5, "whole-paper"),
    ):
        cases.append(request(question, section, top_k).invoke(question, label))
    cases.append(approach.invoke(q1, "approach-after"))
    _check(
        {k: v for k, v in cases[0].items() if k != "case"}
        == {k: v for k, v in cases[-1].items() if k != "case"},
        "Interleaved request/graph state leaked",
    )
    empty_case = next(c for c in cases if c["case"] == "known-paper-without-passages")
    _check(
        empty_case["retry_count"] == 2 and not empty_case["accumulated"],
        "Empty termination",
    )
    code_root = Path(__file__).resolve().parents[2]
    source_files = [
        *sorted((code_root / "src/agent").glob("*.py")),
        *[
            code_root / "src/retrieval" / name
            for name in (
                "agent_integration.py",
                "experiment.py",
                "bm25_retriever.py",
                "dense_retriever.py",
                "hybrid_retriever.py",
                "schemas.py",
                "fusion.py",
            )
        ],
        code_root / "scripts/run_p1_integration.py",
    ]
    report = {
        "status": "passed",
        "evidence_kind": "real retrieval to mock-agent control-flow integration",
        "quality_metrics": {"status": "unavailable", "metrics": None},
        "section_policy": "fixed per request; no gap-driven section switching",
        "annotations_used": False,
        "base_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=code_root, text=True
        ).strip(),
        "source_sha256": {
            str(p.relative_to(code_root)): file_sha256(p) for p in source_files
        },
        "input_provenance": inputs.provenance,
        "index_metadata_sha256": metadata_hashes,
        "model_revision": PINNED_REVISION,
        "model_cache_snapshot": str(snapshot),
        "python": sys.executable,
        "platform": platform.platform(),
        "versions": {
            name: version(name)
            for name in (
                "langgraph",
                "pydantic",
                "sentence-transformers",
                "transformers",
                "torch",
                "faiss-cpu",
                "rank-bm25",
            )
        },
        "cases": cases,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "trace.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return {
        "status": "passed",
        "cases": len(cases),
        "retrieval_rounds": sum(len(c["rounds"]) for c in cases),
    }
