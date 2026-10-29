# P6 UI handoff to P5

Date: 2026-10-29 (Singapore). Branch: `P6/UI-port-integration`.
Status: UI implementation and local tests complete; **actual P5 service integration
and real-model E2E are pending**. This handoff does not certify cluster deployment.
Use the final branch commit containing this file; base commit is
`10e52e926cc6f22395fe8fc180dd7c114950195a`.

## What P6 delivers

- `src/ui/app.py`: lightweight Streamlit client for P5's four endpoints.
- Separate HTTP client, response rendering models, local exported-record loader,
  session/workspace/run tracking and JSON timing export under `src/ui/`.
- Normal/warning answers, three refusal reasons and validator-block presentation,
  original rejected answer, citation text with ID-only fallback, and diagnostics.
- Independent questions in paper-bound workspaces, distinct execution IDs, explicit
  retry lineage, session isolation, timeout outcome-unknown behavior and limits.
- Tests, a synthetic HTTP fixture, and an opt-in actual P5 mock-service smoke test.

P6 does not deliver a model service, retrieval implementation, tunnel, GPU job or
new backend conversation API. Existing generation/retrieval modules are unchanged.

## Required P5 delivery before integration

Please supply the compatible service branch/commit, `docs/P6_UI_CONTRACT.md`,
`docs/DEMO_OPTION_C.md`, `examples/demo_ui_responses.json`, capture script,
service dependency/launch instructions and a small approved exported AgentState
input file outside Git. Those artifacts were absent from this checkout and its
cached P5 branch at implementation time. No P5-captured sample was hand-edited.

The standalone handoff command `PYTHONPATH=src python -m nlp_p5.server --backend mock`
was not runnable here because that package is absent. Please confirm the actual
command for the delivered shared repository; do not substitute a guessed import.

## Install and launch on P5's laptop

Keep the working service/model environment separate from the lightweight UI env.
From the repository root on macOS/Linux:

```bash
python -m venv .venv-ui
source .venv-ui/bin/activate
python -m pip install -r requirements-ui.txt
export P5_API_BASE=http://127.0.0.1:8000
export P5_RECORDS_PATH=/absolute/local/path/to/exported-agent-states.jsonl
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

On Windows PowerShell:

```powershell
python -m venv .venv-ui
.\.venv-ui\Scripts\Activate.ps1
python -m pip install -r requirements-ui.txt
$env:P5_API_BASE = 'http://127.0.0.1:8000'
$env:P5_RECORDS_PATH = 'C:\local\exported-agent-states.jsonl'
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

Open `http://127.0.0.1:8501`. P5 first starts the approved GPU service and tunnel
using P5's own runbook. Both API and UI addresses refer to **P5's laptop** under
Option C. P6 does not connect to P5's localhost remotely.

| Environment variable | Behavior |
| --- | --- |
| `P5_API_BASE` | Default `http://127.0.0.1:8000`; HTTP(S), no embedded credentials/query/fragment |
| `P5_RECORDS_PATH` | Local JSON array or JSONL of original exported states; required for Demo record mode |
| `P5_ANSWER_TIMEOUT` | Answer read timeout, default 120 seconds, allowed 120–3600 |
| `P5_API_TOKEN` | Optional token, never committed; requires an explicitly configured auth header |
| `P5_AUTH_HEADER` | Explicit confirmed header: Authorization, X-API-Key, X-Auth-Token or X-Demo-Token |
| `P5_AUTH_SCHEME` | Optional prefix, e.g. Bearer only if confirmed; empty means send token verbatim |

Authentication configuration is provisional: P6 does not assert which header P5
uses. Connection timeout is 5 seconds; health/papers/passages read timeout is 10
seconds. There are no automatic POST retries. The macOS/Python 3.14 clean resolved
snapshot is `requirements-ui-macos-py314.txt`; it is not a tested Windows/cluster
lockfile. See the completion summary for tested versions.

## How to use the UI

1. Click **Refresh service**. Confirm capability flags and service mode; unknown
   mode must not be presented as live evidence.
2. With retrieval enabled, select a paper and create a **Free question** workspace.
   Enter a complete question and Submit. Each question is independent: previous
   messages are not passed to the model. New paper context uses a new workspace.
3. Without retrieval, choose **Demo record**, create a workspace, select an exported
   state and Submit. The selected object is submitted unchanged. This demonstrates
   generation from supplied state, not newly executed retrieval.
4. Wait for the non-streaming response. The UI uses synchronous HTTP; workspace
   switching during processing is not promised. One request is allowed per session;
   other sessions can still receive backend 429.
5. Inspect final answer/refusal and citations. Validator blocks show the final
   refusal plus reason; the original model answer is inside a rejected-answer
   expander. Missing passage text retains the citation ID.
6. The run caption identifies the execution. Submit again creates a new attempt.
   To explicitly link a retry of the latest matching submission, check **Manual
   retry** before Submit. A timeout does not cancel server inference.
7. Select five runs in the sidebar and download JSON. Answer HTTP time includes
   waiting/processing/transport and excludes citation lookup/rendering; it is not
   isolated model inference latency. Citation HTTP time is separate.
8. Export before clearing/removing a workspace. History is session-only, limited
   to 10 workspaces and 50 attempts each; no silent eviction. Refresh/reconnect,
   another tab or a server restart may lose history. No abandoned-run recovery API.

Exports omit the agent field (which can contain raw AgentState) and sensitive-key
metadata; they retain answer/provenance text. Review downloaded content before
sharing. Do not commit real exported states or downloaded run results.

## Interface compatibility and changes requested from P5

**No mandatory new endpoint, JSON body field, or frozen result change is required.**
The client uses the 2026-10-29 handoff baseline. Please confirm these concrete shapes:

| Endpoint | Client expectation / P5 confirmation needed |
| --- | --- |
| `GET /health` | JSON object with boolean `retrieval` and `passage_text`. Optional `mode` is displayed/exported verbatim; absent means unknown. Consider supplying explicit mock/live mode for reproducibility. |
| `GET /papers` | `{"papers": [{"paper_id": "...", "title": "..."}]}`. Title optional; paper_id required nonempty string. Confirm actual row keys before live free-query testing. |
| `POST /answer` | Exactly `{"question": "...", "paper_id": "..."}` OR `{"record": <original state>}`. No conversation history or extra IDs in JSON. |
| Answer 200 | `request_id`, result's five keys, validation with boolean downgraded and violations list of objects, and generation object. Status exactly SUFFICIENT/INSUFFICIENT; citations list of strings, provenance list, retrieval_rounds nonnegative integer. Confirm severity/code fields; WARNING is currently recognized case-insensitively. |
| `POST /passages` | `{"ids": ["..."]}` -> `{"passages": {id: {"text": "...", ...}}, "missing": [...]}`. Missing IDs/503 preserve final answer and IDs. |
| HTTP errors | 400/401/429/503 receive distinct safe UI messages. Remote detail text is not displayed to avoid accidental credential/stack disclosure. |

P5 owns schema approval. If the formal contract differs, agree an explicit client
adapter with P6; do not change shared answer/passage/split schemas silently.
Passage schemas and split mappings remain `v0-proposed`.

**Optional correlation extension, not implemented or required:** discuss
`X-Client-Run-ID` request/echo and `X-Run-ID` response. Current UI sends neither,
uses local UUID correlation, and displays backend run ID unavailable. Please
confirm existing request_id semantics; a question ID is not a unique execution
ID. Header validation/echoing/error behavior, backend allocation and log propagation
need agreement before support is added. No idempotency or recovery is implied.

## Run actual P5 mock-service smoke

Start P5's real mock server, then in the UI environment set the URL/record path
above and run:

```bash
python -m pip install pytest
P5_RUN_SMOKE=1 python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

PowerShell:

```powershell
$env:P5_RUN_SMOKE = '1'
python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

This calls health, submits the first exported record, conditionally resolves
citations, and executes the record workflow through Streamlit AppTest. It sends
**two sequential answer calls**; use an approved cheap development record. Missing
service/input is a failure when opted in. Without opt-in, this test is explicitly
skipped, not counted as verified P5 integration.

## Real-environment E2E checklist

Record UI/server commits, OS/Python/dependency versions, model revision, prompt,
GPU/job identifier, capability flags, dataset/index versions and timing policy.
Use approved development inputs; avoid tuning with held-out examples.

| Check | Expected evidence | Initial status |
| --- | --- | --- |
| Preflight | Health reachable through P5 tunnel; actual mode/capabilities recorded | Pending P5 |
| Exported record | Original question, completed run ID, final result and diagnostics displayed | Pending P5 |
| Normal/warning/refusals | Verify six display states using approved captures/scenarios | Pending P5 |
| Validator downgrade | Final refusal plus clearly rejected raw answer/reason | Pending P5 |
| Citation capability on/off | Text/metadata when available; ID-only/missing fallback otherwise | Pending P5 |
| Free question | Chosen paper/question goes to P5 retriever; record five actual queries if available | Blocked if retrieval=false |
| Repeated question | Different client_run_id each execution; request_id meaning unchanged | Pending P5 |
| Separate sessions | No shared UI history; backend busy request produces 429 safely | Pending P5 |
| Slow answer | Spinner/no duplicate dispatch; manual retry on timeout, outcome unknown retained | Pending P5 |
| Export | Five selected runs; correct timing definitions, mode, available metadata; no token/state dump | Pending P5 |
| Refresh/reconnect | No persistence/recovery promise; no wrong reassociation of abandoned work | Pending P5 |

Record each as pass/fail/blocked with date, observed latency, sanitized screenshot
or issue reference and owner. A capability-off path passing does not establish the
corresponding live feature works. Mock results do not certify model correctness,
semantic faithfulness or real querying performance.

Troubleshooting: unreachable API -> P5 service/tunnel; 401 -> P5 auth configuration;
400/schema mismatch -> P5/P6 contract reconciliation; 429 -> manual retry after
about 20 seconds; passage 503 -> P5/P3 corpus deployment; retrieval=false -> P5/P2
retriever integration; timeout -> outcome unknown, consult P5 logs before retrying.
