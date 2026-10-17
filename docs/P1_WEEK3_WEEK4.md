# P1 Week 3 / Week 4: real-data retrieval

Owner: Junlin Yin. This workflow reuses the Week 1/2 BM25 and BGE/FAISS
retrievers. P3 produces the data in a separate worktree; no P3 branch merge is
required. P2 fusion/reranking and the P3/P4/P5/P6 implementations are unchanged.

> Current delivery: [Phase 3 Git delivery and final code validation](#phase-3-git-delivery-and-final-code-validation). Earlier statements that work is uncommitted, the branch is unmerged, or Git delivery is deferred describe their original checkpoints; Phase 3 supersedes those delivery restrictions. Experimental provenance is unchanged. [Phase 2 source review](#phase-2-p2-source-review-and-delivery-entry-points) remains an unpublished P2 review draft, and [eight qualitative cases](#fixed-sample-qualitative-analysis-of-saved-baselines) remain pending human review.

## Data and development convention

The source for this run is P3 commit
`499bb6d8ea2952f10e0499bfb8eb2986d683ba06`, with QASPER revision
`fdc9d8214fbab5dd782958601db4d678e6934a54`. Its split policy is still
`qasper-official-paper-disjoint-v0-proposed`; this is a recorded development
convention, not a claim that the team has frozen the policy.

- Index the complete P3 `development` corpus: train and validation paper text.
- Query only official **train** questions, sorted by `question_id`.
- Do not select validation or test questions for this run. Do not use answers
  or evidence annotations to select, rewrite or score the development queries.
- P3's unchanged acquisition/export commands mechanically produce all official
  splits. The P1 adapter selects train queries and discards QA annotations.
- The adapter checks corpus/export hashes, source revisions, split membership,
  counts, unique IDs, nonempty text, neighbor links and the complete saved index
  mappings before retrieval. It constructs the existing retrieval `Passage`
  model from JSONL without changing IDs or adding fields.

The generated development corpus has **32,073 unique passages** from **1,168
indexed papers**: 24,751 train passages and 7,322 validation passages. There are
1,169 source papers. Chunking uses `full_text`, 200 words and 40-word overlap;
normalization is `text-normalization-v1`, chunking is `word-chunking-v1`.
The corpus SHA-256 is
`abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`.

There are 2,593 train questions. Three reference paper `1801.07804`, which has
no generated passages: both its original and exported record have
`full_text=[]`. P3's full-text chunker therefore emits no passages for this
paper. These questions remain in the experiment and receive explicit zero-hit
records rather than being silently excluded. This is a source-data limitation,
not a paper-filtering failure.

## Reproduce the data preparation

Use Python 3.11. The verified local interpreter is
`E:\Miniconda\py311\envs\papergap\python.exe` (Python 3.11.16). Existing
project dependencies are sufficient; no dependency upgrade is part of this work.

From the P1 repository root, the separate, ignored P3 worktree can be created
at the recorded commit. Reuse an existing matching worktree rather than
overwriting it:

```powershell
git worktree add --detach .cache/p3-week3-week4 499bb6d8ea2952f10e0499bfb8eb2986d683ba06
$p1Python = 'E:\Miniconda\py311\envs\papergap\python.exe'
Push-Location .cache/p3-week3-week4
& $p1Python -B -m scripts.download_qasper --output-dir data/raw/qasper --revision fdc9d8214fbab5dd782958601db4d678e6934a54
& $p1Python -B -m scripts.export_qasper --input-dir data/raw/qasper --papers-output data/processed/papers.jsonl --qa-output data/processed/qa.jsonl --manifest-output data/processed/qasper_export.manifest.json
& $p1Python -B -m scripts.check_qasper_export --papers data/processed/papers.jsonl --qa data/processed/qa.jsonl --manifest data/processed/qasper_export.manifest.json
& $p1Python -B -m scripts.build_sample_passages --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --output data/processed/sample_passages_100.jsonl --manifest-output data/processed/sample_passages_100.manifest.json
& $p1Python -B -m scripts.build_corpus --papers data/processed/papers.jsonl --export-manifest data/processed/qasper_export.manifest.json --scope development --output data/processed/passages.jsonl --manifest-output data/processed/passages.manifest.json
& $p1Python -B -m scripts.check_corpus --corpus data/processed/passages.jsonl --manifest data/processed/passages.manifest.json
Pop-Location
```

Download requires network access. Generated targets must not already exist;
when the verified files are present, reuse them instead of rerunning production
commands over their outputs. P3's `papers.jsonl` is a paper export, not a
Passage input; use the generated `passages.jsonl` for indexing.

## Build and reuse indexes

The model remains `BAAI/bge-small-en-v1.5`, revision
`5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. Only queries receive
`Represent this sentence for searching relevant passages: ` (including the
trailing space). Both vector types use L2 normalization and per-paper FAISS
`IndexFlatIP`. Model maximum sequence length remains 512.

From the P1 repository root:

```powershell
$p1Python = 'E:\Miniconda\py311\envs\papergap\python.exe'
$env:HF_HUB_OFFLINE = '1'
$env:TRANSFORMERS_OFFLINE = '1'
$env:OMP_NUM_THREADS = '4'
$env:MKL_NUM_THREADS = '4'
& $p1Python -B -m scripts.build_indexes --passages .cache/p3-week3-week4/data/processed/passages.jsonl --output-dir indexes/p1-week3-week4-development --local-files-only
```

The pinned model is already cached for the recorded run. On another machine,
allow the first model download by omitting `--local-files-only` and the two
offline environment settings. Use a new or empty index output directory.

Saved FAISS files retain passage embeddings and row mappings; reloading does
not re-encode the corpus. BM25 persistence uses a versioned JSON representation
of the original passages and retrieval settings, and rebuilds the in-memory
term-frequency index on load. It does not use pickle. The experiment creates
and reloads a BM25 artifact on its first run and checks it against the entire
input corpus on subsequent runs.

## Run development retrieval

Use `--limit 3` with a distinct output directory for a small smoke run. Omit
`--limit` to run all train questions against the complete development index:

```powershell
& $p1Python -B -m scripts.run_p1_experiment --passages .cache/p3-week3-week4/data/processed/passages.jsonl --corpus-manifest .cache/p3-week3-week4/data/processed/passages.manifest.json --qa .cache/p3-week3-week4/data/processed/qa.jsonl --export-manifest .cache/p3-week3-week4/data/processed/qasper_export.manifest.json --p3-commit 499bb6d8ea2952f10e0499bfb8eb2986d683ba06 --dense-index-dir indexes/p1-week3-week4-development --bm25-index-dir indexes/p1-week3-week4-bm25 --output-dir results/p1-week3-week4-development --top-k 5 --local-files-only
```

Each experiment output directory must be new or empty. The files are:

| File | Contents |
| --- | --- |
| `results.jsonl` | One row per retrieved passage: question ID, paper ID, query, method, rank, passage ID, score and configuration reference. |
| `queries.jsonl` | One row per question/method, including zero-hit outcomes, status and retrieval latency in milliseconds. |
| `run.json` | Data/model revisions and hashes, P1/P3 commits, working-tree state and P1 source hashes, environment, timing policy and actual counts. |

Timing uses `time.perf_counter()` after one warm-up per retriever. It includes
Dense query encoding and excludes input validation, corpus encoding, model
loading, index loading/construction and output serialization.

## Week 4 callable contract

Both retrievers preserve the existing P2-compatible call:

```python
hits = retriever.retrieve(query, paper_id, top_k)
```

They additionally accept a keyword-only exact section name:

```python
hits = retriever.retrieve(rewritten_query, paper_id, top_k, section="Results")
```

Filtering considers all passages in the selected paper before limiting to K.
Section names are exact and case-sensitive; an unknown section returns `[]`.
Ranks remain one-based, continuous and deterministic. BM25 retains the paper's
term statistics when filtering sections. Query rewriting itself belongs to
the calling agent: P1 accepts the new query without altering it, and does not
implement P4's rewriting policy. The optional keyword does not require changes
to P2's existing callbacks; forwarding section requests through P2 is a
separate owner integration task.

### Section callback handoff to P2/P4

The inspected signature is identical for BM25 and Dense:

```python
retrieve(
    query: str, paper_id: str, top_k: int, *, section: str | None = None
) -> list[RetrievalHit]
```

`section` is keyword-only. Omitting it or passing `None` searches the selected
whole paper. A nonempty string selects an exact, case-sensitive section name;
it is not stripped or normalized (`"Methods"`, `"methods"` and `" Methods "`
are different strings). Empty/whitespace-only strings and non-string values
raise `ValueError`, even for an unknown paper. A valid unmatched section or
unknown paper returns `[]`. Both filters apply before top-K truncation. No
filter is stored as mutable state on either retriever.

Reuse initialized retrievers and bind the section to each request's callbacks:

```python
from functools import partial

from scripts.build_indexes import PINNED_REVISION
from src.retrieval.bm25_retriever import BM25Retriever
from src.retrieval.dense_retriever import DenseRetriever
from src.retrieval.hybrid_retriever import HybridRetriever

# Initialize once from the existing local artifacts (repository-root paths).
bm25 = BM25Retriever.load("indexes/p1-week3-week4-bm25")
dense = DenseRetriever.load(
    "indexes/p1-week3-week4-development",
    revision=PINNED_REVISION,
    device="cpu",
    local_files_only=True,
)
query = "How is the input triple translated to a slot-filling task?"
paper_id = "1706.04115"

# The original callback and direct section-aware calls both remain available.
sparse_hits = bm25.retrieve(query, paper_id, 5)
dense_hits = dense.retrieve(query, paper_id, 5)
sparse_section_hits = bm25.retrieve(query, paper_id, 5, section="Approach")
dense_section_hits = dense.retrieve(query, paper_id, 5, section="Approach")

# Create fresh callbacks when the requested section changes; reuse the indexes.
requested_section = "Approach"  # Use None for a whole-paper request.
hybrid = HybridRetriever(
    partial(bm25.retrieve, section=requested_section),
    partial(dense.retrieve, section=requested_section),
    candidate_k=20,
)
fused_hits = hybrid.retrieve(query, paper_id, top_k=5)
```

The current P2 module calls each callback with `(query, paper_id, candidate_k)`;
its outer `top_k` limits the fused results. Its result type is
`list[RetrievedPassage]`, with the original backend ranks/scores retained in
`source_scores`. The example uses the existing RRF path with `scorer=None`.
Do not mutate shared callback keywords or a shared Hybrid instance to switch
requests; construct a new pair of bindings for the chosen section. This
creates no new BM25/FAISS index and changes no P2 algorithm.

The two bounded handoff tests in `tests/test_p1_week4.py` use **the real
HybridRetriever and fusion implementation**, real BM25/FAISS and a deterministic
fake encoder. They verify both section-bound callbacks, candidate versus final
K, and interleaved queries/papers/sections on the same underlying retrievers.
Returning to an earlier request yields the same complete results. Existing
tests already cover direct section calls and the original unbound callbacks.
This validates the P1/P2 callback boundary; the real-model version of the above
example was not rerun in this handoff pass.

P2's external `retrieve()` still has no `section` keyword. P2/P4 must agree how
to carry a request's exact section (or `None`), current query, paper ID and
requested result count to both backend callbacks. They must preserve the
chosen section only for that request and define their candidate budget.
P4 owns query rewriting and retry policy. Neither a P4-to-P2 application call
nor an agent/reranker end-to-end section run has been verified here.

## Verification and remaining dependencies

In the original real-data implementation session (historical verification),
the unchanged P1/P2 regression suite was rerun:
`python -B -m pytest tests/test_p1.py tests/test_p2.py -q` reported **139 passed**.
The separate real-model smoke used 100 real P3 sample passages and three train
questions. That sample contains only one passage per paper and establishes
pipeline operation, not retrieval quality.

A separate real-corpus BM25 roundtrip checked all 2,593 train questions at
K=5: the original and JSON-reloaded retrievers produced identical complete
`RetrievalHit` lists, totaling 12,941 hits with three zero-hit questions. The
local evidence is `results/p1-week3-week4-bm25-roundtrip.json`. Loading rebuilt
the term index from the saved passages and settings as documented above.

Run the offline regression suite with:

```powershell
& $p1Python -B -m pytest tests/test_p1.py tests/test_p1_week4.py tests/test_p1_experiment.py -v
& $p1Python -B -m pytest -q
```

The historical final runs reported **185 passed in 6.89 s** for the three P1 files and
**202 passed in 6.84 s** for the full suite (zero failures or skips). The
original 122 P1 and 17 P2 cases remain intact. The additions are 49 Week 4
contract/persistence cases and 14 experiment/input cases. Dense unit tests use
deterministic encoders with real FAISS, separately from the real BGE runs.
Ruff check and format check passed for all six changed/new Python files in
that session. The current audit/evaluation work started from a newly rerun
baseline of **202 passed in 6.13 s**, with zero failures or skips; this baseline
does not yet verify the new evaluation code.

### Real development run on 11 October 2026

The build command above completed with 32,073 passages, 1,168 paper indexes
and 384-dimensional real BGE embeddings. The cached model ran on CPU with
four PyTorch intra-op threads; no new model download was needed. A separate
three-query experiment loaded the complete saved indexes successfully before
the all-question run. Its output directory is
`results/p1-week3-week4-full-index-smoke`.

The exact full experiment command above completed for **all 2,593 train
questions**, with K=5. It wrote:

- **12,941 BM25 rows and 12,941 Dense rows** in `results.jsonl`.
- **5,186 query/method rows** in `queries.jsonl`: 5,180 successful and six
  `paper_without_passages` records for the three source-data cases described
  above. Four other questions have fewer than five available passages; their
  results are not duplicated to pad K.
- A complete `run.json`, including exact input/model hashes and source-file
  hashes for the uncommitted P1 changes, with `quality_metrics: null`.

The original independent output check verified every result's paper/Passage association,
finite descending scores, continuous unique ranks, output hashes and current
P1 source hashes at the time of that run. The separate three-query reload and full run agreed on all
30 smoke result IDs and scores (absolute/relative tolerance 1e-6). Evidence:
`results/p1-week3-week4-final-validation.json`.

| Method | Mean retrieve latency | p50 | p95 | p99 | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: |
| BM25 | 0.128309 ms | 0.120100 ms | 0.208000 ms | 0.280972 ms | 0.495000 ms |
| Dense | 7.030325 ms | 6.933000 ms | 8.106740 ms | 8.852712 ms | 12.176300 ms |

These statistics are recomputed from the existing `queries.jsonl`; the
audit/evaluation work did not run new retrieval or measure new latency.
They are preliminary timings from one sequential pass, including the three
zero-hit calls per method, after one warm-up per backend. They are not a
multi-run performance benchmark. Dense includes query encoding. The recorded
processor is `Intel64 Family 6 Model 198 Stepping 2, GenuineIntel` (24 logical
CPUs); torch intra-op/inter-op threads were 4/24. All library versions are in
`run.json`, including sentence-transformers 5.7.0, transformers 4.57.6,
faiss-cpu 1.15.1 and rank-bm25 0.2.2.

For the first train query, `How is the input triple translated to a
slot-filling task?` (paper `1706.04115`, question
`0038b073b7cca847033177024f9719c971692042`), the first results were:

| Method | Rank | Section | Score |
| --- | ---: | --- | ---: |
| BM25 | 1 | Dataset | 12.050673 |
| BM25 | 2 | Unseen Entities | 9.312080 |
| BM25 | 3 | Model | 8.881554 |
| Dense | 1 | Approach | 0.703596 |
| Dense | 2 | Dataset | 0.695794 |
| Dense | 3 | Introduction | 0.681121 |

Full original passage IDs are in `results.jsonl` and the final validation
artifact. Different top results are candidates for later analysis, not a
labelled retrieval error or a quality comparison.

### Complete audit of results shorter than K

The existing logs give the same count distribution for BM25 and Dense. Counts
below are **questions per method**, not pooled method calls:

| Returned passages | 0 | 1 | 2 | 3 | 4 | 5 | Total questions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BM25 | 3 | 1 | 1 | 0 | 2 | 2,586 | 2,593 |
| Dense | 3 | 1 | 1 | 0 | 2 | 2,586 | 2,593 |

All seven short-result cases are accounted for below. Candidate counts are
from the complete saved corpus and are identical for both methods.

| Question ID | Paper ID | Available passages / returned by each method | Reason |
| --- | --- | ---: | --- |
| `2a0f14740ee14224d116d4f51dacde6863bcdc1e` | `1801.07804` | 0 / 0 | Source and export have empty `full_text`; no full-text chunks exist. |
| `6d623c96cd3898c3758338e337e9157565f34185` | `1801.07804` | 0 / 0 | Same source-data limitation; retained as a zero-hit query. |
| `82c7d9e92c7d7b784de2cae87fb7293034c551f4` | `1801.07804` | 0 / 0 | Same source-data limitation; retained as a zero-hit query. |
| `a02696d4ab728ddd591f84a352df9375faf7d1b4` | `1605.07683` | 2 / 2 | Three source sections have no paragraphs; the remaining 63-word task section and 20-word acknowledgments each form one chunk. Both are returned. |
| `b13d0e463d5eb6028cdaa0c36ac7de3b76b5e933` | `1611.04642` | 1 / 1 | Six source sections have no paragraphs; only the 37-word acknowledgments remains. Its single chunk is returned. |
| `b974523a6cbd3cdc1fa924243ccc9711bbc7070d` | `1810.10797` | 4 / 4 | Four nonempty sections contain 112/48/182/94 words, each forming one chunk. All four are returned. |
| `beda007307c76b8ce7ffcd159a8280d2e8c7c356` | `1608.04207` | 4 / 4 | Four nonempty sections contain 115/190/60/92 words, each forming one chunk. All four are returned. |

For each method, the hypothetical full-K total is `2,593 * 5 = 12,965` rows.
The actual `12,941` rows are short by 24: **15** from the three zero-candidate
questions, plus **9** from the four nonempty short papers (`3 + 4 + 1 + 1`).
These are candidate-availability limits, not missing retrieval rows. They
remain in the query logs and latency population; no result is duplicated to
reach K. Zero hits alone do not establish that the question is unanswerable.

### Three train-query observations without relevance labels

The following observations use the already saved rankings and their original
Passage text. No answers or evidence annotations were used. They describe
candidate content and rank differences, not successes, failures or system
quality. Passage IDs below omit only the common `qasper-passage-v1-` prefix;
the full identifiers remain unchanged in `results.jsonl`.

| Question / paper | Observed candidates | Interpretation boundary |
| --- | --- | --- |
| `0038b073b7cca847033177024f9719c971692042` / `1706.04115`; input triple and slot filling | BM25 rank 1 is `Dataset` (`3d65804f72b0d7674cddf9b63be5f5f76305ba81c33e69a66e799d7aedbedced`, 12.050673), discussing collection of relation-slot examples and conversion of queries into natural language. Dense rank 1 is `Approach` (`7bc45a7f775256d5f953d348bbcf0b95eacbbf747d424c5b192472f59227e014`, 0.703596), discussing the relation/entity/sentence input and question templates. | The backends emphasize different parts of the same paper. The shared `Dataset` passage is Dense rank 2; no gold annotation establishes which rank is preferable. |
| `0062ad4aed09a57d0ece6aa4b873f4a4bf65d165` / `1903.00058`; n-gram similarity measure | BM25 rank 1 is `Introduction` (`275a3dfddfdcf05fc3a80e84a7ea43fd94ff86946ab391e148930b7e66264567`, 8.040770), introducing local n-gram overlap and a dense-vector extension. Dense rank 1 is `Retrieval Approaches` (`6ef2bc9d2a8e84fa46de70c956522a42b0fdd4326bdd0a4b1498498cee24cb25`, 0.840033), explicitly describing an IDF-based similarity; BM25 rank 3 also discusses IDF-based n-gram retrieval. | The paper distinguishes multiple retrieval variants. Formula placeholders such as `INLINEFORM0` and `DISPLAYFORM0` remain in the source text, so the record does not justify reconstructing missing formulae or declaring a complete answer. |
| `00e9f088291fcf27956f32a791f87e4a1e311e41` / `1804.00079`; combined training objectives | BM25 rank 1 is `Introduction` (`1f5e2d66e886958a635e569f6e60ec2e93663a187645eb9b49e9b611925775e6`, 5.456673), listing NMT, NLI, constituency parsing and skip-thought objectives. Dense rank 1 is `Training Objectives & Evaluation` (`84fdd9d6012e6c3b8837e6de4c9307f6cb31b93b5937dbfa6037bcff3221d0de`, 0.685697), explaining the motivation and selection criteria; the Introduction passage is Dense rank 3. | Section titles and semantic similarity do not by themselves establish answer completeness. Shared candidates appear at different ranks, and both lists need external judgments before quality comparison. |

### Audit and optional evaluation of an existing run

The current P1 evaluation entry point reuses the recorded run and corpus. It
does not rerun BM25/Dense, encode queries or rebuild indexes:

```powershell
& $p1Python -B -m scripts.run_p1_experiment evaluate --run-dir results/p1-week3-week4-development --output-dir results/p1-week3-week4-evaluation-final --evaluation-k 5
```

Use a new or empty evaluation output directory. The output files are
`audit.json`, `counts.jsonl`, `evaluation.json` and `provenance.json`. This
no-qrels command audits result counts, mappings and recorded latency, and
records that real quality metrics are unavailable. The original retrieval
files and their recorded source hashes remain historical inputs; evaluation
records its own code and input provenance separately.

P1 now includes a **provisional** backend for Precision@K, Recall@K and MRR@K,
plus validation of externally supplied relevance judgments. This is not a P6
protocol freeze or evidence of valid real-corpus scores. Actual scoring
requires independent, versioned gold qrels with the matching corpus/split
provenance and explicit mapping/coverage statuses. The JSONL and TREC qrels
formats and eligibility rules are documented in [P1 evaluation](P1_EVALUATION.md).
Synthetic metric tests demonstrate software behavior only. They do not supply
real labels; nDCG and formal labelled failure analysis remain unreported.

### Historical upstream dependency check

This snapshot belongs to the earlier saved-run evaluation pass and is
superseded by the 17 October dependency checkpoint below. After that earlier
`git fetch origin`, the inspected remote refs were:

| Ref | Commit | Actual implementation evidence |
| --- | --- | --- |
| `origin/main` | `44c112f265709fff76484dabb603d073ab141480` | `src/evaluation/`, `src/agent/` and `src/generation/` contain only empty `__init__.py` files. No P6 metric implementation or P4/P5 runtime is delivered there. |
| `origin/p3-qasper-foundation` | `499bb6d8ea2952f10e0499bfb8eb2986d683ba06` | `BuiltPassage` retains internal source coordinates and paragraph indices, but `scripts/build_corpus.py` exports only the public Passage fields. QA export copies annotations; inspection only counts evidence. There is no gold evidence-to-Passage-ID mapping. |
| `origin/p2/week1-fusion-reranking` | `3fd9becd6fbfd22c3136a6c25df4ee7a716569ad` | `HybridRetriever` and its callbacks still accept/forward only `query`, `paper_id`, `top_k`; section forwarding is not implemented. |
| `origin/p1/retrieval` | `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9` | Published P1 Week 1/2 foundation; the local Week 3/4 work has not been pushed. |

At that checkpoint, the fetched remote heads contained no P4/P5/P6 branch. This does not establish
what collaborators may have locally. P3's Week 2 report explicitly lists gold
mapping as later work; its `FLOAT SELECTED` mapping decision remains pending.
The local `docs/EVALUATION.md` matches main's proposal. P3 adds explicit QA
access/freeze boundaries, while still marking the split-role convention as
proposed. K values, partial evidence, no-relevant-document handling and macro
averaging still need P6 agreement. Unjudged candidates are not automatically
negative labels.

Accordingly, real retrieval quality remains **unavailable** until gold mapping
and the protocol are supplied, despite the new local provisional metric code.
At that checkpoint, P1's three-argument callback compatibility was tested,
while P2/P4 section forwarding and a real Agent integration run were pending.

Keep all generated data, indexes, caches and results ignored. The local P3
preparation record is
`.cache/p3-week3-week4/data/processed/p1_data_preparation.run.json`;
P1's independent data validation is
`results/p1-week3-week4-data-validation.json`. These artifacts are local,
not committed datasets or team-level completion claims.

### Final verification of the saved-output evaluation follow-up

The final no-label audit command above actually completed against the existing
real run, writing `results/p1-week3-week4-evaluation-final`. It reported
`status: valid`, 2,593 questions, 12,941 result rows for each method and
`evaluation_status: unavailable`. All 5,186 query/method counts match
`min(5, eligible_passage_count)`. Each method has 2,593 unique question IDs
and 2,593 query logs. There are no missing queries, duplicate records,
unknown/cross-paper results, abnormal query statuses or unexplained lost
results. Section-boundary violation is not applicable: the source run requested
no section filter. The original `run.json`, `results.jsonl` and `queries.jsonl`
hashes are unchanged. The final artifact records the new evaluator source
hashes separately.

The same directory also contains `qualitative_review.json`, a separate earlier qualitative
observation record for the three cases above with full original Passage IDs/text,
sections, ranks and source hashes. It is not a qrels file or a relevance label
set and is not consumed by the metric backend. It records no quality verdict.

This follow-up actually ran the following commands using
`E:\Miniconda\py311\envs\papergap\python.exe` (Python 3.11.16), with
`HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`:

| Command | Passed | Failed | Skipped | Duration |
| --- | ---: | ---: | ---: | ---: |
| `python -B -m pytest -q` (before changes) | 202 | 0 | 0 | 6.13 s |
| `python -B -m pytest tests/test_p1_evaluation.py tests/test_p1_experiment.py -v` | 76 | 0 | 0 | 3.49 s |
| `python -B -m pytest -q` (final) | 264 | 0 | 0 | 8.05 s |

All 202 existing cases remain, with 35 metric/label tests and 27 additional
saved-run/CLI tests. The labeled CLI integration uses a handwritten synthetic
subset, verifies its expected scores and exclusions, and forbids retriever and
encoder calls. It also checks that every original run file remains unchanged.
The real audit does not download/run the model or rerun any real retrieval.

Ruff `check` and `format --check` passed for `experiment.py`, `evaluation.py`,
`run_p1_experiment.py` and the two corresponding test files. `git diff --check`
passed; Git emitted only its existing LF-to-CRLF notices. No changes were made
to the existing BM25/Dense implementations, shared schema or P2/P3/P4/P5/P6
code in this follow-up. Work remains local and unstaged on `p1/week3-week4`.

## Final interface and delivery review

This last pass added only the two missing bound-callback integration tests and
handoff documentation. No production implementation, shared schema, metric
definition, model or retrieval experiment changed. README and CLI commands
were checked against the current scripts; the existing evaluation input format
already meets the handoff requirements and was left unchanged.

### Historical handoff evidence and remaining inputs

| Area | Evidence / status |
| --- | --- |
| Real train retrieval and saved-index workflow | Previously executed and audited: 32,073 passages, 1,168 indexed papers, 2,593 train questions, 12,941 rows per method. This pass reads `results/p1-week3-week4-evaluation-final/audit.json`; it does not repeat the count investigation or retrieval. |
| P1 paper/section API | Implemented; the original three-argument call and keyword-only section behavior are tested. |
| P1 callbacks through existing P2 | Interface-level verification completed with the real Hybrid/RRF code and synthetic controlled embeddings. Actual P2/P4 application forwarding remains pending. |
| Evaluation tooling | JSONL/TREC adapter, provenance checks and provisional Precision@K/Recall@K/MRR@K backend verified previously. Real metrics remain unavailable with null scores until suitable labels arrive. |
| P3 label handoff | Requires original `question_id`, `paper_id`, relevant Passage IDs, mapping status, complete/incomplete relevance declaration and mapping provenance. Preserve opaque IDs; supply the exact corpus SHA and corresponding corpus/chunking manifest, including the 200/40 configuration and version strings for this run. |
| Label coverage | `annotation_coverage` describes records supplied for the whole run scope; per-question `relevance_complete` describes exhaustive relevance within its paper. Missing records, mapping failures and partial mappings must remain explicit. JSONL/TREC file format itself establishes no completeness. |
| P6 protocol | Confirm K (saved depth is 5), truncated MRR@K, Precision denominator K even for short returns, macro averaging, relevance definition and the separate policies for unanswerable/no-relevant/missing/mapping-failed/incomplete cases. Replace/approve the provisional backend without changing P1 retrieval. |
| Team freeze and full agent integration | Not completed by this P1 handoff. The split policy and evaluation conventions remain provisional. |

See [P1 evaluation](P1_EVALUATION.md) for the exact JSONL/TREC schemas and
supplier declarations. The existing real run's corpus hash is
`abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`.
Its chunker is `word-chunking-v1` with `text-normalization-v1`, 200-word chunks
and 40-word overlap, using `full_text`. Label producers should provide the
matching corpus manifest alongside their labels; the scoring adapter binds
the labels via `corpus_sha256` and validates the run's corpus/QA manifests.
It does not infer a chunking version from a Passage ID.

The following commands are ready for reuse from the repository root. The
first is the only pytest command executed in this last handoff pass; the
second is for **future execution after real labels arrive**, using a new or
empty output directory:

```powershell
$p1Python = 'E:\Miniconda\py311\envs\papergap\python.exe'
& $p1Python -B -m pytest tests/test_p1_week4.py -q -p no:cacheprovider
& $p1Python -B -m scripts.run_p1_experiment evaluate --run-dir results/p1-week3-week4-development --output-dir results/p1-week3-week4-labeled --evaluation-k 5 --labels data/p1-development-qrels.jsonl --labels-manifest data/p1-development-qrels.manifest.json
```

The actual new result was **51 passed in 0.32 s**, zero failed/skipped: the
existing 49 section/persistence cases plus two P2 callback handoff cases.
Ruff check and format check passed for this test file. Production code did
not change, so the previous **76 passed** evaluation/experiment run and
**264 passed** full-suite run are retained as earlier evidence, not described
as new runs. Neither the full real query set nor the existing audit was rerun.
The interpreter remains the explicit papergap Python 3.11.16 above.

### Reviewable files and local artifacts

At this historical pre-Agent checkpoint, the uncommitted Week 3/4 delivery,
relative to the Week 1/2 base, was:

| Files suitable for code review | Purpose |
| --- | --- |
| `src/retrieval/bm25_retriever.py`, `dense_retriever.py` | Previously added section filtering and BM25 JSON persistence; unchanged in this last pass. |
| `src/retrieval/experiment.py`, `evaluation.py` | Verified P3 inputs, train-only export, saved-output audit and independent provisional scoring. |
| `scripts/run_p1_experiment.py` | Existing retrieval and `evaluate` entry points. |
| `tests/test_p1_week4.py`, `test_p1_experiment.py`, `test_p1_evaluation.py` | Small, synthetic offline tests; the last pass adds only the two handoff cases. |
| `README.md`, `docs/P1_WEEK3_WEEK4.md`, `P1_EVALUATION.md`, `WEEKLY_TRACKER.md` | Setup, reproducibility, contracts, input requirements and evidence. |

The existing small `tests/fixtures/mock_passages.jsonl` is already part of the
Week 1/2 foundation. No real qrels, corpus or model file belongs in these code
changes. Raw/processed P3 data and its worktree live under `.cache/`; the model
cache is `.cache/huggingface`; saved indexes live under `indexes/`; retrieval,
audit and qualitative outputs live under `results/`. All were checked against
the existing ignore rules. Only `data/README.md` and `results/README.md` are
tracked under those data/output directories; no model/index artifacts are
tracked. Ignored outputs must be regenerated locally with the documented
commands on a new checkout. Reuse the existing artifacts on this machine.

`git diff --check`, branch/status, unchanged other-owner paths and the staged
file list were checked in this pass. No P2/P3/P4/P5/P6 module or shared schema
was changed, and no file was staged, committed, pushed or submitted as a PR.

## Latest dependency integration: 17 October 2026

### Remote state and protected workspace

The fetch and GitHub REST pull-request check observed:

| PR / reference | State | Inspected commit |
| --- | --- | --- |
| main / P4 #6 | #6 merged 17 October | `6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c` (main merge); P4 head `69ea3a0d2475bd16b08cf0e6aa4e8bd58da376d4` |
| P1 #4 | Merged 14 October | `593b3484902272c97e3fdc835f608224205dd8ac` (merge); P1 head `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9` |
| P3 #2 | Merged 14 October | `04bd1ff55d8fc79ab4cabdada693889dc8a93e9b` (merge); P3 head `11bfbf1d88293c183dbe182cd94c151f0142a295` |
| P2 #5 | Open | `0046e680fd361f90b608a949d2dd132d55db71aa` |
| P6 #7 | Open | `82f95d4400ec7c3b0433b16204304bf59f41c0b2` |

The original worktree remains on `p1/week3-week4` at `5d3f447`; its local
Week 3/4 increment was not staged, committed, pushed, or submitted as a PR.
The initial modified/untracked files were backed up under
`results/p1-integration-20261017/baseline/`. The accompanying `baseline.json`
records their hashes plus 1,208 pre-existing data/index/result artifacts.
No original experiment, count audit, or index was replaced. Final hash
verification found all 1,208 artifacts unchanged;
`results/p1-integration-20261017/final-verification.json` records the check,
unchanged original source files, empty staging area, and shared-document merge.

Two detached, ignored worktrees isolate the dependencies:

- `.cache/p1-main-20261017`: actual main `6fa06b5` plus P1 tracked retrieval
  patches and all clearly P1 untracked source, tests, and P1 documents.
- `.cache/p1-p2-20261017`: complete PR #5 head `0046e68` plus the same necessary
  P1 increment. P2 commits and its CLI were not copied into the P1 delivery.

The current `AGENTS.md` and `CONTRIBUTING.md` were read. Shared changes are in
English. `README.md` and `docs/WEEKLY_TRACKER.md` have no upstream content
difference between the original HEAD and inspected main; the P1 additions
were reconciled against those main versions. Other owners' implementations,
AgentState, and P2/P4 application interfaces were left unchanged.

### Actual real-retrieval to Agent control-flow check

The reusable entry point is `scripts/run_p1_integration.py`, backed by
`src/retrieval/agent_integration.py`. It uses the actual main
`HybridRetriever`, `build_agent_graph`, and `AgentState`, real BM25, cached
BGE query encoding, and saved FAISS vectors. Both complete saved Passage
mappings, corpus/export hashes, split membership, model revision and FAISS
checksums/settings were validated before the requests. The existing corpus
hash remains `abc42568dbd7eecaa951ffd28b9f8c58a3629e62f401f102eff3b2a59da97790`;
BGE revision remains `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`.
No corpus embeddings or the original 2,593-question experiment were rerun.

Only projected train `question_id`, `paper_id`, and query text are selected.
P4 receives only `question` and `paper_id`; question ID stays in the external
trace because the unchanged AgentState has no question-ID field. No QA row,
answer, or gold evidence is passed to retrieval, planning, or rewriting.

The four fixed questions were:

| Key | Full question ID | Paper | Original question |
| --- | --- | --- | --- |
| Q1 | `0038b073b7cca847033177024f9719c971692042` | `1706.04115` | How is the input triple translated to a slot-filling task? |
| Q2 | `003f884d3893532f8c302431c9f70be6f64d9be8` | `1705.09665` | Do they report results only on English data? |
| Q3 | `0062ad4aed09a57d0ece6aa4b873f4a4bf65d165` | `1903.00058` | Which similarity measure do they use in their n-gram retrieval approach? |
| Q0 | `2a0f14740ee14224d116d4f51dacde6863bcdc1e` | `1801.07804` | Do they consider relations other than binary relations? |

All section strings below were read from that paper's actual corpus passages.
Each request binds its chosen section to both callbacks, reusing initialized
indexes; the binding persists through every rewrite and retrieval round.
The candidate budget is 20 per source and RRF k is 60.

| Invocation order | Question / bound section | top_k | Available passages | Per-round returns | Retries | Accumulated IDs |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| 1 | Q1 / Approach | 5 | 4 | 4 | 0 | 4 |
| 2 | Q2 / Acknowledgements | 5 | 1 | 1, 1, 1 | 2 | 1 |
| 3 | Q3 / Results | 2 | 1 | 1, 1, 1 | 2 | 1 |
| 4 | Q1 / Model | 3 | 4 | 3, 3, 3 | 2 | 3 |
| 5 | Q0 / whole paper | 5 | 0 | 0, 0, 0 | 2 | 0 |
| 6 | Q1 / whole paper | 5 | 29 | 5 | 0 | 5 |
| 7 | Q1 / Approach, original graph reused | 5 | 4 | 4 | 0 | 4 |

All seven requests / fifteen rounds passed. Per-round traces prove that
original and mock-rewritten queries reached both P1 backends. They retain
available IDs, source candidate IDs/ranks/scores, fused returned IDs,
source_scores, paper/section, top_k, and retry counts. Passage objects are
checked against the original corpus, result counts against candidate union,
and RRF ordering against the source ranks. P4 accumulation is checked for
unique IDs and retention of the first returned provenance. The repeated
Approach invocation matches the first complete trace after the intervening
paper/question/section requests. The known empty paper terminates after the
default two retries / three rounds without an error.

This is **real retrieval to mock-Agent control-flow integration**. The P4
planner, mapper, critic, classifier and rewriter remain keyword mocks. Their
sufficiency values are control-flow observations, not relevance judgments.
The section constraint is fixed by the request; this does **not** demonstrate
gap-driven dynamic section switching or full adaptive RAG quality.

The real cases did not accumulate more than one round's top_k. Two explicitly
controlled tests in `tests/test_p1_agent_integration.py` supplement this:
actual Hybrid/P4 with synthetic P1-shaped candidates returns two per round,
accumulates four distinct IDs over three rounds, preserves the first duplicate's
provenance, and forwards two different mock rewrites. Reusing the same graph
across different questions/papers and an empty request also stays independent.
These controlled cases are interface evidence only, not real retrieval results.

The final authoritative real trace is
`results/p1-integration-20261017/agent-final/trace.json`, including data and
source hashes, actual base commit, model revision and dependency versions.
`agent/trace.json` is the initial successful run before two extra paper/budget
assertions; it is retained separately. The table above describes the final run.

Reproduce from the prepared latest-main worktree using a new output directory:

```powershell
$p1Root = 'E:/Lenovo/Desktop/papergap-rag'
$p1Python = 'E:/Miniconda/py311/envs/papergap/python.exe'
$env:HF_HUB_OFFLINE = '1'
$env:TRANSFORMERS_OFFLINE = '1'
$env:OMP_NUM_THREADS = '4'
$env:MKL_NUM_THREADS = '4'
Push-Location "$p1Root/.cache/p1-main-20261017"
& $p1Python -B -m scripts.run_p1_integration --artifact-root $p1Root --output-dir "$p1Root/results/p1-integration-next/agent"
Pop-Location
```

The old root HEAD lacks P4, so this new entry point and its tests require the
prepared main combination (or a later branch that incorporates main).

### Complete P2 PR #5 CLI check

The actual `python -m scripts.demo_hybrid` ran in its full `0046e68` checkout,
with the required P1 increment, Windows Python 3.11.16, offline cached BGE,
CPU, and four OMP/MKL threads. It reuses the Dense index and rebuilds its
in-memory BM25 from the same cached corpus, as the existing CLI implements.
The complete index mapping and revision checks passed before execution.

| Query above | Paper candidates | BM25 / Dense candidates | Union | Returned |
| --- | ---: | --- | ---: | ---: |
| Q1 | 29 | 20 / 20 | 24 | 5 |
| Q2 | 38 | 20 / 20 | 28 | 5 |
| Q0 | 0 | 0 / 0 | 0 | 0 |

All three CLI executions passed original Passage object/ID and paper-scope
checks, continuous ranks, finite source scores, source rank bounds, RRF score
calculation and deterministic returned order. Each CLI performs one warm-up
and one measured call; these timings are smoke records, not a benchmark.
The CLI exposes source candidate counts and returned source_scores, but not
all candidate IDs. Full per-round candidate-ID traces belong to the separate
Agent check above. The existing CLI has **no section parameter**; no
`--section` argument was invented or tested.

No `BAAI/bge-reranker-base` snapshot at required revision
`2cfc18c9415c912f9d8155881c133215df768a70` was present in the explicit or
standard local caches. Real reranking was not run and no download attempted.
No macOS ARM64 lockfile or Mac repair script was used.

Evidence is `results/p1-integration-20261017/p2/summary.json`, which contains
exact subprocess arguments, full question IDs, environment, source hashes,
cache checks and each assertion outcome. `cli-01-rrf.json` through
`cli-03-rrf.json` are actual CLI outputs. A representative rerunnable command
from that P2 worktree, with the variables/environment above, is:

```powershell
& $p1Python -m scripts.demo_hybrid --passages "$p1Root/.cache/p3-week3-week4/data/processed/passages.jsonl" --dense-index-dir "$p1Root/indexes/p1-week3-week4-development" --query "How is the input triple translated to a slot-filling task?" --paper-id 1706.04115 --top-k 5 --candidate-k 20 --rrf-k 60 --revision 5c38ec7c405ec4b44b94cc5a9bb96e735b38267a --device cpu --cache-folder "$p1Root/.cache/huggingface" --local-files-only --output "$p1Root/results/p1-integration-next/p2-q1.json"
```

### P3/P6 dependency review and owner handoff

P3 `11bfbf1` exports original QA annotations and corpus provenance, but still
has no reliable gold-evidence-to-canonical-Passage mapping or per-question
relevance completeness declaration. `src/data/qasper_export.py` copies QA
annotations; it does not create qrels. `docs/REQUIREMENTS.md` P3-D003 and
`docs/EVALUATION.md` still require mapping review and metric agreement.
On both main and P6 `82f95d4`, `src/evaluation/` contains only an empty
initializer. Thus real metrics remain **unavailable** and team evaluation
**provisional**. Raw evidence text and corpus counts do not establish complete
qrels. This pass did not extend the existing provisional evaluation framework.

P6 was inspected read-only; no UI or P6 index was executed or modified:

| Boundary | P6 currently implements | Required distinction / proposed owner action |
| --- | --- | --- |
| Retrieval request | `IndexedRetriever.retrieve(query, top_k=5, candidates=25)` | Full-corpus search, without paper_id/section. P6/P2/P4 agree request context before integration. |
| Corpus/IDs | `chunk_id`, `section_path`; temporary Passage sets chunk_number=0 | Not canonical mapping by itself. P3/P6 must preserve original opaque Passage IDs and metadata; do not infer an ID conversion. |
| Sparse/Dense index | Lucene plus one `chunks.faiss`, `row_ids.json`, `config.json` | Different from P1 per-paper BM25 and FAISS metadata/row mappings; not P1 index reuse. |
| Model provenance | Default MiniLM, encoder load without immutable revision | Different from pinned BGE/query instruction. P6 chooses an explicit backend and records compatible provenance. |
| Results | Chunk dictionaries plus rrf_score | Original source ranks/scores, final rank and reranker score are not exposed. P6 should adapt the actual RetrievedPassage without losing provenance. |
| Suggested connection | `src/ui/services.py:get_retriever`, then `src/ui/app.py` retrieval call | Construct/reuse the P1+P2 backend here; jointly agree selected-paper and section handling with P2/P4. |
| Generation/display | Adapter before `src/generation/prompting.py:build_messages` | P6/P5 preserve canonical IDs; E1-style labels are display references only. |

P6's `paper__chunk_00018` example is not an enforced parser format: the loader
accepts nonempty unique strings. Naming a field `chunk_id` or assigning it to
`Passage.passage_id` does not establish that the underlying corpus is P3's
canonical corpus or that P1 indexes were reused.

Remaining concrete inputs:

- **P2 / Vishakha:** review/merge #5; agree the request-scoped section binding
  and candidate budget at the application boundary with P4/P6. Supply a matching
  reranker cache or a separately authorized reranker run if that check is needed.
- **P3 / Jingshuai Qian:** matching corpus/chunker manifest, question/paper IDs,
  canonical relevant Passage IDs, mapping failures/ambiguities, run-scope
  coverage and per-question relevance completeness. Review/freeze split policy.
- **P4 / Ananya:** review the current callback integration; own real planner,
  critic/rewriter behavior and any future gap-to-section policy. Fixed section
  binding here does not change AgentState or settle the application contract.
- **P6 / owner name still pending:** decide the P1/P2 UI adapter versus the
  independent index path; provide the metric backend and protocol (K, MRR
  cutoff, Precision denominator, macro averaging, and missing/unanswerable/
  mapping-failed/incomplete-label policies). Coordinate review with P2/P3/P4.

### Tests executed for this checkpoint

Only the new integration risks were tested; there was no new full-suite run.
All commands used the specified papergap interpreter.

| Combination / command | Actual result |
| --- | --- |
| main `6fa06b5` + P1: `python -B -m pytest tests/test_p1_agent_integration.py tests/test_agent.py -q -p no:cacheprovider` | 13 passed in 0.47 s (2 new controlled + 11 existing P4); zero failures/skips |
| Full P2 `0046e68` + P1: `python -m pytest -q tests/test_hybrid_cli.py` | 4 passed in 20.03 s; zero failures/skips |
| main + P1: real integration CLI, final run | 7 requests / 15 rounds passed |
| Full P2 + P1: actual real RRF CLI | 3 fixed train requests passed |
| Ruff check / format --check in main worktree | Passed for the 3 new Python files |

The earlier **51**, **76**, and **264** test counts remain historical evidence
on their original combinations, not current-main results. The P1 retrieval
implementation needed no new compatibility fix; this checkpoint adds only
`agent_integration.py`, `run_p1_integration.py`,
`test_p1_agent_integration.py`, and README/report/tracker updates to the
existing uncommitted Week 3/4 work.

### Proposed commit and PR handoff

Historical pre-delivery proposal: the actual saved commit, main merge and
final-code checks are recorded in [Phase 3](#phase-3-git-delivery-and-final-code-validation).

For the subsequent read-only P2 review and the existing 100-question package,
see [Phase 2](#phase-2-p2-source-review-and-delivery-entry-points).
The P1 PR draft below is separate from the unpublished P2 review draft there.

The old temporary `p1/retrieval` target is superseded: Week 1/2 #4 has merged.
Review only the Week 3/4 increment against inspected latest **main**. The
isolated main worktree demonstrates the current combination; the original
branch has deliberately not been rebased or merged. A future Git delivery
must reconcile that branch with main and obtain the required owner review.
No P2 PR #5 commits belong in this P1 increment.

The P1 increment is ready for a scoped review against the inspected main,
with the evidence/limitations above. It is not a claim that the unchanged old
branch can run P4, that merge approval has been obtained, or that real retrieval
quality / full adaptive RAG / P6 UI integration is complete. The missing gold
labels and owner decisions are explicit handoff dependencies rather than
fabricated completion criteria.

Suggested commit message:

```text
feat(retrieval): add P1 development evaluation and agent integration checks
```

Suggested PR title: `Deliver P1 Week 3/4 retrieval and integration handoff`

Suggested PR body (draft only, target `main`):

```markdown
Adds the P1 Week 3/4 increment over the already merged Week 1/2 foundation:
manifest-validated train-only experiments, section-aware BM25/Dense callbacks,
BM25 persistence, saved-run auditing and provisional independent-qrels scoring.

Adds a bounded real-index P1 -> P2 -> P4 integration check with per-round
query, candidate, provenance and retry traces. Preserves original Passage IDs,
request-bound sections and existing P2/P4 APIs. The Agent policy remains mock.

Validation on main 6fa06b5 plus this increment:
- Real cached BGE/BM25/FAISS: 4 fixed train questions, 7 invocations, 15 rounds.
- 13 targeted tests passed, including 2 controlled multi-round interface cases.
- Complete P2 PR #5 head 0046e68 was checked separately: 3 actual RRF CLI
  requests and 4 CLI tests passed. No P2 commits are included here.
- Ruff and diff checks passed; existing data/index/experiment hashes preserved.
- Historical 51/76/264 test results and the 2,593-question baseline are retained
  as historical evidence, not rerun claims on current main.

Gold mapping and the P6 backend/protocol remain pending; real quality metrics
are unavailable. Fixed request sections do not demonstrate dynamic section
selection. Real reranking was not run because the matching local cache is absent.
P6's separate IndexedRetriever is documented, not changed or called P1 reuse.
```

## Fixed-sample qualitative analysis of saved baselines

**Codex-assisted qualitative analysis — pending human review**

This phase interprets only the original independent BM25/Dense Top-5 from
`results/p1-week3-week4-development/`. No retrieval, query encoding, corpus
encoding, index construction, parameter tuning, or Hybrid/Agent execution was
performed. The preceding integration results are not part of this comparison.
Original QASPER answers/evidence are used only for post-hoc interpretation;
they were not inputs to the original retrieval run or to an Agent. Original
experiments, indexes, prior review artifacts and the existing delivery ZIP
remain unchanged. The ZIP was not rebuilt and does not include this addition.

### Fixed selection and evidence status

Only the earlier three-case review existed; it contained unlabelled candidate
observations, not six to ten complete annotated cases. This phase retains those
three questions and fixes a total of **eight train questions** before inspecting
their annotations. `results/p1-qualitative-20261017/selection.json` records the
IDs, original questions, selection order and reasons. Five additions comprise
an audited empty paper, an audited one-passage paper, and three cases chosen
from saved ranking IDs. For the latter cases, selection takes the first eligible
question ID in lexical order on a paper not already selected. No question was
replaced or added after fixation.

| Case | Question ID | Paper | Original question | Selection reason |
| --- | --- | --- | --- | --- |
| C01 | `0038b073b7cca847033177024f9719c971692042` | `1706.04115` | How is the input triple translated to a slot-filling task? | Retained prior case |
| C02 | `0062ad4aed09a57d0ece6aa4b873f4a4bf65d165` | `1903.00058` | Which similarity measure do they use in their n-gram retrieval approach? | Retained prior case |
| C03 | `00e9f088291fcf27956f32a791f87e4a1e311e41` | `1804.00079` | Which training objectives do they combine? | Retained prior case |
| C04 | `2a0f14740ee14224d116d4f51dacde6863bcdc1e` | `1801.07804` | Do they consider relations other than binary relations? | Known empty full_text |
| C05 | `b13d0e463d5eb6028cdaa0c36ac7de3b76b5e933` | `1611.04642` | What datasets are used to evaluate the model? | Known one-passage corpus |
| C06 | `00bcdffff7e055f99aaf1b05cf41c98e2748e948` | `1909.02764` | What is the baseline method for the task? | Disjoint saved Top-5 ID sets |
| C07 | `018ef092ffc356a2c0e970ae64ad3c2cf8443288` | `2004.03788` | How large is the dataset? | Same top-1 and at least three shared IDs |
| C08 | `02348ab62957cb82067c589769c14d798b1ceec7` | `1909.00578` | What simpler models do they look at? | Exactly one shared Top-5 ID |

This is **purposive explanatory sampling**, not a random sample or an estimate
of failure prevalence. The ordinary-case criterion initially sought identical
Top-5 order, but no eligible pair satisfied it. Before annotation reading, it
was defined as same top-1 with at least three shared IDs; this selection detail
is retained in the fixed manifest. No desired failure category was enforced.

The source paths, recorded hashes, model revision and full_text-only chunking
policy come from the existing `run.json` and manifests. This phase did not
rehash the complete corpus/index inventory. It filters QA rows by
`source_split == "train"`, then by the fixed IDs, before accessing answers and
evidence. Per-case checks compare saved rows and original Passage objects,
paper membership, order, available count and source text. All **62 saved result
rows** are retained exactly, including the empty lists and the two one-hit lists.

Three evidence layers are kept separate:

- **Original QASPER annotations:** verbatim answers, evidence and annotation IDs,
  including conflicting or missing information. They are not new judgments.
- **Automatic facts:** original IDs/ranks/scores and exact case-sensitive text
  alignment after whitespace normalization. Evidence and existing Passage text
  are independently located in exported full_text; overlapping source spans are
  recorded. Partial overlap is not a claim that the complete evidence is present.
  Section-title metadata and figure/table references are handled separately.
- **Codex interpretation:** whether returned text supports an answer, possible
  explanations, and unresolved issues. All are pending human review. No human
  reviewer, confirmation date or human relevance label has been assigned.

These local alignments are not formal gold mappings, qrels or exhaustive
relevance coverage. The inspected original text is the pinned QASPER export,
not a newly inspected complete publisher PDF. Real quality metrics remain
unavailable and the evaluation protocol remains provisional.

### Source-grounded case observations

**C01 ? input triple and slot filling.** The QASPER answer maps relation
`R(x,y)` to a question with answer `y`. Its full Introduction evidence is in
`qasper-passage-v1-5cc660a2ccf6711c4b619805881c534603d80b48d6c88de63a72277bd1f5aa7b`,
an eligible candidate absent from both Top-5 lists. Dense #3 contains only the
evidence tail, not the full mapping statement. Nevertheless, the Approach
passage `qasper-passage-v1-7bc45a7f775256d5f953d348bbcf0b95eacbbf747d424c5b192472f59227e014`
at BM25 #4 / Dense #1 describes the relation/entity/sentence input, extracting
slot values, and translating a relation query into a question template. It
explicitly connects reading comprehension with the slot-filling challenge.
The Codex interpretation is that this offers an alternative support path in
both lists; absence of the original evidence paragraph alone does not establish
whole-question retrieval failure. A human should confirm the sufficiency of
this alternative and the interpretation of the question's "input triple".

**C02 ? n-gram similarity.** Both lists contain the IDF definition passage
`qasper-passage-v1-6ef2bc9d2a8e84fa46de70c956522a42b0fdd4326bdd0a4b1498498cee24cb25`
(BM25 #4 / Dense #1), which describes a "simple inverse document frequency
(IDF) based similarity score". Both also contain
`qasper-passage-v1-3ee3ac44c14c8731cbb2b6dfa96034e8b429938e0c7a3c61f62957b0c1196820`
(BM25 #3 / Dense #5), stating that the same metric applies to n-gram retrieval.
Thus both sets supply textual support for IDF-based similarity despite their
different first results. The original annotated extractive answer and body
contain `INLINEFORM`/`DISPLAYFORM` placeholders: the precise formula cannot be
recovered from these materials. That limitation is already in the source and
is not established as a ranking defect. Human review should distinguish the
IDF-based lexical approach from the separate dense-vector variant in the paper.

**C03 ? combined training objectives.** The original answer lists multilingual
NMT, natural language inference, constituency parsing and skip-thought vectors.
All four appear together in
`qasper-passage-v1-1f5e2d66e886958a635e569f6e60ec2e93663a187645eb9b49e9b611925775e6`
(BM25 #1 / Dense #3). The longer annotated paragraph spans two chunks, but the
answer list itself fits in this first chunk. Dense #1, headed Training Objectives
& Evaluation, discusses motivation and selection criteria without enumerating
the four objectives. Both Top-5 lists therefore contain the enumerated support;
a section title or first-result comparison alone would miss this distinction.
Human review should confirm that this four-item list answers the intended scope.

**C04 ? relations beyond binary.** The original annotation is `yes_no=true`
and `unanswerable=false`, but supplies **no evidence spans**. The exported
paper's `full_text=[]`; it has no indexed candidates and both saved lists are
empty with `paper_without_passages`. No supporting Passage ID can be established.
The unindexed abstract mentions considering all possible relations, which does
not explicitly establish relation arity. The affirmative answer is unverified
from this source material. This is an empty-source/no-supplied-evidence case,
not evidence ranked below Top-5, and does not prove the question unanswerable.

**C05 ? evaluation datasets.** The annotated answer is WN18 and FB15k. Its
`FLOAT SELECTED:` evidence resolves, after removing that literal marker, exactly
to the exported Table 1 caption, which names both datasets. The evidence source
is reliably located, but captions are outside the original full_text-only
indexing scope and have **no canonical Passage ID in this corpus**. Six body
sections have no paragraphs; only the Acknowledgments passage
`qasper-passage-v1-d1554ef289453c646428425c0a546bedf48033e20693dd900a4156d859d75c24`
exists and is returned at rank 1 by both methods. It names neither dataset.
The observed lack of support is therefore a corpus/candidate-scope limitation,
not a demonstrated ranking failure. Human review should confirm whether the
question intends the Table 1 benchmarks or every evaluation dataset.

**C06 ? baseline method.** The annotated text-baseline evidence is fully present
in the eligible Methods passage
`qasper-passage-v1-fb343232e83f3965662fae2299362e6abeab09a9ec506d77f3ab440b909f1959`,
which specifies embeddings, bidirectional LSTM, two dense layers and softmax,
and calls this setup its baseline. Neither Top-5 list returns it. Their ID sets
are disjoint, but neither is wholly devoid of relevant context: BM25 #3 describes
a neural-network approach for text, while Dense #1 describes the baseline's
in-domain train/evaluation setup. Both lack the retrieved architecture detail.
A separate annotation issue needs review: the original free-form answer says
there is no audio/face baseline, whereas BM25 #2/#3 quote the paper's
"baseline predictions with off-the-shelf tools for face and speech emotion
recognition". This tension must not be resolved by treating the annotation as
infallible or by calling all returned material incorrect. Whether the broad
neural-network description adequately answers the question remains a human
judgment; a specific ranking cause has not been established.

**C07 ? dataset size.** The annotated "8757 news records" occurs verbatim in
`qasper-passage-v1-5fe3a011ac60e7daa4e26a54ba1cbab81e1a33065b9de899eb925cb79f3aedc3`
(BM25 #3 / Dense #2), explicitly referring to the **preprocessed** dataset.
Both methods rank a dataset-overview paragraph first and also return a collection
paragraph reporting approximately 9,000 satirical and 11,000 legitimate tweets.
Both lists contain the direct annotated support, but the counts refer to
different processing stages. A human should preserve that qualification rather
than presenting the raw collection total as a contradiction or substituting it
for the annotated answer.

**C08 ? simpler models.** Two original annotations agree on BiGRUs with
attention, ROUGE, language models, and next-sentence prediction. Their four
section-title evidence strings are present in Passage metadata, not lost body
text; their supporting body paragraphs are present in four eligible passages:

- BiGRU: `qasper-passage-v1-2b1065ba6892583b4f372ed889e9c125df71a87fe72925b697ff3cb58714a1e4`.
- ROUGE: `qasper-passage-v1-177159334e9a6f31317ce17567694df834b4a20bdf2e3069f400de611da369e8`.
- LM: `qasper-passage-v1-8f5fce06afa70e04d7b739c533f0a51973c80982936ee74ec534ea10462583d2`.
- Next-sentence prediction: `qasper-passage-v1-89db3626917ecff084af0516cb69a672f01fa6a2c2c7c7df250ff4dec6fcee95`.

None of those four passages is in either saved Top-5. Alternative text still
matters: BM25 #1 discusses ROUGE as background; shared BM25 #5 / Dense #2 discusses
BiGRU models, and Dense #5 explicitly mentions BiGRU-ATT training. These give
partial contextual support but do not enumerate the four annotated baseline
families. The Codex reading is **incomplete support for the four-item answer
within the inspected Top-5**, pending human review; it is not zero support,
missing source evidence, or an established implementation defect. Generic query
wording and broad model-related content are possible explanations, not measured
causes. No extra retrieval or counterfactual ranking experiment was performed.

### Interpretation limits and human review checklist

These cases show differences in where useful text appears, alternative support,
partial support, and source availability. They do not establish that BM25 or
Dense is generally better, nor quantify how often any phenomenon occurs. Saved
scores are retained on their original scales and are not compared numerically
between methods. No Precision@K, Recall@K, MRR, formal qrels or full-corpus
quality conclusions were generated. No confirmed retrieval-code defect or new
deterministic blocker for the existing scoped Git delivery was identified.

Human review priorities (all still pending):

- C01/C03: confirm that the alternative explanation or short enumerated span
  sufficiently answers the question even when the complete annotated paragraph
  is not wholly returned.
- C02: confirm which retrieval variant is intended and whether the textual IDF
  description suffices; consult the original paper for any needed formula.
- C04/C05: distinguish no supplied evidence, absent full_text, and a locatable
  caption excluded from the original candidate scope. Do not relabel all as
  ranking failures or infer unanswerability from zero results.
- C06: resolve the audio/face-baseline annotation/body tension and decide the
  answer detail required by this broad question.
- C07: confirm that "dataset size" means the 8,757-record preprocessed set.
- C08: check the four baseline identities and whether the alternative returned
  mentions provide sufficient support for any subset or the complete answer.

### Local detailed materials and preservation

`results/p1-qualitative-20261017/` is ignored by Git. It contains:

- `selection.json`: the fixed question list and selection rules recorded before
  detailed annotation analysis; `provenance.json`: source paths and original
  recorded hashes, explicitly not recomputed as a new full inventory.
- `C01/` through `C08/`: `source.json`, `source_comparison.md`, `analysis.json`
  and `analysis.md`. These preserve full Top-5 IDs/order/scores/text, original
  QASPER annotations, source excerpts/coordinates, local evidence alignment,
  per-return support assessments and pending review judgments.
- C05/C08 `non-body-evidence-alignment.json`: caption and section-title handling
  with explicit candidate-scope distinctions.
- `README.md`, `human_review_checklist.md` and `verification.json`: navigation,
  review priorities, and the bounded facts/preservation checks.

The original three-case `qualitative_review.json` is retained unchanged as
historical candidate-only observation. This new phase extends it with annotated
post-hoc analysis, without changing the original experiment's annotation-free
query boundary. No algorithm or other-owner module was changed, no interface
tests were repeated, and no Git staging, commit, push, PR or ZIP packaging was
performed in this phase.

## Phase 2: P2 source review and delivery entry points

Review date: 17 October 2026 (Asia/Shanghai).
**Codex-assisted source review — unpublished draft.** This is a bounded P1
interface review, not a completed teammate peer review or P2 acceptance.
The original branch and all existing uncommitted work remain in place.

### Remote state and review scope

`git fetch origin --prune` succeeded. Fresh GitHub API reads of PR #5 and
`commits/main` were checked against the fetched refs. The initial sandboxed
fetch/API attempts failed; the authorized retries succeeded, so these are
current observations rather than copied historical status.

| Item | Observed value |
| --- | --- |
| Original worktree | `p1/week3-week4`, HEAD `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9`, existing unstaged/untracked P1 work |
| Fetched main and independent main API result | `6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c` |
| [P2 PR #5](https://github.com/CodeByVish/papergap-rag/pull/5) | Open, not merged; head branch `p2/week2-hybrid-integration` |
| P2 source reviewed | `0046e680fd361f90b608a949d2dd132d55db71aa` |
| Change from the previous real CLI checkpoint | None in the PR head or inspected main SHA |

The PR payload's base SHA is not used as the current main SHA, and its candidate
merge SHA is not treated as a landed commit. Source was read through immutable
`git show`/diffs and existing local P1 files. No branch checkout, merge, rebase,
production-code edit, or environment change was performed. The applicable main
`AGENTS.md` and `CONTRIBUTING.md` were read; the original old checkout has no
root `AGENTS.md`.

### Source findings and interface boundaries

P2 paths/line numbers below refer to **`0046e680...`**. Rows explicitly marked
local P1 refer to the existing uncommitted increment, not to that PR commit.

| Area | Finding and source location |
| --- | --- |
| Query and budgets | `src/retrieval/hybrid_retriever.py:30-49` forwards the original `query` and `paper_id` to each backend with `top_k=candidate_k`. It fuses the complete returned union and applies final `top_k` after fusion or reranking. `candidate_k` is a per-source budget, not a global union limit. Short results are valid; final size is at most `min(top_k, unique returned candidates)`. |
| Empty and paper scope | `hybrid_retriever.py:41-49` rejects any cross-paper candidate. `fusion.py:18-51` handles empty lists; `reranker.py:87-88` returns immediately for empty candidates. Missing/short candidates are not padded. P1 retrieves within the requested paper's index. |
| IDs, duplicates and order | `fusion.py:25-50` retains the original `Passage`, deduplicates by `passage_id`, rejects conflicting content/ranks/scores and uses the best rank for same-source repeated IDs. RRF ties use original ID order. `reranker.py:94-100` orders by reranker score, RRF score, then original ID. |
| Provenance and scores | `schemas.py:18-41` and `fusion.py:33-48` retain original BM25/Dense ranks and scores separately from `rrf_score`. `reranker_score` defaults to `None`; the scorer-free path does not execute reranking. `reranker.py:91-100` preserves the Passage and source scores while updating final rank/score. The schema does not separately retain an `rrf_rank` after reranking. |
| Fixed section callbacks (local P1) | `src/retrieval/bm25_retriever.py:63-109` filters exact section values before candidate truncation; BM25 statistics remain paper-wide. `dense_retriever.py:213-255` searches the paper index, filters sections before final truncation and handles unavailable sections. `agent_integration.py:47-72` binds a fixed section in separate callbacks for each request, including rewritten queries. |
| P2 external section support | `hybrid_retriever.py:10-11,30-32` accepts three query arguments; a caller can bind P1's section keyword with a closure or `partial`. `scripts/demo_hybrid.py:113-140` has no section argument/forwarding. Fixed request binding does not implement dynamic gap-based section selection. These are application boundaries, not P1 retrieval defects. |
| Real CLI and index mapping | `scripts/demo_hybrid.py:50-60` loads supplied Passage JSONL, constructs BM25 in memory, loads the saved Dense index, and calls `scripts/demo_p1.py:14-25` to compare the complete Passage mapping (including content/metadata). It does not load P1's saved BM25 snapshot. `scripts/build_indexes.py:17-54` validates immutable revision syntax, Passage schema and duplicate IDs. |
| Dense compatibility (local P1) | `dense_retriever.py:293-430` checks saved settings, requested model/revision, paper/ID mapping, FAISS file integrity, dimensions/row counts and normalized vectors. Loading reuses stored vectors. Dataset manifest/split checks belong to P1's adapter; generic `demo_hybrid.py` does not itself consume the QA/corpus manifests or enforce train-only selection. |
| Reranker dependency | `scripts/demo_hybrid.py:71-80` uses the PR's `BGEReranker` cache/offline keywords; `src/retrieval/reranker.py:18-51` forwards them to both model loaders. Main lacks those added constructor options. The full PR dependency set, not a copied CLI alone, is the reviewed CLI combination. Actual BGE reranker inference was not executed in this phase or the earlier P1 CLI smoke. |

No concrete P1-blocking defect was found within this scope. In particular,
`top_k > candidate_k` is legal and can return fewer than `top_k` results when
the union is small; this is a budget contract to communicate, not evidence of
incorrect truncation. These findings do not extend to every P2 script or model
quality. The Windows environment remains the existing papergap interpreter;
no macOS ARM64 lock or repair script was applied.

### Version-specific evidence reused, not rerun

| Combination | Evidence and scope |
| --- | --- |
| main `6fa06b5...` + P1 increment | Historical 13 targeted tests and real 4-train-question / 7-request / 15-round integration. Main exposes the actual Hybrid API and P4 control flow; P4 planner/mapper/critic/rewriter remain keyword mocks. This supports control-flow integration, not real critic or adaptive-RAG quality. |
| Full P2 `0046e680...` + P1 increment | Historical 4 CLI tests and 3 actual RRF requests, with candidate unions 24/28/0 and returned counts 5/5/0. `scripts/demo_hybrid.py` is available in this PR combination, not inspected main. The controlled scorer test is not a real BGE reranker run. |
| 100-question delivery package | A separate historical generation from root HEAD `5d3f447...` plus then-uncommitted files, identified by its own manifest/source snapshot below. It is not the full P2 PR worktree. |

`hybrid_retriever.py`, `fusion.py` and `schemas.py` are identical between the
inspected main and PR head. Among these core P2 modules plus `reranker.py`, only
the latter differs: the PR adds cache/offline forwarding. There is no newer PR
delta requiring another runtime check. Historical evidence remains attributable
to its original combinations; no tests, retrieval, encoding or index building
were rerun here. The earlier 51/76/264 totals also remain historical.

Historical evidence files remain under `results/p1-integration-20261017/`:
`p2/summary.json`, `p2/pytest-record.json`, `agent-final/trace.json` and
`final-verification.json`. Recorded compatibility uses the 32,073-Passage
development corpus and `BAAI/bge-small-en-v1.5` revision
`5c38ec7c405ec4b44b94cc5a9bb96e735b38267a` (384-dimensional normalized
IndexFlatIP vectors). These are reused recorded checks, not freshly recomputed
corpus/index hashes. No matching BGE reranker cache was available in the saved
run; this phase neither downloaded a model nor repeated cache discovery.

### Existing delivery package: accurate entry points

Workspace root: `E:\Lenovo\Desktop\papergap-rag`.
ZIP: `results/p1-retrieval-handoff-20261017.zip`.
Expanded directory: `results/p1-retrieval-handoff-20261017/`.
Both exist. The ZIP is 1,917,042 bytes with 32 entries under the
`p1-retrieval-handoff-20261017/` prefix. Only its entry list and stored manifest
were read; CRC/full-hash validation and packaging were not repeated.

All paths in this table are relative to the expanded directory:

| Entry | Purpose |
| --- | --- |
| `README.md` | Read first; package scope, schema and caveats |
| `samples/hybrid_nonempty.json` | Inspect a complete nonempty Hybrid record |
| `questions.jsonl` | Actual question list: `question_id`, `question`, `paper_id` only |
| `retrieval_bm25.jsonl` | Independent BM25 results |
| `retrieval_dense.jsonl` | Independent Dense results |
| `retrieval_hybrid.jsonl` | Real P2 RRF fusion results; no reranker execution |
| `run_manifest.json` | Generation versions, input provenance, configuration and source hashes |
| `code_snapshot/` | Exact source copies used at generation time |
| `provenance/passages.manifest.json` | Stored corpus manifest |
| `provenance/qasper_export.manifest.json` | Stored QA export manifest |
| `execution_trace.jsonl` | Recorded execution trace |
| `validation.json` | Existing package validation; not rerun in Phase 2 |
| `export_handoff.py`, `verify_handoff.py`, `package_handoff.py` | Archived helper scripts used for this historical package; retained with its provenance, not promoted to new production entry points or rerun during delivery |

Join each result file to the questions by original **`question_id`**, checking
`paper_id` and unchanged question text as well. Do not rely on row positions.
All result rows have `question_id`, `question`, `paper_id`, `retrieval_round`
and `retrieved_passages`. Native BM25/Dense hits contain `passage`, `rank` and
`score`; Hybrid hits contain `passage`, `rank`, `source_scores`, `rrf_score`
and `reranker_score`. Preserve original Passage IDs and nulls. Each method's
`retrieval_round=1` denotes one independent request, not successive Agent
rounds. Preserve rows whose `retrieved_passages` is empty.

The existing manifest/validation records 100 train questions per method,
485 returned passages and three empty results per method. Selection was all
three known empty-paper train questions plus the first 97 other train questions
by ID, then sorted together. It is a delivery sample, not a quality estimate.
The corpus/indexes/model weights are not bundled; this is not a standalone
runtime environment. The later eight-case qualitative analysis is separate.

Generation ran on 17 October 2026 from 13:15:51 to 13:16:04 +08:00. Its recorded
P1 HEAD is `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9` plus the then-uncommitted
increment; P3 is `499bb6d8ea2952f10e0499bfb8eb2986d683ba06`. The manifest has
**no P2 PR head field**. Its `code_source_sha256` and `code_snapshot/` identify
the executed sources. Targeted text comparison, normalizing line endings, found
the archived Hybrid/fusion/schema identical to reviewed `0046e680...`, but the
archived reranker lacks that PR's cache/offline options. Because `scorer=null`
and `reranker_executed=false`, this difference does not affect the delivered
RRF path. Do not relabel the ZIP as generated by the full PR head or latest main.
The archive, expanded files and original provenance were left unchanged.

Configuration was `top_k=5`, per-source `candidate_k=20`, `rrf_k=60`,
`section=null`, one round, no rewriting/retries, and no real reranker.
Keep `reranker_score=null`; these are observed run settings, not a frozen
team configuration, optimized parameters or a reranking experiment.

### Unpublished English P2 review draft

The complete reusable draft follows. It has not been submitted as a GitHub
review/comment or sent separately to another person. Its inclusion in P1
repository documentation does not imply a review request or recipient acceptance.

```markdown
Codex-assisted P1 interface review — unpublished draft

Reviewed PR #5 (https://github.com/CodeByVish/papergap-rag/pull/5), still open
on 17 October 2026, at 0046e680fd361f90b608a949d2dd132d55db71aa. Fetched main
is 6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c. Scope: P1 callbacks, candidate
budgets, paper/section scope, IDs/provenance, saved-index compatibility and the
real Hybrid CLI. No production code was changed. This is not a completed
teammate peer review or confirmation that P2 has accepted the handoff.

No concrete defect affecting the current P1 RRF delivery was found.
At the reviewed commit, src/retrieval/hybrid_retriever.py:30-49 forwards
query/paper_id unchanged and requests candidate_k from each source. Fusion
uses the deduplicated union; final top_k applies after fusion or reranking.
Short/empty returns are valid. Cross-paper candidates raise an error.
fusion.py:25-50 preserves original Passage IDs/content and source ranks/scores;
schemas.py:18-41 separates those from RRF and optional reranker scores.
The scorer-free path leaves reranker_score null. reranker.py:91-100 scores
the complete fused candidates before final truncation.

Local P1 callbacks filter exact sections before candidate truncation
(bm25_retriever.py:63-109; dense_retriever.py:213-255). Callers can bind a
fixed request section. P2's demo_hybrid.py:113-140 has no section argument;
dynamic section selection remains an application-layer follow-up, not a
P1 retrieval defect. P2/P4/P6 should agree on section forwarding and budget
semantics. candidate_k is per source; top_k is an upper bound. P2/P6 should
also agree how to display pre-reranking order if needed: source ranks and
RRF scores survive, but a separate rrf_rank is not stored.

demo_hybrid.py:50-60 loads saved Dense vectors, checks the full Passage
mapping via demo_p1.py:14-25, and builds BM25 from the supplied JSONL.
P1 supplies dataset-manifest/train-split validation outside this generic CLI.
Use the full PR dependencies: its reranker adds cache/offline constructor
options absent from main. Main plus P1 supports the Hybrid/Agent API;
the real Hybrid CLI was validated only with the complete PR plus P1.

The main and PR SHAs are unchanged from the historical checks: 13 tests and
7 Agent requests/15 rounds on main plus P1; 4 CLI tests and 3 real RRF
requests on the full PR plus P1. These were not rerun. P4 policies remain
keyword mocks; no real critic-quality or dynamic-section claim follows.
Real BGE reranking was not run; the saved record reports no matching cache.

Existing delivery: results/p1-retrieval-handoff-20261017.zip, expanded at
results/p1-retrieval-handoff-20261017/. Read README.md, run_manifest.json
and samples/hybrid_nonempty.json first. Join questions.jsonl to
retrieval_bm25.jsonl, retrieval_dense.jsonl and retrieval_hybrid.jsonl by
question_id; also check paper_id/question. The question list has only those
three fields. Each method is one independent retrieval_round=1.

The 100-train-question package was generated from P1 HEAD
5d3f4477f42887067bb4b3f8bd9231f1bc9289e9 plus then-uncommitted sources.
Keep its run_manifest.json/code_snapshot provenance: it records no P2 head.
Archived Hybrid/fusion/schema match the reviewed PR after line-ending
normalization; archived reranker differs. This does not affect scorer-free
RRF. Do not attribute the package to the full reviewed PR. It used final
top_k=5, per-source candidate_k=20, rrf_k=60, no section restriction and no
reranker. Preserve null reranker fields. These are run settings, not agreed
optimal parameters. validation.json remains historical evidence.

P2 handoff acknowledgment, section/parameter conventions, P3 gold mapping
and P6 metric protocol/backend remain follow-ups. Real quality metrics are
unavailable. Eight qualitative cases remain Codex-assisted analysis pending
human review, with no assigned reviewer/date. These follow-ups are not
automatic preconditions to opening a scoped P1 PR. Git delivery and branch
integration belong to the later phase; this draft remains local.
```

### Phase 2 checks and next-phase boundary

This phase performed remote/ref reads, immutable source review/diffs, inspection
of existing integration records, ZIP entry/manifest inspection, expanded-file
schema sampling, targeted comparison of four archived P2 source files, and
documentation checks. No new runtime tests or retrieval checks were warranted
by the unchanged reviewed versions. It did not repeat CRC/full-hash validation,
package generation, the 2,593-question run or interface tests.

Document checks passed: 12 package entries and four historical evidence paths
exist, Markdown fences are balanced, text has no replacement characters or
trailing whitespace, and `git diff --check` passed. HEAD remained `5d3f447...`
and the staging area remained empty. These are documentation/preservation
checks, not new runtime-test results.

Only this report and `docs/WEEKLY_TRACKER.md` were edited in Phase 2. No
deterministic blocker to a scoped P1 PR was identified. Phase 3 must still
reconcile the old P1 branch with main and review only the P1 Week 3/4 increment;
it must not import the complete P2 PR as P1 work. Required repository review
applies to eventual merge. Pending qualitative human review, P2 acknowledgment,
P3/P6 gold/metric inputs and application/parameter decisions are explicit
follow-ups, not automatic prerequisites to creating that P1 PR. No staging,
commit, push, PR/review/comment publication, reviewer request or external
message was performed. This phase ends with local uncommitted changes.

## Phase 3: Git delivery and final code validation

Date: 17 October 2026. This phase was explicitly authorized to commit the
complete P1 increment, merge main normally, push the P1 branch and create/update
a PR into main. The earlier no-delivery checkpoints are historical records.
No merge into main, automatic merge, force push, P2 review publication, reviewer
request or separate teammate message is part of this delivery.

### Saved scope and main integration

Repository: `CodeByVish/papergap-rag`; delivery branch: `p1/week3-week4`.
Fresh fetch/API checks found no existing remote branch or open PR for this head.
P2 PR #5 remained open at `0046e680fd361f90b608a949d2dd132d55db71aa`.

Delivery PR: [#8 — Deliver P1 Week 3/4 retrieval and agent integration](https://github.com/CodeByVish/papergap-rag/pull/8),
opened from `p1/week3-week4` into `main` after an ordinary push with upstream
tracking. It is open and not a draft; it has not been merged and automatic
merge is disabled. The first remote inspection confirmed all 15 intended
Files changed and no requested reviewers. The PR metadata records the current
head, including subsequent documentation-only commits linking this PR.

No workflow files are present in the inspected repository. GitHub reported
zero check runs and zero commit statuses; its aggregate status was `pending`
with no reported jobs. This is not a CI pass or evidence of a running job.
Local test results below remain the executed validation evidence.

- P1 feature commit: `bb064c130f54e3fe1c0c4ba7cc339c0104670749`,
  `feat(retrieval): add P1 development experiments and evaluation handoff`.
- Merged main: `6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c`.
- Normal merge commit: `bea053db9c785000307d0e528cb3fcff02a0cd27`.
  The merge had no conflicts and required no production-code repair.

The reviewed difference from main consists of exactly these 15 P1 files:

| Files | Delivered change |
| --- | --- |
| `src/retrieval/bm25_retriever.py`, `dense_retriever.py` | Exact section filtering before truncation; BM25 JSON persistence and validation; reuse of saved Dense vectors |
| `src/retrieval/experiment.py`, `evaluation.py` | Manifest-checked train input, experiment export/audit, independent label adaptation and provisional metrics boundary |
| `src/retrieval/agent_integration.py` | Bounded real-retrieval to mock-Agent control-flow check and trace |
| `scripts/run_p1_experiment.py`, `run_p1_integration.py` | Experiment/evaluation and existing-artifact integration entry points |
| `tests/test_p1_week4.py`, `test_p1_experiment.py`, `test_p1_evaluation.py`, `test_p1_agent_integration.py` | Offline regression and interface coverage |
| `README.md`, `docs/P1_EVALUATION.md`, `P1_WEEK3_WEEK4.md`, `WEEKLY_TRACKER.md` | Usage, evaluation boundary, historical evidence, qualitative summaries, handoff and unpublished P2 review draft |

The complete source tree for other owners remains identical to main, including
P2 Hybrid/fusion/reranker/schema and P3/P4 implementations. No P2 PR #5 commits,
CLI, lockfile, repair scripts or exclusive dependencies were brought in.
The generated ZIP, full results, detailed cases, corpus, indexes and model
cache remain ignored. Archived package helpers remain inside the ignored
package; their accurate entry points are documented above.

### Checks actually run on the integrated code

Interpreter: `E:\Miniconda\py311\envs\papergap\python.exe`.
Runtime checks used merge commit `bea053db9c785000307d0e528cb3fcff02a0cd27`;
subsequent delivery edits are documentation only. No real corpus retrieval,
passage encoding, real-index rebuilding, model download, parameter scan,
artifact re-export or ZIP repackaging was performed.

```powershell
$p1Python = 'E:\Miniconda\py311\envs\papergap\python.exe'
$env:HF_HUB_OFFLINE = '1'
$env:TRANSFORMERS_OFFLINE = '1'
& $p1Python -B -m pytest tests/test_p1.py tests/test_p1_week4.py tests/test_p1_experiment.py tests/test_p1_evaluation.py tests/test_p1_agent_integration.py tests/test_agent.py tests/test_p2.py -q -p no:cacheprovider
```

Result: **279 passed in 11.14 s**, zero failures/skips. These are the actual
affected P1 tests and main's Agent/Hybrid boundary tests on the merged code,
not a full-repository test run or a sum of historical counts. Dense tests use
fake encoders and synthetic data with real FAISS. No new tests were needed.

```powershell
$p1ChangedPython = @(
  'src/retrieval/bm25_retriever.py', 'src/retrieval/dense_retriever.py',
  'src/retrieval/agent_integration.py', 'src/retrieval/evaluation.py',
  'src/retrieval/experiment.py', 'scripts/run_p1_experiment.py',
  'scripts/run_p1_integration.py', 'tests/test_p1_week4.py',
  'tests/test_p1_experiment.py', 'tests/test_p1_evaluation.py',
  'tests/test_p1_agent_integration.py'
)
& $p1Python -B -m ruff check @p1ChangedPython
& $p1Python -B -m ruff format --check @p1ChangedPython
& $p1Python -B -m scripts.run_p1_experiment --help
& $p1Python -B -m scripts.run_p1_experiment evaluate --help
& $p1Python -B -m scripts.run_p1_integration --help
& $p1Python -B -m scripts.demo_p1 --help
& $p1Python -B -m scripts.run_agent_demo
```

Ruff check passed; all 11 changed Python files were already formatted. All four
help commands exited successfully, verifying default imports without unmerged
P2 dependencies. The existing synthetic Agent demo passed its three scenarios:
recovery in two rounds, exhausted budget in three, and empty retrieval in three.
This demo is controlled evidence, not a new real-retrieval experiment.
Local entry logs are in `results/p1-git-delivery-20261017/entry-checks.json`.

The staged inventory was checked explicitly before commit. Relative-to-main
file/tree checks confirmed no omitted P1 paths, generated artifacts or modified
other-owner implementations. Ignore rules and `git diff --check` passed.
Historical 13/4/51/76/264 counts remain attached to their original versions;
the earlier real main-plus-P1 and full-P2-plus-P1 runs were not repeated.
The optional `demo_hybrid` CLI still requires the full PR #5 combination;
the default P1/Agent commands above do not.

### Evidence and review status retained

The 100-question package remains from `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9`
plus then-uncommitted sources. Its stored manifest/source snapshot, rather than
any new delivery commit, identifies its generation. It used real RRF with
per-source `candidate_k=20`, final `top_k=5`, `rrf_k=60`, no section restriction
and no reranker; null reranker fields and original provenance are unchanged.
The package was not uploaded, resent or acknowledged by a recipient here.

Eight purposively selected train cases retain
**Codex-assisted qualitative analysis — pending human review**; no human
reviewer or date was assigned. The P2 English draft is included for review as
P1 documentation, not published as a P2 GitHub review/comment. Real quality
metrics remain unavailable and the evaluation convention provisional. P3 gold
mapping/coverage, P6 metric backend/protocol, P2 acknowledgment, outer section
forwarding/dynamic strategy, real reranking and parameter agreement remain
follow-ups, not automatic preconditions to this P1 PR.
