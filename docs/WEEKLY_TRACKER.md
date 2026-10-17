# Weekly tracker

Update this file after the weekly meeting. Link to concrete issues, PRs, artifacts or run IDs.

> Current P1 delivery: [Phase 3](#p1-phase-3-git-delivery). Earlier local-only,
> uncommitted and deferred-delivery statements describe their original phases.

| Week | Dates | Exit checkpoint | Status |
| --- | --- | --- | --- |
| 1 | 14–20 Sep | Rubric interpretation, owners, compute, interfaces and split policy | Not recorded |
| 2 | 21–27 Sep | Provisional corpus, independent retrieval, pilot candidates | Not recorded |
| 3 | 28 Sep–4 Oct | Retrieval baselines, annotation pilot, final chunker/corpus freeze | Not recorded |
| 4 | 5–11 Oct | One complete query in Streamlit | Not recorded |
| 5 | 12–18 Oct | Frozen held-out pool and annotation guidelines | Not recorded |
| 6 | 19–25 Oct | 2,000 blind judgments, agreement, adjudication, system freeze | Not recorded |
| 7 | 26 Oct–1 Nov | Final comparisons and analysis | Not recorded |
| 8 | 2–6 Nov | Clean setup, report PDF and links verified | Not recorded |
| Submission | 7 Nov | Blackboard submission before 11:59 PM SGT | Not recorded |

## Meeting actions

| Task / issue | Owner | Due | Required input | Reviewable output | Blocking? | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Confirm rubric document/record units | Team | Week 1 | Instructor clarification | Both interpretations confirmed; see REQUIREMENTS.md | No | Confirmed 16 Sep |
| Confirm compute and evaluator access | P5/P6 | Week 1 | GPU access and judge backend | Feasibility note | Yes: inference setup | Open |
| Fill remaining names and backup owner | Team | Week 1 | Member agreement | Updated README | No | Open |

## P2 Week 1 progress

Fusion, deduplication, proposed schemas, mock handoff and BGE CPU smoke test are implemented on `p2/week1-fusion-reranking`. See [P2 handoff](P2_WEEK1.md). 17 tests passed. Interface agreement with P1/P3/P4 remains pending; this does not mark the whole team checkpoint complete.

## P1 Week 1 / Week 2 progress

This records the historical Week 1/2 verification of P1's independent retrieval
work; later real-data progress is recorded in the Week 3/4 section below. It
does not mark the team's Week 1 or Week 2 exit checkpoints complete.

| Deliverable | Status | Evidence / remaining dependency |
| --- | --- | --- |
| Shared retrieval interface | Implemented | BM25 and dense return the existing `RetrievalHit` schema with original `Passage` fields and IDs. |
| BM25 retrieval | Implemented and tested on synthetic data | Per-paper indexes, parameter validation, stable IDs, filtering and deterministic ranks; `src/retrieval/bm25_retriever.py`, `tests/test_p1.py`. |
| BGE dense retrieval and FAISS | Implemented and tested on synthetic data | Query-only instruction, L2 normalization, per-paper `IndexFlatIP`, finite scores and deterministic top-K; `src/retrieval/dense_retriever.py`. |
| FAISS mapping and persistence | Implemented and tested | Explicit row-to-Passage mappings, save/load without re-encoding passages, model/encoding metadata and consistency checks. |
| P2 callback compatibility | Verified by regression tests | Both retrievers can be used by the existing `HybridRetriever`; P2 algorithms remain unchanged. |
| Real BGE model smoke check | Verified on synthetic passages | `BAAI/bge-small-en-v1.5`, revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`, CPU; separate from fake-encoder unit tests. |
| Reproducible build and sample-query commands | Verified on synthetic data | `scripts/build_indexes.py` and `scripts/demo_p1.py` ran successfully with the pinned real BGE model from the local cache; see the verification evidence below. |
| Preliminary synthetic latency | Measured | One warm-up followed by one timed `retrieve` per retriever: BM25 0.088 ms; dense 7.636 ms. This is a local smoke measurement on 8 synthetic passages, not a real-corpus benchmark. |
| P3 corpus integration | Blocked on P3 data | P3 real corpus integration is still pending. The available fixture has 2 synthetic papers and 8 passages. |
| Real-corpus latency | Blocked on P3 data | Synthetic timing cannot establish real-corpus performance. |
| Week 3 retrieval evaluation | Planned for Week 3 | Precision@K, Recall@K, MRR and formal retrieval failure analysis have not been performed. |

### P1 verification evidence

Interpreter: `E:\Miniconda\py311\envs\papergap\python.exe`, Python 3.11.16. Both test commands below used this interpreter with `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`:

| Command | Passed | Failed | Skipped | Reported duration |
| --- | ---: | ---: | ---: | ---: |
| `python -B -m pytest tests/test_p1.py -v` | 122 | 0 | 0 | 5.68 s |
| `python -B -m pytest -q` | 139 | 0 | 0 | 5.72 s |

All 112 pre-existing P1 cases remain; 10 command-line cases were added. The full suite includes the 17 P2 cases. Dense unit tests use deterministic fake encoders and real FAISS; they do not require downloading or running the real embedding model.

The separate real-model check ran the exact build and demo commands in the [README](../README.md#p1-retrieval-week-1--week-2), with `--local-files-only`, CPU and revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. The build produced indexes for 2 synthetic papers / 8 passages with 384-dimensional embeddings under `indexes/p1-week2-synthetic`. The demo loaded these indexes, queried `synthetic-ir` with `Which method uses sparse term matching for passage retrieval?` and `top_k=3`, and returned:

| Rank | Passage ID | BM25 score | Dense cosine score |
| --- | --- | ---: | ---: |
| 1 | `synthetic-ir-001` | 4.270201 | 0.865788 |
| 2 | `synthetic-ir-002` | 0.000000 | 0.706013 |
| 3 | `synthetic-ir-003` | 0.000000 | 0.621847 |

The demo used `time.perf_counter` for one measured `retrieve` after one warm-up per retriever: BM25 **0.088 ms**, dense **7.636 ms**. Dense timing includes query encoding; both timings exclude model loading, passage encoding and index construction. These single-query synthetic measurements do not establish performance on P3's real corpus.

Local ignored artifacts are `results/p1-week2-build.json` and `results/p1-week2-demo.txt`; rerun the README commands to regenerate the outputs. At this historical Week 1/2 checkpoint, P3 real corpus integration was still pending and no real-corpus retrieval metrics or Week 3 evaluation had been completed. See the later progress below for the current state.

## P1 Week 3 / Week 4 progress

Latest status: see [17 October integration checkpoint](#p1-dependency-integration-checkpoint-17-october-2026). The earlier runs below retain their original evidence and dependency status.

Owner: Junlin Yin. Work is on `p1/week3-week4`, based on the complete P1 Week
1/2 implementation at `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9`. The upstream
P3 worktree is pinned to `499bb6d8ea2952f10e0499bfb8eb2986d683ba06`. See
[commands, contracts and verification](P1_WEEK3_WEEK4.md).

| Deliverable | Status | Evidence / remaining dependency |
| --- | --- | --- |
| P3 data preparation | Verified locally on real QASPER | Unchanged download/export/sample/corpus/check commands in an independent ignored worktree. QASPER revision `fdc9d8214fbab5dd782958601db4d678e6934a54`. |
| Real development corpus input | Verified | 32,073 unique passages / 1,168 indexed papers; train + validation text, 200/40 word chunking. Existing P1 Passage schema accepts all rows; no empty text or invalid neighbor mappings. |
| Development query boundary | Implemented and tested | Train-only, 2,593 questions; manifest/hash/split checks. No held-out queries or annotations used for retrieval experiments. Policy remains `v0-proposed`. |
| Index reuse and stable callbacks | Implemented and tested | Dense reload reuses saved passage vectors. BM25 JSON snapshot reload validates configuration and rebuilds its in-memory term index. Original three-argument P2 callbacks remain valid. |
| Optional section filtering and caller-supplied query rewriting | Implemented and tested at P1 boundary | Exact section matching before top-K, whole-paper BM25 statistics, stable ranks and original IDs. P4 supplies rewritten queries. P2/P4 section forwarding still needs owner integration. |
| Result and latency exporter | Implemented and tested | `scripts/run_p1_experiment.py`: ranked results, per-question/method zero-hit records, configuration, hashes and retrieve-only mean/p50/p95 timings. |
| Complete real-corpus indexes | Built, saved and reloaded | 32,073 passages / 1,168 papers / 384 dimensions with pinned BGE on CPU; Dense at `indexes/p1-week3-week4-development`, BM25 at `indexes/p1-week3-week4-bm25`. BM25 pre/post-save results match for all 2,593 train questions. |
| Real BM25 and Dense candidate baselines | Completed locally | All 2,593 train queries at K=5: 12,941 rows per method, 5,186 query logs including six method-level zero-hit records. `results/p1-week3-week4-development/{results.jsonl,queries.jsonl,run.json}`. |
| Initial real-data latency | Measured | Mean BM25 0.128309 ms / Dense 7.030325 ms; p95 0.208000 / 8.106740 ms. One sequential pass with one warm-up per backend, CPU, four torch intra-op threads; Dense includes query encoding. Not a repeated benchmark. |
| Missing source paper diagnosis | Verified | Train paper `1801.07804` has `full_text=[]` in both source and export; its three questions remain eligible and must be reported as zero-hit cases. |
| Saved-run audit and candidate-count diagnosis | Implemented; uses existing results | Audit the complete 2,593-question rankings without rerunning retrieval. Both methods have count distribution `0:3, 1:1, 2:1, 3:0, 4:2, 5:2586`; all seven short cases match the paper's available candidate count. Full question IDs, source diagnoses and three unlabelled train-query observations are recorded in [the P1 report](P1_WEEK3_WEEK4.md#complete-audit-of-results-shorter-than-k). |
| Provisional P1 metric tooling | Local implementation; not a frozen P6 protocol | Optional independently supplied JSONL/TREC qrels feed provisional Precision@K, Recall@K and MRR@K. The no-qrels path exports an explicit unavailable status. Synthetic tests verify calculation behavior only; see [P1 evaluation](P1_EVALUATION.md). |
| Gold relevance mapping and real retrieval quality | Blocked on P3 and P6 | No gold evidence-to-chunk mapping in inspected P3 code and no P6 metric backend in fetched `origin/main`. Real Precision@K, Recall@K, MRR, nDCG and labelled failure analysis remain unreported despite the new local tooling. |

### Historical Week 3 / Week 4 regression verification

All commands used `E:\Miniconda\py311\envs\papergap\python.exe`, Python
3.11.16, with `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`.

| Command | Passed | Failed | Skipped | Duration |
| --- | ---: | ---: | ---: | ---: |
| `python -B -m pytest tests/test_p1.py tests/test_p2.py -q` (initial baseline) | 139 | 0 | 0 | 6.07 s |
| `python -B -m pytest tests/test_p1.py tests/test_p1_week4.py tests/test_p1_experiment.py -v` | 185 | 0 | 0 | 6.89 s |
| `python -B -m pytest -q` | 202 | 0 | 0 | 6.84 s |

These are the recorded results of the original real-data implementation
session, not reruns of the current audit/evaluation changes. Ruff check and
format check passed for its six changed/new Python files. The
original P1/P2 tests and shared schema are unchanged. These offline tests use
fake encoders with real FAISS and do not replace real-model validation. This
P1 record does not mark the team-wide Week 3/4 checkpoints complete.

The real full-index three-query smoke and full experiment were separate
processes and agreed on IDs and scores within 1e-6. Every exported result was
checked against the original corpus for paper membership, ID, rank and score
validity. Data and output hashes were verified. See
`results/p1-week3-week4-final-validation.json` and the linked P1 report for
the sample query and complete command lines. The earlier Week 1/2 note that
P3 real corpus integration was pending is superseded by this real-data run;
gold mapping, quality evaluation and cross-owner agent integration remain open.

### Historical saved-run audit and evaluation follow-up

This follow-up reuses the completed run at
`results/p1-week3-week4-development`; it does not create a new retrieval run,
rebuild embeddings or remeasure latency. Its newly executed pre-change
baseline was `python -B -m pytest -q`: **202 passed in 6.13 s**, zero failures
or skips, using the same papergap Python 3.11.16 interpreter. That baseline
does not verify the subsequently added evaluation implementation.

The 24-result shortfall per method is fully accounted for: 15 unavailable
slots from three zero-candidate questions, plus nine from four papers with
2/1/4/4 candidates. All original questions remain present. Zero candidates
and unanswerable questions are distinct concepts; no relevance labels are
inferred from candidate counts. Inspection of three train-only cases shows
rank and section differences between BM25 and Dense, but does not assign
gold labels or call either method correct. The full audit table and case
descriptions are in [P1 Week 3/4](P1_WEEK3_WEEK4.md).

Recomputed from the original query logs, the timings are:

| Method | Mean | p50 | p95 | p99 | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: |
| BM25 | 0.128309 ms | 0.120100 ms | 0.208000 ms | 0.280972 ms | 0.495000 ms |
| Dense | 7.030325 ms | 6.933000 ms | 8.106740 ms | 8.852712 ms | 12.176300 ms |

These summarize the original single pass and include zero-hit calls. They
are not new measurements or a repeated performance benchmark.

The new audit/evaluation entry point is:

```powershell
& 'E:\Miniconda\py311\envs\papergap\python.exe' -B -m scripts.run_p1_experiment evaluate --run-dir results/p1-week3-week4-development --output-dir results/p1-week3-week4-evaluation-final --evaluation-k 5
```

The four local artifacts are `audit.json`, `counts.jsonl`, `evaluation.json`
and `provenance.json`. The original retrieval files remain unchanged. Real
metrics stay unavailable without matching independent gold qrels; provisional
P1 scoring code and synthetic fixtures do not remove that dependency.

The earlier upstream check after fetch inspected main
`44c112f265709fff76484dabb603d073ab141480`, P3
`499bb6d8ea2952f10e0499bfb8eb2986d683ba06`, and P2
`3fd9becd6fbfd22c3136a6c25df4ee7a716569ad`. P3 has internal chunk coordinates
and evidence statistics, but no gold mapping. Main's evaluation/agent/generation
packages remain empty placeholders. No P4/P5/P6 remote branch is present in
the fetched heads. P2's three-argument Hybrid callbacks do not forward section
requests; real P2/P4 integration and protocol review are still pending. These
observations concern the inspected repository, not collaborators' unpushed work.

Final verification of this follow-up used the same explicit Python 3.11.16
interpreter with offline Hugging Face/Transformers settings:

| Command | Passed | Failed | Skipped | Duration |
| --- | ---: | ---: | ---: | ---: |
| `python -B -m pytest tests/test_p1_evaluation.py tests/test_p1_experiment.py -v` | 76 | 0 | 0 | 3.49 s |
| `python -B -m pytest -q` | 264 | 0 | 0 | 8.05 s |

The final audit command above actually completed with `valid` status: all
5,186 query/method records match the expected candidate counts, with 12,941
results per method and no unexplained missing/duplicate records. The three
original run files remain hash-identical. The final independent directory
contains the four generated reports and a separate `qualitative_review.json`
record; real quality remains `unavailable` with null metrics. No real queries,
embeddings or latency measurements were rerun. The new 62 cases include
synthetic arithmetic, qrels adapters, invalid-input boundaries and saved-run
CLI integration; they do not establish real QASPER relevance quality.

Ruff check/format check passed for the five Python files changed in this
follow-up. `git diff --check` passed (only existing LF-to-CRLF notices).
Existing retrieval implementations and all other owners' code were preserved.
Gold mapping, P6 protocol/backend alignment, and real P2/P4 section forwarding
and agent integration remain external dependencies. No work was staged,
committed, pushed or opened as a PR.

### Final P1 interface handoff and review preparation

This bounded pass preserved all prior local changes and production code. It
added two tests to `tests/test_p1_week4.py` and the
[section handoff and delivery notes](P1_WEEK3_WEEK4.md#section-callback-handoff-to-p2p4).
The exact signature is keyword-only `section: str | None = None`: `None`
means the whole selected paper, strings match exactly without trimming or
case conversion, blank/non-string values raise `ValueError`, and unmatched
valid names return no results.

| Handoff item | Final status |
| --- | --- |
| P1 direct paper/section filtering | Implemented and tested; original three-argument callbacks preserved. |
| Bound P1 callbacks through current P2 | Interface-level verification completed using `functools.partial`, real Hybrid/RRF, BM25/FAISS and a deterministic fake encoder. Candidate/final K and interleaved query/paper/section requests are checked. |
| P2/P4 application forwarding | Pending. P2's outer API does not accept section; owners must forward the chosen section (or None) to both callbacks per request. No real agent/reranker end-to-end section run is claimed. |
| Real corpus retrieval and quantity audit | Previously completed; reuse `results/p1-week3-week4-evaluation-final`. No new real retrieval or repeated count investigation in this pass. |
| Independent evaluation tooling | Completed provisionally; JSONL/TREC completeness follows explicit manifests and per-question declarations, never format alone. |
| P3 labels | Pending matching question/paper/Passage IDs, exact corpus/chunking provenance, mapping coverage/failures and annotation completeness. |
| P6 agreement | Pending K/MRR cutoff, Precision denominator, macro averaging and policies for unanswerable/missing/mapping-failed/incomplete labels. Real quality metrics remain unavailable. |
| Team corpus/split freeze | Not declared; existing development convention remains proposed. |

The only pytest run in this last pass was:

```powershell
& 'E:\Miniconda\py311\envs\papergap\python.exe' -B -m pytest tests/test_p1_week4.py -q -p no:cacheprovider
```

Actual result: **51 passed in 0.32 s**, zero failed/skipped. Ruff check and
format check passed for that file. The earlier **76 passed** focused suite
and **264 passed** full suite above are retained historical evidence, not
rerun results. README/CLI paths, the final diff, ignored generated artifacts
and an empty staging area were checked. No production or other-owner module
was changed in this pass.

At that historical fetch, HEAD and `origin/p1/retrieval` both equaled `5d3f447`;
`origin/main` was `44c112f`, three Week 1/2 commits behind. The then-proposed temporary target was `p1/retrieval`. That recommendation
is superseded by the 17 October checkpoint: Week 1/2 has merged and the
Week 3/4 increment should now be reviewed against latest main. The complete review-file inventory,
label-ready command, English commit message and PR draft are in the
[final delivery notes](P1_WEEK3_WEEK4.md#final-interface-and-delivery-review).
All work remains local and unstaged; no commit, push or PR was performed.

## P1 dependency integration checkpoint: 17 October 2026

This checkpoint supersedes earlier remote-state and integration-pending notes.
The original `p1/week3-week4` branch remains at `5d3f447` with local unstaged
changes. No staging, commit, push or PR was performed.

| Remote item | Verified state / commit |
| --- | --- |
| Latest main / P4 #6 | #6 merged 17 October; main `6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c` |
| P1 #4 / P3 #2 | Both merged 14 October; P1 `5d3f447`, P3 `11bfbf1` |
| P2 #5 | Open; head `0046e680fd361f90b608a949d2dd132d55db71aa` |
| P6 #7 | Open; head `82f95d4400ec7c3b0433b16204304bf59f41c0b2` |

| New work | Actual evidence / limit |
| --- | --- |
| Protected existing work | Initial modified/untracked files backed up; 1,208 pre-existing data/index/result hashes recorded. All 1,208 hashes match at the final check. Full experiments and quantity audits were not rerun or replaced. |
| Latest main plus P1 | Detached `.cache/p1-main-20261017`, main plus tracked P1 patch and clearly P1 untracked sources/tests. Shared README/tracker content compared with upstream before reconciliation. |
| Actual Hybrid -> Agent | Real BM25/BGE/FAISS -> main HybridRetriever -> build_agent_graph/AgentState. Four fixed train questions, seven invocations, fifteen rounds; all checks passed. |
| Request-scoped sections | Actual Approach, Model, Acknowledgements and Results section names read from corpus, held across rewrites; whole-paper and known empty-paper paths also passed. No claim of dynamic gap-driven section selection. |
| Trace and isolation | Original/rewritten query reaches P1; original paper/Passage IDs, candidate/final counts, source ranks/scores and retry budget checked. Shared-index interleaving plus repeated original graph gives identical traces. |
| Controlled missing branch | Two new synthetic interface tests cover accumulation 4 > per-round top_k 2, first-occurrence dedup/provenance, two different rewrites, and same-graph question/paper/empty isolation. Not real retrieval quality evidence. |
| Complete P2 PR #5 CLI | Separate full-head worktree `.cache/p1-p2-20261017` plus P1; actual RRF CLI ran Q1/Q2/known-empty Q0. Candidate unions 24/28/0, returns 5/5/0. IDs/scope/order/counts/provenance checks passed. |
| Reranker / section limits | No matching local BGE reranker revision; no real rerank run/download. P2 CLI has no section parameter. No Mac environment or repair script used. |
| P3/P6 labels and metrics | No reliable gold evidence-to-Passage mapping, relevance completeness declarations, or P6 metric backend found. Real quality remains unavailable, protocol provisional. |
| P6 UI review | Read-only: independent Lucene + global FAISS IndexedRetriever with chunk_id, no paper/section request fields, different model/index contract, no returned source ranks/scores. This is not P1 reuse. |

Q1/Q2/Q3/Q0 full IDs, exact queries, section/count table, commands and limits
are in [the current P1 report](P1_WEEK3_WEEK4.md#latest-dependency-integration-17-october-2026).
New ignored evidence lives under `results/p1-integration-20261017/`, especially
`agent-final/trace.json` and `p2/summary.json`; existing production artifacts
remain in their original directories.

Actual targeted verification, with the specified Windows papergap interpreter:

| Combination | Command / result |
| --- | --- |
| main `6fa06b5` + P1 | `python -B -m pytest tests/test_p1_agent_integration.py tests/test_agent.py -q -p no:cacheprovider`: **13 passed in 0.47 s** |
| P2 `0046e68` + P1 | `python -m pytest -q tests/test_hybrid_cli.py`: **4 passed in 20.03 s** |
| Real checks | Agent: **7 requests / 15 rounds passed**; P2 CLI: **3 requests passed** |
| New Python files | Ruff check and format check passed in main combination |

There was no new full-suite run. Historical 51, 76 and 264 counts above are not
current-main results. The final real Agent trace is a repeat after adding
explicit paper/budget assertions; the initial trace is retained separately.
P4 planner/mapper/critic/rewriter are still keyword mocks, so this establishes
real retrieval into Agent control flow, not critic or complete adaptive quality.

Concrete owner inputs remain: P2 reviews #5 and agrees section/candidate
forwarding; P3 supplies canonical ID gold mappings, provenance, coverage and
completeness; P4 owns real reasoning/rewrite policy and any future dynamic
section contract; P6 owns the UI adapter and agreed metric protocol/backend.
Suggested UI connection points are `src/ui/services.py:get_retriever` and
`src/ui/app.py` retrieval, with provenance-preserving DTO conversion before
`src/generation/prompting.py:build_messages`. Other-owner code is unchanged.

The [updated PR draft](P1_WEEK3_WEEK4.md#proposed-commit-and-pr-handoff) now
targets **main** and only the Week 3/4 increment; Week 1/2 is already merged.
P1 is ready for scoped code review against the inspected main. Branch refresh
and required owner review are still needed for a later Git delivery; this
checkpoint deliberately leaves the original branch and staging area unchanged.

## P1 fixed-sample qualitative follow-up

**Codex-assisted qualitative analysis — pending human review**

Eight train questions were fixed before detailed annotation reading: three
previously inspected questions, the known empty and one-passage papers, and
three cases selected by saved BM25/Dense ID overlap. This is purposive sampling
for explanation, not a representative quality sample; no case was replaced or
added after fixation. Full question IDs and per-case findings are in
[the P1 report](P1_WEEK3_WEEK4.md#fixed-sample-qualitative-analysis-of-saved-baselines).

Only the original independent BM25/Dense Top-5 were read. No retrieval, index
construction, encoding, tuning or Hybrid/Agent experiment was run. Answers and
evidence were accessed after filtering to the fixed train cases, solely for
post-hoc analysis. All 62 saved result rows were checked against the original
run; source support, alternative support and missing/out-of-scope material were
kept distinct. Findings include alternative support despite missing annotated
passages (C01), source formula placeholders (C02), shared answer lists at
different ranks (C03), no full_text/evidence (C04), caption-only evidence outside
the candidate policy (C05), annotation/body tension (C06), raw versus processed
dataset counts (C07), and incomplete support for four baseline families (C08).

The new ignored directory is `results/p1-qualitative-20261017/`. It contains the
fixed selection, original annotations, full Top-5/source comparisons, separate
automatic facts and Codex judgments, and an unset human-review checklist.
No human reviewer/date or relevance labels were assigned. These local text
alignments do not supply formal qrels, exhaustive relevance coverage or a P6
protocol; real quality metrics remain unavailable and the protocol provisional.

The original run, indexes, prior review and existing delivery ZIP were preserved;
the ZIP was not rebuilt and does not include this documentation addition. No
retrieval implementation or other-owner module changed, no interface tests were
repeated, and no deterministic retrieval-code blocker was identified. The
annotation/body tension and answer sufficiency judgments remain human-review
items. All changes remain local and unstaged; this phase ends without Git delivery.

## P1 Phase 2: P2 source review and package entry points

On 17 October 2026, fetch and fresh GitHub API reads confirmed main
`6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c` and open P2 PR #5 head
`0046e680fd361f90b608a949d2dd132d55db71aa`. Both match the earlier integration
checkpoint. The original `p1/week3-week4` branch remains at `5d3f447...` with
its existing uncommitted P1 increment; it was not switched or merged.

[The P1 report](P1_WEEK3_WEEK4.md#phase-2-p2-source-review-and-delivery-entry-points)
now records the bounded source review, exact package entry points and a complete
**Codex-assisted, unpublished English P2 review draft**. No concrete defect
affecting current P1 RRF delivery was found. Per-source candidate budgets,
final result bounds, paper guards, ID/provenance preservation and null reranker
fields are consistent with existing evidence. P1 fixed-section callbacks work
before truncation; P2 CLI section forwarding and dynamic section selection
remain application-level follow-ups. The CLI requires the full PR dependency
combination; it is not present in inspected main.

The existing ZIP is `results/p1-retrieval-handoff-20261017.zip`; its expanded
directory has the same stem. Start with `README.md` and `run_manifest.json`.
The actual question list is `questions.jsonl`; join by `question_id` to
`retrieval_bm25.jsonl`, `retrieval_dense.jsonl` and `retrieval_hybrid.jsonl`.
The package's original source snapshot/provenance remains authoritative:
P1 HEAD `5d3f447...` plus then-uncommitted files, no recorded P2 PR head.
Its Hybrid/fusion/schema match reviewed P2 source, but its unused reranker
differs. Do not relabel the package as produced by the full reviewed PR.
Hybrid used real RRF with no reranker; keep null scores and describe 20/5/60
only as candidate/final/RRF run settings, not frozen optimal parameters.

This phase performed read-only remote/source/artifact inspection and document
checks. No runtime tests, retrieval, encoding, index building, model downloads,
CRC/full-hash validation or packaging were repeated. The 13/4-test integration
results and earlier 51/76/264 totals remain historical, version-specific evidence.
Only the P1 report and this tracker changed in this phase; production code and
other-owner modules are untouched. No review was published or sent, and P2
acceptance is not claimed.

Eight qualitative cases retain **Codex-assisted qualitative analysis — pending
human review** with reviewer/date unset. P2 acknowledgment, P3 gold mapping,
P6 metric backend/protocol, section strategy and parameter conventions remain
follow-ups; real quality metrics are unavailable. They are not automatic
preconditions to opening a scoped P1 PR. No new deterministic delivery blocker
was found. Branch integration and Git delivery remain for Phase 3; nothing was
staged, committed, pushed or published in this phase.

## P1 Phase 3: Git delivery

On 17 October 2026, the complete 15-file P1 increment was saved as
`bb064c130f54e3fe1c0c4ba7cc339c0104670749`. Main
`6fa06b5ae89a270bc7e5e9b407b998fce3d10e8c` was merged normally into
`p1/week3-week4` as `bea053db9c785000307d0e528cb3fcff02a0cd27`, without conflicts
or production-code fixes. Relative to main, only the reviewed P1 source,
scripts, tests and documentation differ. Other-owner implementations and
shared schemas match main; the unmerged P2 PR #5 was not imported.

Actual validation on the integrated code: **279 affected P1/Agent/Hybrid tests
passed in 11.14 s**, Ruff check/format passed on all 11 changed Python files,
four default P1 CLI help checks passed, and the existing synthetic Agent demo
passed its recovery, budget-exhaustion and empty-result scenarios. These are
new scoped checks, not a full-suite claim or aggregated historical totals.
No real retrieval, corpus encoding, index rebuilding, model download or
packaging was repeated. Commands, exact scope and preserved historical evidence
are in [the Phase 3 report](P1_WEEK3_WEEK4.md#phase-3-git-delivery-and-final-code-validation).

The existing ZIP and results remain ignored, unchanged and local. Their source
is still `5d3f447...` plus the then-uncommitted files, not this delivery commit
or the full P2 PR. Hybrid package results are RRF-only with null reranker fields;
20/5/60 are recorded run settings, not agreed optimal parameters. No package
upload, teammate message, P2 review/comment or reviewer request is implied.

Eight qualitative cases remain **Codex-assisted qualitative analysis — pending
human review**. P2 acknowledgment, P3 gold mapping/coverage, P6 metric backend/
protocol and outer section/parameter decisions remain follow-ups; real quality
metrics are unavailable and the protocol provisional. They do not automatically
block opening the scoped P1 PR. No PR merge or automatic merge is authorized.
