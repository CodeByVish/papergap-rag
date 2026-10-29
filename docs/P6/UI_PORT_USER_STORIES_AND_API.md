# User journeys, conversations and execution contract

Status: design proposal, pending implementation review and P5 contract reconciliation.
This document extends the requirements, acceptance matrix and task specifications;
it does not claim that P5 has implemented the proposed correlation headers.

## Handout alignment

Source: `Assignment.pdf`, AI6127 2026, pages 2–4 (reviewed 2026-10-29).

| Handout requirement | Product behavior / evidence |
| --- | --- |
| Page 2, Querying: simple friendly UI; sophisticated UI is discouraged | Paper selection, explicit question, answer and inspectable evidence; lightweight conversation sidebar |
| Page 3, Question 2: five queries, results and querying speed | Preserve five independent runs in session and export their inputs, results and measured latency |
| Page 3, generation: answers conditioned on inspectable evidence | Citation cards with original text and source metadata when available; honest ID-only fallback |
| Pages 3–4, Questions 3 and 5: retrieval improvements, grounding and agent innovations | Expand supplied validation, provenance, retrieval rounds and optional agent trace; do not invent missing stages or scores |
| Page 4, Question 4: latency, throughput, cost and scalability | Collect per-run timing/metadata for reporting; offline evaluations provide aggregate metrics |

Multiple conversations, persistent accounts and contextual multi-turn chat are
not handout requirements. Conversation workspaces are an organizational feature.
Version 1 treats each question independently and labels that behavior explicitly.
The UI must not imply that “What about its limitations?” includes previous turns.
It does not send conversation history to generation or change P4's agent state.

## User stories

| ID | Story | Behavior and interface | Acceptance |
| --- | --- | --- | --- |
| US01 | As a reader, I select a paper and ask a complete question | Health-gated paper selector, question form and synchronous `/answer` | T02,T06,T07,T26 |
| US02 | As a reader, I organize questions in multiple workspaces | New/select conversation sidebar; one paper per free-query workspace; creating a new paper context creates a new conversation | T28,T29 |
| US03 | As a reader, I know which question produced an answer | Render immutable submission snapshot and local/backend identifiers | T30,T31,T33 |
| US04 | As a reader, I inspect grounding | Citations resolve via `/passages`; validation distinguishes six answer states | T08–T16,T34 |
| US05 | As a presenter, I explain agent behavior | Expand only supplied trace, provenance and round counts; no fabricated progress stages | T14,T17,T36 |
| US06 | As a presenter, I rehearse without free retrieval | Separate exported-record Demo mode submits original AgentState and is labeled as replay input, not fresh retrieval | T04,T24,T37 |
| US07 | As an evaluator, I record five query runs and speed | Export selected session runs with timestamps, latency definition, capability/mode and outcome | T35 |
| US08 | As a user, I recover from busy or failed calls | Preserve prior results, distinguish rejected/failed/unknown outcome; explicit manual retry | T18,T19,T32 |
| US09 | As P5, I reproduce the UI on my laptop | Lightweight install, environment configuration, mock smoke and real deployment checklist | T24–T27,T38 |

## UI layout and behavior

```text
+---------------------+--------------------------------------------+
| New conversation    | Paper / workspace title                    |
| Conversation list   | Service + retrieval + passage capabilities |
|                     |--------------------------------------------|
|                     | Submitted question                         |
|                     | Final answer / refusal / warning           |
|                     | Citation cards                             |
|                     | Expand: validation / provenance / trace    |
|                     | Execution ID + elapsed time                |
|                     | ... earlier independent questions ...      |
| Export selected runs|--------------------------------------------|
| Demo record mode    | Complete question                  Submit  |
+---------------------+--------------------------------------------+
```

Keep the normal reading path short; diagnostics are expandable. A free-query
conversation binds to one paper. If paper selection changes after questions
exist, explicitly create a new conversation rather than relabel old answers.
Demo-record workspaces remain separate from free-query workspaces and preserve
the selected record's own paper/question identity.

Version 1 retains multiple questions and responses in session memory. It does
not promise persistence across refresh/reconnect, browser tabs, or server restart.
Use a proposed limit of 10 workspaces and 50 runs per workspace, subject to user
review; at the limit prompt the user to export/clear, never silently evict pending
or completed runs. Clear applies only to a selected non-pending workspace and
does not cancel server work. Pending workspaces cannot be deleted or cleared.

At most one answer call is pending per UI session across all its workspaces.
Other sessions can still collide; P5's 429 is authoritative across sessions.
Browsing an existing workspace while waiting is desirable, but a blocking
Streamlit call may prevent immediate interaction. Verify actual behavior in I4/I5;
do not introduce background workers or promise interactive switching without
review. Always bind completion to its captured owner, even after a UI rerun.

## Identity model

| Identifier | Meaning / owner | Lifetime and rules |
| --- | --- | --- |
| `ui_session_id` | UI-generated UUID for one Streamlit session | Local isolation only; not a login, authorization token or durable browser identity |
| `conversation_id` | UI-generated UUID for a workspace | Owns mode, paper binding, messages and runs; no implied model memory |
| `message_id` | UI-generated UUID for a question/display message | Links a question to one or more explicit execution attempts |
| `client_run_id` | UI-generated UUID created before dispatch | Unique per explicit attempt, including retry and rerun of identical inputs |
| `run_id` | Proposed P5-generated unique accepted execution ID | Optional until agreed; distinct across executions; never fabricated by UI as a backend ID |
| `request_id` / question ID | Existing P5 response or dataset identifier | Preserve original meaning; uniqueness across repeated executions is not established |

```text
ui_session_id
  conversation A / paper X
    message Q1 -> client run A1 -> optional backend R1
               -> explicit rerun A2 -> optional backend R2
  conversation B / paper Y
    message Q2 -> client run B1 -> optional backend R3
```

The client already knows which synchronous call owns its response; local mapping
does not require a backend schema change. End-to-end log correlation requires
agreement with P5. IDs are correlation values, never access controls. No UI session
or history is stored in process-global caches shared across users.

## Run lifecycle and result routing

Create a run before dispatch with immutable `client_run_id`, `conversation_id`,
`message_id`, mode, paper ID, question or record identity, UTC submitted timestamp,
and capability snapshot. Keep raw records local rather than duplicating them into
export metadata. Store full P5 response, optional server ID, outcome, safe error,
elapsed time and citation lookup state on that run.

```text
pending -> completed          valid HTTP 200 answer, including refusal
        -> rejected           known HTTP 400/401/429/503 response
        -> failed             invalid success payload or locally confirmed failure
        -> outcome_unknown    timeout/disconnect after possible dispatch
```

HTTP error observations do not prove that no server-side work occurred. Treat
ambiguous connection failures conservatively. Separate transport outcome from
answer classification and evidence lookup outcome. A passage lookup failure must
not turn a completed answer into a failed generation.

Capture the run ID and workspace ID when sending. Write the response to that
specific run, never to whichever workspace happens to be active at completion.
Ignore duplicate terminal completions; a mismatched echoed ID is a contract error
and must not attach a response to another run. A late A response cannot overwrite
B. Manual retry creates a new attempt linked to the same question and, optionally,
`retry_of_client_run_id`. Identical input text is not an execution identity.
Citation cards are keyed by client run ID and passage ID, not globally by the
currently selected question. Refresh and display actions never regenerate answers.

An answer timeout does not cancel inference. Show “Outcome unknown; the service
may still be processing.” Do not automatically retry or claim cancellation.
Without a result-recovery endpoint, the abandoned response cannot be recovered
after the client connection is lost. Manual retry can execute the question again.

## Interface baseline from P5's 2026-10-29 handoff

P6 calls P5, not P2 directly:

```text
P6 UI -> P5 /answer -> P2 retriever + P4 agent where integrated
                   -> P5 generation / validator -> response -> owning UI run
```

P5 is the interface contact; P5 coordinates retrieval/trace changes with P2/P4.
Exported-state submission must not be described as triggering new retrieval unless
the actual P5 contract establishes that behavior.

| Endpoint | Handoff baseline | UI behavior |
| --- | --- | --- |
| `GET /health` | `retrieval`, `passage_text` capability flags | Gate dependent controls; unknown is not ready |
| `GET /papers` | `{"papers": [...]}` | Exact paper-row fields pending formal contract |
| `POST /answer` | Exactly one of `{"question": "...", "paper_id": "..."}` or `{"record": <exported AgentState>}` | No extra body fields or message history without P5 agreement |
| `POST /passages` | `{"ids": [...]}` -> `{"passages": {id: {text, paper_id, title, section}}, "missing": [...]}` | Batch deduplicated citations; preserve missing IDs |

The response is P5's answer record: `request_id`, frozen five-key `result`,
`validation`, `generation`, and `agent` only for exported AgentState input according
to this handoff. Do not require agent trace for free queries or invent its contents.
HTTP 200 includes refusal; error bodies use `{"detail": "..."}`. Preserve 400,
401, 429 and 503 behavior described in the requirements. No streaming, >=120-second
answer timeout, one model request at a time. The reported p90 of about 17 seconds
is P5's handoff measurement, not a new UI benchmark.

## Proposed correlation extension: not yet agreed with P5

Preferred minimal extension, subject to P5 review:

```http
POST /answer
X-Client-Run-ID: <client UUID>

HTTP/1.1 200 OK
X-Client-Run-ID: <same client UUID>
X-Run-ID: <P5 accepted execution UUID>
```

Keep the JSON answer-record format and frozen `result` unchanged. P5 should agree
header names, validation/length limits, whether IDs appear on error responses,
logging propagation, and when a backend execution ID is allocated. A 429 need
not have a new accepted execution ID. If P5 supports no headers, local run routing
still works; expose “Backend run ID unavailable,” not an invented value. Never
require header support before P5 approves the extension. An optional conversation
header is useful only if P5 needs workspace-level log correlation; it is not
required by the retriever. Correlation does not provide idempotency or deduplication.

## Deferred API features

Version 1 uses synchronous `/answer`; no polling, cancellation, persistent
conversation service or run recovery is documented. If durable recovery later
becomes necessary, separately design `POST /runs` returning 202 and
`GET /runs/{run_id}`. That requires authenticated ownership, storage/expiry,
restart behavior, idempotency semantics and load control. These are proposals
outside this implementation scope, not endpoints P5 has committed to deliver.

## Timing and export specification

Measure `answer_http_elapsed_ms` with a monotonic clock around `/answer`, including
transport and backend waiting/processing, excluding citation lookup and rendering.
Measure `citation_http_elapsed_ms` separately. Store UTC wall-clock timestamps for
human interpretation. A future backend inference/retrieval timing field must be
separately labeled and agreed; do not derive inference speed from UI elapsed time.

Export a user-selected set of runs as downloadable JSON containing UI export
schema version, IDs, submission snapshot, transport outcome, answer record,
capabilities, mock/live status if known, timing definitions and available
model/prompt/revision metadata. Missing metadata stays unknown. No tokens, raw
AgentState dump or unrequested corpus content. This is a local download, not a Git
artifact. Five mock runs establish UI behavior, not real querying performance;
five real free-input runs are needed to demonstrate live querying when available.

## P5 delivery and decision checklist

| Item | Owner / status | Required action |
| --- | --- | --- |
| Service, tunnel, GPU job and demo Streamlit operation | P5, promised in handoff | Supply compatible revision and launch instructions |
| UI entry point, requirements and mock smoke | P6, planned | Deliver tested code after design approval |
| Formal contract, 12 captured states and capture script | P5, referenced, not verified here | Obtain files; never hand-edit captures |
| Cluster launch script | P5, `scripts/cluster/80_demo_server.sbatch` referenced | P5 operates; P6 records compatible version, not scheduler guesses |
| Free-query retriever | P2/P5, not connected per handoff | Keep free input disabled until `retrieval=true`; real query acceptance blocked |
| Passage corpus | P5/P3, not deployed per handoff | Keep citation IDs usable until `passage_text=true` |
| Exported AgentState input | P5/P4, sample needed | Confirm shape and local file; captures of answers are not valid input records |
| Existing request_id semantics | P5, open | Document question versus execution identity |
| Correlation headers / backend run ID | P5/P6, proposal | Agree or explicitly retain client-only correlation |
| Session/workspace history and five-run export | P6, proposed local UI scope | No backend conversation storage required |
| Free-query trace and retrieval fields | P4/P2/P5, conditional | Display only provided metadata; avoid schema changes without owner review |

Before implementation, reconcile these decisions with `docs/P6_UI_CONTRACT.md`.
The P5 E2E handoff must list agreed/unsupported headers, identity meanings,
multi-session busy behavior, capability limitations and five-query timing evidence.
