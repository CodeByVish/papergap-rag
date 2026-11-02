# P6 UI handoff to P5

Updated: 2026-11-02 (Singapore). Existing branch: `P6/UI-port-integration`;
current work is uncommitted. Earlier reviewed UI: `4584e2c`; current prepared
runtime and source identities: [local E2E guide](P6_REAL_ENV_E2E_GUIDE.md).
Status: approved question-first redesign implemented; local Ollama hybrid/adaptive
pipeline verified separately from synthetic UI tests. School GPU access unavailable.

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

The question-first redesign changes the UI, not model/retrieval/agent interfaces.
The earlier local integration adds an Ollama adapter and a corpus-search extension
([owner review points](CORPUS_SEARCH_CONTRACT.md)); passage/split proposals remain
`v0-proposed`. The frozen five-key answer payload is preserved.

## Install and run the UI

On the prepared Mac, run `./scripts/p6-local.sh start` and open localhost:8501;
no token/path discovery is needed. The following manual setup is for an
independently operated school service. First start that service and its tunnel
as described in the E2E guide. Use a separate
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

1. The drawer shows **NLP Scientific Paper RAG** and **How to use** above
   Connection. Keep Search scope **All papers** (local corpus-capable API) or
   optionally choose **One paper** by title/ID. Legacy services require one paper.
2. Type into **Your question**, or use the examples underneath it. **Browse all
   examples** groups corpus topics and paper-specific questions; the latter show
   both paper title and ID. **Use this question** fills the draft without inference
   or a scope change. In corpus mode the draft includes the paper reference.
3. Click **Ask question**. There is no New workspace step. The next request uses
   the currently selected scope. Questions are independent; history is not sent.
4. The submitted question appears above its **Answer**. **Evidence needs review**
   explains warning-level validation; **What was flagged?** shows exact violations.
   A validator block preserves the final refusal and separates the rejected draft.
   **Sources**, **Pipeline details**, and **Debug information** are expandable.
5. **History** directly below Search scope displays one saved attempt without
   inference. **+ New question** clears only the draft/view. Scope changes never
   relabel a stored answer; failed attempts retain prior successes in History.
6. **Advanced settings → Input mode → Demo record** submits an original prepared
   input unchanged. It generates an answer without fresh retrieval/agent execution.
   Its saved trace must not be described as a fresh pipeline run.
7. Every explicit Ask question has a distinct client_run_id. Manual retry links
   another execution of the latest matching submission; timeout means outcome
   unknown, not cancellation. The synchronous call guards one pending run per
   session; P5 returns 429 for collisions across sessions.
8. Select five runs and download JSON under Advanced settings. Answer/citation
   HTTP timings remain distinct; exports omit agent state/sensitive-key metadata.
   Export before **Clear history**, which removes all session contexts/drafts.
   Limits remain 10 internal contexts / 50 attempts each, created/reused automatically
   by mode/scope. Refresh/reconnect may lose history; there is no recovery endpoint.

## Confirmed contract and interface-change requirements

**The redesign requests no new endpoint or result field.** The client keeps
legacy paper-required compatibility and enables All papers only when health
advertises the documented local `corpus_search` extension (`v0-proposed`).

| Interface | Confirmed behavior |
| --- | --- |
| GET /health | Boolean retrieval/passage_text plus backend, model_id, prompt_version and operational metadata; mode absent |
| GET /papers | `{"papers": ["paper-id", ...]}`; normalized to internal objects by the UI, with object-list backward compatibility |
| POST /answer | Client sends question plus optional paper_id on corpus-capable services, or an original record; legacy services still require paper_id. No history or local run IDs in JSON |
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

**Runtime distinction:** the prepared local launcher already connects real
BM25/dense/RRF/reranking and P4 adaptive retrieval through P5, using Ollama. The
original standalone service may still use a static retriever. Reproduce matching
corpus/index/cache and agent configuration on the GPU host later. A prepared-record
trace alone never demonstrates fresh agent execution.

## Verification and remaining E2E

Historical port evidence: the actual P5 mock API with Bearer auth and synthetic state passed the P6 running-
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
| Fresh free-query retrieval | Local corpus/hybrid connected; school reproduction pending | Matching corpus/index/model identity, five report-quality live queries |
| Fresh adaptive agent trace | Local launcher connected; GPU reproduction pending | Actual graph execution and generated critic/retry evidence |
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
