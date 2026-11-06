# P2 submission results

Final four-method retrieval benchmark at K=1,3,5 and paired K=5 comparisons.
`scored/` contains per-question scores, aggregate CSV/JSON and the original run manifest.
Each comparison folder contains bootstrap differences and its original manifest.
`RESULTS.md` records findings, metric denominators, label limitations and reproduction.
`INPUTS.json` pins input commits and hashes; recover pool files from
`1a1dc15b:data/processed/annotation_common_v3/` and label/review files from
`f70bf95:data/gold/p6/final/`. No corpus, models or indexes are needed to read the outputs.
Original producer paths in manifests are historical; use relative paths here to read outputs.
These top-five retrieval results do not measure generated-answer quality or top-eight retrieval.
