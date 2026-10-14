# Weekly tracker

Update this file after the weekly meeting. Link to concrete issues, PRs, artifacts or run IDs.

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

This records P1's independent retrieval work; it does not mark the team's Week 1 or Week 2 exit checkpoints complete.

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

Local ignored artifacts are `results/p1-week2-build.json` and `results/p1-week2-demo.txt`; rerun the README commands to regenerate the outputs. P3 real corpus integration is still pending. No real-corpus retrieval metrics or Week 3 evaluation have been completed.
