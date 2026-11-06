"""Run the five development demos through the real Streamlit UI and P5 API.

Outputs contain real model records and passage text: keep the output ignored.
Run from the repository root with the prepared P6 Python environment.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)

    from scripts.p6_local import configure

    configure()
    from streamlit.testing.v1 import AppTest
    from src.ui.api_client import ApiConfig, P5ApiClient
    from src.ui.conversation_state import export_runs

    root = Path(__file__).resolve().parents[1]
    sample = root / "results/p6-local/sample-questions.jsonl"
    questions = [json.loads(line) for line in sample.read_text().splitlines() if line]
    expected = [
        "30c6d34b878630736f819fd898319ac4e71ee50b",
        "0ab3df10f0b7203e859e9b62ffa7d6d79ffbbe50",
        "729694a9fe1e05d329b7a4078a596fe606bc5a95",
        "65ad17f614b7345f0077424c04c94971c831585b",
        "5bcc12680cf2eda2dd13ab763c42314a26f2d993",
    ]
    by_id = {q["question_id"]: q for q in questions}
    questions = [by_id[qid] for qid in expected]

    def save(name, value):
        (args.output / name).write_text(json.dumps(value, indent=2))

    def widget(elements, label):
        return next(w for w in elements if w.label == label)

    config = ApiConfig.from_env()
    client = P5ApiClient(config)
    save("health.json", client.health())
    save("questions.json", questions)
    save("source.json", {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "status": subprocess.check_output(["git", "status", "--short"], text=True),
        "source_sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for folder in ("src", "scripts") for p in (root / folder).rglob("*.py")},
        "test_method": "Streamlit AppTest with live HTTP, no mocked responses",
        "selection": "Existing five development-pilot questions; not held-out",
    })
    app = AppTest.from_file(str(root / "src/ui/app.py"),
                            default_timeout=config.answer_timeout + 30).run()
    if app.exception:
        raise RuntimeError(str(app.exception))
    widget(app.button_group, "Search scope").set_value("One paper").run()
    checks = []
    for number, question in enumerate(questions, 1):
        widget(app.selectbox, "Paper title and ID").set_value(question["paper_id"]).run()
        widget(app.text_area, "Your question").set_value(question["question"])
        print(f"START {number}: {question['question']}", flush=True)
        widget(app.button, "Ask question").click().run()
        if app.exception:
            save(f"error-{number}.json", [str(e) for e in app.exception])
            raise RuntimeError(f"UI exception on question {number}")
        state = app.session_state["workspace_state"]
        runs = [r for c in state["conversations"].values() for r in c["runs"].values()]
        run = max(runs, key=lambda r: r["submitted_at"])
        save(f"run-{number}.json", run)
        save(f"rendered-{number}.json", {
            "markdown": [m.value for m in app.markdown],
            "warnings": [m.value for m in app.warning],
            "errors": [m.value for m in app.error],
        })
        record = run.get("answer_record") or {}
        result = record.get("result", {})
        citations = result.get("citations", [])
        lookup = client.passages(citations)
        save(f"citation-lookup-{number}.json", lookup)
        retrieved = {pid for entry in record.get("agent", {}).get("retrieval_log", [])
                     for pid in entry.get("passage_ids", [])}
        checks.append({
            "number": number, "question_id": question["question_id"],
            "outcome": run["outcome"], "answer": result.get("answer"),
            "evidence_status": result.get("evidence_status"),
            "answer_http_ms": run.get("answer_http_elapsed_ms"),
            "citation_http_ms": run.get("citation_http_elapsed_ms"),
            "citation_count": len(citations), "missing_citations": lookup["missing"],
            "citation_papers_match": all(p.get("paper_id") == question["paper_id"]
                                         for p in lookup["passages"].values()),
            "citations_retrieved": all(pid in retrieved for pid in citations),
            "ui_evidence_error": run.get("evidence_error"),
            "warning_codes": [v["code"] for v in record.get("validation", {}).get("violations", [])],
        })
        save("checks.json", checks)
        (args.output / "ui-export.json").write_text(export_runs(state, [r["client_run_id"] for r in runs]))
        print(f"DONE {number}: {run['outcome']}, {len(citations)} citations, "
              f"{run.get('answer_http_elapsed_ms')} ms", flush=True)


if __name__ == "__main__":
    main()
