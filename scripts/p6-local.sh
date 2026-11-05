#!/usr/bin/env bash
set -euo pipefail
P6_REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$P6_REPO_ROOT"
if [[ ! -x .venv-p6/bin/python ]]; then
  echo 'Missing prepared environment. See docs/P6/P6_REAL_ENV_E2E_GUIDE.md.' >&2
  exit 1
fi
# Avoid tokenizer/OpenMP thread oversubscription on laptops.
export TOKENIZERS_PARALLELISM=false
export OMP_NUM_THREADS=1
exec .venv-p6/bin/python -u -m scripts.p6_local "${1:-start}"
