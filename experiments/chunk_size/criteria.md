# Chunk Size Evaluation Criteria

Round 1 completed the $100/200/400$ words-per-chunk BM25 comparison; its valid results are in `results/chunk_size/round1_bm25_20261028_02/`. Round 2 completed $9$ candidates, $200/225/250/275/300/325/350/375/400$, under `results/chunk_size/round2_bm25_20261028_01/`, fulfilling `weekly-work/week-3/TODO.md` item $2.4.2.2$. Round 3 completed the $10$ candidates below under `results/chunk_size/round3_bm25_20261028_01/`, fulfilling item $2.4.2.3$; Current `config.json` uses the Round 4 settings below; historical settings remain in each manifest. All three rounds compare fixed top-$5$ and fixed $500/1000/2000$-word budgets using the same eligible questions from `data/processed/qa.jsonl`, retriever and overlap in words. Previous $150/200/250$ experiments are void and must not contribute to selection or be pooled with these rounds.

## Candidate-size rationale and proposal

### What the execution plan establishes

[`docs/EXECUTION_PLAN.md`](../../docs/EXECUTION_PLAN.md), Week 2 / P3, suggests approximately $200$ words with $40$ words of overlap and section boundaries. Week 3 / P3 lists $150/200/250$ words as examples, using “such as”, and originally required selection using development retrieval results and readability. Readability is now removed from the evaluation; the reason is recorded at the end. It supplies no citations, QASPER length analysis or model-budget justification for those values and does not establish their optimality.

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

**Round 1 runs $100/200/400$ words with $40$-word overlap using BM25.** This is a `v0-proposed` project design, not a literature-standard combination or a frozen corpus. Screen using the two evidence metrics and retrieved word count.

| Candidate | Reason | Main question |
| --- | --- | --- |
| $100$ words | Same-unit precedent from DPR [S1]; half the current default. | Does concentrated matching reduce reading cost, or does evidence become fragmented? |
| $200$ words | Existing project default, rerun as the control in Round 1; not a published optimum. | Does the current cost–completeness compromise remain competitive? |
| $400$ words | Double the default, completing a multiplicative range inspired by broad screening [S2] and QASPER context requirements [S3]. This exact value is our design choice. | Does added context improve complete evidence enough to offset extra text, noise and truncation? |

Do not reuse the void experiments, including their $200$-word result. Use each valid run's `manifest.json` for its historical candidates and controls; the current configuration does not reconstruct historical settings.

### Round 2: confirmed refinement plan

Confirmed and executed on 2026/10/28: compare $200/225/250/275/300/325/350/375/400$ words per chunk, giving $9$ candidates at $25$-word intervals within $200$–$400$ words. Results are in `results/chunk_size/round2_bm25_20261028_01/summary.html`. Input hashes, question IDs/order, evidence filtering and readability source locations were verified; the $200/400$ controls reproduce Round 1's corpus hashes, saved rankings and per-question results exactly, excluding timings. Structured regeneration and summary validation passed. Comparative assessment belongs to TODO item $2.4.3$. Shared interfaces and the final chunk configuration remain `v0-proposed`.

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
5. BM25 findings do not automatically generalize to dense / hybrid / reranker retrieval; apply the model input-length checks below.

Words remain Unicode non-whitespace spans counted by `\S+` in `src/data/chunking.py`; do not convert published token sizes using a fixed ratio. Token-based splitting, sentence-boundary adjustment and different paragraph-merging rules belong in separate experiments.

### Round 3: confirmed local refinement plan

Confirmed and executed on 2026/10/28: compare $325/335/345/350/355/365/375/385/395/400$ words per chunk, giving $10$ candidates recorded in that run's manifest. Results are in `results/chunk_size/round3_bm25_20261028_01/summary.html`, fulfilling `weekly-work/week-3/TODO.md` item $2.4.2.3$. Input hashes, question IDs/order, evidence filtering and readability source locations were verified; all four $325/350/375/400$ controls reproduce Round 2's corpus hashes, saved rankings and per-question results exactly, excluding timings. Structured regeneration and readability summarization leave `summary.json` byte-identical to the initial result; artifact and budget checks passed. Comparative assessment belongs to item $2.4.3$. Shared interfaces and the final chunk configuration remain `v0-proposed`.

Round 2's `summary.html` supports starting at $325$: $375$ has the highest top-$5$ hit / complete evidence rates at $64\%/56\%$, but mean retrieved words are $1291.60$ versus $1203.84$ for $325$. At a $1000$-word budget, $325$ leads both metrics at $58\%/50\%$, compared with $50\%/42\%$ for $375$. Its complete evidence rate at a $500$-word budget is also the highest at $32\%$. Retain the neighborhoods of both $325$ and $375$ rather than searching only around the top-$5$ winner.

| Candidates (words) | Reason |
| --- | --- |
| $325/350/375/400$ | Retain Round 2 controls and verify agreement across rounds. |
| $335/345/355/365/385/395$ | Refine the $325$–$400$ range at approximately $10$-word intervals; retaining existing controls leaves some adjacent points $5$ words apart. |

This local search follows project results; it neither rules out better values outside the range nor establishes a literature-backed optimum. Retain the same $50$ questions and order, evidence eligibility, paper scope, BM25 settings, $40$-word overlap, `top_k=5`, `seed=42` and readability source locations from the previous rounds. Save all $10$ configurations under a new `run_id` without overwriting existing results; verify that corpus, rankings and per-question results for all four controls agree across rounds, excluding timings.

Continue using both evidence metrics at all $500/1000/2000$-word budgets as the main selection evidence, reporting actual words and exhausted-question counts; top-$5$ remains supplementary. Each question represents $2$ percentage points, and $375$ leads $325$ by only $2$ questions on top-$5$. Inspect per-question gains and losses before refining the entire range to $5$-word intervals. Validate candidate values on an independent or expanded development / validation question set before final adoption. BM25 findings do not automatically generalize to dense / hybrid / reranker retrieval.

### Round 4: expanded-question validation plan

This fulfills `weekly-work/week-3/TODO.md` item $2.4.2.4$. Current `config.json` compares $325/365/375$ words, without another dense search around $365$. In Round 3, $365$ leads top-$5$ and the $2000$-word budget, but exceeds $375$ by only $1$ question on each top-$5$ evidence metric; $325$ performs better at $500/1000$ words. Retain all three. Historical settings remain in each run's `manifest.json`.

1. **Expansion and eligibility**: preserve the original $50$ Round 3 questions and order. Reapply the existing `qa.jsonl` filter: original `train/validation` only, papers in every corpus, and nonempty, uniquely located text evidence for every answer. Exclude old IDs, sort remaining IDs, and sample $200$ without replacement using `seed=42`. Use all if fewer are available; never relax evidence rules or use `test`. Recompute pool sizes; the historical $2466$ eligible questions are only a cross-check.
2. **Frozen sample**: write `question_plan.json` before retrieval, recording regression/new/combined IDs and order, input hashes, filtering counts, requested/actual counts, paper IDs/counts, source-split question counts and overlapping papers. New means unused questions, without claiming paper independence. `--prepare-plan` freezes without retrieval; `--question-plan` reuses a plan only if current inputs, configuration and reference hashes match exactly. The run saves the same plan and records its hash in the manifest.
3. **Primary comparison**: predeclare the $1000$-word budget and complete evidence rate on new questions as primary, reporting evidence hit alongside it. This middle budget is an experimental choice, without claiming a confirmed deployment budget. Report all $500/1000/2000$-word budgets and top-$5$ separately for regression, new and combined questions, with numerators/denominators, actual words and exhaustion counts. `summary.json.validation.paired_comparisons` records candidate-exclusive successes and their question IDs for every pair, group and view; combined scores cannot replace validation on new questions.
4. **Controls and regression**: retain paper scope, chunking, BM25, $40$-word overlap, `top_k=5`, `seed=42` and actual readability source locations. Verify input hashes and reference controls. Use a new `run_id` and rebuild all three corpora/rankings. Require identical original question/evidence records, corpus hashes, saved rankings and per-question metrics against Round 3, excluding timing. Write the completion `manifest.json` only after regression verification passes.
5. **Delivery and limits**: save `manifest.json`, `question_plan.json`, `questions.jsonl`, complete retained ranking prefixes, per-question metrics, `summary.json`, grouped `summary.html` and concise `report.md`. The $200$ new questions limit workload but may not resolve small differences. Do not claim significance from small differences, redraw seeds or continue dense searching on this sample. Preserve budget tradeoffs or report that candidates remain unresolved. After selection, these questions cannot serve as independent final tests. Other retrieval modes and final configuration adoption remain separate; interfaces stay `v0-proposed`.

New configuration fields are `validation.reference_run`, `validation.additional_question_count` and `validation.primary_word_budget`; `question_sample_count=250` denotes regression plus requested new questions. Expanded validation is BM25-only. Without `validation`, existing sampling behavior is preserved. See `README.md` for preparation and reuse commands.

Executed on 2026/10/28 under `results/chunk_size/round4_bm25_20261028_01/`. Rechecked $2466$ eligible questions and $2416$ unused ones; froze $50+200=250$ questions. Regression/new/combined groups contain $48/184/224$ papers, with $8$ shared between old and new groups. All three controls reproduce Round 3 exactly, excluding timings; structured regeneration and readability import preserve summary bytes. New-question complete evidence rates at the predeclared $1000$-word budget are $104/200$, $106/200$, $108/200$ for $325/365/375$ respectively; $375$ has $5$ exclusive successes versus $3$ for $365$. This does not establish a stable optimum. Detailed group metrics and paired IDs are in the run's `summary.json`, `summary.html` and `report.md`.

### Interpretation and selection limits

- **Absolute overlap is fixed**: $40$ words means $40\%/20\%/10\%$ overlap for $100/200/400$. This tests window size at fixed overlap words, without isolating overlap ratio. A fixed-ratio comparison would be separate.
- **Fixed top-$5$ is not a fixed text budget**: approximate maxima are $500/1000/2000$ words, subject to short tails and fewer available chunks. Longer windows also favor full-paragraph coverage mechanically. Compare evidence hit rate, complete evidence rate, retrieved word count and failure cases. An equal-input-budget claim needs the separate fixed-budget control implemented for new BM25 runs below.
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
| Evidence Hit@$5$ | Among questions with usable text evidence, the percentage whose first $5$ retrieved chunks together contain at least one complete annotated evidence paragraph. A paragraph split across retrieved chunks still counts. | Higher is better: more questions retrieve useful evidence. A hit does not mean that all evidence needed to answer the question was found. |
| Complete evidence rate@$5$ | Among the same questions, the percentage whose first $5$ chunks together contain every text evidence paragraph from at least one answer annotation. | Higher is better, especially for questions needing several pieces of evidence. This checks whether useful evidence is complete. |
| Retrieved word count | Average total words in the first $5$ retrieved chunks per question, counting overlapping text again if it is passed to the answer model again. | Lower means less text for the model to read. Prefer fewer words when evidence retrieval is similar; fewer words alone do not mean better quality. |
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
6. Aggregate both coverage rates by size and budget, together with mean actual words and exhausted-question counts. Larger-budget retained text must contain the smaller-budget prefix; per-question coverage must not decrease as budget increases within a configuration.

### Reusing existing `evidence_review.md`

Reuse the report's ranking, full chunk text, answer groups, source evidence and locations as review material. However, existing files contain only five chunks, and their coverage tables give evidence-paragraph offsets without a complete mapping from chunk character offsets to source positions. They are not sufficient standalone inputs for every budget. No additional retrieval is needed only when a question's saved ranking prefix fills the budget or is confirmed to contain every chunk in that paper. Reaching the end of a report does not prove corpus exhaustion. For example, five $100$-word chunks supply at most $500$ words, insufficient for full $1000/2000$-word results; short chunks may even prevent filling $500$ words.

For reliable execution, read the valid run's `manifest.json` and verify configuration, code, input hashes and question IDs. Reconstruct chunks with source positions using the same inputs and chunking implementation, and extend the BM25 ranking as needed. Recompute coverage after truncation through the source mapping, rather than inferring it from string similarity or the old table. Use the original top-$5$ reports to check reconstruction; do not use void results as inputs.

The expanded results can still use `evidence_review.md`: retain the original top-$5$ content, append necessary later chunks in rank order under the existing `### Retrieved chunks`, and add budget tables under the existing `### Evaluation results`. For each budget save the allowance, actual words, included passage IDs/ranks, retained words and chunk-local character interval of the last chunk, budgeted source evidence spans, both Boolean outcomes, fully covered annotations and missing evidence, and exhaustion status. Keep full chunk text and separately identify retained intervals so cuts can be reviewed.

Implementation must save per-question budget results and per-size/budget numerators, denominators, rates, mean actual words and exhausted-question counts in `summary.json`. Record budgets, word-count convention, truncation policy, ranking depth, source run ID and input hashes in `manifest.json`. Save the extension under a new `run_id` without overwriting Round 1. Label top-$5$ and budgeted results separately; do not name budgeted results `@5`. Implement and validate the budget list and new fields before execution; this plan is not an existing result.

Compare coverage and actual words at the same budget first, then consider the original top-$5$ cost/coverage tradeoff when choosing later candidates. Higher top-$5$ coverage alone does not establish $400$ words as optimal.

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

These shared inputs serve quantitative retrieval reports through `run` and `regenerate`. `source_spans` additionally stores each segment's `source_text` for standalone validation, splitting CRLF into exact unequal-length segments. Manifest field `structured_inputs` records file hashes, schema, rules, `source_run_id` (null for fresh runs), and `ranking_states` indexed by size and question ID.

## Experiment configuration and precedence

Use `experiments/chunk_size/config.json` as this experiment's configuration authority. Its settings take precedence over settings with the same purpose in `configs/default.yaml` when they overlap or conflict. The current runner reads only the experiment JSON; it does not read or merge `configs/default.yaml`. Omitted values use experiment-code defaults, without falling back to YAML. Selecting another experiment JSON with `--config` makes that file authoritative for the run.

`configs/default.yaml` is a project-level configuration proposal. Git history shows that it was created in the project execution plan and collaboration starter commit `b564db7` on 2026/09/16, then extended by P3 data foundation and unified export commits `1697e10` and `fa19dfc` on 2026/09/26. The available history does not show it being integrated from another part. It covers data, retrieval, Agent, generation and evaluation modules; that scope does not establish it as any individual part's runtime configuration.

| Setting in `configs/default.yaml` | Corresponding experiment setting | Overlap or difference and handling |
| --- | --- | --- |
| `data.overlap_words`: $40$ | `overlap_words`: $40$ | Same chunk overlap setting and current value; use the experiment configuration. |
| `retrieval.top_k`: $5$ | `top_k`: $5$ | Same retrieval result limit and current value; use the experiment configuration. |
| `data.chunk_words`: $200$ | `candidates`: $325/365/375$ | Related purpose with a different structure; compare each Round 4 candidate instead of using the single YAML size. |
| `seed`: $42$ | `seed`: $42$ | Same purpose and value; use the experiment seed for every sampling stage, without reading YAML. |

The YAML `retrieval` section proposes dense models, a reranker, candidate counts and RRF settings, whereas the experiment JSON currently specifies only `retrieval.mode` as `bm25`. This experiment has confirmed that mode and `top_k=5`. These are not equivalent complete retrieval configurations. The experiment does not inherit YAML model or fusion settings. BM25 algorithm parameters use the implementation's library defaults and remain retriever implementation details, outside the configuration choices or tuning scope of this experiment. See `experiments/chunk_size/BM25.en.md` for BM25 inputs, outputs, workflow and current parameters. See `experiments/chunk_size/README.md` for experiment retrieval-code defaults and optional modes.

The following lists common experiment JSON settings except `candidates`, already listed above; the Round 4 section defines the additional `validation` settings. Keep these settings fixed across candidate chunk sizes.

| Experiment setting | Current value | Meaning and constraints |
| --- | --- | --- |
| `overlap_words` | $40$ | Overlap in words between adjacent chunks; every candidate size must exceed this value. |
| `top_k` | $5$ | Maximum retrieved chunks per question; the current metrics require $5$, with fewer returned when fewer chunks are available. |
| `word_budgets` | $500/1000/2000$ | Unique positive word limits for BM25; save enough ranks for the largest budget, independently of top-$5$. |
| `question_sample_count` | $250$ | Regression count plus requested new count in Round 4; record the actual total if unused eligible questions are insufficient. |
| `question_sampling_method` | `simple_random_without_replacement` | Sample the unused eligible pool in Round 4, preserving reference questions separately; all candidates share the same questions. |
| `seed` | $42$ | Seed for question sampling; historical sample exports use the same value with a separate random generator. |
| `retrieval.mode` | `bm25` | Use P1's `BM25Retriever` within the question's paper, with independent indexes for each chunk size and paper; no model weights are required. |

## What to save during evaluation

The following output layout is implemented and remains `v0-proposed` pending team confirmation; see `experiments/chunk_size/README.md` for commands. All paths are relative to the repository root. Use a new `run_id` for each comparison run to avoid overwriting results. Keep each size's files under `results/chunk_size/<run_id>/chunk_size_<size>/`, where `<size>` is a value from that round's `candidates`, such as `200`, `225`, or `400` in Round 2. Share these experiment result files in Git.

| Metric | What the code must save | File under the size directory |
| --- | --- | --- |
| Evidence Hit@$5$ | Save each sampled question, its answers and located evidence paragraphs, the retrieved chunks and their paragraph coverage, and the per-question hit result. Do not display source splits or eligibility fields. | `evidence_review.md`: one level-two section per question, shared with the complete evidence metric. |
| Complete evidence rate@$5$ | In the same question section, save whether at least one answer annotation's entire text evidence set is covered, which annotation satisfies this condition, and missing evidence for annotations that are not fully covered. | `evidence_review.md`. |
| Retrieved word count | Add each chunk's word count to its retrieved-chunk subsection and the total retrieved word count to each question's evaluation results. | `evidence_review.md`: shared with both evidence metrics. |

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

Also save `results/chunk_size/<run_id>/manifest.json` with the actual configuration, code commit and working-tree change status, input paths and hashes, split policy version, retriever/model version, dependencies and random seed. Record selected question IDs, requested and actual question sample counts, filtering counts by reason, and sampling seeds so the comparison can be repeated. Follow the shared experiment-record requirements in `results/README.md` when implementing the runner.

Save the comparison in `results/chunk_size/<run_id>/summary.json`: one entry per size containing evidence hit rate, complete evidence rate, retrieved word count and results at each fixed budget, with numerators and denominators where applicable. Calculate both evidence rates over the same selected questions, using the per-question results shown in `evidence_review.md`. The existing code and historical results may retain readability fields and sample files. They no longer require scoring and do not affect selection.

## Selected chunk size and overlap

Select a chunk size of $365$ words with $40$ words of overlap for the current BM25 setup. The shared configuration remains `v0-proposed`; other retrieval modes still need validation.

The main evidence comes from Round 4's $200$ new questions. The $365$-word setting performs well at top-$5$ and at the $1000/2000$-word budgets. Compared with $375$, it succeeds on $2$ more questions for each top-$5$ evidence metric. At $1000$ words, evidence hits are tied and complete evidence succeeds on $2$ fewer questions. At $2000$ words, it has $1$ more evidence hit and $1$ fewer complete-evidence success. See `results/chunk_size/round4_bm25_20261028_01/report.md`.

The predeclared primary metric was complete evidence rate on new questions at $1000$ words. Here, $375$ scores $108/200$, slightly above $365$ at $106/200$. Choosing $365$ weighs all these results; it does not mean it wins every metric or has been shown to consistently outperform $375$. At the $500$-word budget, $325$ scores higher on both evidence metrics.

Keep the $40$-word overlap used in all four rounds so adjacent chunks share some text. Other overlap values were not compared, so $40$ is not an established optimum.

## Why readability was removed

Readability pass rate is no longer used, and manual readability review is no longer required before selecting a size. Chunks mainly provide answer evidence to the LLM, which reads them together with the question and other retrieved chunks. Each chunk does not need to read like a complete standalone passage. Selection mainly considers evidence hits, evidence completeness and input word count.

Chunks of a few hundred words can usually hold several sentences, but length does not guarantee complete sentences or sufficient context. Obvious missing text and incorrect joins still need checking. Later answer evaluation can check whether these issues affect answers, without a separate readability score. Historical samples and existing code fields may remain; unreviewed samples do not block this selection.
