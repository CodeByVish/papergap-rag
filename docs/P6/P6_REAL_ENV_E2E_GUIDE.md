# P6 real-environment end-to-end test guide

Updated after rebase on 2026-10-29 (Singapore). Reviewed UI code: `4584e2c`;
base main: `97e33b2`, including P5 service/contract `ef5f7a3`. The current P6 branch
contains both implementations. No P6 cluster job was submitted during this work;
account, quota, files and forwarding remain to be verified remotely.

## Decision: can P6 run it?

**Yes, the supported architecture includes P6 submitting the job under P6's own
account, opening a tunnel on P6's laptop, and running Streamlit there.** P5's latest
message selects configuration 2 in `docs/DEMO_OPTION_C.md` section 2.1. Older
statements that P5 must operate the demo are superseded for this deployment.

However, the complete operational information chain is not yet closed:

| Test scope | Can proceed when | Remaining dependency |
| --- | --- | --- |
| Laptop UI + actual P5 mock API | Current rebased P6 checkout; CPU Python deps installed | Verified locally during this review |
| Laptop -> tunnel -> GPU -> real Qwen generation/validation -> citations | Own cluster access/allocation, readable weights, working vLLM environment and approved input dump | Account-specific availability and paths not supplied/verified |
| Fresh user question -> retrieval -> real Qwen -> citations | Above plus a real retriever factory, its dependencies/indexes and matching paper list | P5 explicitly reports free-form retrieval is not connected; real factory absent in the current checkout |
| Fresh query -> P4 adaptive agent/critic/retries -> generation | An explicit service integration that runs P4's agent | Current free-form endpoint only calls the retriever once and then answer_record; no P4 graph execution |

The first real-GPU path uses an **exported retrieval/agent state as input** and
performs fresh model inference. It is not replay of a precomputed answer, but it
also does not run new retrieval or rerun the agent. Do not describe that as a
fully verified fresh-query RAG/agent chain.

## What must be obtained or confirmed

1. P6's cluster username, login/VPN procedure and Slurm GPU quota. Confirm whether
   a partition/account flag is required; P5's script leaves those unspecified.
   The demo requests one GPU, 8 CPUs, 48 GiB RAM and up to six hours. It does not
   pin the GPU model: confirm an A40 (~45 GiB) or a P5-approved equivalent, rather
   than assuming every available GPU can hold this configuration.
2. A P6-readable persistent root, free storage/quota, complete Qwen3-8B checkpoint
   and exact revision. P5's `~/p5` is P5's home, not automatically P6's resources.
3. P6's own working vLLM Python environment, or an explicitly approved compatible
   shared environment. P5 records Python 3.12, vLLM 0.11.0, Transformers 4.x and
   a CUDA-12-compatible Torch stack. Do not upgrade an established environment.
4. An approved development exported-state/retrieval dump on the cluster and a
   local copy for UI record selection. Ask P5 which file is appropriate and how
   P6 may read/copy it. No held-out tuning and no dataset/result commits.
5. For arbitrary questions: P2/P5 must supply the actual `module:factory`, required
   environment variables, matching corpus/index/cache paths and CPU retrieval
   installation instructions. `src.retrieval.demo:make_retriever` in the P5 manual
   is an **example**, not an existing implementation.
6. For original text: `PASSAGES_FROM` may point to the same retrieval dump; this
   resolves its embedded passages. Full-corpus coverage needs P3's corpus. A dump
   is sufficient for an initial record-mode test; a full corpus is not mandatory.

No need for P5's password/account, external LLM API subscription or OpenAI key.
P6 chooses a demo bearer token and configures the same value on server and UI.

## What was actually checked locally

Post-rebase combined tests returned **100 passed, 1 skipped**. The default skip
is the opt-in running-service check. That check separately passed against the
actual P5 mock API with Bearer authentication, synthetic input and the Streamlit
record/citation workflow. P5's socket smoke also passed **15/15**, including busy
handling and test-retriever on/off behavior. These are distinct evidence types,
not real GPU or P2 retrieval measurements; see the
[completion summary](UI_PORT_COMPLETION_SUMMARY.md) for exact commands/counts.

Confirmed interface correction: `/papers` is `{"papers": ["paper-id", ...]}`,
not a list of paper objects. P6 now normalizes string IDs internally; existing
object fixtures remain supported. Authentication is confirmed as
`Authorization: Bearer <token>`. Set both the header and scheme variables below;
setting only P5_API_TOKEN is insufficient for this UI version.

P5 `/health` reports `backend`/`model_id`/`prompt_version`, not `mode`. The UI may
therefore display mode unknown. Use saved health and answer backend metadata to
establish real-vs-mock evidence; do not infer live status from an open port.

## 1. Use the same current source on laptop and cluster

The current `P6/UI-port-integration` branch has already been rebased onto main
`97e33b2`; P5's service is included. **Do not repeat the old separate-branch merge.**
In the existing local P6 checkout, inspect source identity without changing it:

```bash
git branch --show-current
git rev-parse HEAD
git merge-base --is-ancestor 97e33b2 HEAD
git merge-base --is-ancestor 4584e2c HEAD
```

For a new laptop or cluster checkout, the branch owner must first publish the
reviewed rebased branch. This guide does not push or rewrite the remote branch.
Do not assume an older remote P6 branch contains the current code. Once published,
clone into a new directory rather than resetting another workspace:

```bash
git clone --branch P6/UI-port-integration https://github.com/CodeByVish/papergap-rag.git papergap-p6-e2e
cd papergap-p6-e2e
git merge-base --is-ancestor 97e33b2 HEAD
git merge-base --is-ancestor 4584e2c HEAD
git rev-parse HEAD
```

Both ancestor checks must exit 0. Record the same exact source commit on laptop
and cluster; no merge into main is needed to rehearse. If a reviewed source archive
is used instead, record its originating commit and archive hash. Do not transfer
laptop virtualenvs/secrets or put data/models in Git. Confirm both trees contain:

```bash
test -f src/generation/server.py
test -f src/ui/api_client.py
test -f scripts/cluster/80_demo_server.sbatch
test -f docs/P6_UI_CONTRACT.md
```

## 2. Laptop CPU preflight before spending GPU quota

Commands below use **Bash**. Start `bash` first if using macOS zsh and follow the
same shell syntax throughout. From the current P6 repository root:

```bash
python3 -m venv .venv-ui
source .venv-ui/bin/activate
python -m pip install -r requirements-ui.txt 'fastapi>=0.110,<1' 'uvicorn>=0.29,<1' pytest
python scripts/smoke_demo_server.py
```

This installs only the UI plus CPU mock-server/test dependencies. It does not
install the complete research requirements or download Qwen. `pydantic` is already
in requirements-ui. Do not install the laptop dependency snapshot into vLLM.

For a record-mode mock UI rehearsal, create a synthetic input (no real dataset):

```bash
mkdir -p results/p6-ui
python - <<'PYMOCK'
import json
from pathlib import Path
from src.generation.server import WARMUP_RECORD
Path('results/p6-ui/mock-inputs.jsonl').write_text(json.dumps(WARMUP_RECORD) + '\n')
PYMOCK
export P5_RECORDS_PATH="$PWD/results/p6-ui/mock-inputs.jsonl"
python -m src.generation.server --backend mock --port 8000 --papers-from "$P5_RECORDS_PATH" --passages-from "$P5_RECORDS_PATH"
```

In a second terminal, activate the same UI environment, set P5_API_BASE to localhost
port 8000 and P5_RECORDS_PATH to that file's absolute path, and launch Streamlit as
in the handoff. Leave token settings unset for this token-free loopback mock.
Choose Demo record. retrieval=false is expected; the synthetic passage lookup is
available. This is a CPU mock check, not real generation/retrieval evidence. Shut
down the local mock API before reserving local port 8000 for the cluster tunnel.

## 3. Prepare P6's cluster account once

On the laptop, replace the username; the IP is the login host documented by P5.
Confirm VPN/routing and that P6 uses this same cluster:

```bash
export P6_CLUSTER_USER='REPLACE_WITH_YOUR_USERNAME'
export P6_LOGIN_HOST='10.96.189.12'
ssh "$P6_CLUSTER_USER@$P6_LOGIN_HOST"
```

On the cluster login node, enter the same reviewed P6 source checkout. Check allocation
options and create persistent directories **before** submitting Slurm jobs:

```bash
sinfo
squeue --me
mkdir -p logs
export P5_ROOT="$HOME/p6-demo-runtime"
mkdir -p "$P5_ROOT/models" "$P5_ROOT/data"
df -h "$P5_ROOT"
```

P5_ROOT is the script's existing configurable variable; its name does not require
P5's account. Check your storage quota separately using the site's supported tool.
Weights are roughly 16–17 GiB, and environments/caches need substantial additional
space (allow tens of GiB beyond weights). Exact available storage is account-specific.

Preferred: reuse/copy a **permitted complete model snapshot** supplied by P5 into
`$P5_ROOT/models/Qwen3-8B`, recording its revision. Alternatively P5's documented
bootstrap scripts are:

```bash
sbatch --export=ALL scripts/cluster/20_load_qwen3.sbatch
# Wait for completion and inspect logs/p5-load-qwen3-<jobid>.out first.
sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch
# Wait for completion and inspect logs/p5-vllm-<jobid>.out first.
```

These are separate sequential jobs, not commands to launch together blindly.
Add your site's required partition/account flags if needed. Step 20 is an older
Transformers/download/bootstrap job; its dependencies and interpreter are not the
pinned vLLM environment. If it fails, inspect the cause with P5 rather than upgrade
the pinned vLLM stack. A `config.json` alone does not prove all weight shards were
downloaded; the vLLM load/smoke in step 30 is the practical gate. Downloads use
network/storage and may need site-approved access. Never run model inference on
the login node.

The documented vLLM default is `vllm==0.11.0` with Transformers <5, not the newest
vLLM. Verify the available Python module spelling using `module avail python`;
`python312` is P5's measured value, not guaranteed for every account/site.

The service defaults are max_new_tokens=1024, max_model_len=32768 and
vLLM gpu_memory_utilization=0.85. Step 80 exposes token/top-k environment knobs,
not arbitrary constructor overrides. Confirm with P5 before changing the pinned
stack, context budget or GPU settings; record actual configuration with results.

Set an explicit working venv after setup (replace the path with the one printed
in step 30's log; do not use a literal placeholder):

```bash
export VLLM_VENV='/absolute/path/from/the/successful/vllm-job-log'
test -x "$VLLM_VENV/bin/python"
test -f "$P5_ROOT/models/Qwen3-8B/config.json"
```

Copy the approved input dump into `$P5_ROOT/data/demo-inputs.jsonl` through an
approved transfer/shared path, retaining hashes. The same file on the laptop
will be selected by P5_RECORDS_PATH. Do not assume P5's home files are readable.

## 4. Submit the real demo service under P6's account

On the cluster login node, from the P6 repository root in Bash:

```bash
export P5_ROOT="$HOME/p6-demo-runtime"
# Re-export your actual VLLM_VENV here if this is a new SSH session.
export PAPERS_FROM="$P5_ROOT/data/demo-inputs.jsonl"
export PASSAGES_FROM="$P5_ROOT/data/demo-inputs.jsonl"
export DEMO_WARMUP_RECORD="$P5_ROOT/data/demo-inputs.jsonl"
export DEMO_HOST=0.0.0.0
export DEMO_PORT=18080
read -r -s -p 'Choose the demo bearer token: ' DEMO_TOKEN
printf '\n'
export DEMO_TOKEN
unset DEMO_RETRIEVER
mkdir -p logs
sbatch --export=ALL scripts/cluster/80_demo_server.sbatch
squeue --me
```

Record the returned job ID. `unset DEMO_RETRIEVER` deliberately starts the known
record-generation path first. If FastAPI/uvicorn are missing, the job prints its
install instruction; after checking compatibility with P5, resubmit with
`DEMO_INSTALL_DEPS=1` exported. Do not reinstall all research requirements into
a working pinned vLLM environment. The script may request a whole GPU for up to
six hours; cancel rehearsal jobs when finished.

```bash
tail -f logs/p5-demo-REPLACE_JOB_ID.out
```

Wait for `READY TO TUNNEL - job ... on <ACTUAL_NODE>, port 18080`, then inspect
that the server remains running with no bind/load traceback. Note the allocated
node and job end time. Readiness is a socket probe, not proof of a generated
answer. If the port is occupied, cancel your failed job and resubmit on an agreed
free port, updating the tunnel destination to match.

## 5. Open the verified tunnel form on the laptop

P5 measured that compute-node SSH is unavailable. Use the single-hop login-node
TCP forwarding path, not the old ProxyJump/compute-SSH recipe. In a dedicated
laptop Bash terminal (replace node and username with actual values):

```bash
export P6_CLUSTER_USER='REPLACE_WITH_YOUR_USERNAME'
export P6_LOGIN_HOST='10.96.189.12'
export P6_COMPUTE_NODE='REPLACE_FROM_READY_LOG'
ssh -N \
  -o ExitOnForwardFailure=yes \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -L "127.0.0.1:8000:${P6_COMPUTE_NODE}:18080" \
  "$P6_CLUSTER_USER@$P6_LOGIN_HOST"
```

Leave it running and keep the laptop awake during the rehearsal. The compute
service binds its network interface, so the token is required. The laptop tunnel
and UI stay loopback-only. P5's successful forwarding is evidence for that account;
confirm this path also works for P6. Do not assume network access to the login
host establishes compute-port forwarding permission.

In another laptop terminal:

```bash
curl --fail --show-error http://127.0.0.1:8000/health
curl --fail --show-error http://127.0.0.1:8000/papers
```

Expected: status=ok, backend=vllm, correct local Qwen model path,
prompt_version=p5-grounded-qa-v7, nonempty paper IDs. For the initial record path,
retrieval=false is expected; passage_text=true requires usable embedded passages.
A mock backend or empty passage index is not a real-generation/text-display pass.

## 6. Start Streamlit and prove actual model generation

In a separate laptop Bash terminal, from the P6 checkout:

```bash
source .venv-ui/bin/activate
export P5_API_BASE=http://127.0.0.1:8000
export P5_RECORDS_PATH='/absolute/local/path/to/the/approved/demo-inputs.jsonl'
export P5_ANSWER_TIMEOUT=180
export P5_AUTH_HEADER=Authorization
export P5_AUTH_SCHEME=Bearer
read -r -s -p 'Enter the SAME demo bearer token: ' P5_API_TOKEN
printf '\n'
export P5_API_TOKEN
python -m streamlit run src/ui/app.py --server.address 127.0.0.1
```

Open `http://127.0.0.1:8501`. Refresh service, choose Demo record, create a workspace,
select a **nonempty-context, generation-eligible development input**, and Submit.

Check all of the following, not just HTTP 200:

- The question/record identity is correct and a client run ID is displayed.
- The returned generation backend identifies vLLM/Qwen, with the expected prompt.
- Server logs show this submitted request; validation has no GENERATION_ERROR or
  unexpected parser failure. EMPTY_CONTEXT/AGENT_INSUFFICIENT can intentionally
  skip model inference, so those inputs alone cannot prove the real model ran.
- A valid model refusal is a legitimate generated result; it need not be SUFFICIENT.
- Citation IDs match the returned result and lookup text is shown when present.
- Submit the same record twice: two different client run IDs, original P5 request_id
  preserved. Refresh/expand diagnostics does not make a third answer call.
- Run the actual-service UI smoke in the same configured environment:

```bash
P5_RUN_SMOKE=1 python -m pytest -q tests/test_ui_p5_smoke.py::test_actual_p5_service
```

This smoke makes two sequential answer calls; account for the extra inference time.
It proves UI/HTTP shape, not semantic correctness or the absence of generation
errors, so also perform the metadata/log checks above. Do not run it concurrently
with another answer unless explicitly testing 429.

## 7. Enable fresh-query retrieval only after P2/P5 supplies it

Obtain the real factory and dependencies, matching indexes/corpus/paper coverage,
cache locations, and CPU encoder/reranker settings. First prove factory imports
and its returned callable inside an allocated job/environment. Do not replace
it with a static dump lookup and label that fresh retrieval.

On the login node, stop your old server, re-export the settings from section 4,
and set the **actual** approved factory:

```bash
export DEMO_RETRIEVER='REPLACE_WITH_REAL_MODULE:FACTORY'
sbatch --export=ALL scripts/cluster/80_demo_server.sbatch
```

A factory may require its own environment variables; export the exact settings
provided by P2/P5. Startup loads it once. Re-read the new node from the log,
rebuild the tunnel, and confirm retrieval=true and the catalogue covers the
same indexed papers. In Streamlit create a Free question workspace, choose a
paper, ask five independent complete development questions, inspect citations
and download the five runs.

Until this factory/data path is supplied, this section is **blocked**. No missing
P6 API key or GPU flag can enable it. The current endpoint still does not execute
P4's adaptive graph; a full agent demonstration needs a separately reviewed
P4/P5 integration and evidence of critic/retry traces generated for these queries.

## 8. Failure, concurrency and evidence checks

| Scenario | Expected outcome |
| --- | --- |
| Wrong token | 401 shown as authentication issue, not refusal |
| Two browser sessions submit while one is running | One accepted, overlapping call 429; no history mixing |
| Retrieval unavailable | Free input disabled; exported records remain usable |
| Passage lookup missing/503 | Final answer retained; citation IDs remain visible |
| Validator downgrade | Final refusal and reason; original answer clearly rejected |
| Timeout/disconnect | Outcome unknown; no automatic retry/cancellation claim |
| Job/node changes | Read new node, rebuild tunnel, refresh health before another query |
| New tab/reconnect | No durable session-history or abandoned-run recovery promise |

Do not cancel a successful shared GPU job to simulate failure. Perform failure
experiments only on your own rehearsal job and preserve its prior results.
Long-call timing and 429 are best tested during rehearsal, not presentation.

Save health JSON, sanitized screenshots, UI exports and relevant log excerpts
outside Git. Record source commits, model revision, package versions, GPU/job/node,
input/corpus/index hashes, capability flags and timing definitions. P5's supplied
17-second latency is not a new P6 measurement. Mode unknown in an export must be
accompanied by actual health/backend evidence, not relabeled silently.

| Scope | Date / job / revisions | Pass / fail / blocked | Evidence / remaining owner |
| --- | --- | --- | --- |
| P6 account and GPU runtime | Fill after execution | Not run | P6 |
| Real exported-state generation + citations | Fill after execution | Not run | P6/P5 runtime paths |
| Fresh-query retrieval + generation | Fill after execution | Blocked pending factory | P2/P5 |
| Adaptive P4 agent chain | Fill after execution | Not implemented by this service path | P4/P5 |
| Repeated runs / 429 / timeout / export | Fill after execution | Not run on cluster | P6 |

When finished, stop Streamlit and the tunnel with Ctrl+C, then cancel only your
own recorded job from the login node:

```bash
scancel REPLACE_WITH_YOUR_JOB_ID
squeue --me
unset DEMO_TOKEN
```

Unset P5_API_TOKEN in the laptop shell as well. No model inference on the login
node, no credentials/model/index/corpus artifacts in Git, and no merging to main
without the required member review. Passage/split schemas remain `v0-proposed`.
