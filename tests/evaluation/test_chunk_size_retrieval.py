"""Verify configured P1/P2 integration without downloading model weights.

Real BM25, FAISS, fusion and reranking operate on synthetic corpora. Loader
stubs capture inference settings while declaring the simulated model identity
in saved test manifests; they do not claim real BGE quality or tokenization.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from test_chunk_size import chunk_paper, synthetic_paper
from test_chunk_size import (
    exported_inputs as exported_inputs,  # noqa: PLC0414 -- re-export pytest fixture
)

from src.evaluation import chunk_size_retrieval as adapter
from src.evaluation import run_chunk_size as runner


@pytest.fixture
def model_stubs(monkeypatch: pytest.MonkeyPatch) -> dict:
    """Replace only model loaders and record actual inference calls.

    The real dense, hybrid and reranker implementations remain in the path.
    Metadata explicitly labels the resulting test artifacts as simulated.
    """
    import numpy as np
    import sentence_transformers
    import torch
    import transformers

    calls = {
        "dense_load": [],
        "encode": [],
        "reranker_load": [],
        "tokens": [],
        "device": [],
    }

    class SentenceModel:
        """Provide deterministic two-dimensional embeddings for FAISS.

        Constructor and encode calls capture the production loader arguments.
        """

        def __init__(self, name: str, **kwargs) -> None:
            """Capture requested checkpoint and expose its resolved SHA.

            No local model files or network resources are accessed.
            """
            calls["dense_load"].append((name, kwargs, self))
            self.model_card_data = SimpleNamespace(
                base_model_revision=kwargs["revision"]
            )
            self.max_seq_length = None

        def __getitem__(self, index: int) -> SimpleNamespace:
            """Expose the model revision in SentenceTransformer's shape.

            The adapter's immutable-checkpoint validation still executes.
            """
            return SimpleNamespace(
                auto_model=SimpleNamespace(config=SimpleNamespace(_commit_hash=None))
            )

        def encode(self, texts: list[str], **kwargs):
            """Encode full strings and retain options for parameter assertions.

            The vectors are synthetic and make no semantic relevance claim.
            """
            calls["encode"].append((list(texts), kwargs))
            return np.array([[1.0, float("alpha" in text)] for text in texts])

    class Tokenizer:
        """Return small CPU tensors while capturing query-passage pairs.

        Real tokenization and truncation are deliberately outside this test.
        """

        def __call__(self, pairs: list, **kwargs) -> dict:
            """Capture padding, truncation and length options from BGE.

            The batch dimension matches the number of requested pairs.
            """
            calls["tokens"].append((pairs, kwargs))
            return {"input_ids": torch.ones((len(pairs), 2), dtype=torch.long)}

    class PairModel:
        """Return deterministic nonpositive logits for actual rerank logic.

        Calls retain device selection and batching behavior without weights.
        """

        def to(self, device: str):
            """Capture the configured device and return this simulated model.

            The test uses CPU so generated tensors need no accelerator.
            """
            calls["device"].append(device)
            return self

        def eval(self):
            """Match the inference model interface without mutable training.

            There are no learned parameters or dropout in the stub.
            """
            return self

        def __call__(self, input_ids):
            """Return one raw logit per pair, including zero and negative values.

            This exercises the production scorer's expected tensor shape.
            """
            return SimpleNamespace(
                logits=-torch.arange(len(input_ids), dtype=torch.float32).reshape(-1, 1)
            )

    def loader(kind: str, result):
        """Create a capture callback for one Hugging Face loader.

        Both tokenizer and classifier must receive the exact same revision.
        """

        def load(name: str, **kwargs):
            """Record effective loading parameters and return the stub.

            No fallback or remote lookup occurs during this callback.
            """
            calls["reranker_load"].append((kind, name, kwargs))
            return result

        return load

    original_metadata = runner.configured_metadata

    def simulated_metadata(settings: dict) -> dict:
        """Identify loader substitutions honestly in test-only manifests.

        Production metadata is checked separately without the substitutions.
        """
        metadata = original_metadata(settings)
        metadata["test_double"] = "deterministic loader stubs; real BGE unverified"
        for kind in ("dense", "reranker"):
            if metadata[kind]["enabled"]:
                metadata[kind]["model_name"] = f"test/{kind}-stub"
        return metadata

    monkeypatch.setattr(sentence_transformers, "SentenceTransformer", SentenceModel)
    monkeypatch.setattr(
        transformers.AutoTokenizer, "from_pretrained", loader("tokenizer", Tokenizer())
    )
    monkeypatch.setattr(
        transformers.AutoModelForSequenceClassification,
        "from_pretrained",
        loader("model", PairModel()),
    )
    monkeypatch.setattr(runner, "configured_metadata", simulated_metadata)
    return calls


def test_projection_and_bm25_contract() -> None:
    """Check strict projection, intact provenance and paper-only retrieval.

    The adapter must return exactly the ranking produced by the P1 retriever.
    """
    from src.retrieval.bm25_retriever import BM25Retriever

    records = chunk_paper(synthetic_paper(), 4, 1)
    before = copy.deepcopy(records)
    public = adapter.project_passages(records)
    assert [item.model_dump() for item in public] == [
        {key: record[key] for key in adapter.PUBLIC_FIELDS} for record in records
    ]
    retrieve = adapter.make_retriever_factory({})(records)
    expected = BM25Retriever(public).retrieve("alpha", "paper-train", 5)
    assert retrieve("alpha", "paper-train", 5) == [
        (hit.passage.passage_id, hit.score) for hit in expected
    ]
    assert retrieve("alpha", "missing-paper", 5) == []
    assert len(retrieve("alpha", "paper-train", 5)) == len(records) < 5
    assert records == before
    with pytest.raises(ValueError):
        adapter.project_passages([{**records[0], "chunk_number": True}])
    with pytest.raises(ValueError):
        adapter.project_passages([{**records[0], "text": " bad normalization "}])


@pytest.mark.parametrize(
    "patch",
    [
        None,
        [],
        {"unknown": 1},
        {"mode": "other"},
        {"mode": []},
        {"candidate_k": True},
        {"rrf_k": 0},
        {"dense": None},
        {"reranker": []},
        {"dense": {"model_name": "other"}},
        {"dense": {"revision": "main"}},
        {"dense": {"revision": "A" * 40}},
        {"dense": {"device": " "}},
        {"dense": {"cache_folder": ""}},
        {"dense": {"local_files_only": 1}},
        {"dense": {"batch_size": False}},
        {"reranker": {"max_length": 513}},
        {"reranker": {"max_length": True}},
        {"reranker": {"batch_size": -1}},
        {"mode": "hybrid", "candidate_k": 4},
        {"mode": "hybrid_rerank", "candidate_k": 1},
    ],
)
def test_invalid_retrieval_configuration(patch) -> None:
    """Reject malformed and unused nested settings before creating outputs.

    Booleans are not integers and null is never a missing configuration block.
    """
    with pytest.raises(ValueError):
        adapter.normalize_retrieval(patch)


def test_defaults_and_active_metadata() -> None:
    """Verify nested defaults, fixed identities and disabled components.

    Configured metadata must not claim model loading in a BM25 comparison.
    """
    config = adapter.normalize_retrieval({"dense": {"batch_size": 2}})
    assert config["mode"] == "bm25"
    assert config["dense"]["revision"] == adapter.DENSE_REVISION
    assert config["dense"]["batch_size"] == 2
    assert Path(config["dense"]["cache_folder"]).is_absolute()
    assert config["dense"]["local_files_only"] is True
    metadata = adapter.retriever_metadata(config)
    assert metadata["dense"] == {"enabled": False}
    assert metadata["reranker"] == {"enabled": False}
    assert metadata["source_commit"] == adapter.SOURCE_COMMIT
    full = adapter.retriever_metadata({"mode": "hybrid_rerank"})
    assert full["dense"]["query_instruction"] == adapter.QUERY_INSTRUCTION
    assert full["reranker"]["tokenizer_revision"] == adapter.RERANKER_REVISION
    assert full["rerank_all_fused_candidates"] is True
    assert full["persistent_score_cache"] is False


def test_score_conversion_preserves_order() -> None:
    """Zero and negative logits override RRF; None uses the fusion score.

    Conversion must not reorder upstream results by a different score scale.
    """
    hits = [
        SimpleNamespace(
            passage=SimpleNamespace(passage_id=str(i)),
            rrf_score=0.1,
            reranker_score=score,
        )
        for i, score in enumerate((0.0, -2.0, None))
    ]
    assert adapter.scored_ids(hits) == [("0", 0.0), ("1", -2.0), ("2", 0.1)]


@pytest.mark.parametrize("mode", ["dense", "hybrid", "hybrid_rerank"])
def test_upstream_ranking_and_full_union(
    mode: str, model_stubs: dict, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Check P1/P2 scores and full candidate reranking through configuration.

    Eight candidates exceed top-five so premature truncation loses evidence.
    The model constructors receive nondefault settings for forwarding checks.
    """
    from src.retrieval import reranker
    from src.retrieval.bm25_retriever import BM25Retriever
    from src.retrieval.dense_retriever import DenseRetriever
    from src.retrieval.fusion import reciprocal_rank_fusion

    records = [
        {
            "passage_id": f"opaque-{i}",
            "paper_id": "paper",
            "title": "Synthetic",
            "section": "Body",
            "chunk_number": i,
            "text": f"word{i} alpha",
            "previous_passage_id": None,
            "next_passage_id": None,
            "spans": {},
        }
        for i in range(8)
    ]
    observed = []

    class Scorer:
        """Favor the last fused candidate, outside the initial top-five.

        Constructor settings and all scored texts are retained for assertions.
        """

        def __init__(self, **kwargs) -> None:
            """Capture effective BGE settings while declaring a fake identity.

            The scorer has no model weights and is used only for wiring tests.
            """
            self.model_name = "test/full-union-scorer"
            observed.append(kwargs)

        def score(self, query: str, texts: list[str]) -> list[float]:
            """Assign increasing logits after seeing the complete fused union.

            Larger scores reverse the RRF ranking and expose early truncation.
            """
            observed.append(list(texts))
            return [float(i) for i in range(len(texts))]

    monkeypatch.setattr(reranker, "BGEReranker", Scorer)
    settings = {
        "mode": mode,
        "candidate_k": 8,
        "rrf_k": 11,
        "dense": {
            "revision": "a" * 40,
            "batch_size": 3,
            "device": "cpu",
            "cache_folder": "tmp/tmp_models",
            "local_files_only": False,
        },
        "reranker": {
            "revision": "b" * 40,
            "batch_size": 3,
            "max_length": 64,
            "device": "cpu",
            "cache_folder": "tmp/tmp_models",
            "local_files_only": False,
        },
    }
    retrieve = adapter.make_retriever_factory(settings)(records)
    hits = retrieve("alpha", "paper", 5)
    assert retrieve("alpha", "unknown-paper", 5) == []
    normalized = adapter.normalize_retrieval(settings)
    public = adapter.project_passages(records)
    dense = DenseRetriever(public, **normalized["dense"])
    if mode == "dense":
        assert hits == adapter.scored_ids(dense.retrieve("alpha", "paper", 5))
        assert not observed
    else:
        sparse = BM25Retriever(public)
        fused = reciprocal_rank_fusion(
            {
                "bm25": sparse.retrieve("alpha", "paper", 8),
                "dense": dense.retrieve("alpha", "paper", 8),
            },
            rrf_k=11,
        )
        if mode == "hybrid":
            assert hits == [
                (hit.passage.passage_id, hit.rrf_score) for hit in fused[:5]
            ]
            assert not observed
        else:
            assert observed[0] == normalized["reranker"]
            assert observed[1] == [hit.passage.text for hit in fused]
            assert len(observed[1]) == 8
            assert (
                hits
                == [
                    (hit.passage.passage_id, float(i))
                    for i, hit in reversed(list(enumerate(fused)))
                ][:5]
            )
    name, kwargs, _ = model_stubs["dense_load"][0]
    assert name == "BAAI/bge-small-en-v1.5"
    assert kwargs == {
        key: value for key, value in normalized["dense"].items() if key != "batch_size"
    }
    assert model_stubs["encode"][0][1]["batch_size"] == 3


@pytest.mark.parametrize("mode", ["bm25", "dense", "hybrid", "hybrid_rerank"])
def test_modes_end_to_end(
    exported_inputs: tuple, tmp_path: Path, model_stubs: dict, mode: str
) -> None:
    """Run each configured mode through synthetic export, indexes and reports.

    Each candidate's encoded texts and result IDs must match its own corpus;
    shared questions and source locations must match the same seeded baseline.
    """
    papers, qa, export, config_path = exported_inputs
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config["retrieval"] = {
        "mode": mode,
        "dense": {"batch_size": 2},
        "reranker": {"batch_size": 2, "max_length": 128},
    }
    config_path.write_text(json.dumps(config), encoding="utf-8")
    assert json.loads(config_path.read_text(encoding="utf-8")) == config
    run = runner.run_comparison(
        config_path=config_path,
        papers_path=papers,
        qa_path=qa,
        export_manifest=export,
        output_root=tmp_path / "tmp_results",
        run_id=mode,
    )
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    summary = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    assert manifest["retriever"]["mode"] == mode
    assert manifest["retriever"]["test_double"]
    assert manifest["config"]["retrieval"] == adapter.normalize_retrieval(
        config["retrieval"]
    )
    assert manifest["question_ids"] == ["question-train", "question-validation"]
    assert "no hidden warm-up" in manifest["timing_policy"]
    encoded = [
        text
        for texts, _ in model_stubs["encode"]
        for text in texts
        if not text.startswith(adapter.QUERY_INSTRUCTION)
    ]
    expected_encoded = []
    for size in (4, 6):
        corpus = [
            record
            for split in ("train", "validation")
            for record in chunk_paper(synthetic_paper(split), size, 1)
        ]
        by_id = {item["passage_id"]: item for item in corpus}
        expected_encoded.extend(item["text"] for item in corpus)
        result = summary["sizes"][str(size)]
        assert result["index_seconds"] >= 0
        for question in result["questions"]:
            retrieved = [by_id[hit["passage_id"]] for hit in question["retrieved"]]
            assert all(
                item["paper_id"]
                == question["question_id"].replace("question-", "paper-")
                for item in retrieved
            )
            assert question["total_retrieved_words"] == sum(
                len(item["text"].split()) for item in retrieved
            )
            assert question["evidence_hit_at_5"]
        assert (run / f"chunk_size_{size}" / "evidence_review.md").is_file()
        assert (run / f"chunk_size_{size}" / "readability.md").is_file()
    if mode == "bm25":
        assert not model_stubs["dense_load"]
    else:
        assert sorted(encoded) == sorted(expected_encoded)
        assert len(model_stubs["dense_load"]) == 2
        for name, kwargs, model in model_stubs["dense_load"]:
            assert name == "BAAI/bge-small-en-v1.5"
            assert kwargs == {
                "revision": adapter.DENSE_REVISION,
                "device": "cpu",
                "cache_folder": str(adapter.ROOT / ".cache/huggingface"),
                "local_files_only": True,
            }
            assert model.max_seq_length == 512
        assert any(
            texts == [adapter.QUERY_INSTRUCTION + "alpha gamma?"]
            for texts, _ in model_stubs["encode"]
        )
        assert all(
            kwargs
            == {
                "batch_size": 2,
                "convert_to_numpy": True,
                "normalize_embeddings": False,
                "show_progress_bar": False,
                "prompt": "",
            }
            for _, kwargs in model_stubs["encode"]
        )
    if mode == "hybrid_rerank":
        assert len(model_stubs["reranker_load"]) == 4
        for _, name, kwargs in model_stubs["reranker_load"]:
            assert name == "BAAI/bge-reranker-base"
            assert kwargs == {
                "revision": adapter.RERANKER_REVISION,
                "cache_dir": str(adapter.ROOT / ".cache/huggingface"),
                "local_files_only": True,
            }
        assert model_stubs["device"] == ["cpu", "cpu"]
        assert all(
            len(pairs) <= 2
            and kwargs
            == {
                "padding": True,
                "truncation": True,
                "max_length": 128,
                "return_tensors": "pt",
            }
            for pairs, kwargs in model_stubs["tokens"]
        )
    else:
        assert not model_stubs["reranker_load"]
    baseline = runner.run_comparison(
        config_path=config_path,
        papers_path=papers,
        qa_path=qa,
        export_manifest=export,
        output_root=tmp_path / "tmp_results",
        run_id=mode + "_repeat",
    )
    repeated = json.loads((baseline / "manifest.json").read_text(encoding="utf-8"))
    assert repeated["question_ids"] == manifest["question_ids"]
    assert repeated["readability_samples"] == manifest["readability_samples"]


def test_custom_factory_metadata(exported_inputs: tuple, tmp_path: Path) -> None:
    """Retain the Python extension while rejecting mismatched metadata.

    The manifest must identify the custom implementation instead of BGE/BM25.
    """
    papers, qa, export, config = exported_inputs
    args = {
        "config_path": config,
        "papers_path": papers,
        "qa_path": qa,
        "export_manifest": export,
        "output_root": tmp_path / "tmp_results",
        "run_id": "custom",
    }
    with pytest.raises(ValueError, match="custom factory"):
        runner.run_comparison(**args, retriever_metadata={"id": "fake"})
    with pytest.raises(ValueError, match="explicit metadata"):
        runner.run_comparison(**args, retriever_factory=runner.local_bm25)
    run = runner.run_comparison(
        **args,
        retriever_factory=runner.local_bm25,
        retriever_metadata={"id": "custom-p1-wrapper"},
    )
    metadata = json.loads((run / "manifest.json").read_text(encoding="utf-8"))[
        "retriever"
    ]
    assert metadata == {"id": "custom-p1-wrapper", "selection_source": "custom_factory"}


def test_lightweight_subprocess() -> None:
    """A fresh BM25 process and summary import must avoid model libraries.

    Checking sys.modules in a fresh interpreter avoids contamination by tests.
    """
    code = """
import sys
from scripts.evaluate_chunk_size import main
from src.evaluation.run_chunk_size import local_bm25
assert not any(n in sys.modules for n in ('faiss', 'sentence_transformers', 'torch', 'transformers'))
r = dict(passage_id='a', paper_id='p', title='t', section='s', chunk_number=0, text='alpha', previous_passage_id=None, next_passage_id=None, spans={})
assert local_bm25([r])('alpha', 'p', 5)[0][0] == 'a'
assert not any(n in sys.modules for n in ('faiss', 'sentence_transformers', 'torch', 'transformers'))
"""
    subprocess.run(
        [sys.executable, "-c", code],
        cwd=adapter.ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize(
    "failure",
    [
        OSError("missing pinned weights"),
        RuntimeError("unavailable device"),
        ImportError("missing dependency"),
    ],
)
def test_model_failure_is_incomplete(
    exported_inputs: tuple,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: Exception,
) -> None:
    """Model setup failures leave no completion marker or silent fallback.

    The failed run ID remains reserved so a retry cannot overwrite evidence.
    """
    from src.retrieval import dense_retriever

    def fail(*args, **kwargs):
        """Raise the configured setup failure before an index is available.

        This simulates dependency, pinned-cache and device errors offline.
        """
        raise failure

    monkeypatch.setattr(dense_retriever, "DenseRetriever", fail)
    papers, qa, export, config_path = exported_inputs
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config["retrieval"] = {"mode": "dense"}
    config_path.write_text(json.dumps(config), encoding="utf-8")
    assert json.loads(config_path.read_text(encoding="utf-8")) == config
    args = {
        "config_path": config_path,
        "papers_path": papers,
        "qa_path": qa,
        "export_manifest": export,
        "output_root": tmp_path / "tmp_results",
        "run_id": "failed",
    }
    with pytest.raises(RuntimeError, match="No fallback"):
        runner.run_comparison(**args)
    assert not (args["output_root"] / "failed" / "manifest.json").exists()
    with pytest.raises(FileExistsError):
        runner.run_comparison(**args)
