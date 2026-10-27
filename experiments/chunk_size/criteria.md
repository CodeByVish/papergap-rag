# Chunk Size Evaluation Criteria

Compare $150$, $200$, and $250$ words per chunk using the same sampled questions from `data/processed/qa.jsonl`, retriever, overlap in words, and top-$5$ retrieval setting. Apply the question-selection rules below before sampling.

| Metric | What it measures | How it helps choose a chunk size |
| --- | --- | --- |
| Readability pass rate | Manually inspect the same source locations for each size. Count a chunk as a pass when it expresses an understandable idea without needing the previous or next chunk. The rate is passing chunks divided by inspected chunks. | Higher is better. A low rate suggests the chunks cut explanations into pieces that are too small to understand. |
| Evidence Hit@$5$ | Among questions with usable text evidence, the percentage whose first $5$ retrieved chunks together contain at least one complete annotated evidence paragraph. A paragraph split across retrieved chunks still counts. | Higher is better: more questions retrieve useful evidence. A hit does not mean that all evidence needed to answer the question was found. |
| Complete evidence rate@$5$ | Among the same questions, the percentage whose first $5$ chunks together contain every text evidence paragraph from at least one answer annotation. | Higher is better, especially for questions needing several pieces of evidence. This checks whether useful evidence is complete. |
| Retrieved word count | Average total words in the first $5$ retrieved chunks per question, counting overlapping text again if it is passed to the answer model again. | Lower means less text for the model to read. Prefer fewer words when evidence retrieval and readability are similar; fewer words alone do not mean better quality. |

For both evidence metrics, match evidence to its source paper and paragraph; a few matching words are insufficient. Filter out questions without usable text evidence before sampling and record filtering counts in `manifest.json`.

## What to save during evaluation

The following output layout is `v0-proposed`, pending implementation and team confirmation. All paths are relative to the repository root. Use a new `run_id` for each comparison run to avoid overwriting results. The `run_id` identifies the comparison run; the configuration directory names are `chunk_size_150`, `chunk_size_200`, and `chunk_size_250`. Keep each size's files under `results/chunk_size/<run_id>/chunk_size_<size>/`, replacing `<size>` with `150`, `200`, or `250`. Generated files stay out of Git.

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

Save both evidence metrics and retrieved word counts in `results/chunk_size/<run_id>/chunk_size_<size>/evidence_review.md`; no separate retrieval detail file is needed. Sample questions from `data/processed/qa.jsonl`, not raw data. Before sampling, require the question's paper to be present in every compared retrieval corpus and at least one answer annotation to have a non-empty set of text evidence paragraphs that can all be located. Keep the same sampled question IDs across sizes. Show only selected usable questions; do not display source splits, eligibility flags, or exclusion reasons in this report. Preserve source metadata in `qa.jsonl`.

Removing source splits from the report does not change the existing held-out policy. The current default corpus contains only the original `train/validation` papers. Using all of `qa.jsonl`, including original `test` questions, for chunk selection requires a matching corpus and an explicit update to that project policy. Questions used to select chunk size are not an independent final test set.

Use `paper_id + section_index + paragraph_index` to locate each evidence paragraph in `papers.jsonl`. Use zero-based indices; when coverage is partial, add zero-based, end-exclusive character offsets within the paragraph. Preserve answers as separate annotation groups. Record each answer's original text or answer value and each referenced paragraph's location and full original text. For annotations without usable text evidence, state that limitation; never treat an empty evidence set as complete coverage.

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
