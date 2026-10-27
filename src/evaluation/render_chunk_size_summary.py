"""Render chunk-size aggregate metrics as a standalone HTML comparison.

The report uses only summary data, works offline, and leaves JSON unchanged.
Per-question records and source text are deliberately omitted from the tables.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path
from typing import Any


def _table(
    title: str,
    rows: dict[str, dict[str, Any]],
    columns: list[tuple[str, str, bool]],
) -> str:
    """Render numerically ordered sizes with exact maximum-rate highlights.

    Args:
        title: Table caption.
        rows: Aggregate metrics keyed by chunk size in words.
        columns: Metric key, display label and whether higher is better.

    Returns:
        Escaped HTML with missing values distinct from numeric zero.
    """
    headers = '<th scope="col">Chunk size (words)</th>'
    cells: dict[str, list[str]] = {size: [] for size in rows}
    for key, label, maximize in columns:
        headers += f'<th scope="col">{escape(label)}</th>'
        values = {}
        for size, row in rows.items():
            metric = row.get(key)
            values[size] = metric.get("value") if isinstance(metric, dict) else metric
        available = [value for value in values.values() if value is not None]
        best = max(available) if maximize and available else None
        for size, row in rows.items():
            value = values[size]
            metric = row.get(key)
            details = ""
            if isinstance(metric, dict):
                details = f"{metric.get('numerator', 'N/A')} / {metric.get('denominator', 'N/A')}"
            if value is None:
                pending = metric.get("pending", 0) if isinstance(metric, dict) else 0
                display = f"Pending ({pending})" if pending else "N/A"
            else:
                display = str(value) if isinstance(value, int) else f"{value:.4f}"
            # Compare original values: rounding must not introduce artificial ties.
            style = ' class="best"' if best is not None and value == best else ""
            cells[size].append(
                f'<td{style} title="{escape(details, quote=True)}">{escape(display)}</td>'
            )
    body = "".join(
        f'<tr><th scope="row">{escape(size)}</th>{"".join(cells[size])}</tr>'
        for size in sorted(rows, key=int)
    )
    return (
        f'<div class="table-wrap"><table><caption>{escape(title)}</caption>'
        f"<thead><tr>{headers}</tr></thead><tbody>{body}</tbody></table></div>"
    )


def write_summary_html(run_dir: Path, summary: dict[str, Any] | None = None) -> Path:
    """Write an offline comparison beside a run's machine-readable summary.

    Args:
        run_dir: Existing experiment directory containing summary.json.
        summary: Current summary, or None to read the saved JSON without mutation.

    Returns:
        Path to the UTF-8 HTML report, replacing an older rendering if present.
    """
    if summary is None:
        summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
    sizes = summary["sizes"]
    tables = [
        _table(
            "Top-5 retrieval and readability",
            sizes,
            [
                ("evidence_hit_at_5", "Evidence Hit@5 (higher is better)", True),
                (
                    "complete_evidence_rate_at_5",
                    "Complete evidence rate@5 (higher is better)",
                    True,
                ),
                ("retrieved_word_count", "Mean retrieved words", False),
                (
                    "readability_pass_rate",
                    "Readability pass rate (higher is better)",
                    True,
                ),
                ("corpus_passage_count", "Corpus passages", False),
                ("index_seconds", "Index time (seconds)", False),
            ],
        )
    ]
    budgets = {budget for row in sizes.values() for budget in row.get("budgets", {})}
    for budget in sorted(budgets, key=int):
        rows = {
            size: row.get("budgets", {}).get(budget, {}) for size, row in sizes.items()
        }
        tables.append(
            _table(
                f"Word budget: {budget} words",
                rows,
                [
                    ("evidence_hit", "Evidence hit (higher is better)", True),
                    (
                        "complete_evidence_rate",
                        "Complete evidence rate (higher is better)",
                        True,
                    ),
                    ("actual_word_count", "Mean actual words", False),
                    ("question_count", "Questions", False),
                    ("corpus_exhausted_count", "Corpus exhausted (questions)", False),
                ],
            )
        )
    run_id = escape(str(summary.get("run_id", run_dir.name)))
    schema = escape(str(summary.get("schema_version", "N/A")))
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Chunk size comparison: {run_id}</title>
<style>
:root {{ --navy: #1F3864; --blue: #2F5496; --gray: #F2F2F2;
  --text: #333F50; --border: #D9D9D9; --white: #FFFFFF; --highlight: #DCE9FB; }}
body {{ font-family: "Times New Roman", SimSun, serif; font-size: 12pt;
  color: var(--text); margin: 2rem; line-height: 1.5; }}
h1, caption {{ color: var(--navy); }}
h1 {{ font-size: 22pt; }}
a {{ color: var(--blue); }}
.run-id {{ font-family: Consolas, monospace; }}
.metric-notes {{ background: var(--gray); border-left: 3px solid var(--blue);
  padding: .5rem 1rem; margin: 1rem 0; }}
.metric-notes p {{ margin: .5rem 0; }}
.table-wrap {{ overflow-x: auto; margin: 1.5rem 0; }}
table {{ border-collapse: collapse; width: 100%; }}
caption {{ text-align: left; font-weight: bold; font-size: 15pt; padding: .5rem 0; }}
th, td {{ border: 1px solid var(--border); padding: .6rem;
  text-align: center; vertical-align: middle; }}
thead {{ background: var(--navy); color: var(--white); }}
tbody tr:nth-child(even) {{ background: var(--gray); }}
td.best {{ background: var(--highlight); color: var(--navy); font-weight: bold; }}
@media print {{ body {{ margin: 0; }} .table-wrap {{ overflow: visible; }} }}
</style></head><body>
<h1>Chunk size comparison</h1>
<p>Run: <span class="run-id">{run_id}</span> | Schema: {schema} | Source: <a href="summary.json">summary.json</a></p>
<p>Rates use the 0–1 scale. Decimal values use four decimal places.
Blue bold cells mark the highest rate in each column, including exact ties.
Hover over aggregate values for numerator / denominator.
Pending means manual review is unfinished; N/A means unavailable.
Word counts and timings are descriptive and receive no best-value highlight.
Single-run timings do not establish a performance comparison.</p>
<aside class="metric-notes" aria-label="Metric notes">
<p><strong>Mean retrieved words:</strong> Mean total word count of the top-5
retrieved chunks per question (or all returned chunks if fewer than five).
Overlapping text is counted repeatedly.</p>
<p><strong>Corpus passages:</strong> Total number of chunks in the entire
experiment corpus for this chunk size, rather than the number retrieved for
one question. Smaller chunks usually produce more passages.</p>
<p><strong>Corpus exhausted (questions):</strong> Number of questions for which
all available chunks from the question's paper have been read but the specified
word budget is still not filled. This describes exhausted available text;
it does not by itself indicate retrieval failure or missing evidence.</p>
</aside>
{"".join(tables)}
</body></html>
"""
    path = run_dir / "summary.html"
    path.write_text(document, encoding="utf-8")
    return path
