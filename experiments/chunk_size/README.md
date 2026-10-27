# Chunk size experiment

This `v0-proposed` runner compares word-based chunk sizes using the criteria in `criteria.md` and `criteria_zn-CN.md`. It reads verified `papers.jsonl` and `qa.jsonl` exports described in `data/README.md`. It only builds original `train/validation` paper corpora and samples their questions; original `test` questions are excluded before sampling.

## Run

From the repository root, use the existing Python environment with `requirements-dev.txt` installed:

```powershell
python -m scripts.evaluate_chunk_size run --run-id comparison_01
```

Choose a new `--run-id` for every comparison. Existing run directories are rejected. A run writes `manifest.json` last; a directory without that file is incomplete and must not be used as a completed result.

`config.json` defines `candidates` in words, `overlap_words`, `top_k`, `question_sample_count`, `question_sampling_method`, `n_paper`, `n_paragraph`, and `seed`. Defaults are $150/200/250$ words with $40$ words of overlap, top-$5$, $50$ questions, and $5$ papers with $2$ paragraphs each. Question sampling uses `simple_random_without_replacement` (the only supported method and the default when omitted), applied to the eligible question pool after filtering. All sampling uses seed $42$; question and readability samplers initialize separate generators with that value. The runner passes each size and the fixed overlap to both `ChunkingConfig` and `PassageIdContext`. Candidate sizes must exceed overlap; counts must be positive and `top_k` must remain $5$ for the defined metrics. Smaller eligible pools use all available items and record the actual counts.

Readability sampling selects papers without replacement, divides each paper's eligible paragraphs in source order into contiguous intervals, and randomly selects one paragraph per interval; short papers contribute all paragraphs. See `criteria.md` for the complete scheme. Inspect batch paragraph lengths in `manifest.json` under `readability_sampling`, and estimate actual work from `readability_review_chunk_counts` and `readability_review_chunk_count_total`. There is no per-paper length quota or automatic rebalancing. Old custom configurations must replace `readability_sample_count`, `question_seed`, and `readability_seed` with the new keys; historical completed runs still support `summarize`.

The default `retrieval` configuration is `{"mode": "bm25"}`; older configurations without this block use the same defaults. The runner now uses P1/P2 code from fixed upstream commit `5ccfb070a00f71dd2f95f69afb31868c296f35c4`. It builds independent indexes for each chunk size and each paper. Only the eight validated public passage fields enter retrieval; private source spans stay in evaluation. No P4 Agent, P5 generator or P6 UI is needed. The four modes have offline wiring tests; real-model quality, device availability and tokenizer truncation remain unverified.

## Retrieval settings

BM25 is selected for this experiment. A beginner's explanation of its inputs, outputs and complete workflow is available in `BM25.en.md` (English) and `BM25.md` (Chinese). Keep the selected mode and all its parameters fixed across chunk sizes; final parameter confirmation remains in `weekly-work/week-3/EXPERIMENT_GAPS.md`. Comparing different modes does not isolate chunk size effects. Select another configuration file with `--config`; `configs/default.yaml` is not read by this runner.

| `retrieval.mode` | Active components | Returned score |
| --- | --- | --- |
| `bm25` | P1 `BM25Retriever`, no model weights | Raw BM25 |
| `dense` | P1 BGE embedding and FAISS | Cosine similarity |
| `hybrid` | BM25 + dense, P2 RRF | RRF |
| `hybrid_rerank` | BM25 + dense, RRF, BGE reranker | Raw logit |

BM25 uses `rank-bm25`, casefolded Unicode word tokens, `k1=1.5`, `b=0.75` and `epsilon=0.25`. Equal scores use passage ID ascending. Dense uses `BAAI/bge-small-en-v1.5`, L2 normalization and cosine via `IndexFlatIP`; the query alone receives `Represent this sentence for searching relevant passages: ` as its prefix. Dense's single-text limit is $512$ tokens. Reranking uses `BAAI/bge-reranker-base` and pads/truncates each question–passage pair to `max_length`; scores are raw logits, including zero and negative values. Reranker ties use RRF descending, then passage ID ascending. Reports and word counts retain full chunk text even when a model truncates its input.

The following optional configuration shows all retrieval defaults except `mode`, whose default is `bm25`:

```json
{
  "mode": "hybrid_rerank",
  "candidate_k": 20,
  "rrf_k": 60,
  "dense": {
    "revision": "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a",
    "device": "cpu",
    "batch_size": 32,
    "cache_folder": ".cache/huggingface",
    "local_files_only": true
  },
  "reranker": {
    "revision": "2cfc18c9415c912f9d8155881c133215df768a70",
    "device": "cpu",
    "batch_size": 8,
    "max_length": 512,
    "cache_folder": ".cache/huggingface",
    "local_files_only": true
  }
}
```

Put this object under the `retrieval` key alongside the existing chunk settings. Defaults merge within each nested block. Unknown keys, `null` blocks and invalid types are rejected even in unused sections. Candidate counts, RRF constants and batch sizes must be positive integers; hybrid `candidate_k` must be at least `top_k`. Revisions must be lowercase $40$-character SHAs; reranker `max_length` must be an integer from $1$ to $512$. Device and cache path must be nonempty strings; relative cache paths resolve from the project root and the manifest stores their absolute paths. Model names and dense query/length rules are fixed by the imported API.

Each hybrid source supplies up to `candidate_k` results, then RRF deduplicates IDs. `hybrid_rerank` scores the entire fused union before returning top-$5$: with $20$ candidates per source, this can score up to $40$ passages. No persistent score cache or cross-run index reuse is used. Each candidate's retriever is released before building the next index. BM25 does not import FAISS, SentenceTransformers, Torch or Transformers; `hybrid` never creates a BGE scorer, and `summarize` loads no retrieval model.

Install `requirements-dev.txt` in the project environment, including `sentencepiece` for BGE tokenization. Model loading is offline by default. Before a real dense or reranker run, prepare the exact configured checkpoint and tokenizer in `cache_folder` as a separate step, using the model names and revisions above. An explicitly online preparation run may set the relevant `local_files_only` to `false`; the normalized configuration and manifest record that choice. Never substitute a different checkpoint or silently fall back to BM25. Missing dependencies, cached weights or unavailable devices produce an error; a failed output directory has no completion `manifest.json` and cannot be reused under the same run ID. Do not interpret a successful BM25 run as verification of the other modes. Real-model smoke checks must inspect representative long chunks/pairs with the corresponding tokenizer and record observed truncation before a formal comparison.

To use another retriever from Python, pass both `retriever_factory` and `retriever_metadata` to `src.evaluation.run_chunk_size.run_comparison`. The factory receives the full candidate corpus and returns `(query, paper_id, top_k) -> [(passage_id, score)]`. Return ranked unique IDs from the requested paper with finite scores. Metadata must identify the actual implementation, model/revision, tokenizer, scope and scoring parameters; a test double must declare its own identity. Custom metadata is recorded with `selection_source=custom_factory`; metadata without a custom factory is rejected. `local_bm25` remains a compatibility wrapper delegating to P1.

The manifest records normalized settings, fixed source commit, active package versions, score meaning, model/tokenizer revisions, device, batch sizes, length limits and offline policy. Disabled models are marked disabled. `index_seconds` includes each factory's construction, model initialization and passage encoding. Per-question `retrieval_seconds` includes full retrieval and the first BGE scorer's lazy loading. There is no hidden warm-up; report rendering is excluded. These single-run timings are diagnostic and do not establish a performance comparison.

## Review and summarize

Outputs stay local under `results/chunk_size/<run_id>/`. Each size has `evidence_review.md` with answers, source evidence, retrieved chunks, coverage, word counts and automatic decisions, plus `readability.md` with shared sampled source locations and full chunks. There is no separate retrieval detail file. The shared `summary.json` includes per-question metrics, ranked IDs/scores and retrieval timing; the manifest records input hashes, source/split policy, code state, dependencies, hardware, seeds and sample locations. Corpus hashes identify canonical JSON records including private provenance spans; no generated corpus is added to Git.

In `readability.md`, change each `pending` result to `pass` or `fail` and give failures a short reason. Each unique passage ID has exactly one result row, even if the chunk touches several sampled source paragraphs. Then run:

```powershell
python -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/comparison_01
```

Readability pass rate remains `null` while any result is pending. Missing rows, unknown labels, unexpected IDs and duplicate rows are errors. Both evidence rates use all selected questions as their denominator; retrieved word count is the mean of each question's total, including repeated overlap.

Evidence mapping requires an exact normalized paragraph match within the question's paper. Newlines and surrounding whitespace follow the shared chunker; original paragraph character offsets are preserved. Multiple chunks may jointly cover one paragraph, and whitespace-only gaps are ignored. Ambiguous repeated paragraphs and `FLOAT SELECTED` evidence remain unresolved. Before sampling, require at least one answer annotation and nonempty, fully and uniquely located text evidence for every annotation. If any annotation has empty, missing or unresolved evidence, exclude the entire question from both evidence metrics and retrieved word counts; its located paragraphs cannot contribute a hit. The question's paper must also be present in every compared corpus. The manifest's `filtering_counts.invalid_answer_evidence` counts questions excluded by this evidence rule, replacing the former `no_usable_text_evidence` counter. Complete evidence still requires covering all evidence from at least one annotation. Readability source samples use only those common corpora and are shared across sizes.

Historical completed runs can still be summarized, but summarizing does not reapply question filtering. Rerun with a new run ID to obtain results under the all-annotations rule; do not compare these results directly with runs using the former eligibility rule.

This command prepares comparison artifacts; choosing the final size still requires manual readability review and assessment of the evidence results. The baseline and output schema remain `v0-proposed` pending team review.
