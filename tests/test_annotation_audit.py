import json

import pytest

from scripts.audit_annotation_batches import audit


def fake_git(monkeypatch, value="0"):
    def read(args, **kwargs):
        if args[1] == "rev-parse":
            return "abc\n"
        path = args[-1]
        if path.endswith("pairs.jsonl"):
            return (
                "\n".join(
                    json.dumps(
                        {
                            "record_number": i,
                            "question_id": str(i),
                            "passage_id": str(i),
                        }
                    )
                    for i in range(1, 11)
                )
            ).encode()
        number = int(path.rsplit("_", 1)[1].split(".")[0])
        label = value if "annotator_B" in path and number == 10 else "1"
        return f"#### Relevance {number}\n\nLabel: {label}\n".encode()

    monkeypatch.setattr(
        "scripts.audit_annotation_batches.subprocess.check_output", read
    )


def test_conflict_does_not_become_gold(monkeypatch):
    fake_git(monkeypatch)
    result = audit("test")
    assert result["observed_label_agreement"] == 0.9
    assert result["disagreements"][0]["record_number"] == 10
    assert not result["ready_for_final_scoring"]


def test_missing_is_not_negative(monkeypatch):
    fake_git(monkeypatch, "")
    result = audit("test")
    assert result["missing_judgments"] == 1
    assert result["paired_records"] == 9
    assert not result["all_labels_present"]


def test_invalid_label_rejected(monkeypatch):
    fake_git(monkeypatch, "2")
    with pytest.raises(ValueError):
        audit("test")
