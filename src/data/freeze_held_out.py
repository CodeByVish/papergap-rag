"""Retire historical BM25 artifacts and freeze an independent held-out version.

The standard-library CLI fingerprints history without displaying its content.
Eligibility and sampling operate on identifiers and corpus metadata; original
question text is projected only after the draw. No retrieval is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import random
import subprocess
from collections import Counter
from pathlib import Path

from src.data.build_held_out_exclusions import (
    FIELDS,
    build,
    index_questions,
    read_jsonl,
    sha256,
)

DATA = Path("data/processed")
CONFIG = Path("configs/held_out_sampling_v2.json")
RETIREMENT = DATA / "historical_bm25_retirement.manifest.json"
OUTPUT = DATA / "qa_for_held_out_v2.jsonl"


def write_new(path: Path, payload: bytes) -> None:
    """Create an artifact without replacing any prior version.

    Args:
        path: Unused destination; parents are created as needed.
        payload: Exact UTF-8 serialized bytes to preserve.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)


def json_bytes(value: dict) -> bytes:
    """Serialize metadata consistently across generation and verification.

    Args:
        value: JSON-compatible manifest.

    Returns:
        Indented, sorted UTF-8 JSON with a final newline.
    """
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def historical_hashes() -> dict[str, str]:
    """Fingerprint every retained old question, retrieval and annotation file.

    Returns:
        Repository-relative paths and exact byte hashes. Files remain in place.
    """
    paths = [DATA / "qa_for_held_out.jsonl", DATA / "qa_for_held_out.manifest.json"]
    paths += sorted(p for p in (DATA / "annotation_held_out").rglob("*") if p.is_file())
    if not (DATA / "annotation_held_out/manifest.json").is_file():
        raise ValueError("historical BM25 manifest missing")
    return {p.as_posix(): sha256(p) for p in paths}


def retire(verify_only: bool = False) -> dict:
    """Retain history and record its exclusion from the replacement evaluation.

    Args:
        verify_only: Compare the saved retirement record without writing.

    Returns:
        Retirement metadata and question-level usage audit from Step 2.4.
    """
    if not verify_only and RETIREMENT.exists():
        raise FileExistsError(RETIREMENT)
    banned = build(
        Path("configs/held_out_exclusions.json"),
        DATA / "qa_banned_for_held_out.jsonl",
        True,
    )
    old = index_questions(read_jsonl(DATA / "qa_for_held_out.jsonl"))
    old_manifest = json.loads(
        (DATA / "annotation_held_out/manifest.json").read_text(encoding="utf-8")
    )
    decision = next(
        d
        for d in banned["usage_decisions"]
        if d["source_id"] == "P3-historical-BM25-evaluation"
    )
    if (
        len(old) != 200
        or set(old) != set(old_manifest["question_ids"])
        or set(old) != set(decision["question_ids"])
    ):
        raise ValueError("historical question inventory disagrees with usage audit")
    banned_ids = set(index_questions(read_jsonl(DATA / "qa_banned_for_held_out.jsonl")))
    result = {
        "schema_version": "v0-proposed",
        "status": "retired; historical BM25 version only",
        "reason": json.loads(CONFIG.read_text(encoding="utf-8"))["reason"],
        "retained_files": historical_hashes(),
        "banned_manifest_sha256": sha256(DATA / "qa_banned_for_held_out.manifest.json"),
        "usage_decision": decision,
        "historical_question_count": len(old),
        "historical_banned_question_ids": sorted(set(old) & banned_ids),
        "other_historical_question_ids": sorted(set(old) - banned_ids),
        "reuse_policy": "Eligible historical IDs may be randomly redrawn; never reuse old pairs, ranks, scores, labels or record numbering for the new evaluation.",
        "replacement_questions": OUTPUT.as_posix(),
    }
    if verify_only:
        if json.loads(RETIREMENT.read_text(encoding="utf-8")) != result:
            raise ValueError("historical retirement or retained bytes changed")
    else:
        write_new(RETIREMENT, json_bytes(result))
    return result


def eligible_ids(
    metadata: list[dict], banned: set[str], counts: Counter, minimum: int
) -> tuple[list[str], dict]:
    """Filter candidates without consulting queries, answers or gold relevance.

    Args:
        metadata: Gold mapping projection containing only identity fields.
        banned: Complete verified cross-branch exclusion IDs.
        counts: Number of distinct nonempty passages per paper.
        minimum: Required retrievable passage count per paper.

    Returns:
        Sorted eligible IDs and disjoint rejection lists, banned before size.
    """
    indexed = index_questions(metadata)
    rejected = {"banned": [], "fewer_than_minimum_passages": []}
    eligible = []
    for qid in sorted(indexed):
        row = indexed[qid]
        if any(
            not isinstance(row.get(k), str) or not row[k].strip()
            for k in ("paper_id", "source_split")
        ):
            raise ValueError("incomplete candidate identity")
        if qid in banned:
            rejected["banned"].append(qid)
        elif counts[row["paper_id"]] < minimum:
            rejected["fewer_than_minimum_passages"].append(qid)
        else:
            eligible.append(qid)
    return eligible, rejected


def draw_ids(eligible: list[str], seed: int, count: int) -> list[str]:
    """Draw questions uniformly without replacement and retain random order.

    Args:
        eligible: Unique candidate identifiers; input order is ignored.
        seed: Predeclared independent random generator seed.
        count: Required number of questions.

    Returns:
        Draw order, independent of split or historical retrieval performance.
    """
    if len(set(eligible)) != len(eligible) or len(eligible) < count:
        raise ValueError("duplicate or insufficient eligible questions")
    return random.Random(seed).sample(sorted(eligible), count)


def freeze(output: Path = OUTPUT, verify_only: bool = False) -> dict:
    """Validate prerequisites, reconstruct the draw and create or verify a freeze.

    Args:
        output: New versioned JSONL path; companion uses .manifest.json.
        verify_only: Compare all saved bytes and metadata without writes.

    Returns:
        Frozen sampling provenance, eligibility accounting and validation.

    Raises:
        ValueError: Input hashes, corpus identity or reconstructed output differ.
        FileExistsError: Generation would replace either existing output.
    """
    companion = output.with_suffix(".manifest.json")
    if not verify_only and (output.exists() or companion.exists()):
        raise FileExistsError("refusing to replace an existing held-out version")
    retirement = retire(True)
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if config["question_count"] != 200 or config["minimum_passages_per_paper"] != 5:
        raise ValueError("this freeze requires 200 questions and five passages")
    paths = [
        CONFIG,
        RETIREMENT,
        DATA / "qa_banned_for_held_out.jsonl",
        DATA / "qa_banned_for_held_out.manifest.json",
        DATA / "gold_evidence_mapping_all_splits.jsonl",
        DATA / "gold_evidence_mapping_all_splits.manifest.json",
        DATA / "passages_all_paper_text.jsonl",
        DATA / "passages_all_paper_text.manifest.json",
        DATA / "qa.jsonl",
    ]
    inputs = {p.as_posix(): sha256(p) for p in paths}
    corpus_manifest = json.loads(
        (DATA / "passages_all_paper_text.manifest.json").read_text(encoding="utf-8")
    )
    gold_manifest = json.loads(
        (DATA / "gold_evidence_mapping_all_splits.manifest.json").read_text(
            encoding="utf-8"
        )
    )
    for key, value in (("chunk_size_words", 365), ("chunk_overlap_words", 40)):
        if (
            corpus_manifest["chunking"][key] != value
            or gold_manifest["chunking"][key] != value
        ):
            raise ValueError("corpus must use fixed 365/40 chunking")
    if (
        corpus_manifest["scope"] != "all-paper-text"
        or gold_manifest["scope"] != "all-splits-reference"
    ):
        raise ValueError("incorrect corpus or gold scope")
    if corpus_manifest["output"]["sha256"] != sha256(
        DATA / "passages_all_paper_text.jsonl"
    ):
        raise ValueError("corpus hash mismatch")
    if gold_manifest["output"]["sha256"] != sha256(
        DATA / "gold_evidence_mapping_all_splits.jsonl"
    ):
        raise ValueError("gold mapping hash mismatch")
    for item in gold_manifest["inputs"].values():
        path = DATA / item["file"]
        if sha256(path) != item["sha256"]:
            raise ValueError(f"gold input hash mismatch: {path}")
        inputs[path.as_posix()] = sha256(path)
    corpus = read_jsonl(DATA / "passages_all_paper_text.jsonl")
    passage_ids = [r["passage_id"] for r in corpus]
    if len(set(passage_ids)) != len(corpus) or any(
        not r["text"].strip() for r in corpus
    ):
        raise ValueError("duplicate or empty corpus passages")
    if len(corpus) != corpus_manifest["output"]["passage_count"]:
        raise ValueError("corpus count mismatch")
    counts = Counter(r["paper_id"] for r in corpus)
    # Do not expose or use candidate queries, answers, evidence or rankings.
    metadata = [
        {k: r[k] for k in ("question_id", "paper_id", "source_split")}
        for r in read_jsonl(DATA / "gold_evidence_mapping_all_splits.jsonl")
    ]
    qa = index_questions(
        [
            {k: r[k] for k in ("question_id", "paper_id", "source_split")}
            for r in read_jsonl(DATA / "qa.jsonl")
        ]
    )
    if any(r != qa.get(r["question_id"]) for r in metadata):
        raise ValueError("gold candidate metadata differs from canonical QA")
    banned_ids = set(index_questions(read_jsonl(DATA / "qa_banned_for_held_out.jsonl")))
    eligible, rejected = eligible_ids(
        metadata, banned_ids, counts, config["minimum_passages_per_paper"]
    )
    selected = draw_ids(eligible, config["seed"], config["question_count"])
    # Text is copied verbatim only after IDs have been selected and fixed.
    chosen = {
        r["question_id"]: r
        for r in read_jsonl(DATA / "qa.jsonl")
        if r["question_id"] in set(selected)
    }
    rows = [{k: chosen[qid][k] for k in FIELDS} for qid in selected]
    if len(set(selected)) != 200 or set(selected) & banned_ids:
        raise ValueError("held-out uniqueness or exclusion violation")
    if any(
        any(not isinstance(r[k], str) or not r[k].strip() for k in FIELDS) for r in rows
    ):
        raise ValueError("incomplete selected question fields")
    payload = "".join(
        json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows
    ).encode("utf-8")
    result = {
        "schema_version": "v0-proposed",
        "purpose": "frozen held-out question list for common three-algorithm evaluation",
        "status": "frozen",
        "configuration": config,
        "inputs": inputs,
        "code": {
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], text=True
            ).strip(),
            "python": platform.python_version(),
            "implementation_sha256": sha256(Path(__file__)),
        },
        "candidate_count": len(metadata),
        "banned_question_count": len(banned_ids),
        "eligible_question_ids": eligible,
        "rejections": rejected,
        "question_ids": selected,
        "question_count": len(rows),
        "paper_count": len({r["paper_id"] for r in rows}),
        "source_split_counts": dict(
            sorted(Counter(r["source_split"] for r in rows).items())
        ),
        "selected_paper_passage_counts": {
            p: counts[p] for p in sorted({r["paper_id"] for r in rows})
        },
        "historical_redrawn_question_ids": sorted(
            set(selected) & (set(retirement["other_historical_question_ids"]))
        ),
        "validation": {
            "exactly_200_unique": True,
            "banned_intersection_empty": True,
            "at_least_five_passages_per_paper": True,
            "canonical_question_text": True,
            "retained_history_hashes_verified": True,
            "exclusion_inventory_reconstructed": True,
        },
        "output": {
            "path": output.as_posix(),
            "sha256": hashlib.sha256(payload).hexdigest(),
        },
        "next_action": "Step 2.6: fresh BM25/Dense/Hybrid retrieval under pre-frozen development settings; no retrieval or annotation export performed by this command.",
    }
    if verify_only:
        saved = json.loads(companion.read_text(encoding="utf-8"))
        result["code"]["commit"] = saved["code"]["commit"]
        if output.read_bytes() != payload or saved != result:
            raise ValueError("freeze differs from reconstructed sample or provenance")
    else:
        write_new(output, payload)
        write_new(companion, json_bytes(result))
    return result


def main() -> None:
    """Expose retirement, freeze and read-only reconstruction operations.

    Run retirement first; generation refuses replacement and prints counts only.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("retire", "freeze", "verify"))
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = (
        retire()
        if args.action == "retire"
        else freeze(args.output, args.action == "verify")
    )
    print(
        json.dumps(
            {
                k: result[k]
                for k in (
                    "status",
                    "question_count",
                    "candidate_count",
                    "source_split_counts",
                )
                if k in result
            }
        )
    )


if __name__ == "__main__":
    main()
