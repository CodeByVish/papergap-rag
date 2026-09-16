# Requirements and decisions

## Rubric mapping

| Requirement supplied | Proposed evidence | Owner | Status |
| --- | --- | --- | --- |
| Knowledge base: ≥10,000 documents and ≥100,000 words (20 pts with annotation) | Corpus manifest, source-paper count, unique passage count, word counts and cleaning/chunking commands | P3 | Passage-document interpretation confirmed; counts pending |
| Manually label ≥1,000 held-out records, ≥80% agreement | Proposed 1,000 unique query–passage pairs, two blind labels each, pre-adjudication agreement and preserved labels | Everyone; P6 coordinates | Query–passage interpretation confirmed; annotation pending |
| Hybrid retrieval (40 pts) | BM25, dense, RRF; Precision@K, Recall@K, MRR, nDCG; Streamlit UI | P1/P2/P6 | Planned |
| Evidence-conditioned downstream task (40 pts) | QA with EM/token F1/ROUGE-L and RAGAS Faithfulness/Relevance | P5/P6 | Planned |
| Single PDF and external code/data/results links | Report, contributions, reproducibility and link-access check | Everyone; P6 assembles | Planned |

## Decisions to resolve before freezing scope

- **Confirmed rubric interpretation (team confirmation, 16 September 2026):** passage chunks count as documents and query–passage pairs count as evaluation records. The proposed QASPER design may therefore use ≥10,000 passages and 1,000 unique labeled pairs. Verify actual counts; do not duplicate or pad records to meet thresholds. Report source words separately from overlap-inflated chunk words.
- **Dataset context:** QASPER has roughly 1,500 source papers ([Ai2 dataset listing](https://allenai.org/open-data), [dataset card](https://huggingface.co/datasets/allenai/qasper)). Report source-paper and passage counts separately. The project's selected-paper retrieval scope should be explicit in the report; confirm any additional course expectation about corpus-wide search.
- **Team: P3/P5/P6 assignments and backup integration owner.** Not decided yet; names remain pending. Suggested fit: P3 for data processing/detail-oriented validation, P5 for PyTorch/model inference, P6 for integration/UI/evaluation coordination.
- **P5: compute.** University GPU access is available (team confirmation). GPU type, VRAM, quotas/booking limits, serving method and feasible Qwen3-8B context length remain pending. Verify with a small run in Week 1; access alone does not establish model capacity or experiment throughput.
- **P1/P5: model choices.** Exact BGE embedding checkpoint is pending. Proposed reranker is `BAAI/bge-reranker-base`; proposed generator is `Qwen/Qwen3-8B`. Freeze revisions and inference settings after feasibility checks.
- **P6: RAGAS.** Confirm judge/embedding backend, access, cost budget and metric definitions early. Do not wait until final experiment week to test the evaluator.
- **P3/P5/P6: splits.** Record official split availability and adopt paper-disjoint development/validation/held-out evaluation. Held-out paper text can be indexed as inference evidence; its questions, answers and labels must not enter tuning or prompts.
- **Team: submission metadata.** Confirm official deadline year, group number, report filename, member details and final cloud locations. The supplied instructions do not specify a filename convention.

## Scope priority

The assignment explicitly requires corpus construction, annotation, hybrid retrieval, rank-aware metrics, UI, generation/task metrics and RAGAS. Reranking, the agent and citations are the proposed PaperGap contribution, not additional rubric requirements. Dual critics and NLI stay optional. Keep a working static RAG baseline even if agent development slips.

## Keeping development compute manageable

- Use mocks for UI, schemas, graph transitions, retry budgets and citation-ID tests.
- Develop BM25 and metrics on small CPU fixtures; use a small passage subset for early dense/reranking checks.
- Cache corpus embeddings by dataset/chunker/model revision. Recompute when those inputs change; reuse them across query experiments.
- Test generation on 5–10 development examples before larger batches. Log input/output tokens, context length, elapsed time and peak GPU memory.
- Reuse one model service if university policy allows. Avoid each member loading a separate 8B model for routine integration.
- Benchmark a representative batch before allocating full experiment runs. Estimate GPU time from measured throughput × examples × configurations, including critic/rewrite calls and a rerun allowance.
- Cache evaluation outputs only with complete model/prompt/config keys. Agree on the RAGAS backend separately; university GPU access does not imply a hosted judge API budget.

There is no reliable hour or VRAM estimate until the GPU, precision, context lengths and call counts are known. Keep optional experiments behind completion of required evaluations.
