# Evaluation protocol — Week 1 proposal

## Annotation and held-out data

The team confirmed that query–passage pairs count as evaluation records; the proposed design is 100 questions / 1,000 unique pairs. Freeze the chunker before mapping evidence or creating the final annotation pool. Select disjoint development pilot records in Week 2, run a 30–50-record pilot in Week 3, and resolve guideline ambiguity before the Week 5 held-out pool.

Use two independent, blinded judgments per record. Proposed labels are binary relevance (0/1); P3/P5/P6 must define how partial evidence is treated before annotation. Hide retrieval system, score and other annotator's label. Include varied question types, hard negatives and unanswerable examples where practical. Deduplicate by question ID and passage ID. Ten distinct passages may not exist for every paper: validate this before selecting questions; never duplicate records to reach 1,000.

For the proposed three fixed annotator pairs, report raw agreement overall and by pair, plus Cohen's kappa separately for each pair with sample sizes. Do not describe pooled changing annotators as one fixed-pair Cohen's kappa. Agreement must be measured **before** adjudication; adjudicated labels do not establish 80% independent agreement. Preserve original labels. A third member who was not in the original pair adjudicates disagreements. Budget adjudication work in addition to each member's 332–334 initial judgments.

If pre-adjudication agreement falls below 80%, report it honestly, clarify guidelines and conduct fresh independent labeling under a documented protocol. Do not silently overwrite disagreements or remove difficult records to inflate agreement.

## Retrieval metrics

P6 defines K values, relevance rules, no-relevant-document handling and macro averaging before runs. P3 maps QASPER evidence to chunk IDs and records mapping failures. Deduplicate overlapping evidence for evidence-level measures where appropriate.

A pool of ten judged passages per question is incomplete relevance coverage. Report judged coverage at K. Label pool-based scores explicitly, and do not present pool recall as exhaustive full-paper recall. Evaluate ranking within the judged pool separately from full retrieval; where available, also report QASPER evidence-based metrics with mapping limitations. Unjudged results are unknown, not automatically confirmed negatives. Any additional judging must follow a frozen, system-neutral protocol.

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
