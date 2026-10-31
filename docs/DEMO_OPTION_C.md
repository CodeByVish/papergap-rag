# Demo architecture — Option C: live service on the cluster, UI on the laptop

**Status (2026-10-29): decided.** The demo runs `answer_record` behind a small
FastAPI service on the compute node, and the UI on the laptop reaches it through
an SSH tunnel. Option A+ (precompute the pool, replay the answer JSONL) is the
fallback, not the plan.

This document is the operating manual: what the service is, how to start it, how
to open the tunnel, and what to do on demo day when one of the known failure
modes fires.

---

## 1. Why C, and what it costs

The two options that were on the table:

| | A+ — precompute + replay | C — live service (chosen) |
|---|---|---|
| Demo input | pick from the frozen question set | free-form question about a chosen paper |
| GPU at demo time | none | one A40 held for the whole window |
| Answer semantics | same code path, from a file | same code path, `answer_record`, live |
| Failure mode | stale data | the job or the tunnel dies mid-demo |

C won because free-form input is the point of a demo, and because the service
calls `answer_record(pipeline, record)` — the identical function P6's runner uses
— so parse / validate / downgrade semantics cannot drift between the demo and
the scored runs.

Three risks were accepted with the decision, and §6 is the mitigation for each:

1. **The 6-hour limit kills the service.** A demo in hour 6.1 is a dead demo.
2. **A sleeping laptop kills the tunnel.** The UI stays up; its requests stop.
3. **It depends on two unverified cluster properties**: port forwarding from the
   login node to the compute node, and P2's retriever being loadable in the
   server process. §5 verifies the first in five minutes; §7 covers the second.

---

## 2. Architecture and division of labour

```
laptop                                  login node                        compute node (A40)
┌────────────────────┐   ssh -L 8000   ┌──────────────┐  direct-tcpip    ┌────────────────────────────┐
│ Streamlit UI       │ ──────────────> │ 10.96.189.12 │ ───────────────> │ 127.0.0.1:8000             │
│ (P6: src/ui/)      │                 └──────────────┘                  │ src.generation.server (P5)          │
└────────────────────┘                                                   │  └─ GroundedQAPipeline      │
                                                                         │       └─ one vLLM engine    │
                                                                         │  └─ retriever (optional,CPU)│
                                                                         └────────────────────────────┘
```

- **P5 owns the server**: `src/generation/server.py`, plus
  `scripts/cluster/80_demo_server.sbatch`.
- **P6 owns the UI**: `src/ui/`. It speaks only HTTP and reads only the fields in
  §3; it never imports P5.
- The server binds **127.0.0.1**. The tunnel is the only path in; nothing on the
  node's LAN can reach the port, and no bearer token is required by default.

### 2.1 Who submits the job, who opens the tunnel, who opens the browser

These are three different questions, and conflating them is how the plan looks
broken when it is not.

| question | answer | why |
|---|---|---|
| whose GPU quota? | the account that runs `sbatch` | a GPU belongs to a job, and a job belongs to an account |
| whose laptop runs the tunnel? | the job owner's | SSH is account-authenticated; nobody else can log in to that compute node |
| whose machine runs Streamlit? | any machine that can reach the tunnel's local port | Streamlit is a web server; `streamlit run` only decides where the *server* lives |
| whose browser? | anyone | the end user needs no cluster account and no GPU |

The constraint that looks like a gap is row two: P6 cannot tunnel into a job
submitted under P5's account. That is not a design flaw in the HTTP contract;
it is SSH doing its job. The three configurations below are the ways out.

| | job account | tunnel + Streamlit | browser | cost |
|---|---|---|---|---|
| **1 (recommended)** | P5 | P5's laptop | P5's laptop (projected) | none; P6's code runs from the same checkout |
| 2 | P6 | P6's laptop | P6's laptop | one-time setup for P6: own vLLM venv (`30_vllm.sbatch`) and own 16 GiB `Qwen3-8B` copy - `docs/AGENT_HANDOFF.md` §6 |
| 3 (two machines) | P5 | P5's laptop, exposed on the LAN | P6 or anyone on the same network | depends on the same subnet and the Windows firewall; not for demo day unless rehearsed |

Configuration 3, in full, because the details are where it fails:

```bash
# P5's laptop: bind the tunnel's local end to the LAN, and require a token
# (the port is now reachable by anyone on the Wi-Fi).
ssh -N -L 0.0.0.0:8000:localhost:8000 -J <p5>@10.96.189.12 <p5>@<node>
# and start the server with --token so the exposed port is not open house
```

```powershell
# P5's laptop: serve Streamlit to the room
streamlit run src/ui/app.py --server.address 0.0.0.0 --server.port 8501
# P6's browser: http://<p5-laptop-lan-ip>:8501
```

If instead P6's Streamlit needs to reach P5's tunnel directly, it points at
`http://<p5-laptop-lan-ip>:8000` and must send the bearer token.

### 2.2 The UI does not need the cluster to be developed

The UI depends on the endpoints in §3, not on the cluster:

```powershell
# any laptop, no GPU, no queue, no credentials
python -m src.generation.server --backend mock
```

The contract, the status codes and the answer-record shape are identical to the
cluster run; only the generator behind them differs. P6 writes and tests the UI
against this, and on demo day the endpoint string changes - nothing else.

**The one-line brief for P6:**

> The UI only needs `GET /health`, `GET /papers`, `POST /answer` and (to render
> citation text) `POST /passages`; `/answer` returns the frozen five-key answer
> record. Develop against `python -m src.generation.server --backend mock`; on demo day
> the same endpoints are served by P5's cluster job. Full field reference:
> `docs/P6_UI_CONTRACT.md`.

---

## 3. The HTTP contract

| Endpoint | Method | Purpose |
|---|---|---|
| `/answer` | POST | one answer record, or one free-form question |
| `/health` | GET | liveness for the tunnel check and the UI status badge |
| `/papers` | GET | the paper ids the UI may offer in its selector |
| `/passages` | POST | citation id -> passage text; optional (503 when not loaded) |

`/passages` exists because citation ids are opaque hashes
(`qasper-passage-v1-<sha256>`), so a UI without it can only display ids. It is
kept separate from `/answer` so the answer record stays byte-identical to the
one in the scored JSONL files. The full field-by-field contract for P6 is
`docs/P6_UI_CONTRACT.md`.

**`POST /answer`** accepts exactly one of two bodies:

```json
{"record": { ...AgentState.model_dump(mode="json")... }}
```

```json
{"question": "What result is reported?", "paper_id": "1706.04115"}
```

The free-form form requires `paper_id` because QASPER retrieval is paper-scoped
(`paper_scope: question.paper_id`): a new question is about a paper already
indexed, not about an arbitrary paper.

The response is **the canonical answer record, unchanged** — the same object
`answer_record` returns to P4's harness:

```json
{
  "request_id": "q-001",
  "result": {"answer": "...", "citations": ["qasper-passage-v1-..."],
             "evidence_status": "SUFFICIENT", "retrieval_rounds": 1,
             "provenance": [{"claim": "...", "passage_ids": ["..."], "support": "direct"}]},
  "validation": {"violations": [], "downgraded": false, "downgrade_reason": null},
  "generation": {"backend": {...}, "prompt_version": "p5-grounded-qa-v7", ...},
  "agent": {"paper_id": "...", "sufficient": true, "gap_label": "NONE", ...}
}
```

`agent` is present when the input was an exported `AgentState`, and also on a
free-form question served by an agent hook (`--record-fn`), because the hook
returns that same exported state. Plain `--retriever` free-form answers do not
carry it.

Status codes are about **transport, not answers**:

| code | meaning | UI behaviour |
|---|---|---|
| 200 | an answer, including a refusal | read `result.evidence_status` |
| 400 | the payload is not the contract (no question, record not an object, both forms at once) | show a bug, not a refusal |
| 401 | bearer token configured and missing/wrong | fix the client |
| 429 | another answer is in flight | retry after ~20 s; do not block the UI |
| 503 | free-form sent with no retriever, or the backend is unavailable | disable the input, say why |

A refusal is a **200**. Treating it as an error would make refusals count as
demo failures and hide the ground-truth behaviour the project is about.

---

## 4. Start the service

After step 3 (vLLM venv) and step 2 (weights):

```bash
sbatch scripts/cluster/80_demo_server.sbatch
squeue --me
tail -f logs/p5-demo-<jobid>.out
```

The log prints, in order: the four preconditions, the node it landed on, the
job's end time, the tunnel command, and then — only after the weights load and
one warm-up answer runs — a line like:

```
READY TO TUNNEL - job 51234 on TC2N03, port 8000
```

If `fastapi`/`uvicorn` are missing from the venv the job stops and prints the
install command. Resubmit with `DEMO_INSTALL_DEPS=1` to let it install them
(pure Python; torch and transformers are not touched).

Useful overrides, all via `--export=ALL,...`:

| variable | default | meaning |
|---|---|---|
| `DEMO_PORT` | `8000` | port on the compute node |
| `DEMO_RETRIEVER` | none | `module:factory` for plain free-form retrieval; §7 |
| `DEMO_RECORD_FN` | none | `module:factory` for the agent hook; mutually exclusive with `DEMO_RETRIEVER`; §7.1 |
| `PAPERS_FROM` | `$P5_ROOT/data/corpus/passages.jsonl` | source of `GET /papers` |
| `PASSAGES_FROM` | `$P5_ROOT/data/corpus/passages.jsonl` | backing `POST /passages`; a corpus file or a retrieval dump both work (the dump's `retrieved_passages` are indexed) |
| `DEMO_WARMUP_RECORD` | built-in synthetic | JSONL whose first record warms up |
| `MAX_NEW_TOKENS` | `1024` | frozen v7 budget |

---

## 5. The tunnel — verify it before demo day

**Measured on this cluster (2026-10-29): SSH to the compute nodes is not
available.** Password authentication is denied, and the laptop's key is accepted
by the login node but **not** by the compute node, so `ssh -J ... <node>` cannot
work. The working method is the single-hop fallback — the server binds the node's
network interface and the *login node* opens the TCP connection, so no SSH
session to the compute node is created at all.

```bash
# on the login node
export DEMO_HOST=0.0.0.0
export DEMO_PORT=18080
export DEMO_TOKEN=<pick-one>
sbatch --time=06:00:00 --export=ALL scripts/cluster/80_demo_server.sbatch
```

```powershell
# on the laptop; <node> comes from the "READY TO TUNNEL" line
ssh -N -L 8000:<node>:18080 <you>@10.96.189.12
```

- `DEMO_HOST` other than `127.0.0.1` makes the job **refuse to start without
  `DEMO_TOKEN`** — the port is reachable from the cluster network, and `/answer`
  must not be open to it.
- The token travels as `Authorization: Bearer <token>` on `/answer` and
  `/passages`; `/health` and `/papers` stay open.
- Port 8000 on a compute node is often already taken; 18080 was free.
- Give the same token to the UI (`P5_API_TOKEN`), or every answer is a 401.

If a future cluster does allow compute-node SSH, the loopback form still works:
keep `DEMO_HOST=127.0.0.1` and use
`ssh -N -L 8000:localhost:<port> -J <you>@<login-host> <you>@<node>`.

**Local pre-check, no cluster and no GPU**: `scripts/smoke_demo_server.py` starts
two loopback servers (with and without a retriever) and exercises every endpoint
over real sockets, including the `{200, 429}` concurrency guarantee.

```bash
python scripts/smoke_demo_server.py
```

Run it after any change to `src.generation/server.py`, before a demo.

**The five-minute check** (do this once, on a throwaway job, before the demo):

1. submit `80_demo_server.sbatch`, wait for `READY TO TUNNEL`;
2. open the tunnel from the laptop;
3. `curl -s http://127.0.0.1:8000/health` — expect `"status": "ok"`,
   `"prompt_version": "p5-grounded-qa-v7"`, `"papers": <n>`;
4. `python scripts/demo_client.py --record runs/week3/p4_state_smoke.jsonl --token <token>`
   — expect `200 SUFFICIENT`, citations, and a latency of roughly 8-17 s;
5. cancel the job.

If step 3 fails, the problem is forwarding, not the model — and C is not viable
as planned. Switch the UI to the A+ replay contract (§8) rather than debugging
on demo day.

### Laptop power settings

The local shell is PowerShell:

```powershell
powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 15
```

Restore afterwards with the values you had (typically 10 and 10). Closing the
lid to "sleep" still breaks the tunnel even with the AC timeout disabled.

---

## 6. Demo-day operations

| Risk | Mitigation |
|---|---|
| 6-hour limit | submit so the window covers the whole demo, not just its start; the server prints a warning at 5 h 30 and 5 h 45 |
| job dies / node changes | resubmit, read the new node from the log, re-open the tunnel; the port and the UI URL do not change |
| laptop sleeps | §5 power settings; `ServerAliveInterval`; keep the tunnel in its own terminal |
| user hammers the button | the server returns 429 rather than queuing; the UI should show "busy, retry in ~20 s" |
| answer is slow | p90 is 16.9 s on this card; show a spinner and set the HTTP client timeout to at least 120 s |
| retriever is not wired | `/health` reports `"retrieval": false`; the UI disables free-form and offers records only |
| the UI is on someone else's laptop | that laptop cannot tunnel into this job; use configuration 1 or 2 in §2.1, or expose the tunnel on the LAN (§2.1) |
| everything is on fire | switch to A+ (§8) — the UI already reads that contract |

Two habits that cost nothing and save the demo:

- keep `squeue --me` visible in one terminal;
- leave the traceback in `logs/p5-demo-<jobid>.out` — the server logs one line
  per request with request id, paper, latency and violation codes.

---

## 7. Wiring free-form retrieval

The server knows nothing about P2's code. It accepts a factory:

```bash
sbatch --export=ALL,DEMO_RETRIEVER='src.retrieval.demo:make_retriever' \
       scripts/cluster/80_demo_server.sbatch
```

```python
# src/retrieval/demo.py  (owned by P2/P4, not by P5)
def make_retriever():
    # build/load BM25 + dense for the demo corpus, ONCE
    def retrieve(question: str, paper_id: str, top_k: int):
        return hybrid_retriever.search(question, paper_id=paper_id, top_k=top_k)
    return retrieve
```

Requirements on the returned callable:

- signature `(question, paper_id, top_k) -> list of hits`;
- hits may be P2's nested `{"passage": {...}}` objects or flat ones — both go
  through `build_request`, which is the same adapter the batch path uses;
- a hit must carry `passage_id` and `text`; an id the model can cite but the
  validator cannot resolve is worse than no hit.

Operationally:

- **Load the index at startup**, inside the factory. A factory that loads on the
  first request makes the demo's first question look broken.
- **Run the embedder and reranker on CPU.** The 8B engine at
  `gpu_memory_utilization=0.85` reserves ~38.3 GiB of the 45 GiB card; a
  single-query BGE embed is milliseconds on CPU, and keeping it there removes a
  whole class of OOM-at-hour-3 failures.
- The call is serialized with generation behind one lock, so a slow retriever
  delays the next question rather than crashing the engine.

If P5's copy is used, `--papers-from` should point at the same dump the retriever
was built from, so the UI's selector cannot offer a paper with no index.

### 7.1 The agent hook (`--record-fn`)

When the demo should show the agent loop and the critic, use the record hook
instead of a plain retriever. It is mutually exclusive with `--retriever`.

```bash
sbatch --export=ALL,DEMO_RECORD_FN='src.agent.demo:make_record_fn' \
       scripts/cluster/80_demo_server.sbatch
```

```python
# src/agent/demo.py  (owned by P4)
def make_record_fn(pipeline):                 # called once, after the engine loads
    retriever = build_demo_retriever()        # loads corpus/index, from env
    critic = GeneratorChatClient(pipeline.generator)   # same engine

    def record_fn(question: str, paper_id: str) -> dict:
        record = run_system(
            [ExperimentItem(question_id=..., question=question, paper_id=paper_id)],
            retriever, adaptive=True, critic_client=critic,
            top_k=5, answer_fn=None,          # P5 answers, once, in the server
        )[0]
        if "error" in record:
            raise RuntimeError(record["error"])
        return record                         # export_record(state), no "answer"
    return record_fn
```

The server calls `answer_record(pipeline, record)` after the hook, so the demo
and the batch runs share the parse/validate/downgrade path and there is exactly
one generation. A record that already contains `answer` is a 500, not a second
generation. `/health` reports `"agent": true`. The factory reads
`PAPERGAP_CORPUS`, `PAPERGAP_DENSE_INDEX`, `PAPERGAP_BM25_INDEX` and `HF_HOME`
from the job environment.

---

## 8. Fallback: Option A+ (replay)

The UI should be written so this is a data-source switch, not a rewrite. A+
needs three files and no cluster at all:

```
runs/week6/answers-vllm-*.jsonl     # answer records
<retrieval dump>.jsonl              # {passage_id: text} for citation highlighting
questions manifest                  # question_id -> question text
```

The join key is `request_id == question_id`. The UI renders `result`,
`validation.violations` and the `agent` block exactly as it would from the live
service, because the service returns the same record.

Switching to A+ during a failed demo is a configuration change in the UI, which
is why the three-file contract is worth building even though C is the plan.

---

## 9. Why not serve `vllm serve` and point the UI at it?

Because that exposes raw completion text and bypasses `parse_response` and
`CitationValidator`. The UI would then show answers whose citations were never
checked against the rendered passages, and the downgrade-to-refusal policy —
the thing the project is about — would silently not apply. The wrapper exists so
that the demo and the evaluation cannot diverge.

---

## 10. Known limits, stated honestly

- one question at a time (429 under concurrency);
- no streaming; the first token appears after the whole answer is validated;
- no gold answers on the 100-question pool, so the UI can show compliance
  (`SUFFICIENT` / violations), not correctness;
- free-form is paper-scoped, not open-domain;
- the service is tied to one 6-hour job and one node;
- no authentication unless `--token` is passed (loopback plus tunnel is the
  security boundary).
