# P1 question usage inventory

Owner: P1 / Junlin Yin. Prepared on **2026-10-28** for the team-wide question exclusion audit.

[p1_used_question_ids.jsonl](p1_used_question_ids.jsonl) contains **2,593 unique QASPER train question IDs across 888 papers**. Each has saved evidence of P1 BM25/Dense retrieval use. The full baseline has 5,186 query/method log rows. All three questions that returned zero hits are retained.

This is exclusion metadata: no question text, answers, evidence, passages, ranks or scores are published here. Retrieval exposure does not imply model training or human inspection of every question.

## Canonical publication hash

The published inventory uses UTF-8 without a BOM and LF line endings. Its
SHA-256, also recorded in `inventory.sha256` in the manifest, is:

```text
89be5063f405a3a63718567b793580a2bac0e2e41f7a60ac5e8c89ddc9746744
```

On **2026-10-29**, the manifest was corrected from the original local CRLF
hash (`0b50e6ee...`) to the published LF hash. The inventory already stored in
Git has not changed; all 2,593 records, including their metadata, are identical.
The manifest retains the old local hash under `publication` for provenance.
Historical source-file hashes and the original `prepared_on` date are unchanged.

The local `results/p1-question-usage-20261028/validation.json` records the original
generation check, which used CRLF bytes. It is not the corrected publication
verification. The scoped `.gitattributes` pins LF for the three P1 handoff files,
including Windows checkouts with `core.autocrlf=true`.

Verify exact bytes after cloning the corrected branch, or downloading its raw
inventory and manifest files into these paths:

```python
import hashlib
import json
from pathlib import Path

root = Path("docs/handoffs")
payload = (root / "p1_used_question_ids.jsonl").read_bytes()
manifest = json.loads((root / "p1_question_usage_manifest.json").read_bytes())
assert b"\r" not in payload and not payload.startswith(b"\xef\xbb\xbf")
actual = hashlib.sha256(payload).hexdigest()
assert actual == manifest["inventory"]["sha256"]
print(actual)
```

For future generation, write explicit LF bytes (or use `write_text` with
`encoding="utf-8", newline="\n"`) before calculating the hash. Also compare
the staged/committed inventory bytes with the manifest and verify a raw download
after publishing. The original local generation script remains historical and
uses the platform's default text newline behavior.

## Scope and provenance

The source checkout was `6828629debe89e73740a3f49037bc98bb8c65143` on `p1/week3-week4`. The ignored local experiment files have their own historical commits and SHA-256 hashes; the checkout commit does not imply that those files were tracked by Git or generated at that commit. [p1_question_usage_manifest.json](p1_question_usage_manifest.json) records each selected source and the complete saved-artifact ID coverage audit.

The authoritative exposure source is `results/p1-week3-week4-development/queries.jsonl`, rather than only the ranked-hit file. Queries with no hits are absent from that ranked-hit file. The local QA export is used only to validate ID, paper, split and original query identity; its presence is not evidence that a question was used.

The dataset revision is `fdc9d8214fbab5dd782958601db4d678e6934a54`. The historical baseline was generated from P1 `5d3f4477f42887067bb4b3f8bd9231f1bc9289e9` with uncommitted source changes recorded in its run manifest. Source split conventions remain `v0-proposed`; this delivery does not approve a final split or configuration.

## Coverage

| Evidence | Unique questions | Relation to full inventory |
| --- | ---: | --- |
| Saved BM25/Dense baseline query log | 2,593 | Complete inventory |
| Earlier P1 retrieval handoff | 100 | Subset |
| Early real-data smoke | 3 | Subset |
| Full-index smoke | 3 | Subset |
| Real-retrieval to mock-Agent integration | 4 | Subset |
| P2 CLI integration run by P1 | 3 | Subset |
| Earlier saved-ranking qualitative inspection | 3 | Subset; no answers/evidence used |
| Later Codex-assisted answer/evidence inspection | 8 | Subset; pending human review |
| Union of handoff, smoke/integration and qualitative samples | 101 | Subset |

**The previous 100-question handoff is not the complete P1 usage list.** The eight-case analysis adds one question outside that handoff, `b13d0e463d5eb6028cdaa0c36ac7de3b76b5e933`, while the full baseline covers substantially more questions. Category counts overlap and must not be added together.

The eight later cases retain the status **Codex-assisted qualitative analysis — pending human review**. They must not be represented as completed human annotations or gold relevance labels. Synthetic Week 2 queries are excluded because they have no QASPER question IDs. Agent query rewrites are associated with their original IDs.

The saved-artifact scan found no additional IDs outside the 2,593 in local `results/p1*` JSON/JSONL files. This scope cannot establish completeness for unsaved runs, other machines, other members, or later work. Indexing validation paper text is distinct from using validation questions.

## Record fields

The first five fields retain P2's field types for straightforward union by `question_id`.

| Field | Meaning |
| --- | --- |
| `question_id` | Original opaque QASPER question ID; primary join key. |
| `paper_id` | Original paper ID, validated against local QA metadata. |
| `source_split` | Official source split; `train` for every P1 record here. |
| `sources` | Sorted local artifact paths containing this question ID as usage evidence. Hashes and source categories are in the manifest. Local ignored paths are provenance references, not promises that the artifacts are in Git. |
| `usage` | `development_or_integration_exposure`, matching the P2 inventory convention. |
| `usage_categories` | Sorted exposure categories for this specific record; several may apply. |

Category definitions:

- `bm25_dense_baseline`: present in the saved full baseline query log.
- `handoff_100_questions`: included in the 100-question BM25/Dense/Hybrid handoff.
- `smoke_or_integration`: present in saved real-data smoke or integration outputs.
- `saved_ranking_qualitative_inspection`: one of the earlier three cases inspected without answers/evidence.
- `qualitative_evidence_inspected_codex_pending_human_review`: one of eight later cases with saved source packets and Codex-assisted answer/evidence analysis; human review remains pending.

## Use for held-out exclusion

Collect every member's inventory, union the original `question_id` values, and anti-join candidate held-out records against that union. For a repeated question with several candidate passages, exclude all of its question–passage records. Preserve each member's provenance separately.

```python
import json
from pathlib import Path

inventory_paths = [
    Path("docs/handoffs/p1_used_question_ids.jsonl"),
    # Add the independently obtained P2 inventory and other owners' inventories.
]
used_ids = {
    json.loads(line)["question_id"]
    for path in inventory_paths
    for line in path.read_text(encoding="utf-8").splitlines()
    if line.strip()
}

# candidate_records is the proposed held-out list, loaded separately.
eligible_records = [
    row for row in candidate_records if row["question_id"] not in used_ids
]
```

This code performs question-level exclusion only. P3/P6 must decide whether exposure to any question or paper text also excludes other questions from the same paper, and must agree the official split, question count, candidate pool and freeze manifest. No unseen-final-test or configuration-freeze claim is made here. The screenshot's reported seven overlaps have not been reproduced against a supplied held-out list.

## Independent P2 cross-check

P2's `p2/question-usage-inventory` branch at `3b13f22fe6df29d15babea529cf2fc8f13c18f68` contains 106 unique train question IDs in `docs/handoffs/p2_used_question_ids.jsonl`. A read-only ID/paper/split comparison found all 106 within this P1 inventory. That file remains P2's independent usage record and should still be collected for the team audit; it was not used to infer P1 exposure. This comparison does not establish that the team's inventory is complete.

## Verification

The generation and validation scripts/records remain local under `results/p1-question-usage-20261028/`. Verification checked unique sorted IDs, exact baseline coverage including zero-hit questions, original QA identity and split, source membership and hashes, the 101-question sample union, the independent P2 comparison, and the absence of dataset content fields in the published JSONL. No retrieval, model inference, index build or experiment rerun was needed.

`prepared_on` is the inventory delivery date. Missing historical execution timestamps or command arguments remain unrecorded; they were not reconstructed from filenames.
