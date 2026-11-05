"""Exercise persisted formal-pool verification with synthetic retrieval results.

These tests ensure malformed cross-file mappings cannot be accepted merely
because a saved output manifest contains plausible counts.
"""

import copy
import os
import sys

import pytest

from src.data import build_common_pool
from src.data.build_common_pool import run, validate_pool
from src.data.build_multi_retriever_pilot import pool_rankings
from tests.data.test_multi_retriever_pilot import fixture_pool


def test_saved_rankings_reconstruct_unique_pairs():
    """Accept full native rankings and count each union member once.

    The fixture includes two-way overlap, three-way overlap and unique hits.
    """
    questions, corpus, retrievers, _ = fixture_pool()
    pairs, rankings = pool_rankings(questions, corpus, retrievers)
    result = validate_pool(questions, corpus, pairs, rankings)
    assert result["pair_count"] == 9
    assert result["ranking_count"] == 3
    assert result["pair_count_range"] == [9, 9]


@pytest.mark.parametrize(
    "damage", ["duplicate", "missing", "rank", "mapping", "score", "label", "text"]
)
def test_reject_inconsistent_saved_pool(damage):
    """Reject damaged rankings, labels and source projections independently.

    Args:
        damage: Cross-file invariant to corrupt while retaining plausible sizes.
    """
    questions, corpus, retrievers, _ = fixture_pool()
    pairs, rankings = pool_rankings(questions, corpus, retrievers)
    pairs, rankings = copy.deepcopy(pairs), copy.deepcopy(rankings)
    if damage == "duplicate":
        rankings.append(rankings[0])
    elif damage == "missing":
        rankings.pop()
    elif damage == "rank":
        rankings[0]["hits"][0]["rank"] = 2
    elif damage == "mapping":
        rankings[0]["hits"][0]["record_number"] = 2
    elif damage == "score":
        rankings[0]["hits"][0]["score"] = float("nan")
    elif damage == "label":
        pairs[0]["label"] = 1
    else:
        pairs[0]["passage"] = "altered"
    with pytest.raises(ValueError):
        validate_pool(questions, corpus, pairs, rankings)


def test_generation_refuses_existing_directory(tmp_path):
    """Preserve completed and partial versions before any retrieval begins.

    Args:
        tmp_path: Isolated existing directory supplied by pytest.
    """
    with pytest.raises(FileExistsError):
        run(tmp_path)


@pytest.mark.parametrize("previous", [None, "0"])
def test_cli_uses_development_offline_policy_and_restores_environment(
    monkeypatch, previous
):
    """Keep optional model probes offline and restore caller state on failure.

    Args:
        monkeypatch: Pytest environment and CLI isolation fixture.
        previous: Absent or explicitly disabled prior offline setting.
    """
    if previous is None:
        monkeypatch.delenv("HF_HUB_OFFLINE", raising=False)
    else:
        monkeypatch.setenv("HF_HUB_OFFLINE", previous)
    monkeypatch.setattr(sys, "argv", ["build_common_pool", "run"])

    def fail_without_loading_model(output):
        """Observe the pre-import environment without model side effects.

        Args:
            output: Default new output path passed by the CLI.
        """
        assert output == build_common_pool.DEFAULT_OUTPUT
        assert os.environ["HF_HUB_OFFLINE"] == "1"
        raise RuntimeError("synthetic loading failure")

    monkeypatch.setattr(build_common_pool, "run", fail_without_loading_model)
    with pytest.raises(RuntimeError, match="synthetic"):
        build_common_pool.main()
    assert os.environ.get("HF_HUB_OFFLINE") == previous
