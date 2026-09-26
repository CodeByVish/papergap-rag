# P2 Week 1 — fusion and reranking

Owner: Vishakha. Implementation is on `p2/week1-fusion-reranking`.

## What you are building

BM25 and dense retrieval produce different score scales. Reciprocal Rank Fusion (RRF) combines their **ranks**, using `sum(1 / (60 + source_rank))` for each passage. A passage found by both sources receives both contributions. Duplicate IDs within one source contribute only once, using their best rank. Ties use passage ID for reproducibility.

A cross-encoder then reads each question and candidate passage together and scores their relevance. It is more expensive than rank fusion, so it runs on retrieved candidates rather than every corpus passage. The BGE implementation follows the [official model card](https://huggingface.co/BAAI/bge-reranker-base#usage-for-reranker): inference mode, raw sequence-classification logits and a 512-token input limit. These logits are not probabilities. Long question/passage pairs are truncated.

## Run it

From the repository root, with Python 3.11:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-p2.txt
python -m pytest -q
python -m scripts.demo_p2
```

The default demo uses fixed mock scores, not BGE, and never downloads a model. Its passages and scores are synthetic. For a real BGE CPU run (first execution downloads weights):

```bash
HF_HOME="$PWD/.cache/huggingface" python -m scripts.demo_p2 --bge --output results/p2-bge-smoke.json
```

Use `--revision <model-commit>` to pin weights. CPU is the default for this small check; the Python class also accepts an explicit device. Model caching stays in the ignored project directory with the command above. The full project does not need to be installed for these P2 tasks.

## Files and handoff

| File | Purpose |
| --- | --- |
| `src/retrieval/schemas.py` | Proposed passage, source-hit and final-result models |
| `src/retrieval/fusion.py` | RRF and deduplication |
| `src/retrieval/reranker.py` | Lazy BGE loading and reranking with injectable scorer |
| `src/retrieval/hybrid_retriever.py` | Connects two retriever callbacks to fusion/reranking |
| `tests/fixtures/mock_retrieval_results.json` | P1-shaped synthetic rankings |
| `tests/fixtures/mock_reranked_results.json` | P4 handoff with explicitly mock scores |
| `tests/test_p2.py` | Offline correctness and integration tests |

Junlin supplies callbacks with signature `retrieve(query, paper_id, top_k) -> list[RetrievalHit]`. Ranks are one-based and authoritative; raw scores are retained without normalization. Distinct passages must not share a rank within a source. The callback must enforce paper scope; hybrid retrieval rejects cross-paper output. Empty results are allowed. Unknown-paper behavior needs agreement with P1 (the mock callbacks return an empty list).

Ananya can call `HybridRetriever(...).retrieve(query, paper_id, top_k)` and consume `list[RetrievedPassage]`. Each result contains the full passage, final rank, original source ranks/scores, RRF score and nullable reranker score. Serialize using `model_dump()` or `model_dump_json()`. `scorer=None` selects fusion-only behavior. Every unique fused candidate is reranked before final top-K selection; fewer than K available passages returns fewer than K results.

The mock JSON file wraps the result list in metadata (`query`, `paper_id`, `scorer`, `synthetic_passages`). This wrapper belongs to the demo; the retrieval API returns the list itself.

## Review before freezing

- P1 and P3: approve passage schema, rank rules, stable IDs and error behavior.
- P4: approve nested `passage` output and required trace fields.
- Team: these schemas are a proposal, not evidence that collaborators have agreed.
- P2 Week 2: integrate real retrievers, measure candidate sizes and latency, and select a pinned model revision. Section filtering and performance tuning are not implemented yet.

Passing a three-passage smoke test establishes that the model loads and scores pairs. It does not establish retrieval quality on QASPER.

## Verified locally

- 17 offline tests passed; Ruff checks and `pip check` passed.
- Real BGE CPU smoke test completed on three synthetic passages.
- Model revision: `2cfc18c9415c912f9d8155881c133215df768a70`.
- Python 3.11; Transformers 4.57.6; PyTorch 2.14.0; Pydantic 2.13.5.
- Ranked sections / raw logits: results (-1.9851), setup (-3.2678), method (-9.7260).
- Local outputs: `results/p2-bge-smoke.json` and `results/p2-environment.txt` (ignored by Git).

## Team contract decisions and P3 integration

P2 proposes these defaults for Week 1: two named sources (`bm25`, `dense`), one-based source ranks, finite raw scores, opaque passage IDs, selected-paper retrieval, positive top-K, and empty lists for no matches. Unknown-paper behavior remains an explicit P1 decision. Final ranking retains both source scores plus RRF and nullable BGE scores. Initial candidate count is 20 per source and final top-K is 5; these are development defaults, not tuned settings.

P3's open PR #2 defines the same eight passage fields in `src/data/schemas.py`, with stricter validation. It uses opaque hashed IDs: never parse IDs to infer paper or section. Its `chunk_number` resets within each source container, so the three independent sections in our mock fixture each use chunk number zero. After the P3 contract lands and is reviewed, consolidate on its canonical Passage model rather than maintaining two independent definitions. Until then, P1 can pass serialized passage dictionaries matching these fields. Passing an instance of P3's different Pydantic class directly is not the agreed integration path.

P3 has implemented sample-generation tooling on its branch; that does not establish that the full corpus or chunking choices are frozen. P2 can continue with mocks or provisional samples now. Final reproducible comparisons require the same frozen corpus/IDs/index version across systems, real P1 callbacks, a fixed split policy and P6's metric conventions.
