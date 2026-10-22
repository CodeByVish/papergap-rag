# P2 report contribution — draft for P6

## Hybrid retrieval and reranking

PaperGap retrieves evidence within a selected paper. BM25 and the pinned
`BAAI/bge-small-en-v1.5` dense retriever each return up to 20 candidates. Dense
queries use the documented BGE retrieval instruction; passages retain original
text. Vectors are L2 normalized and FAISS IndexFlatIP supplies cosine scores.

We deduplicate by opaque passage ID and fuse source ranks using
`RRF(p) = sum_s 1 / (60 + rank_s(p))`. Source scores remain separate because
BM25 and cosine scores do not share a scale. Missing-source contributions are
absent. Ties use passage ID. The pinned `BAAI/bge-reranker-base` cross-encoder
scores the full unique union (at most 40 candidates) and selects the final five.
It uses raw logits, maximum input length 512, batch size eight and CPU inference.
Long query/passage pairs are truncated by the tokenizer. Reranker ties are
resolved by RRF score then passage ID. Empty and short candidate pools remain
empty/short rather than being padded.

Returned records preserve the full passage, final rank, source ranks and raw
scores, RRF score and nullable reranker score. RRF-only output has null reranker
scores. Exact-section forwarding, per-round agent trace and persistent
content/configuration-keyed score caching are proposed in PR #10. P4's current
planner/critic are keyword mocks, so retrieval integration does not establish
adaptive critic quality.

## Reproducibility and integration evidence

The development corpus has 32,073 passages from 1,168 papers with nonempty
passages; its SHA-256 is
`abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`.
Model revisions and reproduction commands are recorded in P2_WEEK2.md and
P2_EVALUATION_HANDOFF.md. Split/schema conventions remain proposed pending team
agreement. Corpus text may be indexed as inference evidence; held-out questions
and labels must not be used for tuning.

The 17 October integration handoff reran P1's unchanged 100 training questions.
Each method returned 485 passages across 97 nonempty questions; three questions
had no indexed full text and returned empty lists. The fresh local RRF output
matched P1's top-five passage order for every question. BGE changed selection or
order for all 97 nonempty questions. These are wiring/provenance observations,
not relevance-quality conclusions.

## Preliminary latency

The earlier six-training-question paired pilot on macOS ARM64 CPU measured:

| Candidates per source | RRF p50 / p95 ms | RRF+BGE p50 / p95 ms |
| --- | --- | --- |
| 10 | 10.1 / 10.4 | 1835.3 / 2147.8 |
| 20 | 10.3 / 11.9 | 3172.5 / 4151.5 |

Each path was warmed; model loading/index construction were excluded. The
embedding index was built on Metal, with retrieval/reranking on CPU and four
threads. These percentiles describe only that small pilot, not final benchmark
latency or throughput. BGE dominated CPU latency. Cache-hit timings must be
reported separately from fresh cross-encoder inference.

## Quality ablations and error analysis — awaiting independent labels

Compare BM25, dense, RRF and RRF+BGE on identical frozen inputs at agreed K.
Select candidate count/RRF constant only using labelled development/validation
results, then freeze before held-out inference. Report paired differences on the
same covered questions to isolate fusion and reranking contributions. Include
judged coverage, exclusions, short/empty pools and mapping limitations. Pooled
recall is not exhaustive full-paper recall; unjudged passages are unknown.

| Result | Status |
| --- | --- |
| Precision@K, Recall@K, MRR@K, nDCG@K | Pending P3/P6 labels and metric agreement |
| Best development parameters | Not selected; 20/60/top-5 remain development defaults |
| Held-out four-method table | Pending approved freeze/question manifest and labels |
| Error-category counts and reviewed examples | Awaiting labelled run and human review |
| Independent annotation agreement | Pending human labels and P6 aggregation |

Use the execution scripts to populate this section after inputs arrive. Do not
replace missing metrics with the synthetic test fixture, ranking-change counts,
LLM-generated relevance judgments, or the three-question workflow smoke run.
