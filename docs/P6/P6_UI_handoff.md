# P6 UI handoff to P5

Updated: 2026-10-29 (Singapore). Branch: `P6/UI-port-integration`.
Reviewed UI code: `4584e2c`; base main: `97e33b2`, including P5 service `ef5f7a3`.
Status: local UI and actual P5 mock integration verified; real-cluster E2E pending.

## Ownership and delivered source

P6 operates its **own** cluster job, tunnel and laptop Streamlit, per P5's latest
message (configuration 2 in the P5 operations manual). P5 owns the service code and
model-serving configuration; P2 owns the real retrieval adapter/data dependencies;
P4 owns the adaptive-agent integration. P5 can reproduce the same UI on its own
account/laptop but is not required to operate P6's rehearsal.

The current rebased P6 branch contains both service and UI. There is no missing
server/contract/capture-script delivery and no separate P5-branch merge required.
Use the branch version containing this handoff; main alone does not yet contain
the P6 UI port. Sources:

- [P5 field-level API](../P6_UI_CONTRACT.md), [service](../../src/generation/server.py),
  [cluster script](../../scripts/cluster/80_demo_server.sbatch).
- [UI entry point](../../src/ui/app.py), api_client/view_models/record_loader/
  conversation_state modules, requirements-ui.txt and tests.
- [Completion evidence](UI_PORT_COMPLETION_SUMMARY.md) and
  [P6 real-environment execution guide](P6_REAL_ENV_E2E_GUIDE.md).

No model service, real retriever, agent graph or shared schema was changed by the
UI port. The service is inherited from main; all passage/split proposals remain
`v0-proposed`.

## Install and run the UI

First start the service and tunnel as described in the E2E guide. Use a separate
lightweight laptop environment, not the pinned cluster vLLM environment.

Bash (start bash first on macOS if using zsh):

```bash
python3 -m venv .venv-ui
source .venv-ui/bin/activate
python -m pip install -r requirements-ui.txt
export P5_API_BASE=http://127.0.0.1:8000
export P5_RECORDS_PATH='/absolute/local/path/to/exported-states.jsonl'
export P5_AUTH_HEADER=Authorization
export P5_AUTH_SCHEME=Bearer
read -r -s -p 'Enter the server demo token: ' P5_API_TOKEN
printf '\n'
export P5_API_TOKEN
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

PowerShell (enter the same token as the server; no literal token in source):

```powershell
python -m venv .venv-ui
.\.venv-ui\Scripts\Activate.ps1
python -m pip install -r requirements-ui.txt
$env:P5_API_BASE = 'http://127.0.0.1:8000'
$env:P5_RECORDS_PATH = 'C:\local\exported-states.jsonl'
$env:P5_AUTH_HEADER = 'Authorization'
$env:P5_AUTH_SCHEME = 'Bearer'
$demoToken = Read-Host 'Enter the server demo token' -AsSecureString
$env:P5_API_TOKEN = [System.Net.NetworkCredential]::new('', $demoToken).Password
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

The token is stored in process environment for the client; never save its value
in a committed script or print the environment while collecting evidence.
For a token-free loopback mock, leave P5_API_TOKEN/P5_AUTH_HEADER/P5_AUTH_SCHEME
unset. Network-bound real jobs require a server token; setting only P5_API_TOKEN
is insufficient for this UI's explicit auth configuration.

Open `http://127.0.0.1:8501` on the operator's laptop. Under the selected deployment,
127.0.0.1:8000 is **P6's** local tunnel, not P5's computer. Do not expose the laptop
API/UI on the LAN to work around a missing tunnel.

| Variable | Current behavior |
| --- | --- |
| P5_API_BASE | Default http://127.0.0.1:8000; HTTP(S), no embedded credentials/query/fragment |
| P5_RECORDS_PATH | Local nonempty JSON array/JSONL of original exported inputs, required for Demo record mode |
| P5_ANSWER_TIMEOUT | Read timeout, default 120 seconds; allowed 120–3600 |
| P5_API_TOKEN | Same value chosen for the server's DEMO_TOKEN; never committed |
| P5_AUTH_HEADER | Set Authorization for the confirmed P5 service |
| P5_AUTH_SCHEME | Set Bearer for the confirmed P5 service |

Connection timeout is 5 seconds; auxiliary read timeout is 10 seconds. No automatic
POST retries. [The dependency snapshot](requirements-ui-macos-py314.txt) is an
earlier macOS/Python 3.14 UI environment, not a server/Windows/GPU lockfile.

## User workflow

1. Refresh service and inspect capabilities. P5 health has no mode field, so the
   UI may show unknown. Inspect/save backend/model/prompt information separately.
2. For real generation without a fresh retriever, create a Demo record workspace,
   select an approved exported input and Submit. The state is sent unchanged;
   generation is fresh, retrieval/agent state is supplied rather than rerun.
3. When a real factory is configured and retrieval=true, select a paper and create
   a Free question workspace. Each complete question is independent; history is
   not sent to generation. A new paper context requires a new workspace.
4. Wait for a single non-streaming response. Blocking calls may prevent workspace
   browsing. The UI guards one pending call per session; the backend handles
   collisions between sessions with 429.
5. Inspect accepted answer/refusal, citations and diagnostics. A validator block
   prominently shows the final refusal/reason and labels the original answer as
   rejected. Missing text keeps the citation ID visible.
6. Repeated submits have different client_run_id values. Check Manual retry to
   explicitly link the latest matching question to another execution. Timeout
   means outcome unknown, not cancellation; manual retry can duplicate work.
7. Select five runs and download JSON for the report. Answer/citation HTTP timings
   are distinct and do not isolate inference speed. Export omits agent state and
   sensitive-key metadata but retains answer/provenance/requested evidence text.
8. Export before clear/remove. Limits are 10 workspaces / 50 attempts each. History
   is session-only; refresh/reconnect/new tabs may lose it. No server-run recovery.

## Confirmed contract and interface-change requirements

**No mandatory new endpoint or JSON field is requested.** The current client is
compatible with P5's supplied contract; it preserves the frozen result payload.

| Interface | Confirmed behavior |
| --- | --- |
| GET /health | Boolean retrieval/passage_text plus backend, model_id, prompt_version and operational metadata; mode absent |
| GET /papers | `{"papers": ["paper-id", ...]}`; normalized to internal objects by the UI, with object-list backward compatibility |
| POST /answer | Client sends either `{"question": "...", "paper_id": "..."}` or `{"record": <original state>}`; no history or local run IDs in JSON |
| Answer 200 | request_id, five-key result, validation and generation; optional supplied agent trace. Refusal is still success. |
| Result fields | answer string, citations string list, SUFFICIENT/INSUFFICIENT, nonnegative retrieval_rounds integer and provenance list |
| Validation | Boolean downgraded, violations object list with code/severity/message/subject, optional raw_result and downgrade_reason |
| POST /passages | IDs -> passages map plus missing list; missing text/503 preserves answer and IDs |
| Auth | Authorization: Bearer when token configured; health/papers open. UI can send the configured header on all calls. |
| Errors | 400/401/429/503 mapped to safe distinct messages; raw remote detail/exception content is not shown |

request_id is a business/question identifier, not the UI execution identity.
Exported input IDs pass through the adapter; free-query IDs currently use a ui-
epoch-milliseconds value. Local UUID client_run_id identifies every attempt.

**Deferred optional extensions:** X-Client-Run-ID request/echo and X-Run-ID response,
explicit mode and richer reproducibility metadata. No ID header is currently sent,
validated or echoed by the UI. Agree semantics, validation, allocation/logging and
error behavior before adding support. Correlation does not supply idempotency,
cancellation or recovery, and is not required for local routing.

**Dependencies, not API changes:** P2/P5 must supply the real retriever factory and
matching CPU/index/cache configuration for free queries. The current server calls
that retriever once then generates; fresh P4 critic/retry execution needs separate
P4/P5 work. A supplied trace does not demonstrate fresh agent execution.

## Verification and remaining E2E

The actual P5 mock API with Bearer auth and synthetic state passed the P6 running-
service UI smoke separately. Post-rebase combined tests: 100 passed, 1 default
opt-in skip. See the completion summary for exact commands and non-additive counts.

To rerun against an already running mock or real service, set the environment above:

```bash
python -m pip install pytest
P5_RUN_SMOKE=1 python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

PowerShell: set `$env:P5_RUN_SMOKE = '1'` then run the same pytest target without
the Bash prefix. The check makes **two sequential answer calls** and validates
shape/rendering/citations, not semantic quality or successful model inference.
When not opted in it is skipped intentionally; the server code is not missing.

| Remaining check | Owner / status | Required evidence |
| --- | --- | --- |
| Own-account allocation/runtime/tunnel | P6, not executed | Readable complete weights/venv/input, actual job/node/end time, health backend |
| Real exported-state generation | P6 with P5 runtime support, pending | Generation-eligible input, vLLM/Qwen metadata/logs, no hidden generation/parser failure |
| Real citation coverage | P6/P3/P5, pending | Actual lookup text/missing IDs and configured dump/corpus hash |
| Fresh free-query retrieval | P2/P5 factory missing | Real configured retriever, matching paper/index coverage, five live-query runs |
| Fresh adaptive agent trace | P4/P5, outside current service path | Actual graph execution and generated critic/retry evidence |
| GPU concurrency/timeout/session/reconnect/export | P6, pending real rehearsal | T27,T32,T35,T36,T38,T40 pass/fail/blocked records |

Use [the E2E guide](P6_REAL_ENV_E2E_GUIDE.md) for commands and the results form.
No HTTP 200/refusal alone establishes successful real inference. Inspect violations:
EMPTY_CONTEXT/AGENT_INSUFFICIENT can skip the model; GENERATION_ERROR/PARSE_ERROR
must not be counted as a healthy generated answer.

Escalation: connectivity/allocation -> P6 operator and cluster support; service/model
failure -> P5; auth -> runner's matching DEMO_TOKEN/UI config; catalogue/contract ->
P5/P6; missing real retrieval -> P2/P5; full corpus -> P3/P5; adaptive graph -> P4/P5.
Keep raw inputs, production results and tokens outside Git; obtain member review
before merge into main.
