# Chunk size experiment

This `v0-proposed` runner compares word-based chunk sizes using the criteria in `criteria.md` and `criteria_zn-CN.md`. It reads verified `papers.jsonl` and `qa.jsonl` exports described in `data/README.md`. It only builds original `train/validation` paper corpora and samples their questions; original `test` questions are excluded before sampling.

## Run

From the repository root, use the existing Python environment with `requirements-dev.txt` installed:

```powershell
python -m scripts.evaluate_chunk_size run --run-id comparison_01
```

Choose a new `--run-id` for every comparison. Existing run directories are rejected. A run writes `manifest.json` last; a directory without that file is incomplete and must not be used as a completed result.

`config.json` defines `candidates` in words, `overlap_words`, `top_k`, `question_sample_count`, `question_sampling_method`, `n_paper`, `n_paragraph`, and `seed`. Round 1 compares $100/200/400$ words with $40$ words of overlap, top-$5$, $50$ questions, and $5$ papers with $2$ paragraphs each. Previous $150/200/250$ experiments are void by the experiment owner's decision; retain their files for provenance only and exclude them from selection. Question sampling uses `simple_random_without_replacement` (the only supported method and the default when omitted), applied to the eligible question pool after filtering. All sampling uses seed $42$; question and readability samplers initialize separate generators with that value. The runner passes each size and the fixed overlap to both `ChunkingConfig` and `PassageIdContext`. Candidate sizes must exceed overlap; counts must be positive and `top_k` must remain $5$ for the defined metrics. Smaller eligible pools use all available items and record the actual counts.

Readability sampling selects papers without replacement, divides each paper's eligible paragraphs in source order into contiguous intervals, and randomly selects one paragraph per interval; short papers contribute all paragraphs. See `criteria.md` for the complete scheme. Inspect batch paragraph lengths in `manifest.json` under `readability_sampling`, and estimate actual work from `readability_review_chunk_counts` and `readability_review_chunk_count_total`. There is no per-paper length quota or automatic rebalancing. Old custom configurations must replace `readability_sample_count`, `question_seed`, and `readability_seed` with the new keys; historical completed runs still support `summarize`.

The default `retrieval` configuration is `{"mode": "bm25"}`; older configurations without this block use the same defaults. The runner now uses P1/P2 code from fixed upstream commit `5ccfb070a00f71dd2f95f69afb31868c296f35c4`. It builds independent indexes for each chunk size and each paper. Only the eight validated public passage fields enter retrieval; private source spans stay in evaluation. No P4 Agent, P5 generator or P6 UI is needed. The four modes have offline wiring tests; real-model quality, device availability and tokenizer truncation remain unverified.

## Round 4 frozen validation sample

Current `config.json` compares $325/365/375$ words on the original $50$ questions plus $200$ unused eligible questions. `validation.reference_run` identifies Round 3; `validation.additional_question_count` requests new questions, and `validation.primary_word_budget=1000` predeclares the main budget. Complete evidence rate on new questions is primary; evidence hit and other budgets remain reported. The primary budget is an experimental choice; the deployment budget remains unconfirmed. `question_sample_count` must equal reference question count plus requested new count. Fewer available new questions are used without relaxing eligibility. This mode requires BM25; omitting `validation` preserves the earlier sampling workflow.

Freeze before retrieval, then reuse the exact plan (choose a new plan filename if it already exists):

```powershell
python -m scripts.evaluate_chunk_size run --run-id round4_bm25_20261028_01 --prepare-plan experiments/chunk_size/round4_question_plan.json
python -m scripts.evaluate_chunk_size run --run-id round4_bm25_20261028_01 --question-plan experiments/chunk_size/round4_question_plan.json
```

Preparation builds candidate corpora to verify common-paper eligibility but does no retrieval and creates no run directory. A reused plan must exactly match current configuration, inputs, reference hashes and seeded selection. A normal validation run without these flags freezes its plan before retrieval. Every run saves `question_plan.json` and its hash, group membership, paper/source counts and paper overlap; it checks regression question records, corpus hashes, rankings and metrics against the reference before writing the completion manifest. A failed regression leaves an incomplete directory. The reference files remain unchanged.

`summary.json.validation` contains separate `regression`, `new` and `combined` summaries and paired candidate gains/losses with exact question IDs at top-$5$ and every word budget. `summary.html` displays all groups, while `report.md` presents budget metrics and paired new-question counts. `regenerate` rebuilds these views from structured inputs and the frozen plan, preserving readability labels. New questions may share papers with old ones and are no longer independent final-test questions once used for selection.

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

Every successful `run`, `regenerate`, and `summarize` writes `summary.html` beside `summary.json`. Open it in a browser for an offline comparison: rows are chunk sizes in numeric order, with a top-$5$/readability table and one table per word budget. Rates remain on the $0$–$1$ scale with four decimal places; blue bold cells mark the highest rates, including exact ties. Hover over aggregate values to see numerators and denominators. Pending manual reviews show `Pending`; unavailable metrics show `N/A`. Word counts, corpus counts, and diagnostic index timings are descriptive and are not ranked. The page needs no external libraries or network connection.

Generate or refresh only the HTML for an existing run without changing JSON, readability labels, or retrieval outputs:

```powershell
python -m scripts.evaluate_chunk_size render --run-dir results/chunk_size/round1_bm25_20261028_02
```

Share outputs in Git under `results/chunk_size/<run_id>/`. Each size has `evidence_review.md` with answers, source evidence, retrieved chunks, coverage, word counts and automatic decisions, plus `readability.md` with shared sampled source locations and full chunks. New BM25 runs also save shared `questions.jsonl` and per-size `ranked_chunks.jsonl`; the independent replay contract is described below. Other retrieval modes retain their existing top-$5$ workflow. The shared `summary.json` includes per-question metrics, ranked IDs/scores and retrieval timing; the manifest records input hashes, source/split policy, code state, dependencies, hardware, seeds and sample locations. Corpus hashes identify canonical JSON records including private provenance spans; no generated corpus is added to Git.

BM25 additionally evaluates `word_budgets` in the experiment JSON, defaulting to $500/1000/2000$ words when omitted; values must be unique positive integers. `manifest.json` includes `structured_inputs` with schema `chunk-size-inputs-v0-proposed`, JSONL file SHA-256 hashes, word/truncation rules, and per-size/per-question `ranking_states`. The runner retrieves the paper's full BM25 ranking, then saves the shortest prefix with at least $5$ chunks and enough full-chunk words for the largest budget, or all available chunks. Each state records `saved_count`, `available_count`, `saved_word_count`, `ranking_complete`, and `retention_satisfied`. Full chunks carry exact `source_spans`, including `source_text` for independent validation; CRLF normalization uses separate segments where character lengths differ. The shared question file retains full evidence and separate answer groups.

Both top-$5$ and budgeted evidence decisions are calculated from validated JSONL. Budgeted reading follows the same ranking, counts repeated overlap, and truncates only the last included chunk after the last retained word. Coverage is recomputed from retained source spans. `summary.json` stores per-question `budgets` and per-size `budgets` aggregates, including numerators, denominators, mean actual words, and `corpus_exhausted_count`. Exhaustion requires confirmed complete retrieval and unused allowance. Reports show full saved chunks, budget tables, retained chunk character ranges, source evidence spans, covered annotations, and missing evidence.

Recalculate the derived evidence reports from a completed structured run without raw data, models, or BM25:

```powershell
python -m scripts.evaluate_chunk_size regenerate --run-dir results/chunk_size/comparison_01
python -m scripts.evaluate_chunk_size regenerate --run-dir results/chunk_size/comparison_01 --word-budgets 500 1000
```

`regenerate` replaces `summary.json` and `evidence_review.md` after all structured inputs and requested budgets validate; JSONL and the manifest stay unchanged. `summary.json.word_budgets` identifies the budgets used for that rendering; manifest configuration describes the original retrieval/retention requirements. Existing readability metrics and retrieval/corpus timing metadata are preserved. `readability.md` remains independently maintained; use `summarize` to import edited labels. A missing or insufficient ranking raises an error before report writes. When larger budgets need more ranks, retrieve into a new run ID with the same verified inputs/settings. Historical runs lacking structured inputs require reconstruction and verification; `regenerate` does not infer mappings from their Markdown or migrate them automatically. No historical or void experiment files are overwritten by `run`.

In `readability.md`, change each `pending` result to `pass` or `fail` and give failures a short reason. Each unique passage ID has exactly one result row, even if the chunk touches several sampled source paragraphs. Then run:

```powershell
python -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/comparison_01
```

Readability pass rate remains `null` while any result is pending. Missing rows, unknown labels, unexpected IDs and duplicate rows are errors. Both evidence rates use all selected questions as their denominator; retrieved word count is the mean of each question's total, including repeated overlap.

Evidence mapping requires an exact normalized paragraph match within the question's paper. Newlines and surrounding whitespace follow the shared chunker; original paragraph character offsets are preserved. Multiple chunks may jointly cover one paragraph, and whitespace-only gaps are ignored. Ambiguous repeated paragraphs and `FLOAT SELECTED` evidence remain unresolved. Before sampling, require at least one answer annotation and nonempty, fully and uniquely located text evidence for every annotation. If any annotation has empty, missing or unresolved evidence, exclude the entire question from both evidence metrics and retrieved word counts; its located paragraphs cannot contribute a hit. The question's paper must also be present in every compared corpus. The manifest's `filtering_counts.invalid_answer_evidence` counts questions excluded by this evidence rule, replacing the former `no_usable_text_evidence` counter. Complete evidence still requires covering all evidence from at least one annotation. Readability source samples use only those common corpora and are shared across sizes.

Historical completed runs can still be summarized, but summarizing does not reapply question filtering. Rerun with a new run ID to obtain results under the all-annotations rule; do not compare these results directly with runs using the former eligibility rule.

This command prepares comparison artifacts; choosing the final size still requires manual readability review and assessment of the evidence results. The baseline and output schema remain `v0-proposed` pending team review.
