# Evaluation protocol — Week 1 proposal

## Annotation and held-out data

`Instruction.pdf`, page $4$, Question $4$, requires at least $1{,}000$ manually labeled records and at least $80\%$ inter-annotator agreement; two annotators are allowed. The assignment does not explicitly prescribe question-level or paper-level isolation. The team's query–passage record interpretation and the user's Week 4 design use $200$ questions with $5$ distinct passages each, giving $1{,}000$ unique pairs.

The all-splits gold mapping is a reference union, not an ordinary-test designation. Coverage alone neither freezes nor invalidates held-out status. The current pool uses question-level isolation, allows shared papers and samples from all official splits. Exclude the saved $250$ chunk-selection questions and every additional question found in local experiment records, including invalidated runs. The audit covers persisted local records; unrecorded external use cannot be established from this repository.

Use two independent blind judgments per pair. Label $1$ when the passage helps answer the question, including useful partial evidence; topic overlap alone is insufficient. Label $0$ otherwise. Hide gold evidence, retrieval method, score, rank, internal identifiers and the other person's labels. Export two independent slots, each with $10$ English Markdown batches of $20$ questions / $100$ records. Assign slots to distinct people for every record before distribution. The preparation script does not assign team identities or collect labels.

Calculate raw agreement before adjudication, preserve both independent judgments and separately record the final adjudicated label. Report agreement by annotator pair and Cohen's kappa for each fixed pair with sample sizes. If agreement is below $80\%$, report it honestly and document any fresh independent labeling; never overwrite disagreements to inflate agreement. Assignment, collection and adjudication are Week 4 Step $2.8$, outside the completed pool-generation scope.

## Retrieval metrics

P6 defines K values, relevance rules, no-relevant-document handling and macro averaging before runs. P3 maps QASPER evidence to chunk IDs and records mapping failures. Deduplicate overlapping evidence for evidence-level measures where appropriate.

A pool of five judged passages per question is incomplete relevance coverage. Report judged coverage at K. Label pool-based scores explicitly, and do not present pool recall as exhaustive full-paper recall. Evaluate ranking within the judged pool separately from full retrieval; where available, also report QASPER evidence-based metrics with mapping limitations. Unjudged results are unknown, not automatically confirmed negatives. Any additional judging must follow a frozen, system-neutral protocol.

## Minimal experiment ladder

| ID | Configuration | Evaluation |
| --- | --- | --- |
| R1 | BM25 | Rank-aware retrieval metrics and latency |
| R2 | Dense | Same |
| R3 | Hybrid RRF | Same |
| R4 | Hybrid RRF + reranker | Same |
| G0 | Generator without retrieval | QA baseline; evidence faithfulness is not applicable |
| G1 | BM25 RAG | QA, RAGAS and latency |
| G2 | Dense RAG | Same |
| G3 | Hybrid RAG | Same |
| G4 | Static hybrid + reranker RAG | Same; primary static baseline |
| G5 | Adaptive hybrid + reranker, single critic | Same plus retries, recovery and abstention |
| Optional | Gold-evidence reference, dual critic, NLI, citation-validator ablation | Only after required runs complete |

Use the same frozen generator, answer prompt, decoding settings, question set and context budget for static/adaptive comparisons; report additional retrieval/model calls and token cost. Retain citation validation in both G4 and G5. A separate validator ablation changes only the validator. The original E/F and G/H comparisons otherwise overlap or mix factors.

Maximum two retries means **three retrieval rounds total**. Report p50/p95 latency with hardware, caching and warm-up policy. Bootstrap uncertainty over questions (or papers), not over correlated query–passage records as if independent.

## QA, citations and RAGAS

Define normalization, multiple reference-answer handling, answer-type scoring and abstention behavior before final evaluation. Report answerable/unanswerable subsets and mapping exclusions. RAGAS judge scores complement manual inspection; record evaluator version, judge model, prompt, parameters, embedding model and cost. Establish refusal handling and missing-score policy in advance.

Citation-ID validation establishes that a cited passage was supplied to the generator. It does **not** establish entailment or that numbers are supported. Evaluate citation correctness/grounding separately using manual checks and the chosen faithfulness metric. Do not claim the validator prevents all unsupported factual statements.

Tune only on development/validation data. Freeze all prompts, retrieval settings and optional variants before evaluating held-out labels. Log genuine post-freeze bug fixes and rerun affected comparisons consistently.

## Held-out freeze sequence

Run `python -m scripts.build_annotation_pool prepare`, then `pilot`, `freeze`, and `export`. Commands must run from the repository root. The default paths and complete field tables are in `data/README.md`.

Preparation extracts the persisted fourth-round $250$ questions without resampling. The pilot uses only the first $5$ of these development questions with the fixed $365/40$ all-paper corpus, paper-scoped BM25 and top-$5$ retrieval. Before sampling, validate the completed pilot and input/source hashes. Eligibility uses only IDs, prior-use records, source split and per-paper passage counts; require at least $5$ retrievable passages. Do not preview candidate queries, answers or evidence.

The predeclared seed is $20261028$: sort eligible question IDs, call Python `Random(seed).sample` without replacement for $200$ IDs and preserve draw order. Persist `qa_for_held_out.jsonl` before retrieval; export uses that file without resampling. Save input hashes, exclusions, eligible/final IDs, retrieval settings, HEAD, dirty status and source hashes. Freeze is specific to this annotation-pool configuration; other final system variants still require their own settings freeze before evaluation.

Held-out questions, answers, evidence, labels and results must never drive tuning, development or prompt design. The corpus contains paper content only. Retrieval sees only the query and paper scope; gold references are associated afterward in `verification.jsonl`. Distribute only the appropriate Markdown batch, keeping verification files private. An unjudged passage remains unknown, not automatically irrelevant. Genuine post-freeze bugs require a recorded cause and consistent reruns of affected configurations, never a result-driven targeted improvement.

## Unified QA export and access boundary

`qa.jsonl` and the gold mapping physically cover all official splits. Mechanical copying, hashing, schema checks and ID-only eligibility checks do not authorize content inspection for tuning. The current pool is determined by saved question IDs and actual usage, not by official split names. The legacy `src/data/split_policy.py` guard remains available for historical split-based development runners; do not reinterpret those historical runs under the new pool policy. Keep all raw data, generated question lists, pair records and annotation files outside Git.
