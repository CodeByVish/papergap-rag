# Requirements and decisions

*Written in Week 1 as a proposal; updated on 7 November 2026 with what was delivered. The original wording is kept where the decision still stands, and each outcome is marked **Outcome**. Results and limitations are in `results/final/` and the report.*

## Rubric mapping

| Requirement supplied | Proposed evidence | Owner | Status |
| --- | --- | --- | --- |
| Knowledge base: ≥10,000 documents and ≥100,000 words (20 pts with annotation) | Corpus manifest, source-paper count, unique passage count, word counts and cleaning/chunking commands | P3 | Delivered: 28,617 passages (365-word chunks, 40-word overlap) and 5,659,921 source words from 1,584 papers; split mapping remains `v0-proposed` |
| Manually label ≥1,000 held-out records, ≥80% agreement | Proposed 1,000 unique query–passage pairs, two blind labels each, pre-adjudication agreement and preserved labels | Everyone; P6 coordinates | Delivered with limits: 200 questions from 174 papers, 1,853 judged query–passage pairs, two annotators, 89.854% agreement; one reviewer resolved the 188 disagreements and AI suggestions were used in some batches, so this is not independent third-person adjudication (report, Q4.3) |
| Hybrid retrieval (40 pts) | BM25, dense, RRF; Precision@K, Recall@K, MRR, nDCG; Streamlit UI | P1/P2/P6 | Delivered: BM25, dense, RRF and RRF + reranker compared at K = 5 on the accepted pooled labels (`results/final/p1`, `p2`); Streamlit UI on the answer service |
| Evidence-conditioned downstream task (40 pts) | QA with EM/token F1/ROUGE-L and RAGAS Faithfulness/Relevance | P5/P6 | Delivered: Qwen3-8B grounded QA on 200 held-out questions, EM and token F1 (ROUGE-L was not computed), live RAGAS faithfulness, response relevance and context precision (`results/final/p4`, `p5`) |
| Single PDF and external code/data/results links | Report, contributions, reproducibility and link-access check | Everyone; P6 assembles | Report drafted; the code and data/results links are added at assembly |

## Decisions to resolve before freezing scope

The items below are the Week 1 questions; each ends with its outcome.

- **Confirmed rubric interpretation (team confirmation, 16 September 2026):** passage chunks count as documents and query–passage pairs count as evaluation records. The proposed QASPER design may therefore use ≥10,000 passages and 1,000 unique labeled pairs. Verify actual counts; do not duplicate or pad records to meet thresholds. Report source words separately from overlap-inflated chunk words. **Outcome:** counts verified: 28,617 passages, 5,659,921 source words, 1,853 labelled pairs; source words are reported separately from overlap-inflated passage words.
- **Dataset context:** QASPER has roughly 1,500 source papers ([Ai2 dataset listing](https://allenai.org/open-data), [dataset card](https://huggingface.co/datasets/allenai/qasper)). Report source-paper and passage counts separately. The project's selected-paper retrieval scope should be explicit in the report; confirm any additional course expectation about corpus-wide search. **Outcome:** the formal evaluation uses selected-paper search; all-papers search is a demonstration feature (report, Q2).
- **Team: P3/P5/P6 assignments and backup integration owner.** Not decided yet; names remain pending. Suggested fit: P3 for data processing/detail-oriented validation, P5 for PyTorch/model inference, P6 for integration/UI/evaluation coordination. **Outcome:** assigned; see the team table in the README.
- **P5: compute.** University GPU access is available (team confirmation). GPU type, VRAM, quotas/booking limits, serving method and feasible Qwen3-8B context length remain pending. Verify with a small run in Week 1; access alone does not establish model capacity or experiment throughput. **Outcome:** Slurm jobs on one NVIDIA A40; Qwen3-8B in bfloat16 through vLLM 0.11.0 with a 32,768-token window (`results/final/p5/README.md`).
- **P1/P5: model choices.** Exact BGE embedding checkpoint is pending. Proposed reranker is `BAAI/bge-reranker-base`; proposed generator is `Qwen/Qwen3-8B`. Freeze revisions and inference settings after feasibility checks. **Outcome:** dense `BAAI/bge-small-en-v1.5` at the pinned revision in `configs/p4_freeze.json`; the reranker was evaluated and left off; generator `Qwen/Qwen3-8B` (its Hub revision pin remains open).
- **P6: RAGAS.** Confirm judge/embedding backend, access, cost budget and metric definitions early. Do not wait until final experiment week to test the evaluator. **Outcome:** RAGAS 0.2.15 with `qwen-plus-2025-12-01` as judge and `qwen3.7-text-embedding` through DashScope; scoring the two held-out arms cost about 0.63 Singapore dollars (`results/final/p4/held-out/ragas`).
- **P3/P5/P6: splits.** The proposal is paper-disjoint development/validation/held-out evaluation; official split availability is recorded, but the project-role mapping remains pending `P3-D004`. Held-out paper text can be indexed as inference evidence; its questions, answers and labels must not enter tuning or prompts. **Outcome:** the project-role mapping remains `v0-proposed` (`P3-D004`). The 200 held-out questions are not all from the official test split: 122 are from test and 78 from validation, a departure from the proposed mapping that is disclosed (`validation-in-held-out` in `configs/p4_freeze.json`, and the report, Q4.3).
- **Team: submission metadata.** Confirm official deadline year, group number, report filename, member details and final cloud locations. The supplied instructions do not specify a filename convention. **Outcome:** deadline 7 November 2026, 11:59 PM SGT; Group 24; the final file is exported as `24.pdf`.

## P3 data-contract decisions pending team review

The following entries are proposals for the shared data and evaluation boundary. Each status is `pending team review`; no entry records a confirmed team decision. As of 7 November 2026 this is unchanged: the team's 6 November sign-off covered the use of the held-out questions, the frozen held-out list and the freeze (`docs/P4_FREEZE_RECORD.md`), not these contracts, so shared schemas and split mappings stay `v0-proposed`.

- **P3-D001 — Deferred provenance fields.** Status: `pending team review`. Proposal: keep the public eight-field `Passage` unchanged for this proposal, and record source split, project role, policy version, chunking configuration, and output hashes in corpus manifests. Affected roles: P1, P2, P4, P5, and P6. Blocked outputs: the shared Passage contract and corpus-manifest schema. Owner: `TBD at team meeting`. Update locations: `data/README.md` and the relevant schema or manifest documentation after review.

- **P3-D002 — Abstract and figure/table passages.** Status: `pending team review`. Safe default: generate `full_text` passages only; keep abstract and `figure_table` source kinds reserved but unindexed. Affected roles: P1, P2, P4, P5, and P6. Blocked outputs: corpus scope, passage counts, retrieval indexing, and citation inputs. Owner: `TBD at team meeting`. Update locations: `data/README.md`, the chunking configuration, and corpus statistics documentation after review.

- **P3-D003 — `FLOAT SELECTED` mapping.** Status: `pending team review`. Safe default: retain the observed `FLOAT SELECTED: ` prefix as evidence text and do not infer a figure/table index. Affected roles: P3, P5, and P6. Blocked outputs: evidence-to-passage mapping, evidence-level metrics, and citation analysis. Owner: `TBD at team meeting`. Update locations: `docs/QASPER_DATASET_INSPECTION.md`, `docs/EVALUATION.md`, and the mapping implementation after review.

- **P3-D004 — Official split to project-role mapping.** Status: `pending team review`. Proposal: map `train -> development`, `validation -> validation`, and `test -> held_out` at the whole-paper level, subject to P5/P6 review and a repeated leakage check. A single physical papers file and QA file may each contain all official splits while every row retains `source_split`; this storage choice does not approve or freeze the project-role mapping or held-out pool. Affected roles: P3, P5, and P6. Blocked outputs: split policy, experiment manifests, and held-out usage controls. Owner: `TBD at team meeting`. Update locations: `data/README.md`, `docs/EVALUATION.md`, `configs/default.yaml`, and the split-policy implementation after review.

- **P3-D005 — Held-out freeze record and manifest.** Status: `pending team review`. Safe default: keep `evaluation.held_out_manifest: null` and do not create or tune on a final held-out question or annotation pool. Note (7 November 2026): the 200 held-out questions are now pinned by SHA-256 in the freeze record `configs/p4_freeze.json`, which was written before the run; `held_out_manifest` stays `null` because the contract is still pending and a test asserts it. Affected roles: P3, P5, and P6. Blocked outputs: the held-out question/annotation manifest, freeze record, and final-evaluation handoff. Owner: `TBD at team meeting`. Update locations: `docs/EVALUATION.md`, `configs/default.yaml`, and the future held-out manifest documentation after review.

- **P3-D006 — Post-freeze bug-fix and rerun rule.** Status: `pending team review`. Proposal: permit only genuine post-freeze bug fixes, record the cause and affected configurations, and rerun every affected comparison consistently; never use held-out results to target an improvement. Affected roles: P3, P5, and P6. Blocked outputs: the final evaluation protocol and reproducible result records. Owner: `TBD at team meeting`. Update locations: `docs/EVALUATION.md` and the experiment-record schema after review.

## Scope priority

The assignment explicitly requires corpus construction, annotation, hybrid retrieval, rank-aware metrics, UI, generation/task metrics and RAGAS. Reranking, the agent and citations are the proposed PaperGap contribution, not additional rubric requirements. Dual critics and NLI stayed optional and were not built. Keep a working static RAG baseline even if agent development slips.

## Keeping development compute manageable

- Use mocks for UI, schemas, graph transitions, retry budgets and citation-ID tests.
- Develop BM25 and metrics on small CPU fixtures; use a small passage subset for early dense/reranking checks.
- Cache corpus embeddings by dataset/chunker/model revision. Recompute when those inputs change; reuse them across query experiments.
- Test generation on 5–10 development examples before larger batches. Log input/output tokens, context length, elapsed time and peak GPU memory.
- Reuse one model service if university policy allows. Avoid each member loading a separate 8B model for routine integration.
- Benchmark a representative batch before allocating full experiment runs. Estimate GPU time from measured throughput × examples × configurations, including critic/rewrite calls and a rerun allowance.
- Cache evaluation outputs only with complete model/prompt/config keys. Agree on the RAGAS backend separately; university GPU access does not imply a hosted judge API budget.

There is no reliable hour or VRAM estimate until the GPU, precision, context lengths and call counts are known. Keep optional experiments behind completion of required evaluations.
