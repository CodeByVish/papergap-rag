# Held-out context-budget ablation — job 51705 (8 x 2,500 characters)

`COMPLETED`, exit 0, elapsed **1:49:19** on TC2N04 (L40S). Code `012ae82`.

Inputs and settings are identical to job 51585 except the character budget:
the same 200 held-out items (sha `84e909e7…`), all-paper-text corpus
(`8eeef011…`), the same dense index, `TOP_K=8`, `WIDE_K=15`,
`CANDIDATE_K=20`, `MAX_RETRIES=2`, `SCOPED=1`, `OFFLINE=1`, `BGE=0`,
`ANSWERS=p5`, `CRITIC=generator`, `CRITIC_VIEW=generator`,
`max_new_tokens=1024`, prompt `p5-grounded-qa-v7`.
Only `MAX_CHARS_PER_PASSAGE` differs: **2,500** here, 1,200 in 51585.

## Side by side with 51585 (same 200 questions)

| | 51585 static | 51705 static | 51585 adaptive | 51705 adaptive | 51585 static-wide | 51705 static-wide |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| answered | 194 | 193 | 191 | 192 | 194 | 193 |
| refused | 6 | 7 | 9 | 8 | 6 | 7 |
| downgraded | 2 | 3 | 2 | 4 | 2 | 3 |
| mean citations | 1.75 | 1.88 | 1.81 | 1.89 | 1.75 | 1.88 |
| answer chars, median | 116.5 | 122 | 127 | 123.5 | 116.5 | 122 |
| prompt tokens, min–max | 3,225–5,732 | 3,449–7,258 | 2,626–5,587 | 3,449–7,258 | 3,225–5,732 | 3,449–7,258 |
| mean rounds | 1.000 | 1.000 | 1.440 | 1.360 | 1.000 | 1.000 |
| retries | 0 | 0 | 88 | 72 | 0 | 0 |
| whole-job elapsed | 2:23:09 | 1:49:19 | | | | |

`static` and `static-wide` answers are identical by design: `select_passages`
caps the rendered context at 8 even when the wide arm retrieved 15.

## Validator differences

| code | 51585 static / adaptive | 51705 static / adaptive |
| --- | ---: | ---: |
| CITATION_PROVENANCE_MISMATCH (warning) | 23 / 24 | **15 / 19** |
| PROVENANCE_OVERSTATED (warning) | 69 / 69 | 64 / 66 |
| UNCOVERED_REQUIRED_COMPONENT (warning) | 45 / 44 | 42 / 40 |
| UNSUPPORTED_CLAIM (warning) | 4 / 5 | 5 / 5 |
| UNSUPPORTED_NUMERIC_CLAIM (error) | 0 / 0 | **1 / 1** |
| PARSE_ERROR (error) | 2 / 2 | 2 / **3** |

So 2,500 reduces citation/provenance mismatch, but introduces one unsupported
numeric claim (an extra downgrade) and one extra parse error in the adaptive arm.

Status flips on the same questions: static 2 refused→answered, 3 answered→refused
(net −1 answered); adaptive 4 refused→answered, 3 answered→refused (net +1).
122–125 of 200 answer texts differ.

## What P6 needs to do

Score **both** runs against gold on the same 200 questions: answer exact match /
token F1 / ROUGE-L, evidence F1, citation precision/recall, and refusal rates on
answerable and unanswerable questions. The items file carries no gold at
generation time; the gold mapping is P6's.

## Reporting recommendation

Job 51585 (8/1,200) remains the pre-registered primary result. Job 51705
(8/2,500) is a separately labelled sensitivity analysis on the same held-out
questions. The report should show both rows and state the trade-off above;
2,500 should not be described as the only held-out run.
