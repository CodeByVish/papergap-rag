# P3 chunk-size experiment results

This directory contains the four valid BM25 runs used to select the passage chunk size. The original artifacts are restored byte for byte from P3 commit `03c2ae4` after main's revert `26d82ff` removed them. `.gitattributes` disables newline conversion for these files so manifest SHA-256 values survive checkout.

## Submitted runs

| Run | Role | Entry point |
| --- | --- | --- |
| `round1_bm25_20261028_02` | Broad comparison of $100/200/400$ words on $50$ questions | [Report](round1_bm25_20261028_02/report.md) |
| `round2_bm25_20261028_01` | Comparison of $200$ through $400$ words in $25$-word steps | [Report](round2_bm25_20261028_01/report.md) |
| `round3_bm25_20261028_01` | Fine comparison around the shortlisted sizes | [Report](round3_bm25_20261028_01/report.md) |
| `round4_bm25_20261028_01` | Validation on $200$ new questions plus $50$ regression questions | [Final report and selection](round4_bm25_20261028_01/report.md) |

Each run includes `manifest.json`, `questions.jsonl`, `summary.json`, `summary.html`, `report.md` and candidate-level `ranked_chunks.jsonl` and evidence-review reports. Round 4 also includes its frozen `question_plan.json`. Manifests retain configuration, code/input provenance, dependency versions, timing and structured-input hashes. Historical readability samples are preserved but do not contribute to the selection.

## Selection and scope

The selected setting is $365$ words per chunk with $40$ words of overlap. On Round 4's $200$ new questions, it obtains $147/200$ evidence hits and $125/200$ complete-evidence successes at top-$5$. Selection considered top-$5$ results, word budgets and context length together.

The predeclared primary metric was complete evidence at a $1000$-word budget on new questions. Here $375$ scores $108/200$ and $365$ scores $106/200$; $365$ does not win that metric. Small differences do not establish significance or a stable optimum. Overlap was fixed throughout, rather than optimized. These questions were used for configuration selection and are not an independent final test set. See the final report for all budgets, paired comparisons and limitations.

The invalidated runs `smoke_p1_bm25_01`, `formal_bm25_20261028_01` and `round1_bm25_20261028_01` are excluded from this submission. Their artifacts and invalidation notices remain available in P3 Git history at commit `03c2ae4`; do not combine their metrics with the valid runs.

## Reproduction and access

Download this directory from the merged delivery branch, or from `p3/final-chunk-size-results` while its integration PR is pending. Keep the directory structure intact. Open each `summary.html` directly for the saved metrics; no model or index download is needed.

The experiment runner, configuration and full reproduction instructions are preserved in [the P3 experiment guide at the selection commit](https://github.com/CodeByVish/papergap-rag/blob/03c2ae4/experiments/chunk_size/README.md). Use a separate checkout of that commit and the documented environment and data inputs when regenerating results; the current main branch does not contain that runner. Run commands from that checkout's repository root, and use a copy of the submitted run when regenerating derived reports:

```powershell
python -m scripts.evaluate_chunk_size regenerate --run-dir results/chunk_size/round4_bm25_20261028_01
```

The frozen plan, structured rankings and their manifest hashes allow the saved evidence metrics to be regenerated without rerunning retrieval. Full retrieval reproduction additionally requires the original exported data and configuration described in the linked guide. Shared passage schemas and split mappings retain their recorded `v0-proposed` status.
