# Acceptance criteria and test cases

Status: proposed; no cases have been executed for the new UI.
Test levels: U = pure unit; A = Streamlit AppTest; S = live local P5 mock service;
E = P5's real deployment. Synthetic fixtures are permitted in Git. P5's captured
responses are read as supplied and never manually edited; regeneration uses P5's
capture script. Do not commit raw QASPER records or generated corpora/results.

| Case / requirements | Setup and action | Expected result | Level |
| --- | --- | --- | --- |
| T01 / R01 | Set URL with trailing slash; create client; also try invalid scheme | Correct normalized endpoint; invalid configuration shown before calls | U,A |
| T02 / R02 | Health retrieval=false, passage_text=false | Free question disabled with explanation; record mode remains usable; no passage request | A,S |
| T03 / R02 | Health unreachable, then refresh succeeds | Offline status; no unsafe submission; controls recover after refresh | U,A |
| T04 / R03 | Load valid JSON and JSONL record files; select one and submit | Exactly one POST with only `record`; original nested object unchanged | U,A,S |
| T05 / R03 | Missing file, invalid JSON, invalid row, empty file | Actionable local-file error; no answer POST; app stays usable | U,A |
| T06 / R04 | Retrieval=true; select paper and enter question | Exactly one POST with question and paper_id only | U,A,S |
| T07 / R04 | Empty papers, failed catalogue, blank question, no paper selection | Free submission disabled or locally rejected; no answer POST | U,A |
| T08 / R05,R06 | Sufficient result, downgraded=false, no violations | Normal answer, citations, retrieval rounds and provenance available | U,A,S |
| T09 / R06 | Sufficient result with WARNING-only violations | Answer retained; warning badge and details visible | U,A,S |
| T10 / R06 | Insufficient + EMPTY_CONTEXT | Empty-context refusal; no generic HTTP error | U,A,S |
| T11 / R06 | Insufficient + AGENT_INSUFFICIENT | Agent evidence refusal, distinct from empty context | U,A,S |
| T12 / R06 | Insufficient without a recognized code | Model refusal; still treated as HTTP success | U,A,S |
| T13 / R07 | Insufficient + downgraded=true + raw answer/reason | Validator block prominent; rejected answer in labeled expander; precedence preserved even with another code | U,A,S |
| T14 / R05 | Free-input response lacks agent; another response has agent | Both render; trace appears only when supplied | U,A |
| T15 / R08 | Text capability=true; citations repeat; response contains known/missing IDs | One lookup with deduplicated IDs; metadata/text shown; missing ID retained as unavailable | U,A,S |
| T16 / R08 | passage_text=false or lookup returns 503 | Answer survives; IDs displayed; no crash or full-answer failure | U,A,S,E |
| T17 / R09 | Submit slow answer; inspect request timeout and UI state | Timeout >=120s; loading indication; no second dispatch from same action | U,A,E |
| T18 / R10 | Return 400, 401, 429, 503 separately | Specific safe message; no automatic POST retry; 429 advises manual retry after ~20s | U,A,S |
| T19 / R10 | Timeout, connection failure, non-JSON body, missing result keys | Safe actionable error; previous success retained; no fabricated answer | U,A |
| T20 / R11 | After success, expand evidence, refresh health, change paper/mode | No extra answer POST; old answer retains original submission identity | A |
| T21 / R11 | Clear after success/error | Answer, evidence and error cleared; no network generation call | A |
| T22 / R12 | Fake token and hostile HTML in server content/error | Token absent from rendered output/log messages; no unsafe HTML execution | U,A |
| T23 / R06 | Sufficient result with unexpected severity or contradictory downgrade | Visible inconsistent-response warning; not labeled clean | U,A |
| T24 / R03,R05,R08 | Run real P5 mock server; record -> answer -> citation lookup | Actual HTTP request/response path renders without AppTest exceptions; IDs resolve or degrade as advertised | S |
| T25 / R01–R12 | P5 launches approved real environment; submit approved development record | Real backend metadata, final state, citations and timing inspected; no mock presented as real | E |
| T26 / R04 | P5 real health retrieval=true, run approved paper-scoped query | Returned answer/trace tied to chosen paper; if false, mark blocked by retrieval capability rather than pass | E |
| T27 / R09,R10 | P5 submits from two sessions while one is running | Busy request gives 429 without corrupting first answer; UI recovers on manual retry | E |

| T28 / R13,R14 | Create workspaces A/B and separate UI sessions | Distinct IDs and isolated histories; no global cached answer leaks | U,A |
| T29 / R14 | Switch paper after questions; use an ambiguous follow-up | New paper context creates new conversation; independent-question guidance; no history added to request | U,A |
| T30 / R13,R15 | Execute identical query twice and rerun same exported record | New client_run_id for each attempt; original question/request identifiers preserved | U,A,S |
| T31 / R15 | Simulate A completion after active workspace changes to B; deliver duplicate completion | Only A's captured run updated once; B unchanged | U,A |
| T32 / R16 | Timeout after dispatch; manually retry | First attempt outcome_unknown, second has new ID/retry link; no automatic retry or cancellation claim | U,A,E |
| T33 / R18 | Service echoes matching/mismatching/no IDs | Matching IDs associated; mismatch flagged; absent optional backend ID shown unavailable; JSON contract unchanged | U,A,S |
| T34 / R15 | Two runs cite same ID with different lookup outcomes | Evidence stays attached to owning run; one lookup error does not fail another answer | U,A |
| T35 / R17 | Select five runs for export, including mock/failure/missing metadata | Valid sanitized JSON; answer vs citation latency distinct; unknown metadata retained; mock timings not labeled live performance | U,A,E |
| T36 / R09,R14 | Slow synchronous call while multiple workspaces exist | One pending call across session, truthful processing spinner; no fabricated stage progress or unverified switching promise | A,E |
| T37 / R03,R14 | Compare record Demo mode and free-query mode | Distinct labels; original record preserved; no claim replay performs fresh retrieval | A,S |
| T38 / R13–R18 | P5 real environment runs identical query twice, then another browser session | Run IDs/headers reflect actual agreement; no history crossing sessions; 429 handled; evidence recorded | E |
| T39 / R11,R14 | Clear active/non-active/pending workspace and reach history limit | Only intended non-pending history removed; pending clear blocked; limit prompts export/clear without silent eviction | U,A |
| T40 / R14 | Reconnect/refresh or open new browser tab | No durable/shared history promise; no wrong association with abandoned executions | A,E |

## Execution and evidence

After implementation, run the targeted unit and AppTest suite, then the actual
P5 mock-service smoke path. Record commands, exit codes, test counts, Python and
package versions, service/UI commit IDs, and any skips in the completion summary.
Use a clean lightweight UI environment to verify no GPU/index dependency is
required. Also run affected existing tests when imports/dependencies change.
Do not repeatedly broaden tests after relevant checks pass without a new concern.

Planned targeted command (files will be added during implementation):

```bash
python -m pytest -q tests/test_ui_api_client.py tests/test_ui_view_models.py tests/test_ui_record_loader.py tests/test_ui_conversation_state.py tests/test_ui.py
```

The exact opt-in smoke command will be documented after the real P5 package and
mock scenario controls are inspected. In-process mocked HTTP tests alone do not
satisfy T24. Inspect the actual browser layout for loading, long answers, long
citation IDs, expanded validation, and narrow windows; record observations.

## Release gates

1. User reviews design before source implementation, including the linked
   [user stories and API proposal](UI_PORT_USER_STORIES_AND_API.md).
2. P5 contract and record sample are available; mismatches resolved with owners.
3. Relevant unit/AppTest checks and T24 pass; record outstanding limitations honestly.
4. P6 provides completion summary and runnable P5 E2E handoff.
5. P5 records E cases as pass/fail/blocked with capability flags. Missing retrieval
   or corpus is an explicit limitation, not proof of complete E2E functionality.
6. Another member reviews the PR before merge. Shared milestone updates go in
   `docs/WEEKLY_TRACKER.md` with actual result/PR links.

P5 real verification additionally covers T32,T35,T36,T38,T40. Unsupported
correlation headers do not block client-only routing tests; record them as
unsupported, not implemented. Five live free-query runs remain blocked while
retrieval=false; exported-record runs are a distinct demonstration path.
