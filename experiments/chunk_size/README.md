# Chunk size experiment

This `v0-proposed` runner compares word-based chunk sizes using the criteria in `criteria.md` and `criteria_zn-CN.md`. It reads verified `papers.jsonl` and `qa.jsonl` exports described in `data/README.md`. It only builds original `train/validation` paper corpora and samples their questions; original `test` questions are excluded before sampling.

## Run

From the repository root, use the existing Python environment with `requirements-dev.txt` installed:

```powershell
python -m scripts.evaluate_chunk_size run --run-id comparison_01
```

Choose a new `--run-id` for every comparison. Existing run directories are rejected. A run writes `manifest.json` last; a directory without that file is incomplete and must not be used as a completed result.

`config.json` defines `candidates` in words, `overlap_words`, `top_k`, `question_sample_count`, `readability_sample_count`, `question_seed`, and `readability_seed`. Defaults are $150/200/250$ words with $40$ words of overlap, top-$5$, $50$ questions, and $10$ source paragraphs. Seeds default to $42$ for questions and $43$ for readability. The runner passes each size and the fixed overlap to both `ChunkingConfig` and `PassageIdContext`. Candidate sizes must exceed overlap; counts must be positive and `top_k` must remain $5$ for the defined metrics. Smaller eligible pools use all available items and record the actual counts.

The local baseline uses `rank-bm25` with casefolded Unicode word tokens and a separate index per paper. Equal scores are ordered by passage ID. This is an experiment baseline pending integration with P1/P2; it does not require P5's generator. To use another retriever from Python, pass `retriever_factory` and `retriever_metadata` to `src.evaluation.run_chunk_size.run_comparison`. The factory receives the candidate corpus and returns a callable with `(query, paper_id, top_k) -> [(passage_id, score)]`. Return ranked unique IDs from the requested paper with finite scores. Metadata must identify the implementation, model/revision, tokenizer, scope and scoring parameters. Preserve the same retriever settings across all sizes.

## Review and summarize

Outputs stay local under `results/chunk_size/<run_id>/`. Each size has `evidence_review.md` with answers, source evidence, retrieved chunks, coverage, word counts and automatic decisions, plus `readability.md` with shared sampled source locations and full chunks. There is no separate retrieval detail file. The shared `summary.json` includes per-question metrics, ranked IDs/scores and retrieval timing; the manifest records input hashes, source/split policy, code state, dependencies, hardware, seeds and sample locations. Corpus hashes identify canonical JSON records including private provenance spans; no generated corpus is added to Git.

In `readability.md`, change each `pending` result to `pass` or `fail` and give failures a short reason. Each unique passage ID has exactly one result row, even if the chunk touches several sampled source paragraphs. Then run:

```powershell
python -m scripts.evaluate_chunk_size summarize --run-dir results/chunk_size/comparison_01
```

Readability pass rate remains `null` while any result is pending. Missing rows, unknown labels, unexpected IDs and duplicate rows are errors. Both evidence rates use all selected questions as their denominator; retrieved word count is the mean of each question's total, including repeated overlap.

Evidence mapping requires an exact normalized paragraph match within the question's paper. Newlines and surrounding whitespace follow the shared chunker; original paragraph character offsets are preserved. Multiple chunks may jointly cover one paragraph, and whitespace-only gaps are ignored. Ambiguous repeated paragraphs and `FLOAT SELECTED` evidence remain unresolved. An annotation is usable only when its nonempty evidence set is fully located; an empty or partially unresolved annotation cannot satisfy complete evidence. A question needs at least one usable annotation and a paper present in every compared corpus. Readability source samples use only those common corpora and are shared across sizes.

This command prepares comparison artifacts; choosing the final size still requires manual readability review and assessment of the evidence results. The baseline and output schema remain `v0-proposed` pending team review.
