# P2 demo loader confirmation — 2 November 2026

Verified locally against shared source `c232edb` using the supplied P1 archive.

## Configuration

Use hybrid RRF + BGE, not a silent dense-only/BM25-only substitution: 20 candidates
per source, RRF constant 60, rerank the full deduplicated union (up to 40), final
K=5. Reranker: `BAAI/bge-reranker-base`, immutable revision
`2cfc18c9415c912f9d8155881c133215df768a70`; CPU, batch 8, maximum 512 tokens.
The embedder is `BAAI/bge-small-en-v1.5`, revision
`5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, also CPU.

## Artifact verification and real local run

- Archive SHA-256: `8773b7b0f84d95a53bdba26ec20b577faf05efb19375cbf9c03cfec7c77a2cda`.
- All internal SHA256SUMS entries and all 1,169 entries in the separately supplied
  dense checksum list verified. Corpus-to-index passage mapping also passed.
- Current `DenseRetriever.load` loaded all per-paper indexes offline. An actual
  query used the embedding snapshot inside the package (not a mock encoder).
- `BM25Retriever(passages)` rebuilt the term index in about 2.31 seconds on the
  local machine. Use this existing startup path; no snapshot-loader port is needed.
- Hybrid+BGE returned five finite reranker-scored passages for the package's
  development example (paper `1909.00694`). First call: 12.54 seconds, including
  lazy model loading; second call: 3.94 seconds, no persistent score cache.
  These are two macOS CPU calls with four threads, not cluster benchmarks.
  Cross-encoder reranking is not generally a millisecond operation here.
- The package contains the embedding model, NOT the reranker. The real check
  used our separately cached pinned reranker. P5 must provision both snapshots.

The ZIP is the historical **200/40**, 32,073-passage development corpus with hash
`abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`.
This proves loader compatibility, not readiness for final **365/40** evaluation.
Never combine this index with new passage IDs. Rebuild matching indexes for the
agreed 365/40 corpus and record its manifest/hash before final evaluation.

## Factory and paths

Reuse P4's existing factory `scripts.demo_agent_factory:factory` (takes P5's
pipeline, returns the full agent record callable). It delegates retrieval to
`scripts.run_agent_experiment.build_retriever(args, passages)`, which returns
`HybridRetriever.retrieve`, with optional section adapters. This is the shared
retrieval constructor; a second `src/retrieval/demo.py` implementation is unnecessary.
It does NOT use `IndexedRetriever` or the Lucene/single-FAISS layout.

Set these in P5's environment using paths on P5's account:

```bash
export PAPERGAP_CORPUS="$P5_ROOT/data/corpus/passages.jsonl"
export PAPERGAP_DENSE_INDEX="$P5_ROOT/data/indexes/dense-bge-small"
export HF_HOME="$P5_ROOT/hf"
export DEMO_AGENT_BGE=1
export DEMO_AGENT_CANDIDATE_K=20
export DEMO_AGENT_DEVICE=cpu
export DEMO_AGENT_OFFLINE=1
```

Set the server's final top-K to 5. `PAPERGAP_BM25_INDEX` is intentionally unused;
BM25 is rebuilt once from the same corpus. Do not move the two metadata files
into one directory.

`cache_folder` means the directory containing `models--BAAI--...`, not necessarily
HF_HOME itself. The existing factory chooses `$HF_HOME/hub` if present, otherwise
`$HF_HOME`; `DEMO_AGENT_CACHE_FOLDER` overrides that choice. Place both pinned
model snapshots under the same resolved cache directory. The package's `hf-cache`
is itself such a cache directory. Loading indexes alone does not test model
availability; perform a warm-up query before declaring the service ready.

## Remaining P5 server bridge

At audited main `c232edb`, the P4 factory exists, but `src/generation/server.py`
and `80_demo_server.sbatch` still lack the `record_fn`/`--record-fn` wiring described
in `P4_AGENT_DEMO_HOOK_20261030.md`. P5 must connect that hook before claiming the
live free-form endpoint executes P4's full agent. Passing the pipeline-taking
factory into the server's plain retriever factory is not interchangeable.
No real cluster/Qwen/server test was performed by this P2 check. P5 owns the
account/job and can run that rehearsal; P2 does not require account access.
