# Scientific paper QA report

Editable LaTeX review draft for AI6127, **Group 24**. The report title is **Evidence-grounded question answering over NLP research papers**. It uses no product name or running headers; the due date, **7 November 2026**, appears on the title page. The handout specifies 11:59 pm SGT.

This is a review draft, not a submission-ready report. Retrieval results use the accepted pooled relevance labels; agent and UI measurements remain development findings. Final QA/RAG scores and controlled ablations remain pending. Highlighted notes identify missing evidence, provisional AI assessments and temporary review assignments.

## Files and report structure

Paths in this section are relative to `report/`.

| File or directory | Purpose |
| --- | --- |
| `main.tex` | Entry point, title page, formatting and reviewer-visibility switch |
| `sections/01-system.tex` | Q1.1–Q1.3: corpus; Q2.1–Q2.2: interface and five queries |
| `sections/02-retrieval.tex` | Q3: retrieval design, comparisons, chunking and depth |
| `sections/03-evaluation.tex` | Q4.1–Q4.6: generation, preprocessing, annotation, quality and performance |
| `sections/04-discussion.tex` | Q5: innovations and ablations; conclusions, limitations and future work |
| `sections/05-ai-disclosure.tex` | Final numbered section before References; AI-use statement awaiting confirmation |
| `review-checks/` | 13 highlighted question-level assessments and lead/support review assignments |
| `review-checks/p1-evidence.md` | P1 method/result sources, exact qualitative-case identifiers and scoped owner approval |
| `review-checks/p5-evidence.md` | P5 generation/answer sources, final held-out job 51585 hashes and scoped owner approval |
| `tables/` | Available retrieval, agreement and five-query tables |
| `figures/` | Pipeline figure wrappers and the development UI screenshot |
| `images/` | Supplied offline/online pipeline PNGs and companion PDFs |
| `references.bib` | Literature and QASPER dataset-source references |
| `scripts/` | Optional table refresh and pipeline-chart generation |
| `source-audit.json` | Hashes of selected drafting inputs; not an experiment freeze |
| `build/main.pdf` | Compiled review PDF; local and ignored by Git |

The former “Reproducibility and submission materials” section has been removed. Its archive-link placeholders are absent from the report; the handout's link requirements still need to be addressed before submission.

## Build and preview

From `report/`, use an installed LaTeX toolchain:

```sh
make pdf
```

This runs `latexmk` with pdfLaTeX and writes `build/main.pdf`. Alternatively:

```sh
mkdir -p build
tectonic --outdir build --keep-logs main.tex
```

The draft has been built with Tectonic 0.17.0. A temporary compiler at `/tmp/tectonic` was used during authoring; a fresh environment needs its own compiler installation. No custom fonts are required. For Overleaf, upload the source, bibliography, tables, review checks, figures and images, select `main.tex`, and use pdfLaTeX. Local raw results are not needed to compile the existing report assets.

Rebuild after edits and inspect affected PDF pages, figure readability, captions, page breaks, citations and cross-references. The P1 sign-off build on 6 November 2026 has **22 pages**, no unresolved references and no overfull/underfull box warnings. Its affected pages were rendered and visually checked; see `review-checks/p1-evidence.md` for the build boundary and non-blocking environment messages. The extra page follows the addition of the scoped review-completion markers; technical content is unchanged. Pagination will change as draft material is resolved.

Once the report is ready, the required submission filename is **`24.pdf`**. Keep `build/main.pdf` as the working preview until then.

## Figures

| Placement | Included asset | Wrapper |
| --- | --- | --- |
| Q1.1: collection, cleaning and storage | `images/offline-corpus-index.png` | `figures/offline-indexing.tex` |
| Q2.1: user interface | `figures/ui-answer.png` | Included directly in `sections/01-system.tex` |
| Q3: hybrid retrieval | `images/online-hybrid-retrieval.png` | `figures/hybrid-retrieval.tex` |

The pipeline images replace the earlier simplified TikZ diagrams and are maintained by the chart-generation script below, with captions and cross-references. The reviewed versions disclose the Dense 512-token input limit and show the critic retry path from the clipped generator view; the online caption distinguishes the agent's top-eight setting from the reported retrieval comparison at $K=5$. Their companion PDFs are available but are not used by the current build. The system overview in Q2.1 remains an inline TikZ diagram. Reserved visuals remain for retrieval depth, final performance and a reviewed qualitative example.

To regenerate both pipeline PNGs and companion PDFs, run from the repository root using a Python environment with Matplotlib:

```sh
python3 report/scripts/draw_pipeline_charts.py
```

This overwrites the four pipeline image files. Review diagram content against the implementation before regenerating or replacing them.

## Review workflow and assignments

Each handout item has its own highlighted five-star assessment: **Q1.1–Q1.3, Q2.1–Q2.2, Q3, Q4.1–Q4.6 and Q5**. Ratings assess the evidence currently available; **5/5 means “strong implementation”** as an editorial target, not an official course grade. Each box states concrete checks and a lead/support assignment.

| Tag | Member | Main project responsibility |
| --- | --- | --- |
| P1 | Junlin Yin | Sparse and dense retrieval |
| P2 | Maheshwari Vishakha Praveen | Fusion, reranking and retrieval ablations |
| P3 | Jingshuai Qian | Corpus, chunking and annotation data |
| P4 | Ananya Redhu | Agent, adaptive retrieval and agent experiments |
| P5 | Junyu Hu | Generation, citations and answer outputs |
| P6 | Changyan Xu | UI, evaluation infrastructure and integration |

| Question | Lead reviewer | Supporting reviewers |
| --- | --- | --- |
| Q1.1 | P3 | P1, P2 |
| Q1.2 | P6 | P4, P5 |
| Q1.3 | P3 | P6 |
| Q2.1 | P6 | P4, P5 |
| Q2.2 | P6 | P5, P4 |
| Q3 | P2 | P1, P3, P4, P6 |
| Q4.1 | P5 | P4, P6 |
| Q4.2 | P3 | P1, P5, P4 |
| Q4.3 | P3 | P6 and all annotators |
| Q4.4 | P5 | P4, P3, P6 |
| Q4.5 | P5 | P6 |
| Q4.6 | P4 | P5, P6, P1, P2 |
| Q5 | P4 | P5, P2, P6 |

Assignments follow the repository README and evaluation handoff. The handoff proposes P5 for QA/RAGAS runs and P4 for agent performance/cost; confirm run ownership with the team. P6 coordinates review and cross-checks results without taking over each experiment. All annotators must confirm their label provenance, independence and prior question exposure for Q4.3.

Junlin Yin approved the current P1 report content on **6 November 2026**. The highlighted **DONE FOR DRAFT - P1** markers cover indexing-diagram consistency (Q1.1), BM25/Dense methods, comparison and cases (Q3), lexical/Dense preprocessing (Q4.2), and the sources and wording of historical retrieval measurements (Q4.6). Other owners' reviews remain open; this does not approve the whole Q3 section or the team report, rerun timing measurements, or confirm final GPU performance. Individual annotation-process statements, the group AI-use disclosure and missing member information retain their existing confirmation requirements. The approved baseline and scope are recorded in `review-checks/p1-evidence.md` and `source-audit.json`.

Junyu Hu approved the current P5 report content on **6 November 2026**. The highlighted **DONE FOR DRAFT - P5** markers cover answer/refusal behavior and refusal wording (Q1.2), the generation approach and final serving/decoding settings (Q4.1), prompt rendering and output parsing (Q4.2), the scorer policy and final answer/refusal records (Q4.4), the RAGAS runner description (Q4.5), and the model/GPU record and final generation timings (Q4.6). Final EM/F1 and RAGAS scores, the Qwen3-8B Hub revision and other owners' reviews remain open; this does not approve the whole Q4 section or the team report. The supporting evidence is recorded in `review-checks/p5-evidence.md` and `source-audit.json`.

To hide temporary P1–P6 assignments, change `\draftreviewerstrue` to `\draftreviewersfalse` in `main.tex`. The switch controls only `\draftreview{lead}{support}{scope}` text. It does **not** hide AI ratings, other review boxes, missing-result markers or TODOs. Resolve those items, then remove the editorial notes from the submission copy. Keep substantive limitations and annotation disclosures in the final prose.

Search for `\todo`, `\begin{review}`, `\pending`, `\assetplaceholder` and `\draftreview` to locate unfinished material. Internal P1–P6 labels appear only in the temporary review assignments, not the explanatory prose. These assignments are not an individual contribution/grading declaration. The handout makes individual contribution attribution optional and recommends the shared project-grade option.

## Refresh available tables

From the repository root:

```sh
python3 report/scripts/refresh_tables.py
```

This script uses the Python standard library and existing local inputs. It overwrites the three available tables, copies `output/playwright/p6-local-answer.png` to `report/figures/ui-answer.png`, and refreshes `source-audit.json`. It does not run evaluation, generate labels, update the prose or modify the supplied pipeline images.

The script requires its listed ignored result files, the local UI screenshot and the original handout. Do not run it merely to rebuild the PDF. If switching experiments, update the script's sources, output summaries, surrounding prose and provenance together. Saved five-query answer summaries are fixed text in the script and need review if the input questions change. The separately maintained `tables/bm25-dense-comparison.tex` uses the verified P1 comparison bundle; the generic refresh script does not regenerate that table. Its sources and exact checks are recorded in `review-checks/p1-evidence.md` and the `p1_review_update` entry in `source-audit.json`.

## Evidence and provenance

Paths below are relative to the **repository root**, unless stated otherwise. The original handout is `../Assignment.pdf` from the repository root, or `../../Assignment.pdf` from `report/`.

| Report content | Evidence and limits |
| --- | --- |
| Assignment requirements | Original handout; takes precedence over older planning notes |
| Corpus design, counts and chunk comparison | `docs/ASSIGNMENT_WORKBOOK.md`, `configs/p4_freeze.json` and retrieval manifest; original word/type and chunk-tuning outputs were unavailable in the inspected inputs |
| Retrieval implementation | Repository README, `docs/P2_REPORT_CONTRIBUTION.md` and retrieval source |
| Accepted-label top-five retrieval table | `results/p2-final-retrieval-handoff/scored/summary.json` and its run manifest; accepted label commit `f70bf95593a6b9f705674770b8c3e833ca76290c`, frozen ranking commit `1a1dc15b824590a39c80ea11a568fbe5814a926e` |
| Paired BM25--Dense comparison | `results/p1-bm25-vs-dense-verification-20261105/comparison/ablation.csv`; one independent comparison execution reproduced the P2 CSV exactly, without rerunning retrieval or initial scoring |
| Contrasting BM25/Dense examples | Saved questions, rankings, passage text and final labels in `results/p2-final-retrieval-handoff/inputs/`; exact identifiers in `review-checks/p1-evidence.md`; Junlin Yin approved the P1 final wording on 6 November 2026 |
| Revised-label agreement and pairwise kappa | `results/p6/annotation-audit-verified-20261105/agreement.json` |
| Label balance and resolution provenance | `data/gold/p6/final/final_labels_manifest.json`; 102 human-reviewed and 86 human-spot-checked resolutions. Read its historical pre-merge review note alongside subsequent P3 confirmation and PR #50 acceptance; acceptance does not independently establish annotation independence |
| Five-query outputs, warnings and timing | `results/p6-local/five-queries-20261105.json`; output summaries are not verified factual answers |
| Development UI capture | `output/playwright/p6-local-answer.png`; not proof of a final GPU rehearsal |
| Adaptive/depth results, retry rates and intervals | `docs/P4_REPORT_CONTRIBUTION.md`; reported cluster findings, with raw cluster records unavailable locally during drafting |
| Historical reranking latency | `docs/P2_REPORT_CONTRIBUTION.md`; older 200/40 corpus, not a current benchmark |
| QA scoring policy | `src/evaluation/qa.py`; proposed project evaluator, not official QASPER scoring |
| Dataset source and literature | `references.bib`; includes the QASPER paper and Ai2 dataset distribution; corpus prose links the actual v0.3 archives |

`source-audit.json` captures selected input hashes, including the handout hash; it does not cover every report asset or establish an experimental freeze. Historical producer commit IDs in the workbook and run manifests identify different snapshots. Do not equate them with the current checkout or claim that the draft alone reproduces those runs.

The 200-question relevance pool and 40-question agent-development slice have different labels, denominators and roles. Keep pool-relative relevance recall separate from mapped-evidence recall. Final EM, token F1, RAGAS, GPU throughput and factorial ablation results cannot be inferred from either.

## Outstanding checks before submission

1. Confirm official member spellings/order and add four missing matriculation numbers. Group 24, Changyan Xu / G2607680G and Junlin Yin / G2604768B are already entered. Names are alphabetical by displayed full name.
2. Confirm annotation validity and preserve revised-label agreement, independence, method visibility and single-reviewer resolution disclosures. The accepted manifest records 102 human-reviewed and 86 human-spot-checked resolutions; the latter include the 66 previously unchecked suggestions. Their updated status does not demonstrate independent third-person adjudication or recover original independent submissions.
3. Confirm the evaluation freeze, accepted gold, prior question exposure and all-200/remaining-160 reporting. Keep passage schemas and split mappings `v0-proposed` until team confirmation.
4. Insert verified final QA/RAGAS scores, denominators, failures, uncertainty, controlled ablations and final performance/cost results. Record model revisions, prompts, decoding, hardware and timing policy.
5. Obtain the raw cluster evidence and corpus/chunk-tuning outputs supporting the transcribed findings. Reviewers should verify claims against those records.
6. Check all five demonstration answers, the critic/refusal mismatch and citation lookup. Rehearse the final GPU UI. The report uses the raw agent-log retrieval median of 31.58 ms, rounded to 31.6 ms; the workbook's 31.4 ms comes from a separate timing record.
7. Complete reserved figures and the qualitative example; confirm the supplied pipeline charts and screenshot still match the final system. Future-work proposals must remain distinct from tested improvements.
8. Have all members confirm the AI-use disclosure, additional tools/purposes, actual human verification and any required course declaration format.
9. Restore the required data/results ZIP and code/libraries ZIP links in an appropriate final location. Removing the former submission-materials section did not remove the handout requirement. Check link access and archive completeness.
10. Resolve highlighted items, remove temporary reviewer assignments and AI editorial ratings, retain substantive disclosures, rebuild and visually inspect the final PDF. Submit **`24.pdf`** through Blackboard by **7 November 2026, 11:59 pm SGT**.
