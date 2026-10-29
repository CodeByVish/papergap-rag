"""Check four-method pooling and projection independently of real model scores.

The additional system can introduce new pairs or share any original result;
neither case may lose native rankings or leak private fields to annotation.
"""

import copy

import pytest

from src.data import build_annotation_pool, build_four_method_pool
from src.data.build_common_pool import validate_pool
from src.data.build_multi_retriever_pilot import (
    FOUR_METHODS,
    pool_rankings,
    render_multi_batches,
)
from src.data.export_common_annotations import IDENTITY_INSTRUCTION, validate_views
from tests.data.test_multi_retriever_pilot import fixture_pool


def four_fixture():
    """Add one reranker-exclusive passage to the original overlap fixture.

    Returns:
        Questions, corpus and four callbacks with their frozen display names.
    """
    questions, corpus, original, _ = fixture_pool()
    corpus.append({**corpus[0], "passage_id": "secret_extra", "text": "New evidence"})

    def reranked(query, paper_id, top_k):
        """Return four shared candidates and one newly introduced result.

        Args:
            query: Original query, unused by this deterministic fixture.
            paper_id: Original paper scope, unused by this fixture.
            top_k: Required complete output depth.

        Returns:
            Five native raw-logit scores, including valid negative values.
        """
        assert top_k == 5
        return [
            (pid, float(-i))
            for i, pid in enumerate(
                ["secret_extra", "secret_p0", "secret_p1", "secret_p2", "secret_p3"]
            )
        ]

    callbacks = dict(zip(FOUR_METHODS, [*original.values(), reranked]))
    return questions, corpus, callbacks


def test_four_method_union_and_english_views(tmp_path):
    """Retain a new fourth-method pair, shared attribution and all five groups.

    Args:
        tmp_path: Independent two-slot export directory.
    """
    questions, corpus, callbacks = four_fixture()
    pairs, rankings = pool_rankings(questions, corpus, callbacks, FOUR_METHODS)
    result = validate_pool(questions, corpus, pairs, rankings, FOUR_METHODS)
    assert result["pair_count"] == 10 and result["ranking_count"] == 4
    assert pairs[-1]["retrieved_by"] == [FOUR_METHODS[-1]]
    assert pairs[0]["retrieved_by"] == list(FOUR_METHODS)
    render_multi_batches(pairs, tmp_path, FOUR_METHODS)
    for path in tmp_path.rglob("*.md"):
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "Annotator: \n\n", f"Annotator: \n\n{IDENTITY_INSTRUCTION}\n\n"
            ),
            encoding="utf-8",
        )
    assert validate_views(pairs, tmp_path, FOUR_METHODS)[0]["pair_count"] == 10
    text = (tmp_path / "annotator_A/batch_01.md").read_text(encoding="utf-8")
    assert "secret_" not in text
    assert f"### {FOUR_METHODS[-1]}\n" in text
    assert "New evidence" in text


@pytest.mark.parametrize("damage", ["missing", "foreign", "rank", "label"])
def test_fourth_method_corruption_rejected(damage):
    """Reject corruption affecting the new method despite valid old rankings.

    Args:
        damage: Missing list, wrong-paper passage, native rank or filled label.
    """
    questions, corpus, callbacks = four_fixture()
    pairs, rankings = pool_rankings(questions, corpus, callbacks, FOUR_METHODS)
    pairs, rankings = copy.deepcopy(pairs), copy.deepcopy(rankings)
    if damage == "missing":
        rankings.pop()
    elif damage == "foreign":
        corpus[-1]["paper_id"] = "other_paper"
    elif damage == "rank":
        rankings[-1]["hits"][0]["rank"] = 5
    else:
        pairs[-1]["label"] = 1
    with pytest.raises(ValueError):
        validate_pool(questions, corpus, pairs, rankings, FOUR_METHODS)


def test_archived_fallback_checks_exact_bytes(monkeypatch, tmp_path):
    """Read deleted legacy blobs while preferring current bytes and strict hashes.

    Args:
        monkeypatch: Isolate Git responses and the current working directory.
        tmp_path: Empty synthetic checkout without legacy working files.
    """
    import hashlib
    from pathlib import Path

    monkeypatch.chdir(tmp_path)
    path = Path("data/processed/annotation_pilot_multi_v2/frozen_config.json")

    def git_output(command, **kwargs):
        """Provide one archived blob without invoking external Git.

        Args:
            command: Git log or show command composed by the reader.
            **kwargs: Text decoding options for the commit query.

        Returns:
            A pinned commit name or its exact historical JSON bytes.
        """
        return "a" * 40 if command[1] == "log" else b'{"original": true}\n'

    monkeypatch.setattr(build_annotation_pool.subprocess, "check_output", git_output)
    digest = hashlib.sha256(b'{"original": true}\n').hexdigest()
    build_annotation_pool.verify_snapshot({path.as_posix(): digest})
    assert not path.exists()
    path.parent.mkdir(parents=True)
    path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="frozen file changed"):
        build_annotation_pool.verify_snapshot({path.as_posix(): digest})
    with pytest.raises(FileNotFoundError):
        build_annotation_pool.artifact_bytes(Path("data/processed/current_input.json"))


def test_original_rank_change_stops_export(monkeypatch):
    """Reject a plausible replacement top-five from an original algorithm.

    Args:
        monkeypatch: Replace historical ranking loading with synthetic records.
    """
    questions, corpus, callbacks = four_fixture()
    _, rankings = pool_rankings(questions, corpus, callbacks, FOUR_METHODS)
    original = copy.deepcopy(rankings[:3])
    original[2]["method"] = "Hybrid"
    monkeypatch.setattr(build_four_method_pool, "read_jsonl", lambda path: original)
    rankings[0]["hits"][0]["passage_id"] = "changed_valid_id"
    with pytest.raises(ValueError, match="original native IDs/ranks differ"):
        build_four_method_pool.compare_history(rankings)
