# Dense: retrieving paper chunks with semantic vectors

This guide explains the main idea, inputs, outputs and complete workflow of the project's `DenseRetriever`, distinguishing standalone Dense retrieval from the Dense branch inside Hybrid. It follows the current implementation and three-method retrieval configuration; the shared passage contract remains `v0-proposed`. Chinese version: [dense.md](dense.md).

## 1. Main idea

Dense retrieval encodes a question and each paper chunk into fixed-length numerical vectors, then ranks chunks by vector similarity. A pretrained model computes these vectors from text, aiming to assign higher similarity to semantically related questions and chunks without requiring identical keywords.

For example, a question asks `How does the model reduce overfitting?`, while a chunk says `We randomly disable neurons during training.` The encoder may recognize the connection despite the different terminology. Semantic similarity still does not guarantee a complete answer or correct interpretation of negation, numbers or experimental conditions.

The default model is `BAAI/bge-small-en-v1.5`, called through `SentenceTransformer`. The same encoder processes questions and chunks. The current retrieval code runs inference with pretrained weights; it performs no training or fine-tuning.

Let $q$ be a question, $p$ a chunk and $E$ the encoder. The code obtains and normalizes their vectors:

$$
\mathbf{v}_q=E(\text{instruction}+q),\qquad \mathbf{v}_p=E(p.\text{text}),\qquad \hat{\mathbf{v}}=\frac{\mathbf{v}}{\lVert\mathbf{v}\rVert_2}
$$

It then computes cosine similarity as the inner product of normalized vectors:

$$
\operatorname{score}(q,p)=\hat{\mathbf{v}}_q^\top\hat{\mathbf{v}}_p=\frac{\mathbf{v}_q^\top\mathbf{v}_p}{\lVert\mathbf{v}_q\rVert_2\lVert\mathbf{v}_p\rVert_2}
$$

Here, `instruction` is a retrieval instruction added only to the question. Higher scores rank first for that question. The equality between inner product and cosine similarity depends on both vectors being L2 normalized.

## 2. Inputs

### Index construction

`DenseRetriever(passages, ...)` receives an existing collection of `Passage` objects. P3 paper text comes from `data/processed/papers.jsonl`, and upstream code creates the chunks; Dense does not choose chunk boundaries. The current three-method configuration uses approximately $365$ words per chunk with $40$ words of overlap. These are project settings, not inherent Dense algorithm limits.

| Field | Type | Role in Dense retrieval |
| --- | --- | --- |
| `passage_id` | `str` | Globally unique identifier used for index row mapping and tie-breaking. |
| `paper_id` | `str` | Groups chunks into separate paper indexes and limits query scope. |
| `title` | `str` | Preserved for display and traceability; not appended to encoded text. |
| `section` | `str` | Preserved section information; not appended to encoded text. |
| `chunk_number` | `int` | Nonnegative chunk number retained in the record. |
| `text` | `str` | Nonempty chunk body; the only field encoded for a passage. |
| `previous_passage_id` | `str` or `null` | Optional preceding chunk ID; adjacent chunks are not added automatically. |
| `next_passage_id` | `str` or `null` | Optional following chunk ID; adjacent chunks are not added automatically. |

The P3 adapter projects only these eight public fields. Source positions, reference answers, gold evidence and human relevance labels do not enter the Dense index or similarity calculation. The caller separately retains additional fields needed for evaluation.

### Queries

The query interface is `retrieve(query, paper_id, top_k)`.

| Parameter | Type and constraint | Meaning |
| --- | --- | --- |
| `query` | Nonempty `str`, not whitespace-only | Original question text; the retriever adds a fixed instruction before encoding. |
| `paper_id` | Nonempty `str`, not whitespace-only | Search only this paper's chunks. |
| `top_k` | Positive integer, excluding booleans | Maximum number of returned chunks; each method currently returns $5$ in the three-method comparison. |

The current Dense interface has no `section` filter parameter. Section metadata accompanies results but does not automatically restrict retrieval to a section.

## 3. Outputs

A direct retrieval call returns a similarity-ranked `list[RetrievalHit]`. Each result contains:

| Field | Type | Meaning |
| --- | --- | --- |
| `passage` | `Passage` | Original chunk record, including the eight fields above and complete `text`. |
| `rank` | `int` | Final Dense rank, starting at $1$. |
| `score` | Finite `float` | Cosine similarity between the current question and this chunk. |

P3's `scored_ids()` converts these results into an ordered list of `(passage_id, score)` pairs without changing the ranking. The evaluator uses each ID to recover the complete chunk and its source positions.

Cosine scores mathematically range from $-1$ to $1$, subject to floating-point error in storage. They are neither relevance probabilities nor answer accuracy, and should not be directly added to or treated as sharing a scale with raw BM25 scores, RRF scores or reranker logits.

There is no minimum similarity threshold: zero and negative scores remain eligible. A paper with $N$ chunks returns $\min(\text{top\_k},N)$ results; a valid but unknown paper ID returns `[]`. Invalid arguments raise `ValueError`. Results sort by descending `score`, then ascending `passage_id` for ties. Even an entirely irrelevant candidate set can produce a full top-$K$ list.

## 4. Complete workflow

```text
Index construction
Paper text -> upstream chunking -> validate public fields and unique IDs
    -> group by paper_id; sort each group by passage_id ascending
    -> encode each chunk's text with BGE -> L2 normalization
    -> build one FAISS IndexFlatIP per paper; retain row-to-passage mappings
    -> optionally save indexes and metadata.json

Querying
query + paper_id + top_k
    -> validate arguments -> select the paper index; return [] if absent
    -> prepend the fixed instruction -> encode with the same BGE revision
    -> L2 normalization -> inner products against every chunk in this paper
    -> sort by score descending, passage_id ascending
    -> return at most top_k RetrievalHit objects

Downstream processing
Dense results -> standalone evaluation, or RRF fusion inside Hybrid
Evaluator -> recover full text and source positions by ID
    -> compare against evidence or human labels
```

### Step 1: prepare and group chunks

Upstream code cleans and chunks text before constructing `Passage` objects. The retriever rejects duplicate `passage_id` values, groups records by `paper_id` and sorts each paper's chunks by ascending `passage_id`. This order determines the mapping between FAISS rows and original chunks. A changed chunk size or candidate corpus requires indexes built for that new corpus.

### Step 2: load the encoder

The default encoder loads the model on its first encoding call. Its default cache is `.cache/huggingface/` under the project root. The current experimental configuration pins revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. Direct `DenseRetriever` callers can also supply a revision; initial loading resolves and records an immutable model commit.

Indexing and querying must use the same model, revision and encoding rules. Matching vector dimensions alone does not ensure compatibility. The code checks encoder identity and rejects changes after indexing. Tests can inject an alternative encoder with a declared identity; that is separate from the current real-model experiment path.

### Step 3: encode chunks and handle length

Only `text` is encoded for each chunk, without a query instruction or appended title or section. The code passes `prompt=""` to prevent `SentenceTransformer` from implicitly adding another prompt.

The default BGE path sets `max_seq_length=512`; the tokenizer truncates text exceeding this model input limit. The limit counts model tokens, including special tokens, and question inputs must also fit the instruction. Experimental word counts use whitespace separation, which differs from token counting: approximately $365$ words do not necessarily fit within $512$ tokens.

Each chunk is encoded as a single input. The implementation does not apply an internal sliding window or separately encode and aggregate the truncated remainder. Results and evaluation reports retain the complete `text`, so returned text may be longer than the text actually seen by the encoder. Experiment metadata records the truncation policy; this does not establish that truncation was checked for every chunk with the real tokenizer.

### Step 4: normalize vectors and build indexes

The code validates vector count, dimensions, numerical type and finiteness, and rejects zero vectors. Normalization uses `float64`, first scaling by the largest absolute component to avoid norm overflow, then converts the result into a contiguous `float32` matrix.

Each paper gets a `faiss.IndexFlatIP` containing its normalized chunk vectors; all papers share one encoder. This flat index performs exact inner-product search within the paper, rather than approximate nearest-neighbor search. The original chunk list maps index rows back to text and metadata.

### Step 5: encode the question

The retriever validates `query`, `paper_id` and `top_k`, then checks whether the paper exists. It encodes the question only if the matching index is present. The following instruction is prepended; the code's string includes a trailing space:

```text
Represent this sentence for searching relevant passages:
```

The same encoder produces the question vector, which is L2 normalized using the same rules as passage vectors.

### Step 6: score, sort and select

The code calls `index.search(query_vector, index.ntotal)` to obtain scores and row numbers for every chunk in the selected paper. It then sorts by descending score and ascending `passage_id`, finally taking `top_k`. Retrieving all candidates includes every tie at the $K$ boundary, so FAISS's internal ordering of tied items does not decide the final selection.

For $N$ chunks in the paper and vector dimension $d$, vector scoring costs approximately $O(Nd)$, followed by a full sort costing approximately $O(N\log N)$, excluding question encoding. `top_k` controls the output size; this implementation still scores all candidates.

### Step 7: deliver results or persist indexes

Standalone Dense retrieval returns `RetrievalHit` objects. Evaluation and answer generation belong to downstream modules. Dense itself does not read reference answers, decide whether evidence is sufficient or generate an answer.

Optional `save(directory)` writes per-paper vectors to files such as `paper-000000.faiss`. Its `metadata.json` stores model identity, encoding settings, vector dimension, complete passage row mappings and each index file's SHA-256. The destination must be new or empty. Index files do not include model weights.

`DenseRetriever.load(directory, ...)` restores saved vectors without re-encoding passages. It checks metadata, checksums, row mappings, index type, dimensions and normalization. The real encoder loads the saved model revision only on the first query, so index reuse still requires the corresponding model files. Model weights and indexes remain outside Git.

## 5. A hand-calculable example

Suppose the normalized question vector is $(1,0)$ and one paper has the following three chunks. These hypothetical two-dimensional vectors explain the calculation; they are neither real BGE outputs nor experiment results.

| Chunk ID | Normalized vector | Inner product with the question |
| --- | --- | --- |
| `A` | $(0.8,0.6)$ | $1\times0.8+0\times0.6=0.8$ |
| `B` | $(0.8,-0.6)$ | $0.8$ |
| `C` | $(-1,0)$ | $-1$ |

With `top_k=2`, the results are `A` and `B`, both scoring approximately $0.8$, with ranks $1$ and $2$. `A` wins the tie by ID. With `top_k=5`, only three chunks are available, so the results are `A`, `B` and `C`, including the negative score for `C`. Enough returned results do not establish sufficient evidence.

## 6. Current settings and the role inside Hybrid

| Setting | Current implementation or experimental configuration |
| --- | --- |
| Model | `BAAI/bge-small-en-v1.5`; fixed for the default real encoder. |
| Experimental revision | `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. |
| Device and encoding batch | `device="cpu"`, `batch_size=32` in the current three-method configuration. |
| Maximum input length | $512$ tokens for the default BGE path; no internal chunk sliding window. |
| Passage input | Only `text`, without the retrieval instruction. |
| Question input | Fixed retrieval instruction plus the original question. |
| Vectors and indexes | L2 normalization, `float32`, one `IndexFlatIP` per paper. |
| Scope and ties | Selected paper only; ascending `passage_id` for tied scores. |
| Model cache | `.cache/huggingface/`; experiments set `local_files_only=true`, requiring a prepared cache. |
| Standalone Dense results | Top-$5$ in the current three-method comparison; the interface accepts other positive integers. |
| Dense candidates inside Hybrid | Up to $20$ per call, then RRF with BM25 candidates using `rrf_k=60`, returning $5$ final results. |

`src/data/build_multi_retriever_pilot.py` shares the same sparse and dense indexes across BM25, Dense and Hybrid. Standalone Dense ranks by cosine scores. Hybrid applies RRF to the two rankings instead of adding raw BM25 and cosine scores. The current three-method pool builder does not enable reranking. The separate `hybrid_rerank` mode additionally calls a BGE cross-encoder; its logits are not the Dense scores described here.

The three-method configuration starts in `configs/annotation_pilot.json`; formal pool construction saves frozen settings and provenance. The `dense_model: null` entry in `configs/default.yaml` remains a shared configuration placeholder and does not mean the implemented model is undecided. See the [data guide](../../data/README.md) for authoritative freeze rules, provenance and artifact access, and the [evaluation protocol](../../docs/EVALUATION.md) for evaluation boundaries.

## 7. Running the existing entry points

Run the following commands from the project root in a Python environment with project dependencies installed. They use a synthetic fixture and do not read formal evaluation questions. `--local-files-only` requires complete model files for the pinned revision to be cached already.

First build indexes. `.cache/dense-demo/` must be new or empty. This entry point also validates BM25 index construction but persists only Dense indexes.

```powershell
python -m scripts.build_indexes --passages tests/fixtures/mock_passages.jsonl --output-dir .cache/dense-demo --device cpu --local-files-only
```

Then load the index and query using the same passage file:

```powershell
python -m scripts.demo_p1 --passages tests/fixtures/mock_passages.jsonl --dense-index-dir .cache/dense-demo --paper-id synthetic-ir --query "How are semantic vectors used for retrieval?" --top-k 5 --device cpu --local-files-only
```

The demo prints independent BM25 and Dense results with rank, passage ID, score, section and a text preview; it performs no Hybrid fusion. It warms up each backend once, then times one complete retrieval call, excluding model loading and index construction. One timing sample is not a performance benchmark. For real data, substitute the appropriate Passage JSONL and paper ID, ensuring that the query input file exactly matches the passages in the saved index.

## 8. Code references

- [dense_retriever.py](../../src/retrieval/dense_retriever.py): encoding instruction, normalization, paper indexes, exact retrieval, stable ordering, saving and loading.
- [schemas.py](../../src/retrieval/schemas.py): `Passage` and `RetrievalHit` fields; shared contracts remain `v0-proposed`.
- [chunk_size_retrieval.py](../../src/evaluation/chunk_size_retrieval.py): P3 field projection, retrieval mode selection, score adaptation and experimental metadata.
- [build_multi_retriever_pilot.py](../../src/data/build_multi_retriever_pilot.py) and [build_common_pool.py](../../src/data/build_common_pool.py): shared indexes for the three methods and formal common-pool construction.
- [hybrid_retriever.py](../../src/retrieval/hybrid_retriever.py) and [fusion.py](../../src/retrieval/fusion.py): RRF fusion of Dense candidates and the optional reranking entry point.
- [annotation_pilot.json](../../configs/annotation_pilot.json): current three-method retrieval parameters.
- [build_indexes.py](../../scripts/build_indexes.py) and [demo_p1.py](../../scripts/demo_p1.py): local build, load and query entry points.
