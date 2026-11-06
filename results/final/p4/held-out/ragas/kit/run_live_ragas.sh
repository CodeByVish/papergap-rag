#!/usr/bin/env bash
# Run the live RAGAS judge for one held-out arm.
#
#   export DASHSCOPE_API_KEY=...      # or the env var named in judge-config.json
#   bash run_live_ragas.sh static
#
# CPU only; no GPU and no sbatch. The key is read from the environment by
# src/evaluation/ragas_runner.py and never appears in this script or in argv.
set -euo pipefail

ARM="${1:?usage: run_live_ragas.sh static|adaptive|static-wide}"
BASE="${P5_BASE:-$HOME/p4-heldout-20261106}"
REPO="${P5_REPO:-$HOME/p4-critic-20261103/repo-heldout}"
PY="${P6_PY:-$HOME/p6-ragas-venv/bin/python}"
CFG="$BASE/ragas/judge-config.json"
OUT="$BASE/ragas/$ARM-live"

: "${DASHSCOPE_API_KEY:?export DASHSCOPE_API_KEY first}"
[ -f "$CFG" ] || { echo "missing $CFG (copy judge-config.template.json and fill it)"; exit 2; }
[ -e "$OUT" ] && { echo "$OUT exists; move it or choose a new output name"; exit 2; }
[ -f "$BASE/ragas/$ARM-contexts/contexts.jsonl" ] || { echo "missing contexts for $ARM"; exit 2; }

cd "$REPO"
# DashScope embeddings need check_embedding_ctx_length=False; the wrapper applies
# that to the unchanged evaluator CLI (see run_p6_evaluation_dashscope.py).
exec "$PY" "$BASE/live-ragas-kit/run_p6_evaluation_dashscope.py" ragas \
  --questions "$BASE/p4_held_out_items.jsonl" \
  --predictions "$BASE/runs/p4/held-out-200/$ARM.jsonl" \
  --references "$BASE/qa/qa.jsonl" \
  --contexts "$BASE/ragas/$ARM-contexts/contexts.jsonl" \
  --arm "$ARM" --role development \
  --live --judge-config "$CFG" \
  --cache "$BASE/ragas/judge-cache" \
  --output "$OUT"
