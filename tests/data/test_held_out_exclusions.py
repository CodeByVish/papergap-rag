"""Exercise exclusion identity checks and lossless provenance merging.

Synthetic cases cover overlaps and invalid source records without requiring
network access, historical runs or retrieval model dependencies.
"""

import pytest

from src.data.build_held_out_exclusions import index_questions, merge_sources


def test_merge_preserves_all_owner_provenance() -> None:
    """Keep overlapping uses, original metadata and canonical unmodified text.

    Both owners must remain represented for the same question after deduplication.
    """
    qa = [{"question_id": "q", "paper_id": "p", "question": " Original? ", "source_split": "train", "answers": ["private"]}]
    original = {"question_id": "q", "paper_id": "p", "source_split": "train", "sources": ["missing-history.json"], "usage_categories": ["tuning"]}
    sources = [{"source_id": owner, "records": [dict(original)], "usage": "designated", "reason": "owner"} for owner in ["P1", "P2"]]
    rows = merge_sources(qa, sources)
    assert len(rows) == 1
    assert rows[0]["question"] == " Original? "
    assert "answers" not in rows[0]
    assert [item["source_id"] for item in rows[0]["sources"]] == ["P1", "P2"]
    assert all(item["original_record"] == original for item in rows[0]["sources"])


@pytest.mark.parametrize("field,value", [("paper_id", "wrong"), ("source_split", "test"), ("question", "changed")])
def test_reject_identity_mismatch(field: str, value: str) -> None:
    """Reject disagreement rather than silently replacing delivered identity.

    Args:
        field: Canonical field deliberately corrupted in the source record.
        value: Conflicting delivered value.
    """
    qa = [{"question_id": "q", "paper_id": "p", "question": "Query?", "source_split": "train"}]
    source = {"source_id": "P1", "records": [{"question_id": "q", field: value}], "usage": "development", "reason": "owner"}
    with pytest.raises(ValueError, match="identity mismatch"):
        merge_sources(qa, [source])


def test_reject_unknown_missing_and_duplicate_ids() -> None:
    """Fail closed for unknown IDs, duplicates and incomplete canonical rows.

    No invalid record may disappear silently during indexing or joining.
    """
    for rows in [[{}], [{"question_id": ""}], [{"question_id": "q"}] * 2]:
        with pytest.raises(ValueError, match="missing or duplicate"):
            index_questions(rows)
    source = {"source_id": "P1", "records": [{"question_id": "q"}], "usage": "development", "reason": "owner"}
    with pytest.raises(ValueError, match="unknown"):
        merge_sources([], [source])
    with pytest.raises(ValueError, match="incomplete"):
        merge_sources([{"question_id": "q"}], [source])
