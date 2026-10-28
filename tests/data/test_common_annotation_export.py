"""Check formal Markdown coverage and reject damaged annotation templates.

Synthetic records exercise native-rank ordering separately from record order,
multiline content, empty groups and a question crossing the batch boundary.
"""

from pathlib import Path

import pytest

from src.data.build_multi_retriever_pilot import render_multi_batches
from src.data.export_common_annotations import IDENTITY_INSTRUCTION, validate_views


def make_export(output: Path) -> list[dict]:
    """Create two slots for twenty-one synthetic questions with private fields.

    Args:
        output: Empty pytest directory for generated templates.

    Returns:
        Source records whose internal metadata must stay outside the views.
    """
    rows = []
    for question in range(21):
        for offset, (sources, rank) in enumerate(
            [(["BM25", "Dense", "Hybrid"], 1), (["BM25"], 3), (["BM25"], 2)]
        ):
            rows.append(
                {
                    "question_id": f"secret_question_{question}",
                    "paper_id": "secret_paper",
                    "passage_id": f"secret_passage_{offset}",
                    "record_number": len(rows) + 1,
                    "paper_title": "Real title",
                    "question": "Original question?\nSecond line?",
                    "passage": f"Text {offset}\n### Original heading",
                    "retrieved_by": sources,
                    "retrievals": [
                        {"method": source, "rank": rank, "score": 99.9}
                        for source in sources
                    ],
                    "display_group": "Common Retrieved Chunks"
                    if len(sources) > 1
                    else sources[0],
                    "label": None,
                    "gold_evidence": "secret_gold",
                }
            )
    render_multi_batches(rows, output)
    for path in output.rglob("*.md"):
        text = path.read_text(encoding="utf-8").replace(
            "Annotator: \n\n", f"Annotator: \n\n{IDENTITY_INSTRUCTION}\n\n"
        )
        path.write_text(text, encoding="utf-8")
    return rows


def test_coverage_and_projection(tmp_path: Path) -> None:
    """Retain whole questions, native exclusive order and independent copies.

    The last question gets its own batch; metadata cannot leak from extra keys.
    """
    rows = make_export(tmp_path)
    assert validate_views(rows, tmp_path) == [
        {"batch": 1, "question_count": 20, "pair_count": 60},
        {"batch": 2, "question_count": 1, "pair_count": 3},
    ]
    text = (tmp_path / "annotator_A/batch_01.md").read_text(encoding="utf-8")
    assert text.index("#### Passage 3\n") < text.index("#### Passage 2\n")
    assert "secret_" not in text and "99.9" not in text
    assert "### Dense\n\nNone" in text
    assert text == (tmp_path / "annotator_B/batch_01.md").read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "before,after",
    [
        ("#### Passage 1\n", "#### Passage 2\n"),
        ("Retrieved by: BM25, Dense, Hybrid", "Retrieved by: BM25"),
        ("Text 0", "Changed text"),
        ("Label: \n", "Label: 1\n"),
        ("### Dense\n\nNone", "### Dense\n\n"),
        ("Paper: Real title", "Paper: Fake title"),
        ("## Question 0001", "## Question 0002"),
    ],
)
def test_changed_views_rejected(tmp_path: Path, before: str, after: str) -> None:
    """Reject content and mapping damage even without consulting output hashes.

    Args:
        tmp_path: Isolated export directory.
        before: Valid source fragment to replace once.
        after: Invalid annotation or structure to inject.
    """
    rows = make_export(tmp_path)
    path = tmp_path / "annotator_B/batch_01.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(before, after, 1), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        validate_views(rows, tmp_path)


def test_missing_batch_rejected(tmp_path: Path) -> None:
    """Reject missing files rather than reporting partial coverage as complete.

    This guards independent slot coverage beyond the correctness of one file.
    """
    rows = make_export(tmp_path)
    (tmp_path / "annotator_B/batch_02.md").unlink()
    with pytest.raises(ValueError, match="batches"):
        validate_views(rows, tmp_path)
