import json

import pytest

from scripts.make_dev_items import build_items, spread
from scripts.run_agent_experiment import load_items_jsonl


def write(path, rows):
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return path


def passage(pid, paper):
    return {"passage_id": pid, "paper_id": paper}


def mapping_row(qid, paper, split, gold):
    return {"question_id": qid, "question": f"q {qid}?", "paper_id": paper,
            "source_split": split, "gold_passage_ids": gold}


def qa_row(qid, paper, split, unanswerable):
    return {"question_id": qid, "question": f"q {qid}?", "paper_id": paper, "source_split": split,
            "answers": [{"answer": {"unanswerable": unanswerable}}]}


@pytest.fixture()
def files(tmp_path):
    passages = write(tmp_path / "passages.jsonl", [
        passage("a1", "pa"), passage("a2", "pa"), passage("b1", "pb"), passage("c1", "pc"),
    ])
    mapping = write(tmp_path / "mapping.jsonl", [
        mapping_row("q1", "pa", "train", ["a1"]),
        mapping_row("q2", "pa", "train", ["a2"]),         # same paper: only one is kept
        mapping_row("q3", "pb", "train", ["b1"]),
        mapping_row("q4", "pc", "validation", ["c1"]),    # other split
        mapping_row("q5", "pz", "train", ["z1"]),         # paper not in the corpus
    ])
    qa = write(tmp_path / "qa.jsonl", [
        qa_row("u1", "pa", "train", True),
        qa_row("u2", "pb", "train", True),
        qa_row("q1", "pa", "train", False),
    ])
    return mapping, passages, qa


def test_items_carry_mapped_gold_and_unanswerable_questions_carry_none(files, tmp_path):
    items = build_items(*files, "train", answerable=2, unanswerable=1)
    by_id = {i["question_id"]: i for i in items}
    assert by_id["q1"]["gold_passage_ids"] == ["a1"] and by_id["q3"]["gold_passage_ids"] == ["b1"]
    assert "q2" not in by_id and "q4" not in by_id and "q5" not in by_id
    unanswerable = [i for i in items if not i["answerable"]]
    assert len(unanswerable) == 1 and "gold_passage_ids" not in unanswerable[0]

    out = write(tmp_path / "items.jsonl", items)
    loaded = load_items_jsonl(out)  # the runner accepts the file as written
    assert len(loaded) == 3 and sum(bool(i.gold_passage_ids) for i in loaded) == 2


def test_mapping_built_on_other_chunking_is_rejected(files, tmp_path):
    mapping, _, qa = files
    other = write(tmp_path / "other.jsonl", [passage("x1", "pa"), passage("x2", "pb")])
    with pytest.raises(ValueError, match="different chunking"):
        build_items(mapping, other, qa, "train", answerable=1, unanswerable=0)


def test_test_split_is_refused(files):
    with pytest.raises(ValueError, match="test split is refused"):
        build_items(*files, "test", answerable=1, unanswerable=0)


def test_asking_for_more_questions_than_papers_is_an_error():
    rows = [{"question_id": "q", "paper_id": "p"}]
    with pytest.raises(ValueError, match="only 1 papers"):
        spread(rows, 2)
