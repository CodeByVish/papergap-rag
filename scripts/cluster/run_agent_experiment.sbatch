#!/usr/bin/env bash
#
# P4 agent experiment on the cluster: static and adaptive arms over real retrieval,
# the Qwen3-8B critic and P5's answer step, all sharing ONE in-process vLLM engine.
#
#   sbatch scripts/cluster/run_agent_experiment.sbatch
#
# Everything is configured through environment variables; override with --export:
#
#   sbatch --export=ALL,ITEMS=$HOME/p4/items.jsonl,OUT_DIR=runs/p4/held-out-001 \
#       scripts/cluster/run_agent_experiment.sbatch
#
# A killed or timed-out job continues where it stopped (records are written one
# by one):  sbatch --export=ALL,OUT_DIR=<same dir>,RESUME=1 ...
#
# THIS SCRIPT INSTALLS NOTHING AND MODIFIES NO VENV, like P5's scripts. P5's vLLM
# environment is a triple pin (python312, vllm==0.11.0, transformers<5). The agent
# also needs faiss-cpu, sentence-transformers, rank-bm25 and langgraph in whichever
# environment runs this. The preflight below names anything missing; adding it is
# your decision, ideally in a copy of the environment.
#
# PRECONDITIONS this script cannot create:
#   * PASSAGES and DENSE_INDEX exist (python -m scripts.build_corpus / build_indexes)
#   * the repo checkout contains P5's src/generation (on main)
#   * Qwen3-8B weights are at MODEL_DIR
#
#SBATCH --job-name=p4-agent
#SBATCH --output=logs/p4-agent-%j.out
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1

set -uo pipefail

P5_ROOT="${P5_ROOT:-$HOME/p5}"
export HF_HOME="${HF_HOME:-$P5_ROOT/hf}"

VENV="${VENV:-${VLLM_VENV:-}}"                    # environment with vllm + the agent deps
MODEL_DIR="${MODEL_DIR:-$P5_ROOT/models/Qwen3-8B}"
PASSAGES="${PASSAGES:-data/processed/passages.jsonl}"
DENSE_INDEX="${DENSE_INDEX:-indexes/p2-qasper-development}"
OUT_DIR="${OUT_DIR:-runs/p4/${SLURM_JOB_ID:-manual}}"

# Questions: a JSONL of items (preferred for the held-out set) or development
# questions drawn from qa.jsonl. The test split is refused by the script.
ITEMS="${ITEMS:-}"
QA="${QA:-data/processed/qa.jsonl}"
SPLIT="${SPLIT:-validation}"
LIMIT="${LIMIT:-100}"

ARMS="${ARMS:-static adaptive}"
CRITIC="${CRITIC:-generator}"                     # generator | rules
ANSWERS="${ANSWERS:-p5}"                          # p5 | none
SCOPED="${SCOPED:-0}"                             # 1 = per-paper section-scoped retries
BGE="${BGE:-0}"                                   # 1 = BGE reranker (slower, CPU)
SCORE_CACHE="${SCORE_CACHE:-}"                    # fresh path for cold latency numbers
RESUME="${RESUME:-0}"
OFFLINE="${OFFLINE:-0}"                           # 1 = never touch the network (BGE-small must be cached)

cd "${SLURM_SUBMIT_DIR:-$PWD}" || exit 1
mkdir -p logs

section() { printf '\n%s\n%s\n' "$1" "----------------------------------------"; }

section "JOB"
echo "job       : ${SLURM_JOB_ID:-manual} on ${SLURMD_NODENAME:-<unset>}"
echo "started   : $(date -Is)"
echo "repo      : $PWD ($(git rev-parse --short HEAD 2>/dev/null || echo no-git))"
echo "out dir   : $OUT_DIR  (resume=$RESUME)"
echo "arms      : $ARMS   critic=$CRITIC   answers=$ANSWERS   scoped=$SCOPED   bge=$BGE"

FAILED=""
fail() { echo "PRECONDITION FAILED: $1"; FAILED="${FAILED:+$FAILED; }$1"; }

section "PRECONDITIONS"
if [ -n "$VENV" ] && [ -f "$VENV/bin/activate" ]; then
    # shellcheck disable=SC1091
    source "$VENV/bin/activate"
    echo "venv      : $VENV"
else
    fail "VENV (or VLLM_VENV) is not set to an environment with bin/activate"
fi
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,memory.used,memory.total --format=csv,noheader
else
    fail "no GPU on this node"
fi
[ -f "$PASSAGES" ] || fail "PASSAGES not found: $PASSAGES"
[ -d "$DENSE_INDEX" ] || fail "DENSE_INDEX not found: $DENSE_INDEX"
[ -d "$MODEL_DIR" ] || fail "MODEL_DIR not found: $MODEL_DIR"
if [ -n "$ITEMS" ]; then
    [ -f "$ITEMS" ] && echo "items     : $ITEMS ($(wc -l < "$ITEMS") lines, sha256 $(sha256sum "$ITEMS" | cut -c1-16))" \
        || fail "ITEMS not found: $ITEMS"
else
    [ -f "$QA" ] || fail "QA not found: $QA"
    echo "items     : $LIMIT $SPLIT questions from $QA"
fi
if [ -d "$OUT_DIR" ] && [ -n "$(ls -A "$OUT_DIR" 2>/dev/null)" ] && [ "$RESUME" != "1" ]; then
    fail "OUT_DIR is not empty; choose a new one or pass RESUME=1"
fi
if [ -z "$FAILED" ]; then
    python - <<'PY' || fail "python imports (see above)"
import importlib, sys
need = ["vllm", "torch", "faiss", "sentence_transformers", "rank_bm25", "langgraph", "pydantic"]
missing = [m for m in need if importlib.util.find_spec(m) is None]
try:
    import src.generation  # noqa: F401  (P5, on main)
except Exception as error:
    missing.append(f"src.generation ({error})")
if missing:
    print("missing:", ", ".join(missing))
    sys.exit(1)
print("imports   : ok")
PY
fi
if [ -n "$FAILED" ]; then
    echo; echo "Not starting: $FAILED"
    exit 2
fi

section "RUN"
ARGS=(--passages "$PASSAGES" --dense-index-dir "$DENSE_INDEX" --out-dir "$OUT_DIR"
      --arms $ARMS --critic "$CRITIC" --answers "$ANSWERS"
      --generator vllm --model-id "$MODEL_DIR" --cache-folder "$HF_HOME/hub")
if [ "$OFFLINE" = "1" ]; then
    ARGS+=(--local-files-only)
    export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
fi
if [ -n "$ITEMS" ]; then ARGS+=(--items "$ITEMS"); else ARGS+=(--from-qa "$QA" --split "$SPLIT" --limit "$LIMIT"); fi
[ "$SCOPED" = "1" ] && ARGS+=(--scoped)
[ "$BGE" = "1" ] && ARGS+=(--bge)
[ -n "$SCORE_CACHE" ] && ARGS+=(--score-cache "$SCORE_CACHE")
[ "$RESUME" = "1" ] && ARGS+=(--resume)

python -m scripts.run_agent_experiment "${ARGS[@]}"
STATUS=$?

section "DONE"
echo "exit      : $STATUS"
echo "finished  : $(date -Is)"
echo "outputs   : $OUT_DIR  (static.jsonl adaptive.jsonl metrics.md metrics.json run_manifest.json)"
echo "inspect   : critic replies are in adaptive.jsonl -> critic_log[*].raw_replies"
exit "$STATUS"
