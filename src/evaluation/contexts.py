"""Reconstruct P5 rendered evidence only under an explicitly reviewed prompt configuration."""

from src.evaluation.common import index_rows
from src.evaluation.qa import prediction


def reconstruct_contexts(rows, config, expected_version, review_note):
    from src.generation.adapters.retrieval import build_request
    from src.generation.prompts.grounded_qa import (
        PROMPT_VERSION,
        PromptConfig,
        format_passage,
        select_passages,
    )

    if not review_note.strip() or expected_version != PROMPT_VERSION:
        raise ValueError(
            "Reviewed configuration and matching checked-out prompt version required"
        )
    if set(config) != set(PromptConfig.model_fields):
        raise ValueError(
            "Supply every original PromptConfig field; no implicit defaults"
        )
    index_rows(rows)
    prompt = PromptConfig.model_validate(config)
    result = []
    for row in rows:
        _, status = prediction(row)
        if status != "answered":
            continue
        envelope = row.get("answer", row)
        actual_version = envelope.get("generation", {}).get("prompt_version")
        if actual_version != expected_version:
            raise ValueError("Saved generation prompt version differs or is missing")
        # Requires original retriever/agent input, not only the five-key answer object.
        adapted = build_request(row)
        if adapted.report.dropped_total:
            raise ValueError("Context reconstruction dropped passages; inspect adapter")
        selected = select_passages(adapted.request, prompt)
        result.append(
            {
                "question_id": row["question_id"],
                "paper_id": row["paper_id"],
                "exact_rendered": True,
                "contexts": [
                    format_passage(i, p, prompt) for i, p in enumerate(selected, 1)
                ],
                "passage_ids": [p.passage_id for p in selected],
                "provenance": {
                    "method": "reconstructed_from_pinned_P5_renderer",
                    "prompt_version": expected_version,
                    "prompt_config": config,
                    "owner_review_note": review_note,
                },
            }
        )
    if not result:
        raise ValueError("No answered records with reconstructable contexts")
    return result
