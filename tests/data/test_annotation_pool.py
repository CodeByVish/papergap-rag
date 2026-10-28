"""Test pool isolation, blind projection and stable annotation numbering.

Synthetic inputs keep tests independent of local QASPER content and downloads.
"""

import json
from pathlib import Path

import pytest

from src.data.build_annotation_pool import (
    SETTINGS,
    freeze,
    generate_pairs,
    render_batches,
    snapshot,
    unique_rows,
    verify_snapshot,
    write_json,
    write_jsonl,
)


def test_blind_projection_and_gold_join(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep references and retrieval details out of the independent view.

    The backend sees question text and paper scope, without gold evidence.
    """
    corpus = [
        {"passage_id": f"p{i}", "paper_id": "paper", "text": f"Text {i}"}
        for i in range(5)
    ]
    queries = []

    def factory(records: list) -> object:
        """Capture retrieval arguments without reading gold annotations.

        Args:
            records: Corpus with no evaluation reference fields.

        Returns:
            Synthetic five-hit retrieval function.
        """
        assert records == corpus

        def retrieve(query: str, paper: str, count: int) -> list:
            """Return fixed distinct hits and retain the observed query contract.

            Args:
                query: Query text only.
                paper: Selected paper identifier.
                count: Required passage count.

            Returns:
                Ranked synthetic IDs and scores.
            """
            queries.append((query, paper, count))
            return [(f"p{i}", 5.0 - i) for i in range(5)]

        return retrieve

    monkeypatch.setattr(
        "src.data.build_annotation_pool.make_retriever_factory",
        lambda settings: factory,
    )
    question = {"question_id": "q", "paper_id": "paper", "question": "Question?"}
    gold = {
        "q": {
            **question,
            "gold_passage_ids": ["p1"],
            "evidence_paragraphs": [{"text": "secret evidence"}],
        }
    }
    blind, verification = generate_pairs(
        [question], corpus, gold, {"paper": "Real title"}
    )
    assert queries == [("Question?", "paper", 5)]
    assert len(blind) == 5
    assert all(row["label"] is None for row in blind)
    assert not {
        "score",
        "rank",
        "retrieval_method",
        "gold_passage_ids",
        "evidence_paragraphs",
    } & set(blind[0])
    assert [row["gold_evidence_match"] for row in verification] == [
        False,
        True,
        False,
        False,
        False,
    ]
    with pytest.raises(ValueError, match="query and gold"):
        generate_pairs(
            [{**question, "question": "Changed?"}],
            corpus,
            gold,
            {"paper": "Real title"},
        )


def test_markdown_batches_preserve_global_mapping(tmp_path: Path) -> None:
    """Split 1,000 pairs into ten batches per independent annotator slot.

    Source headings stay quoted so they cannot masquerade as record sections.
    """
    rows = [
        {
            "record_number": number,
            "question_id": f"q{(number - 1) // 5}",
            "paper_id": "paper_private",
            "passage_id": f"private{number}",
            "paper_title": "Full Paper Title",
            "question": "What?",
            "passage": "Text\n## Record fake",
            "label": None,
        }
        for number in range(1, 1001)
    ]
    render_batches(rows, tmp_path)
    for slot in ("A", "B"):
        paths = sorted((tmp_path / f"annotator_{slot}").glob("*.md"))
        assert len(paths) == 10
        for index, path in enumerate(paths):
            text = path.read_text(encoding="utf-8")
            assert text.count("\n## Record ") == 100
            assert text.count("\nLabel: \n") == 100
            assert f"## Record {index * 100 + 1:04d}" in text
            assert f"## Record {(index + 1) * 100:04d}" in text
            assert "Paper: Full Paper Title" in text
            assert "paper_private" not in text
            assert "private1" not in text
            assert "> ## Record fake" in text
            assert "Notes" not in text
        assert (
            paths[0].read_bytes()
            == (tmp_path / "annotator_A" / paths[0].name).read_bytes()
        )


def test_snapshot_and_duplicate_guards(tmp_path: Path) -> None:
    """Reject changed frozen bytes and repeated question identifiers.

    These guards prevent silently replacing a list between freeze and export.
    """
    path = tmp_path / "tmp_input.jsonl"
    path.write_text("original\n", encoding="utf-8")
    hashes = snapshot([path])
    verify_snapshot(hashes)
    path.write_text("changed\n", encoding="utf-8")
    with pytest.raises(ValueError, match="frozen file changed"):
        verify_snapshot(hashes)
    with pytest.raises(ValueError, match="duplicate"):
        unique_rows([{"question_id": "q"}, {"question_id": "q"}], "question_id")


def test_freeze_uses_ids_and_excludes_prior_queries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Sample across splits with shared papers and preserve the exact saved draw.

    A deliberately small paper is ineligible even when its gold mapping exists.
    The completed pilot is synthetic; production checks its persisted hashes.
    """
    data, pilot = tmp_path / "data", tmp_path / "pilot"
    corpus = [{"paper_id": "shared"} for _ in range(5)]
    monkeypatch.setattr(
        "src.data.build_annotation_pool.load_corpus", lambda directory: corpus
    )
    monkeypatch.setattr(
        "src.data.build_annotation_pool.code_identity", lambda: {"source_sha256": {}}
    )
    questions = [
        {
            "question_id": f"q{i:03d}",
            "paper_id": "small" if i == 300 else "shared",
            "question": f"Synthetic {i}?",
            "source_split": ("train", "validation", "test")[i % 3],
        }
        for i in range(301)
    ]
    write_jsonl(data / "qa.jsonl", questions)
    write_jsonl(data / "gold_evidence_mapping_all_splits.jsonl", questions)
    write_jsonl(data / "qa_for_choosing_chunk_size.jsonl", questions[:5])
    preparation = {
        "inputs": snapshot([data / "qa.jsonl"]),
        "usage_audit": [],
        "excluded_question_ids": [q["question_id"] for q in questions[:20]],
        "seed": 20261028,
        "scope": ["train", "validation", "test"],
        "sampling_rule": "sorted IDs, seeded sample without replacement",
        "isolation": "question-level",
    }
    write_json(data / "annotation_preparation.manifest.json", preparation)
    write_json(
        pilot / "manifest.json",
        {
            "inputs": preparation["inputs"],
            "settings": SETTINGS,
            "outputs": {},
            "code": {"source_sha256": {}},
            "purpose": "development pilot",
            "pair_count": 25,
            "question_ids": [q["question_id"] for q in questions[:5]],
        },
    )
    freeze(data, pilot)
    saved = (data / "qa_for_held_out.jsonl").read_bytes()
    manifest = json.loads(
        (data / "qa_for_held_out.manifest.json").read_text(encoding="utf-8")
    )
    assert len(manifest["question_ids"]) == len(set(manifest["question_ids"])) == 200
    assert not set(manifest["question_ids"]) & set(preparation["excluded_question_ids"])
    assert "q300" not in manifest["question_ids"]
    assert set(manifest["source_split_counts"]) == {"train", "validation", "test"}
    with pytest.raises(FileExistsError, match="never resample"):
        freeze(data, pilot)
    assert (data / "qa_for_held_out.jsonl").read_bytes() == saved
