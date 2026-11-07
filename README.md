# PaperGap

An evidence-gap-driven agentic RAG system for adaptive multi-section question answering over NLP research papers.

**Status (7 November 2026, submission day):** the system, the experiments and the report draft are complete. The frozen configuration was evaluated once on 200 held-out questions (Slurm job 51585), with a post-hoc sensitivity run at a larger context budget and a development-slice ablation of rewriting and reranking. The final results are committed under [`results/final/`](results/final/README.md) and written up in [`report/`](report/README.md). Hybrid retrieval (BM25 + dense, fused by RRF) is the retrieval baseline; on the held-out run the evidence-gap loop adds 0.013 to mapped-evidence recall over static top-eight retrieval but nothing over reading the same number of passages, so the report does not claim that it improves recall or answers (see [Final configuration and results](#final-configuration-and-results)). Shared schemas and split mappings stay `v0-proposed` until the team confirms them.

## Start here

- [Final results](results/final/README.md): reviewed outputs per owner (`p1`, `p2`, `p4`, `p5`), with checksums.
- [Report source](report/README.md): the LaTeX report, how to build it and where its numbers come from.
- [Week-by-week execution plan](docs/EXECUTION_PLAN.md): tasks, deliverables and integration checkpoints.
- [Requirements and open decisions](docs/REQUIREMENTS.md): rubric mapping and decisions to resolve in Week 1.
- [Evaluation protocol](docs/EVALUATION.md): annotation, held-out data and experiment comparisons.
- [Contributing](CONTRIBUTING.md): setup, branches, reviews and module ownership.
- [Weekly tracker](docs/WEEKLY_TRACKER.md): update at each team meeting.
- [P4 freeze record](docs/P4_FREEZE_RECORD.md) and [agent contribution](docs/P4_REPORT_CONTRIBUTION.md): what was fixed before the held-out run and how it was scored.
- [P1 used-question inventory](docs/handoffs/P1_QUESTION_USAGE.md): prior development usage for the team held-out exclusion audit.

## Team

| Member | Name | Main ownership | Experiment ownership |
| --- | --- | --- | --- |
| P1 | Junlin Yin | BM25 and dense retrieval; standard retrieval API | BM25 vs dense |
| P2 | Vishakha | Hybrid fusion and reranking | Hybrid and reranking ablations |
| P3 | Jingshuai Qian | QASPER processing, chunks and passage schema | Chunking and corpus statistics |
| P4 | Ananya | LangGraph planner, critic and adaptive retrieval | Static vs adaptive RAG |
| P5 | Junyu Hu | Generation, citations and answer API (v7/R4 integrated) | QA and grounding |
| P6 | Changyan Xu | Streamlit, evaluation infrastructure and reproducibility | RAGAS and end-to-end latency |

Everyone annotates, writes their report section, validates their module and reviews another member's work. P6 coordinates integration; each producer owns their interface and integration fixes.

## Pipeline

Selected paper + question → BM25 and dense (`BAAI/bge-small-en-v1.5`) retrieval → reciprocal rank fusion (RRF) → top eight passages → evidence critic → targeted retrieval if needed → evidence-conditioned answer (Qwen3-8B) or abstention → citation validation → Streamlit UI.

Maximum: one initial retrieval plus two retries (at most three rounds). The `BAAI/bge-reranker-base` reranker is implemented but **off** in the final configuration: on the accepted relevance labels it lowered all four top-five metrics. Dual critics and an NLI check were not part of the evaluated pipeline. The frozen settings are in [`configs/p4_freeze.json`](configs/p4_freeze.json); the knowledge base is 28,617 passages (365-word chunks, 40-word overlap) from 1,584 QASPER papers.

## Final configuration and results

| Question | Result | Where |
| --- | --- | --- |
| Retrieval, K = 5, 200 questions, accepted pooled labels | MRR@5: RRF 0.804, dense 0.799, BM25 0.730; adding the BGE reranker lowers all four top-five metrics | [`results/final/p1`](results/final/p1/README.md), [`p2`](results/final/p2/README.md) |
| Held-out agent run, 200 questions, mapped-evidence recall | Static top-8 0.858; adaptive 0.871; the loop's gain at an equal passage budget is 0.001 (95% interval −0.014 to 0.016) | [`results/final/p4`](results/final/p4/README.md), [`RESULTS.md`](results/final/p4/RESULTS.md) |
| Answer quality (token F1) | 0.368 static, 0.366 adaptive | same |
| Cost of the loop | about 56% more median latency | same |
| Generation run (job 51585) | Qwen3-8B on vLLM 0.11.0, one A40, 8 passages × 1,200 characters | [`results/final/p5`](results/final/p5/README.md) |

The 1,200-character budget is the primary result. A post-hoc run at 2,500 characters (job 51705) is reported next to it as a sensitivity analysis; the code default and the final live demo use 2,500. To reproduce the primary result, check out commit `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`, or run a later commit with `MAX_CHARS_PER_PASSAGE=1200`. The held-out results do not establish independently held-out downstream performance: the agent developer read 40 of the 200 questions during annotation, and the report states this limitation.

## Local setup

Use Python 3.11 as the starter environment. Run these commands inside the cloned `papergap-rag` directory:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Windows activation: `.venv\Scripts\activate`.

The dependency files are ranges, not a tested lockfile. Installation downloads libraries, not model weights or the dataset. The held-out run used Qwen3-8B with vLLM 0.11.0 on one NVIDIA A40 on the university cluster ([run record](results/final/p5/README.md)); vLLM and GPU-specific packages are installed separately there and are not in `requirements.txt`. Launch the UI with `python -m streamlit run src/ui/app.py`; see [UI setup and usage](src/ui/README.md).

The UI talks to the answer service (`src/generation/server.py`, served on the cluster GPU) through `P5ApiClient`; see the [demo architecture](docs/DEMO_OPTION_C.md) and the [P6 end-to-end guide](docs/P6/P6_REAL_ENV_E2E_GUIDE.md). The final demo uses 8 passages of at most 2,500 characters, top eight, with the reranker off.

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

Dense unit tests use deterministic fake encoders with real FAISS and do not download models. A real SentenceTransformer run is a separate check. See the [Week 1/2 verification record](docs/WEEKLY_TRACKER.md#p1-verification-evidence) for historical synthetic runs, the Week 3/4 workflow below for P1 real-corpus experiments, and the [P2 real-data handoff](docs/P2_WEEK2.md) for Hybrid/reranking evidence. The final retrieval metrics are in [`results/final/`](results/final/README.md). Keep real data, model weights, caches, indexes and raw run output in ignored local directories; only small synthetic fixtures and the reviewed outputs under `results/final/` belong in Git.

## P1 retrieval: Week 3 / Week 4

The real-data workflow and reproducible PowerShell commands are documented in
[P1 Week 3 / Week 4](docs/P1_WEEK3_WEEK4.md). It runs P3's pinned data preparation
in a separate worktree and validates its Passage JSONL and manifests before
using the existing P1 retrievers. The recorded development convention indexes
train plus validation paper text and queries **train only**; the split policy
remains `v0-proposed`.

`python -B -m scripts.run_p1_experiment --help` describes the experiment entry
point. It loads the saved Dense index, saves/reloads a reproducible BM25 JSON
snapshot, verifies both complete Passage mappings, and writes `results.jsonl`,
`queries.jsonl` and `run.json` to a new or empty output directory. `--limit`
limits queries only; the full corpus remains indexed. Zero-hit questions are
retained. The run records input hashes, model revision, code state, source
hashes and retrieval latency. BM25 loading rebuilds its in-memory term index;
Dense loading reuses the stored passage vectors without re-encoding them.
The `evaluate` subcommand audits saved rankings and adapts independently supplied
labels; see the [provisional evaluation contract](docs/P1_EVALUATION.md).

The original `retrieve(query, paper_id, top_k)` callback remains supported.
Both independent retrievers also accept keyword-only `section="Results"`
with exact matching before top-K selection. Callers can supply a rewritten
query directly. Merged P2 Hybrid retrieval forwards exact sections to both
callbacks, and the P4 graph accepts a caller-supplied section selector. P4 still
owns the per-paper selector and same-round unscoped fallback. The historical
P1 integration checks used fixed request bindings; they do not establish
dynamic section selection. See [section interfaces](docs/P2_AGENT_CACHE.md).

P1 saved-ranking scoring and P2 retrieval evaluation/pooling tools are
available. This workflow exports real retrieval candidates and latency; quality metrics
come from scoring those rankings against the accepted pooled relevance labels, and the
final comparison is in [`results/final/p1`](results/final/p1/README.md) and
[`p2`](results/final/p2/README.md). See the [P2 evaluation handoff](docs/P2_EVALUATION_HANDOFF.md)
and the linked P1 verification record for scope and limitations.

The Week 3/4 delivery branch includes main's merged P2 and P4 APIs.
`python -B -m scripts.run_p1_integration --help` describes the bounded integration
check using existing artifacts and fixed request sections. It does not establish
dynamic section selection or real critic quality. The [18 October integration](docs/P1_WEEK3_WEEK4.md#main-integration-after-p2-merge-18-october-2026)
records historical execution. The [28 October checkpoint](docs/WEEKLY_TRACKER.md#p1-question-usage-handoff-and-main-sync-28-october-2026)
records the question-use handoff; see the [29 October checkpoint](docs/WEEKLY_TRACKER.md#p1-main-sync-after-ui-and-generation-merge-29-october-2026)
for the current branch refresh and validation.

## P2 real-data Hybrid and reranking

`python -B -m scripts.demo_hybrid --help` is now available from main. The CLI
loads the supplied Passage JSONL and saved Dense index, checks their mapping,
and runs RRF; `--bge` enables optional BGE reranking. See [P2 commands, model
revisions and measured pilot](docs/P2_WEEK2.md) for inputs, offline cache controls
and `scripts.benchmark_p2`. Use dependencies appropriate to your platform;
the documented macOS ARM64 lock and repair procedure are platform-specific.

P1's 100-question handoff remains RRF-only with null reranker fields. P2's later
independent reranked export is recorded separately and does not change the P1
package's provenance or establish a retrieval-quality gain. See the [separate
artifact records](docs/P1_WEEK3_WEEK4.md#separate-p1-and-p2-artifacts).

## Repository layout

```text
docs/                 Plan, requirements, evaluation, team tracker, per-owner handoffs (docs/P6 for evaluation and UI)
configs/              Shared configuration; configs/p4_freeze.json is the held-out freeze record
src/data/             P3: data preparation
src/retrieval/        P1/P2: retrievers, fusion and reranking
src/agent/            P4: planning, critic, adaptive retrieval and the freeze protocol
src/generation/       P5: generation, citation validation and the answer service
src/evaluation/       P6 + experiment owners: metrics and logging
src/ui/               P6: Streamlit
scripts/              Reproducible command-line entry points
tests/                Module and integration tests
report/               LaTeX source of the final report (see report/README.md)
results/final/        Reviewed final outputs per owner, with checksums (committed)
results/              Everything else is local experiment output (ignored)
notebooks/, examples/ Evaluation walkthrough and annotation notebooks; example response schema
data/                 Local datasets (ignored except README)
```

## Assignment delivery

Deadline: **7 November 2026, 11:59 PM SGT**. Submit one PDF (exported as `24.pdf`) with team details, the full report, and accessible links to the code and to the data and results archives. The report source is in [`report/`](report/README.md); each owner's reviewed results are described in [`results/final/`](results/final/README.md). Raw run archives and the data zip are delivered outside Git.

**Rubric clarification confirmed by the team:** passage chunks count toward 10,000 documents, and query–passage pairs count toward 1,000 evaluation records. The knowledge base has 28,617 passages from 1,584 papers; the judged pool has 1,853 question–passage pairs with 89.854% agreement. See [requirements](docs/REQUIREMENTS.md) and the report's annotation section for the process and its limitations.
