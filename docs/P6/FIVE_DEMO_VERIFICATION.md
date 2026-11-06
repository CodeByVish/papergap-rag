# Five development-demo verification

Verification date: 6 November 2026 (Singapore). UI checkout: `P6/UI-improvement`,
`7bd2243`. This is an AI-assisted technical verification, not P4/P5 human approval
or final GPU acceptance. Shared schemas and split mappings remain `v0-proposed`.

## Selection and purpose

Keep the existing five P3 development-pilot questions in their original order.
They are a convenience demonstration sample, not a random accuracy sample or a
held-out evaluation. Official source splits are train, validation, validation,
train and train; their use in the development pilot determines their project use.

| # | Paper ID | Question ID | Question |
| --- | --- | --- | --- |
| 1 | 1912.10167 | 30c6d34b878630736f819fd898319ac4e71ee50b | Are any experiments performed to try this approach to word embeddings? |
| 2 | 1911.07555 | 0ab3df10f0b7203e859e9b62ffa7d6d79ffbbe50 | What evaluation metric is used? |
| 3 | 1904.10503 | 729694a9fe1e05d329b7a4078a596fe606bc5a95 | What results do they achieve using their proposed approach? |
| 4 | 1904.05584 | 65ad17f614b7345f0077424c04c94971c831585b | Which model architecture do they use to obtain representations? |
| 5 | 1912.01046 | 5bcc12680cf2eda2dd13ab763c42314a26f2d993 | What evaluation metrics were used in the experiment? |

Use **One paper**, not All papers, for these paper-dependent questions. Preserve
failures and warnings rather than selecting replacements after seeing answers.

## Reference and passage review

The original 5 November outputs were checked against their cited passage text
and only the five matching QASPER reference records at P3 `1a1dc15b`.

- Query 1: affirmative answer and method/evaluation details are supported. Two
  additional citations are not linked to provenance claims.
- Query 2: average classification accuracy is supported. One reference also
  includes execution performance; do not claim that the short answer covers
  every annotation detail. The critic still requested missing results.
- Query 3: the reported OntoNotes 88% and Wiki(gold) 53% F1 values and additional
  category results match the cited Results passage.
- Query 4: BiLSTM with max pooling matches the reference and cited section.
  The evidence map omits that valid citation although critic support includes it.
- Query 5: the reference is answerable. Retrieved passages contain tolerance
  accuracy, accuracy/MRR and pipeline accuracy. Refusal is a missed answer,
  not a successful unanswerable example.

In the earlier 6 November run, prompt rendering omitted the metric statements
from three retrieved passages, including the sentence quoted by the critic.
The critic could: `scripts/p6_local.py` then left it on the 3,000-character pool
view. A later local replay reproduced the same refusal, critic quote and 4,461
prompt tokens as `run-5.json`, which confirms clipping as the cause in this local
setup. Passing the generator's view to the critic alone did not produce an answer;
raising the budget to 2,500 did. See
[Fresh 2,500-character run](#fresh-2500-character-run). The cluster demo and frozen
evaluation runs already give the critic the generator's view.

## Fresh live UI results

All five submissions completed through the current UI's AppTest harness against
the live Ollama API. Each answer string was identical to the saved 5 November
answer. No UI exceptions or citation lookup errors occurred. All seven citation
IDs resolved, matched the selected paper and appeared in the retrieval log.
All five runs survived the UI export; exported records omit agent traces as
designed. Sources had nonempty resolved passage objects.

| # | Answer HTTP seconds | Citations | UI citation seconds | Outcome |
| --- | ---: | ---: | ---: | --- |
| 1 | 108.176 | 4 | 0.0051 | Answer with provenance warnings |
| 2 | 56.365 | 1 | 0.0080 | Answer despite critic insufficiency; provenance warning |
| 3 | 95.810 | 1 | 0.0042 | Supported answer, no validator warnings |
| 4 | 62.425 | 1 | 0.0041 | Supported answer, evidence-map warning |
| 5 | 42.831 | 0 | Not applicable | Model refusal despite available full-passage evidence |

Mean answer HTTP latency was 73.121 s; median was 62.425 s. Sum of the five
measured calls was 365.607 s. Dividing five by that sum gives a serial-call rate
estimate of 0.01368 requests/s, not independently measured batch throughput.
Seven retrieval calls had median 53.192 ms and range 13.614–260.291 ms.
These are fresh measurements, not corrections to the old 122.7-second mean.
The service was already warm; no cold-start comparison is established.

Setup: Apple M5, 24 GiB, local Ollama `qwen3:14b`, 8,192-token context,
1,024-token completion budget, top-8 hybrid retrieval, BGE reranking disabled.
The corpus contains 28,617 passages from 1,584 papers. Model digest and prompt
version are preserved in the raw answer records. Corpus/index metadata hashes
and dependency versions are in `environment.json`.

The running backend's startup metadata names `ff233c0` with then-uncommitted
changes. Comparing its recorded Python source hashes to this checkout found
only `src/ui/app.py` different; backend sources match. The fresh AppTest run
uses the current UI source. Do not label the server a clean `7bd2243` build.

Local UI/API/view-model regression validation: 51 tests passed. This validates
the tested UI behavior and does not establish answer accuracy on a broader set.

A separate actual-browser query-4 call completed in 37.438 s and displayed its
supporting source text, paper link and retrieval ranks. Pending controls were
disabled; Sources, Flagged, Pipeline and Debug were inspected. The Run JSON
download was read back successfully (one completed run with citation evidence).
This browser call is excluded from the five-call statistics. Debug exposes
backend records and progress, not the exact generator input prompt.

The Save screenshot button returned from Saving to its idle label, but the
automation did not receive a downloadable PNG (a bounded download wait timed
out). A browser screenshot was visually inspected, but no PNG is included in the
handoff bundle. Screenshot download is therefore not accepted as passed.

## Fresh 2,500-character run

**Final demo setting: `P6_MAX_CHARS_PER_PASSAGE=2500`.** Use this for the demo.

Run on 6 November 2026, saved separately in ignored
`results/p6-ui-verification-20261106-2500-premerge/`. **Label: pre-merge, local
override, 2,500 characters.** It covers the same five questions and order.

The critic and generator both read 8 passages of at most 2,500 characters, set by
`P6_MAX_CHARS_PER_PASSAGE=2500`; `runtime.json` records the effective budget. The
shared default had not yet adopted that override and P5's `p5/context-2500` branch was not merged.
The source was `e2fe038` with the `scripts/p6_local.py` change later committed as
`904e7f4`, so `source.json` shows one modified file.

| # | Outcome | Citations | Change from the 6 November run | Validator warnings |
| --- | --- | ---: | --- | --- |
| 1 | Answered | 1 | New answer; was 4 citations | `UNCOVERED_REQUIRED_COMPONENT`, `PROVENANCE_OVERSTATED` |
| 2 | Answered | 1 | Same answer | `GENERATED_WITH_INSUFFICIENT_EVIDENCE`, `PROVENANCE_OVERSTATED` |
| 3 | Answered | 1 | Same answer | None |
| 4 | Answered | 1 | Same answer | `UNCOVERED_REQUIRED_COMPONENT` |
| 5 | Answered: accuracy and MRR | 1 | Was refused | `UNCOVERED_REQUIRED_COMPONENT` |

Query 2's critic still reported `MISSING_RESULT` in all three rounds, so clipping
does not explain that verdict.

Query 1's new answer was checked against its cited passage and QASPER reference
record at P3 `1a1dc15b`. Its "yes" matches the reference. Its method description
is supported by the cited Results ::: Accuracy passage, with one simplification:
the English word's Google translation is checked against the 20 words nearest the
predicted embedding. The cited passage does not state "yes" outright, which fits
the `PROVENANCE_OVERSTATED` warning, and the reference's evidence is a different
sentence (the Europarl dataset). Treat it as supported, keeping the warning.

All citation IDs resolved, matched the selected paper and appeared in the retrieval
log. No UI evidence errors occurred.

Largest prompt: 5,549 tokens, within the 8,192-token context. Answer HTTP mean was
126.0 s and median 113.8 s. Do not compare these timings with the runs above or
attribute the difference to the budget: another local service was running and this
API had just started.

This run used AppTest, not a browser, and five development questions do not
establish an accuracy change. Its rendering configuration differs from the earlier evaluation settings, so
label it accordingly. Repeat a short confirmation after P5's change is merged. The
evidence ZIP below does not contain this run; share it separately.

## Reproduce the live UI verification

Prepare the local runtime using [the E2E guide](P6_REAL_ENV_E2E_GUIDE.md), including
the matching corpus/index, model and development samples. The preparation entry
point is `./scripts/p6-local.sh setup`; it requires the documented dependencies,
P3 reference and model availability. Never put credentials in this document.

Start the service and UI in one terminal:

```bash
printf 'P6_MAX_CHARS_PER_PASSAGE=2500\n' >> .env.p6.local
./scripts/p6-local.sh start
```

Skip the first line if `.env.p6.local` already sets it. In another terminal, from the repository root:

```bash
.venv-p6/bin/python -m scripts.verify_p6_demo \
  --output results/p6-ui-verification-NEW-RUN
```

The output directory must not already exist. The script runs the actual current
Streamlit source with AppTest against the real HTTP API, submits five fresh
questions serially, and saves each run immediately. It does not mock inference,
automatically retry questions or overwrite earlier evidence. It also checks
POST `/passages` using the UI client's correct `{"ids": [...]}` request shape.
Avoid other inference requests while this serial verification runs.

AppTest verifies UI execution/state/rendered text, not browser layout. For visual
acceptance, open the UI, select One paper and the appropriate paper, enter a
question, submit once, and inspect Answer, Sources, Flags and Pipeline. A repeated
browser call is a separate run and must not be mixed into the five-call timing.

## Artifact handoff and Git policy

The script and this document are outside ignored directories and can be reviewed
and committed normally. No `.gitignore` exception is necessary for them.

Raw runs, exports, rendered text, citation text, environment records and the
renderer reproduction remain under ignored `results/p6-ui-verification-20261106/`.
The local evidence ZIP is `results/p6-ui-verification-20261106.zip`. Share it via
the team's approved data/results channel; do not commit it. A teammate must
receive that ZIP separately to inspect the exact saved run evidence.

The bundle contains per-question `run-N.json`, `rendered-N.json` and
`citation-lookup-N.json`; `checks.json`; the sanitized `ui-export.json`;
`source.json`, `health.json` and `environment.json`; and
`query5-renderer-audit.json`. It excludes credentials, the corpus, models and
indexes. A checksum manifest accompanies the evidence. UI exports deliberately
omit agent traces, so use the raw local run records when reviewing the critic.

## Remaining approvals and operational checks

1. P4/P5 should review the critic/evidence-map warnings, the query-5 context
   mismatch and the answer-support findings. This document does not supply their
   approval. Any prompt/chunk-selection fix requires a separately recorded run.
2. Rehearse the school GPU service and tunnel if the report claims final GPU UI
   acceptance or performance. Laptop timings cannot establish that claim.
3. Share the local evidence ZIP and record its accessible team link in the final
   submission materials. Verify access from a teammate's account.
4. Review and commit the script/document/workbook changes on this task branch,
   obtain another member's review and follow CONTRIBUTING.md for the PR.
5. Confirm the 2,500 run after P5's merge.
6. Manually test Save screenshot in your normal browser, check the resulting
   PNG, and add the final screenshot to the report materials. If no file is
   downloaded, use the browser console to investigate the capture/download path.

The original 5 November and fresh 6 November measurements must remain separate.
Do not update an old run's evidence to imply that an earlier citation request
succeeded.
