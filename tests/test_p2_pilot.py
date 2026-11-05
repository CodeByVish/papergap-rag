"""Pilot selection must retain complete papers and preserve existing artifacts."""

import json
from pathlib import Path

import pytest

from scripts.build_indexes import load_passages
from scripts.prepare_p2_pilot import prepare_pilot


def test_pilot_keeps_every_passage_of_selected_train_papers(tmp_path):
    source = Path(__file__).parent / "fixtures/mock_passages.jsonl"
    qa = tmp_path / "qa.jsonl"
    qa.write_text(
        json.dumps(
            {
                "source_split": "train",
                "paper_id": "synthetic-ir",
                "question_id": "q1",
                "question": "Which method?",
                "answers": ["not for retrieval"],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    output, manifest_path = tmp_path / "passages.jsonl", tmp_path / "manifest.json"
    manifest = prepare_pilot(source, qa, output, manifest_path, questions=1, minimum=2)
    selected = load_passages(output)
    assert selected == [
        p for p in load_passages(source) if p.paper_id == "synthetic-ir"
    ]
    assert manifest["passage_count"] == 4
    assert manifest["paper_ids"] == ["synthetic-ir"]
    assert set(manifest["query_inputs"][0]) == {"question_id", "paper_id", "question"}
    assert json.loads(manifest_path.read_text()) == manifest
    with pytest.raises(FileExistsError):
        prepare_pilot(source, qa, output, manifest_path)
    assert load_passages(output) == selected
