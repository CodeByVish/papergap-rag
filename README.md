# PaperGap

An evidence-gap-driven agentic RAG system for adaptive multi-section question answering over NLP research papers.

**Status:** P1 independent BM25 and dense/FAISS retrieval are implemented and verified with synthetic passages. P2 Week 1 fusion, reranking and mock integration are implemented. P3 real corpus integration is still pending. Generation and the UI are also pending. See [P2 setup and handoff](docs/P2_WEEK1.md).

## Start here

- [Week-by-week execution plan](docs/EXECUTION_PLAN.md): tasks, deliverables and integration checkpoints.
- [Requirements and open decisions](docs/REQUIREMENTS.md): rubric mapping and decisions to resolve in Week 1.
- [Evaluation protocol](docs/EVALUATION.md): annotation, held-out data and experiment comparisons.
- [Contributing](CONTRIBUTING.md): setup, branches, reviews and module ownership.
- [Weekly tracker](docs/WEEKLY_TRACKER.md): update at each team meeting.

## Team

| Member | Name | Main ownership | Experiment ownership |
| --- | --- | --- | --- |
| P1 | Junlin Yin | BM25 and dense retrieval; standard retrieval API | BM25 vs dense |
| P2 | Vishakha | Hybrid fusion and reranking | Hybrid and reranking ablations |
| P3 | Jingshuai Qian | QASPER processing, chunks and passage schema | Chunking and corpus statistics |
| P4 | Ananya | LangGraph planner, critic and adaptive retrieval | Static vs adaptive RAG |
| P5 | Pending | Generation, citations and answer API | QA and grounding |
| P6 | Pending | Streamlit, evaluation infrastructure and reproducibility | RAGAS and end-to-end latency |

Everyone annotates, writes their report section, validates their module and reviews another member's work. P6 coordinates integration; each producer owns their interface and integration fixes.

## Planned pipeline

Selected paper + question → BM25 and dense retrieval → RRF → reranking → evidence critic → targeted retrieval if needed → evidence-conditioned answer or abstention → citation validation → Streamlit.

Maximum: one initial retrieval plus two retries. Optional dual critics and NLI come after the required pipeline and evaluation work.

## Local setup

Use Python 3.11 as the starter environment. Run these commands inside the cloned `papergap-rag` directory:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Windows activation: `.venv\Scripts\activate`.

The dependency files are provisional ranges, not a tested lockfile. Installation downloads libraries, not model weights or the dataset. University GPU access is available; P5 must confirm hardware and allocation details before model setup; vLLM and GPU-specific packages are deliberately separate decisions. P6 should record resolved versions after the first successful clean installation. No application launch command exists yet.

## P1 retrieval: Week 1 / Week 2

Use Python 3.11 with the dependencies from `requirements-dev.txt` installed as described above. For an existing Conda environment, run `conda activate papergap` and check `python --version`; a VS Code interpreter selection does not change every terminal's Python. Run all commands below from the repository root.

`BM25Retriever` and `DenseRetriever` share this interface:

```python
retrieve(query: str, paper_id: str, top_k: int) -> list[RetrievalHit]
```

Both use the existing `Passage` and `RetrievalHit` schemas. Results preserve the original Passage fields and IDs, use continuous ranks starting at 1, and contain at most K distinct passages from the selected paper. Unknown papers return `[]`; invalid queries, paper IDs and K values raise `ValueError`. Each paper has its own index, so retrieval selects the top K within that paper. Equal scores are ordered by passage ID.

Dense retrieval uses `BAAI/bge-small-en-v1.5`. The commands below pin revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` and default to CPU. Only queries receive `Represent this sentence for searching relevant passages: `, including the trailing space; passages use their original text. Both embedding types receive L2 normalization, and FAISS `IndexFlatIP` computes cosine similarity. This embedding model is separate from P2's `BAAI/bge-reranker-base` cross-encoder.

Build the dense index from an explicit Passage JSONL input:

```bash
python -B -m scripts.build_indexes --passages tests/fixtures/mock_passages.jsonl --output-dir indexes/p1-week2-synthetic --local-files-only
```

The output directory must be new or empty. The saved artifacts contain the per-paper FAISS indexes, complete row-to-Passage mappings, and checked model/encoding metadata; loading them does not re-encode passages. BM25 is built in memory from the JSONL input and is not persisted by this command. `--model-name` accepts only the selected BGE model; `--revision`, `--device` and `--cache-folder` are available when an explicit setting is needed. `--revision` must be a 40-character lowercase commit SHA; branch and tag names such as `main` are rejected. Use the same revision when building and loading. The default model cache is `.cache/huggingface`. `--local-files-only` requires the pinned model to be cached; omit it to allow a first model download.

Run a sample query against BM25 and the saved dense index:

```bash
python -B -m scripts.demo_p1 --passages tests/fixtures/mock_passages.jsonl --dense-index-dir indexes/p1-week2-synthetic --paper-id synthetic-ir --query "Which method uses sparse term matching for passage retrieval?" --top-k 3 --local-files-only
```

Without `--dense-index-dir`, the demo builds dense indexes in memory from the supplied JSONL. The demo reports both rankings and times `retrieve` with `time.perf_counter` after one warm-up call per retriever. Loading, passage encoding and index construction are excluded; dense query encoding is included. The bundled fixture has eight synthetic passages across two papers. These timings are only a local smoke measurement, not real-corpus performance results.

Run the offline regression tests with the same Python 3.11 interpreter:

```bash
python -B -m pytest tests/test_p1.py -v
python -B -m pytest -q
```

Dense unit tests use deterministic fake encoders with real FAISS and do not download models. A real SentenceTransformer run is a separate smoke check. See the [P1 verification record](docs/WEEKLY_TRACKER.md#p1-verification-evidence) for the completed CLI run, regression results and preliminary synthetic timings. P3 real corpus integration is still pending. Week 3 retrieval metrics and failure analysis are outside these commands. Keep real data, model weights, caches, indexes and generated results in the ignored local directories; only the small synthetic fixture belongs in Git.

## Repository layout

```text
docs/                 Plan, requirements, evaluation and team tracker
configs/              Proposed shared configuration
src/data/             P3: data preparation
src/retrieval/        P1/P2: retrievers, fusion and reranking
src/agent/            P4: planning and adaptive retrieval
src/generation/       P5: generation and citation validation
src/evaluation/       P6 + experiment owners: metrics and logging
src/ui/               P6: Streamlit
scripts/              Reproducible command-line entry points
tests/                Module and integration tests
data/                Local datasets (ignored except README)
results/              Local experiment outputs (ignored except README)
```

## Assignment delivery

Deadline supplied: **7 November, 11:59 PM SGT**. Submit one PDF with team details, the full report, and accessible links to code and datasets/results. Target code/report freeze: 6 November.

**Rubric clarification confirmed by the team:** passage chunks count toward 10,000 documents, and query–passage pairs count toward 1,000 evaluation records. Actual corpus size and annotation agreement still need verification; see [requirements](docs/REQUIREMENTS.md).
