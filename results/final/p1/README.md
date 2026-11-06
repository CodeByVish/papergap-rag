# P1 verified BM25-Dense comparison

This archive preserves P1's independent reproduction of the **paired BM25 versus Dense comparison at K=5**, run on 5 November 2026 from P2's saved per-question scores. It did not rerun retrieval, the original scoring stage, models or annotation. Archiving these files does not execute a new experiment.

## Contents and results

The five original files are preserved byte for byte:

- `comparison/ablation.csv`: four metric differences and bootstrap intervals.
- `comparison/summary.json`: the same comparison as structured data.
- `comparison/run_manifest.json`: original execution arguments, versions, paths and hashes.
- `VERIFICATION.md`: original verification findings and limitations.
- `verification.json`: full original verification record.

This README, `SHA256SUMS.txt` and `.gitattributes` are new archive metadata. The checksum list covers the other seven files. The directory-local `* -text` rule preserves file bytes, including original line endings, only within this P1 archive.

Differences are **Dense minus BM25**. The 95% intervals use **1,000 paper-cluster bootstrap resamples, seed 42**; the table rounds values to four decimal places.

| Metric | Paired questions | Papers | Difference | 95% interval |
| --- | ---: | ---: | ---: | --- |
| Precision@5 | 200 | 174 | +0.0450 | [0.0171, 0.0728] |
| Pool recall@5 | 199 | 174 | +0.0909 | [0.0419, 0.1421] |
| MRR@5 | 200 | 174 | +0.0696 | [0.0168, 0.1222] |
| Pool nDCG@5 | 199 | 174 | +0.0833 | [0.0366, 0.1314] |

There are no unmatched question IDs. One question has no positive label: its pool recall/nDCG are null and excluded, while its precision/MRR are zero and included. All comparisons cover 174 papers. Full precision and the excluded question ID are retained in the original records.

## Pinned input and original code

- Shared input: [`../p2/scored/scores.jsonl`](../p2/scored/scores.jsonl), or `results/final/p2/scored/scores.jsonl` from the repository root (2,400 rows; only BM25 and Dense at K=5 are selected).
- Input snapshot commit: `a78275eb26d4c1fbb2fa75e23276a41b99e27886` ([pinned file](https://github.com/CodeByVish/papergap-rag/blob/a78275eb26d4c1fbb2fa75e23276a41b99e27886/results/final/p2/scored/scores.jsonl)).
- Input SHA-256: `5d74e32fbbb175c9cade7f974df70d3c55d2e76556f40c4f91d4e9fd7e450b7e` (both comparison arms).
- Original P1 execution code: `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`, Python 3.11.16. Package versions and source hashes remain in the original manifest.
- P2 producer code, gold and pool provenance remain in `VERIFICATION.md` and `verification.json`; the manifest schema remains `v0-proposed`.

The input is referenced, not duplicated here. The CSV matches P2's shared `dense-vs-bm25/ablation.csv` byte for byte; the JSON summary matches its parsed data. Their JSON bytes differ only in CRLF/LF line endings, which have been preserved.

## Reproduce into a new directory

These are instructions for a future reproduction, not an additional run performed for this archive. From a clone containing both pinned commits, create a separate checkout of the original execution code:

```powershell
git worktree add --detach ../papergap-p1-reproduction-ad02d51 ad02d5103e28dbca2230555dd90e36c5cdc70f4f
Set-Location ../papergap-p1-reproduction-ad02d51
```

Use a compatible Python environment with the recorded dependencies. The following PowerShell block verifies the code revision and input bytes, creates a **new** directory (fails if it already exists), then invokes the original comparison. Choose another unused `run_root` for any later run. Never use `results/final/p1/comparison` or the original output directory as an output target.

```powershell
@'
import hashlib
from pathlib import Path
import subprocess
import sys

code = "ad02d5103e28dbca2230555dd90e36c5cdc70f4f"
head = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
if head != code:
    raise SystemExit("Use the original execution-code checkout.")
pin = "a78275eb26d4c1fbb2fa75e23276a41b99e27886"
path = "results/final/p2/scored/scores.jsonl"
data = subprocess.check_output(["git", "show", f"{pin}:{path}"])
expected = "5d74e32fbbb175c9cade7f974df70d3c55d2e76556f40c4f91d4e9fd7e450b7e"
if hashlib.sha256(data).hexdigest() != expected:
    raise SystemExit("Input checksum mismatch.")
run_root = Path("results/p1-compare-reproduction-new")
run_root.mkdir(parents=True, exist_ok=False)
scores = run_root / "scores.jsonl"
with scores.open("xb") as stream:
    stream.write(data)
subprocess.run([
    sys.executable, "-B", "-m", "scripts.run_p6_evaluation", "compare",
    "--left", str(scores), "--right", str(scores),
    "--left-arm", "BM25", "--right-arm", "Dense", "--k", "5",
    "--metrics", "precision_at_k", "pool_recall_at_k", "mrr_at_k", "pool_ndcg_at_k",
    "--resamples", "1000", "--seed", "42", "--output", str(run_root / "comparison"),
], check=True)
'@ | python -B -
```

Compare the new CSV and parsed summary with the archived results. New manifest paths and environment details will naturally differ; do not overwrite the preserved originals. Cross-platform JSON line endings may also differ without changing parsed values.

## Historical records and limits

Absolute paths and the original statements that no commit, PR, report edit or `DONE FOR DRAFT` marking had occurred describe the **5 November comparison step only**. The manifest's `git_commit` remains the code used for that run, not a report or archive commit. The P1 report contribution was subsequently delivered through [PR #55](https://github.com/CodeByVish/papergap-rag/pull/55). This archive does not revise that report or its sign-off.

These checks validate a paired comparison from saved scores, not the earlier retrieval/scoring pipeline, annotation independence, generated-answer quality, RAGAS or runtime performance. Pool metrics describe the fixed judged pool, not exhaustive corpus relevance. Conclusions remain conditional on the supplied questions and label provenance. K=5 here is the retrieval benchmark cutoff; it does not measure the top-eight agent pipeline or resolve later generation-context experiments.
