"""Tests for the proposed official QASPER split policy."""

from __future__ import annotations

from pathlib import Path
from types import MappingProxyType

import pytest
import yaml

from src.data.split_policy import (
    DATA_ASSETS,
    DATA_USE_MATRIX,
    DATA_USE_PURPOSES,
    HELD_OUT_USAGE_POLICY,
    OFFICIAL_SPLITS,
    OFFICIAL_TO_PROJECT_ROLE,
    PROJECT_ROLES,
    SPLIT_POLICY_VERSION,
    assert_data_use_allowed,
    project_role_for_official_split,
    validate_paper_disjoint_splits,
)

ROOT = Path(__file__).resolve().parents[2]


def _valid_paper_ids() -> dict[str, list[str]]:
    """Return a small paper-level fixture with synthetic IDs only."""

    return {
        "train": ["paper-train-a", "paper-train-b"],
        "validation": ["paper-validation-a"],
        "test": ["paper-test-a", "paper-test-b"],
    }


def test_mapping_is_exact_and_immutable() -> None:
    assert OFFICIAL_SPLITS == ("train", "validation", "test")
    assert PROJECT_ROLES == ("development", "validation", "held_out")
    assert dict(OFFICIAL_TO_PROJECT_ROLE) == {
        "train": "development",
        "validation": "validation",
        "test": "held_out",
    }
    assert isinstance(OFFICIAL_TO_PROJECT_ROLE, MappingProxyType)
    with pytest.raises(TypeError):
        OFFICIAL_TO_PROJECT_ROLE["train"] = "held_out"  # type: ignore[index]


@pytest.mark.parametrize(
    ("official_split", "expected_role"),
    [
        ("train", "development"),
        ("validation", "validation"),
        ("test", "held_out"),
    ],
)
def test_project_role_mapping_is_exact(
    official_split: str,
    expected_role: str,
) -> None:
    assert project_role_for_official_split(official_split) == expected_role


@pytest.mark.parametrize(
    "invalid_split",
    [None, 1, "", "   ", " train", "train ", "dev", "DEV"],
)
def test_project_role_mapping_rejects_unknown_or_malformed_names(
    invalid_split: object,
) -> None:
    with pytest.raises((TypeError, ValueError), match="official split|unknown"):
        project_role_for_official_split(invalid_split)


def test_valid_paper_disjoint_input_passes_and_is_repeatable() -> None:
    paper_ids_by_split = _valid_paper_ids()

    assert validate_paper_disjoint_splits(paper_ids_by_split) is None
    assert validate_paper_disjoint_splits(paper_ids_by_split) is None


@pytest.mark.parametrize(
    "paper_ids_by_split",
    [
        {
            "train": ["paper-train-a"],
            "validation": ["paper-validation-a"],
        },
        {
            "train": ["paper-train-a"],
            "validation": ["paper-validation-a"],
            "test": ["paper-test-a"],
            "extra": ["paper-extra"],
        },
    ],
)
def test_split_keys_must_be_exact(paper_ids_by_split: dict[str, list[str]]) -> None:
    with pytest.raises(ValueError, match="keys must be exactly"):
        validate_paper_disjoint_splits(paper_ids_by_split)


def test_split_input_must_be_a_mapping() -> None:
    with pytest.raises(TypeError, match="must be a mapping"):
        validate_paper_disjoint_splits([])  # type: ignore[arg-type]


@pytest.mark.parametrize("duplicate_split", ["train", "validation", "test"])
def test_duplicate_paper_id_within_each_split_is_rejected(
    duplicate_split: str,
) -> None:
    paper_ids_by_split = _valid_paper_ids()
    paper_ids_by_split[duplicate_split] = ["paper-duplicate", "paper-duplicate"]

    with pytest.raises(
        ValueError,
        match=rf"duplicate paper ID in split '{duplicate_split}'",
    ):
        validate_paper_disjoint_splits(paper_ids_by_split)


@pytest.mark.parametrize(
    ("left_split", "right_split"),
    [
        ("train", "validation"),
        ("train", "test"),
        ("validation", "test"),
    ],
)
def test_cross_split_paper_overlap_is_rejected(
    left_split: str,
    right_split: str,
) -> None:
    paper_ids_by_split = _valid_paper_ids()
    paper_ids_by_split[right_split] = [paper_ids_by_split[left_split][0]]

    with pytest.raises(
        ValueError,
        match="paper ID appears in multiple official splits",
    ):
        validate_paper_disjoint_splits(paper_ids_by_split)


@pytest.mark.parametrize(
    "invalid_paper_id",
    [None, 1, "", "   ", " paper-id", "paper-id "],
)
def test_paper_ids_must_be_clean_strings(invalid_paper_id: object) -> None:
    paper_ids_by_split = _valid_paper_ids()
    paper_ids_by_split["train"] = [invalid_paper_id]  # type: ignore[list-item]

    with pytest.raises((TypeError, ValueError), match="paper ID in split"):
        validate_paper_disjoint_splits(paper_ids_by_split)


@pytest.mark.parametrize("invalid_values", [None, "paper-id", {"paper-id": 1}])
def test_paper_id_collection_must_be_an_iterable_of_ids(
    invalid_values: object,
) -> None:
    paper_ids_by_split = _valid_paper_ids()
    paper_ids_by_split["train"] = invalid_values  # type: ignore[assignment]

    with pytest.raises(TypeError, match="must be an iterable of strings"):
        validate_paper_disjoint_splits(paper_ids_by_split)


def test_config_matches_python_policy_and_keeps_held_out_manifest_unset() -> None:
    config_path = ROOT / "configs" / "default.yaml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    split_policy = config["data"]["split_policy"]

    assert split_policy["version"] == SPLIT_POLICY_VERSION
    assert split_policy["unit"] == "paper"
    assert split_policy["official_to_project_role"] == dict(
        OFFICIAL_TO_PROJECT_ROLE
    )
    held_out_usage = split_policy["held_out_usage"]
    assert tuple(DATA_ASSETS) == (
        "paper_text",
        "question",
        "answer",
        "label",
    )
    assert tuple(DATA_USE_PURPOSES) == (
        "index_for_inference",
        "tuning",
        "prompt_design",
        "chunk_selection",
        "final_evaluation",
    )
    assert set(DATA_USE_MATRIX) == set(PROJECT_ROLES)
    assert held_out_usage["index_paper_text"] is HELD_OUT_USAGE_POLICY[
        "index_paper_text"
    ]
    assert tuple(held_out_usage["forbidden_purposes"]) == tuple(
        HELD_OUT_USAGE_POLICY["forbidden_purposes"]
    )
    assert held_out_usage["require_frozen_for_final_evaluation"] is (
        HELD_OUT_USAGE_POLICY["require_frozen_for_final_evaluation"]
    )
    assert config["evaluation"]["held_out_manifest"] is None


@pytest.mark.parametrize(
    ("project_role", "asset", "purpose", "evaluation_frozen"),
    [
        ("development", "paper_text", "tuning", False),
        ("development", "question", "prompt_design", False),
        ("validation", "answer", "chunk_selection", False),
        ("validation", "label", "final_evaluation", False),
        ("held_out", "paper_text", "index_for_inference", False),
        ("held_out", "question", "final_evaluation", True),
        ("held_out", "answer", "final_evaluation", True),
        ("held_out", "label", "final_evaluation", True),
    ],
)
def test_allowed_data_uses_pass(
    project_role: str,
    asset: str,
    purpose: str,
    evaluation_frozen: bool,
) -> None:
    assert (
        assert_data_use_allowed(
            project_role=project_role,
            asset=asset,
            purpose=purpose,
            evaluation_frozen=evaluation_frozen,
        )
        is None
    )


@pytest.mark.parametrize("project_role", ["development", "validation"])
def test_development_validation_matrix_allows_every_declared_use(
    project_role: str,
) -> None:
    for asset in DATA_ASSETS:
        for purpose in DATA_USE_PURPOSES:
            assert_data_use_allowed(
                project_role=project_role,
                asset=asset,
                purpose=purpose,
                evaluation_frozen=False,
            )


@pytest.mark.parametrize("asset", DATA_ASSETS)
@pytest.mark.parametrize(
    "purpose",
    ["tuning", "prompt_design", "chunk_selection"],
)
def test_held_out_non_evaluation_uses_are_rejected(
    asset: str,
    purpose: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=r"role='held_out'.*asset=.*purpose=.*",
    ):
        assert_data_use_allowed(
            project_role="held_out",
            asset=asset,
            purpose=purpose,
            evaluation_frozen=False,
        )


@pytest.mark.parametrize("asset", ["question", "answer", "label"])
def test_held_out_final_evaluation_requires_an_explicit_freeze(
    asset: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="held-out final evaluation requires evaluation_frozen=True",
    ):
        assert_data_use_allowed(
            project_role="held_out",
            asset=asset,
            purpose="final_evaluation",
            evaluation_frozen=False,
        )


def test_held_out_paper_text_is_only_for_the_inference_index() -> None:
    with pytest.raises(
        ValueError,
        match=r"role='held_out'.*asset='paper_text'.*purpose='final_evaluation'",
    ):
        assert_data_use_allowed(
            project_role="held_out",
            asset="paper_text",
            purpose="final_evaluation",
            evaluation_frozen=True,
        )


@pytest.mark.parametrize(
    ("project_role", "asset", "purpose"),
    [
        ("development", "unknown", "tuning"),
        ("validation", "question", "unknown"),
        ("unknown", "question", "tuning"),
    ],
)
def test_unknown_data_use_literals_are_rejected(
    project_role: str,
    asset: str,
    purpose: str,
) -> None:
    with pytest.raises(
        ValueError,
        match=r"role=.*asset=.*purpose=.*",
    ):
        assert_data_use_allowed(
            project_role=project_role,
            asset=asset,
            purpose=purpose,
            evaluation_frozen=False,
        )


@pytest.mark.parametrize("evaluation_frozen", [None, 0, 1, "true"])
def test_evaluation_frozen_must_be_a_boolean(evaluation_frozen: object) -> None:
    with pytest.raises(
        TypeError,
        match=r"role='held_out'.*asset='question'.*purpose='final_evaluation'.*"
        r"evaluation_frozen must be a boolean",
    ):
        assert_data_use_allowed(
            project_role="held_out",
            asset="question",
            purpose="final_evaluation",
            evaluation_frozen=evaluation_frozen,
        )
