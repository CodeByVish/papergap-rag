# NLP Scientific Paper RAG UI

From the repository root on the prepared Apple M5:

```bash
./scripts/p6-local.sh start
```

Open http://127.0.0.1:8501. The launcher supplies the corpus, indexes, samples and
Ollama configuration. See [the local E2E guide](../../docs/P6/P6_REAL_ENV_E2E_GUIDE.md)
for their locations, all environment variables, setup/debug commands and the
future school GPU connection.

## Interaction

The left drawer contains the product title and **ⓘ How to use**, followed by
Connection, Search scope, **History directly below Search scope**, and Advanced
settings. The main area shows the question input, Ask question, examples, then
one submitted question and its Answer. No workspace creation is required.

The heading is **Ask the paper collection** for All papers,
**Ask Paper 'Selected paper title'** for One paper (ID fallback if no title is supplied),
and **Generate from prepared evidence** in Demo record mode. **Browse all
examples** is the only example entry point; no standalone example buttons remain.

1. Keep **All papers** for corpus search, or choose **One paper** and its title/ID.
   Scope changes apply to the next submission. Legacy services without
   `corpus_search` require a paper selection.
2. Type into **Your question**, or open **Browse all
   examples**. The library groups corpus topics and paper-specific questions;
   paper-specific options show both title and ID. **Use this question** fills the
   editable draft without submitting. In corpus mode it includes the paper
   reference without changing the scope. A paper filter limits the library to
   matching examples.
3. Click **Ask question** and wait. Requests are synchronous and non-streaming;
   no automatic POST retries or cancellation. Every question is independent;
   history is not sent to the model.
4. Read the submitted question and **Answer**, then any validation explanation.
   **Evidence needs review** means an answer retained warning-level issues; open
   **What was flagged?** for exact details. A validator block shows the accepted
   refusal, with rejected text separately labelled. No status certifies accuracy.
5. Expand **Sources** for titles/IDs, sections and passages, **Pipeline details**
   for supplied retrieval/critic events, and **Debug information** for IDs,
   timings and raw metadata. Candidate rankings and fusion/reranking scores are
   not currently supplied by the API.
6. Open a previous result from **History**; only one result is displayed and
   browsing does not run inference. **+ New question** clears the draft/result
   view and keeps history. Manual retry explicitly links another execution of
   the latest matching submission; timeout means outcome unknown.
7. Under **Advanced settings**, choose runs and download JSON for reporting.
   Export before **Clear history**, which deletes all local session runs/drafts.
   Limits are 10 internal mode/scope contexts and 50 attempts per context;
   refresh/reconnect may lose history. Export omits the agent block and sensitive
   keys but retains answer/provenance/evidence content. Timings measure answer
   HTTP waiting/processing, not isolated model inference; citation timing is separate.

**Advanced settings → Input mode → Demo record** generates from a local original
AgentState input. It does not perform fresh retrieval or rerun the agent. The
record's own question/paper identity is preserved; switch back to Free question
for the full pipeline. Use `P5_RECORDS_PATH` only for this optional mode.

## Independently managed API

The UI is a lightweight P5 HTTP client. It imports no models/indexes/retrieval
libraries. The reusable legacy provider adapters remain for existing callers.

```bash
python3 -m venv .venv-ui
source .venv-ui/bin/activate
python -m pip install -r requirements-ui.txt
export P5_API_BASE=http://127.0.0.1:8000
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

`P5_API_BASE` defaults to localhost:8000. `P5_RECORDS_PATH` optionally points to a
nonempty JSON array/JSONL of original exported inputs, not answer captures or the
corpus. Semantic record validation belongs to P5. `P6_SAMPLES_PATH` supplies the
optional sample JSONL; `P6_PAPER_CATALOG_PATH` supplies local ID-to-title labels
when `/papers` returns IDs only. Real data and credentials stay outside Git.

`P5_ANSWER_TIMEOUT` defaults to 120 seconds (range 120–3600); the prepared launcher
sets 900 seconds for local LLM calls. Connection timeout is 5 seconds and auxiliary
read timeout is 10 seconds. An authenticated service requires both `P5_API_TOKEN`
and `P5_AUTH_HEADER`; use `P5_AUTH_SCHEME=Bearer` only for a confirmed bearer API.
No token is required for the default local service. Saved launcher configuration
wins over stale terminal exports; use private overrides as described in the guide.

## Verification

```bash
.venv-p6/bin/python -m pytest -q tests/test_ui_api_client.py tests/test_ui_view_models.py tests/test_ui_record_loader.py tests/test_ui_conversation_state.py tests/test_ui.py tests/test_ui_p5_smoke.py
```

The default HTTP test starts a localhost synthetic fixture, not a real model.
The opt-in running-service test requires configured API and `P5_RECORDS_PATH`:

```bash
P5_RUN_SMOKE=1 python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

It makes two actual record-generation calls; it does not verify fresh retrieval
or semantic correctness. The [P6 handoff](../../docs/P6/P6_UI_handoff.md) describes
ownership, transport contracts and remaining GPU checks.
