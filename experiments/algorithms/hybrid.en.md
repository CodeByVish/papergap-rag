# Hybrid: combining lexical and semantic retrieval

This guide explains the core idea, inputs, outputs and complete workflow of the project's `HybridRetriever`, following the current implementation and three-method retrieval configuration. The shared passage contract remains `v0-proposed`. Chinese version: [hybrid.md](hybrid.md).

## 1. Core idea

Hybrid runs BM25 and Dense for the same question within the same paper, then combines their candidates through Reciprocal Rank Fusion (RRF). BM25 scores term matches and helps locate textual clues such as terminology and model names. Dense scores cosine similarity between semantic vectors and can add relevant passages that use different wording. See [BM25.en.md](BM25.en.md) and [dense.en.md](dense.en.md) for their individual workflows.

Raw BM25 scores and Dense cosine scores do not share a scale. The implementation therefore calculates fusion scores from source ranks alone, without directly adding or normalizing raw scores. For a passage $p$, let $S(p)$ contain the sources that returned it:

$$
\operatorname{RRF}(p)=\sum_{s\in S(p)}\frac{1}{k_{\mathrm{RRF}}+r_s(p)}
$$

Here, $r_s(p)$ is the original one-based rank within source $s$, and $k_{\mathrm{RRF}}$ is the code's `rrf_k`, defaulting to $60$. Sources have equal weight. A source contributes $0$ if it did not return the passage. Higher ranks contribute more; a passage returned by both sources receives both contributions.

`rrf_k` smooths rank differences; it is not a candidate count. `candidate_k` limits candidates per source, while `top_k` limits final results. Hybrid aims to combine complementary retrieval clues, but improvements in evidence recall or answer quality require experimental validation.

## 2. Inputs

### Initialization inputs

`HybridRetriever(sparse, dense, *, scorer=None, candidate_k=20, rrf_k=60)` accepts prepared retrieval callbacks. It does not chunk papers or build indexes itself.

| Parameter | Type and default | Meaning |
| --- | --- | --- |
| `sparse` | Retrieval callback | The project uses `BM25Retriever.retrieve`. |
| `dense` | Retrieval callback | The project uses `DenseRetriever.retrieve`. |
| `scorer` | `PairScorer` or `None`, default `None` | Optional reranker exposing `score(query, texts)`; without it, only RRF runs. |
| `candidate_k` | Positive integer, default $20$ | Maximum candidates requested from each source. |
| `rrf_k` | Positive integer, default $60$ | Smoothing constant in the RRF formula. |

Each callback accepts `(query, paper_id, top_k)` and returns `list[RetrievalHit]`. Hybrid passes its `candidate_k` as the callback's `top_k`. Each hit contains the full `passage`, a one-based `rank` and a finite floating-point `score`.

Both sources should use the same passage corpus and ID mapping. The public `Passage` fields are `passage_id`, `paper_id`, `title`, `section`, `chunk_number`, `text`, `previous_passage_id` and `next_passage_id`; see [Dense inputs](dense.en.md#2-inputs) for their types and meanings. The complete passage record for a shared ID must agree across sources. Original text spans, reference answers, gold evidence and human labels stay on the evaluation side and do not participate in Hybrid retrieval or fusion.

### Query inputs

The query interface is `retrieve(query, paper_id, top_k=5, *, section=None)`.

| Parameter | Type and constraint | Meaning |
| --- | --- | --- |
| `query` | Nonempty, non-whitespace `str` | Both sources receive the same original question; Dense internally adds its fixed retrieval instruction. |
| `paper_id` | Nonempty, non-whitespace `str` | Both sources search only this paper. |
| `top_k` | Positive integer, default $5$ | Maximum final results. |
| `section` | Nonempty, non-whitespace `str` or `None` | Reserved section filter; no section restriction by default. |

`candidate_k`, `rrf_k` and `top_k` reject booleans. The Hybrid class itself does not require `candidate_k >= top_k`, but the experiment adapter imposes this constraint for Hybrid modes.

When `section` is provided, Hybrid forwards it as a keyword argument to both callbacks and checks the returned sections. The project's current `BM25Retriever.retrieve` and `DenseRetriever.retrieve` do not accept this argument, so passing it directly raises `TypeError`. The existing three-method path uses `section=None`. This reserved interface requires callbacks that implement section filtering before it can be used.

## 3. Outputs

The output is a `list[RetrievedPassage]` in final rank order, rather than a generated answer.

| Field | Type | Meaning |
| --- | --- | --- |
| `passage` | `Passage` | Complete original passage, including text and metadata. |
| `rank` | `int` | Final one-based rank; the reranked position when reranking is enabled. |
| `source_scores` | `dict[str, SourceScore]` | Only sources that actually returned this passage; current keys are `bm25` and `dense`. |
| `source_scores[source].rank` | `int` | Original one-based rank within that source. |
| `source_scores[source].score` | Finite `float` | Original source score for traceability; not used to calculate RRF. |
| `rrf_score` | Positive finite `float` | RRF score calculated from source ranks; retained after reranking. |
| `reranker_score` | Finite `float` or `None` | `None` without reranking; a raw logit with BGE reranking. |

If the deduplicated candidate union contains $U$ passages, the output contains $\min(\text{top\_k},U)$ results. When both callbacks respect their candidate limit, $U\leq 2\times\text{candidate\_k}$, giving at most $40$ unique candidates by default. Two empty source lists produce `[]`; one empty source still allows fusion of the other list. The existing BM25 and Dense retrievers return empty lists for valid but unknown paper IDs, so Hybrid also returns `[]`.

Without reranking, results sort by `rrf_score` descending and `passage_id` ascending. With reranking, they sort by `reranker_score` descending, then `rrf_score` descending and `passage_id` ascending. Neither RRF scores nor reranker logits are relevance probabilities or answer accuracy. There is no minimum relevance threshold: candidates with zero or negative upstream scores can still appear in final results through their ranks.

P3's `scored_ids()` converts results to ordered `(passage_id, score)` pairs while preserving final rank. It selects the reranker score when present, otherwise the RRF score. Zero and negative reranker logits are valid; only `None` falls back to RRF.

## 4. Complete workflow

```text
Preparation
Paper text -> upstream chunking into a shared Passage collection
    -> build BM25 term indexes and Dense vector indexes, or load saved Dense indexes
    -> supply both retrieve callbacks to HybridRetriever

Query
query + paper_id + top_k
    -> validate query parameters
    -> BM25: score and rank within the paper, up to candidate_k hits
    -> Dense: encode query, normalize and rank by cosine, up to candidate_k hits
    -> check candidate paper scope
    -> merge by passage_id; check content and within-source rank consistency
    -> calculate RRF from original ranks, retaining original ranks and scores
    -> sort by RRF descending, passage_id ascending
    -> no scorer: take top_k
    -> scorer enabled: rerank the entire candidate union, then take top_k
    -> return RetrievedPassage records for downstream evaluation or answer generation
```

### Step 1: prepare both indexes

Upstream processing cleans and chunks papers and assigns stable passage IDs. P3's adapter projects only the eight public fields into the retrieval interface. BM25 and Dense build their own paper-scoped indexes. The three-method pool builder reuses the same sparse and dense instances for standalone BM25, standalone Dense and Hybrid.

BM25 uses term statistics from passage `text`. Dense encodes `text` with `BAAI/bge-small-en-v1.5`, applies L2 normalization and stores vectors in FAISS `IndexFlatIP`. Titles, sections and neighboring passage IDs remain in returned records without being appended to either source's retrieval text. Neither source automatically expands neighboring passages. Hybrid has no separate third index.

### Step 2: validate the query and retrieve from each source

Hybrid validates the nonempty question and paper ID, positive integer `top_k` and optional `section`, then calls sparse followed by dense. The current calls are sequential. Both receive the same question and paper ID and return up to `candidate_k` candidates each, sorted by raw score descending and ID ascending, with original source ranks.

Dense internally prefixes the question with `Represent this sentence for searching relevant passages: `; passage text receives no such instruction. Its default input limit is $512$ tokens, with longer text truncated, while returned records retain the full text. Hybrid does not change either source's encoding, tokenization or truncation rules.

### Step 3: check scope and deduplicate by ID

Hybrid raises `ValueError` if either source returns a passage from another paper. RRF then merges records by `passage_id`. A passage appears only once in the candidate union while retaining each source's rank and original score.

If a source returns the same ID repeatedly, only its best original rank contributes. Contributions are not counted twice, and other ranks are not compressed. Conflicting passage content for one ID, assigning one rank to different IDs within a source, or conflicting scores for one ID at the same source rank all raise `ValueError`.

### Step 4: calculate and sort RRF scores

For each candidate ID, sum contributions from all sources that returned it. The code uses `RetrievalHit.rank`, rather than the hit's current list position, and does not recompute ranks from raw scores. Sorting by RRF descending and ID ascending produces a deterministic list with newly assigned consecutive final ranks.

### Step 5: optionally rerank, then truncate

With the default `scorer=None`, return the first `top_k` RRF results. With a scorer, score the entire deduplicated union before truncation; the RRF list is not first reduced to `top_k`.

The optional `BGEReranker` uses `BAAI/bge-reranker-base`. It pairs the question with each candidate's `text`, defaults to batches of $8$ pairs and tokenizes with padding and truncation at `max_length=512` tokens. It returns one raw logit per pair without a sigmoid probability conversion. Reranking requires exactly one finite score per candidate, otherwise it raises an error. Results sort by reranker score, RRF and ID, receive new final ranks and retain their source information and original RRF scores.

### Step 6: deliver traceable results

The caller receives a final passage list that can be serialized to JSON, or converted by P3 into ID/score pairs and joined with complete text and evidence spans. Hybrid does not assess answer sufficiency, read gold evidence or generate answers. Fusion and reranking cannot recover passages outside the retrieved candidate union. Candidate count, chunking and model truncation jointly constrain the final results.

## 5. A worked example

Suppose `rrf_k=60` and each source returns $3$ candidates: BM25 returns `A, B, C`, while Dense returns `B, D, A`. Letters below denote passage IDs.

| Passage | BM25 rank | Dense rank | RRF calculation | Approximate score |
| --- | --- | --- | --- | --- |
| `A` | $1$ | $3$ | $1/61+1/63$ | $0.032266$ |
| `B` | $2$ | $1$ | $1/62+1/61$ | $0.032522$ |
| `C` | $3$ | Not returned | $1/63$ | $0.015873$ |
| `D` | Not returned | $2$ | $1/62$ | $0.016129$ |

The final RRF order is `B, A, D, C`. With `top_k=2` and no reranking, the output is `B, A`. With reranking enabled, all of `A, B, C, D` are scored first, and the final order may change.

## 6. Current project settings and entry points

| Item | Current setting or behavior |
| --- | --- |
| Retained three-method configuration | `configs/annotation_pilot.json`: `mode="hybrid"`, `candidate_k=20`, `rrf_k=60`, `top_k=5`. |
| Chunking | About $365$ words with $40$ words of overlap; project settings, not inherent Hybrid limits. |
| Dense model revision | `BAAI/bge-small-en-v1.5`, revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. |
| Three-method reranking | In three-method mode, `build_multi_retriever_pilot.py` supplies no scorer and does not enable BGE reranking. |
| Formal four-method evaluation | `configs/annotation_four.json` freezes the added BGE reranker; `python -m src.data.build_common_pool run --four` reruns all methods into the current verified `annotation_common_v3/` pool. Full settings, fields and reproduction: [data guide](../../data/README.md). |
| Optional experiment modes | `hybrid` uses RRF alone; `hybrid_rerank` applies BGE reranking to the entire fused candidate union. |
| Model lengths | Dense defaults to $512$ tokens per input text; BGE reranking defaults to $512$ tokens per question/passage pair. Words and tokens are different units. |

With matching Passage JSONL and saved Dense indexes available, run `scripts/demo_hybrid.py` from the project root. Replace the placeholder paths and paper ID below with actual values:

```powershell
python -m scripts.demo_hybrid --passages "path/to/passages.jsonl" --dense-index-dir "path/to/dense-index" --query "What is the main contribution?" --paper-id "paper-id" --candidate-k 20 --rrf-k 60 --top-k 5 --local-files-only
```

The demo checks that the input passages match the saved index mapping. It runs RRF by default; add `--bge` to enable reranking. `--local-files-only` requires the necessary models to be cached already. The output JSON includes settings, model revisions, per-source candidate counts, unique candidate count, results and timing. Timing measures one complete retrieval call after one warm-up, excluding model and index loading. One timing sample is not a performance benchmark.

## 7. Implementation references

- [hybrid_retriever.py](../../src/retrieval/hybrid_retriever.py): query orchestration, parameter and scope checks, optional reranking entry point.
- [fusion.py](../../src/retrieval/fusion.py): RRF formula, deduplication, consistency checks and tie handling.
- [schemas.py](../../src/retrieval/schemas.py): `v0-proposed` input and output structures.
- [reranker.py](../../src/retrieval/reranker.py): BGE pair scoring and final reranking.
- [build_multi_retriever_pilot.py](../../src/data/build_multi_retriever_pilot.py) and [annotation_pilot.json](../../configs/annotation_pilot.json): shared indexes and current three-method settings.
- [chunk_size_retrieval.py](../../src/evaluation/chunk_size_retrieval.py): experiment modes, parameter constraints and ID/score adaptation.
- [demo_hybrid.py](../../scripts/demo_hybrid.py): saved-index query entry point and timing policy.
