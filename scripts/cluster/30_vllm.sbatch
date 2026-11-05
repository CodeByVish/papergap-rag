#!/usr/bin/env bash
#
# Step 3 — the production backend. Loads Qwen3-8B under vLLM and runs the same
# smoke test, which is the gate docs/GPU_FEASIBILITY.md §7 names for confirming
# the serving method.
#
#   sbatch scripts/cluster/30_vllm.sbatch
#
# WHY A SEPARATE VENV. vLLM pins its own torch, and often a different CUDA build
# than the cu126 wheels step 2 validated. Installing it into $P5_ROOT/venv would
# replace a torch that is known to work with the A40 and leave nothing to fall
# back to. Two venvs, ~6 GiB, and either one can be deleted without touching the
# other. This is the whole reason the step is separate rather than folded into
# 20_load_qwen3.sbatch.
#
# PRECONDITIONS, none of which this script can create for you:
#   * step 2 has run and exited 0 (weights at $P5_ROOT/models/Qwen3-8B)
#   * the partition/account are the ones measured on 2026-09-23
#
# The one number worth hunting for in the output is vLLM's own KV cache
# accounting, which is the measurement §2 of the feasibility note is waiting on:
#     GPU KV cache size: N tokens
#
#SBATCH --job-name=p5-vllm
#SBATCH --output=logs/p5-vllm-%j.out
# No --error directive, for the reason given in 20_load_qwen3.sbatch: a traceback
# in a file nobody tails is how a job appears to fail silently.
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1

set -uo pipefail

P5_ROOT="${P5_ROOT:-$HOME/p5}"
export HF_HOME="$P5_ROOT/hf"

# THREE independent constraints decide which vLLM can run here. The defaults
# below satisfy all three, and each was found the hard way on 2026-09-23:
#
#   1. INTERPRETER. vLLM dropped Python 3.9 in v0.11.1. On the system 3.9,
#      0.11.0 installs (its metadata still claims >=3.9) but dies at import with
#      "TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'" -
#      PEP 604 unions that 3.9 cannot evaluate at runtime. Hence python312.
#   2. DRIVER. This cluster runs driver 570 (CUDA 12.8). CUDA 13 wheels need
#      driver >= 580, and recent vLLM pulls exactly that (0.30.0 -> torch
#      2.13.0/cu13), failing with "The NVIDIA driver on your system is too old
#      (found version 12080)". So the pin must be a CUDA 12-era vLLM.
#   3. TRANSFORMERS. vLLM 0.11.x calls tokenizer.all_special_tokens_extended,
#      removed in transformers 5.x. Unbounded, pip picks 5.17.0 and vLLM loads
#      into "AttributeError: Qwen2Tokenizer has no attribute
#      all_special_tokens_extended". Hence the <5 cap below.
#
# The common thread: vLLM's declared ranges are open upwards, so on a cluster
# whose driver and interpreter lag the frontier, "install the newest" is the
# wrong strategy and a verified pin is the right one.
#
# Interpreter and vLLM spec below put the environment in a DIFFERENT venv (see
# VENV_DIR), so an environment built for one combination is never silently
# reused for another:
#
#   sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch
#   sbatch --export=ALL,PYTHON_MODULE=python312,VLLM_SPEC='vllm==0.10.2' ...
#
# To move to a newer vLLM, check what CUDA its torch targets first; anything on
# the CUDA 13 line is unusable until the cluster's driver moves past 580.
VLLM_SPEC="${VLLM_SPEC:-}"

#: Optional interpreter override. A `module load` typed on the login node does
#: NOT follow you into a batch job - the job gets a fresh environment - so the
#: module has to be loaded inside this script, which is what this parameter is
#: for:
#:
#:   sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch
#:
#: This is the durable fix for the py3.9 problem: with a 3.10+ interpreter the
#: vLLM pin stops mattering and the default resolves to a current release.
PYTHON_MODULE="${PYTHON_MODULE:-}"

#: Exact interpreter path, for when the versioned-binary probe below picks the
#: wrong one (a module that ships several pythons, say). Wins over
#: PYTHON_MODULE's PATH. Example:
#:   sbatch --export=ALL,PYTHON_BIN=/cm/local/apps/python312/bin/python3.12 ...
PYTHON_BIN="${PYTHON_BIN:-}"

# The default MUST be assigned before the branch below, not inside one arm of
# it. An earlier version of this script put it in the `if` arm only, so setting
# PYTHON_MODULE sent execution down the `else` and left VLLM_SPEC empty - and
# `pip install ""` installs nothing and exits 0, so the install step "succeeded"
# while putting no vLLM in the venv. The failure only surfaced at the import
# check several sections later.
# Pinned, not "newest". This cluster's 570 driver caps us at CUDA 12.x, and recent
# vLLM releases pull a torch built for CUDA 13 (vLLM 0.30.0 -> torch 2.13.0/cu13),
# which needs driver >= 580 and fails with "The NVIDIA driver on your system is
# too old (found version 12080)". So an unpinned install is a KNOWN-BROKEN default
# here, twice over: it also resolves to the 0.11.0 that py3.9 cannot import.
#
# 0.11.0 is the pin because its torch stack was OBSERVED working on this cluster
# (job 37229: torch 2.8.0, CUDA 12.8, cuda available: True) - it only failed
# there on the Python 3.9 union-annotation error, which does not exist on 3.12.
# Verified beats newest when the driver is the binding constraint.
VLLM_SPEC="${VLLM_SPEC:-vllm==0.11.0}"

#: transformers is capped below 5 for the same reason the driver caps vLLM: the
#: upper bound is missing upstream. vLLM 0.11.x calls
#: `tokenizer.all_special_tokens_extended`, which transformers 5.x removed, so an
#: unbounded resolve picks 5.17.0 and vLLM dies at load with
#: "AttributeError: Qwen2Tokenizer has no attribute all_special_tokens_extended".
#: 4.57.6 is the version this project's Transformers backend already ran Qwen3-8B
#: with, so it is verified against the same weights.
TRANSFORMERS_SPEC="${TRANSFORMERS_SPEC:-transformers>=4.51.0,<5}"

# Belt and braces: an empty spec can never reach pip again. `pip install ""`
# installs nothing and exits 0, so an empty value here fails silently.
for spec_name in VLLM_SPEC TRANSFORMERS_SPEC; do
    if [ -z "${!spec_name}" ]; then
        echo "BUG: $spec_name resolved to an empty string; refusing to run." >&2
        exit 1
    fi
done

if [ -z "$PYTHON_MODULE" ] && [ -z "$PYTHON_BIN" ]; then
    VENV_DIR="$P5_ROOT/vllm-venv"
else
    # The venv name encodes every knob. Changing any of them must not silently
    # reuse an environment built for another: a venv created by Python 3.9 would
    # be picked up by a 3.10+ job, and a venv holding vLLM 0.11.0 would be
    # reused for a pin that expects 0.10. Same knobs -> same venv, so ordinary
    # resubmits stay idempotent.
    TAG=$(printf '%s_%s_%s' "$VLLM_SPEC" "${PYTHON_MODULE:-systempy}" \
                          "${PYTHON_BIN:-defaultbin}" \
          | tr -c 'a-zA-Z0-9' '_')
    VENV_DIR="$P5_ROOT/vllm-venv-${TAG}"
fi

MODEL_DIR="$P5_ROOT/models/Qwen3-8B"
MAX_NEW_TOKENS=768

cd "${SLURM_SUBMIT_DIR:-$PWD}" || exit 1

section() {
    printf '\n'
    printf '=%.0s' {1..72}
    printf '\n%s\n' "$1"
    printf '=%.0s' {1..72}
    printf '\n'
}

FAILED_PRECONDITION=""

section "JOB"
echo "job      : ${SLURM_JOB_ID:-<unset>} on ${SLURMD_NODENAME:-<unset>} (${SLURM_JOB_PARTITION:-<unset>})"
echo "started  : $(date -Is)"
echo "repo     : $PWD"
echo "P5_ROOT  : $P5_ROOT"

section "PRECONDITION 1/2 — GPU present"
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,memory.total,compute_cap --format=csv,noheader 2>&1 || true
else
    echo "nvidia-smi missing — this job did not land on a GPU node."
    FAILED_PRECONDITION="no GPU on this node"
fi

section "PRECONDITION 2/2 — are the weights already here?"
if [ -f "$MODEL_DIR/config.json" ]; then
    ls -1 "$MODEL_DIR"/*.safetensors 2>/dev/null | wc -l | xargs -I{} echo "  safetensors shards : {}"
    du -sh "$MODEL_DIR" 2>/dev/null || true
else
    echo "MISSING: $MODEL_DIR/config.json"
    echo
    echo "Run step 2 first — it downloads the weights. This script deliberately"
    echo "does NOT download them: one job should own the download, so that a"
    echo "failure here cannot leave a half-fetched snapshot behind."
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }weights not downloaded"
fi

section "PYTHON"
if [ -n "$PYTHON_MODULE" ]; then
    # The module system is a shell function, not a binary, so a non-interactive
    # batch shell does not have it until the init is sourced. Bright Cluster
    # Manager (which this cluster runs, judging by /cm/local/modulefiles) keeps
    # its init in a different place from a stock Environment Modules install, so
    # several candidates are tried.
    for init in /etc/profile.d/modules.sh /etc/profile.d/lmod.sh \
                /usr/share/Modules/init/bash /usr/share/Modules/init/profile.sh \
                /usr/share/lmod/lmod/init/bash \
                /cm/local/apps/environment-modules/current/init/bash; do
        if [ -r "$init" ]; then
            # shellcheck disable=SC1090  # runtime probe, cannot be resolved statically
            . "$init"
            break
        fi
    done
    if ! command -v module >/dev/null 2>&1; then
        section "STOPPING: the module command is unavailable in this job"
        echo "PYTHON_MODULE=$PYTHON_MODULE was requested but no module init was"
        echo "found. Locate it on the login node and source it before the module"
        echo "line in this script:"
        echo "    ls /etc/profile.d/ | grep -i mod"
        echo "or bypass the module system entirely:"
        echo "    sbatch --export=ALL,PYTHON_BIN=/full/path/to/python3.12 ..."
        exit 1
    fi
    echo "loading module: $PYTHON_MODULE"
    if module load "$PYTHON_MODULE" 2>&1; then
        echo "module loaded."
    else
        echo "FAILED to load '$PYTHON_MODULE'. Run 'module avail python' on the"
        echo "login node for the exact spelling, then resubmit."
        exit 1
    fi
fi
# A module named e.g. python312 very often ships `python3.12` WITHOUT shadowing
# the system `python3`. Picking `python3` unconditionally would then load the
# module and still run 3.9 - the exact bug this parameter exists to fix. So when
# a module is requested, the versioned binaries are preferred, newest first.
PY=""
if [ -n "$PYTHON_BIN" ]; then
    if [ -x "$PYTHON_BIN" ]; then
        PY="$PYTHON_BIN"
    else
        echo "PYTHON_BIN=$PYTHON_BIN is not an executable file."
        exit 1
    fi
elif [ -n "$PYTHON_MODULE" ]; then
    for candidate in python3.13 python3.12 python3.11 python3.10; do
        if command -v "$candidate" >/dev/null 2>&1; then
            PY="$candidate"
            break
        fi
    done
    if [ -z "$PY" ]; then
        echo "module '$PYTHON_MODULE' is loaded but exposes no python3.10+ binary."
        echo "Found instead:"
        for candidate in python3 python; do
            command -v "$candidate" >/dev/null 2>&1 && \
                echo "  $candidate -> $("$candidate" --version 2>&1)"
        done
        echo "Run 'module show $PYTHON_MODULE' on the login node to see what it"
        echo "sets, then set PYTHON_BIN explicitly."
        exit 1
    fi
fi
if [ -z "$PY" ]; then
    PY=python3
    command -v python3 >/dev/null 2>&1 || PY=python
fi
echo "interpreter        : $(command -v "$PY" 2>/dev/null || echo none)"
"$PY" --version 2>&1 || true

PY_MAJOR_MINOR=$("$PY" -c 'import sys; print(f"{sys.version_info[0]}.{sys.version_info[1]}")' 2>/dev/null || echo "0.0")
echo "version            : $PY_MAJOR_MINOR"

# Refuse to spend ten minutes installing something known not to work. vLLM
# dropped 3.9 in v0.11.1, so an unpinned install on 3.9 resolves to the broken
# 0.11.0. Catching it here costs seconds; catching it after the install costs a
# queue slot.
case "$PY_MAJOR_MINOR" in
    3.9|3.8|3.7|0.0)
        if [ "$VLLM_SPEC" = "vllm>=0.8.5" ]; then
            section "STOPPING: this interpreter cannot run a current vLLM"
            echo "Interpreter is Python $PY_MAJOR_MINOR, and the vLLM spec is the"
            echo "unpinned default, which resolves to 0.11.0 - installable but not"
            echo "importable on 3.9 (vLLM dropped 3.9 in v0.11.1)."
            echo
            echo "Either name a newer interpreter:"
            echo "  sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch"
            echo "or pin a series that supports 3.9:"
            echo "  sbatch --export=ALL,VLLM_SPEC='vllm==0.10.2' scripts/cluster/30_vllm.sbatch"
            exit 1
        fi
        ;;
esac

if [ -x "$VENV_DIR/bin/python" ]; then
    echo "reusing existing vllm venv: $VENV_DIR"
    VENV_PY="$VENV_DIR/bin/python"
else
    echo "creating separate venv at $VENV_DIR"
    if "$PY" -m venv "$VENV_DIR" 2>&1; then
        VENV_PY="$VENV_DIR/bin/python"
    else
        # No --user fallback here, deliberately. Falling back to the system
        # interpreter would install vLLM for whatever Python that is - very
        # likely the 3.9 this run exists to avoid - and the failure would then
        # look like a vLLM bug rather than a missing venv package.
        section "STOPPING: could not create a venv"
        echo "The interpreter is $PY ($PY_MAJOR_MINOR). Most likely the venv module"
        echo "is not available for it. Check on the login node:"
        echo "    module show $PYTHON_MODULE 2>&1 | head -30"
        echo "then set PYTHON_BIN to the interpreter that has venv, if a different"
        echo "one is on the module's PATH."
        exit 1
    fi
fi

if [ -n "$FAILED_PRECONDITION" ]; then
    section "STOPPING EARLY"
    echo "Unmet precondition(s): $FAILED_PRECONDITION"
    exit 1
fi

section "vllm PIN"
echo "spec : $VLLM_SPEC"
echo "venv : $VENV_DIR"

# The environment counts as ready only when BOTH hold. Checking `import vllm`
# alone is not enough: this venv already has a working vLLM 0.11.0 plus a
# transformers 5.17.0, and the mismatch only shows up later as
# "AttributeError: Qwen2Tokenizer has no attribute all_special_tokens_extended"
# when vLLM calls something transformers 5.x removed.
vllm_env_ready() {
    "$VENV_PY" - <<'PYEOF' >/dev/null 2>&1
import sys
try:
    import vllm  # noqa: F401
    import transformers
except Exception:
    sys.exit(1)
# vLLM 0.11.x cannot drive transformers 5.x.
sys.exit(0 if transformers.__version__.split(".")[0] == "4" else 1)
PYEOF
}

if ! vllm_env_ready; then
    section "INSTALLING vllm + transformers  (large: it brings its own torch — 10+ minutes)"
    # No `| tail` here, deliberately. A pipe into tail buffers everything until
    # the command exits, so a ten-minute download produces a completely silent
    # log - which reads as "hung" and invites killing a job that is working.
    # --progress-bar off removes the carriage-return spam; the Collecting /
    # Downloading / Installing lines still stream, so progress is visible.
    "$VENV_PY" -m pip install --progress-bar off --upgrade pip 2>&1
    # Both specs are passed together so pip resolves them JOINTLY. Installing
    # vLLM alone lets it pull transformers 5.x, which is the failure above.
    if ! "$VENV_PY" -m pip install --progress-bar off \
            "$VLLM_SPEC" "$TRANSFORMERS_SPEC" 2>&1; then
        section "STOPPING: the vLLM stack could not be installed"
        echo "vLLM spec         : $VLLM_SPEC"
        echo "transformers spec : $TRANSFORMERS_SPEC"
        echo "interpreter       : $("$VENV_PY" --version 2>&1)"
        echo
        echo "Check what versions exist for this interpreter, then widen or"
        echo "narrow the specs:"
        echo "    \"$VENV_PY\" -m pip index versions vllm"
        echo "    \"$VENV_PY\" -m pip index versions transformers"
        exit 1
    fi
fi

section "CAN vllm ACTUALLY BE IMPORTED?"
# The check that the 2026-09-23 run was missing. Installation succeeding says
# nothing about importability: vLLM 0.11.0 installs cleanly on Python 3.9 and
# then raises TypeError at import, because its annotations use PEP 604 unions
# (`X | None`) that 3.9 cannot evaluate at runtime. Catching it here names the
# cause, instead of letting it surface later as an opaque load failure.
VLLM_IMPORT=$("$VENV_PY" -c "import vllm; print(vllm.__version__)" 2>&1)
echo "$VLLM_IMPORT"
if ! "$VENV_PY" -c "import vllm" >/dev/null 2>&1; then
    section "STOPPING: vllm is installed but not importable"
    if echo "$VLLM_IMPORT" | grep -q "unsupported operand type(s) for |"; then
        echo "This is the Python 3.9 incompatibility, not a torch or CUDA problem."
        echo "The interpreter here is $("$VENV_PY" --version 2>&1)."
        echo
        echo "Pick one:"
        echo "  1. An older vLLM that genuinely supports 3.9 (fastest, no new infra):"
        echo "       sbatch --export=ALL,VLLM_SPEC='vllm==0.9.2' scripts/cluster/30_vllm.sbatch"
        echo "  2. A newer interpreter, if the cluster offers one:"
        echo "       module avail python"
        echo "     then load it and resubmit (the venv is rebuilt against it)."
    else
        echo "Cause is not the known py3.9 union-syntax issue; see the error above."
    fi
    exit 1
fi

# Same reason as step 2: P5's own runtime dependency is not part of the vLLM
# stack, and a fresh venv has none of it.
if ! "$VENV_PY" -c "import pydantic" >/dev/null 2>&1; then
    section "INSTALLING the project's own runtime dependencies"
    "$VENV_PY" -m pip install --progress-bar off -r requirements.txt 2>&1
fi

section "RESOLVED VERSIONS  (recorded, not assumed)"
"$VENV_PY" - <<'PYEOF' 2>&1 || true
import importlib.metadata as md
for pkg in ("vllm", "torch", "transformers", "pydantic"):
    try:
        print(f"  {pkg:<14}: {md.version(pkg)}")
    except md.PackageNotFoundError:
        print(f"  {pkg:<14}: NOT INSTALLED")
import torch
print(f"  torch CUDA    : {torch.version.cuda}")
print(f"  cuda available: {torch.cuda.is_available()}")
PYEOF

section "CAN TORCH SEE THE GPU?"
# This gate was missing from the run that produced the CUDA 13 failure: the
# script printed "cuda available: False" and then carried on to the smoke test
# anyway, so a job that could not possibly work spent minutes failing opaquely.
if ! "$VENV_PY" -c "import torch; raise SystemExit(0 if torch.cuda.is_available() else 1)" >/dev/null 2>&1; then
    TORCH_CUDA=$("$VENV_PY" -c "import torch; print(torch.version.cuda)" 2>/dev/null)
    DRIVER=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null | head -1)
    section "STOPPING: torch cannot see the GPU"
    echo "torch CUDA build : ${TORCH_CUDA:-unknown}"
    echo "node driver      : ${DRIVER:-unknown}"
    echo
    echo "A CUDA MAJOR version bump requires a matching driver major. CUDA 13"
    echo "wheels need driver >= 580; this cluster runs the 570 branch (CUDA 12.8)."
    echo "So a torch built for CUDA 13 is unusable here however new it is - and"
    echo "plain 'pip install vllm' now resolves to exactly that, because the PyPI"
    echo "default wheel tracks the newest CUDA."
    echo
    echo "Fix: pin a vLLM whose torch is a CUDA 12 build. vLLM 0.11.0 bundles"
    echo "torch 2.8.0 / CUDA 12.8, which this driver does support:"
    echo
    echo "  sbatch --export=ALL,PYTHON_MODULE=python312,VLLM_SPEC='vllm==0.11.0' \\"
    echo "         scripts/cluster/30_vllm.sbatch"
    echo
    echo "Note this is the same vLLM that failed on Python 3.9 with the union"
    echo "annotation error. On 3.12 that problem does not exist, which is why it"
    echo "is the right pin rather than a fallback."
    exit 1
fi
echo "torch sees the GPU."

section "PREFLIGHT — imports"
PREFLIGHT=$("$VENV_PY" - <<'PYEOF' 2>&1
import sys
sys.path.insert(0, ".")
try:
    from src.generation.generators import get_generator
    from src.generation.pipeline import GroundedQAPipeline  # noqa: F401
    from src.generation.schema import GenerationRequest  # noqa: F401
except Exception as exc:
    print(f"IMPORT FAILED: {type(exc).__name__}: {exc}")
    raise SystemExit(1)
print("all imports resolve")
PYEOF
)
echo "$PREFLIGHT"
if echo "$PREFLIGHT" | grep -q "IMPORT FAILED"; then
    section "STOPPING: the environment is incomplete"
    exit 1
fi

section "SMOKE TEST  (vLLM backend)"
echo "First run compiles CUDA graphs and warms the engine, so startup is slower"
echo "than later runs. The line to look for in the output is vLLM's own cache"
echo "accounting, which is the measurement the feasibility note is waiting on."
echo

CAPTURE="$P5_ROOT/vllm-smoke-${SLURM_JOB_ID:-manual}.log"
"$VENV_PY" scripts/smoke_test_qwen3.py \
    --backend vllm \
    --model "$MODEL_DIR" \
    --max-new-tokens "$MAX_NEW_TOKENS" \
    --show-prompt 2>&1 | tee "$CAPTURE"
SMOKE_EXIT=${PIPESTATUS[0]}

section "vLLM's OWN NUMBERS  (the authority over every estimate in §2)"
if grep -E "GPU KV cache size|Maximum concurrency|gpu_memory_utilization" "$CAPTURE" 2>/dev/null; then
    :
else
    echo "(none found — the engine may not have reached the cache-sizing stage)"
fi

section "RESULT"
echo "smoke test exit code : $SMOKE_EXIT"
echo "  0 = loaded, answered, passed validation   <- the target, and the gate"
echo "  1 = could not load at all"
echo "  2 = loaded, but the answer was refused or downgraded (prompt tuning,"
echo "      not a crash — see docs/PROMPT_TEMPLATE.md)"
echo "finished : $(date -Is)"
echo
echo "Full capture: $CAPTURE"
echo
echo "If this exits 0, P5's serving method is confirmed and P6 can be planned"
echo "against it. Record in docs/GPU_FEASIBILITY.md §2, replacing the last"
echo "estimates: load time, generation latency, peak VRAM, and the"
echo "'GPU KV cache size: N tokens' line above."
echo
echo "Do NOT install anything else into this venv without re-running this job —"
echo "a validated vLLM+torch pair is worth more than a marginally newer one."

exit "$SMOKE_EXIT"
