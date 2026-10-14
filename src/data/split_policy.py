"""Proposed paper-disjoint mapping for the official QASPER splits."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from types import MappingProxyType
from typing import Literal, TypeAlias, cast

SPLIT_POLICY_VERSION = "qasper-official-paper-disjoint-v0-proposed"

OfficialSplit: TypeAlias = Literal["train", "validation", "test"]
ProjectRole: TypeAlias = Literal["development", "validation", "held_out"]
DataAsset: TypeAlias = Literal["paper_text", "question", "answer", "label"]
DataUsePurpose: TypeAlias = Literal[
    "index_for_inference",
    "tuning",
    "prompt_design",
    "chunk_selection",
    "final_evaluation",
]

OFFICIAL_SPLITS: tuple[OfficialSplit, ...] = ("train", "validation", "test")
PROJECT_ROLES: tuple[ProjectRole, ...] = (
    "development",
    "validation",
    "held_out",
)
DATA_ASSETS: tuple[DataAsset, ...] = (
    "paper_text",
    "question",
    "answer",
    "label",
)
DATA_USE_PURPOSES: tuple[DataUsePurpose, ...] = (
    "index_for_inference",
    "tuning",
    "prompt_design",
    "chunk_selection",
    "final_evaluation",
)
HELD_OUT_USAGE_POLICY: Mapping[str, object] = MappingProxyType(
    {
        "index_paper_text": True,
        "forbidden_purposes": (
            "tuning",
            "prompt_design",
            "chunk_selection",
        ),
        "require_frozen_for_final_evaluation": True,
    }
)
OFFICIAL_TO_PROJECT_ROLE: Mapping[OfficialSplit, ProjectRole] = MappingProxyType(
    {
        "train": "development",
        "validation": "validation",
        "test": "held_out",
    }
)


def _build_data_use_matrix() -> Mapping[
    ProjectRole, Mapping[DataAsset, frozenset[DataUsePurpose]]
]:
    """Build the explicit asset-purpose matrix used by the policy guard."""

    development_validation = MappingProxyType(
        {
            asset: frozenset(
                {
                    "index_for_inference",
                    "tuning",
                    "prompt_design",
                    "chunk_selection",
                    "final_evaluation",
                }
            )
            for asset in DATA_ASSETS
        }
    )
    held_out = MappingProxyType(
        {
            "paper_text": frozenset({"index_for_inference"}),
            "question": frozenset({"final_evaluation"}),
            "answer": frozenset({"final_evaluation"}),
            "label": frozenset({"final_evaluation"}),
        }
    )
    return MappingProxyType(
        {
            "development": development_validation,
            "validation": development_validation,
            "held_out": held_out,
        }
    )


DATA_USE_MATRIX = _build_data_use_matrix()


def _require_clean_string(value: object, *, field_name: str) -> str:
    """Return a non-blank string without changing its value."""

    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    if value == "":
        raise ValueError(f"{field_name} must not be empty")
    if value.strip() == "":
        raise ValueError(f"{field_name} must not be blank")
    if value != value.strip():
        raise ValueError(
            f"{field_name} must not have leading or trailing whitespace"
        )
    return value


def project_role_for_official_split(name: object) -> ProjectRole:
    """Return the exact project role assigned to one official split."""

    official_split = _require_clean_string(name, field_name="official split")
    if official_split not in OFFICIAL_TO_PROJECT_ROLE:
        raise ValueError(f"unknown official split: {official_split!r}")
    return OFFICIAL_TO_PROJECT_ROLE[official_split]  # type: ignore[return-value]


def _data_use_request_text(
    *,
    project_role: object,
    asset: object,
    purpose: object,
) -> str:
    """Return a stable description for data-use errors."""

    return (
        "data use request rejected: "
        f"role={project_role!r}, asset={asset!r}, purpose={purpose!r}"
    )


def _require_data_use_value(
    value: object,
    *,
    field_name: str,
    allowed_values: tuple[str, ...],
    request_text: str,
) -> str:
    """Validate a policy literal without normalizing or guessing aliases."""

    if not isinstance(value, str) or value not in allowed_values:
        raise ValueError(
            f"{request_text}; invalid {field_name}, expected one of "
            f"{allowed_values!r}"
        )
    return value


def assert_data_use_allowed(
    *,
    project_role: object,
    asset: object,
    purpose: object,
    evaluation_frozen: object,
) -> None:
    """Reject data uses that violate the explicit split-policy matrix.

    The caller must state the evaluation-freeze state explicitly. This pure
    function does not inspect dates, branches, files, environment variables,
    or any other mutable project state.
    """

    request_text = _data_use_request_text(
        project_role=project_role,
        asset=asset,
        purpose=purpose,
    )
    role_value = _require_data_use_value(
        project_role,
        field_name="project role",
        allowed_values=PROJECT_ROLES,
        request_text=request_text,
    )
    asset_value = _require_data_use_value(
        asset,
        field_name="asset",
        allowed_values=DATA_ASSETS,
        request_text=request_text,
    )
    purpose_value = _require_data_use_value(
        purpose,
        field_name="purpose",
        allowed_values=DATA_USE_PURPOSES,
        request_text=request_text,
    )
    if type(evaluation_frozen) is not bool:
        raise TypeError(
            f"{request_text}; evaluation_frozen must be a boolean, "
            f"got {evaluation_frozen!r}"
        )

    typed_role = cast(ProjectRole, role_value)
    typed_asset = cast(DataAsset, asset_value)
    typed_purpose = cast(DataUsePurpose, purpose_value)
    allowed_purposes = DATA_USE_MATRIX[typed_role][typed_asset]
    if typed_purpose not in allowed_purposes:
        raise ValueError(
            f"{request_text}; this asset-purpose combination is not allowed"
        )
    if (
        typed_role == "held_out"
        and typed_purpose == "final_evaluation"
        and evaluation_frozen is not True
    ):
        raise ValueError(
            f"{request_text}; held-out final evaluation requires "
            "evaluation_frozen=True"
        )


def validate_paper_disjoint_splits(
    paper_ids_by_split: Mapping[object, object],
) -> None:
    """Validate exact official split keys and paper-level disjointness.

    The function validates only the supplied values. It does not read files,
    consult configuration, or infer a split from a paper, question, or passage.
    """

    if not isinstance(paper_ids_by_split, Mapping):
        raise TypeError("paper_ids_by_split must be a mapping")

    expected_keys = set(OFFICIAL_SPLITS)
    actual_keys = set(paper_ids_by_split)
    if actual_keys != expected_keys:
        missing = tuple(
            split for split in OFFICIAL_SPLITS if split not in paper_ids_by_split
        )
        extra = tuple(
            sorted(
                repr(key)
                for key in paper_ids_by_split
                if key not in expected_keys
            )
        )
        raise ValueError(
            "paper_ids_by_split keys must be exactly "
            f"{OFFICIAL_SPLITS!r}; missing={missing!r}; extra={extra!r}"
        )

    owner_by_paper_id: dict[str, OfficialSplit] = {}
    for split in OFFICIAL_SPLITS:
        paper_ids = paper_ids_by_split[split]
        if (
            isinstance(paper_ids, (str, bytes, Mapping))
            or not isinstance(paper_ids, Iterable)
        ):
            raise TypeError(
                f"paper IDs for split {split!r} must be an iterable of strings"
            )

        seen_in_split: set[str] = set()
        for paper_id in paper_ids:
            clean_paper_id = _require_clean_string(
                paper_id,
                field_name=f"paper ID in split {split!r}",
            )
            if clean_paper_id in seen_in_split:
                raise ValueError(
                    f"duplicate paper ID in split {split!r}: "
                    f"{clean_paper_id!r}"
                )
            seen_in_split.add(clean_paper_id)

            previous_split = owner_by_paper_id.get(clean_paper_id)
            if previous_split is not None:
                raise ValueError(
                    "paper ID appears in multiple official splits: "
                    f"{clean_paper_id!r} ({previous_split!r}, {split!r})"
                )
            owner_by_paper_id[clean_paper_id] = split
