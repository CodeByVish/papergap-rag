"""Read a run's critic: every verdict against whether the gold passages were within its reach.

    python -m scripts.audit_critic --run-dir runs/p4/critic-fourth-40 --items items.jsonl

Prints the table used in docs/P4_REPORT_CONTRIBUTION.md (Section 3.3): how often the critic said
"insufficient" although all gold was in view, how often it accepted a question it should not
have (gold missing, or the paper cannot answer), and the verdict sources (llm, fallback, rules,
reused). `--items` needs gold, so for a held-out run it is used only after the run, with the
gold released for scoring.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.run_agent_experiment import load_items_jsonl  # noqa: E402
from src.agent.experiments import audit_critic, format_audit  # noqa: E402


def main(argv: Sequence[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--run-dir", type=Path, required=True, help="folder with <arm>.jsonl records")
    p.add_argument("--items", type=Path, required=True, help="items JSONL with gold passages")
    p.add_argument("--arm", default="adaptive", help="which arm's records to read")
    p.add_argument("--out-json", type=Path, help="also write the counts as JSON")
    args = p.parse_args(argv)

    path = args.run_dir / f"{args.arm}.jsonl"
    if not path.exists():
        raise SystemExit(f"{path} not found")
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    audit = audit_critic(records, load_items_jsonl(args.items))
    print(format_audit(audit))
    if args.out_json:
        args.out_json.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
