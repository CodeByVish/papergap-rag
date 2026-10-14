# P2: real retriever integration and development pilot

Owner: Vishakha. Branch: `p2/week2-hybrid-integration`.
P1 PR #4 and P3 PR #2 are merged into main. Their passage and split contracts
remain provisional; this integration does not freeze the evaluation policy.

## What P2 does

P1 provides BM25 keyword retrieval and BGE dense retrieval. P2 combines their
rankings with Reciprocal Rank Fusion (RRF), deduplicating by passage ID. An
optional BGE cross-encoder scores every unique candidate using the question and
passage together, then selects final top-K. The result retains original source
ranks/scores, RRF scores and raw reranker logits for P4's agent/provenance trace.

Week 1 already implemented RRF, duplicate handling, reranking and callback wiring
with synthetic fixtures. This work adds real P1 index loading, corpus consistency
checks, a reproducible development comparison and cache/offline controls for BGE.

## Environment

Install `requirements-p2.txt` for the P2/P1/P3 integration tools. The tested
Python 3.11 macOS ARM64 snapshot is `requirements-p2-macos-arm64.lock.txt`.
It is platform-specific; it is not a GPU or full-application dependency lock.
Model weights, data, indexes and generated results stay ignored.

On this machine FAISS 1.15.1 and PyTorch 2.14.0 each bundled an OpenMP runtime.
The repair links FAISS to PyTorch's existing runtime and preserves the original:

```bash
python -m scripts.repair_macos_openmp          # inspect only
python -m scripts.repair_macos_openmp --apply  # opt-in, this environment only
python -m pytest -q
```

Use this only for the observed duplicate-libomp problem on macOS ARM64. It changes
an installed library link, not source ranking behavior. `--restore` undoes the
repair; reinstalling FAISS may also replace the link. No duplicate-runtime bypass
flag is used. Full tests and real-model runs must validate the repaired environment.
The repair is not implied by the dependency snapshot alone.

## Reproduce the corpus and index

Run from the repository root with the project Python environment. These commands
reject existing generated output paths; reuse verified existing artifacts or pick
new names for another build.

```bash
python -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
OMP_NUM_THREADS=4 VECLIB_MAXIMUM_THREADS=4 python -m scripts.build_indexes --passages data/processed/passages.jsonl --output-dir indexes/p2-qasper-development --cache-folder .cache/huggingface/hub
```

The verified development corpus has 32,073 passages, 1,168 indexed papers and
4,262,446 source words. SHA-256:
`abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`.
It contains train/validation paper text. The pilot reads only train questions;
held-out questions, answers and evidence are not used for selection or tuning.

## Run one hybrid query

```bash
OMP_NUM_THREADS=4 python -m scripts.demo_hybrid --passages data/processed/passages.jsonl --dense-index-dir indexes/p2-qasper-development --paper-id 1601.00901 --query 'How did they induce the CFG?' --candidate-k 20 --top-k 5 --cache-folder .cache/huggingface/hub --local-files-only --output results/p2-hybrid.json
```

Add `--bge` for reranking. Dense and reranker model revisions have pinned commit
SHA defaults; override using `--revision` or `--reranker-revision` explicitly.
`--local-files-only` applies to both models. Remove it for a first model download.
The command rejects mismatching JSONL/index passage mappings. Its timing is one
complete retrieval call after warm-up, excluding model loading/index construction.

## Paired development comparison

```bash
OMP_NUM_THREADS=4 VECLIB_MAXIMUM_THREADS=4 python -m scripts.benchmark_p2 --passages data/processed/passages.jsonl --qa data/processed/qa.jsonl --dense-index-dir indexes/p2-qasper-development --questions 6 --min-passages 20 --candidate-ks 10 20 --top-k 5 --local-files-only --output results/p2-development-pilot.json
```

Questions are selected deterministically from train: sort paper ID then question
ID, take one question per paper with at least 20 passages. Only question ID,
paper ID and question text reach retrieval; answer/evidence annotations are never
passed. Both methods use identical questions, corpus, candidate counts and top-K.
One complete call per method/question/configuration is measured after one warm-up
per method/configuration. Method order alternates. BGE tokenization/scoring is
included; loading and indexing are excluded. The saved JSON contains results,
source provenance, candidate counts, code/data hashes, model revisions, dependency
versions, platform, thread count and per-query timings. Existing outputs are refused.

Report ranking changes and descriptive p50/p95 for this small pilot. No relevance
labels are used, so it does not establish precision, recall or a reranking quality
gain. Candidate defaults remain untuned. Formal quality evaluation requires P3's
evidence mapping and P6's agreed metric/annotation protocol.

## Verification

419 tests pass in one process after the environment repair. Ruff checks all
source, scripts and tests. The pinned real BGE synthetic smoke run and the full
real-corpus comparison are recorded separately from unit-test evidence.

Pilot results will be recorded after the full index finishes building.
