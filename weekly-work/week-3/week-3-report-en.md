# Week 3 Report: Chunk-Size Selection and Passage Delivery

**English** | [简体中文](week-3-report-zn.md)

Status as of 2026/10/28

## Work completed

P3 completed a coarse-to-fine chunk-size comparison for the QASPER knowledge base, selected $365$ words per chunk with $40$ words of overlap for the current BM25 setup, and rebuilt and verified the passage databases. This report covers P3 delivery; other modules' Week $3$ checkpoints are outside its scope.

Quantitative criteria used evidence hit rate, complete evidence rate and retrieved word count. Fixed $500/1000/2000$-word budgets were the main comparison, with top-$5$ as supplementary evidence; readability scoring was excluded. Metric definitions, sampling, controls and research supporting the search design are in the [evaluation criteria](../../experiments/chunk_size/criteria.md). Experiment dependencies were integrated into `p3`; their sources and destinations are in the [integration plan](INTEGRATION_PLAN.md).

## From screening to validation

The first three rounds reused the same $50$ eligible development/validation questions. Round $4$ retained them for regression checks and added $200$ previously unused questions, reporting the groups separately. Repeated controls reproduced the previous round's corpus, rankings and per-question results, excluding timings. Held-out `test` supervision was not used for selection. Earlier $150/200/250$ experiments were void and excluded.

| Round | Candidates, in words | Main finding | Results | Assessment |
| --- | --- | --- | --- | --- |
| $1$: broad screening | $100/200/400$ | $100$ did no better on either evidence metric at any fixed budget; refine between $200$ and $400$. | [summary.html](../../results/chunk_size/round1_bm25_20261028_02/summary.html) | [report.md](../../results/chunk_size/round1_bm25_20261028_02/report.md) |
| $2$: interval refinement | $200$–$400$ at $25$-word intervals, $9$ candidates | $375$ led top-$5$; $325$ led both metrics at $1000$ words. Retain their neighborhoods. | [summary.html](../../results/chunk_size/round2_bm25_20261028_01/summary.html) | [report.md](../../results/chunk_size/round2_bm25_20261028_01/report.md) |
| $3$: local refinement | $325/335/345/350/355/365/375/385/395/400$ | $365$ led top-$5$ and both metrics at $2000$ words; $325$ retained advantages at smaller budgets. | [summary.html](../../results/chunk_size/round3_bm25_20261028_01/summary.html) | [report.md](../../results/chunk_size/round3_bm25_20261028_01/report.md) |
| $4$: expanded-question validation | $325/365/375$ | New-question results retained budget-dependent tradeoffs; adopt $365$ as an overall choice. | [summary.html](../../results/chunk_size/round4_bm25_20261028_01/summary.html) | [report.md](../../results/chunk_size/round4_bm25_20261028_01/report.md) |

On the $200$ new questions, $365$ achieved top-$5$ evidence hits of $147/200$ and complete evidence of $125/200$, each $2$ questions ahead of $375$, with fewer retrieved words on average ($1246.83$ versus $1261.78$). However, on the predeclared primary metric, complete evidence at $1000$ words, $375$ scored $108/200$ versus $106/200$ for $365$; evidence hits tied at $131/200$. At $500$ words, $325$ led both metrics. The selection is an overall tradeoff, not a primary-metric win or proof of a stable optimum; detailed reasoning is in the Round $4$ assessment above. Overlap was fixed at $40$ words and was not separately tuned.

## Configuration and corpus delivery

The parameters are implemented in [`configs/default.yaml`](../../configs/default.yaml). These local outputs and their manifests were regenerated and verified; commands, hashes and verification details are in the [data guide](../../data/README.md).

| Output under `data/processed/` | Passages |
| --- | --- |
| `passages.jsonl` — development corpus | $21{,}360$ |
| `passages_all_paper_text.jsonl` — all-paper-text inference corpus | $28{,}617$ |
| `sample_passages_100.jsonl` — dependency sample | $100$ |

Verification covered configuration agreement, nonempty text, the $365$-word limit, unique IDs, contiguous numbering, valid reciprocal neighbor links within original source containers, corpus scope and output hashes. Both full corpora passed `scripts.check_corpus`; paper/QA export and export-manifest hashes remained unchanged. Generated data stays outside Git. Builders require explicit $365/40$ CLI arguments and do not automatically read YAML.

P3 configuration and corpus delivery are complete. Shared interfaces and split mappings remain `v0-proposed`; project-wide freezing requires the affected module owners' confirmation. Changed passage IDs require downstream indexes and references to be updated. Dense, hybrid and reranker modes need their own token-length, truncation and retrieval checks. New questions share $8$ papers with the original group and have now been used for selection; they are not an independent final test set.
