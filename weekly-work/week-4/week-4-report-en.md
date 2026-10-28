# Week 4 Work Report

**English** | [简体中文](week-4-report-zn-CN.md)

Status as of 2026/10/28

## Paper catalog for UI selection

Completed a lightweight paper catalog builder that extracts paper metadata from `data/processed/papers.jsonl` and combines it with `data/processed/passages.jsonl`, the passage corpus used by the current configuration, to produce paper and section lists for the UI to load once. The catalog includes only papers and sections that have passages; retrievable here means that passages are available for retrieval, without guaranteeing a match for every query. UI integration is not yet complete.

### Code involved

| Code path | Responsibility |
| --- | --- |
| `src/data/build_paper_catalog.py` | Provides `build_paper_catalog()`, reads papers and passages, validates unique IDs, nonempty text and paper/section references, and aggregates passage counts for each paper and section. |
| `scripts/build_paper_catalog.py` | Provides the command-line entry point, requires an explicit `--passages` argument, writes UTF-8 JSON, and refuses to overwrite an existing output. |
| `tests/data/test_paper_catalog.py` | Contains $9$ tests covering source order, merging sections with the same name, missing metadata, an empty corpus, duplicate IDs, invalid references, empty text and output protection. |

### Output and fields

The local output, `data/processed/paper_catalog.json`, contains $1{,}168$ selectable papers and $16{,}187$ paper/section-name entries, covering all $21{,}360$ passages in the selected corpus. The generated file remains ignored by Git; no data Release was published as part of this work.

The catalog has the top-level fields `schema_version`, `passages_file` and `papers`. The schema remains `v0-proposed`, and `passages_file` records the corpus used for this build, `data/processed/passages.jsonl`. Each paper contains `paper_id`, `title`, `authors`, `passage_count` and `sections`; each section contains `name` and `passage_count`. Field types and meanings, build commands, and local reproduction/Release usage workflows are documented in the [catalog section in English](../../data/README.md#dataprocessedpaper_catalogjson) in `data/README.md` and the [corresponding section in Chinese](../../data/README_zh-CN.md#dataprocessedpaper_catalogjson) in `data/README_zh-CN.md`.

Sections follow their first occurrence in the source text. Sections with the same normalized name are merged and their passage counts combined; section counts sum to the paper count. Missing or blank strings use `null`, and missing author lists use `[]`, without inferring unavailable values; the current QASPER export does not provide authors. UI retrieval must use the same corpus recorded in `passages_file`, and the catalog must be rebuilt whenever that corpus is replaced.

### Verification results

The saved catalog and passage corpus were read independently to verify unique paper IDs, consistent passage counts for every paper and section, and complete coverage of the total passage count. All $9$ new tests and all $530$ tests in the full suite passed; character, Python syntax and Ruff checks also passed. The full-suite command below explicitly uses a temporary directory inside the repository to avoid access restrictions affecting the old temporary directory:

```powershell
python -m pytest tests -q --basetemp tmp/tmp_pytest_week4_catalog --tb=short
```
