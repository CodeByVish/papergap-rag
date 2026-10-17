# PaperRAG UI

Run commands from the repository root. All Streamlit presentation code lives in
`src/ui/`; retrieval and generation live in their existing `src/` packages.

## Launch

Activate your virtual environment (see the root README). For a new environment
with the optional Pyserini backend, use Python 3.12 and Java 21, as recommended
by its linked installation guide.
For just the UI, without downloading retrieval dependencies:

```bash
python -m pip install -r requirements-ui.txt
python -m streamlit run src/ui/app.py
```

Open http://localhost:8501. The app opens without credentials or indexes and
shows a setup checklist. It does not invent sample answers. Stop with Ctrl+C.

## Enable real answers

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`.
   Set `api_key`, `base_url`, and `model` for at least one provider (`qwen`,
   `grok`, or `groq`). Use the endpoint and model available to your account. Keep this
   ignored file private. The sidebar displays the configured model.
   For Groq, configure `[llm.groq]` using the example endpoint and a model
   available to your account, then select **groq** in the sidebar.
   Groq is separate from **grok**, which uses xAI.
2. Install the retrieval dependencies:
   `python -m pip install -r requirements-indexes.txt`.
   Pyserini also needs Java 21; consult
   [Pyserini's installation instructions](https://github.com/castorini/pyserini#installation).
3. Prepare `data/chunks.jsonl`: one nonempty passage per line, with unique
   `chunk_id`, nonempty `paper_id` and `text`, and preferably `title`,
   `section_path` (list of strings), `page_start`, `page_end`, and `source_url`.
   Use the schema in the implementation plan. Existing P3 `passage_id` records
   need an explicit export to this format. Exclude evaluation questions/answers.
4. Build indexes offline using the same corpus and embedding model:

```bash
python scripts/export_pyserini.py --chunks data/chunks.jsonl --output data/pyserini_collection
python -m pyserini.index.lucene --collection JsonCollection --input data/pyserini_collection --index indexes/sparse/lucene --generator DefaultLuceneDocumentGenerator --threads 4 --storeRaw
python scripts/build_dense_index.py --chunks data/chunks.jsonl --output indexes/dense --model sentence-transformers/all-MiniLM-L6-v2
python -m streamlit run src/ui/app.py
```

The dense builder writes `chunks.faiss`, `row_ids.json`, and `config.json` together.
Update `[rag]` in secrets if you change paths or the embedding model. Relative
artifact paths resolve from the repository root. Restart after rebuilding indexes
to clear cached resources. Index creation never runs inside the UI.

## Ask and inspect

Select a configured provider, choose 3–10 evidence passages, then submit a question
in the bottom input. Retrieval searches the entire corpus, fuses BM25 and dense
rankings, and sends the selected passages to the provider. Name papers in your
question when comparing them; this baseline has no strict paper/year filter.

Answers use `[E1]` citations matching the **Sources and evidence** cards. Expand
sources to read passages and open paper links. Enable **Show diagnostics** for
latency, chunk IDs and RRF scores. Unknown or missing citation labels trigger a
warning; label checking does not prove that a passage supports a claim.

Only the latest question/result is kept in session memory. Changing display
settings does not call the API again; a new submitted question does. **Clear
answer** removes the displayed result. Failed generation retains retrieved
sources. No persistent chat history, uploads, adaptive agent loop, or reranker
is enabled in this baseline.

The app selects the first configured provider. Without indexes, it defaults to
**Direct chat**, which calls the selected model without paper evidence or citations.
Choose **Paper RAG** for retrieval-backed answers after building the indexes.
The input stays editable during setup; submitting with incomplete configuration
shows an actionable message without calling the provider. Authentication, rate limits, connection
failures and empty responses produce UI messages without raw exception details
or credentials. Dense retrieval always finds nearest neighbors, so inspect the
evidence even if a question is outside the corpus.

## Verification and hosting

```bash
python -m pip install pytest
python -m pytest -q tests/test_ui.py tests/test_p2.py
```

UI tests use Streamlit AppTest with fake retriever/provider boundaries; they do
not download models or call a paid API. Real retrieval additionally needs the
index artifacts, Java and model weights. The full application dependency file
is `requirements.txt`; the optional Lucene adapter adds `requirements-indexes.txt`.

For hosting, use `src/ui/app.py` as the entry point, install the optional index
dependencies and compatible Java, provision the artifacts, and set deployment
secrets. A host without Java cannot run this Lucene backend.
