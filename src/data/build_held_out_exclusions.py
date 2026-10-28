"""Build a provenance-preserving ban list from delivered usage inventories.

This standard-library-only entry point verifies pinned owner snapshots, joins
original QA identities and classifies persisted P3 use without resampling or
opening historical retrieval results. Run as a module from the repository root.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

FIELDS = ("question_id", "paper_id", "question", "source_split")


def sha256(path: Path) -> str:
    """Fingerprint exact artifact bytes, including original line endings.

    Args:
        path: Existing input or output artifact.

    Returns:
        Lowercase SHA-256 digest.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    """Decode nonblank UTF-8 JSONL records in saved order.

    Args:
        path: Structured source artifact.

    Returns:
        Parsed JSON objects.
    """
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def index_questions(rows: list[dict]) -> dict[str, dict]:
    """Reject missing or duplicate question IDs before joining sources.

    Args:
        rows: Source records containing question IDs.

    Returns:
        Unique identifier-to-record mapping.

    Raises:
        ValueError: An identifier is missing, empty or duplicated.
    """
    indexed = {}
    for row in rows:
        qid = row.get("question_id")
        if not isinstance(qid, str) or not qid or qid in indexed:
            raise ValueError("missing or duplicate question_id")
        indexed[qid] = row
    return indexed


def merge_sources(qa_rows: list[dict], sources: list[dict]) -> list[dict]:
    """Join original question text while preserving every usage record.

    Args:
        qa_rows: Canonical QA export; answers are never copied to the ban list.
        sources: Exclusion sources with source_id, reason, usage and records.

    Returns:
        Complete question records sorted by question_id, with all provenance.

    Raises:
        ValueError: A question is unknown or supplied identity fields disagree.
    """
    qa = index_questions(qa_rows)
    merged = {}
    for source in sources:
        index_questions(source["records"])
        for record in source["records"]:
            qid = record["question_id"]
            if qid not in qa:
                raise ValueError(f"unknown question_id: {qid}")
            original = qa[qid]
            if any(not isinstance(original.get(key), str) or not original[key].strip() for key in FIELDS):
                raise ValueError(f"incomplete canonical fields: {qid}")
            for key in FIELDS:
                if key in record and record[key] != original[key]:
                    raise ValueError(f"identity mismatch: {qid}/{key}")
            row = merged.setdefault(qid, {**{key: original[key] for key in FIELDS}, "sources": []})
            row["sources"].append({
                "source_id": source["source_id"],
                "usage": source["usage"],
                "exclusion_reason": source["reason"],
                "original_record": record,
            })
    return [merged[qid] for qid in sorted(merged)]


def build(config_path: Path, output: Path, verify_only: bool = False) -> dict:
    """Validate sources and generate or independently reconstruct the artifacts.

    Args:
        config_path: Versioned source pins and purpose classifications.
        output: New JSONL destination; its companion uses .manifest.json.
        verify_only: Compare regenerated rows and metadata with existing output.

    Returns:
        Manifest with source counts, hashes, coverage and validation results.

    Raises:
        ValueError: Hashes, identities, coverage or reconstructed output disagree.
        FileExistsError: Generation would replace existing output.
    """
    manifest_path = output.with_suffix(".manifest.json")
    if not verify_only and (output.exists() or manifest_path.exists()):
        raise FileExistsError("refusing to replace an existing exclusion version")
    config = json.loads(config_path.read_text(encoding="utf-8"))
    inputs = {}
    sources = []
    descriptors = []
    decisions = []

    def track(path: Path) -> Path:
        """Register an exact input digest before reading its structured content.

        Args:
            path: Existing artifact used by this audit.

        Returns:
            The same path for composable reads.
        """
        inputs[path.as_posix()] = sha256(path)
        return path

    track(config_path)
    qa_path = track(Path("data/processed/qa.jsonl"))
    for item in config["owner_inventories"]:
        path = track(Path(item["snapshot"]))
        if sha256(path) != item["sha256"]:
            raise ValueError(f"owner snapshot hash mismatch: {path}")
        records = read_jsonl(path)
        if len(index_questions(records)) != item["question_count"]:
            raise ValueError(f"owner inventory count mismatch: {path}")
        sources.append({"source_id": item["source_id"], "records": records,
                        "usage": "owner-designated development/integration inventory",
                        "reason": "explicit owner designation; no owner correction removing IDs"})
        descriptors.append(dict(item))

    selection_path = track(Path(config["selection_questions"]))
    selection = read_jsonl(selection_path)
    selected = set(index_questions(selection))
    if len(selected) != 250:
        raise ValueError("selection list must contain exactly 250 persisted questions")
    sources.append({"source_id": "P3-selection", "records": selection,
                    "usage": "chunk-size selection, round four",
                    "reason": "used to choose the 365/40 configuration"})
    preparation_path = track(Path(config["preparation_manifest"]))
    preparation = json.loads(preparation_path.read_text(encoding="utf-8"))
    if preparation["inputs"][selection_path.as_posix()] != sha256(selection_path):
        raise ValueError("selection hash differs from persisted preparation")
    audited_ids = set()
    for item in preparation["usage_audit"]:
        ids = item["question_ids"]
        audited_ids.update(ids)
        # The saved audit already contains historical IDs; old outputs are not
        # reparsed or required for accepting the owner-delivered inventories.
        functional = item["file"] in config["functional_runs"]
        if not functional and not set(ids) <= selected:
            raise ValueError(f"unresolved selection use outside saved list: {item['file']}")
        decision = {
            "source_id": f"P3-history:{item['file']}", "path": item["file"],
            "sha256": item["sha256"], "question_ids": ids,
            "decision": "not_automatically_excluded" if functional else "exclude",
            "usage": "pure functional adapter smoke check" if functional else "chunk-size selection, including superseded/void candidates",
            "reason": "Week 3 TODO 2.3 records functional verification only; no known tuning use" if functional else "candidate comparisons informed chunk-size development; void status does not restore eligibility",
        }
        decisions.append(decision)
        if not functional:
            sources.append({"source_id": decision["source_id"],
                            "records": [{"question_id": qid} for qid in ids],
                            "usage": decision["usage"], "reason": decision["reason"]})
    if audited_ids != set(preparation["excluded_question_ids"]):
        raise ValueError("persisted preparation ID coverage mismatch")
    for name in config["development_pilots"]:
        path = track(Path("data/processed") / name / "manifest.json")
        run = json.loads(path.read_text(encoding="utf-8"))
        ids = run["question_ids"]
        if not set(ids) <= selected:
            raise ValueError(f"unresolved pilot use outside selection list: {name}")
        sources.append({"source_id": f"P3-{name}",
                        "records": [{"question_id": qid} for qid in ids],
                        "usage": run["purpose"],
                        "reason": "development workflow/configuration verification; already used for selection"})
    frozen_path = track(Path(config["frozen_evaluation_manifest"]))
    frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
    decisions.append({"source_id": "P3-historical-BM25-evaluation",
                      "path": frozen_path.as_posix(), "sha256": sha256(frozen_path),
                      "question_ids": frozen["question_ids"],
                      "decision": "not_automatically_excluded",
                      "usage": "normal evaluation under frozen configuration",
                      "reason": "no known tuning use; retirement/resampling alone does not imply contamination; owner inventories still take precedence"})
    qa_rows = read_jsonl(qa_path)
    qa_ids = set(index_questions(qa_rows))
    for decision in decisions:
        if not set(decision["question_ids"]) <= qa_ids:
            raise ValueError(f"unknown IDs in usage decision: {decision['source_id']}")
    rows = merge_sources(qa_rows, sources)
    source_counts = {s["source_id"]: len(s["records"]) for s in sources}
    actual_counts = Counter(p["source_id"] for row in rows for p in row["sources"])
    if dict(actual_counts) != source_counts:
        raise ValueError("lost source provenance during merge")
    payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows).encode("utf-8")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    branch = subprocess.check_output(["git", "branch", "--show-current"], text=True).strip()
    manifest = {
        "schema_version": "v0-proposed", "purpose": "held-out exclusion inventory; not a held-out freeze",
        "repository": "https://github.com/CodeByVish/papergap-rag.git",
        "local_source_version": {"branch": branch, "commit": head},
        "implementation": {"path": Path(__file__).relative_to(Path.cwd()).as_posix(), "sha256": sha256(Path(__file__))},
        "inputs": inputs, "owner_inventories": descriptors,
        "source_counts": source_counts, "usage_decisions": decisions,
        "scope": config["scope"], "exclusion_rule": config["exclusion_rule"],
        "configuration": {"join_key": "question_id", "order": "question_id ascending", "question_fields": list(FIELDS), "sampling": "none"},
        "question_count": len(rows), "provenance_count": sum(actual_counts.values()),
        "source_split_counts": dict(sorted(Counter(r["source_split"] for r in rows).items())),
        "unresolved_records": [],
        "validation": {"unique_ids": True, "complete_fields": True, "canonical_identity_match": True,
                       "all_owner_and_selection_ids_included": True, "all_source_records_preserved": True,
                       "no_known_unresolved_eligibility_records_within_scope": True},
        "output": {"path": output.as_posix(), "sha256": hashlib.sha256(payload).hexdigest()},
    }
    if verify_only:
        saved = json.loads(manifest_path.read_text(encoding="utf-8"))
        # A later commit must not invalidate the recorded generation identity.
        manifest["local_source_version"] = saved["local_source_version"]
        if output.read_bytes() != payload or saved != manifest:
            raise ValueError("existing artifacts differ from reconstructed rows/manifest")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("xb") as handle:
            handle.write(payload)
        with manifest_path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    return manifest


def main() -> None:
    """Expose deterministic generation and read-only verification commands.

    Existing artifacts are never overwritten; use a new output for new evidence.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("configs/held_out_exclusions.json"))
    parser.add_argument("--output", type=Path, default=Path("data/processed/qa_banned_for_held_out.jsonl"))
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    manifest = build(args.config, args.output, args.verify)
    print(json.dumps({"question_count": manifest["question_count"], "source_counts": manifest["source_counts"], "unresolved_records": manifest["unresolved_records"], "output": manifest["output"]}))


if __name__ == "__main__":
    main()
