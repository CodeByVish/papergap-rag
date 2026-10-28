# Chunk Size Evaluation Criteria

Round 1 completed the $100/200/400$ words-per-chunk BM25 comparison; its valid results are in `results/chunk_size/round1_bm25_20261028_02/`. Following `weekly-work/week-3/TODO.md` item $2.4.2.2$, the current `config.json` now contains the confirmed Round 2 candidates below, which have not been run. Both rounds compare fixed top-$5$ and fixed $500/1000/2000$-word budgets using the same eligible questions from `data/processed/qa.jsonl`, retriever and overlap in words. Previous $150/200/250$ experiments are void and must not contribute to selection or be pooled with these rounds.

## Candidate-size rationale and proposal

### What the execution plan establishes

[`docs/EXECUTION_PLAN.md`](../../docs/EXECUTION_PLAN.md), Week 2 / P3, suggests approximately $200$ words with $40$ words of overlap and section boundaries. Week 3 / P3 lists $150/200/250$ words as examples, using “such as”, and requires selection using development retrieval results and readability. It supplies no citations, QASPER length analysis or model-budget justification for those values and does not establish their optimality.

Interpreting this as a local sensitivity check within $25\%$ of $200$ words is our inference. It can test the current default's neighborhood while missing useful shorter or longer windows.

### Research and project evidence

These primary sources motivate a search range; their settings do not establish an optimum for this project. Words, model tokens, domains and retrieval methods must remain distinct.

| Source | Original setting or finding | Project implication | Limitation |
| --- | --- | --- | --- |
| DPR, EMNLP 2020, Section 4.1 [S1] | Disjoint Wikipedia passages of $100$ words. | Add a $100$-word short-window control. | QASPER differs; retaining our $40$-word overlap does not reproduce DPR. |
| Wang et al., EMNLP 2024, Section 3.2, Appendix A.2, Table 3 [S2] | Tests $128/256/512/1024/2048$ chunk scales; intermediate scales perform well in its Lyft-report experiment, using long-input embeddings, generation evaluation and $20$-token overlap. | Borrow broad, multiplicative screening. | Its token settings cannot be copied as word counts or assumed optimal here. |
| QASPER, NAACL 2021 [S3] | Scientific full-paper questions can require information from different locations; supporting evidence is annotated. | Keep complete-evidence evaluation and test a longer window for context. | No fixed word-count recommendation; longer chunks cannot replace cross-section retrieval. |
| Official BAAI `bge-small-en-v1.5` card [S4] and local `src/retrieval/reranker.py` | Embedding sequence length is $512$ tokens; the local reranker defaults to truncating question–passage pairs to $512$ tokens. | Check actual tokenizer lengths before final dense / hybrid / reranker selection. | A word count below $512$ does not guarantee no truncation. |

### Proposed values and reasons

**Round 1 runs $100/200/400$ words with $40$-word overlap using BM25.** This is a `v0-proposed` project design, not a literature-standard combination or a frozen corpus. Screen using the two evidence metrics and retrieved word count; export readability samples but leave their labels pending in this round.

| Candidate | Reason | Main question |
| --- | --- | --- |
| $100$ words | Same-unit precedent from DPR [S1]; half the current default. | Does concentrated matching reduce reading cost, or do fragmented evidence and readability suffer? |
| $200$ words | Existing project default, rerun as the control in Round 1; not a published optimum. | Does the current cost–completeness compromise remain competitive? |
| $400$ words | Double the default, completing a multiplicative range inspired by broad screening [S2] and QASPER context requirements [S3]. This exact value is our design choice. | Does added context improve complete evidence enough to offset extra text, noise and truncation? |

Do not reuse the void experiments, including their $200$-word result. Use the valid Round 1's `manifest.json` for its historical candidates and controls; the current Round 2 configuration does not reconstruct historical settings.

### Round 2: confirmed refinement plan

Confirmed on 2026/10/28: compare $200/225/250/275/300/325/350/375/400$ words per chunk, giving $9$ candidates at $25$-word intervals within $200$–$400$ words. Only this plan and `config.json` have been updated; the experiment has not been run. Shared interfaces and the final chunk configuration remain `v0-proposed`.

The valid Round 1's `summary.html` supports this range: $100$ words performs no better than $200/400$ on either evidence metric at any fixed budget, while $200$ and $400$ each have advantages that warrant testing intermediate values.

| Fixed budget | $200$ words: hit rate / complete evidence rate | $400$ words: hit rate / complete evidence rate |
| --- | --- | --- |
| $500$ words | $38\%/24\%$ | $30\%/26\%$ |
| $1000$ words | $54\%/42\%$ | $54\%/46\%$ |
| $2000$ words | $78\%/70\%$ | $72\%/68\%$ |

| Candidates (words) | Reason |
| --- | --- |
| $200/400$ | Retain endpoint controls and verify agreement across rounds. |
| $300$ | Test whether the midpoint improves the cost–coverage compromise. |
| $250/350$ | Test the lower and upper halves of the range. |
| $225/275/325/375$ | Refine the spacing to $25$ words to check whether a favorable region is stable. |

These exact values come from local results and a uniform search design; the literature does not establish their optimality. Apply the following execution and selection rules.

1. Retain the valid Round 1's same $50$ questions and order, evidence eligibility, paper scope, BM25 settings, $40$-word overlap, `top_k=5`, `seed=42` and readability source locations. Verify question IDs, order and source locations before execution; a fixed seed does not replace verification.
2. Save all $9$ configurations under a new `run_id`, retaining and checking the $200/400$ controls without overwriting Round 1. Use both evidence metrics at all $500/1000/2000$-word budgets as the main selection evidence, reporting actual words and exhausted-question counts; use top-$5$ as supplementary evidence.
3. Do not select longer chunks solely on top-$5$: Round 1's complete evidence rate is $52\%$ for $400$ words versus $40\%$ for $200$, but mean retrieved words also increase from $832.88$ to $1332.72$.
4. Each question represents $2$ percentage points, so inspect small differences per question. If winners differ across budgets, preserve the cost–coverage tradeoff. If fixed-budget results still favor an endpoint, test $175$ below or $425/450$ above before claiming a global optimum.
5. Complete readability review before final adoption. BM25 findings do not automatically generalize to dense / hybrid / reranker retrieval; apply the model input-length checks below.

Words remain Unicode non-whitespace spans counted by `\S+` in `src/data/chunking.py`; do not convert published token sizes using a fixed ratio. Token-based splitting, sentence-boundary adjustment and different paragraph-merging rules belong in separate experiments.

### Interpretation and selection limits

- **Absolute overlap is fixed**: $40$ words means $40\%/20\%/10\%$ overlap for $100/200/400$. This tests window size at fixed overlap words, without isolating overlap ratio. A fixed-ratio comparison would be separate.
- **Fixed top-$5$ is not a fixed text budget**: approximate maxima are $500/1000/2000$ words, subject to short tails and fewer available chunks. Longer windows also favor full-paragraph coverage mechanically. Compare all four existing metrics and failure cases. An equal-input-budget claim needs the separate fixed-budget control implemented for new BM25 runs below.
- **BM25 selection is conditional on BM25**: $400$ words is a long-window stress point, not guaranteed BGE compatibility. Before formal model-based comparisons, record untruncated token-length distributions and overflow rates for passages and question–passage pairs using the actual checkpoints and tokenizers. With truncation, full-text evidence coverage does not prove model-visible coverage. These checks have not been run and are not existing automatic report fields.
- **Tune on development / validation only**: retain paper-level splits, evidence eligibility and the same question sample. Do not use held-out final labels to choose values or expand the range. The current $50$ questions support screening; inspect small differences per question and do not claim statistical significance without a defined criterion.
- **Final adoption**: verify corpus quantity and quality requirements, then select using the metrics and failure cases. Freezing a project-wide setting requires P3 and affected owners such as P1/P2 to confirm and synchronize configuration, corpus versions and bilingual documents. Round 1 screening does not freeze a project-wide setting.

### References: candidate-size rationale

1. [S1] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. 2020. [Dense Passage Retrieval for Open-Domain Question Answering](https://aclanthology.org/2020.emnlp-main.550/). *EMNLP 2020*, pp. 6769–6781. DOI: [10.18653/v1/2020.emnlp-main.550](https://doi.org/10.18653/v1/2020.emnlp-main.550). Section 4.1 supplies the passage-size precedent.
2. [S2] Xiaohua Wang et al. 2024. [Searching for Best Practices in Retrieval-Augmented Generation](https://aclanthology.org/2024.emnlp-main.981/). *EMNLP 2024*, pp. 17716–17736. DOI: [10.18653/v1/2024.emnlp-main.981](https://doi.org/10.18653/v1/2024.emnlp-main.981). Published Section 3.2, Appendix A.2 and Table 3 supply the screening precedent.
3. [S3] Pradeep Dasigi, Kyle Lo, Iz Beltagy, Arman Cohan, Noah A. Smith, and Matt Gardner. 2021. [A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers](https://aclanthology.org/2021.naacl-main.365/). *NAACL-HLT 2021*, pp. 4599–4610. DOI: [10.18653/v1/2021.naacl-main.365](https://doi.org/10.18653/v1/2021.naacl-main.365). Task and evidence motivation, not a fixed-length recommendation.
4. [S4] BAAI. [bge-small-en-v1.5: Official Model Card](https://huggingface.co/BAAI/bge-small-en-v1.5). `Evaluation`, `Sequence Length` column; accessed 2026/10/28. Input constraints, not evidence of an optimal chunk size.

## Evaluation metrics

| Metric | What it measures | How it helps choose a chunk size |
| --- | --- | --- |
| Readability pass rate | Manually inspect the same source locations for each size, checking semantic completeness, sufficient necessary context and logical coherence against the [readability assessment criteria](#readability-assessment-criteria). The rate is passing chunks divided by inspected chunks. | Higher is better. A low rate suggests the chunks cut explanations into pieces that are too small to understand. |
| Evidence Hit@$5$ | Among questions with usable text evidence, the percentage whose first $5$ retrieved chunks together contain at least one complete annotated evidence paragraph. A paragraph split across retrieved chunks still counts. | Higher is better: more questions retrieve useful evidence. A hit does not mean that all evidence needed to answer the question was found. |
| Complete evidence rate@$5$ | Among the same questions, the percentage whose first $5$ chunks together contain every text evidence paragraph from at least one answer annotation. | Higher is better, especially for questions needing several pieces of evidence. This checks whether useful evidence is complete. |
| Retrieved word count | Average total words in the first $5$ retrieved chunks per question, counting overlapping text again if it is passed to the answer model again. | Lower means less text for the model to read. Prefer fewer words when evidence retrieval and readability are similar; fewer words alone do not mean better quality. |
| Evidence coverage at the same word budget | Read at most $B$ words per question and compute evidence hit rate and complete evidence rate using the definitions above, without a chunk-count limit. | Higher coverage at the same budget is better; compare several budgets to assess cost versus coverage without rewarding larger chunks merely for supplying more text. |

For both evidence metrics, match evidence to its source paper and paragraph; a few matching words are insufficient. Before sampling, exclude an entire question if it has no answer annotations or any annotation lacks nonempty, fully and uniquely located text evidence. Record these exclusions in `manifest.json` under `filtering_counts.invalid_answer_evidence`.

## Evidence coverage at a fixed word budget: execution plan

This `v0-proposed` workflow was executed in the valid Round 1 and is retained for Round 2, using `word_budgets` in `config.json`; historical summaries are not retroactively extended. A fixed budget means the same word allowance, not a preselected source interval; configurations may retrieve different text. It measures evidence supplied for reading, not generated-answer quality.

### Budgets and metric definitions

Predefine $B\in\{500,1000,2000\}$ words and apply all three budgets to every chunk size; do not select only a favorable budget after inspecting results. These originally corresponded to Round 1's nominal top-$5$ maxima for $100/200/400$-word chunks and remain unchanged in Round 2 for comparison across rounds. They are project controls, not literature recommendations. Reuse the valid Round 1's same $50$ questions, order, evidence eligibility, paper scope, BM25 parameters, overlap and seed. Do not resample or use void experiments.

- **Budgeted evidence hit rate**: questions whose retained text jointly covers at least one complete annotated evidence paragraph, divided by all questions in the shared sample.
- **Budgeted complete evidence rate**: questions whose retained text jointly covers every evidence paragraph of at least one answer annotation, divided by all questions in that sample. These retain the two existing coverage decisions rather than introducing an undefined percentage of evidence covered.
- **Actual reading words**: words actually retained per question. Repeated overlap consumes budget again; merge source spans for evidence coverage without double counting evidence. Count chunk body text only, excluding headings, IDs, prompts and separators; do not convert words to model tokens.

### Per-question execution

1. Run BM25 independently within the question's paper for each configuration, sorting by score descending and passage ID ascending for ties. Do not use answers or evidence labels in ranking; preserve text order inside each chunk.
2. Append chunks in rank order until reaching $B$ words. The original top-$5$ limit does not apply: obtain enough ranked chunks for the largest budget, or every available chunk in the paper. Stopping at five must not be mistaken for corpus exhaustion. All three budgets use prefixes of the same ranking.
3. If the final chunk exceeds the remaining allowance, retain only its first $r$ words, where $r$ is the allowance. Do not skip it to fit a later shorter chunk or select text using evidence locations. Count Unicode non-whitespace spans with `\S+`; cut immediately after the last retained word, preserving preceding original text. Append nothing when the allowance is $0$.
4. Recompute source character coverage from the retained text. Evidence beyond the cut does not count; multiple retained spans may jointly cover a complete paragraph, using the existing whitespace-gap rule. Do not reuse full-chunk `full/partial` labels or top-$5$ Boolean results as budgeted decisions.
5. If all available chunks supply fewer than $B$ words, use their actual text and record actual words, `corpus_exhausted` and unused allowance. Do not pad or exclude that question. The allowance is shared, but actual reading lengths can differ in this case; report exhausted-question counts per size and budget rather than claiming every question reads exactly the budget.
6. Aggregate both coverage rates by size and budget, together with mean actual words and exhausted-question counts. Larger-budget retained text must contain the smaller-budget prefix; per-question coverage must not decrease as budget increases within a configuration. Review readability on full chunks, without scoring the artificial final budget cut.

### Reusing existing `evidence_review.md`

Reuse the report's ranking, full chunk text, answer groups, source evidence and locations as review material. However, existing files contain only five chunks, and their coverage tables give evidence-paragraph offsets without a complete mapping from chunk character offsets to source positions. They are not sufficient standalone inputs for every budget. No additional retrieval is needed only when a question's saved ranking prefix fills the budget or is confirmed to contain every chunk in that paper. Reaching the end of a report does not prove corpus exhaustion. For example, five $100$-word chunks supply at most $500$ words, insufficient for full $1000/2000$-word results; short chunks may even prevent filling $500$ words.

For reliable execution, read the valid run's `manifest.json` and verify configuration, code, input hashes and question IDs. Reconstruct chunks with source positions using the same inputs and chunking implementation, and extend the BM25 ranking as needed. Recompute coverage after truncation through the source mapping, rather than inferring it from string similarity or the old table. Use the original top-$5$ reports to check reconstruction; do not use void results as inputs.

The expanded results can still use `evidence_review.md`: retain the original top-$5$ content, append necessary later chunks in rank order under the existing `### Retrieved chunks`, and add budget tables under the existing `### Evaluation results`. For each budget save the allowance, actual words, included passage IDs/ranks, retained words and chunk-local character interval of the last chunk, budgeted source evidence spans, both Boolean outcomes, fully covered annotations and missing evidence, and exhaustion status. Keep full chunk text and separately identify retained intervals so cuts can be reviewed.

Implementation must save per-question budget results and per-size/budget numerators, denominators, rates, mean actual words and exhausted-question counts in `summary.json`. Record budgets, word-count convention, truncation policy, ranking depth, source run ID and input hashes in `manifest.json`. Save the extension under a new `run_id` without overwriting Round 1. Label top-$5$ and budgeted results separately; do not name budgeted results `@5`. Implement and validate the budget list and new fields before execution; this plan is not an existing result.

Compare coverage and actual words at the same budget first, then consider the original top-$5$ cost/coverage tradeoff and full-chunk readability when choosing later candidates. Higher top-$5$ coverage alone does not establish $400$ words as optimal.

## Structured data storage and report generation

This `v0-proposed` output contract is implemented for new BM25 runs. Store questions and evidence independently rather than parsing Markdown as computational input: JSONL holds the calculation inputs, `summary.json` holds results, and `evidence_review.md` displays those same results. Changing budgets or presentation requires no repeated BM25 execution or parsing of Markdown headings, tables and fences when the saved ranking supports the requested budget. Commands and schema field paths are documented in `README.md`; other retrieval modes retain their existing top-$5$ workflow.

### File responsibilities

All paths are under `results/chunk_size/<run_id>/`. Share experiment results in Git; raw datasets and generated corpora stay out of Git.

| Path | Contents and purpose |
| --- | --- |
| `questions.jsonl` | One eligible sampled question per line, including answer groups and full evidence; shared by all chunk sizes in the run. |
| `chunk_size_<size>/ranked_chunks.jsonl` | One BM25 result for one question per line, including full chunk text; input for all quantitative retrieval metrics. |
| `manifest.json` | Configuration, provenance, file hashes and per-question ranking retention status, establishing sufficiency or actual exhaustion. |
| `summary.json`, `chunk_size_<size>/evidence_review.md` | Generated from structured inputs for programmatic results and human review respectively; not original inputs to quantitative metrics. |

### Shared questions: `questions.jsonl`

Each record contains at least `question_id`, `paper_id`, `question`, `annotations` and `evidence_paragraphs`. Each annotation retains its original `annotation_id`, `answer` and `evidence_locations`; do not combine different answers' evidence into one set. Store deduplicated evidence paragraphs for that question with `location`, `section_index`, `paragraph_index` and full original `text`. Locations retain the existing `paper_id:section_index:paragraph_index` format with zero-based indices.

Write exactly one record per sampled eligible question in shared sample order. Source splits, exclusions and input hashes remain in the manifest/upstream exports; reports still omit source splits. Do not duplicate this file per chunk size. Later coverage calculations read its original evidence text without reopening raw data or parsing Markdown.

### Ranked results: `ranked_chunks.jsonl`

| Field | Meaning |
| --- | --- |
| `question_id`, `paper_id` | Link to the shared question and its paper. |
| `rank`, `score` | Contiguous ranks starting at $1$ and finite raw BM25 scores; score descending, passage ID ascending for ties. |
| `passage_id`, `text`, `word_count` | Chunk identity, full untruncated body and word count using `\S+`. |
| `source_spans` | Mapping chunk-local character ranges to source positions; each entry contains at least `chunk_start`, `chunk_end`, `location`, `source_start`, `source_end`. |

Map all original-source text in each chunk, not only the current answer's evidence. Character ranges are zero-based and end-exclusive; inserted separators do not become source evidence. The mapping must project any budget cut onto the original paragraph. Where normalization changes character positions, retain finer segments or an equivalent exact mapping rather than assuming both intervals always have equal lengths.

Write records in shared question order, then rank order. Passage IDs must be unique within each question and belong to its paper. Ranking must not use answers or evidence; do not add score thresholds excluding zero or negative scores. Both JSONL files use UTF-8 with one JSON object per line, joined by `question_id`, not line number or Markdown display order.

### Retention and completeness

Save the shortest ranked prefix satisfying both conditions: at least the first $5$ results and cumulative full-chunk words reaching the largest budget $B_{\max}=2000$ words. If the paper's available chunks run out first, save all of them. Save the entire final boundary chunk and truncate only during calculation. There is no need to save exactly $100$ results or impose a count cap that prevents filling the budget. If resources force an early stop, mark it incomplete and reject unsupported metrics rather than treating missing ranks as exhaustion or zero coverage.

In `manifest.json`, record `saved_count`, `available_count`, `saved_word_count`, `ranking_complete` and `retention_satisfied` for each size and question. `ranking_complete` means all available chunks in that paper were saved; `retention_satisfied` means the top-$5$ and maximum-budget requirements are met, or all available chunks were saved. Questions with no available chunks must still appear in the shared question file and status records. Budget-level `corpus_exhausted` is true only when all available chunks were consumed without filling that budget, not merely when the JSONL ends.

### Shared calculation and rendering workflow

1. Retrieval saves shared questions, per-size rankings and the manifest, recording file SHA-256 hashes, schema version, question order, chunk configuration, BM25 parameters, budgets, truncation policy and ranking retention status.
2. Calculation validates file hashes, question sets, continuous ranks, sorting, unique IDs, word counts and source mappings. Use the first $5$ results per question for Evidence Hit@5, complete evidence rate@5 and retrieved word count, and prefixes of that same ranking for both budgeted coverage rates and actual words. Fewer than five results require verified complete-ranking status.
3. Calculate coverage from question evidence and chunk source mappings, recomputing after truncation. Generate `summary.json` and `evidence_review.md` from the same per-question calculation results rather than implementing two decision paths. Markdown retains questions, answers, rankings, evidence spans and outcomes, adding budgeted results.
4. When saved rankings support a changed budget, recalculate and render directly from JSONL without retrieval. If more ranks are needed, extend using the same inputs and BM25 settings and save under a new run ID; missing ranks are not misses. Migration from original Round 1 first reconstructs and verifies artifacts as described above, without guessing source mappings from old Markdown.

Readability still uses independently sampled full chunks and manual labels. Those samples may not occur in question rankings, so ranked results alone cannot generate readability samples. These shared inputs serve quantitative retrieval reports through `run` and `regenerate`; `summarize` continues to import manual readability labels. `source_spans` additionally stores each segment's `source_text` for standalone validation, splitting CRLF into exact unequal-length segments. Manifest field `structured_inputs` records file hashes, schema, rules, `source_run_id` (null for fresh runs), and `ranking_states` indexed by size and question ID.

## Readability reviewers, chunk-size visibility and disagreements

1. The experiment owner and teammates will review the chunks; if the workload is large, review by Codex may be considered.
2. The tentative plan is to show chunk sizes and directly display the readability `.md` files described in this document.
3. Disagreements will be considered case by case; no resolution procedure has been defined.

## Readability assessment criteria

Readability in this experiment means that a chunk can be understood independently while retaining complete meaning. Assume reviewers have basic NLP knowledge. First read only the current chunk, without adjacent chunks or source text. After making a preliminary judgment, consult the source to verify omissions caused by splitting; understanding supplemented by the source must not substitute for the chunk's own interpretability.

| Criterion | Assessment question | Typical failure |
| --- | --- | --- |
| Semantic completeness | Are statements complete, without cutting off essential conditions, objects or conclusions? | Ending with “The model outperforms the baseline when…” or omitting a qualification essential to the statement's meaning. |
| Sufficient necessary context | Can the reader identify the research objects, methods and essential referents in the central statements? | Only “This method improves it significantly.” appears, without identifying the method or what it improves. |
| Logical coherence | Are relationships between sentences understandable, without abrupt combinations that impede understanding? | A method description suddenly switches to another experiment without the structure or transition needed to understand their relationship. |

Assign `pass` when all three criteria are met; assign `fail` when any criterion has a problem that impedes understanding. For failures, use the existing `Reason` column to identify the criterion, specific text and missing content, for example: “Insufficient necessary context: the referent of `This method` is in the previous chunk and cannot be identified here.” These are dimensions of the same pass/fail judgment, not additional aggregate metrics or scoring fields.

Apply the following boundaries:

- Background terms such as BM25 and Transformer do not automatically cause failure. Paper-specific symbols, abbreviations or objects essential to understanding the current statement need sufficient explanation.
- Citations and figure or table references do not automatically cause failure. “Table 2 shows that model A outperforms model B.” conveys the main conclusion; “The results are shown in Table 2.” lacks necessary context if the results cannot be understood without the table.
- Starting with a connective such as “However” does not automatically cause failure. Fail only when the missing contrast or preceding content affects understanding of the current statement.
- A chunk need not answer an entire question or contain every experimental detail. Evidence metrics assess whether the evidence needed for an answer is complete.

The following are simplified examples written for this experiment:

| Chunk text | Result | Reason |
| --- | --- | --- |
| “We evaluate BM25 on QASPER. BM25 retrieves five passages for each question.” | `pass` | Objects, operations and statements are complete, with clear sentence relationships. |
| “It performs better under these settings.” | `fail` | Insufficient necessary context: the object, comparison baseline and settings cannot be identified. |
| “BM25 retrieves five passages for each question. We exclude questions without” | `fail` | Incomplete semantics: the final selection condition is cut off. |

### References and scope of adaptation

These are manual review rules adapted for this experiment, not a standardized scale provided by the following papers.

1. Arihant Jain, Purav Aggarwal, and Anoop Saladi. 2025. [AutoChunker: Structured Text Chunking and its Evaluation](https://aclanthology.org/2025.acl-industry.69/). In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 6: Industry Track)*, pages 983–995. DOI: [10.18653/v1/2025.acl-industry.69](https://doi.org/10.18653/v1/2025.acl-industry.69). Section 4.2 and Appendix B.2, Prompt 3 assess chunk completeness through self-containment, complete ideas, necessary context and non-abrupt boundaries. This experiment adapts those dimensions from LLM binary judgments to manual review.
2. Eunsol Choi, Jennimaria Palomaki, Matthew Lamm, Tom Kwiatkowski, Dipanjan Das, and Michael Collins. 2021. [Decontextualization: Making Sentences Stand-Alone](https://aclanthology.org/2021.tacl-1.27/). *Transactions of the Association for Computational Linguistics*, 9:447–461. DOI: [10.1162/tacl_a_00377](https://doi.org/10.1162/tacl_a_00377). This paper studies whether sentences can be understood outside their original context while preserving meaning. This experiment draws on its treatment of necessary context and clear references, without rewriting sentences.

## Experiment configuration and precedence

Use `experiments/chunk_size/config.json` as this experiment's configuration authority. Its settings take precedence over settings with the same purpose in `configs/default.yaml` when they overlap or conflict. The current runner reads only the experiment JSON; it does not read or merge `configs/default.yaml`. Omitted values use experiment-code defaults, without falling back to YAML. Selecting another experiment JSON with `--config` makes that file authoritative for the run.

`configs/default.yaml` is a project-level configuration proposal. Git history shows that it was created in the project execution plan and collaboration starter commit `b564db7` on 2026/09/16, then extended by P3 data foundation and unified export commits `1697e10` and `fa19dfc` on 2026/09/26. The available history does not show it being integrated from another part. It covers data, retrieval, Agent, generation and evaluation modules; that scope does not establish it as any individual part's runtime configuration.

| Setting in `configs/default.yaml` | Corresponding experiment setting | Overlap or difference and handling |
| --- | --- | --- |
| `data.overlap_words`: $40$ | `overlap_words`: $40$ | Same chunk overlap setting and current value; use the experiment configuration. |
| `retrieval.top_k`: $5$ | `top_k`: $5$ | Same retrieval result limit and current value; use the experiment configuration. |
| `data.chunk_words`: $200$ | `candidates`: $200/225/250/275/300/325/350/375/400$ | Related purpose with a different structure; compare each candidate instead of using the single YAML size. |
| `seed`: $42$ | `seed`: $42$ | Same purpose and value; use the experiment seed for every sampling stage, without reading YAML. |

The YAML `retrieval` section proposes dense models, a reranker, candidate counts and RRF settings, whereas the experiment JSON currently specifies only `retrieval.mode` as `bm25`. This experiment has confirmed that mode and `top_k=5`. These are not equivalent complete retrieval configurations. The experiment does not inherit YAML model or fusion settings. BM25 algorithm parameters use the implementation's library defaults and remain retriever implementation details, outside the configuration choices or tuning scope of this experiment. See `experiments/chunk_size/BM25.en.md` for BM25 inputs, outputs, workflow and current parameters. See `experiments/chunk_size/README.md` for experiment retrieval-code defaults and optional modes.

The following lists every current experiment JSON setting except `candidates`, already listed above. Keep these settings fixed across candidate chunk sizes.

| Experiment setting | Current value | Meaning and constraints |
| --- | --- | --- |
| `overlap_words` | $40$ | Overlap in words between adjacent chunks; every candidate size must exceed this value. |
| `top_k` | $5$ | Maximum retrieved chunks per question; the current metrics require $5$, with fewer returned when fewer chunks are available. |
| `word_budgets` | $500/1000/2000$ | Unique positive word limits for BM25; save enough ranks for the largest budget, independently of top-$5$. |
| `question_sample_count` | $50$ | Requested question count after applying the eligibility rules below; use all eligible questions when fewer are available and record the actual count. |
| `question_sampling_method` | `simple_random_without_replacement` | Simple random sampling without replacement from the filtered question pool; currently the only supported method. All candidate configurations share the selected questions. |
| `n_paper` | $5$ | Requested paper count for readability sampling; use all eligible papers if fewer are available. |
| `n_paragraph` | $2$ | Requested paragraphs per sampled paper; use all eligible paragraphs if fewer are available. |
| `seed` | $42$ | Shared seed for question, paper and interval sampling. Question and readability samplers each initialize their own random generator with this value. |
| `retrieval.mode` | `bm25` | Use P1's `BM25Retriever` within the question's paper, with independent indexes for each chunk size and paper; no model weights are required. |

## Readability sampling

Randomly select up to `n_paper` papers without replacement from the verified `data/processed/papers.jsonl` export. Only original `train/validation` papers present in every candidate corpus and containing nonempty chunkable paragraphs are eligible; this pool is independent of the sampled questions. Sort eligible paper IDs before seeded sampling. Empty paragraphs and unnamed sections are excluded consistently with the chunker.

Within each sampled paper, order eligible paragraphs by section and paragraph index. Divide this sequence into `n_paragraph` contiguous intervals, with boundaries $\lfloor iL/k\rfloor$ for $i=0,\ldots,k$, where $L$ is the eligible paragraph count and $k=\min(L,\texttt{n\_paragraph})$. Randomly select one paragraph per interval. If there are fewer paragraphs than requested, select all. Share these source locations across all chunk sizes. This spreads samples across a few papers without requiring every paper to be reviewed.

The default budget is $5\times2=10$ source paragraphs. Aim for roughly balanced short and long paragraphs across the whole batch, without a per-paper quota. After sampling, inspect `readability_sampling.paragraph_word_counts` and `length_check` in `manifest.json`: short means at most $150$ whitespace-separated words, long means more than $150$. These are diagnostic categories, not pass/fail criteria; sampling does not automatically rebalance or guarantee equal counts. If coverage or workload is unsuitable, adjust the sample counts in a saved configuration and use a new run ID; retain the shared seed.

Estimate review workload from `readability_review_chunk_counts` and `readability_review_chunk_count_total` in `manifest.json`, not from the paragraph budget. Each size includes every chunk touching a sampled paragraph, deduplicated by passage ID within that size. The total adds the counts across sizes, since each candidate needs a separate review. `readability_sampling` also records requested/actual paper counts, selected paper IDs and actual paragraphs per paper. All labels remain `pending` until manual review.

The old `readability_sample_count`, `question_seed` and `readability_seed` configuration keys are rejected. Migrate custom run configurations to `n_paper`, `n_paragraph` and `seed`; completed historical runs remain readable by `summarize`.

## What to save during evaluation

The following output layout is implemented and remains `v0-proposed` pending team confirmation; see `experiments/chunk_size/README.md` for commands. All paths are relative to the repository root. Use a new `run_id` for each comparison run to avoid overwriting results. Keep each size's files under `results/chunk_size/<run_id>/chunk_size_<size>/`, where `<size>` is a value from that round's `candidates`, such as `200`, `225`, or `400` in Round 2. Share these experiment result files in Git.

| Metric | What the code must save | File under the size directory |
| --- | --- | --- |
| Readability pass rate | Export the source text, source locations (paper, section, paragraph and character span), passage IDs, and full chunk text for manual review. Keep the sampled source locations the same across sizes. Use the Markdown layout below; record `pass` or `fail` for each chunk, with a short reason for failures. | `readability.md`: one level-two section per sampled source text. |
| Evidence Hit@$5$ | Save each sampled question, its answers and located evidence paragraphs, the retrieved chunks and their paragraph coverage, and the per-question hit result. Do not display source splits or eligibility fields. | `evidence_review.md`: one level-two section per question, shared with the complete evidence metric. |
| Complete evidence rate@$5$ | In the same question section, save whether at least one answer annotation's entire text evidence set is covered, which annotation satisfies this condition, and missing evidence for annotations that are not fully covered. | `evidence_review.md`. |
| Retrieved word count | Add each chunk's word count to its retrieved-chunk subsection and the total retrieved word count to each question's evaluation results. | `evidence_review.md`: shared with both evidence metrics. |

### Manual readability review layout

Save the review file at `results/chunk_size/<run_id>/chunk_size_<size>/readability.md`. Each sampled source text gets a `##` section containing exactly three `###` subsections: source text, chunks (ID and text), and evaluation results. Include every chunk selected for review in full, and give each unique passage ID one result row. Do not count the same chunk twice if it appears under several source samples. Generated review reports use English headings, as shown below.

```markdown
# Readability Review

## Source sample: <sample_id>

### Source text

Paper: <paper_id>; section: <section_index>; paragraphs: <paragraph_indices>; character span: <start:end>.

<Original source text, with enough context to check the chunk boundaries.>

### Chunks (ID and text)

Passage ID: `<passage_id>`

<Full chunk text. Repeat the ID and text for each selected chunk.>

### Evaluation results

| Passage ID | Result | Reason |
| --- | --- | --- |
| `<passage_id>` | pending | |
```

The code initially writes `pending`; the reviewer replaces it with `pass` or `fail`. Judge each chunk's readability on its own; use the source text to check what was cut off. After review, the summary code reads the result table and calculates passing unique chunks divided by all unique reviewed chunks. Unknown labels or missing result rows must be reported instead of silently counted as failures.

### Evidence review layout and question selection

Save both evidence metrics and retrieved word counts in `results/chunk_size/<run_id>/chunk_size_<size>/evidence_review.md`; the planned calculation inputs are JSONL files defined in the structured-data section. Sample questions from `data/processed/qa.jsonl`, not raw data. Before sampling, require the question's paper to be present in every compared retrieval corpus, at least one answer annotation, and nonempty text evidence in every annotation, with every evidence item uniquely located in an original paragraph. Empty evidence, missing text, ambiguous repeated paragraphs or `FLOAT SELECTED` evidence in any annotation excludes the entire question; even its located evidence cannot contribute a hit. Excluded questions do not enter either evidence metric or retrieved word counts. Keep the same sampled question IDs across sizes. Show only selected usable questions; do not display source splits, eligibility flags, or exclusion reasons in this report. Preserve source metadata in `qa.jsonl`.

Removing source splits from the report does not change the existing held-out policy. The current default corpus contains only the original `train/validation` papers. Using all of `qa.jsonl`, including original `test` questions, for chunk selection requires a matching corpus and an explicit update to that project policy. Questions used to select chunk size are not an independent final test set.

Use `paper_id + section_index + paragraph_index` to locate each evidence paragraph in `papers.jsonl`. Use zero-based indices; when coverage is partial, add zero-based, end-exclusive character offsets within the paragraph. Preserve answers as separate annotation groups. Record each answer's original text or answer value and each referenced paragraph's location and full original text. All annotations in the report have passed the evidence eligibility rule; an empty evidence set never counts as complete coverage. This filtering rule does not change the complete evidence metric: covering every evidence paragraph from at least one annotation is sufficient.

Each `##` question section contains four `###` subsections. Each answer and each of the top-$5$ retrieved chunks gets its own `####` subsection. Generated reports use English headings and fields; preserve original question, answer, and paragraph text.

```markdown
# Evidence Review

## Question: <question_id>

### Question ID and text

Question ID: `<question_id>`; paper ID: `<paper_id>`.

<Original question text.>

### Answers

#### Answer: <annotation_id>

<Original answer text or answer value.>

Evidence location: `<paper_id>:<section_index>:<paragraph_index>`

<Full original evidence paragraph. Repeat for each referenced paragraph.>

### Retrieved chunks

#### Rank 1: <passage_id>

Passage ID: `<passage_id>`; retrieval score: <score>.

Word count: <word_count>.

<Full chunk text. Repeat this subsection for each retrieved chunk.>

| Evidence location | Coverage | Character span within paragraph |
| --- | --- | --- |
| `<paper_id>:<section_index>:<paragraph_index>` | full / partial | <start:end> |

### Evaluation results

Evidence Hit@5: <true or false>

Complete evidence rate@5: <true or false>

Total retrieved words: <sum of the retrieved chunks' word counts>.

Fully covered answer annotations: <annotation IDs, or none>.

Missing evidence by answer annotation: <paragraph locations and uncovered spans>.
```

The code computes the per-question results from the combined source spans of the retrieved chunks; the Markdown provides the reviewable details. List all annotated evidence paragraphs touched by each chunk, marking full or partial coverage; write `none` if none are touched. Partial coverage alone is not a hit, but several chunks may together cover a complete paragraph. A hit requires at least one complete evidence paragraph; complete evidence requires every text evidence paragraph from at least one usable answer annotation. Both summary rates use the number of sampled questions as their denominator and describe this sample's performance.

Count words in the displayed chunk text using the same Unicode non-whitespace runs as the chunker, not model tokens. Each question's total is the sum of its retrieved chunks' word counts, including repeated overlap. The retrieved word count in `summary.json` is the mean of these totals over the same sampled questions.

Also save `results/chunk_size/<run_id>/manifest.json` with the actual configuration, code commit and working-tree change status, input paths and hashes, split policy version, retriever/model version, dependencies and random seed. Record the readability sample locations, selected question IDs, requested and actual question sample counts, filtering counts by reason, and sampling seeds so the comparison can be repeated. Follow the shared experiment-record requirements in `results/README.md` when implementing the runner.

Save the comparison in `results/chunk_size/<run_id>/summary.json`: one entry per size containing the four metric values, their numerators and denominators where applicable, and pending readability review counts. Calculate both evidence rates over the same selected questions, using the per-question results shown in `evidence_review.md`. Keep readability pass rate as `null` until all sampled chunks have been reviewed; then update it from the manual labels. Do not treat pending reviews as failures.
