"""Test held-out eligibility and retirement boundaries with synthetic IDs.

Cases cover cross-split sampling, exclusion precedence, immutable artifacts and
refusal to run the retired BM25-only path without downloading models.
"""

from collections import Counter
from pathlib import Path

import pytest

from src.data.build_annotation_pool import export_pool, freeze
from src.data.freeze_held_out import draw_ids, eligible_ids, write_new


def test_eligibility_uses_all_splits_and_bans_before_size() -> None:
    """Keep qualified historical IDs and all splits with enough passages.

    A banned question is recorded once even when its paper is too small.
    """
    rows = [
        {"question_id": "old", "paper_id": "p", "source_split": "train"},
        {"question_id": "v", "paper_id": "p", "source_split": "validation"},
        {"question_id": "t", "paper_id": "q", "source_split": "test"},
        {"question_id": "banned", "paper_id": "small", "source_split": "test"},
        {"question_id": "short", "paper_id": "small", "source_split": "train"},
    ]
    eligible, rejected = eligible_ids(rows, {"banned"}, Counter(p=5, q=6, small=4), 5)
    assert eligible == ["old", "t", "v"]
    assert rejected == {"banned": ["banned"], "fewer_than_minimum_passages": ["short"]}


def test_draw_is_order_independent_and_without_replacement() -> None:
    """Use only the predeclared seed and unique IDs to determine saved order.

    Reversing source-file order must not change the frozen draw.
    """
    candidates = [f"q{i:03d}" for i in range(300)]
    selected = draw_ids(candidates, 2026102805, 200)
    assert selected == draw_ids(list(reversed(candidates)), 2026102805, 200)
    assert len(set(selected)) == 200
    assert set(selected) <= set(candidates)


def test_invalid_candidates_fail_closed() -> None:
    """Reject duplicates, missing identity and an insufficient candidate pool.

    These cases must fail before writing either member of a frozen version.
    """
    row = {"question_id": "q", "paper_id": "p", "source_split": "test"}
    for rows in ([row, row], [{"question_id": "q", "paper_id": "p"}]):
        with pytest.raises(ValueError):
            eligible_ids(rows, set(), Counter(p=5), 5)
    for candidates in (["q"], ["q", "q"]):
        with pytest.raises(ValueError):
            draw_ids(candidates, 1, 2)


def test_retirement_blocks_legacy_writes(tmp_path: Path) -> None:
    """Stop historical freeze and formal export before any input is opened.

    Args:
        tmp_path: Isolated data directory supplied by pytest.
    """
    (tmp_path / "historical_bm25_retirement.manifest.json").write_text(
        "{}", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="retired"):
        freeze(tmp_path, tmp_path / "pilot")
    with pytest.raises(ValueError, match="retired"):
        export_pool(tmp_path, tmp_path / "output")
    assert not (tmp_path / "output").exists()


def test_new_artifact_never_overwrites_history(tmp_path: Path) -> None:
    """Preserve exact existing bytes when generation is accidentally repeated.

    Args:
        tmp_path: Isolated output directory supplied by pytest.
    """
    path = tmp_path / "questions.jsonl"
    write_new(path, b"historical\r\n")
    with pytest.raises(FileExistsError):
        write_new(path, b"replacement\n")
    assert path.read_bytes() == b"historical\r\n"
