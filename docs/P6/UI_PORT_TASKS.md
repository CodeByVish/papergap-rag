# Task breakdown and implementation specifications

Updated: 2026-10-29 after rebase onto main `97e33b2`. Design review is complete.
Local UI code `4584e2c` and actual P5 mock integration have been verified.
This table records actual delivery status, not an instruction to restart I0–I7.

| Task | Specification and actual output | Current status / remaining work |
| --- | --- | --- |
| I0: Review package | Requirements R01–R18, user stories, identity model and T01–T40 under docs/P6; user reviewed before implementation | Complete |
| I1: Reconcile P5 contract | P5 service/contract ef5f7a3 now inherited from main; confirmed shared import path, string paper IDs, Bearer auth, violation objects and request_id behavior; client-only correlation retained | Local contract reconciliation complete. Own-account paths and approved real inputs remain deployment prerequisites. |
| I2: HTTP boundary | api_client.py: config, four endpoints, normalized paper IDs, explicit auth, safe errors, 5s connect / >=120s answer-read / 10s auxiliary-read timeouts, no POST retries | Implemented and tested |
| I3: Pure state/display logic | view_models.py, record_loader.py, conversation_state.py: classifications, input files, captured IDs, terminal transitions, retry lineage, bounded history, evidence ownership and sanitized export | Implemented and locally tested; no backend persistence/recovery |
| I4: Streamlit integration | app.py: capability-gated modes, paper-bound workspaces, independent questions, histories/diagnostics, explicit retries and downloads; old adapters preserved | Implemented/AppTest verified. No promise of interactive switching during blocking inference. |
| I5: Packaging and local verification | requirements-ui.txt, src/ui/README.md, clean-environment snapshot, actual P5 mock-service smoke, server socket smoke and post-rebase regression | Complete for local scope: combined suite 100 passed/1 opt-in skip; actual P5 mock passed separately. Live GPU acceptance remains open. |
| I6: Completion record | UI_PORT_COMPLETION_SUMMARY.md separates current results, earlier clean evidence and outstanding gates | Delivered; update after real execution |
| I7: Operational handoff | P6_UI_handoff.md and P6_REAL_ENV_E2E_GUIDE.md provide usage, API compatibility, own-account runtime/tunnel instructions and results checklist | Documents delivered. P6 performs rehearsal; P5/P2/P4 supply their owned dependencies. Review/PR/merge is a separate repository workflow. |

## Client and record specifications

Keep transport outcomes distinct from answer classification. A valid HTTP 200
refusal is completed. An invalid success payload is failed; non-200 responses are
rejected, while timeout/disconnect may be outcome_unknown. None proves that the
server cancelled work. Errors omit raw exception/remote detail text. Manual retry
creates a new execution and can duplicate server work.

`P5_RECORDS_PATH` accepts a nonempty JSON array or JSONL of original state objects.
The loader rejects malformed files/rows and answer-record captures; P5 still owns
semantic input validation. Selector labels include file position, while payloads
remain unchanged. Real records stay outside Git; no `/records` endpoint is added.

## State and rendering specifications

- `begin_run` captures owning workspace, question/record identity, capabilities and
  timestamps before dispatch. Each attempt has a new client_run_id; an explicit
  retry of the latest matching submission links to the same message_id.
- `finish_run` handles completed/rejected/failed/outcome_unknown in one guarded
  function. Duplicate terminal transitions are ignored. Results never target the
  currently selected workspace by accident.
- `attach_evidence` writes to the owning completed run. Passage lookup failure
  preserves the final answer and citation IDs. Deduplicate IDs before lookup.
- Clear/remove requires a non-pending workspace in the pure state API. The current
  UI conservatively disables both controls across the session while a call is
  pending. Neither clears server work nor cancels inference.
- Histories retain at most 10 workspaces and 50 attempts per workspace, with explicit
  export/clear and no silent eviction. No refresh/reconnect/cross-tab persistence.
- Render final answers first. Downgrades show reason plus rejected original text in
  a labeled expander. Display supplied validation/provenance/agent JSON, not invented
  trace stages. Unknown insufficient codes may use Model refusal as a fallback;
  validation diagnostics remain necessary for operational failure analysis.

## Timing/export specifications

Use monotonic answer HTTP time, measured before citation lookup. Citation time is
separate; UTC timestamps describe submission/completion. These values include
network/waiting overhead and do not isolate model inference. Downloads contain
selected run data, not an automatic exactly-five restriction: the user selects five
for report evidence. Agent state and sensitive-key metadata are omitted, but answer,
provenance and already-resolved evidence text remain in the downloaded JSON.

P5 health has no mode field, so service_mode may be unknown. Generation metadata
is preserved as supplied; missing revisions are not invented. Save raw health and
actual version/model/job metadata separately during real tests.

## Test iteration and remaining owner work

For future changes, add meaningful boundary/behavior tests and fix affected
regressions before proceeding. The completed source suite and evidence are in
[the summary](UI_PORT_COMPLETION_SUMMARY.md); acceptance levels are in
[the matrix](UI_PORT_ACCEPTANCE.md). Synthetic HTTP success is separate from the
actual P5 mock pass and from real-cluster success. Do not count skips as passes.

Remaining operational work:

1. P6: verify own account/quota, complete readable weights, approved vLLM environment,
   development input paths and token; run the real-environment guide and record results.
2. P2/P5: supply the real retriever factory, matching corpus/index/cache and CPU
   dependency/configuration instructions before accepting fresh free queries.
3. P4/P5: separately integrate the adaptive agent if a fresh critic/retry trace is
   required. Current free-query server code does not run that graph.
4. P5/P6: review any future correlation-header extension. No such headers or backend
   run IDs exist in this port; no polling/cancellation/recovery service is in scope.
5. Another member: review before merge to main. Shared milestones belong in
   docs/WEEKLY_TRACKER.md; private runtime artifacts and credentials remain local.
