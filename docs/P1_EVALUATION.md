# P1 saved-ranking evaluation (provisional)

This is the independent scoring stage of the existing P1 experiment workflow.
It reuses `experiment.py`, `run_p1_experiment.py`, the verified P3 input adapter
and the saved rankings. It does not run BM25, load FAISS or encode queries.
P2/P3/P4/P5/P6 implementations are unchanged. The current real development run
has **no supplied gold passage-ID labels**; its quality metrics are unavailable.
The executable metric tests use explicitly synthetic, hand-calculated labels.

## Audit an existing run

From the repository root, using the papergap Python 3.11 environment:

```powershell
$p1Python = 'E:\Miniconda\py311\envs\papergap\python.exe'
& $p1Python -B -m scripts.run_p1_experiment evaluate --run-dir results/p1-week3-week4-development --output-dir results/p1-week3-week4-evaluation-final --evaluation-k 5
```

Output must be new/empty and outside the original run directory. On another
machine, override `--passages`, `--corpus-manifest`, `--qa`, `--export-manifest`
to relocate the original inputs; hashes and question scope must still match.
Do not rebuild or rerun retrieval just to audit or score existing rankings.

| Output | Contents |
| --- | --- |
| `audit.json` | Original run/input/output hashes, K, filter policy, status, per-method counts, 0..K distributions, all short-return cases, latency distribution and discrepancies. |
| `counts.jsonl` | Every question/method: paper/eligible Passage counts, expected `min(K, count)`, actual/logged result counts, reason and detected discrepancies. |
| `evaluation.json` | Metric conventions, label coverage, exclusions, per-question and macro scores when supplied labels permit them; otherwise `unavailable`, with null metrics. |
| `provenance.json` | Source run hash, evaluator source hashes, interpreter, optional label/manifest hashes; explicitly records that retrieval was not repeated. |

Validation covers the original corpus and QA manifests, hashes, train-only
question identity and coverage, unique logs, Passage IDs, paper membership,
requested section (if any), finite scores, descending order, continuous unique
ranks, query statuses, expected counts and run completion. Corrupt identities,
hashes, ranks or labels fail closed with a clear error. Count/status/completion
discrepancies produce an `invalid` audit, skip scoring and exit with code 2.
Original experiment files are never changed. Latency is recomputed from the
recorded `retrieve()` measurements, not measured anew.

The original exporter omitted a `filters` field. Its exact recorded source
SHA-256 is recognized as the reviewed three-argument, paper-only exporter.
Unknown legacy exporters are rejected rather than guessing their filter policy.
New runs explicitly record paper/section filters. No section was requested in
the existing real baseline, so differing returned section names are permitted.

## Independent JSONL labels

P3/P5/P6 must supply the judgments and their provenance. Do not manufacture
gold by text matching, retrieval scores, a model's opinion, or the test fixture.
Keep real labels and manifests in ignored `data/` paths. The following IDs and
judgments illustrate the **synthetic test format**, not QASPER labels:

```json
{"question_id":"q1","paper_id":"paper-a","status":"mapped","relevance_complete":true,"relevant_passage_ids":["a1","a3"]}
```

Each line requires the five fields above. Optional `judged_passage_ids` lists
all explicitly judged passages, including negatives, and must include every
relevant ID. It defaults to the relevant IDs. `relevance_complete: true` is a
supplier's explicit claim of complete relevance coverage for this question's
paper, not just that all ten pooled candidates have been judged. The adapter
can validate IDs and versions; it cannot establish the scientific correctness
of a supplier's completeness declaration.

The companion manifest is a JSON object. Replace placeholder hashes and scope
IDs with independently verified values, not the example values:

```json
{
  "format_version": 1,
  "labels_format": "jsonl",
  "labels_sha256": "<SHA-256 of the label file bytes>",
  "corpus_sha256": "<SHA-256 of the exact passages.jsonl bytes>",
  "source": "<supplier, annotation source and provenance>",
  "mapping": {
    "version": "<evidence-to-passage mapping version>",
    "description": "<coverage, overlap, ambiguity and figure/table policies>"
  },
  "annotation_coverage": "partial",
  "question_scope": {
    "source_split": "train",
    "project_role": "development",
    "split_policy_version": "qasper-official-paper-disjoint-v0-proposed",
    "question_ids": ["q1", "q2"]
  }
}
```

`question_scope.question_ids` must identify the **whole saved run's question
set**, even when labels cover only a subset. This prevents silently substituting
a smaller evaluation scope. `annotation_coverage: complete` requires a record
for every scoped question; `partial` allows missing records and reports their
exclusion. These are different from per-question `relevance_complete`.

Duplicate question/Passage IDs, duplicate JSON keys, unknown IDs, wrong paper
associations, changed corpus/label hashes, different split policy or a scope
containing non-development questions are errors. Passage IDs remain opaque;
paper membership comes from the validated Passage schema. A different corpus
or chunking version requires its own matching labels, never an inferred ID
conversion.

## Four-column TREC qrels adapter

Alternatively use `labels_format: trec` and whitespace-separated rows:

```text
q1 0 a2 0
q1 0 a1 1
q1 0 a3 2
```

The columns are question ID, ignored iteration, Passage ID, nonnegative integer
relevance grade. Grades greater than zero are relevant; zero is explicitly
nonrelevant. Negative/noninteger grades and duplicate question/Passage pairs
are rejected. Unjudged passages have no row and are not automatically negatives.

TREC itself lacks paper IDs, answerability and mapping state. Add an
`assessments` object to the same manifest, with one entry per annotated
question, including excluded questions that have no qrels rows:

```json
{
  "assessments": {
    "q1": {"paper_id":"paper-a","status":"mapped","relevance_complete":true},
    "q2": {"paper_id":"paper-b","status":"mapping_failed","relevance_complete":false}
  }
}
```

All positive and negative IDs pass the same corpus, paper and scope checks.
TREC row presence alone is insufficient to declare exhaustive relevance.

Once reliable labels are delivered, use a separate output directory:

```powershell
& $p1Python -B -m scripts.run_p1_experiment evaluate --run-dir results/p1-week3-week4-development --output-dir results/p1-week3-week4-labeled --evaluation-k 5 --labels data/p1-development-qrels.jsonl --labels-manifest data/p1-development-qrels.manifest.json
```

This labeled command is a future handoff command, not a claim that those real
label files currently exist or that real quality scoring has run.

## Provisional metric and exclusion policy

P6 has not supplied a callable backend or frozen the metric conventions in the
fetched remote branches. `src/retrieval/evaluation.py` therefore exposes a
replaceable `MetricsBackend.score(retrieved, relevant, *, k)` interface and a
minimal `ProvisionalMetricsBackend`. Reports identify it as `P6_pending`.

For eligible questions, count unique relevant hits in the first K positions:

| Measure | Definition |
| --- | --- |
| Precision@K | Relevant hits / K, including when fewer than K passages were returned. |
| Recall@K | Relevant hits / size of the complete relevant Passage set. |
| MRR@K | Reciprocal rank of the first relevant hit at or before K; zero if none. |

Aggregate each measure with an unweighted mean across the same eligible
questions for each method. The current retrieval only saved K=5: evaluation
may use K<=5, but deeper K is rejected. **MRR@K is truncated**, never reported
as full-ranking MRR. A known relevant Passage at rank K+1 is a miss at this K.
No nDCG, evidence-span aggregation or uncertainty estimates are implemented.

| Input state | Provisional handling |
| --- | --- |
| `mapped`, complete relevance, nonempty relevant IDs | Eligible; a true retrieval miss or empty retrieval receives zero scores. |
| Missing question record in partial annotations | Exclude as `missing_labels`; metrics null for that question. |
| `mapping_failed` | Exclude separately; use no claimed relevant IDs. |
| `unanswerable` | Exclude separately, pending P6's answerability policy. |
| `no_relevant` | Exclude separately; requires an explicit complete-relevance declaration and empty relevant IDs. |
| `mapped` but incomplete relevance | Exclude as `incomplete_relevance`; report judged coverage only. |

Partially mapped evidence with some usable IDs must remain incomplete until
the supplier establishes a complete relevant set. Do not mark it complete
merely because some evidence matched. Completely failed mappings use
`mapping_failed`. Status and relevance IDs must be consistent.

For incomplete pools, report `judged_coverage_at_k` as explicitly judged
returned IDs / actual returned IDs at K (null when there are no returned IDs).
The aggregate coverage is micro over returned IDs; quality scores are macro
over eligible questions. There is no pool-recall score masquerading as
full-paper recall. Missing labels, failed mappings and unjudged candidates
are never silently converted into quality zeros.

Only supplied, mapped, complete-relevance questions can form a scored subset.
Reports include its eligible size, individual question IDs, excluded counts
and reasons. A partial subset is not the complete 2,593-question benchmark.
With no eligible questions, metrics remain null. All conventions remain
provisional until P6 confirms or replaces the backend and exclusion policy.

## Tests and hand-calculated example

`tests/test_p1_evaluation.py` uses fictional papers and explicit labels. At K=2:

- q1 ranking `[a2, a1, a3]`, relevant `{a1, a3}`: P=.5, R=.5, RR=.5.
- q2 ranking `[b1]`, relevant `{b1}`: P=.5, R=1, RR=1.
- Macro means: **P=.5, R=.75, MRR@2=.75**.

These numbers establish arithmetic only. They say nothing about BM25 or BGE
on QASPER. Integration tests additionally verify saved-output auditing without
constructing retrievers or encoders, input rejection, and output preservation.

```powershell
& $p1Python -B -m pytest tests/test_p1_evaluation.py tests/test_p1_experiment.py -v
& $p1Python -B -m pytest -q
```

See [P1 Week 3/4](P1_WEEK3_WEEK4.md) for the actual count reconciliation,
qualitative train-only review, remote dependency evidence and verified runs.
