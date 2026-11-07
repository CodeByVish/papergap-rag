# Evaluation protocol

*Written in Week 1 as the proposed protocol; updated on 7 November 2026 with what was done. The original text is kept as the protocol the team worked towards; where the delivered work differs, the difference is stated below and in the report.*

## Status (7 November 2026)

- **Annotation (delivered, with departures).** The proposal was 100 questions and 1,000 pairs, three fixed annotator pairs and a third-member adjudicator. Delivered: 200 questions from 174 papers, 1,853 pooled query–passage pairs (top five from BM25, Dense, Hybrid RRF and Hybrid RRF + BGE rerank), two annotators, 89.854% agreement on the submitted labels, and 188 disagreements. One reviewer resolved all 188, including 73 pairs they had annotated, with AI suggestions possibly visible and 176 resolutions lacking written reasons. This is **not** the independent third-person adjudication proposed below. Details and Cohen's kappa are in the report (Q4.3).
- **Retrieval metrics (delivered).** Pool-based Precision, pool recall, MRR and nDCG at K = 5 (P2 also K = 1 and 3), macro-averaged over questions, with the judged-pool limits stated; paired bootstrap resamples papers (1,000 resamples, seed 42). The agent is scored on mapped-evidence recall (P3's evidence-to-passage mapping; question-level bootstrap, 2,000 resamples, seed 0).
- **Experiments (partly run).** See the status column of the ladder below.
- **Held-out freeze (done).** The configuration was fixed on 6 November 2026 at commit `ad02d5103e28dbca2230555dd90e36c5cdc70f4f` and recorded in `configs/p4_freeze.json` and `docs/P4_FREEZE_RECORD.md`; the 200 held-out questions were run once (job 51585). A later run at a larger context budget is reported as a post-hoc sensitivity analysis, not as the primary result. The agent developer had read 40 of the 200 questions during annotation; both all-200 and the remaining-160 results are reported.
- **QA and RAGAS (delivered).** Exact match and token F1 under the proposed `p6-qa-v0-proposed` normalisation (ROUGE-L was not computed); live RAGAS faithfulness, response relevance and context precision with `qwen-plus-2025-12-01` as judge. See `results/final/`.

## Annotation and held-out data

The team confirmed that query–passage pairs count as evaluation records; the proposed design was 100 questions / 1,000 unique pairs (the delivered pool is 200 questions / 1,853 pairs; see Status above). Freeze the chunker before mapping evidence or creating the final annotation pool. Select disjoint development pilot records in Week 2, run a 30–50-record pilot in Week 3, and resolve guideline ambiguity before the Week 5 held-out pool.

Use two independent, blinded judgments per record. Proposed labels are binary relevance (0/1); P3/P5/P6 must define how partial evidence is treated before annotation. Hide retrieval system, score and other annotator's label. Include varied question types, hard negatives and unanswerable examples where practical. Deduplicate by question ID and passage ID. Ten distinct passages may not exist for every paper: validate this before selecting questions; never duplicate records to reach 1,000.

For the proposed three fixed annotator pairs, report raw agreement overall and by pair, plus Cohen's kappa separately for each pair with sample sizes. Do not describe pooled changing annotators as one fixed-pair Cohen's kappa. Agreement must be measured **before** adjudication; adjudicated labels do not establish 80% independent agreement. Preserve original labels. A third member who was not in the original pair adjudicates disagreements. Budget adjudication work in addition to each member's 332–334 initial judgments.

If pre-adjudication agreement falls below 80%, report it honestly, clarify guidelines and conduct fresh independent labeling under a documented protocol. Do not silently overwrite disagreements or remove difficult records to inflate agreement.

## Retrieval metrics

P6 defines K values, relevance rules, no-relevant-document handling and macro averaging before runs. P3 maps QASPER evidence to chunk IDs and records mapping failures. Deduplicate overlapping evidence for evidence-level measures where appropriate.

A pool of ten judged passages per question is incomplete relevance coverage. Report judged coverage at K. Label pool-based scores explicitly, and do not present pool recall as exhaustive full-paper recall. Evaluate ranking within the judged pool separately from full retrieval; where available, also report QASPER evidence-based metrics with mapping limitations. Unjudged results are unknown, not automatically confirmed negatives. Any additional judging must follow a frozen, system-neutral protocol.

## Minimal experiment ladder

| ID | Configuration | Evaluation | Status (7 Nov 2026) |
| --- | --- | --- | --- |
| R1 | BM25 | Rank-aware retrieval metrics and latency | Done (K = 5, accepted pooled labels) |
| R2 | Dense | Same | Done |
| R3 | Hybrid RRF | Same | Done |
| R4 | Hybrid RRF + reranker | Same | Done; it lowered all four top-five metrics and is off in the final configuration |
| G0 | Generator without retrieval | QA baseline; evidence faithfulness is not applicable | Not run |
| G1 | BM25 RAG | QA, RAGAS and latency | Not run |
| G2 | Dense RAG | Same | Not run |
| G3 | Hybrid RAG | Same | Done on the held-out run as the `static` arm (top eight, no reranker), plus the `static-wide` arm (top 15) |
| G4 | Static hybrid + reranker RAG | Same; primary static baseline | Development slice only (the "reranking only" cell of the 40-question ablation); the held-out static baseline is G3 |
| G5 | Adaptive hybrid + reranker, single critic | Same plus retries, recovery and abstention | Held-out: the `adaptive` arm without a reranker; with a reranker on the development slice only (the "both" cell) |
| Optional | Gold-evidence reference, dual critic, NLI, citation-validator ablation | Only after required runs complete | Not done |

Use the same frozen generator, answer prompt, decoding settings, question set and context budget for static/adaptive comparisons; report additional retrieval/model calls and token cost. Retain citation validation in both G4 and G5. A separate validator ablation changes only the validator. The original E/F and G/H comparisons otherwise overlap or mix factors.

Maximum two retries means **three retrieval rounds total**. Report p50/p95 latency with hardware, caching and warm-up policy. Bootstrap uncertainty over questions (or papers), not over correlated query–passage records as if independent.

## QA, citations and RAGAS

Define normalization, multiple reference-answer handling, answer-type scoring and abstention behavior before final evaluation. Report answerable/unanswerable subsets and mapping exclusions. RAGAS judge scores complement manual inspection; record evaluator version, judge model, prompt, parameters, embedding model and cost. Establish refusal handling and missing-score policy in advance.

Citation-ID validation establishes that a cited passage was supplied to the generator. It does **not** establish entailment or that numbers are supported. Evaluate citation correctness/grounding separately using manual checks and the chosen faithfulness metric. Do not claim the validator prevents all unsupported factual statements.

Tune only on development/validation data. Freeze all prompts, retrieval settings and optional variants before evaluating held-out labels. Log genuine post-freeze bug fixes and rerun affected comparisons consistently.

## Held-out freeze sequence

The observed official QASPER splits are paper-disjoint, but their mapping to the project roles remains the proposal recorded as `P3-D004` and is pending team review. The current safe default is `train -> development`, `validation -> validation`, and `test -> held_out`; this mapping must not be treated as confirmed until reviewed by the affected owners.

Use only `development` and `validation` assets to choose among the `$150`/`$200`/`$250` chunk sizes (the final corpus uses 365-word chunks with 40-word overlap), overlap and boundary settings, retrieval rules, model settings, prompts, few-shot examples, and stopping rules. Keep the held-out paper text available only through the approved inference index, and do not use held-out questions, answers, evidence, or labels to make these choices.

Before reading any held-out question, record the final Git commit and configuration, then freeze the chunker, prompts, retrieval settings, model settings, and evaluation protocol. After that freeze, run the held-out questions as final evaluation queries; read held-out answers and labels only afterward for scoring and reporting.

The final question pool must be kept separate from development experiments. `evaluation.held_out_manifest: null` remains unchanged until the question and annotation pool is actually frozen under `P3-D005`. As of 7 November 2026 the 200 held-out questions are pinned by SHA-256 in `configs/p4_freeze.json`, but `P3-D005` is still `pending team review` and the field stays `null`. The post-freeze bug-fix and rerun rule remains the proposal in `P3-D006`: a genuine bug fix must record its cause and rerun every affected configuration consistently; a held-out result must never drive a targeted improvement.

## Unified QA export and access boundary

`data/processed/qa.jsonl` is a physical union of the official `train`, `validation`, and `test` questions. Every row preserves its original question object and complete answer annotation array, with `paper_id` and `source_split` added for linkage. The export and a structural integrity check may read every row before the freeze only to copy fields, count records, hash files, and verify paper links; their summaries must not include question or answer content. This mechanical handling does not authorize people or experiment code to preview or use `test` questions, answers, evidence, or labels.

After the evaluation freeze, an evaluation entry point must select rows by `source_split` and purpose. During query execution, it may expose only `question_id`, `paper_id`, and `question` to the RAG system. It must persist query inputs and results before separately reading `answers` and evidence for scoring. Passing a complete QA row to the model is prohibited because the row contains annotations and evidence alongside the query. The export remains local under `data/processed/` and is not committed.
