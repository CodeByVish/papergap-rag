# P6 UI handoff to P5

Updated: 2026-11-03 (Singapore). Existing branch: `P6/UI-port-integration`;
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

## 0. Download and copy the P3 passage corpus

Download [P3's passages.jsonl](https://github.com/CodeByVish/papergap-rag/blob/p3-qasper-foundation/data/processed/passages.jsonl)
using GitHub's **Download raw file** action, then copy it to
`data/processed/passages.jsonl` in this checkout. Save the JSONL itself, not the
GitHub HTML page. 
Expect `data/processed/passages.jsonl: OK`. This download supplies the passage corpus only.

## 1. Run the prepared demo on this Mac (Ollama)

These commands use the existing checkout and prepared Python environment. They do
not create branches, commit or push. In a Mac terminal (zsh or bash):

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
./scripts/p6-local.sh config
ollama list
curl --fail --silent --show-error http://127.0.0.1:11434/api/tags
./scripts/p6-local.sh start
```

If the Ollama check fails, open the Ollama macOS app (or run `ollama serve` in a
separate terminal), then retry. The prepared model is `qwen3:14b`; do not download
another model unless intentionally changing the experiment. If a private
`.env.p6.local` exists, `config` shows its effective overrides; defaults alone
select Ollama. Config output masks the token.

Wait for `API ready` and `Open http://127.0.0.1:8501`, then open
[the UI](http://127.0.0.1:8501). Keep the launcher terminal running. Ctrl+C stops
its API and UI, but does not stop the existing Ollama service. If ports 8000/8501
are occupied by a previous launcher, stop that launcher in its own terminal first;
do not start a second copy or kill unrelated processes.

The launcher supplies these locations automatically; do not fill env vars by hand:

| Item | Prepared location/value |
| --- | --- |
| Saved defaults | `configs/p6-local.env`, with optional ignored `.env.p6.local` overrides |
| UI / P5 API / Ollama | `127.0.0.1:8501` / `127.0.0.1:8000` / `127.0.0.1:11434` |
| LLM | Ollama `qwen3:14b`; model files managed under `/Users/changyanxu/.ollama/models/` |
| P3 text corpus | `data/processed/passages.jsonl`: 21,360 passages from 1,168 development papers |
| Dense index | `indexes/p6-development-bge/`; BM25, RRF and BGE reranking use the same corpus |
| Retrieval model cache | `.cache/huggingface/hub/` |
| Question library | `results/p6-local/sample-questions.jsonl` plus corpus topic examples in the UI |
| Readable samples | `results/p6-local/SAMPLE_QUESTIONS.md` |
| Paper titles | `data/processed/p6-paper-catalog.json` |
| Optional prepared-record inputs | `results/p6-local/demo-records.jsonl` (`P5_RECORDS_PATH`); this is not the corpus |
| API logs / reproducibility | `results/p6-local/api.log` / `results/p6-local/runtime.json` |
| Authentication | No token required for the prepared local loopback API |

From a second Mac terminal, check readiness:

```bash
curl --fail --silent --show-error http://127.0.0.1:8000/health
```

Expect backend `ollama`, model `qwen3:14b`, and `retrieval`, `passage_text`,
`corpus_search`, `agent` all `true` for the default adaptive configuration.
The API appears only after the models/indexes finish loading. Startup failure:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
tail -n 100 results/p6-local/api.log
```

For rebuilding a missing environment/corpus/index, use section 5 of the
[full E2E guide](P6_REAL_ENV_E2E_GUIDE.md); a normal demo does not need setup again.

## 2. Connect to school GPU: choose the service capability first

Read section 2.0 before choosing a route. Sections 2.1–2.6 deploy the **full P6
pipeline**; connecting to P5's existing record-only service needs only route A.

**Deployment recipe, not an executed school test.** Account access, approved
GPU allocation, server paths and the compatible vLLM environment are still needed.
Keep the same UI/API contract. **Route B** moves the **P5 API, hybrid retrieval,
P4 agent and generation** to the allocated GPU node; the Mac keeps Streamlit.
It does not connect the UI to a raw model endpoint.

```text
Route B: Mac browser :8501 -> Mac Streamlit -> Mac :8000 (SSH tunnel)
  -> allocated GPU node :18080 (P5 API + retrieval + agent + vLLM/Qwen3-8B)
```

### 2.0 Compatibility with P5's supplied cluster guide

Reference reviewed 2026-11-03: P5's supplied `启动集群.md`, which reports a
2026-10-29 run. Its node/job IDs, timings and counts are historical examples;
check the actual running job and `/health` rather than reusing them.
Do not copy its example token into shared source/config files.

**The P6 UI matches the API, but P5's documented deployment is record-only.**
The full-GPU recipe in sections 2.1–2.6 is a different runtime deployment, not a
description of capabilities already enabled on that P5 server.

| Concern | P5 supplied guide | Current P6 full-pipeline recipe | Action |
| --- | --- | --- | --- |
| SSH route | Compute-node SSH/ProxyJump unavailable; login node forwards TCP to compute node | Same single-hop `-L 127.0.0.1:8000:NODE:18080 LOGIN` | Compatible; do not use `-J` on this setup |
| API auth and endpoints | Bearer token; `/health`, `/papers`, `/answer`, `/passages` | Same HTTP boundary | Existing UI can connect by config |
| Code/entry point | Standalone `~/project-nlp-p5`, `nlp_p5.server`, `80_demo_server.sbatch` | Shared project checkout, `scripts.p6_local serve` | Full pipeline needs this shared runtime, not just an env change in the old job |
| LLM/environment | `~/p5/models/Qwen3-8B`; `~/p5/vllm-venv-vllm__0_11_0_python312_defaultbin` | Can reuse approved readable weights/environment; also needs retrieval/agent dependencies | Resolve absolute paths under your authorized account; validate GPU imports |
| Fresh questions | Explicitly `retrieval=false`; free input returns 503 | Corpus hybrid retrieval and adaptive graph enabled | Cannot enable missing server capabilities from UI config |
| Passage text | Retrieval dump covering 478 passages / 93 papers in that reported run | Matching P3 corpus: 21,360 passages / 1,168 papers | P5 dump is not a substitute for the full corpus/index |
| Agent trace | May be supplied by the posted AgentState | Fresh graph execution on Free question | An `agent` block alone does not prove a fresh critic run |
| Configuration names | `DEMO_HOST`, `DEMO_PORT`, `DEMO_TOKEN`, `PASSAGES_FROM`, `DEMO_RETRIEVER` | `P6_API_HOST`, `P6_API_PORT`, `P5_API_TOKEN`, `PAPERGAP_CORPUS`, built-in corpus retriever | Separate launchers; these names are not interchangeable aliases |

**Choose the route:**

- **A — connect to P5's existing record-only service:** no P6 application-code
  change or new GPU deployment. Set the Mac UI config, open the tunnel and choose
  Demo record. This verifies UI/generation/citations, not fresh hybrid retrieval.
- **B — preserve the current All papers + hybrid + agent demo on GPU:** follow
  sections 2.1–2.6 once, using a separate existing shared-project runtime checkout.
  Do not overlay this source onto P5's standalone checkout. The current P6 runtime
  already supports its vLLM backend; no new LLM adapter is required for this route.
  Source/artifact transfer, compatible dependencies and the correct GPU launch
  entry point are one-time prerequisites. Afterwards, selecting the private UI
  config and opening the tunnel switches between deployed local/school APIs.

For **route A**, P5 (or the authorized operator) starts the existing job using
P5's own guide. Obtain its current node, API token and an original compatible
AgentState input. Do not change or restart another operator's job. On this Mac:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
export P6_SCHOOL_SSH='YOUR_AUTHORIZED_USER@YOUR_LOGIN_HOST'
mkdir -p results/p6-school
# P5's guide places this original input under ~/project-nlp-p5 on its account.
# Adjust the remote input path only if the authorized operator supplied another.
scp "$P6_SCHOOL_SSH:project-nlp-p5/runs/week3/p4_state_smoke.jsonl" \
  results/p6-school/p5-state-smoke.jsonl
```

This path is on the SSH account being used. Another account does not automatically
have access to P5's checkout/weights/job. Ask the operator for an approved copy
if needed. Keep this input local/ignored; an `answer.json` capture is not valid
as input. Do not assume the Mac's default P3 demo records share the passage IDs
available in P5's small retrieval dump.

Create the private UI config once; if it already exists, edit/reuse it instead:

```bash
if [ ! -e .env.p6.p5-ui ]; then
  (umask 077; cp configs/p6-p5-record-ui.env.example .env.p6.p5-ui)
fi
chmod 600 .env.p6.p5-ui
nano .env.p6.p5-ui
```

Replace `P5_API_TOKEN` with the **existing job's current DEMO_TOKEN**, not a newly
generated different token. The template already sets `Authorization`, `Bearer`,
the Mac input path, a 900-second timeout and the tunnel URL. `P6_BACKEND` and
`P6_MODEL` do not select a model in `remote` mode: the running API does.

Stop any local `start` launcher to free ports 8000/8501. In **Mac terminal A**,
set the actual node reported by the current job and keep the tunnel open:

```bash
export P6_SCHOOL_SSH='YOUR_AUTHORIZED_USER@YOUR_LOGIN_HOST'
P6_COMPUTE_NODE='ACTUAL_RUNNING_JOB_NODE'
ssh -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 \
  -L "127.0.0.1:8000:$P6_COMPUTE_NODE:18080" "$P6_SCHOOL_SSH"
```

In **Mac terminal B**:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
curl --fail --silent --show-error http://127.0.0.1:8000/health
P6_CONFIG_FILE=.env.p6.p5-ui ./scripts/p6-local.sh config
P6_CONFIG_FILE=.env.p6.p5-ui ./scripts/p6-local.sh remote
```

For the service described in P5's guide, expect `backend=vllm`,
`retrieval=false`, `passage_text=true`; `corpus_search` may be absent. In the UI,
choose **Advanced settings → Input mode → Demo record → Exported record → Ask
question**. Free question being disabled is expected, not a broken UI. The
reported 93 papers/478 passages are not required constants for a later job.

The current full-pipeline sections below deliberately expect `retrieval=true`,
`corpus_search=true`, `agent=true`; those expectations apply to **route B only**.
Adding `DEMO_RETRIEVER` to P5's original service would require a compatible
installed factory/index and does not by itself reproduce P6's all-paper adaptive
runtime. If the intent is instead to keep retrieval on the Mac and move **only
LLM calls** to GPU, P5's guide does not expose a general chat endpoint for P4's
critic; that is a third architecture requiring an additional remote model adapter,
not a config-only switch supported by the current P6 launcher.


### 2.1 Route B: what changes for the full pipeline

| Setting | Local Ollama | School GPU |
| --- | --- | --- |
| Launch API | `./scripts/p6-local.sh start` starts local API and UI | GPU allocation runs `python -m scripts.p6_local serve`; Mac runs `remote` |
| `P6_BACKEND` (API host) | `ollama` | `vllm` |
| `P6_MODEL` (API host) | Installed Ollama tag `qwen3:14b` | Absolute approved **local Qwen3-8B checkpoint directory on GPU host** |
| `P6_API_HOST`, `P6_API_PORT` | `127.0.0.1`, `8000` | `0.0.0.0`, `18080` for the login-node TCP-forwarding route below |
| Corpus/index/cache paths | Mac paths resolved from the checkout | GPU-host paths to copies of the matching artifacts |
| `P6_PIPELINE` | `adaptive` | Keep `adaptive` for fresh critic/retry traces |
| Retrieval device | `cpu` | Keep `DEMO_AGENT_DEVICE=cpu`; vLLM uses the allocated GPU |
| `P5_API_BASE` (Mac UI) | `http://127.0.0.1:8000` | Same URL, now backed by the SSH tunnel |
| API authentication | Blank | Same private token on GPU API and Mac UI; `Authorization: Bearer` |
| `P6_OLLAMA_BASE`, `P6_OLLAMA_CONTEXT` | Used by Ollama adapter | Ignored by the `vllm` branch; no Ollama process needed |

`P6_MODEL` is **not** a server URL. P5's vLLM backend loads the checkpoint in
process and shares that generator with the critic. Current backend defaults are
BF16, one GPU, a 32,768-token context limit and 0.85 GPU memory utilization; use
a P5-approved GPU/environment that can support them. The P6 launcher does not
expose context/VRAM tuning as environment variables. There is no separate
`vllm serve` command in this launch path. Changing from quantized local 14B to
school 8B changes the experiment; record model/revision and timings separately.

The loader reads `configs/p6-local.env` then the file selected by
`P6_CONFIG_FILE`. It replaces stale shell exports. A selected school override
replaces `.env.p6.local` as the override file; it does not stack on top of it.
Do not edit the shared defaults or merely export `P6_BACKEND=vllm`.

### 2.2 Prepare the GPU runtime and copy this working tree

Use a shared-project runtime checkout separate from P5's standalone
`project-nlp-p5` directory. The school host must already have an **existing Git checkout** for this project
(the launcher records Git metadata), P5's approved Linux/CUDA/vLLM environment,
and complete Qwen3-8B weights. Use the intended runtime checkout; the following
sync updates its code. This is necessary because the current Mac implementation
is uncommitted and will not arrive through a Git pull. No push is required.
Do not copy the Mac `.venv-p6`, Ollama model store or OpenMP repair to Linux, and
do not install the Mac requirements snapshot into P5's pinned GPU environment.

In the Mac terminal, replace these four values with your confirmed school values:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
export P6_SCHOOL_SSH='YOUR_USER@YOUR_LOGIN_HOST'
export P6_SCHOOL_REPO='/absolute/path/to/existing/papergap-rag'
export P6_SCHOOL_VENV='/absolute/path/to/approved/vllm-venv'
export P6_SCHOOL_MODEL='/absolute/path/to/approved/Qwen3-8B'
```

On the school login host, create artifact destinations in that existing checkout
(using the same repository path as above):

```bash
cd /absolute/path/to/existing/papergap-rag
mkdir -p data/processed indexes/p6-development-bge .cache/huggingface/hub logs results/p6-school
```

Back on the Mac, copy the current source and matching generated artifacts:

```bash
rsync -az --exclude='__pycache__' src scripts configs \
  "$P6_SCHOOL_SSH:$P6_SCHOOL_REPO/"
rsync -az data/processed/passages.jsonl data/processed/passages.manifest.json \
  data/processed/p6-paper-catalog.json "$P6_SCHOOL_SSH:$P6_SCHOOL_REPO/data/processed/"
rsync -az indexes/p6-development-bge/ \
  "$P6_SCHOOL_SSH:$P6_SCHOOL_REPO/indexes/p6-development-bge/"
rsync -az .cache/huggingface/hub/ \
  "$P6_SCHOOL_SSH:$P6_SCHOOL_REPO/.cache/huggingface/hub/"
```

The cache transfer includes the prepared BGE encoder/reranker snapshots and their
relative symlinks. Keep corpus, index and cache out of Git. Mac-side samples and
Demo record files stay on the Mac: the UI sends the selected record in the POST.
The remote API does not need local UI sample files for free questions.

### 2.3 Create the two private configs with one shared token

In the **same Mac terminal** as the exported values, run this once. It generates
both ignored files, sets mode `0600`, and never prints the token. This is for
a **new route-B API job**, not for connecting to an existing P5 job whose token
is already fixed. It refuses to
replace existing configs; if they already exist, review/reuse them instead.

```bash
.venv-p6/bin/python - <<'PY'
import os
import secrets
from pathlib import Path

root = os.environ['P6_SCHOOL_REPO'].rstrip('/')
model = os.environ['P6_SCHOOL_MODEL']
paths = [Path('.env.p6.school'), Path('.env.p6.school-ui')]
if any(path.exists() for path in paths):
    raise SystemExit('Private school config already exists; review/reuse it instead of overwriting.')
if not root.startswith('/') or not model.startswith('/'):
    raise SystemExit('Set absolute GPU repository and checkpoint paths first.')
# Quote paths so spaces are preserved in dotenv values.
def quoted(value):
    if any(c in value for c in "'\n\r"):
        raise SystemExit('Use paths without single quotes or newlines.')
    return "'" + value + "'"
token = secrets.token_hex(32)
shared = f'P5_API_TOKEN={token}\nP5_AUTH_HEADER=Authorization\nP5_AUTH_SCHEME=Bearer\n'
server = (
    'P6_BACKEND=vllm\nP6_PIPELINE=adaptive\nP6_API_HOST=0.0.0.0\nP6_API_PORT=18080\n'
    'DEMO_AGENT_DEVICE=cpu\nDEMO_AGENT_OFFLINE=1\n'
    f'P6_MODEL={quoted(model)}\n'
    f'PAPERGAP_CORPUS={quoted(root + "/data/processed/passages.jsonl")}\n'
    f'PAPERGAP_DENSE_INDEX={quoted(root + "/indexes/p6-development-bge")}\n'
    f'HF_HOME={quoted(root + "/.cache/huggingface")}\n'
    f'DEMO_AGENT_CACHE_FOLDER={quoted(root + "/.cache/huggingface/hub")}\n'
    + shared
)
ui = 'P5_API_BASE=http://127.0.0.1:8000\nP5_ANSWER_TIMEOUT=900\n' + shared
for path, content in zip(paths, (server, ui)):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as handle:
        handle.write(content)
print('Created .env.p6.school and .env.p6.school-ui; token not displayed.')
PY
scp .env.p6.school "$P6_SCHOOL_SSH:$P6_SCHOOL_REPO/.env.p6.school"
```

The GPU file selects model/backend and GPU-side paths; the Mac UI file selects
the tunnel URL and authentication. The Mac's normal sample/catalog/record paths
are inherited from the defaults. `P5_RECORDS_PATH` is optional for Free question
and required only for Demo record. Future template references remain in
`configs/p6-school.env.example` and `configs/p6-school-ui.env.example`.

### 2.4 Start the complete API inside a Slurm GPU allocation

On the school login host, set the same paths and your approved scheduler values:

```bash
export P6_SCHOOL_REPO='/absolute/path/to/existing/papergap-rag'
export P6_SCHOOL_VENV='/absolute/path/to/approved/vllm-venv'
export P6_SLURM_ACCOUNT='YOUR_APPROVED_ACCOUNT'
export P6_SLURM_PARTITION='YOUR_APPROVED_GPU_PARTITION'
cd "$P6_SCHOOL_REPO"
chmod 600 .env.p6.school
mkdir -p logs results/p6-school
cat > results/p6-school/serve.sbatch <<'SBATCH'
#!/usr/bin/env bash
#SBATCH --job-name=p6-demo
#SBATCH --output=logs/p6-demo-%j.out
#SBATCH --time=06:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1
set -euo pipefail
cd "$P6_SCHOOL_REPO"
# If P5's environment requires a site module, load that confirmed module here.
nvidia-smi
"$P6_SCHOOL_VENV/bin/python" -c 'import vllm, transformers, torch, faiss, sentence_transformers, rank_bm25, langgraph, dotenv, fastapi, uvicorn; print("Runtime imports OK; vLLM", vllm.__version__, "transformers", transformers.__version__)'
export P6_CONFIG_FILE="$P6_SCHOOL_REPO/.env.p6.school"
exec "$P6_SCHOOL_VENV/bin/python" -u -m scripts.p6_local serve
SBATCH
sbatch --export=ALL --account="$P6_SLURM_ACCOUNT" \
  --partition="$P6_SLURM_PARTITION" results/p6-school/serve.sbatch
squeue --me
```

Use the site's approved resource/time limits. Omit `--account` or `--partition`
only if your allocation uses a confirmed scheduler default. If the environment
requires a module (for example the one specified by P5), add its confirmed
`module load ...` before the Python calls. The import check diagnoses missing
retrieval/API dependencies; it does not install or change pinned packages.
Resolve environment compatibility with P5 before resubmitting.

Record the numeric job ID printed by `sbatch`. Watch its log (replace `123456`):

```bash
P6_JOB_ID=123456
squeue --jobs="$P6_JOB_ID" --format='%.18i %.9T %.20N'
tail -f "logs/p6-demo-$P6_JOB_ID.out"
```

Wait for `RUNNING`, successful model/index initialization and Uvicorn listening
on `0.0.0.0:18080`. This job does not print the original script's `READY TO TUNNEL`
marker. Loading a checkpoint is not instantaneous. Never run this server on a
login node. The original `80_demo_server.sbatch` invokes a different P5 entry
point; changing `P6_BACKEND` in its shell does not enable this runtime's corpus
search/adaptive-agent hook. Use the job above for the full P6 pipeline.

### 2.5 Connect the Mac UI through the tunnel

First stop the local `start` launcher with Ctrl+C so ports 8000/8501 are free.
In **Mac terminal A**, use your actual school login and running job ID:

```bash
export P6_SCHOOL_SSH='YOUR_USER@YOUR_LOGIN_HOST'
P6_JOB_ID=123456
P6_COMPUTE_NODE="$(ssh "$P6_SCHOOL_SSH" "squeue --jobs=$P6_JOB_ID --noheader --format=%N")"
printf 'Tunnel target: %s\n' "$P6_COMPUTE_NODE"
ssh -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 \
  -L "127.0.0.1:8000:$P6_COMPUTE_NODE:18080" "$P6_SCHOOL_SSH"
```

Use a single actual node, not an empty/pending `squeue` result. This route requires
login-host TCP forwarding to the compute node; confirm the account/site permits
it. The GPU API binds a network address, so the private bearer token is required.
The Mac endpoint remains loopback-only. Keep terminal A running.

In **Mac terminal B**, start only Streamlit, not another local API:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
curl --fail --silent --show-error http://127.0.0.1:8000/health
P6_CONFIG_FILE=.env.p6.school-ui ./scripts/p6-local.sh config
P6_CONFIG_FILE=.env.p6.school-ui ./scripts/p6-local.sh remote
```

Open [the same UI](http://127.0.0.1:8501). `/health` must now report backend
`vllm`, the **school checkpoint** as `model_id`, and `retrieval`, `passage_text`,
`corpus_search`, `agent` all `true`. If it still says `ollama`, you reached the
old local API. If `agent`/`corpus_search` is false or absent, check the server
entry point/configuration. The `remote` launcher checks health but does not
validate those expected values for you.

Use Browse all examples and Ask question as below. A 401 means mismatched token;
429 means another request is running. Inspect generation/validation/agent details
and citations, not HTTP 200 alone. The school model/path is shown in Connection;
Refresh service cannot change backends because config/model changes need restart.

### 2.6 Stop the school demo and return to local Ollama

1. Ctrl+C in Mac terminal B (UI), then terminal A (tunnel).
2. On the school host, cancel only the recorded job: `scancel 123456` (substitute
   your actual job ID). Ctrl+C on `tail -f` alone does **not** stop the GPU job.
3. On the Mac:

```bash
cd '/Users/changyanxu/Documents/NTU/AI6127 - DNN NLP/Project/papergap-rag'
unset P6_CONFIG_FILE
./scripts/p6-local.sh config
./scripts/p6-local.sh start
```

This uses the local defaults and any `.env.p6.local` override again. Confirm
`P6_BACKEND=ollama`, `P6_MODEL=qwen3:14b` in config and `ollama` in `/health`.
No change to committed defaults is needed; private school configs can stay for
next time. Export useful UI history before stopping either deployment.


## 3. Use the UI for the demo

1. The drawer shows **PaperRAG** and **How to use** above
   Connection. Keep Search scope **All papers** (local corpus-capable API) or
   optionally choose **One paper** by title/ID. The main heading changes from
   **Ask the paper collection** to **Ask Paper** followed by the quoted paper
   title. Legacy services require one paper.
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

## 4. Confirmed contract and interface-change requirements

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

## 5. Verification and remaining E2E

The commands in this handoff were checked against the current launcher and
backend code on 2026-11-03. All documented Bash blocks, the generated Slurm script and
embedded Python passed syntax checks. The private-config generator was exercised
in a temporary directory: matching token, expected backend/paths, file mode 0600
and refusal to overwrite existing configs passed. The record-only UI template was also checked against the configuration loader.
No school job, transfer or model server was started by these documentation checks.

Historical port evidence: the actual P5 mock API with Bearer auth and synthetic state passed the P6 running-
service UI smoke separately. Post-rebase combined tests: 100 passed, 1 default
opt-in skip. See the completion summary for exact commands and non-additive counts.

For the prepared local service, use this opt-in check from the Mac repository root:

```bash
.venv-p6/bin/python - <<'PYTEST'
import os
import pytest
from scripts.p6_local import configure
configure()
os.environ['P5_RUN_SMOKE'] = '1'
raise SystemExit(pytest.main(['-q', 'tests/test_ui_p5_smoke.py::test_actual_p5_service']))
PYTEST
```

For the tunneled school API, prefix that Python command with
`P6_CONFIG_FILE=.env.p6.school-ui` so URL/auth come from the private school config.
The check makes **two sequential answer calls** and validates
shape/rendering/citations, not semantic quality or successful model inference.
When not opted in it is skipped intentionally; the server code is not missing.

| Remaining school GPU check | Owner / status | Required evidence |
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
