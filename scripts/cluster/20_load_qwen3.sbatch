#!/usr/bin/env bash
#
# Step 2 — actually load Qwen3-8B on the A40 and answer one grounded question.
#
# This is the "verify Qwen3-8B loads" step: it creates a Python environment,
# fetches the weights, loads them in bf16, and runs the end-to-end smoke test
# from scripts/smoke_test_qwen3.py.
#
#   mkdir -p logs
#   sbatch scripts/cluster/20_load_qwen3.sbatch
#
# Anything P5_ROOT / MODEL_ID / TORCH_INDEX below can be overridden without
# editing the file, which is what the variables at the top are for:
#
#   sbatch --export=ALL,P5_ROOT=/scratch/junyu007/p5 scripts/cluster/20_load_qwen3.sbatch
#
# WHY THIS IS ONE SCRIPT AND NOT THREE. The unknowns here — is there internet on
# a compute node, is there disk for 17 GB of weights, does py3.9 have a working
# venv — each cost about a minute to answer but hours to discover the hard way.
# So every one of them is checked in the first ~30 seconds and reported, and the
# expensive parts (the pip install, the 17 GB download) only run once the cheap
# preconditions have passed. A job that cannot succeed fails in two minutes.
#
# The 6-hour wall clock is why the download is resumable and cached: HF_HOME is
# set to a persistent path, so a second submission re-uses whatever the first
# one managed to fetch instead of starting from zero.
#
#SBATCH --job-name=p5-load-qwen3
#SBATCH --output=logs/p5-load-qwen3-%j.out
# Deliberately NO --error directive. When --error is absent SLURM merges stderr
# into the --output file; when it is present, a Python traceback lands in a file
# this script never prints, and the job "fails silently". One file, everything
# in it. This is not hypothetical: the first run of this script died on a
# missing import and the .out file showed an empty smoke-test section, which
# looked like the script had skipped a step rather than like Python had crashed.
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1

set -uo pipefail

# ---------------------------------------------------------------------------
# Configuration. Override via `sbatch --export=ALL,VAR=value ...`.
# ---------------------------------------------------------------------------

# Everything P5 downloads lives under one root, so that "delete the cluster
# experiment" is a single `rm -rf`. It is ~22 GiB in total: ~5 GiB of venv plus
# ~17 GiB of weights. Check `df -h "$P5_ROOT"` below before committing to it.
P5_ROOT="${P5_ROOT:-$HOME/p5}"

VENV_DIR="$P5_ROOT/venv"
export HF_HOME="$P5_ROOT/hf"

MODEL_ID="Qwen/Qwen3-8B"
MODEL_DIR="$P5_ROOT/models/Qwen3-8B"

# Measured on TC2N02: driver 570.148.08, CUDA 12.8, A40, compute cap 8.6.
# cu126 is the safe choice — a 12.8 driver runs 12.6 wheels fine, and cu126 has
# py3.9 wheels for every torch from 2.6 up. Do NOT copy the cu124 URL from
# docs/GPU_FEASIBILITY.md; that predates this measurement.
TORCH_INDEX="https://download.pytorch.org/whl/cu126"

MAX_NEW_TOKENS=768

# ---------------------------------------------------------------------------

cd "${SLURM_SUBMIT_DIR:-$PWD}" || exit 1

section() {
    printf '\n'
    printf '=%.0s' {1..72}
    printf '\n%s\n' "$1"
    printf '=%.0s' {1..72}
    printf '\n'
}

FAILED_PRECONDITION=""

section "JOB AND ENVIRONMENT"
echo "job      : ${SLURM_JOB_ID:-<unset>} on ${SLURMD_NODENAME:-<unset>} (${SLURM_JOB_PARTITION:-<unset>})"
echo "started  : $(date -Is)"
echo "repo     : $PWD"
echo "P5_ROOT  : $P5_ROOT"
echo "HF_HOME  : $HF_HOME"
echo

section "PRECONDITION 1/4 — is this really a GPU node?"
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,memory.total,compute_cap --format=csv,noheader 2>&1 || true
    CAP=$(nvidia-smi --query-gpu=compute_cap --format=csv,noheader 2>/dev/null | head -1 | tr -d ' ')
    echo
    echo "compute capability: ${CAP:-unknown}  (bf16 needs >= 8.0)"
else
    echo "nvidia-smi missing — this job did not land on a GPU node."
    FAILED_PRECONDITION="no GPU on this node"
fi

section "PRECONDITION 2/4 — can a compute node reach the internet?"
# This is the assumption most likely to be wrong on a university cluster, and the
# one that costs the most to discover late: without it, a 17 GB download cannot
# start. Checked with python rather than curl so that it works even where curl
# is not installed.
NET_STATUS=$("${PY:-python3}" - <<'PYEOF' 2>/dev/null || echo "unavailable"
import urllib.request
for url in ("https://huggingface.co", "https://download.pytorch.org"):
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            print(f"  {url} -> HTTP {r.status}")
    except Exception as exc:
        print(f"  {url} -> FAILED ({type(exc).__name__}: {exc})")
PYEOF
)
echo "$NET_STATUS"
if echo "$NET_STATUS" | grep -q "FAILED"; then
    echo
    echo "One or more hosts are unreachable from this compute node."
    echo "If huggingface.co is the failure and the weights are not already at"
    echo "  $MODEL_DIR"
    echo "then this job cannot proceed. Fix, in order of preference:"
    echo "  1. Download on the LOGIN node instead (it usually has internet), then"
    echo "     resubmit pointing at the local path:"
    echo "       P5_ROOT=$P5_ROOT python3 -c 'from huggingface_hub import snapshot_download; \\"
    echo "         snapshot_download(\"$MODEL_ID\", local_dir=\"$MODEL_DIR\")'"
    echo "  2. Set a proxy: sbatch --export=ALL,HTTPS_PROXY=... "
    echo "  3. Ask the HPC admin whether compute nodes have outbound access."
fi

section "PRECONDITION 3/4 — is there disk for ~22 GiB?"
echo "-- $P5_ROOT --"
if [ -d "$P5_ROOT" ]; then
    df -h "$P5_ROOT" 2>&1 | tail -2
else
    echo "(does not exist yet; will be created)"
    df -h "$HOME" 2>&1 | tail -2
fi
echo
echo "-- home quota, if enforced --"
command -v quota >/dev/null 2>&1 && quota -s 2>&1 | head -10 || echo "(quota command unavailable)"
echo
FREE_GIB=$(df -BG "${P5_ROOT%/*}" 2>/dev/null | awk 'NR==2 {gsub("G","",$4); print $4}')
if [ -n "${FREE_GIB:-}" ] && [ "$FREE_GIB" -lt 40 ] 2>/dev/null; then
    echo "WARNING: only ${FREE_GIB} GiB free where P5_ROOT points. The venv and the"
    echo "weights together need roughly 22 GiB, and HF keeps incomplete downloads"
    echo "as well. Point P5_ROOT at a larger filesystem if one exists:"
    echo "  sbatch --export=ALL,P5_ROOT=/scratch/$USER/p5 scripts/cluster/20_load_qwen3.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }not enough disk"
fi

section "PRECONDITION 4/4 — python, pip and venv"
PY=python3
command -v python3 >/dev/null 2>&1 || PY=python
echo "system interpreter : $(command -v "$PY" 2>/dev/null || echo none)"
"$PY" --version 2>&1 || true
echo

# A venv is required, not optional: $HOME is writable but system site-packages
# are not, and polluting the cluster's python with a 5 GiB torch is not a thing
# to do on a shared account. Note the py3.9 constraint — it caps which torch and
# especially which vLLM versions are installable, so it is printed here.
if [ -x "$VENV_DIR/bin/python" ]; then
    echo "reusing existing venv: $VENV_DIR"
    VENV_PY="$VENV_DIR/bin/python"
else
    echo "creating venv at $VENV_DIR"
    mkdir -p "$P5_ROOT" 2>/dev/null || true
    if "$PY" -m venv "$VENV_DIR" 2>&1; then
        VENV_PY="$VENV_DIR/bin/python"
        echo "venv created."
    else
        echo
        echo "FAILED to create a venv. On Rocky Linux this usually means the"
        echo "python3-venv / ensurepip package is absent, which needs root or a"
        echo "module. Try:  module avail python   then load a newer python and"
        echo "resubmit. Falling back to --user installs with the system python."
        VENV_PY="$PY"
        export PIP_USER=1
    fi
fi
echo "using interpreter: $VENV_PY"
echo

if [ -n "$FAILED_PRECONDITION" ]; then
    section "STOPPING EARLY"
    echo "Unmet precondition(s): $FAILED_PRECONDITION"
    echo "Nothing expensive was attempted. Fix the above and resubmit — the job"
    echo "cost two minutes, not two hours, which is the whole point of the checks."
    exit 1
fi

# ---------------------------------------------------------------------------
# Everything below only runs once the cheap checks have passed.
# ---------------------------------------------------------------------------

if ! "$VENV_PY" -c "import torch" >/dev/null 2>&1; then
    section "INSTALLING torch  (cu126 wheels, ~2.5 GiB — a few minutes)"
    # No `| tail` on the installs below. Piping into tail buffers everything
    # until the command exits, so a several-minute download leaves the log
    # completely silent - which reads as "hung" and invites killing a job that
    # is working. --progress-bar off drops the carriage-return noise while the
    # Collecting / Downloading / Installing lines keep streaming.
    "$VENV_PY" -m pip install --progress-bar off --upgrade pip 2>&1
    "$VENV_PY" -m pip install --progress-bar off torch --index-url "$TORCH_INDEX" 2>&1
fi

if ! "$VENV_PY" -c "import transformers" >/dev/null 2>&1; then
    section "INSTALLING transformers + accelerate"
    "$VENV_PY" -m pip install --progress-bar off "transformers>=4.51.0" \
        "accelerate>=0.30" "huggingface_hub[cli]" 2>&1
fi

# The GPU stack above is not the whole story: P5 has its own runtime dependency
# (pydantic, via schema.py) and a fresh venv has none of it. Omitting this step
# is what made the first run of this script die one second into the smoke test
# with an empty log. Read from requirements.txt rather than restated here, so
# the list cannot drift from what the project declares; the GPU extras in that
# file stay commented out on purpose, because torch and transformers were
# installed above from the CUDA wheel index rather than from PyPI.
if ! "$VENV_PY" -c "import pydantic" >/dev/null 2>&1; then
    section "INSTALLING the project's own runtime dependencies"
    "$VENV_PY" -m pip install --progress-bar off -r requirements.txt 2>&1
fi

section "TORCH SEES THE GPU?"
"$VENV_PY" - <<'PYEOF' 2>&1 || true
import torch
print(f"  torch          : {torch.__version__}")
print(f"  torch CUDA     : {torch.version.cuda}")
print(f"  cuda available : {torch.cuda.is_available()}")
if torch.cuda.is_available():
    p = torch.cuda.get_device_properties(0)
    free, total = torch.cuda.mem_get_info(0)
    print(f"  device         : {p.name}")
    print(f"  VRAM           : {free / 1024**3:.2f} free / {total / 1024**3:.2f} GiB total")
    print(f"  capability     : {p.major}.{p.minor}")
    print(f"  bf16 supported : {torch.cuda.is_bf16_supported()}")
PYEOF

if ! "$VENV_PY" -c "import torch; raise SystemExit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
    section "STOPPING: torch cannot see a CUDA device"
    echo "The most common cause is a wheel built against a CUDA version the"
    echo "driver is too old for. Observed driver: 570.148.08 (CUDA 12.8)."
    echo "Retry with a different wheel index:"
    echo "  sbatch --export=ALL,TORCH_INDEX=https://download.pytorch.org/whl/cu128 \\"
    echo "         scripts/cluster/20_load_qwen3.sbatch"
    exit 1
fi

if [ ! -f "$MODEL_DIR/config.json" ]; then
    section "DOWNLOADING $MODEL_ID  (~17 GiB, resumable)"
    echo "Target: $MODEL_DIR"
    echo "Starting at $(date -Is)"
    # ignore_patterns skips the 'original/' directory that some Qwen repos carry
    # as a duplicate copy of the weights in a different layout. Fetching it would
    # double both the download and the disk footprint for no benefit, because
    # transformers only ever reads the sharded safetensors.
    "$VENV_PY" - <<PYEOF 2>&1 || echo "download failed (see above)"
import os
from huggingface_hub import snapshot_download
path = snapshot_download(
    "$MODEL_ID",
    local_dir="$MODEL_DIR",
    ignore_patterns=["original/*", "*.pth", "*.gguf", "*.msgpack", "*.h5"],
)
print(f"snapshot at: {path}")
PYEOF
    echo "Finished at $(date -Is)"
fi

if [ ! -f "$MODEL_DIR/config.json" ]; then
    section "STOPPING: the weights are not present"
    echo "Expected $MODEL_DIR/config.json after the download step."
    echo "Resubmit the same command — HF_HOME and MODEL_DIR are on persistent"
    echo "storage, so an interrupted download resumes rather than restarting."
    exit 1
fi

section "MODEL FILES"
ls -1 "$MODEL_DIR"/*.safetensors 2>/dev/null | wc -l | xargs -I{} echo "  safetensors shards : {}"
du -sh "$MODEL_DIR" 2>/dev/null || true

section "PREFLIGHT — can the smoke test even import?"
# Loading 16 GiB of weights takes tens of seconds; failing on an import takes
# one. Distinguishing the two up front means a missing package reports itself by
# name instead of surfacing as a mystery exit code with no output.
PREFLIGHT=$("$VENV_PY" - <<'PYEOF' 2>&1
import sys
sys.path.insert(0, ".")
try:
    from src.generation.generators import get_generator        # noqa: F401
    from src.generation.pipeline import GroundedQAPipeline     # noqa: F401
    from src.generation.prompts.grounded_qa import build_prompt  # noqa: F401
    from src.generation.schema import GenerationRequest        # noqa: F401
except Exception as exc:
    print(f"IMPORT FAILED: {type(exc).__name__}: {exc}")
    raise SystemExit(1)
print("all imports resolve")
PYEOF
)
echo "$PREFLIGHT"
if echo "$PREFLIGHT" | grep -q "IMPORT FAILED"; then
    section "STOPPING: the environment is incomplete"
    echo "The smoke test would have died before printing anything, which is exactly"
    echo "the failure mode this check exists to turn into a readable message."
    exit 1
fi

section "SMOKE TEST  (load + one grounded question, end to end)"
echo "This is the actual answer to 'can Qwen3-8B run here'. It prints load time,"
echo "generation latency, and peak VRAM."
echo
# 2>&1 so an in-process traceback cannot hide in a file nobody reads.
"$VENV_PY" scripts/smoke_test_qwen3.py \
    --backend transformers \
    --model "$MODEL_DIR" \
    --max-new-tokens "$MAX_NEW_TOKENS" \
    --show-prompt 2>&1
SMOKE_EXIT=$?

section "RESULT"
echo "smoke test exit code : $SMOKE_EXIT"
echo "  0 = loaded, answered, passed validation   <- the target"
echo "  1 = could not load at all"
echo "  2 = loaded, but the answer was refused or downgraded (a prompt-tuning"
echo "      signal, not a crash — see docs/PROMPT_TEMPLATE.md)"
echo "finished : $(date -Is)"
echo
echo "Record these in docs/GPU_FEASIBILITY.md §2, replacing the estimates:"
echo "  load time, generation latency, peak VRAM (torch.cuda.max_memory_allocated)"
echo
echo "Environment for later jobs (reuse it, do not rebuild it):"
echo "  venv      : $VENV_DIR"
echo "  HF cache  : $HF_HOME"
echo "  weights   : $MODEL_DIR"
echo
echo "Next, once this exits 0: the vLLM path, which is the production backend."
echo "Install it into a SEPARATE venv — vLLM pins its own torch, and letting it"
echo "replace the torch this job just validated would throw away a known-good"
echo "configuration."

exit "$SMOKE_EXIT"
