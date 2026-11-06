# P1 BM25 versus Dense comparison verification

Status: **PASS**. Verified at 2026-11-05 15:47:09 UTC.

One local offline execution of the existing P6 `compare` command reproduced the supplied P2 BM25-versus-Dense comparison at K=5. The generated CSV is byte-for-byte identical to the reference. All four metric differences, paper-cluster bootstrap intervals and denominators match exactly; no numerical tolerance was used.

## Results

Differences are **Dense minus BM25**. Intervals use 1,000 paper-cluster bootstrap resamples with seed 42.

| Metric | Paired questions | Papers | Difference | 95% interval |
| --- | ---: | ---: | ---: | --- |
| Precision@5 | 200 | 174 | +0.0450 | [0.0171, 0.0728] |
| Pool recall@5 | 199 | 174 | +0.0909 | [0.0419, 0.1421] |
| MRR@5 | 200 | 174 | +0.0696 | [0.0168, 0.1222] |
| Pool nDCG@5 | 199 | 174 | +0.0833 | [0.0366, 0.1314] |

Both arms contain the same 200 unique question IDs and matching paper IDs, with zero left-only or right-only questions. Precision and MRR include all 200. Pool recall and pool nDCG exclude one question with no positive label and therefore use 199. All four comparisons still cover 174 papers.

The excluded question is `06cc8fcafc0880cf69a2514bb7341642b9833041` from paper `1809.06537`. Its pool contains nine judged passages and zero relevant passages. Both arms record null pool recall/nDCG and zero precision/MRR for this question.

Dense has higher values for the four metrics in this supplied pool, and all four reported intervals are above zero. This is conditional on the supplied labels and question set; it does not establish general superiority or remove annotation bias.

## Inputs and versions

- Source package: `results/p2-final-retrieval-handoff.zip`.
- Extracted package: `results/p2-final-retrieval-handoff/`.
- Input scores: `scored/scores.jsonl` inside the package.
- Reference comparison: `dense-vs-bm25/ablation.csv` inside the package.
- Current code commit: `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`.
- P2 producer code commit: `ceeaca8718daa0bbd2e6a9a3409b3eab6c4aa153`.
- P3 pool/ranking commit recorded by P2: `1a1dc15b824590a39c80ea11a568fbe5814a926e`.
- Gold commit recorded by P2: `f70bf95593a6b9f705674770b8c3e833ca76290c`.
- Interpreter: `E:/miniconda/py311/envs/papergap/python.exe`, Python 3.11.16.
- Package SHA-256: `390793afc22508c4f10fbb74d2c8d42f936b941b840a4537d08c102187d89d69`.
- Scores SHA-256: `5d74e32fbbb175c9cade7f974df70d3c55d2e76556f40c4f91d4e9fd7e450b7e`.
- Reproduced and reference CSV SHA-256: `8e2b7fa7acdcdb98e46fb5e769ec0e8e5548d3a78b5020eb921dbbfb1605fb0a`.

All 23 entries in the package checksum list matched. Its 24 files passed ZIP CRC validation and matched the extracted files byte for byte. The scores contain 2,400 rows across four arms and three cutoffs; this comparison selected only BM25 and Dense at K=5.

The 13 evaluation source files are identical between the two Git commits and match P2's recorded source hashes. The working files differ from canonical Git bytes only where Windows checkout line-ending conversion applies. These facts are recorded separately in `verification.json`; the comparison logic was not modified.

## Executed command

Run from `E:/Lenovo/Desktop/papergap-rag` in PowerShell:

```powershell
& 'E:\miniconda\py311\envs\papergap\python.exe' -B -m scripts.run_p6_evaluation compare --left 'results/p2-final-retrieval-handoff/scored/scores.jsonl' --right 'results/p2-final-retrieval-handoff/scored/scores.jsonl' --left-arm BM25 --right-arm Dense --k 5 --metrics precision_at_k pool_recall_at_k mrr_at_k pool_ndcg_at_k --resamples 1000 --seed 42 --output 'results/p1-bm25-vs-dense-verification-20261105/comparison'
```

The command ran once and exited with code 0. The output directory now exists, so the recorded command must not be rerun against it. No second comparison run was performed.

## Output and exact-match checks

- [comparison/ablation.csv](comparison/ablation.csv): four comparison rows, identical to the reference bytes.
- [comparison/summary.json](comparison/summary.json): exactly equal parsed data to the reference summary.
- [comparison/run_manifest.json](comparison/run_manifest.json): local run provenance, exact arguments, input and output hashes.
- [verification.json](verification.json): preflight, source identity, preservation checks and exact comparison evidence.

The JSON summary's raw bytes differ only by LF versus CRLF line endings. No file was rewritten to force byte equality. The new run manifest intentionally records the current commit and local Windows paths, so it is not expected to match the producer manifest byte for byte.

After the run, all 38 protected files were unchanged: the ZIP, its 24 extracted files, and 13 annotation Markdown files. All 13 checked evaluation source files were unchanged. The branch remained `main` at `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`; tracked worktree state, local branches and other worktrees were unchanged.

## Scope and limits

This verifies the paired comparison computed from P2's saved per-question scores. It does not independently reproduce the earlier retrieval-scoring stage from rankings and labels, rerun retrieval or models, validate annotation independence, or establish final QA, RAGAS or latency results. Pool recall and pool nDCG describe the judged pool rather than exhaustive paper relevance.

The P2 package's declared label provenance remains part of any subsequent interpretation. This automated check neither changes that provenance nor supplies human approval. It does not resolve the Agent Top-5 versus Top-8 discussion.

No dependencies were installed and no model/network scoring was performed. The original package, annotations and project source were preserved. No branch switch, commit, push, PR action, report edit or `DONE FOR DRAFT` marking was performed.

