# BGE=0 control — job 51690, 40 dev items (2026-11-06)

`COMPLETED`, exit 0, elapsed **00:15:21**.

**Hardware:** TC2N04, 1 x NVIDIA L40S (46 GB), 8 CPUs, 48 GB host memory.

**Code and settings:** `fb303bc`, run with `MAX_CHARS_PER_PASSAGE=1200`
(explicit override of the branch default). The rendered prompt and the
generation path are the same as `ad02d51`; the only code difference is the
explicit budget override and its recording in the manifest. `BGE=0`,
`ARMS="static adaptive"`, `CRITIC=generator`, `SCOPED=1`, `OFFLINE=1`,
`TOP_K=8`, `CANDIDATE_K=20`, `MAX_RETRIES=2`, `ANSWERS=p5`.
Same 40 development items (sha `ff69f9a0…`), development corpus
(`ecb1c601…`) and dense index (`365-40-dev`) as jobs 51521 and 51802.
The run manifest records `prompt_budget = {8, 1200}` and `bge: false`.

If the ablation table requires a byte-identical commit to 51802
(`ad02d51`), use this row with a footnote: 51690 is `fb303bc` with an
explicit 1,200-character override, not `ad02d51`. The model inputs are the
same; the commit differs only in the budget plumbing.

## Paired with 51802 (BGE=1, same 40 items, same 8 x 1,200 budget)

| | static BGE=0 | static BGE=1 | adaptive BGE=0 | adaptive BGE=1 |
| --- | ---: | ---: | ---: | ---: |
| answered / refused | 36 / 4 | 35 / 5 | 36 / 4 | 35 / 5 |
| downgraded | 3 | 4 | 3 | 3 |
| mean citations | 1.89 | 1.40 | 1.92 | 1.51 |
| citation gold recall | 0.694 | 0.550 | 0.726 | 0.650 |
| citation gold precision | 0.580 | 0.461 | 0.577 | 0.522 |
| retrieval recall, before retries | 0.885 | 0.854 | 0.885 | 0.854 |
| answerable answered | 31 / 32 | 30 / 32 | 31 / 32 | 30 / 32 |
| whole-job elapsed | 0:15:21 | 0:31:12 | | |

## Files

```
runs/p4/context-dev-1200/static.jsonl
runs/p4/context-dev-1200/adaptive.jsonl
runs/p4/context-dev-1200/run_manifest.json
runs/p4/context-dev-1200/metrics.json
runs/p4/context-dev-1200/metrics.md
logs/p4-agent-51690.out
p4_dev_items_40.jsonl
SHA256SUMS.txt
```
