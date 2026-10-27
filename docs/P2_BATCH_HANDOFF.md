# P2 batch retrieval handoff — 17 October 2026

Run from the repository root. Use the current P2 source, including
`scripts/batch_hybrid.py` and `src/retrieval/reranker.py`.

```bash
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
python -m scripts.batch_hybrid \
  --questions results/p1-handoff-input/questions.jsonl \
  --passages data/processed/passages.jsonl \
  --dense-index-dir indexes/p2-qasper-development-mps \
  --output-dir results/p1-handoff-reranked-new \
  --bge --candidate-k 20 --rrf-k 60 --top-k 5 \
  --cache-folder .cache/huggingface/hub --local-files-only
```

Replace input/index/cache paths with the paths on the receiving machine. The
question file is the unmodified `questions.jsonl` from P1's 17 October ZIP.
Output directories must be new. In PowerShell, set environment variables with
`$env:HF_HUB_OFFLINE='1'` (and likewise for the others), then run the Python
command on one line. Offline operation requires both pinned models cached first.
To allow initial model downloads, omit the offline environment settings and
`--local-files-only`.

The batch loads the corpus, index and models once. It retrieves up to 20
candidates per source, fuses the deduplicated union (up to 40 passages), scores
that entire union, and then returns five. Do not rerank only the previously
exported top five. Omit `--bge` to export the RRF-only baseline.

- Dense: `BAAI/bge-small-en-v1.5`, revision
  `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`.
- Reranker: `BAAI/bge-reranker-base`, revision
  `2cfc18c9415c912f9d8155881c133215df768a70`, CPU by default,
  batch size 8, maximum sequence length 512, raw relevance logits.
- `retrieval.jsonl`: one record per question in input order; original IDs,
  question and paper preserved; `retrieval_round=1`; nested `RetrievedPassage`.
- `latency.jsonl`: one elapsed time per question. First model use may be cold;
  these measurements are not a warmed latency benchmark.
- `run_manifest.json`: completion/failure status, parameters, input/output hashes,
  source hashes, dependency versions, platform and working-tree state.

Missing paper passages return `[]`. Model/index failures abort and mark the
manifest failed; partial files from a failed run must not be consumed. A completed
manifest is required. Duplicate IDs and malformed questions are rejected.

## Snapshot comparison

After normalizing Windows line endings, P1's schema, fusion and hybrid modules
match the local P2 modules. The only reranker differences are the added
`cache_folder` and `local_files_only` constructor options and their forwarding to
both Hugging Face loaders. Pair construction, tokenization, model scoring,
sorting, tie-breaking and output updates match. Use the newer reranker module
when passing these cache/offline options.

## Scope

The execution plan lists BGE reranking as mandatory. Preserve the fusion-only
baseline and include a separate reranked run for the planned system freeze.
This does not freeze the still-proposed shared schemas or split policy.
P1's 100 training questions are integration examples, intentionally including
three empty results; they are not the held-out evaluation sample or evidence of
retrieval quality improvement.

## Baseline comparison on this machine

The local corpus hash matches P1's recorded corpus exactly. The fresh local
RRF-only export reproduces all 100 question outputs' passage IDs and order,
source ranks, BM25 scores, RRF scores and passage metadata. Dense score differences
are at most `2.980232238769531e-07` across the returned passages, consistent with
floating-point variation between machines. The three empty results are preserved.

## Completed real-model run

Both RRF-only and BGE exports completed on the unchanged P1 question list:
100 records each, 97 nonempty records with five passages each, and three empty
records (485 passages per method). Independent validation checked schema, query
identity/order, paper scope, metadata and source provenance against P1's full
candidate trace, RRF scores, finite reranker logits, score ordering and hashes.
BGE changed the top-five selection/order for all 97 nonempty questions; this is
not a claim of improved retrieval quality. All 423 repository tests passed;
Ruff lint and formatting checks passed for the new Python files.

Local outputs are `results/p1-handoff-rrf-offline-20261017/` and
`results/p1-handoff-reranked-offline-20261017/`. The shareable bundle is
`results/p2-batch-reranking-handoff-20261017.zip`. It includes both exports,
question list, manifests, validation report, source snapshots and these
instructions, with no model weights or indexes. The executed batch snapshot and
the current linted version differ only in import ordering; the executed snapshot
matches the source hash recorded in the reranked run manifest.

## Artifact verification — 27 October 2026

The local ZIP `results/p2-batch-reranking-handoff-20261017.zip` exists (about
531 KiB); every entry listed in its checksum manifest passed SHA-256 verification.
ZIP SHA-256: `194bf9fa15a68ea7de64af945b495dba9e6988781974178793bd9c950fa7dae3`.
It contains 100 question records and separate `rrf/` and `bge/` outputs, with
485 returned passages and three empty questions per method. These are P1's
training integration questions, not the frozen held-out evaluation set.

P5 should consume `bge/retrieval.jsonl` for the reranked integration and preserve
the fusion-only Week-3 baseline separately. Do not overwrite `runs/week3/`.
The ZIP has now been uploaded and metadata-verified in the team Drive folder:
[download the handoff](https://drive.google.com/file/d/1XM84LDukvCmQaNXFOBFfAW_j_JkkpWV3/view).
Folder sharing determines teammate access; individual permissions were not changed. The bundle preserves the historical
executed source and manifests; do not relabel it as a run of newer code.
