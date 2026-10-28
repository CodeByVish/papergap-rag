# Weekly tracker

Update this file after the weekly meeting. Link to concrete issues, PRs, artifacts or run IDs.

| Week | Dates | Exit checkpoint | Status |
| --- | --- | --- | --- |
| 1 | 14–20 Sep | Rubric interpretation, owners, compute, interfaces and split policy | Not recorded |
| 2 | 21–27 Sep | Provisional corpus, independent retrieval, pilot candidates | Not recorded |
| 3 | 28 Sep–4 Oct | Retrieval baselines, annotation pilot, final chunker/corpus freeze | P3 delivery completed on 2026/10/28: [English report](../weekly-work/week-3/week-3-report-en.md) / [Chinese report](../weekly-work/week-3/week-3-report-zn.md). BM25 Rounds $1$–$4$ assessed without readability scoring; selected $365/40$ words as an overall tradeoff, not a proven optimum. Default configuration updated; development/all-paper-text/sample corpora rebuilt and verified at $21{,}360/28{,}617/100$ passages. Shared interfaces remain `v0-proposed`; project-wide freeze awaits module-owner confirmation. Other checkpoints not recorded. |
| 4 | 5–11 Oct | One complete query in Streamlit | P3 paper catalog completed on 2026/10/28: `scripts/build_paper_catalog.py` builds local `data/processed/paper_catalog.json` from the configured passage corpus, with $1{,}168$ selectable papers, $16{,}187$ paper/section-name entries and $21{,}360$ passages. [Data guide](../data/README.md) / [Chinese guide](../data/README_zh-CN.md) document the `v0-proposed` fields and reproduction. Annotation pool completed on 2026/10/28: $250$ saved selection queries recovered, $253$ used IDs audited, $200$ question-isolated held-out queries frozen with BM25/$365/40$/top-$5$, and $1{,}000$ unique pairs verified. Two independent English Markdown sets contain $10$ batches each. Code and input hashes are recorded in local pool manifests. Full suite: $534$ tests passed. Team assignment, labeling, agreement/adjudication and UI integration remain pending; no data Release published. Audit covers persisted local records only. |
| 5 | 12–18 Oct | Frozen held-out pool and annotation guidelines | Not recorded |
| 6 | 19–25 Oct | 2,000 blind judgments, agreement, adjudication, system freeze | Not recorded |
| 7 | 26 Oct–1 Nov | Final comparisons and analysis | Not recorded |
| 8 | 2–6 Nov | Clean setup, report PDF and links verified | Not recorded |
| Submission | 7 Nov | Blackboard submission before 11:59 PM SGT | Not recorded |

## Meeting actions

2026/10/28: Week 4 Step $2.3$ completed a development-only three-retriever pilot in `data/processed/annotation_pilot_multi_v2/`: $5$ saved selection questions, $36$ unique pairs, $25$ common, $5$ BM25-only and $6$ Dense-only; no Hybrid-only pairs. Pinned BGE/cosine and RRF $20/60$ configuration is saved before future formal expansion. Source attribution is disclosed, human labels remain blank, and gold is kept in verification. Targeted tests: $46$ passed; independent persisted-artifact checks passed. The Week 4 BM25 snapshot in the table above is historical; cross-branch exclusions, current held-out eligibility and formal expansion remain pending. Next: TODO Step $2.4$.

| Task / issue | Owner | Due | Required input | Reviewable output | Blocking? | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Confirm rubric document/record units | Team | Week 1 | Instructor clarification | Both interpretations confirmed; see REQUIREMENTS.md | No | Confirmed 16 Sep |
| Confirm compute and evaluator access | P5/P6 | Week 1 | GPU access and judge backend | Feasibility note | Yes: inference setup | Open |
| Fill remaining names and backup owner | Team | Week 1 | Member agreement | Updated README | No | Open |
