# Q5 BGE reranker ablation — job 51802, 40 dev items (2026-11-06)

`COMPLETED`, exit 0, elapsed **00:31:12**.

**Hardware:** TC2N02, 1 x NVIDIA A40 (46 GB), 8 CPUs, 48 GB host memory.
The BGE reranker ran on the CPU (`--device cpu`).

**Code and settings:** clean detached worktree of `ad02d51` (the frozen
8 x 1,200 configuration, not `context-2500`). `BGE=1`,
`ARMS="static adaptive"`, `CRITIC=generator`, `SCOPED=1`, `OFFLINE=1`,
`TOP_K=8`, `CANDIDATE_K=20`, `MAX_RETRIES=2`, `ANSWERS=p5`.
Same 40 development items (sha `ff69f9a0…`), development corpus
(`ecb1c601…`) and dense index (`365-40-dev`) as jobs 51521 / 51690.
The requested configuration has two arms, so this archive contains
`static.jsonl` and `adaptive.jsonl` only; there is no `static-wide.jsonl`.

## Paired with job 51690 (BGE=0, same 40 items, same 8 x 1,200 budget)

| | static BGE=0 | static BGE=1 | adaptive BGE=0 | adaptive BGE=1 |
| --- | ---: | ---: | ---: | ---: |
| answered / refused | 36 / 4 | 35 / 5 | 36 / 4 | 35 / 5 |
| downgraded | 3 | 4 | 3 | 3 |
| mean citations | 1.89 | 1.40 | 1.92 | 1.51 |
| citation gold recall | 0.694 | **0.550** | 0.726 | **0.650** |
| citation gold precision | 0.580 | **0.461** | 0.577 | **0.522** |
| answer chars, median | 125.5 | 132 | 125.5 | 132 |
| retrieval recall, before / after retries | 0.885 / 0.885 | **0.854 / 0.854** | 0.885 / 0.927 | **0.854 / 0.917** |
| answerable answered | 31 / 32 | **30 / 32** | 31 / 32 | **30 / 32** |
| unanswerable answered | 5 / 8 | 5 / 8 | 5 / 8 | 5 / 8 |
| whole-job elapsed | 0:15:21 | **0:31:12** | | |

Per-question gold-citation count versus BGE=0: static better 1 / worse 8;
adaptive better 1 / worse 6. 23 of 40 answer texts differ.

## Reading

On this development set the BGE reranker is worse on every answer metric:
fewer answered, more refusals, lower citation gold recall and precision, and
it roughly doubles wall-clock time. Retrieval recall at top-8 also drops
(0.885 -> 0.854 before retries). This is consistent with the earlier
retrieval-depth finding that BGE is below plain RRF at every depth, and it
does not support turning the reranker on for the final configuration.

## Files

```
runs/p4/q5-bge-dev/static.jsonl
runs/p4/q5-bge-dev/adaptive.jsonl
runs/p4/q5-bge-dev/run_manifest.json
runs/p4/q5-bge-dev/metrics.json
runs/p4/q5-bge-dev/metrics.md
logs/p4-agent-51802.out
p4_dev_items_40.jsonl
SHA256SUMS.txt
```
