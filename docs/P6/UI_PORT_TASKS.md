# Task breakdown and specifications

Status: planning only. Execute I0 now; I1–I7 start after user design approval.
Dependencies are sequential where stated. Fix failing relevant tests before
proceeding; update the design if the approved contract requires a material change.

| Task | Inputs and detailed work | Outputs / completion evidence | Depends on |
| --- | --- | --- | --- |
| I0: Review package | Inspect contributing rules, current UI and updated P5 handoff. Create requested branch and requirements, architecture, cases, and task specifications. | Five planning Markdown files under `docs/P6/`; no implementation. User review pending. | None |
| I1: Reconcile P5 contract | Obtain exact P5 commit, field-level contract, server environment and exported record. Compare import paths, paper rows, severity representation, auth, sample keys, mock scenario controls and refusal values. Confirm request_id semantics and proposed correlation headers, error echoing and backend run_id allocation; record agreed or unsupported extensions. Do not merge unrelated upstream work blindly. | Contract compatibility notes in requirements; known-good service launch and sample locations. Block service-dependent work if unavailable. | User approval |
| I2: HTTP boundary | Implement ApiConfig/client/ApiError. Validate config and mutually exclusive requests, inject session, enforce >=120s answer timeout, parse errors safely, avoid automatic POST retries, support confirmed auth without exposing it. | `api_client.py`; T01,T06,T18,T19,T22 transport tests pass. | I1 |
| I3: Data and display logic | Implement pure response parsing, state classification, citation IDs/cards and JSON/JSONL loader. Preserve raw/final answer distinction and unknown metadata. Validate UI needs without redefining P5's whole schema. Implement conversation_state.py with per-session UUIDs, bounded workspaces, immutable run snapshots, lifecycle transitions, retry lineage, stale-response guards and export. Create small synthetic fixtures; read supplied captures without editing. | `view_models.py`, `record_loader.py`, unit tests; T04–T05,T08–T16,T23 pass at U level. | I1 |
| I4: Streamlit integration | Replace legacy provider UI entry point with record/free-question modes, connection refresh, capability gating, session-wide pending state, conversation sidebar and paper binding, independent-question guidance, per-run history/export, diagnostics, response identity, six outcomes and citation degradation. Keep existing generation/retrieval APIs untouched. Move still-useful legacy adapter tests out of old entry-point tests. | Updated `app.py`, AppTest cases; relevant A cases pass. | I2,I3 |
| I5: Packaging and mock smoke | Update lightweight requirements and `src/ui/README.md`; document macOS and PowerShell environment setup, configured record file, optional auth, and separate P5 service dependencies. Add opt-in service smoke test using real P5 mock server and known sample. Test in clean UI environment; visually inspect browser behavior. | Reproducible mock launch + smoke commands; targeted tests including T28–T40 at applicable levels and T24 pass; dependency snapshot/version evidence. | I4 |
| I6: Completion record | Summarize actual files/functions changed, request path, test commands/counts/results, browser observations, dependency versions and unresolved upstream limitations. Separate mock verification from real-model verification. | `docs/P6/UI_PORT_COMPLETION_SUMMARY.md`; no unsupported “all E2E passed” claim. | I5 |
| I7: P5 real E2E handoff | Provide exact UI commit, installation/start commands, env table, record source, health preflight, correlation agreement, five-query timing procedure, approved development sample and T25–T27 plus T32,T35,T36,T38,T40 checklist. P5 operates allocation/tunnel/model. Include expected screenshots/statuses, troubleshooting and results form. Prepare reviewable PR per CONTRIBUTING; attach if created. | `docs/P6/P5_UI_E2E_HANDOFF.md`; reviewer-ready diff; P5 execution pending until P5 reports results. | I6 |

## Implementation details and invariants

### Client and record workflow

Keep transport errors distinct from answer status. A 200 refusal is parsed and
rendered normally. Validation errors in a success payload must produce a safe
contract error rather than a false “model refused” classification. Use bounded
health/catalogue/lookup timeouts independent of the long answer timeout; record
chosen values in setup instructions. Do not print token headers or raw HTTP
exceptions. Retry is user initiated, including after a timeout where server work
may still be running.

Local exported records are supplied by P5 outside Git. The loader must not
interpret an answer-record capture as AgentState. Confirm supported record
container shapes in I1. If record labels are duplicated, use file position as
a stable discriminator while retaining original payload IDs. No new endpoint
or shared state schema may be invented to solve record selection.

### UI state and evidence

Keep network access behind the client. Submit only on an explicit action, using
a pending guard and `try/finally` recovery. Display a spinner while awaiting
the single non-streaming result. Streamlit AppTest verifies dispatch count and
state recovery; real browser inspection verifies the visible waiting behavior.
Health refresh should not erase an existing answer. Each run owns its
submission snapshot and evidence data; new results must not erase another run.
Capture conversation/message/client-run IDs before dispatch and apply completion
only to their owner, never the current selector. Timeout is outcome_unknown when
execution may continue; retries create new IDs. Clear cannot cancel a pending run.
Deduplicate lookup IDs, preserve their display order and show unresolved IDs.

Classify downgrade before other insufficient states. For rejected answers,
show the final result as authoritative and original content only inside clearly
labeled diagnostic UI. If raw_result/reason is absent, show unavailable details
without crashing or reconstructing an answer. Provenance and optional agent
trace may be expandable JSON until their exact display fields are confirmed.

### Test iteration policy

For each implementation increment: add meaningful boundary/behavior tests, run
the affected subset, fix regressions, and then integrate. At I5 run the complete
targeted suite once plus affected legacy checks and real mock HTTP smoke. Never
replace missing service evidence with synthetic success or mark skipped tests
as passed. Record P5 artifact blockers and continue only independent work.

## Required final document contents

`UI_PORT_COMPLETION_SUMMARY.md` must include scope and code revision, changed
modules/functions, fulfilled acceptance IDs, exact verification evidence,
remaining failed/blocked cases, and real-environment limitations.

`P5_UI_E2E_HANDOFF.md` must include:

- UI branch/commit and compatible P5 server/contract revision.
- Lightweight installation, URL/token/record-path configuration and Streamlit command.
- P5-owned service/tunnel preflight and expected capability flags.
- Record-mode happy path, validator downgrade, warnings/refusals, citations,
  capability-off behavior, busy response, timeout/recovery and optional free query.
- A results table for environment, date, case, outcome, observed latency, sanitized
  evidence and issue reference; do not put private records/tokens in the report.
- Troubleshooting for import mismatch, 401, 429, 503, no corpus, no retrieval,
  connection failure and timeout; escalation owner for each boundary.
- Explicit statement that P6 mock success does not certify model quality,
  citation semantic faithfulness or cluster deployment.

## Additional implementation specifications

The [user stories and API design](UI_PORT_USER_STORIES_AND_API.md) defines the
expanded scope. I3 owns pure conversation/run state and sanitized timing export;
I4 owns sidebar/history and user-visible independent-query semantics. No backend
conversation service, background worker, task polling or persistence is authorized
by this design. Confirm Streamlit's blocking-call behavior in I4/I5 before promising
interactive workspace switching while processing.

The client function signatures may gain an optional client correlation argument
only after I1 confirms P5 support. Do not insert IDs into the existing JSON request
body or frozen result. Log unsupported extensions explicitly and retain local
routing. Carry backend metadata as optional; never invent backend execution IDs.

Use a monotonic timer for answer HTTP elapsed time and separate citation lookup
latency. Export selected five runs with UTC timestamps, explicit mock/live/unknown
mode and actual available revision/model/prompt metadata. Evaluate live query
speed only when free retrieval works. Extend I6 evidence to T28–T40 and I7 with
workspace isolation, repeated-query IDs, timeout/late-response behavior, five-query
export and all unresolved P5/P2/P4 dependencies. Final handoff must state the actual
history retention limits and lack of refresh/cross-tab persistence.
