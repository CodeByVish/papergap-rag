from __future__ import annotations

import pytest

from scripts.build_sample_passages import PassageGroup, select_groups


def _group(
    paper_id: str,
    section_index: int,
    count: int,
    *,
    split: str = "train",
) -> PassageGroup:
    passages = tuple(object() for _ in range(count))
    return PassageGroup(
        source_split=split,
        project_role="development" if split == "train" else "validation",
        paper_id=paper_id,
        source_kind="full_text",
        section_index=section_index,
        passages=passages,  # type: ignore[arg-type]
    )


def test_selection_hits_exact_target_with_complete_containers() -> None:
    groups = [
        _group("paper-a", 0, 40),
        _group("paper-b", 0, 30),
        _group("paper-c", 0, 20),
        _group("paper-d", 0, 10),
    ]

    selected = select_groups(groups, target_count=100)

    assert sum(len(group.passages) for group in selected) == 100
    assert {group.paper_id for group in selected} == {
        "paper-a",
        "paper-b",
        "paper-c",
        "paper-d",
    }


def test_selection_uses_at_most_one_container_per_paper() -> None:
    groups = [
        _group("paper-a", 0, 60),
        _group("paper-a", 1, 40),
        _group("paper-b", 0, 50),
        _group("paper-c", 0, 50),
    ]

    selected = select_groups(groups, target_count=100)

    assert len(selected) == 2
    assert len({group.paper_id for group in selected}) == 2
    assert sum(len(group.passages) for group in selected) == 100


def test_selection_fails_when_complete_containers_cannot_sum_to_target() -> None:
    with pytest.raises(ValueError, match="could not select"):
        select_groups([_group("paper-a", 0, 3)], target_count=4)
