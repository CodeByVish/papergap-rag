# QASPER Dataset Inspection

This report describes the local QASPER acquisition inspected by `scripts.inspect_qasper`. It is generated from the four files under `data/raw/qasper/` and does not download, normalize, clean, chunk, or rewrite source data.

## Provenance

The inspected dataset is `allenai/qasper`, configuration `qasper`, source dataset version `0.3.0`, and resolved revision `fdc9d8214fbab5dd782958601db4d678e6934a54`. The source license recorded by the acquisition is `CC BY 4.0`; the Hub card records `cc-by-4.0`.

The input split fingerprints recorded in the manifest and revalidated by the inspector are:

| Split | Rows | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `train` | 888 | 29,564,540 | `7a25389963d05d97de9462d4e46b2ef367f37b898de55f5833bae7aa4b6e8732` |
| `validation` | 281 | 10,379,828 | `f3e8f8072bbb42c6f770cdbc311672738683505eef401a7b75e0c08cfb7c5945` |
| `test` | 416 | 16,326,418 | `308380c3da5287ac450582c457a9a75303b8361360dd88e727afd021c8320779` |

The deterministic machine report is `data/processed/qasper_inspection.json`. Its SHA-256 is `deff21fdc2297dbd5b23299f243a214e4d92bd8b26cd544d6d1e0d6184f7f81a`.

## Counting definitions

- `paper_count` is the number of successfully parsed non-empty JSONL lines.
- `question_count` is the sum of the lengths of all papers' `qas` lists.
- `answer_annotation_count` is the sum of the lengths of all questions' `answers` lists. Fields inside one answer annotation and evidence items are not separate annotations.
- Unique ID counts include only non-blank string values. Malformed values remain in anomaly counts.
- Paragraph duplicate comparison uses exactly `paragraph.strip()`, preserving case, internal whitespace, punctuation, and Unicode. Blank paragraphs are excluded.
- `chapter_count` counts `full_text` list items. `paragraph_count` counts entries in list-typed `paragraphs` fields, including blank and non-string entries; `paragraph_string_count` counts string entries only.
- Answer types use this mutually exclusive precedence: `unanswerable is True`, boolean `yes_no`, at least one non-blank extractive span, non-blank `free_form_answer`, and otherwise `invalid_or_empty`. `ambiguous_payload` is counted separately when more than one valid payload is present.

## Split counts

| Split | Papers | Unique papers | Questions | Unique questions | Answer annotations | Per-question annotations (min / median / max) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `train` | 888 | 888 | 2,593 | 2,593 | 2,675 | 1 / 1 / 2 |
| `validation` | 281 | 281 | 1,005 | 1,005 | 1,764 | 1 / 2 / 3 |
| `test` | 416 | 416 | 1,451 | 1,451 | 3,554 | 1 / 2 / 6 |
| Total | 1,585 | 1,585 | 5,049 | 5,049 | 7,993 | Not applicable |

## Observed field structure and anomalies

Every successfully parsed paper record was checked for `id`, `title`, `abstract`, `full_text`, `qas`, and `figures_and_tables`. The expected types observed in the acquisition are string for `id`, `title`, and `abstract`, and list for the other three fields.

No top-level field was missing, `null`, or of the wrong type. Empty-list observations were `full_text=1` in `train` and `figures_and_tables=20` in `train`, `6` in `validation`, and `8` in `test`.

There were `21,909` chapters and `81,502` paragraph entries, all of which were strings. The observed chapter and paragraph conditions were `section_name` empty after stripping in `8` chapters, `section_name` null in `12` chapters, empty `paragraphs` lists in `12` chapters, zero-paragraph chapters in `12` chapters, and blank paragraph strings in `1,537` entries. No chapter item or paragraph item had a wrong type.

All question objects, `question`, `question_id`, and `answers` fields were structurally valid in the observed data. No blank question, blank or duplicate `question_id`, missing answer annotations, or malformed question/answer nesting was observed. Among answer payload fields, `yes_no=null` occurred `6,883` times and was treated as the observed nullable representation; empty `evidence`, `extractive_spans`, `free_form_answer`, and `highlighted_evidence` lists or strings occurred `1,023`, `3,851`, `6,062`, and `998` times respectively.

## Answer types

| Split | Unanswerable | Yes/no | Extractive | Free-form | Invalid or empty | Ambiguous payload |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `train` | 281 | 409 | 1,363 | 622 | 0 | 0 |
| `validation` | 163 | 208 | 962 | 431 | 0 | 0 |
| `test` | 366 | 493 | 1,817 | 878 | 0 | 0 |
| Total | 810 | 1,110 | 4,142 | 1,931 | 0 | 0 |

## Evidence representation

For both `evidence` and `highlighted_evidence`, the inspector reports total items, blank items, non-string items, annotations containing at least one item, `FLOAT SELECTED` hits, the observed prefix forms, the number of hit papers, and the number of `figures_and_tables` items in those hit papers.

The only observed `FLOAT SELECTED` prefix form was `FLOAT SELECTED: `. No evidence string was mapped to a particular figure or table.

| Split | Evidence items | Evidence annotations | Evidence blank / non-string | Evidence hits | Highlighted items | Highlighted annotations | Highlighted blank / non-string | Highlighted hits | Hit-paper figures/tables |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `train` | 4,209 | 2,308 | 0 / 0 | 386 | 3,579 | 2,317 | 2 / 0 | 386 | 1,975 |
| `validation` | 2,808 | 1,552 | 0 / 0 | 253 | 2,330 | 1,555 | 0 / 0 | 253 | 904 |
| `test` | 5,744 | 3,110 | 0 / 0 | 459 | 4,797 | 3,123 | 6 / 0 | 460 | 1,399 |
| Total | 12,761 | 6,970 | 0 / 0 | 1,098 | 10,706 | 6,995 | 8 / 0 | 1,099 | 4,278 |

The hit-paper counts are `250`, `114`, and `188` for `train`, `validation`, and `test`, respectively, for `552` unique hit papers globally. The figure/table count in the final column is the sum for papers with a hit within that split; a cross-split paper mapping is not inferred because the official paper sets are disjoint.

## Duplicate paragraphs

Using the fixed `paragraph.strip()` comparison key, the inspector found `348` same-paper duplicate groups involving `1,006` paragraph occurrences. It found `184` cross-paper duplicate groups involving `766` paragraph occurrences across `259` papers. The report retains at most ten stable coordinate examples per anomaly category and never stores paragraph text in the machine-readable output.

## Split overlap

The three paper-ID intersections were all empty: `train`/`validation`, `train`/`test`, and `validation`/`test`. Each split also had no duplicate `paper_id`, so the observed official split is paper-disjoint. The three cross-split `question_id` intersections were also empty.

This is an observation about the distributed split labels only. It is not an automatic decision that the official `train`, `validation`, and `test` names are the project's development, validation, and held-out policy.

## Reproduction and limitations

Run the following command from the repository root after the local acquisition is present:

```powershell
python -m scripts.inspect_qasper --input-dir data/raw/qasper --output data/processed/qasper_inspection.json
```

The command first requires exactly `manifest.json`, `train.jsonl`, `validation.jsonl`, and `test.jsonl`, then validates manifest hashes and row counts before parsing records. Invalid JSON, non-object top-level records, and critical nested failures stop the inspection instead of silently dropping data.

The report records the observed nested sequence representation already produced by the Step 2 local parser: `full_text` is a list of chapter records and each chapter exposes `section_name` and `paragraphs` fields. It does not define a `Passage` schema, normalize text, select a chunk size, map `FLOAT SELECTED` strings to figure/table indices, or freeze a development/validation/held-out policy. The related open decisions are tracked as `P3-D001` through `P3-D005` in `docs/REQUIREMENTS.md`; this report records observations only.
