# Local QASPER data

Generated or downloaded data stays out of Git. Do not commit `data/raw/`, source archives, Hugging Face cache files, staging directories, or other locally generated data.

## Scope and data shape

The acquisition command downloads the uncleaned, unchunked, paper-level QASPER source data as JSONL. Each JSONL line represents one paper record.

The source members `train`, `dev`, and `test` are published as `train.jsonl`, `validation.jsonl`, and `test.jsonl`, respectively. The acquisition stage does not clean or chunk these records; the later sections document the current proposed Passage contract, deterministic chunking behavior, and the 100-passage dependency sample.

## Passage ID contract

The passage ID is an opaque, deterministic identifier. Its public constructor is `make_passage_id(*, context, paper_id, source_kind, section_index, chunk_index) -> str` from `src/data/passage_ids.py`; callers must provide every argument explicitly.

The immutable context is `PassageIdContext(dataset_id, resolved_revision, local_parser_version, normalization_version, chunking_version, chunk_size_words, chunk_overlap_words)`. Production QASPER configuration uses `dataset_id="allenai/qasper"`, a full lowercase 40-character `resolved_revision`, positive integer `local_parser_version`, non-empty version strings, positive `chunk_size_words`, and `0 <= chunk_overlap_words < chunk_size_words`.

The canonical payload has exactly four top-level keys: `scheme`, `dataset`, `transform`, and `coordinate`. `dataset` contains `dataset_id`, `resolved_revision`, and `local_parser_version`; `transform` contains `normalization_version`, `chunking_version`, `chunk_size_words`, and `chunk_overlap_words`; `coordinate` contains `paper_id`, `source_kind`, `section_index`, and `chunk_index`. The implementation serializes this payload with UTF-8 `json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)` and hashes the complete bytes with SHA-256.

The final format is `qasper-passage-v1-<64 lowercase hex characters>`. `qasper-passage-v1` is `PASSAGE_ID_SCHEME_VERSION`; the digest is not truncated. Consumers must treat the value as opaque and read metadata from the `Passage` record or corpus manifest instead of parsing the ID.

P2 uses `passage_id` for duplicate removal, P5 uses it for citations, and `previous_passage_id`/`next_passage_id` use the same generated values for neighboring links. The ID function itself does not query or validate other records.

`section_index` is the zero-based position of the source container before filtering empty or unselected containers. `chunk_index` is the zero-based position emitted by the deterministic chunker within that source container. The allowed `source_kind` values are `full_text`, `abstract`, and `figure_table`; `full_text` and `figure_table` use their source-list positions, while `abstract` uses index `0`. The allowed source kinds reserve unambiguous ID coordinates; only source types approved by the team may generate passages.

The ID includes the immutable source revision, parser version, normalization version, chunking version, chunk configuration, paper ID, source kind, and source coordinates. It excludes display titles, section names, passage text, source split, output order, file paths, run time, and machine state. Therefore, `source_split` is not part of passage identity; the corpus manifest and output hash identify the complete generated collection.

Any normalization or chunking change that can alter passage bytes must increment its version string. Changes to the canonical payload, field meanings, hash method, or output prefix require a new `PASSAGE_ID_SCHEME_VERSION`; old and new IDs are not assumed compatible. The passage ID function does not generate passages, choose abstract or figure/table indexing policy, fill neighbor links, or map evidence.

For a synthetic context with `paper_id="paper-a"`, `source_kind="full_text"`, `section_index=2`, and `chunk_index=3`, the resulting ID is `qasper-passage-v1-fe1214d2ab869911e267500cd9b8903dc8e3d4d1e66bde218d0bcc938da8c6ee`.

## Passage sequence contract

The passage sequence contract is `v0-proposed` and defines the public meaning of `chunk_number` and the two neighbor fields without adding deferred provenance fields to `Passage`; the provenance-field question is tracked as `P3-D001` and remains pending team review.

`chunk_number` is equal to the `chunk_index` passed to `make_passage_id`. It is a zero-based, contiguous position within one source-container sequence, so a sequence containing $N$ passages must have exactly the positions `0..N-1`. The sequence boundary is the internal coordinate `(paper_id, source_kind, section_index)`, and numbering resets to `0` at every boundary. For `source_kind="full_text"`, every original `full_text[section_index]` is a separate sequence; `abstract` and each `figure_table` container follow the same rule if those source kinds are approved for indexing.

`previous_passage_id` and `next_passage_id` refer only to the direct predecessor and successor after ordering by `chunk_number` within the same source-container sequence. Non-null links must point to an existing passage and be mutual reverse links. A source container that is blank, invalid, or not approved produces no records; the builder must not create holes, renumber silently, or link around a missing passage. The public model does not attempt to validate these collection-level conditions because `source_kind` and `section_index` are internal construction coordinates.

At sequence boundaries, the missing neighbor is Python `None` and serializes as an explicit JSON `null`. Empty strings, missing keys, sentinel values, self-links, dangling IDs, and cross-container links are invalid representations of a missing neighbor.

The following synthetic examples illustrate the contract:

1. A three-passage sequence in one source container uses `0 -> 1 -> 2`; the first record has `previous_passage_id=null`, and the last has `next_passage_id=null`.
2. When the next `full_text` section begins, its first passage restarts at `chunk_number=0`; the last passage of the previous section and the first passage of the next section both have `null` at their respective outer boundaries.
3. A single-passage source container has `chunk_number=0`, `previous_passage_id=null`, and `next_passage_id=null`.
4. Two source containers may display the same `section` string, but their records remain separate sequences and must not link to one another; each sequence starts at `0` and uses `null` at its own boundaries.

This contract does not decide whether abstract or figure/table containers will actually be indexed, nor how `FLOAT SELECTED` evidence will map to figure/table passages. These open questions are tracked as `P3-D002` and `P3-D003`.

## Passage chunk-boundary contract

The `Passage` chunk-boundary contract is `v0-proposed`. Every passage must be produced from exactly one internal source container identified by `(paper_id, source_kind, section_index)`. The normalized `text` may contain multiple source paragraphs only when they belong to that same container and remain in their original order.

A change in `paper_id` is always a hard boundary. Different `source_kind` values are also isolated and must never be merged. For `source_kind="full_text"`, each original `full_text[section_index]` list item is a separate source container, even when adjacent list items have the same display title. If the team later approves `abstract` or `figure_table` indexing, the abstract container and every individual figure/table container remain separate boundaries as well.

The initial rule does not infer relatedness from section-title text, semantic similarity, or title hierarchy. A missing or blank title does not relax the boundary, and equal titles do not merge containers. A word chunker may combine source paragraphs in their original order within one source container, but it must not join the final text of one container to the first text of another to reach a target size. Retrieval should return multiple passages when cross-section context is needed.

This chunk boundary is stricter than the item 3 adjacency boundary, although both use the same internal coordinate. Chunking decides which source text may enter one passage; adjacency decides which already-created passages may receive direct neighbor links. Neither rule may be inferred from output-file order or the display value of `section`.

Step 5 must enforce this contract through a builder interface that accepts one source container together with its `(paper_id, source_kind, section_index)` coordinate, preserves paragraph order, and then invokes the word-level chunker. Callers must not pass a string assembled from multiple source containers. Step 7 must add collection-level negative tests using synthetic records with two papers, two sections, repeated section titles, and blank section titles to prove that no output passage crosses a hard boundary. The single-record `Passage` model only declares the text-source precondition; it cannot verify these internal coordinates.

Whether abstract or figure/table containers will actually be indexed remains a team decision. This contract also does not define `FLOAT SELECTED` evidence mapping; the mapping remains `P3-D003` pending team review.

## Normalization and chunking contract

The Step 5 implementation is in `src/data/chunking.py`. The current provisional configuration is `normalization_version="text-normalization-v1"`, `chunking_version="word-chunking-v1"`, `chunk_size_words=200`, and `chunk_overlap_words=40`. Week 3 must compare `$150`, `$200`, and `$250` chunk sizes using development and validation data before selecting a working setting.

Normalization is deliberately conservative. For each source paragraph, the builder replaces CRLF and lone CR line endings with LF, removes only leading and trailing Unicode whitespace, drops paragraphs that become empty, and leaves internal whitespace, punctuation, casing, Unicode content, paragraph order, and evidence-marker text unchanged. Section names and paper titles receive the same line-ending and outer-whitespace treatment; a blank or `null` section name is dropped rather than replaced with a guessed label, and a blank paper title causes that paper to produce no passages. The returned `NormalizationReport` records paragraph and section counts, dropped blanks or `null` section names, line-ending replacements, outer-whitespace trims, and invalid-paper drops so a corpus manifest can preserve the observed transformations.

The word rule is the number of Unicode-aware non-whitespace runs matched by `\\S+`. A chunk window contains at most `chunk_size_words` runs; the next window starts `chunk_size_words - chunk_overlap_words` runs later. Chunk text is the original normalized character span from the first selected run through the last selected run, so internal whitespace and punctuation are not reconstructed or collapsed. Paragraphs are joined only with an internal LF-LF separator inside one source container, and the private build result retains the original paragraph indices touched by each chunk.

`build_passages_from_record` reads only `id`, `title`, and `full_text`. It never reads `qas`, answers, evidence, highlighted evidence, or figure/table metadata. Each original `full_text[section_index]` is processed independently, including sections with repeated or blank display names. Empty sections do not cause later sections to be renumbered: the original `section_index` remains in the passage ID coordinate. The current public record builder generates `full_text` passages only; abstract and figure/table sources remain deferred team decisions.

`build_passages_from_records` produces a deterministic order by `paper_id`, source kind, original section index, and chunk index. The private coordinate is `(paper_id, source_kind, section_index, chunk_index)`, while the public `Passage` remains the eight-field contract. Neighbor links are filled only within one `(paper_id, source_kind, section_index)` sequence, and `validate_built_passages` rejects duplicate IDs, empty text, missing chunk numbers, dangling links, and non-mutual or cross-container adjacency. The builder never infers boundaries from output order or display section names.

## Unified paper and QA exports

The local data flow is: verify the fixed-revision download; export one combined paper file, one combined question file, and a manifest; build development passages, the 100-passage sample, or an all-paper-text inference index from the paper file; then select questions and answers from the QA file under the evaluation protocol. The source `data/raw/qasper/` files and manifest remain unchanged.

`papers.jsonl` has one record per paper in `train`, `validation`, `test` order and preserves every original top-level field except `qas`; it adds only `source_split`. `qa.jsonl` has one record per question, retains the complete original question object and `answers` array, and adds `paper_id` and `source_split`. It contains all three source splits. Neither the paper builder nor the paper loader opens `qa.jsonl`.

`qasper_export.manifest.json` records the pinned source metadata, source manifest hash, input split hashes and row counts, output filenames and hashes, counts by source split, and the current `v0-proposed` split policy version. Output filenames in the manifest are basenames and all three export files share one directory. The JSONL outputs use deterministic compact JSON, UTF-8 without a BOM, and LF line endings. Generated files under `data/processed/` are ignored by Git.

Export and independently verify the combined files with:

```powershell
python -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
python -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
```

The export command and structural checker may read `test` records mechanically to project fields, calculate hashes and counts, and verify links. Their summaries contain no question or answer text. People and experiment code must not preview or use `test` questions, answers, evidence, or labels before the evaluation freeze. A future evaluation entry point must first expose only `question_id`, `paper_id`, and `question` to RAG, persist query results, and read `answers` and evidence separately for scoring after inference.

The export command refuses any existing target. If publication is interrupted before the manifest is present, inspect the partial files manually before choosing new output names. It uses `tmp_` sibling files while staging; it does not silently replace an existing export.

## 100-passage dependency sample

Build the sample from the verified paper-only export:

```powershell
python -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
```

The builder selects only `train` and `validation`, uses `full_text`, selects complete source-container sequences with a stable paper-ordered subset-sum rule, and validates each output record with `Passage`. The generated JSONL contains exactly `100` passages from `100` papers. For the pinned source revision and default $200$-word chunks with $40$-word overlap, its expected SHA-256 is `d017b7937d2e9a54ee653c8a3a94f37afa2819d548c0f79eacc93f08832bdb42`. The manifest records the export papers hash and source split hashes. Existing outputs are rejected; choose new output names when rebuilding for comparison.

## Full development corpus and rubric check

Build the default development corpus and independently check its published passage file:

```powershell
python -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
python -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
```

The default `development` scope processes only `train` and `validation`. The alternate `--scope all-paper-text` also processes `test` paper bodies and labels its output purpose as `index_for_inference`; use distinct output filenames and never use that corpus as tuning or prompt-design material. Both scopes enforce at least $10{,}000$ passages and $100{,}000$ source words. The manifest records the chosen scope, export papers SHA-256, and paper and passage counts by official source split. The checker validates the generated passage file and its manifest without needing the export inputs.

For the pinned source revision and default $200$-word chunks with $40$-word overlap, the current development baseline is $1{,}169$ source papers, $1{,}168$ indexed papers, $32{,}073$ unique passages, $4{,}262{,}446$ source words, $4{,}897{,}846$ passage words, and $174{,}636$ case-folded passage word types. Its expected passage SHA-256 is `abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`. Word counts use Unicode non-whitespace runs. Existing output paths are never overwritten; use new filenames to compare a rebuild. These counts describe the current development scope and do not freeze the team's split or source-kind decisions.

## Proposed split policy

The split policy is `qasper-official-paper-disjoint-v0-proposed` and applies at the whole-paper level. The proposal maps the official source splits exactly as `train -> development`, `validation -> validation`, and `test -> held_out`. The official split name and project role are both retained in corpus or experiment manifests; neither `source_split` nor the project role is part of a single `Passage` identity.

The proposal is supported by the deterministic inspection report for resolved revision `fdc9d8214fbab5dd782958601db4d678e6934a54`: `train`, `validation`, and `test` contain `888`, `281`, and `416` papers, respectively; each split has zero duplicate paper IDs; all three pairwise paper-ID intersections are empty; and the report records `observed_paper_disjoint: true`. These are review evidence, not hard-coded runtime counts.

The paper-level invariant is strict: a paper's title, text, questions, answers, evidence, and all passages derived from that paper stay in one project role. The policy does not split or rebalance papers by question or passage, and it does not claim that the official names are model-training semantics. `validate_paper_disjoint_splits` in `src/data/split_policy.py` requires exactly the three official split keys, clean non-empty paper IDs, no within-split duplicates, and no cross-split overlap; it reads no files and does not modify its input.

The configuration is still a proposal under `P3-D004`, pending P5/P6 review. `evaluation.held_out_manifest: null` means that the held-out question and annotation pool has not been created; it is not permission to sample from `test` for tuning. Any future remapping must increment the policy version and repeat the paper-leakage check. The `Passage` schema and passage ID remain unchanged, while corpus manifests must record the source split, project role, policy version, chunking configuration, and relevant output hashes.

## Held-out asset-use policy

The policy distinguishes the assets `paper_text`, `question`, `answer`, and `label` from the purposes `index_for_inference`, `tuning`, `prompt_design`, `chunk_selection`, and `final_evaluation`. `label` includes human relevance labels and supervision derived from answers or evidence; `prompt_design` includes template wording, few-shot example selection, and critic or generator prompt iteration.

The complete policy matrix is:

| Project role | Asset | `index_for_inference` | `tuning` | `prompt_design` | `chunk_selection` | `final_evaluation` |
| --- | --- | --- | --- | --- | --- | --- |
| `development` or `validation` | `paper_text`, `question`, `answer`, `label` | Allowed | Allowed | Allowed | Allowed | Allowed |
| `held_out` | `paper_text` | Allowed | Forbidden | Forbidden | Forbidden | Forbidden |
| `held_out` | `question` | Forbidden | Forbidden | Forbidden | Forbidden | Allowed after freeze |
| `held_out` | `answer` or `label` | Forbidden | Forbidden | Forbidden | Forbidden | Allowed after freeze |

`src/data/split_policy.py:assert_data_use_allowed` is the machine-readable guard. Every caller must provide `evaluation_frozen` explicitly as a boolean; held-out questions may be used only as final evaluation queries after freeze, and held-out answers or labels may be used only for final scoring and reporting after freeze. The guard does not infer freeze state from a date, branch, file, or environment variable.

Development and validation assets may support tuning, prompt design, and chunk-selection decisions, but those decisions must be recorded and frozen before any held-out evaluation asset is read. Permission to use development or validation supervision for an experiment does not permit writing questions, answers, evidence, worker IDs, annotation IDs, or labels into the retrieval passage corpus.

## Held-out index sanitization

Held-out paper text may be indexed for inference evidence only. Before normalization or chunking, a passage builder that receives a complete QASPER paper record must construct an internal view from an explicit allowlist of team-approved paper-content fields; it must exclude `qas` and all nested `question`, `answers`, `evidence`, `highlighted_evidence`, `worker_id`, and `annotation_id` fields. Indexing held-out paper text does not authorize use of the supervision fields distributed in the same source record.

Corpus manifests must record the source split, project role, `SPLIT_POLICY_VERSION`, chunking configuration, and relevant output hashes, while a single `Passage` must not gain a split field. The held-out or annotation manifest must remain separate from the retrieval corpus and preserve the freeze commit and configuration used to create it; its creation is tracked as `P3-D005`.

The current `data.split_policy.held_out_usage` configuration records `index_paper_text: true`, forbids `tuning`, `prompt_design`, and `chunk_selection`, and requires an explicit frozen state for final evaluation. `evaluation.held_out_manifest: null` means that the question pool has not been created; it is not permission to sample temporary held-out questions for tuning. The freeze-record and rerun rules remain `P3-D005` and `P3-D006` pending team review.

## Requirements

Run the command from the repository root with the project Python 3.11 environment. Install the project dependencies first, for example with `python -m pip install -r requirements.txt` or `python -m pip install -r requirements-dev.txt`.

## Reproducible local workflow

Run the following commands from the repository root in order. The commands use repository-relative paths and do not depend on a local shell variable or a hidden configuration file.

1. Download the pinned acquisition: `python -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54`.
2. Inspect the existing acquisition without network access: `python -m scripts.inspect_qasper --input-dir data/raw/qasper --output data/processed/qasper_inspection.json`.
3. Export and structurally verify the combined files using the commands in [Unified paper and QA exports](#unified-paper-and-qa-exports).
4. Build the 100-passage dependency sample using the command in [100-passage dependency sample](#100-passage-dependency-sample), or build a passage corpus as described in [Full development corpus and rubric check](#full-development-corpus-and-rubric-check).

The download command requires `--output-dir`; `--revision` defaults to the pinned commit SHA and `--force` is required to replace an existing acquisition directory. The inspection command requires `--input-dir` and `--output`, creates the report parent directory, and replaces the report at the requested output path; it has no `--force` flag. Before writing a report, it requires exactly `manifest.json`, `train.jsonl`, `validation.jsonl`, and `test.jsonl`, verifies split hashes and row counts, and stops on invalid JSON or critical nested structure errors. `download_qasper` and `inspect_qasper` still take the raw acquisition directory. The `build_corpus` and `build_sample_passages` commands now take `--papers` and `--export-manifest`; their former `--input-dir` form has been replaced. Generated export, sample, and passage outputs reject existing names, so use new names when rebuilding for comparison.

The acquisition requires network access to the Hugging Face Hub and the official QASPER source archives. QASPER is public data; do not configure or provide a Hugging Face token for this command.

## Reproducible acquisition

The recommended team command pins the supported QASPER source revision explicitly:

```powershell
python -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54
```

If `--revision` is omitted, the CLI uses the same fixed commit SHA as its default. Team reproductions should still pass the SHA explicitly so that the intended source version is visible in the command.

The command resolves the requested branch, tag, or SHA to a full commit SHA and records both values in `manifest.json`. The acquisition only accepts the fixed source profile supported by the local parser.

## Command-line options

| Option | Required | Behavior |
| --- | --- | --- |
| `--output-dir PATH` | Yes | Destination directory for the published acquisition, such as `data/raw/qasper`. |
| `--revision REVISION` | No | Hub branch, tag, or commit SHA to resolve. The default is `fdc9d8214fbab5dd782958601db4d678e6934a54`; both requested and resolved revisions are recorded in the manifest. |
| `--force` | No | Replace an existing destination only after the new result has been completely staged, verified, serialized, and given a valid manifest. |

Without `--force`, an existing output directory is rejected before downloading. `--force` is a whole-directory replacement operation, not an append, resume, or partial-overwrite operation. The previous directory is retained until the new directory is published successfully, with rollback on a publish failure.

## Successful output

On success, the output directory contains exactly these four files:

```text
data/raw/qasper/
├── train.jsonl
├── validation.jsonl
├── test.jsonl
└── manifest.json
```

The JSONL files use UTF-8 encoding, LF newlines, recursively sorted JSON keys, compact JSON separators, and one record per line. Use `manifest.json` as the authority for the observed row counts, byte counts, and SHA-256 digests; this document does not provide machine-specific download results.

The CLI prints the output directory, resolved revision, split row counts, and aggregate SHA-256 after a successful publication. The aggregate digest covers the relative path and individual SHA-256 of each JSONL file in lexicographic path order; `manifest.json` is not included.

## Manifest reference

`manifest.json` is deterministic metadata for the acquisition and contains no timestamp, username, hostname, absolute path, cache path, token, environment variable, or complete environment dump.

| Top-level field | Contents and purpose |
| --- | --- |
| `manifest_schema_version` | Version of the manifest field contract. |
| `dataset` | Dataset ID and configuration, `requested_revision`, resolved immutable `resolved_revision`, supported source dataset version, and `local_parser_version`. |
| `licenses` | License information reported by the Hub dataset card and the fixed source metadata. |
| `repository_files` | Observed byte count and SHA-256 for the pinned `qasper.py` and `dataset_infos.json` files. These files are read as ordinary bytes only; they are not imported or executed. |
| `splits` | Output split name, JSONL filename, observed row count, byte count, and individual SHA-256 for `train`, `validation`, and `test`. |
| `source_verification` | Identifier for the source verification contract, including archive SHA-256 checks and required-member checks. |
| `source_archives` | Each official archive URL, declared and observed byte counts, declared and observed SHA-256 values, and the required archive members read by the parser. |
| `libraries` | Runtime Python version and the `huggingface-hub` package version used by the acquisition. |
| `output` | JSONL encoding and newline rules, the aggregate-hash algorithm identifier, and `aggregate_sha256` for the three JSONL files. |

The two official source archives must match their declared byte counts and SHA-256 values. The parser reads only the explicitly whitelisted root members and does not extract the archive to disk. If the source version, archive URL, checksum, required member, repository-file fingerprint, or supported schema changes, the acquisition fails closed instead of guessing a new format.

## Source safety and reproducibility

The Hub copies of `qasper.py` and `dataset_infos.json` are downloaded only to validate fixed source metadata and fingerprints. The acquisition never imports or executes the Hub `qasper.py`, uses `trust_remote_code`, or relies on a remote dataset loader.

`--revision main` is useful only for actively checking upstream changes and is not the team reproduction command. Even if `main` resolves to a new SHA, the command safely fails when that revision is not supported by the current source profile or parser.

For an experiment reproduction, retain the manifest values for `resolved_revision`, `local_parser_version`, repository-file fingerprints, source-archive fingerprints, split file digests, and `aggregate_sha256`.

## Loading the local JSONL files

The files can be loaded locally with the `datasets` JSON loader. This example uses local paths and does not access the Hub:

```python
import datasets

dataset = datasets.load_dataset(
    "json",
    data_files={
        "train": "data/raw/qasper/train.jsonl",
        "validation": "data/raw/qasper/validation.jsonl",
        "test": "data/raw/qasper/test.jsonl",
    },
)
```

At this point the records are still paper-level raw QASPER records. They are not passage-cleaned, passage-chunked, or converted into the project's later retrieval corpus.

The offline inspection report is a deterministic validation artifact at `data/processed/qasper_inspection.json`. It contains provenance, split counts, field and nested-structure anomalies, answer types, evidence observations, duplicate-paragraph observations, and split-overlap results. The exporter publishes `data/processed/papers.jsonl`, `data/processed/qa.jsonl`, and `data/processed/qasper_export.manifest.json`; the corpus and sample builders publish their passage JSONL files and manifests. All are generated artifacts and remain outside Git.

## Git ignore check and cleanup

Verify that the generated acquisition is ignored before working with it:

```powershell
git check-ignore -v data/raw/qasper/manifest.json
```

The check should match the repository rule for `/data/*`. Keep `data/raw/`, downloaded archives, Hugging Face cache files, staging directories, and other generated data local; remove them when they are no longer needed, subject to any local experiment-retention requirements.
