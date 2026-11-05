# P2 annotation review, batches 08–10

These 563 judgments were produced by Codex (AI), not by a human annotator. They are suggestions for reviewing disagreements with separately completed human work, not ground truth or an accuracy benchmark. No other annotator labels or gold answers were consulted during labeling. Retrieval-source identities were visible in the templates.

The files are intentionally outside `annotation_common_v3_markdown/annotator_A` and `annotator_B`. Do not include them in human inter-annotator agreement, the manual-label count, adjudicated gold, or final evaluation labels. Preserve original independent human labels before any review. These judgments must not be used to tune retrieval on held-out data.

- `batch_08.md`: 191 labels; `batch_09.md`: 177; `batch_10.md`: 195.
- `batch_*.ai-review.md`: uncertain-case notes.
- `batch_*.ai-review.json`: per-record reasons and provenance.
- `manifest.json`: source template commit, counts and hashes.

Markdown question, passage and relevance numbers match the P3 templates. A label is 1 for useful answer evidence (including partial evidence), otherwise 0. Record numbers are export row numbers, not stable passage IDs. Join through P3's matching export/version.

See [the English data guide](../../README.md) or [中文数据指南](../../README_zh-CN.md) for acquisition and field definitions. The original blank templates are available at the manifest's source commit. The judgments were produced in an interactive Codex session, not by a deterministic generation script; fetching the committed artifact reproduces the exact bytes.
