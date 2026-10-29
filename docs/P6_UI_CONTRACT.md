# P6 UI contract — the demo service

**Status (2026-10-29): decided.** P5 runs everything for the demo: the cluster
job, the SSH tunnel and the Streamlit app. P6 owns the UI code. This document is
the interface between the two, and it is what the UI should be written against.

Deployment detail (who runs what, and why the tunnel cannot be opened by a
different account) is in `docs/DEMO_OPTION_C.md` §2.1.

---

## 1. What you can rely on

| | |
|---|---|
| Base URL during the demo | `http://127.0.0.1:8000` (on the machine that runs the tunnel) |
| Auth | `Authorization: Bearer <token>` on `/answer` and `/passages`; P5 provides the token. `/health` and `/papers` are open |
| UI URL during the demo | `http://127.0.0.1:8501` (Streamlit) |
| Development without the cluster | `python -m src.generation.server --backend mock` |
| Captured responses for every state | `examples/demo_ui_responses.json` |
| Answer record shape | identical to the JSONL files in `runs/` |

The server never changes the answer record it returns. The five keys under
`result` are the frozen P5→P6 payload; `validation` and `generation` are the
audit trail. A refusal is a **200**, not an error status.

---

## 2. Endpoints

### `POST /answer`

Two mutually exclusive request forms:

```json
{"record": {"question_id": "...", "question": "...", "paper_id": "...",
            "retrieved_passages": [...], ...}}
```

```json
{"question": "What result is reported?", "paper_id": "1706.04115"}
```

The second form is the free-form one. `paper_id` is mandatory because QASPER
retrieval is paper-scoped — offer a selector fed by `GET /papers`.

Response (trimmed; the full bodies are in the fixture):

```json
{
  "request_id": "0038b073b7...",
  "result": {
    "answer": "The model sets a new state of the art.",
    "citations": ["qasper-passage-v1-3d65..."],
    "evidence_status": "SUFFICIENT",
    "retrieval_rounds": 1,
    "provenance": [{"claim": "...", "passage_ids": ["qasper-passage-v1-3d65..."],
                    "support": "direct"}]
  },
  "validation": {
    "violations": [{"code": "UNSUPPORTED_CLAIM", "severity": "WARNING",
                    "message": "...", "subject": "..."}],
    "downgraded": false,
    "downgrade_reason": null,
    "raw_result": null,
    "final_result": {"...": "same object as result"},
    "checks_run": ["..."]
  },
  "generation": {
    "backend": {"backend": "vllm", "model_id": "...", "loaded": true, "...": "..."},
    "prompt_version": "p5-grounded-qa-v7",
    "raw_text_excerpt": "...",
    "raw_text_chars": 412
  },
  "agent": {"paper_id": "...", "sufficient": true, "gap_label": "NONE",
            "rewritten_query": null, "required_components": ["result"],
            "evidence_map": {"result": ["qasper-passage-v1-..."]},
            "retrieval_log": [...]}
}
```

`agent` is present only when the input was an exported `AgentState`; the
free-form form does not produce it.

### `GET /health`

```json
{"status": "ok", "backend": "vllm", "model_id": "...",
 "prompt_version": "p5-grounded-qa-v7", "retrieval": true,
 "passage_text": true, "top_k": 5, "papers": 100,
 "warmup_seconds": 41.2, "uptime_seconds": 812.4}
```

Use it for the status badge. `retrieval: false` means free-form is disabled;
`passage_text: false` means citations can only be shown as ids.

### `GET /papers`

```json
{"papers": ["1706.04115", "1801.07804"]}
```

The paper ids the corpus/retrieval was built for. Empty when the server was
started without `--papers-from`.

### `POST /passages` (optional)

Citation ids are opaque `qasper-passage-v1-<sha256>` hashes, so this is how the
UI shows the cited text:

```json
{"ids": ["qasper-passage-v1-3d65...", "qasper-passage-v1-0000..."]}
```

```json
{"passages": {"qasper-passage-v1-3d65...": {"text": "...", "paper_id": "...",
                                            "title": "...", "section": "results"}},
 "missing": ["qasper-passage-v1-0000..."]}
```

Render `missing` as "source not in corpus", not as an error. A 503 means the
server was started without `--passages-from`; fall back to showing ids.

### Status codes are transport, not answers

| code | meaning | what the UI does |
|---|---|---|
| 200 | an answer (including a refusal) | render `result` |
| 400 | the payload is not this contract | show a bug; do not retry |
| 401 | bearer token required and wrong | fix configuration |
| 429 | another answer is in flight | show "busy", retry after ~20 s |
| 503 | free-form with no retriever, or passage text not loaded | disable that feature, show `detail` |

All error bodies have FastAPI's shape: `{"detail": "..."}`.

---

## 3. Mapping a 200 to a UI state

Everything below is decided from the response body, never from the status code.

| condition | UI |
|---|---|
| `result.evidence_status == "SUFFICIENT"`, `downgraded == false`, no violations | answered |
| same, with only `severity == "WARNING"` violations | answered + warnings badge (expandable list) |
| `INSUFFICIENT`, `downgraded == false`, code `EMPTY_CONTEXT` | refused: nothing was retrieved |
| `INSUFFICIENT`, `downgraded == false`, code `AGENT_INSUFFICIENT` | refused: the agent's critic judged the gap unanswerable |
| `INSUFFICIENT`, `downgraded == false`, no code | refused by the model itself |
| `INSUFFICIENT`, `downgraded == true` | **blocked by the validator** — show `validation.raw_result.answer` as the rejected answer, and `downgrade_reason` |

The last row is the one worth designing for: the model did answer, and the
validator threw the answer away. Showing only "refused" hides the evidence that
the grounding rules fired, which is the point of the project.

Field reference:

- `result.answer` — the answer text; refusals are the canonical string
  `"Insufficient evidence in the retrieved passages to answer this question."`
- `result.citations` — passage ids; resolve with `POST /passages`
- `result.evidence_status` — `SUFFICIENT` / `INSUFFICIENT` (the refusal flag)
- `result.retrieval_rounds` — how many retrieval rounds produced the context
- `result.provenance` — claim → passage ids, filled by the model or derived
  deterministically (`PROVENANCE_DERIVED` warning when derived)
- `validation.violations[].code | severity | message | subject` — full rule list
  in `docs/P6_HANDOFF.md`
- `validation.raw_result` — the model's own parsed output before any downgrade
  (`null` when nothing was parsed or no model call happened)
- `generation.prompt_version` — must be `p5-grounded-qa-v7`; show it if you want
  the demo to be undeniable
- `generation.raw_text_excerpt` — first 2000 chars of the model output

---

## 4. Develop against the fixture, not the cluster

`examples/demo_ui_responses.json` contains **real** responses captured from the
service with the mock backend, one per state:

`answered`, `refused_model`, `refused_empty_context`,
`refused_agent_insufficient`, `downgraded`, `warning_partial`, `bad_request`,
`free_form_unconfigured`, `citation_text`, `health`, `papers`, `busy`.

It is generated by `scripts/capture_demo_responses.py`; regenerate it rather
than editing it, so the fixture cannot drift from the server.

Live mock server for interaction tests:

```powershell
python -m src.generation.server --backend mock
# in another terminal
streamlit run src/ui/app.py
```

Point the UI at the server with an environment variable rather than a hard-coded
URL, e.g. `P5_API_BASE=http://127.0.0.1:8000`. That is the only thing that
changes on demo day.

---

## 5. Constraints to design around

- **One answer at a time.** The engine is not thread-safe; a concurrent request
  gets 429. Serialize in the UI and show progress.
- **p90 is ~17 s.** Set the HTTP timeout to at least 120 s and keep a spinner;
  a Streamlit button that looks frozen for 20 s is the most common demo failure.
- **No streaming.** The answer arrives validated, in one piece.
- **Paper selector required** for free-form; `GET /papers` is the source.
- **Citations are hashes**; text comes from `POST /passages`.
- **No gold answers** on the 100-question pool: the UI can show compliance
  (`SUFFICIENT`, violations, citations), not correctness.

---

## 6. What P6 delivers

- `src/ui/app.py` — Streamlit app, config via `P5_API_BASE`.
- `requirements-ui.txt` — `streamlit`, `requests` (plus whatever the app needs).
- One UI test or smoke path that runs against the mock server, so a change to the
  UI cannot silently break the demo.

P5 delivers the service, the fixture, the tunnel and the runner on demo day.
