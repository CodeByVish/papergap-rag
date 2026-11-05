# Week 1 Work Report: QASPER Data Foundation

**English** | [简体中文](week-1-report-zn.md)

As of September $26$, $2026$

## 1. Overview and Scope

This week I completed acquisition and quality checks for a pinned QASPER release, the separated paper and question exports, the `Passage` model and construction flow, and a targeted audit of figure and table evidence availability. I also documented measurements for the 100-passage dependency sample and two corpus scopes. The development values come from the existing baseline in `data/README.md`; the all-paper-text values were checked against the local manifest. This report records work I completed with traceable sources. The split-role mapping and `Passage` interface remain team-review proposals marked `v0-proposed`; retrieval and QA experiments are not reported as completed work.

The work and evidence chain was: acquire and inspect the pinned raw data → separate paper and question records → define and build `Passage` records → document the 100-item sample and measurements for both corpus scopes → inspect figure and table availability. The raw official splits remain unchanged, and downloaded or generated data stays in local ignored directories.

## 2. Pinned Data, Acquisition, and Inspection

The input is configuration `qasper` of `allenai/qasper`, pinned to revision `fdc9d8214fbab5dd782958601db4d678e6934a54`, corresponding to source version `0.3.0`. Pinning the full revision makes the input reproducible. The acquisition code verifies each official archive's declared size and SHA-256, reads only the allow-listed archive members, and writes a `manifest.json` with version, split row counts, and hashes. Acquisition preserves the raw `train`, `validation`, and `test` records without cleaning or chunking. The offline inspector checks the manifest, split hashes, and row counts before parsing structure and writing an inspection report.

| Official split | Papers | Questions | Answer annotations | Raw file SHA-256 |
| --- | ---: | ---: | ---: | --- |
| `train` | $888$ | $2{,}593$ | $2{,}675$ | `7a25389963d05d97de9462d4e46b2ef367f37b898de55f5833bae7aa4b6e8732` |
| `validation` | $281$ | $1{,}005$ | $1{,}764$ | `f3e8f8072bbb42c6f770cdbc311672738683505eef401a7b75e0c08cfb7c5945` |
| `test` | $416$ | $1{,}451$ | $3{,}554$ | `308380c3da5287ac450582c457a9a75303b8361360dd88e727afd021c8320779` |
| Total | $1{,}585$ | $5{,}049$ | $7{,}993$ | — |

One raw JSONL row represents one paper. Question count is the sum of the lengths of all `qas` lists; answer-annotation count is the sum of all questions' `answers` list lengths. Fields or evidence items inside one answer annotation are not counted as separate answers. The inspection report found no duplicate paper IDs within a split and no overlap among the three official splits. This describes the distributed split labels and does not by itself assign project evaluation roles.

Inspection found one paper with an empty `full_text` list, $8$ section names that became blank after trimming, $12$ `null` section names, and $1{,}537$ blank paragraph strings. These are raw-structure observations; they do not mean the acquisition or inspector dropped whole papers. The split counts and anomalies are recorded in `docs/QASPER_DATASET_INSPECTION.md`; the raw split SHA-256 values match `data/raw/qasper/manifest.json`.

## 3. Raw Structure and Unified Export

The data flow is: three raw splits, with `qas` nested in each paper → read-only projection → `papers.jsonl` (one paper per line) + `qa.jsonl` (one question per line) + `qasper_export.manifest.json`. The derived files write splits in `train`, `validation`, `test` order and preserve `source_split` on each row for provenance. Physical combination does not change the official splits or project evaluation boundaries.

Field types follow the fixed [QASPER 0.3.0 schema](https://huggingface.co/datasets/allenai/qasper/blob/fdc9d8214fbab5dd782958601db4d678e6934a54/dataset_infos.json). The tables use JSON types; `array<T>` means an array whose elements have type `T`, and `null` means the JSON null value.

### Raw Paper Record

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | `string` | Source paper ID; exported question rows refer to it through `paper_id`. |
| `title` | `string` | Paper title, preserved as a source field. |
| `abstract` | `string` | Paper abstract, preserved as a source field. |
| `full_text` | `array<object>` | Ordered list of paper sections; each item has `section_name` (`string` or `null`) and `paragraphs` (`array<string>`), and supplies text for `Passage` construction. |
| `figures_and_tables` | `array<object>` | Figure/table items; each has a `caption` (`string`) and a `file` (`string` filename). The metadata does not mean an image file is available. |
| `qas` | `array<object>` | Questions and complete answer annotations nested in the paper; removed from the paper-only export. |

### `papers.jsonl`

This file retains the paper fields listed above except `qas`, and adds the following provenance field.

| Field | Type | Meaning |
| --- | --- | --- |
| `source_split` | `string` | Records whether a paper came from the official `train`, `validation`, or `test` split; this field is added during export. |

### `qa.jsonl`

Each row is one question record. It retains the complete question object and answer annotations, and adds paper linkage and source-split fields.

| Field | Type | Meaning |
| --- | --- | --- |
| `question_id` | `string` | Question ID. |
| `paper_id` | `string` | ID of the paper containing the question; matches `id` in `papers.jsonl`. |
| `source_split` | `string` | Official `train`, `validation`, or `test` split of the source paper. |
| `question` | `string` | Question text. |
| `answers` | `array<object>` | Complete answer-annotation array for the question; each item has the structure shown below. |
| `nlp_background` | `string` | NLP experience reported by the question writer. |
| `paper_read` | `string` | Records whether the question writer had read the paper. |
| `question_writer` | `string` | Question-writer ID. |
| `search_query` | `string` | Query used by the question writer to find the paper's abstract among candidate abstracts; it may be an empty string. |
| `topic_background` | `string` or `null` | Question writer's familiarity with the paper's topic; the raw data allows `null`. |

### Answer Annotation

Each item in the `answers` array is one answer annotation.

| Field | Type | Meaning |
| --- | --- | --- |
| `annotation_id` | `string` | Answer-annotation ID. |
| `worker_id` | `string` | Answer annotator ID. |
| `answer` | `object` | Answer content, including evidence, answer text, or labels; its fields are listed below. |

### Answer Content

| Field | Type | Meaning |
| --- | --- | --- |
| `answer.evidence` | `array<string>` | Evidence paragraph, figure, or table text items used by the annotator. |
| `answer.extractive_spans` | `array<string>` | List of answer spans extracted from the paper. |
| `answer.free_form_answer` | `string` | Free-form answer text. |
| `answer.highlighted_evidence` | `array<string>` | Evidence sentences selected by the annotator; these are finer-grained than the paragraph-level text in `evidence`. |
| `answer.unanswerable` | `bool` | Indicates whether the question cannot be answered. |
| `answer.yes_no` | `bool` or `null` | Yes/no answer label; it may be a boolean or JSON `null`. |

`papers.jsonl` preserves the original paper-level fields except `qas`, then adds `source_split`. `qa.jsonl` preserves each complete original question object and all answer annotations, then adds `paper_id` and `source_split`. The files join on `paper_id`. The corpus builder reads only the paper export; it does not read questions, answers, or evidence annotations from `qa.jsonl`.

The exporter rejects duplicate paper IDs and question IDs. The independent checker verifies source provenance, output hashes, row and split counts, answer-annotation counts, and each question's paper and split links. The recorded row-by-row projection comparison found matching fields and values for all source papers and questions. Structural handling of `test` was limited to mechanical projection, counting, hashing, and link checks; it did not preview `test` question or answer text or use it for tuning.

## 4. `Passage` Model, Construction, and IDs

The current public `Passage` model has eight fields. Its field set and sequence semantics remain `v0-proposed`. “Null” below describes the JSON representation; every field except the two neighbor fields requires a non-empty value.

| Field | Type or nullability | Meaning | Construction rule or downstream use |
| --- | --- | --- | --- |
| `passage_id` | Non-empty string | Stable reference ID for a passage. | Generated from fixed dataset/transformation context and source coordinates; used for deduplication and citations. |
| `paper_id` | Non-empty string | ID of the source paper. | Matches the source paper's `id`. |
| `title` | Non-empty string | Normalized paper title. | Only line endings and outer whitespace are normalized; a blank title yields no passages. |
| `section` | Non-empty string | Display section name. | Does not determine source-container boundaries; sections with equal names are not merged. |
| `chunk_number` | Integer starting at $0$ | Contiguous chunk position within one source container. | Equals the ID coordinate `chunk_index` and resets to $0$ for each container. |
| `text` | Non-empty string | Body chunk from one source container. | Chunked by Unicode non-whitespace runs; never crosses paper or section boundaries. |
| `previous_passage_id` | Non-empty string or JSON `null` | Direct predecessor in the same source container. | `null` for the first chunk; otherwise points to the direct previous chunk. |
| `next_passage_id` | Non-empty string or JSON `null` | Direct successor in the same source container. | `null` for the last chunk; otherwise points to the direct next chunk. |

The current builder reads only paper `id`, `title`, and `full_text`; it does not read `qas`, questions, answers, evidence, or figure/table metadata. Every original `full_text[section_index]` is processed as a separate source container, including sections with repeated names. Multiple non-empty paragraphs within one section are joined in source order with a blank line before chunking. Text normalization converts CRLF and CR line endings to LF, trims paragraph edges, and drops empty paragraphs. It preserves internal whitespace, casing, punctuation, Unicode content, paragraph order, and evidence-marker text. Section names and titles receive the same line-ending and outer-whitespace treatment. Chunking counts Unicode non-whitespace runs (`\S+`); the current window is $200$ words, with $40$ words of overlap and a $160$-word step. These are working settings, not experimentally optimized or frozen parameters.

Blank or `null` section names and sections with no usable body are skipped; malformed section structure raises an error. Skipped sections keep their original `section_index`, so later sections are not renumbered. `source_split`, `section_index`, and `source_kind` are export provenance, internal coordinates, or manifest metadata rather than fields in the public eight-field model. The only source kind currently built is `full_text`.

The internal ID coordinate is `(paper_id, source_kind, section_index, chunk_index)`. The hash input also includes the pinned data revision, parser version, normalization version, chunking version, and chunk-size/overlap parameters. The final format is `qasper-passage-v1-` followed by a 64-character lowercase SHA-256 digest. Display title, section name, `source_split`, and output row number do not affect the ID. This keeps same-named sections separate and makes references and deduplication keys stable for the same pinned input and configuration. Neighbor links connect direct adjacent chunks only within the same `(paper_id, source_kind, section_index)`; each container's outer neighbor is JSON `null`. Abstract and figure/table sources are reserved by the coordinate type but do not currently produce passages.

The original `section_index` is the zero-based position in the `full_text` section list and is not renumbered when an earlier section is skipped. The current ID context uses parser version $1$, `text-normalization-v1`, and `word-chunking-v1`.

## 5. Sample, Complete Corpora, and Counting Rules

The 100-passage dependency sample uses paper text from `train` and `validation` only. It selects complete section chunk groups in stable paper order, at most one group per paper, and contains passages from 100 distinct papers. It supports interface and reproducibility checks and does not represent full-corpus size. The local `sample_passages_100.manifest.json` records its file SHA-256 as `d017b7937d2e9a54ee653c8a3a94f37afa2819d548c0f79eacc93f08832bdb42`.

| Corpus scope | Source splits | Purpose | Source papers | Papers producing passages | Unique passages | Source words excluding overlap | Passage words including overlap | SHA-256 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `development` | `train` + `validation` | Passage collection built from paper text in the `train` and `validation` splits for development | $1{,}169$ | $1{,}168$ | $32{,}073$ | $4{,}262{,}446$ | $4{,}897{,}846$ | `abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790` |
| `all-paper-text` | Paper text from all three official splits | `index_for_inference` | $1{,}585$ | $1{,}584$ | $42{,}719$ | $5{,}659{,}921$ | $6{,}495{,}041$ | `32fa43714d6be6822636fd8513af8358cfff78474d50f7c310a1b90d28a868fa` |

“Source papers” counts papers included in the scope; “papers producing passages” counts papers that generated at least one body passage. The difference is one, but the available aggregate counts do not identify that paper, so it cannot be asserted to be the paper with an empty `full_text`. “Unique passages” is counted by distinct `passage_id`. Source-word count counts each source paragraph that contributed to a passage once; passage-word count counts output chunks separately and therefore includes repeated words in overlapping windows. Counts use Unicode non-whitespace runs.

The project size threshold is at least $10{,}000$ passages and $100{,}000$ words. The current development corpus exceeds it; these are corpus-size statistics, not retrieval or QA performance. The `development` row is the existing baseline recorded in `data/README.md`; the corresponding corpus JSONL and manifest are not retained in the current workspace, so these values are not presented as a newly rebuilt result. The `all-paper-text` row comes from the local `data/processed/passages_all_paper_text.manifest.json` and matches its counts and SHA-256.

## 6. Split Isolation, Figures, and Tables

The proposed mapping from official splits to project roles remains `v0-proposed`: `train → development`, `validation → validation`, and `test → held_out`. It separates whole papers and does not randomly resplit questions or passages. Paper-ID disjointness is an inspection finding; confirmation of the project-role mapping and final evaluation freeze is still pending. `all-paper-text` includes `test` paper bodies for inference indexing only. `test` questions, answers, evidence, and manually assigned labels must not be used for tuning, prompt design, or chunk-parameter selection.

The existing focused figure/table audit records $1{,}551$ papers with figure/table entries and $11{,}364$ references: $6{,}492$ table references and $4{,}872$ figure references. The records include captions and `.png` filenames, but the pinned official archive has no corresponding image files; $0$ of the $11{,}364$ referenced images can be located locally. These reference counts come from the focused audit in the existing report, not automatic manifest statistics or a newly run audit.

Paper `full_text` sometimes repeats individual table facts but does not guarantee complete cell data. Targeted sampling found both cases where body text could answer and cases where evidence appeared only in missing table images. This limits evidence recall from body passages. `FLOAT SELECTED: ` is an observed evidence marker, but it has not been mapped to a specific figure or table item. Targeted examples cannot estimate overall QA coverage.

## 7. Deliverables, Reproduction, and Conclusion

| Artifact | Role | Source, state, or reproduction entry point |
| --- | --- | --- |
| `data/raw/qasper/manifest.json` | Pinned input version, split rows, and hashes. | Generated during download; present locally. The raw data directory is not in Git. |
| `data/processed/qasper_inspection.json` | Split structure and anomaly counts. | Generated by `scripts.inspect_qasper`; the inspection document records SHA-256 `deff21fdc2297dbd5b23299f243a214e4d92bd8b26cd544d6d1e0d6184f7f81a`, but the file is not currently retained. |
| `data/processed/papers.jsonl`, `qa.jsonl`, `qasper_export.manifest.json` | Separated paper/question export and its counts, links, and hashes. | Generated by `scripts.export_qasper`; present locally in the ignored processed-data directory. |
| `data/processed/sample_passages_100.jsonl` and its manifest | 100-item interface sample with selection, counts, and hash. | Generated by `scripts.build_sample_passages`; present locally. |
| `data/processed/passages.jsonl` and `passages.manifest.json` | Existing `development` corpus baseline. | Files and manifest are not retained; `data/README.md` records reproducible baseline counts and hash. |
| `data/processed/passages_all_paper_text.jsonl` and its manifest | Inference index built from paper text across all three splits. | Generated by `scripts.build_corpus --scope all-paper-text`; present locally and restricted to inference indexing. |

The complete field and command details are in [`data/README.md`](../../data/README.md). Run the following commands from the repository root to reproduce the pinned inputs, sample, and both corpus scopes. The example uses new output names; the acquisition directory, export files, sample, and corpus output paths must not already exist. Use unused names for another reproduction. Reproduction downloads and generates local data; these commands were not run while editing this report.

```powershell
# Download the pinned QASPER revision.
python -m scripts.download_qasper --output-dir data/raw/qasper-week1-reproduction --revision fdc9d8214fbab5dd782958601db4d678e6934a54
# Inspect the raw data structure and save a report.
python -m scripts.inspect_qasper --input-dir data/raw/qasper-week1-reproduction --output data/processed/qasper_inspection_week1_reproduction.json
# Export papers, questions, and the manifest separately.
python -m scripts.export_qasper --input-dir data/raw/qasper-week1-reproduction --papers-output data/processed/papers_week1_reproduction.jsonl --qa-output data/processed/qa_week1_reproduction.jsonl --manifest-output data/processed/qasper_export_week1_reproduction.manifest.json
# Check the export files, counts, and links.
python -m scripts.check_qasper_export --papers data/processed/papers_week1_reproduction.jsonl --qa data/processed/qa_week1_reproduction.jsonl --manifest data/processed/qasper_export_week1_reproduction.manifest.json
# Build the 100-passage sample.
python -m scripts.build_sample_passages --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --output data/processed/sample_passages_100_week1_reproduction.jsonl --manifest-output data/processed/sample_passages_100_week1_reproduction.manifest.json
# Build the Passage collection for development from paper text in `train` and `validation`.
python -m scripts.build_corpus --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --scope development --output data/processed/passages_development_week1_reproduction.jsonl --manifest-output data/processed/passages_development_week1_reproduction.manifest.json
# Check the development corpus.
python -m scripts.check_corpus --corpus data/processed/passages_development_week1_reproduction.jsonl --manifest data/processed/passages_development_week1_reproduction.manifest.json
# Build the all-paper-text corpus.
python -m scripts.build_corpus --papers data/processed/papers_week1_reproduction.jsonl --export-manifest data/processed/qasper_export_week1_reproduction.manifest.json --scope all-paper-text --output data/processed/passages_all_paper_text_week1_reproduction.jsonl --manifest-output data/processed/passages_all_paper_text_week1_reproduction.manifest.json
# Check the all-paper-text corpus.
python -m scripts.check_corpus --corpus data/processed/passages_all_paper_text_week1_reproduction.jsonl --manifest data/processed/passages_all_paper_text_week1_reproduction.manifest.json
```

Raw data and generated JSONL/manifest files under `data/raw/` and `data/processed/` are excluded from Git. Teammates can reproduce them locally using `data/README.md` and the commands above. This report records artifact names, counting rules, and provenance hashes without including question, answer, evidence, or large sample content.

The data foundation produced this week consists of reproducible acquisition and inspection for a pinned release, complete separation of paper and question exports, an eight-field `Passage` builder that reads paper text only, the 100-passage dependency sample, the development-corpus baseline above the course size threshold, and an all-paper-text inference index. Current limitations are missing image files and incomplete table text, unoptimized chunk parameters, and a `Passage` interface and split-role mapping still marked `v0-proposed`; targeted figure/table examples do not establish overall coverage.
