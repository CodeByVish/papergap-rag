#!/usr/bin/env bash
#
# Step 8 - the Option-C demo service: FastAPI around answer_record, one A40.
#
# Decision of 2026-10-29: the demo runs LIVE on the cluster, with the UI on the
# laptop talking to this server through an SSH tunnel. Option A+ (precompute the
# pool, replay the JSONL) is the fallback, not the plan.
#
#   laptop UI  --ssh -L-->  login node  --direct-tcpip-->  compute node:8000
#
# This job is a *server*, so unlike 40/50/60/70 it does not exit - it holds the
# GPU for its whole wall-clock window. Consequences, all deliberate:
#
#   * the port opens only AFTER the weights load and one warm-up answer runs,
#     because a server that looks broken for its first 90 seconds is exactly
#     when nobody can debug it;
#   * the server binds 127.0.0.1 on the compute node - the tunnel is the only
#     path in, and nothing on the node's LAN can reach it;
#   * the log prints the tunnel command for the node it actually landed on, the
#     job's end time, and a 30-minute warning, because "the demo died silently
#     at hour 6" is the failure this design is known to have.
#
#   # on the login node, after step 3 (venv) and step 2 (weights):
#   sbatch scripts/cluster/80_demo_server.sbatch
#   squeue --me
#   tail -f logs/p5-demo-<jobid>.out        # wait for "READY TO TUNNEL"
#
#   # optional knobs:
#   sbatch --export=ALL,DEMO_PORT=8000 scripts/cluster/80_demo_server.sbatch
#   sbatch --export=ALL,DEMO_RETRIEVER='src.retrieval.demo:make_retriever' ...
#   sbatch --export=ALL,DEMO_RECORD_FN='src.agent.demo:make_record_fn' ...
#   sbatch --export=ALL,DEMO_INSTALL_DEPS=1 ...   # pip install fastapi/uvicorn
#
# DEMO_RETRIEVER and DEMO_RECORD_FN are mutually exclusive. The first wraps
# plain retrieval hits into a one-round record; the second runs P4's agent loop
# (retrieval + critic) and returns the pre-answer export, which the server then
# answers exactly once through answer_record.
#
# PRECONDITIONS this script cannot create:
#   * step 3 has run and exited 0            (vllm==0.11.0 venv)
#   * $P5_ROOT/models/Qwen3-8B exists         (step 2)
#   * fastapi + uvicorn in that venv          (DEMO_INSTALL_DEPS=1 installs them)
#
# THIS SCRIPT INSTALLS NOTHING BY DEFAULT. The vLLM environment is a triple pin
# (python312, vllm==0.11.0, transformers<5); see 30_vllm.sbatch. fastapi and
# uvicorn are pure-Python and cannot move torch or transformers, which is why
# the opt-in install below is safe - it is opt-in so the pin stays auditable.
#
#SBATCH --job-name=p5-demo
#SBATCH --output=logs/p5-demo-%j.out
#SBATCH --time=06:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1

set -euo pipefail

P5_ROOT="${P5_ROOT:-$HOME/p5}"
export HF_HOME="$P5_ROOT/hf"

MODEL_DIR="$P5_ROOT/models/Qwen3-8B"
DEMO_PORT="${DEMO_PORT:-8000}"
# Loopback by default: the -J tunnel reaches the compute node's own 127.0.0.1.
# Set DEMO_HOST=0.0.0.0 only for the single-hop fallback below, where the
# LOGIN NODE talks to this port directly because compute-node SSH is blocked.
DEMO_HOST="${DEMO_HOST:-127.0.0.1}"
# Required with DEMO_HOST=0.0.0.0: the port is then reachable from the cluster
# network, and /answer must not be open to it.
DEMO_TOKEN="${DEMO_TOKEN:-}"
DEMO_RECORD_FN="${DEMO_RECORD_FN:-}"
TOP_K="${TOP_K:-5}"
MAX_NEW_TOKENS="${MAX_NEW_TOKENS:-1024}"
SERVER_MODULE="${SERVER_MODULE:-}"
PAPERS_FROM="${PAPERS_FROM:-$P5_ROOT/data/corpus/passages.jsonl}"
# Two different files, deliberately separate variables:
#   PAPERS_FROM  - the corpus (or a retrieval dump); its paper_id values are
#                  used for GET /papers
#   PASSAGES_FROM - the corpus; passage_id -> text for POST /passages
PASSAGES_FROM="${PASSAGES_FROM:-$P5_ROOT/data/corpus/passages.jsonl}"

# Corpus/index paths for P4's record_fn factory. The factory reads these; the
# defaults are the layout proposed for P1's handoff. A missing file is a
# factory startup error, not silently ignored.
export PAPERGAP_CORPUS="${PAPERGAP_CORPUS:-$P5_ROOT/data/corpus/passages.jsonl}"
export PAPERGAP_DENSE_INDEX="${PAPERGAP_DENSE_INDEX:-$P5_ROOT/data/indexes/dense-bge-small}"
export PAPERGAP_BM25_INDEX="${PAPERGAP_BM25_INDEX:-$P5_ROOT/data/indexes/bm25}"

# Keep the old single-file layout working during the transition.
if [ ! -f "$PAPERS_FROM" ] && [ -f "$P5_ROOT/data/p1_hybrid.jsonl" ]; then
    PAPERS_FROM="$P5_ROOT/data/p1_hybrid.jsonl"
fi
if [ ! -f "$PASSAGES_FROM" ] && [ -f "$P5_ROOT/data/passages.jsonl" ]; then
    PASSAGES_FROM="$P5_ROOT/data/passages.jsonl"
fi

cd "${SLURM_SUBMIT_DIR:-$PWD}" || exit 1

# One script, two checkouts: the standalone P5 repo keeps the package under
# src/ (nlp_p5.server), the shared repo keeps it at src/generation
# (src.generation.server). Detect instead of hard-coding, so the same file works
# in both, and so an accidental cross-checkout import still fails loudly.
if [ -z "$SERVER_MODULE" ]; then
    if [ -f "src/generation/server.py" ]; then
        SERVER_MODULE="src.generation.server"
    elif [ -f "src/nlp_p5/server.py" ]; then
        SERVER_MODULE="nlp_p5.server"
    else
        echo "cannot find src/generation/server.py or src/nlp_p5/server.py in $PWD" >&2
        exit 1
    fi
fi

# Set PYTHONPATH to match the module's root rather than exporting both roots, so
# an accidental cross-checkout import fails instead of loading the other copy.
case "$SERVER_MODULE" in
    src.*) export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}" ;;
    *)     export PYTHONPATH="$PWD/src${PYTHONPATH:+:$PYTHONPATH}" ;;
esac

JOB_ID="${SLURM_JOB_ID:-manual}"

section() {
    printf '\n'
    printf '=%.0s' {1..72}
    printf '\n%s\n' "$1"
    printf '=%.0s' {1..72}
    printf '\n'
}

FAILED_PRECONDITION=""

section "JOB"
echo "job       : $JOB_ID on ${SLURMD_NODENAME:-<unset>} (${SLURM_JOB_PARTITION:-<unset>})"
echo "started   : $(date -Is)"
echo "repo      : $PWD"
echo "P5_ROOT   : $P5_ROOT"
echo "module    : $SERVER_MODULE"
if [ "$DEMO_HOST" = "127.0.0.1" ]; then
    echo "bind      : $DEMO_HOST:$DEMO_PORT (loopback; reach it through a -J tunnel)"
else
    echo "bind      : $DEMO_HOST:$DEMO_PORT (NETWORK-REACHABLE; token required)"
fi
echo "token     : $([ -n "$DEMO_TOKEN" ] && echo 'required' || echo 'not set')"
echo "retriever : ${DEMO_RETRIEVER:-<none>}"
echo "agent     : ${DEMO_RECORD_FN:-<none>}"

section "PRECONDITION 1/4 - GPU present"
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>&1 || true
else
    echo "nvidia-smi missing - this job did not land on a GPU node."
    FAILED_PRECONDITION="no GPU on this node"
fi

section "PRECONDITION 2/4 - weights"
if [ -f "$MODEL_DIR/config.json" ]; then
    du -sh "$MODEL_DIR" 2>/dev/null || true
else
    echo "MISSING: $MODEL_DIR/config.json"
    echo "Run step 2 first:  sbatch scripts/cluster/20_load_qwen3.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }weights missing"
fi

section "PRECONDITION 3/4 - vLLM venv"
VLLM_PY=""
for candidate in ${VLLM_VENV:-} "$P5_ROOT"/vllm-venv-* "$P5_ROOT/vllm-venv"; do
    [ -x "$candidate/bin/python" ] || continue
    if "$candidate/bin/python" -c 'import vllm, transformers; import sys; sys.exit(0 if transformers.__version__.split(".")[0] == "4" else 1)' 2>/dev/null; then
        VLLM_PY="$candidate/bin/python"
        break
    fi
done
if [ -n "$VLLM_PY" ]; then
    echo "using $VLLM_PY"
    "$VLLM_PY" -c 'import vllm, transformers; print("vllm", vllm.__version__, "| transformers", transformers.__version__)' || true
else
    echo "No venv imports vLLM with transformers 4.x."
    echo "Run step 3 first:  sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }no working vLLM venv"
fi

section "PRECONDITION 4/4 - fastapi + uvicorn"
if [ -n "$VLLM_PY" ]; then
    if "$VLLM_PY" -c 'import fastapi, uvicorn' 2>/dev/null; then
        "$VLLM_PY" -c 'import fastapi, uvicorn; print("fastapi", fastapi.__version__, "| uvicorn", uvicorn.__version__)'
    elif [ "${DEMO_INSTALL_DEPS:-0}" = "1" ]; then
        echo "installing fastapi + uvicorn into the vLLM venv (pure Python;"
        echo "torch and transformers are not touched)"
        "$VLLM_PY" -m pip install --progress-bar off "fastapi>=0.110" "uvicorn>=0.29"
        "$VLLM_PY" -c 'import fastapi, uvicorn; print("fastapi", fastapi.__version__, "| uvicorn", uvicorn.__version__)'
    else
        echo "fastapi/uvicorn are missing from the vLLM venv."
        echo "Either resubmit with DEMO_INSTALL_DEPS=1, or install once by hand:"
        echo "    \"$VLLM_PY\" -m pip install \"fastapi>=0.110\" \"uvicorn>=0.29\""
        FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }fastapi/uvicorn missing"
    fi
fi

if [ -n "$FAILED_PRECONDITION" ]; then
    section "STOPPING EARLY"
    echo "Unmet precondition(s): $FAILED_PRECONDITION"
    exit 1
fi

if [ "$DEMO_HOST" != "127.0.0.1" ] && [ -z "$DEMO_TOKEN" ]; then
    section "STOPPING: network-reachable but no token"
    echo "DEMO_HOST=$DEMO_HOST makes /answer reachable from the cluster network."
    echo "Set DEMO_TOKEN=<something> (the UI sends it as a bearer token),"
    echo "or leave DEMO_HOST at its loopback default."
    exit 1
fi

if [ -n "${DEMO_RETRIEVER:-}" ] && [ -n "$DEMO_RECORD_FN" ]; then
    section "STOPPING: two free-form hooks"
    echo "DEMO_RETRIEVER and DEMO_RECORD_FN are mutually exclusive."
    echo "Use DEMO_RECORD_FN for the agent loop; it runs retrieval itself."
    exit 1
fi

NODE_NAME="$(hostname -s)"
END_TIME="$(scontrol show job "$JOB_ID" 2>/dev/null | sed -n 's/.*EndTime=\([^ ]*\).*/\1/p' || true)"
END_TIME="${END_TIME:-unknown}"

section "SERVE"
if [ "$DEMO_HOST" = "127.0.0.1" ]; then
    TUNNEL_HINT="ssh -N -L ${DEMO_PORT}:localhost:${DEMO_PORT} -J <user>@<login-host> <user>@${NODE_NAME}"
    TUNNEL_NOTE="  # if ProxyJump is not permitted, two hops:
  ssh -N -L 2222:${NODE_NAME}:22 <user>@<login-host> &
  ssh -N -L ${DEMO_PORT}:localhost:${DEMO_PORT} -p 2222 <user>@localhost"
    CURL_URL="http://127.0.0.1:${DEMO_PORT}"
else
    TUNNEL_HINT="ssh -N -L 8000:${NODE_NAME}:${DEMO_PORT} <user>@<login-host>"
    TUNNEL_NOTE="  # single hop: the login node connects to ${NODE_NAME}:${DEMO_PORT} itself,
  # so no SSH session to the compute node is opened at all."
    CURL_URL="http://127.0.0.1:8000"
fi

cat <<EOF
The server listens only after the weights load and one warm-up answer runs.
Watch for "READY TO TUNNEL" below, then open a tunnel FROM THE LAPTOP:

  ${TUNNEL_HINT}

${TUNNEL_NOTE}

  # then, on the laptop:
  curl -s ${CURL_URL}/health

Job end time: ${END_TIME}   (the 6-hour limit kills this service)
EOF

# Warn before the wall clock does something surprising.
(
    sleep 19800  # 5 h 30 min
    echo "[warn] 30 minutes of wall clock left; the demo will stop at ${END_TIME}"
    sleep 900    # 5 h 45 min
    echo "[warn] 15 minutes left. Resubmit and re-tunnel now, or switch to the A+ replay fallback."
) &

# Print READY only once the port actually accepts a connection, so the operator
# never has to guess whether the model finished loading. The probe always uses
# 127.0.0.1: with DEMO_HOST=0.0.0.0 the bind address is not itself a destination.
(
    for _ in $(seq 1 120); do
        if (exec 3<>/dev/tcp/127.0.0.1/${DEMO_PORT}) 2>/dev/null; then
            exec 3>&- 3<&-
            echo
            echo "READY TO TUNNEL - job ${JOB_ID} on ${NODE_NAME}, port ${DEMO_PORT}"
            echo "  ${TUNNEL_HINT}"
            echo "  curl -s ${CURL_URL}/health"
            break
        fi
        sleep 5
    done
) &

ARGS=(
    --backend vllm
    --model "$MODEL_DIR"
    --host "$DEMO_HOST"
    --port "$DEMO_PORT"
    --top-k "$TOP_K"
    --max-new-tokens "$MAX_NEW_TOKENS"
    --log-level info
)
if [ -n "${DEMO_RETRIEVER:-}" ]; then
    ARGS+=(--retriever "$DEMO_RETRIEVER")
fi
if [ -n "$DEMO_RECORD_FN" ]; then
    ARGS+=(--record-fn "$DEMO_RECORD_FN")
fi
if [ -f "$PAPERS_FROM" ]; then
    ARGS+=(--papers-from "$PAPERS_FROM")
    echo "paper list: $PAPERS_FROM"
else
    echo "paper list: none ($PAPERS_FROM missing); GET /papers will be empty"
fi
if [ -f "$PASSAGES_FROM" ]; then
    ARGS+=(--passages-from "$PASSAGES_FROM")
    echo "passage text: $PASSAGES_FROM (POST /passages enabled)"
else
    echo "passage text: none ($PASSAGES_FROM missing); citations resolve as ids only"
fi
if [ -n "${DEMO_WARMUP_RECORD:-}" ] && [ -f "$DEMO_WARMUP_RECORD" ]; then
    ARGS+=(--warmup-record "$DEMO_WARMUP_RECORD")
fi
if [ -n "$DEMO_TOKEN" ]; then
    ARGS+=(--token "$DEMO_TOKEN")
fi

# exec so uvicorn is PID 1's replacement: SLURM's 6-hour SIGTERM reaches the
# server directly instead of a wrapper shell that ignores it.
exec "$VLLM_PY" -u -m "$SERVER_MODULE" "${ARGS[@]}"
