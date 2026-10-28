# P5 question-usage inventory (2026-10-28)

This is P5's input to the team-wide held-out exclusion audit. It answers one question:
**which QASPER questions has P5 actually used, and are any of them outside P1's inventory?**

## Result

P5 used **100 train-split questions**, all from P1's 100-question handoff. **All 100 are
already in P1's 2,593-question inventory; P5 adds no new QASPER question IDs.**

| item | value |
|---|---:|
| P5 QASPER questions | 100 |
| papers | 93 |
| source split | `train` 100 |
| in P1 inventory | 100 |
| not in P1 inventory | **0** |
| synthetic benchmark IDs excluded | 8 (`bench-b01` … `bench-b08`) |

The 8 `bench-*` IDs are fictional SciReader/SQuAD samples in `examples/` and the Week-2
benchmark. They are not QASPER questions, so they cannot overlap the held-out QASPER pool;
they are listed separately in `p5_question_usage_manifest.json` rather than dropped
silently.

## Files

| file | content |
|---|---|
| `p5_used_question_ids.jsonl` | one row per question, with paper id, split, the run files that used it, and usage categories |
| `p5_question_usage_manifest.json` | counts, hashes, the P1 cross-check and the synthetic exclusions |

Provenance covers Week-3 evidence binding (both backends), Week-4 AgentState fixtures,
Week-5 v7 quality runs, and the Week-6 R4 BGE run (the cluster artefact is recorded as a
source even though its answers file is not in this checkout).

## Cross-module audit

| module | inventory | count | overlap with P1 | note |
|---|---|---:|---:|---|
| P1 | `docs/handoffs/p1_used_question_ids.jsonl` (branch `p1/week3-week4`, commit `f0f861b`) | 2,593 | — | all `train`; includes the handoff 100 |
| P2 | `docs/handoffs/p2_used_question_ids.jsonl` (branch `p2/question-usage-inventory`) | 106 | 106/106 | all `train`; subset of P1 |
| P3 | `data/processed/annotation_pilot_multi_v1/questions.jsonl` (branch `p3-qasper-foundation`) | 5 | 3/5 | 3 `train`, **2 `validation`** |
| P4 | no separate file | — | — | uses P1's 100-question handoff and the same AgentState fixtures |
| P5 | this inventory | 100 | 100/100 | all `train`; adds 0 |
| P6 | held-out pool not frozen | — | — | `evaluation.held_out_manifest` is null |

**The only new development exposure found is P3's two validation pilot questions:**

- `0ab3df10f0b7203e859e9b62ffa7d6d79ffbbe50`
- `729694a9fe1e05d329b7a4078a596fe606bc5a95`

They are not in P1's inventory because P1's scope is `train`. P6 must include them in the
team-wide exclusion union, even though the current split proposal maps `validation` to
validation and `test` to held-out: a question that has been inspected/annotated in a pilot
must not reappear as a held-out evaluation question.

**Union found so far: 2,595 IDs** = P1's 2,593 + P3's 2 validation pilot questions. P5
adds zero. Both P1 and P2 describe their inventories as scoped to saved local artefacts,
not as a complete team inventory; unsaved or external runs can still add IDs.

## Proposed held-out pool overlap (must be cleaned before freeze)

P3's `annotation_held_out` manifest on `p3-qasper-foundation`
(`data/processed/annotation_held_out/manifest.json`, schema `v0-proposed`, 200 questions
/ 1,000 pairs) was audited against the development inventories:

| overlap | count |
|---|---:|
| held-out questions also in P1's train inventory | **95 / 200** |
| held-out questions P5 already answered | **7 / 200** |
| held-out questions in P2's inventory | 7 |
| held-out questions in P3's pilot | 0 |
| held-out questions not in P1's train inventory | 105 |

The seven P5-exposed questions are:

- `00bcdffff7e055f99aaf1b05cf41c98e2748e948`
- `00ef9cc1d1d60f875969094bb246be529373cb1d`
- `0106bd9d54e2f343cc5f30bb09a5dbdd171e964b`
- `0427ca83d6bf4ec113bc6fec484b2578714ae8ec`
- `04f72eddb1fc73dd11135a80ca1cf31e9db75578`
- `06095a4dee77e9a570837b35fc38e77228664f91`
- `09a993756d2781a89f7ec5d7992f812d60e24232`

All seven appeared in the Week-3 evidence run, the Week-5 v7 run and the Week-6 R4 run.
They cannot serve as held-out evaluation questions. The manifest is `v0-proposed`, so the
correction belongs **before** P6 freezes the pool: rebuild from the held-out split only,
or remove the full 2,595-ID development union. The machine-readable report is
`docs/handoffs/p5_held_out_overlap.json`.

## One upstream integrity note

P1's manifest declares `inventory.sha256 = 0b50e6ee…`, but the committed JSONL hashes to
`89be5063…`. The difference is line endings: the declared hash is the CRLF serialisation of
the same 2,593 rows. The audit compared question IDs, so the result is unaffected, but P1
should publish the LF hash (or state the canonicalisation) so the integrity check is
reproducible across platforms.

## For P6

- Exclude the 2,595-ID union from the held-out question pool.
- Add P5's manifest to the audit record; no P5-only IDs need resolution.
- If a future P5 run (R4-v2, agent trace, annotation calibration) uses a question not in
  this inventory, add it before the freeze.
