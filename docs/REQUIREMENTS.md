# Requirements and decisions

## Week 4 multi-system extension status

Step $2.5$ completed the independent held-out freeze in `data/processed/qa_for_held_out_v2.jsonl`: $200$ distinct IDs, zero banned overlap, $174$ papers and at least $6$ passages per selected paper. Predeclared seed $2026102805$ selected from $1445$ eligible all-splits gold IDs after $1884$ banned rejections. The outcome is $78$ validation/$122$ test questions; no split filter or quota is used. The retirement manifest retains hashes of all $25$ historical BM25 files; $95$ historical IDs are banned through other usage and $13$ eligible old IDs were randomly redrawn. Retirement alone does not ban old questions. `configs/default.yaml` now points to the `v2` question freeze; legacy formal BM25 commands refuse operation. Both data guides document generation and read-only verification. Formal three-algorithm retrieval, new templates and independent human judgments remain pending under Steps $2.6$–$2.9$; old pairs, ranks, scores, labels and numbering are not reused.

Step $2.4.2$ completes the scoped cross-branch inventory in `data/processed/qa_banned_for_held_out.jsonl`: $2654$ unique questions, covering all owner-designated P1/P2 IDs and all $250$ P3 selection questions, with merged provenance, fixed source commits/hashes and no known unresolved eligibility records in the accepted scope. Pure functional checks and normal frozen evaluation are not automatic exclusion grounds; owner-designated IDs remain banned unless explicitly corrected. Unrecorded external/P4–P6 use is outside the claim and later explicit evidence requires updating the inventory. The cross-branch audit and Step $2.5$ eligibility/resampling prerequisites are complete to this scope; formal retrieval remains pending. Both data guides contain commands and fields; no assignment requirement is changed.

Step $2.3$ adds a development-only BM25/Dense/Hybrid pilot with the first $5$ saved selection queries and the same $365/40$, original-query, paper-scoped top-$5$ contract. `configs/annotation_pilot.json` and `data/processed/annotation_pilot_multi_v2/frozen_config.json` record the successful BGE small pinned revision, cosine and RRF $20/60$ configuration. Source retrievers and public interfaces are reused unchanged; schemas remain `v0-proposed`. Full provenance and fields are in both data guides.

The original BM25 $200$-question/$1{,}000$-pair pool below is historical. The cross-branch banned-list audit and held-out eligibility checks are complete to the accepted scope. The intended common pool is $200$ questions and $5$–$15$ unique pairs per question, with actual $1{,}000$–$3{,}000$ pairs after deduplication. Original per-method top-$5$ ranks share one final relevance label per pair. The pilot discloses algorithm sources and annotator identity; gold evidence is confined to verification, and human labels remain empty. Formal expansion, new formal templates and independent human annotation are pending; the pilot does not establish manual agreement. See `docs/EVALUATION.md` for the current protocol; older blind-view and fixed-count descriptions below apply only to BM25 history.

## Rubric mapping

| Requirement supplied | Proposed evidence | Owner | Status |
| --- | --- | --- | --- |
| Knowledge base: ≥10,000 documents and ≥100,000 words (20 pts with annotation) | Corpus manifest, source-paper count, unique passage count, word counts and cleaning/chunking commands | P3 | Current development corpus verified: 32,073 unique passages and 4,262,446 source words; split mapping remains `v0-proposed` |
| Manually label ≥1,000 records, ≥80% agreement | 200 held-out questions × 5 distinct passages = 1,000 unique query–passage pairs, two blind labels each, pre-adjudication agreement and preserved labels | Everyone; P6 coordinates | Query–passage interpretation confirmed; annotation pending |
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
- **P3/P5/P6: splits.** The user-selected Week 4 pool uses question-level isolation across all official splits, with shared papers allowed. Exclude the saved $250$ selection questions and all other recorded experimental questions. The official-split mapping is retained only for historical experiment compatibility; it does not define this pool.
- **Team: submission metadata.** Confirm official deadline year, group number, report filename, member details and final cloud locations. The supplied instructions do not specify a filename convention.

## P3 data-contract decisions pending team review

The following entries are proposals for the shared data and evaluation boundary. Each status is `pending team review`; no entry records a confirmed team decision.

- **P3-D001 — Deferred provenance fields.** Status: `pending team review`. Proposal: keep the public eight-field `Passage` unchanged for this proposal, and record source split, project role, policy version, chunking configuration, and output hashes in corpus manifests. Affected roles: P1, P2, P4, P5, and P6. Blocked outputs: the shared Passage contract and corpus-manifest schema. Owner: `TBD at team meeting`. Update locations: `data/README.md` and the relevant schema or manifest documentation after review.

- **P3-D002 — Abstract and figure/table passages.** Status: `pending team review`. Safe default: generate `full_text` passages only; keep abstract and `figure_table` source kinds reserved but unindexed. Affected roles: P1, P2, P4, P5, and P6. Blocked outputs: corpus scope, passage counts, retrieval indexing, and citation inputs. Owner: `TBD at team meeting`. Update locations: `data/README.md`, the chunking configuration, and corpus statistics documentation after review.

- **P3-D003 — `FLOAT SELECTED` mapping.** Status: `pending team review`. Safe default: retain the observed `FLOAT SELECTED: ` prefix as evidence text and do not infer a figure/table index. Affected roles: P3, P5, and P6. Blocked outputs: evidence-to-passage mapping, evidence-level metrics, and citation analysis. Owner: `TBD at team meeting`. Update locations: `docs/QASPER_DATASET_INSPECTION.md`, `docs/EVALUATION.md`, and the mapping implementation after review.

- **P3-D004 — Annotation-pool isolation.** Status: `user-selected Week 4 implementation; shared review pending`. Use question-level isolation, allow shared papers, retain `source_split` as provenance, and sample across all official splits after the recorded-use audit. Coverage of the all-splits gold reference alone determines no held-out status. Shared Passage interfaces stay `v0-proposed`; historical split-based runners remain compatible. Affected roles: P3/P5/P6. See `docs/EVALUATION.md` and the bilingual data guides.

- **P3-D005 — Annotation-pool freeze.** Status: `Step 2.5 question freeze complete; formal common retrieval pending`. `data/processed/qa_for_held_out_v2.manifest.json` records exact IDs, eligibility/rejections, input/banned hashes and predeclared sampling rules. `configs/default.yaml:evaluation.annotation_pool_manifest` identifies this current workflow; the original BM25 freeze is retired with byte-preserving history. Use the development-frozen $365/40$/paper-scoped/top-$5$ method configurations for fresh Step $2.6$ retrieval. This question freeze does not freeze future generator or agent configurations. Human labeling and adjudication remain pending.

- **P3-D006 — Post-freeze changes.** Status: `applies to this pool`. Never tune against held-out questions, answers, evidence, judgments or results. A genuine post-freeze bug requires its cause, affected settings and consistent reruns to be recorded; preserve prior artifacts and independent judgments. Future downstream evaluation protocols still require P5/P6 review.

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
