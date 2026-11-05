#!/usr/bin/env bash
#
# Step 5 - the Week-3 evidence-binding run. Answers real retrieved passages
# through the real pipeline under BOTH backends, over the same dump, and prints
# the two question classes side by side.
#
#   sbatch scripts/cluster/50_week3_evidence.sbatch
#
# One backend only, if that is what you want:
#
#   sbatch --export=ALL,BACKEND=vllm scripts/cluster/50_week3_evidence.sbatch
#
# THIS SCRIPT INSTALLS NOTHING AND MODIFIES NO VENV, for the same reason step 4
# does not: both environments were validated on 2026-09-23 and the vLLM one is a
# triple pin - python312, vllm==0.11.0, transformers<5 - every element of which
# is load-bearing. It only runs what is already there, and says so loudly if
# what is already there is missing.
#
# WHICH DUMP IT RUNS ON IS THE WHOLE POINT OF THE WEEK, so it is printed at the
# top of the job and again in the summary. The default is the committed fixture,
# whose SHAPE is real but whose CONTENT is synthetic. A run over the fixture is
# a harness check; a run over a real retriever dump is the Week-3 deliverable.
# The script cannot tell the difference for you, so it says which one it used
# rather than letting a synthetic run be filed as evidence.
#
# PRECONDITIONS, none of which this script can create for you:
#   * step 2 has run and exited 0    (Transformers venv + weights)
#   * step 3 has run and exited 0    (the vLLM venv)
#   * the retriever dump exists      (or accept the fixture and know it)
#
#SBATCH --job-name=p5-week3
#SBATCH --output=logs/p5-week3-%j.out
# No --error directive, for the reason given in 20_load_qwen3.sbatch: a traceback
# in a file nobody tails is how a job appears to fail silently.
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1

# NOT `set -e`: each phase is allowed to fail without taking the other down, and
# its exit code is reported rather than swallowed. See 10_probe_gpu.sbatch.
set -uo pipefail

P5_ROOT="${P5_ROOT:-$HOME/p5}"
export HF_HOME="$P5_ROOT/hf"

BACKEND="${BACKEND:-both}"
TRANSFORMERS_VENV="${TRANSFORMERS_VENV:-$P5_ROOT/venv}"
VLLM_VENV="${VLLM_VENV:-}"

MODEL_DIR="$P5_ROOT/models/Qwen3-8B"
MAX_NEW_TOKENS=768

#: The retriever dump. Override with a real one:
#:   sbatch --export=ALL,RETRIEVAL="$P5_ROOT/data/p2_retrieval.jsonl" \
#:          scripts/cluster/50_week3_evidence.sbatch
RETRIEVAL="${RETRIEVAL:-tests/fixtures/retrieval_sample.jsonl}"
FIXTURE_PATH="tests/fixtures/retrieval_sample.jsonl"

OUT_DIR="runs/week3"

cd "${SLURM_SUBMIT_DIR:-$PWD}" || exit 1

JOB_ID="${SLURM_JOB_ID:-manual}"
ARTEFACT_DIR="$P5_ROOT/week3-$JOB_ID"

section() {
    printf '\n'
    printf '=%.0s' {1..72}
    printf '\n%s\n' "$1"
    printf '=%.0s' {1..72}
    printf '\n'
}

section "JOB"
echo "job       : $JOB_ID on ${SLURMD_NODENAME:-<unset>} (${SLURM_JOB_PARTITION:-<unset>})"
echo "started   : $(date -Is)"
echo "repo      : $PWD"
echo "P5_ROOT   : $P5_ROOT"
echo "backends  : $BACKEND"
echo "retrieval : $RETRIEVAL"

# --------------------------------------------------------------------------- #
# Preconditions
# --------------------------------------------------------------------------- #

FAILED_PRECONDITION=""

section "PRECONDITION 1/5 — GPU present and actually free"
if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=index,name,memory.used,memory.total,driver_version \
               --format=csv,noheader 2>&1 || true
    # The card this job owns. SLURM sets CUDA_VISIBLE_DEVICES to a physical
    # index, and on a 4-GPU node `nvidia-smi` with no --id reports device 0 -
    # very often another tenant's card.
    # `${VAR:-}` rather than the bare form: under `set -u` an unset
    # CUDA_VISIBLE_DEVICES aborts the job with "unbound variable", which reads
    # like a submission problem rather than a missing SLURM variable.
    DEVICE="${CUDA_VISIBLE_DEVICES:-}"
    DEVICE="${DEVICE%%,*}"
    DEVICE="${DEVICE:-0}"
    case "$DEVICE" in
        ''|*[!0-9]*) DEVICE=0 ;;
    esac
    BASELINE=$(nvidia-smi --id="$DEVICE" --query-gpu=memory.used \
                          --format=csv,noheader,nounits 2>/dev/null || echo "")
    echo "job device : $DEVICE   (CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-<unset>})"
    echo "baseline   : ${BASELINE:-unknown} MiB used before anything starts"
    if [ -n "$BASELINE" ] && [ "$BASELINE" -gt 1024 ] 2>/dev/null; then
        echo
        echo "WARNING: $BASELINE MiB is already in use on this card. Expect the vLLM"
        echo "phase to fail its own memory check before it tries to measure anything."
    fi
else
    echo "nvidia-smi missing - this job did not land on a GPU node."
    FAILED_PRECONDITION="no GPU on this node"
fi

section "PRECONDITION 2/5 — retriever dump, and whether it is real"
if [ ! -f "$RETRIEVAL" ]; then
    echo "MISSING: $RETRIEVAL"
    echo
    echo "Point the job at the retriever's output:"
    echo "    sbatch --export=ALL,RETRIEVAL=/path/to/dump.jsonl scripts/cluster/50_week3_evidence.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }no retrieval dump"
elif [ "$RETRIEVAL" = "$FIXTURE_PATH" ]; then
    echo "Using the committed fixture: $RETRIEVAL"
    echo
    echo "NOTE: this fixture's SHAPE is real (confirmed with the retrieval phase on"
    echo "2026-10-10) but its CONTENT is synthetic - the paper ids, titles and"
    echo "figures in it are invented. A run over it proves the pipeline works. It is"
    echo "NOT the Week-3 deliverable, which requires a real retriever dump."
else
    echo "Using: $RETRIEVAL"
    echo "records: $(wc -l < "$RETRIEVAL") line(s), sha256 $(sha256sum "$RETRIEVAL" | cut -c1-16)..."
fi

section "PRECONDITION 3/5 — weights"
if [ -f "$MODEL_DIR/config.json" ]; then
    du -sh "$MODEL_DIR" 2>/dev/null || true
else
    echo "MISSING: $MODEL_DIR/config.json"
    echo "Run step 2 first:  sbatch scripts/cluster/20_load_qwen3.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }weights missing"
fi

section "PRECONDITION 4/5 — Transformers venv"
TF_PY="$TRANSFORMERS_VENV/bin/python"
if [ -x "$TF_PY" ] && "$TF_PY" -c "import torch, transformers" >/dev/null 2>&1; then
    echo "using $TRANSFORMERS_VENV"
    "$TF_PY" -c "import torch, transformers, pydantic; print('  torch', torch.__version__, '| transformers', transformers.__version__, '| cuda', torch.cuda.is_available())"
else
    echo "not usable: $TRANSFORMERS_VENV (missing, or torch/transformers do not import)"
    echo "Run step 2 first:  sbatch scripts/cluster/20_load_qwen3.sbatch"
    FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }no usable Transformers venv"
fi

section "PRECONDITION 5/5 — vLLM venv"
# Same probing logic as step 4, and for the same reason: an account can hold
# several vLLM venvs, the FILENAME PROVES NOTHING about which works, and a venv
# named for 0.11.0 can still be a Python 3.9 one where vLLM installs cleanly and
# dies at import. The import check is the authority, not the glob order.
PREFERRED_VLLM_TAG="vllm__0_11_0"

vllm_env_ready() {
    "$1" - <<'VLLMEOF' >/dev/null 2>&1
import sys
try:
    import vllm  # noqa: F401
    import transformers
except Exception:
    sys.exit(1)
sys.exit(0 if transformers.__version__.split(".")[0] == "4" else 1)
VLLMEOF
}

vllm_version_of() {
    "$1" -c "import vllm; print(vllm.__version__)" 2>/dev/null || echo "unimportable"
}

VLLM_PY=""

if [ "$BACKEND" = "transformers" ]; then
    echo "skipped: BACKEND=transformers, so no vLLM venv is needed."
else
    if [ -n "$VLLM_VENV" ]; then
        CANDIDATES=("$VLLM_VENV")
        echo "VLLM_VENV was set explicitly; probing it and nothing else."
    else
        CANDIDATES=()
        for candidate in "$P5_ROOT"/vllm-venv-* "$P5_ROOT/vllm-venv"; do
            [ -x "$candidate/bin/python" ] && CANDIDATES+=("$candidate")
        done
        echo "Probing ${#CANDIDATES[@]} candidate venv(s) under $P5_ROOT."
    fi

    USABLE=()
    for candidate in ${CANDIDATES+"${CANDIDATES[@]}"}; do
        if vllm_env_ready "$candidate/bin/python"; then
            printf '  usable   %s  (vllm %s)\n' "$candidate" "$(vllm_version_of "$candidate/bin/python")"
            USABLE+=("$candidate")
        else
            printf '  unusable %s  (vllm %s)\n' "$candidate" "$(vllm_version_of "$candidate/bin/python")"
        fi
    done

    case "${#USABLE[@]}" in
        1)
            VLLM_VENV="${USABLE[0]}"
            VLLM_PY="$VLLM_VENV/bin/python"
            echo
            echo "using $VLLM_VENV  (vllm $(vllm_version_of "$VLLM_PY"))"
            ;;
        0)
            echo
            echo "None of the candidates can import a working vLLM. Step 3 builds the"
            echo "pinned one that was validated on this cluster:"
            echo "    sbatch --export=ALL,PYTHON_MODULE=python312 scripts/cluster/30_vllm.sbatch"
            FAILED_PRECONDITION="${FAILED_PRECONDITION:+$FAILED_PRECONDITION; }no usable vLLM venv"
            ;;
        *)
            VLLM_VENV="${USABLE[0]}"
            for candidate in "${USABLE[@]}"; do
                case "$candidate" in *"$PREFERRED_VLLM_TAG"*) VLLM_VENV="$candidate" ;; esac
            done
            VLLM_PY="$VLLM_VENV/bin/python"
            echo
            echo "${#USABLE[@]} of them work. Using the one matching the validated pin:"
            echo "    $VLLM_VENV  (vllm $(vllm_version_of "$VLLM_PY"))"
            echo "Override with --export=ALL,VLLM_VENV=<path> if you meant a different one."
            ;;
    esac
fi

if [ -n "$FAILED_PRECONDITION" ]; then
    section "STOPPING EARLY"
    echo "Unmet precondition(s): $FAILED_PRECONDITION"
    echo
    echo "Nothing was loaded and no GPU time was spent."
    exit 1
fi

# --------------------------------------------------------------------------- #
# Phase 0 - prove the harness works before paying for a model load
# --------------------------------------------------------------------------- #

section "PHASE 0 — harness preflight (mock backend, no GPU, ~2 seconds)"
# The alternative is discovering a typo in the dump after a ten-minute weight
# load. It uses the Transformers interpreter because that venv is the one
# guaranteed to have pydantic.
PREFLIGHT_DIR=$(mktemp -d)
if ! "$TF_PY" scripts/generate_from_retrieval.py \
        --retrieval "$RETRIEVAL" \
        --backend mock \
        --out "$PREFLIGHT_DIR/answers.jsonl" \
        --notes-out "$PREFLIGHT_DIR/notes.json" \
        --no-resume >"$PREFLIGHT_DIR/preflight.log" 2>&1; then
    section "STOPPING: the harness itself fails"
    echo "The mock path could not run the dump. Full output:"
    cat "$PREFLIGHT_DIR/preflight.log"
    echo
    echo "Re-run it visibly to see why:"
    echo "    $TF_PY scripts/generate_from_retrieval.py --retrieval $RETRIEVAL \\"
    echo "        --backend mock --out /tmp/p5-preflight.jsonl"
    exit 1
fi
cat "$PREFLIGHT_DIR/preflight.log"
echo
echo "The dump adapts, the pipeline runs, artefacts write. Proceeding."
rm -rf "$PREFLIGHT_DIR"

mkdir -p "$OUT_DIR" "$ARTEFACT_DIR"

# The job owns these two tags. Removing them is what makes a resubmit idempotent
# rather than silently resuming over a previous run's records.
for stale in "$OUT_DIR/answers-transformers-cluster.jsonl" \
             "$OUT_DIR/answers-vllm-cluster.jsonl" \
             "$OUT_DIR/notes-transformers-cluster.json" \
             "$OUT_DIR/notes-vllm-cluster.json"; do
    if [ -f "$stale" ]; then
        echo "removing previous artefact: $stale"
        rm -f "$stale"
    fi
done

# --------------------------------------------------------------------------- #
# The phases
# --------------------------------------------------------------------------- #

TF_EXIT="skipped"
VLLM_EXIT="skipped"

run_phase() {
    # $1 backend, $2 interpreter, $3 gateway flag name
    local backend="$1" interpreter="$2"
    local capture="$ARTEFACT_DIR/week3-${backend}-${JOB_ID}.log"
    # Declared BEFORE the pipeline: `local` is itself a command and resets
    # PIPESTATUS, so a declaration placed after the pipeline makes
    # ${PIPESTATUS[0]} read `local`'s own status - always 0. Every phase then
    # reports success, including one that crashed or wrote nothing.
    local exit_code=0

    section "PHASE — $backend  (its own process; VRAM is released when it exits)"
    # `-u` because stdout is a pipe into `tee`, and a pipe makes Python block-
    # buffer: without it the log sits empty for minutes and reads as a hung job.
    "$interpreter" -u scripts/generate_from_retrieval.py \
        --retrieval "$RETRIEVAL" \
        --backend "$backend" \
        --model "$MODEL_DIR" \
        --tag cluster \
        --out "$OUT_DIR/answers-${backend}-cluster.jsonl" \
        --max-new-tokens "$MAX_NEW_TOKENS" \
        2>&1 | tee "$capture"
    exit_code=${PIPESTATUS[0]}

    echo
    echo "  $backend exit code: $exit_code"
    echo "  full capture: $capture"
    echo "  VRAM after: $(nvidia-smi --id="$DEVICE" --query-gpu=memory.used \
                              --format=csv,noheader,nounits 2>/dev/null || echo '?') MiB"
    sleep 5
    return "$exit_code"
}

if [ "$BACKEND" = "both" ] || [ "$BACKEND" = "transformers" ]; then
    run_phase transformers "$TF_PY"
    TF_EXIT=$?
fi

if [ "$BACKEND" = "both" ] || [ "$BACKEND" = "vllm" ]; then
    run_phase vllm "$VLLM_PY"
    VLLM_EXIT=$?
fi

# --------------------------------------------------------------------------- #
# The two question classes
# --------------------------------------------------------------------------- #

section "TWO QUESTION CLASSES — answerable vs insufficient evidence"
# Read straight off the records, no model involved, so either interpreter runs
# it. This is the table docs/WEEK3_EVIDENCE_BINDING.md transcribes, and it is
# printed here rather than computed later because the job is the only place the
# real run's output exists.
"$TF_PY" - "$OUT_DIR" <<'SUMMARYEOF'
import json, sys
from pathlib import Path

out_dir = Path(sys.argv[1])
print(f"{'backend':<16} {'answered':>8} {'refused':>8} {'downgraded':>11} {'no-cite':>8}  violations")
print("-" * 92)
for backend in ("transformers", "vllm"):
    path = out_dir / f"answers-{backend}-cluster.jsonl"
    if not path.exists():
        print(f"{backend:<16} {'-':>8} {'-':>8} {'-':>11} {'-':>8}  (not run)")
        continue
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    counts: dict[str, int] = {}
    answered = refused = downgraded = no_cite = 0
    for record in records:
        result, validation = record["result"], record["validation"]
        if result["evidence_status"] == "SUFFICIENT":
            answered += 1
            if not result["citations"]:
                no_cite += 1
        else:
            refused += 1
        if validation["downgraded"]:
            downgraded += 1
        for violation in validation["violations"]:
            counts[violation["code"]] = counts.get(violation["code"], 0) + 1
    print(f"{backend:<16} {answered:>8} {refused:>8} {downgraded:>11} {no_cite:>8}  "
          + (", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "-"))
print()
print("'no-cite' must be 0: a SUFFICIENT answer with no citation is a contract violation.")
print("A refusal is a result, not a failure - the empty-retrieval case is supposed to refuse.")
SUMMARYEOF

section "RESULT"
echo "retrieval dump    : $RETRIEVAL"
if [ "$RETRIEVAL" = "$FIXTURE_PATH" ]; then
    echo "                    ^ SYNTHETIC CONTENT. Harness check, not Week-3 evidence."
fi
echo "transformers exit : $TF_EXIT"
echo "vllm exit         : $VLLM_EXIT"
echo "  0 = ran and wrote   1 = could not load/run   2 = nothing produced"
echo "finished          : $(date -Is)"
echo
echo "Artefacts:"
ls -1 "$ARTEFACT_DIR" 2>/dev/null || true
echo
echo "NEXT - the numbers are not a deliverable until they are written down:"
echo "  1. copy the answers and notes back into the repo:"
echo "       scp <user>@<login>:$PWD/$OUT_DIR/answers-*-cluster.jsonl <local repo>/$OUT_DIR/"
echo "       scp <user>@<login>:$PWD/$OUT_DIR/answers-*-cluster.notes.json <local repo>/$OUT_DIR/"
echo "  2. transcribe the two-question-class table above into"
echo "     docs/WEEK3_EVIDENCE_BINDING.md, quoting the job id ($JOB_ID)."
echo "  3. if this ran on the fixture, say so in the document. A synthetic run"
echo "     filed as real evidence is the one error this script cannot prevent."
echo

if [ ! -f "$OUT_DIR/answers-transformers-cluster.jsonl" ] && \
   [ ! -f "$OUT_DIR/answers-vllm-cluster.jsonl" ]; then
    echo "No answers file was produced at all - resubmitting unchanged will not help."
    exit 1
fi

exit 0
