"""Check offline aggregate reports and the render-only command.

Synthetic summaries exercise missing reviews, exact ties and HTML escaping
without requiring datasets, retrieval dependencies or browser downloads.
"""

import json
from pathlib import Path

import pytest

from scripts.evaluate_chunk_size import main
from src.evaluation.render_chunk_size_summary import write_summary_html


def test_summary_tables_preserve_metric_meaning(tmp_path: Path) -> None:
    """Sort numeric sizes and budgets while distinguishing pending and zero.

    Only rate columns may highlight maxima; rounded near-ties remain distinct.
    """
    sizes = {}
    for size, rate in (("100", 0.50001), ("20", 0.50002), ("4", 0.50002)):
        sizes[size] = {
            "evidence_hit_at_5": {"value": rate, "numerator": 1, "denominator": 2},
            "readability_pass_rate": {"value": None, "pending": 3},
            "retrieved_word_count": {"value": 0.0, "numerator": 0, "denominator": 2},
            "budgets": {
                "1000": {"evidence_hit": {"value": 0.0}},
                "500": {"evidence_hit": {"value": None}},
            },
        }
    path = write_summary_html(tmp_path, {"run_id": '<script>"&', "sizes": sizes})
    html = path.read_text(encoding="utf-8")
    assert "<script>" not in html
    assert "&lt;script&gt;&quot;&amp;" in html
    assert html.index('scope="row">4<') < html.index('scope="row">20<')
    assert html.index('scope="row">20<') < html.index('scope="row">100<')
    assert html.index("Word budget: 500 words") < html.index("Word budget: 1000 words")
    top, rest = html.split("Word budget: 500 words", 1)
    assert top.count('class="best"') == 2
    assert rest.count('class="best"') == 3  # All zero rates tie in budget 1000.
    assert "Pending (3)" in html and ">N/A<" in html
    assert 'title="1 / 2">0.5000<' in html
    assert '<td title="0 / 2">0.0000<' in html  # Word counts are never ranked.
    assert 'src="http' not in html and "<script" not in html


def test_render_cli_keeps_json_unchanged(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Render a historical summary with no budgets, manifest or model access.

    Repeated renders replace stale HTML without changing source JSON bytes.
    """
    source = tmp_path / "summary.json"
    source.write_text(json.dumps({"sizes": {"200": {}}}), encoding="utf-8")
    original = source.read_bytes()
    report = tmp_path / "summary.html"
    report.write_text("stale", encoding="utf-8")
    monkeypatch.setattr(
        "sys.argv", ["evaluate_chunk_size", "render", "--run-dir", str(tmp_path)]
    )
    assert main() == 0
    html = report.read_text(encoding="utf-8")
    assert 'scope="row">200<' in html and "Word budget:" not in html
    assert source.read_bytes() == original
