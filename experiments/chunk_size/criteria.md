# Chunk Size Evaluation Criteria

Compare $150$, $200$, and $250$ words per chunk using the same sampled questions from `data/processed/qa.jsonl`, retriever, overlap in words, and top-$5$ retrieval setting. Apply the question-selection rules below before sampling.

| Metric | What it measures | How it helps choose a chunk size |
| --- | --- | --- |
| Readability pass rate | Manually inspect the same source locations for each size. Count a chunk as a pass when it expresses an understandable idea without needing the previous or next chunk. The rate is passing chunks divided by inspected chunks. | Higher is better. A low rate suggests the chunks cut explanations into pieces that are too small to understand. |
| Evidence Hit@$5$ | Among questions with usable text evidence, the percentage whose first $5$ retrieved chunks together contain at least one complete annotated evidence paragraph. A paragraph split across retrieved chunks still counts. | Higher is better: more questions retrieve useful evidence. A hit does not mean that all evidence needed to answer the question was found. |
| Complete evidence rate@$5$ | Among the same questions, the percentage whose first $5$ chunks together contain every text evidence paragraph from at least one answer annotation. | Higher is better, especially for questions needing several pieces of evidence. This checks whether useful evidence is complete. |
| Retrieved word count | Average total words in the first $5$ retrieved chunks per question, counting overlapping text again if it is passed to the answer model again. | Lower means less text for the model to read. Prefer fewer words when evidence retrieval and readability are similar; fewer words alone do not mean better quality. |

For both evidence metrics, match evidence to its source paper and paragraph; a few matching words are insufficient. Before sampling, exclude an entire question if it has no answer annotations or any annotation lacks nonempty, fully and uniquely located text evidence. Record these exclusions in `manifest.json` under `filtering_counts.invalid_answer_evidence`.

## Experiment configuration and precedence

Use `experiments/chunk_size/config.json` as this experiment's configuration authority. Its settings take precedence over settings with the same purpose in `configs/default.yaml` when they overlap or conflict. The current runner reads only the experiment JSON; it does not read or merge `configs/default.yaml`. Omitted values use experiment-code defaults, without falling back to YAML. Selecting another experiment JSON with `--config` makes that file authoritative for the run.

`configs/default.yaml` is a project-level configuration proposal. Git history shows that it was created in the project execution plan and collaboration starter commit `b564db7` on 2026/09/16, then extended by P3 data foundation and unified export commits `1697e10` and `fa19dfc` on 2026/09/26. The available history does not show it being integrated from another part. It covers data, retrieval, Agent, generation and evaluation modules; that scope does not establish it as any individual part's runtime configuration.

| Setting in `configs/default.yaml` | Corresponding experiment setting | Overlap or difference and handling |
| --- | --- | --- |
| `data.overlap_words`: $40$ | `overlap_words`: $40$ | Same chunk overlap setting and current value; use the experiment configuration. |
| `retrieval.top_k`: $5$ | `top_k`: $5$ | Same retrieval result limit and current value; use the experiment configuration. |
| `data.chunk_words`: $200$ | `candidates`: $150$, $200$, $250$ | Related purpose with a different structure; compare each candidate instead of using the single YAML size. |
| `seed`: $42$ | `seed`: $42$ | Same purpose and value; use the experiment seed for every sampling stage, without reading YAML. |

The YAML `retrieval` section proposes dense models, a reranker, candidate counts and RRF settings, whereas the experiment JSON currently specifies only `retrieval.mode` as `bm25`. This experiment has confirmed that mode and `top_k=5`. These are not equivalent complete retrieval configurations. The experiment does not inherit YAML model or fusion settings. BM25 algorithm parameters use the implementation's library defaults and remain retriever implementation details, outside the configuration choices or tuning scope of this experiment. See `experiments/chunk_size/BM25.en.md` for BM25 inputs, outputs, workflow and current parameters. See `experiments/chunk_size/README.md` for experiment retrieval-code defaults and optional modes.

The following lists every current experiment JSON setting except `candidates`, already listed above. Keep these settings fixed across candidate chunk sizes.

| Experiment setting | Current value | Meaning and constraints |
| --- | --- | --- |
| `overlap_words` | $40$ | Overlap in words between adjacent chunks; every candidate size must exceed this value. |
| `top_k` | $5$ | Maximum retrieved chunks per question; the current metrics require $5$, with fewer returned when fewer chunks are available. |
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

The following output layout is implemented and remains `v0-proposed` pending team confirmation; see `experiments/chunk_size/README.md` for commands. All paths are relative to the repository root. Use a new `run_id` for each comparison run to avoid overwriting results. The `run_id` identifies the comparison run; the configuration directory names are `chunk_size_150`, `chunk_size_200`, and `chunk_size_250`. Keep each size's files under `results/chunk_size/<run_id>/chunk_size_<size>/`, replacing `<size>` with `150`, `200`, or `250`. Generated files stay out of Git.

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

Save both evidence metrics and retrieved word counts in `results/chunk_size/<run_id>/chunk_size_<size>/evidence_review.md`; no separate retrieval detail file is needed. Sample questions from `data/processed/qa.jsonl`, not raw data. Before sampling, require the question's paper to be present in every compared retrieval corpus, at least one answer annotation, and nonempty text evidence in every annotation, with every evidence item uniquely located in an original paragraph. Empty evidence, missing text, ambiguous repeated paragraphs or `FLOAT SELECTED` evidence in any annotation excludes the entire question; even its located evidence cannot contribute a hit. Excluded questions do not enter either evidence metric or retrieved word counts. Keep the same sampled question IDs across sizes. Show only selected usable questions; do not display source splits, eligibility flags, or exclusion reasons in this report. Preserve source metadata in `qa.jsonl`.

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
