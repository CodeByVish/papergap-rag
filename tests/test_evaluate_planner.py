"""Tests for the planner/mapper evaluation, at paragraph level and at chunk level."""

import json

from scripts import evaluate_planner as ep

PARA_A = "Our model achieves 91 percent accuracy on the held out test set after training for ten epochs."
PARA_B = "We thank the anonymous reviewers for their detailed and helpful comments on this paper."
PARA_C = ("Training used the Adam optimiser with a small learning rate and early stopping on the "
          "development set while the batch size stayed fixed throughout every experiment we ran.")


def paper(evidence):
    return {
        "id": "p1",
        "full_text": [{"section_name": "Results", "paragraphs": [PARA_A]},
                      {"section_name": "Acknowledgments", "paragraphs": [PARA_B, PARA_C]}],
        "qas": [{"question": "What accuracy did the model achieve?",
                 "answers": [{"answer": {"unanswerable": False, "evidence": evidence}}]}],
    }


def test_gold_chunks_marks_a_whole_paragraph_and_ignores_others():
    chunks = [("Results", f"intro words {PARA_A} more words"), ("Other", PARA_B)]
    assert ep.gold_chunks(chunks, {PARA_A}) == {0}


def test_gold_chunks_marks_both_chunks_of_a_paragraph_that_straddles_them():
    words = PARA_C.split()
    first, second = " ".join(words[:18]), " ".join(words[10:])  # overlap, as in the 365/40 chunker
    chunks = [("Method", f"before. {first}"), ("Method", f"{second} after."), ("Method", "unrelated text")]
    assert ep.gold_chunks(chunks, {PARA_C}) == {0, 1}


def test_gold_chunks_ignores_whitespace_differences():
    assert ep.gold_chunks([("Results", PARA_A.replace(" ", "  \n"))], {PARA_A}) == {0}


def test_load_chunks_orders_by_chunk_number(tmp_path):
    path = tmp_path / "passages.jsonl"
    rows = [{"paper_id": "p1", "chunk_number": 2, "section": "B", "text": "second"},
            {"paper_id": "p1", "chunk_number": 1, "section": "A", "text": "first"},
            {"paper_id": "p2", "chunk_number": 1, "section": "C", "text": "other"}]
    path.write_text("\n".join(json.dumps(r) for r in rows))
    assert ep.load_chunks(path) == {"p1": [("A", "first"), ("B", "second")], "p2": [("C", "other")]}


def test_paragraph_level_counts_gold_and_matched_hard_negatives():
    total, types, by_type = ep.evaluate([paper([PARA_A])])
    assert total == 1 and types["result"] == 1
    n, gold, hard, matched = by_type["result"]
    assert n == 1 and gold == 1  # the Results section satisfies the plan
    assert hard == 0 and matched == 0  # the lookalikes sit in Acknowledgments with no result words


def test_chunk_level_uses_chunks_not_paragraphs():
    chunks = {"p1": [("Results", PARA_A), ("Acknowledgments", f"{PARA_B} {PARA_C}")]}
    total, _, by_type = ep.evaluate([paper([PARA_A])], chunks)
    assert total == 1 and by_type["result"][:2] == [1, 1]


def test_questions_without_gold_chunks_or_a_chunked_paper_are_skipped():
    _, _, by_type = ep.evaluate([paper([PARA_A])], {"other-paper": [("Results", PARA_A)]})
    assert not by_type
    _, _, by_type = ep.evaluate([paper(["text that is not a paragraph of the paper"])])
    assert not by_type


def test_matched_set_has_as_many_lookalikes_as_gold_units():
    # two gold paragraphs: 'any of two lookalikes' must be what is compared, not 'any of five'
    two = paper([PARA_A, PARA_B])
    _, _, by_type = ep.evaluate([two])
    n, gold, hard, matched = by_type["result"]
    assert n == 1 and matched <= hard
