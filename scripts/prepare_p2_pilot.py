"""Select complete training papers for a bounded, paper-scoped P2 pilot."""

import argparse
import json
from collections import Counter
from pathlib import Path

from scripts.benchmark_p2 import select_queries, sha256
from scripts.build_indexes import load_passages


def prepare_pilot(
    passages_path, qa_path, output, manifest_output, questions=6, minimum=20
):
    if output.resolve() == manifest_output.resolve():
        raise ValueError("Passage and manifest outputs must differ")
    if output.exists() or manifest_output.exists():
        raise FileExistsError(
            "Choose new output paths; existing artifacts are preserved"
        )
    passages = load_passages(passages_path)
    queries = select_queries(
        qa_path, Counter(p.paper_id for p in passages), questions, minimum
    )
    papers = {row["paper_id"] for row in queries}
    selected = [passage for passage in passages if passage.paper_id in papers]
    output.parent.mkdir(parents=True, exist_ok=True)
    manifest_output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as destination:
        for passage in selected:
            destination.write(passage.model_dump_json() + "\n")
    manifest = {
        "purpose": "training-only scoped retrieval pilot",
        "source_corpus_sha256": sha256(passages_path),
        "qa_export_sha256": sha256(qa_path),
        "corpus_sha256": sha256(output),
        "passage_count": len(selected),
        "paper_ids": sorted(papers),
        "query_inputs": queries,
        "selection": "same select_queries defaults as scripts.benchmark_p2; retain all passages for each selected paper",
    }
    with manifest_output.open("x", encoding="utf-8") as destination:
        json.dump(manifest, destination, indent=2)
        destination.write("\n")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--qa", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest-output", type=Path, required=True)
    parser.add_argument("--questions", type=int, default=6)
    parser.add_argument("--min-passages", type=int, default=20)
    args = parser.parse_args()
    try:
        result = prepare_pilot(
            args.passages,
            args.qa,
            args.output,
            args.manifest_output,
            args.questions,
            args.min_passages,
        )
        print(
            json.dumps(
                {key: value for key, value in result.items() if key != "query_inputs"},
                indent=2,
            )
        )
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
