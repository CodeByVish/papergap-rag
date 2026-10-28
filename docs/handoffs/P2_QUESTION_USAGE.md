# P2 question-use inventory — 28 October 2026

For P3's team-wide prior-use audit, consume `p2_used_question_ids.jsonl` in this
directory. It contains 106 distinct QASPER training-question IDs with paper IDs,
source splits and provenance paths. No question text, answers, evidence or human
labels are published here. Exclude these IDs from a proposed unseen evaluation
set; do not treat this file as relevance labels or held-out approval.

This is a conservative union of observed IDs in persisted local result JSON/JSONL,
the P2 pilot manifest and the shared ZIP's question list. Inclusion means an
input or output exists, not that every inference completed. It includes the 100
P1-supplied integration questions plus additional development inputs. Other
teammates must supply their own inventories; this is not a team-wide audit.

The 100-question list was already shared as `questions.jsonl` inside the
[Drive handoff ZIP](https://drive.google.com/file/d/1XM84LDukvCmQaNXFOBFfAW_j_JkkpWV3/view).
This inventory makes those IDs, and the additional observed P2 IDs, directly
available in GitHub. The accompanying manifest records source hashes and the
inventory hash. Local source paths describe provenance, not team-accessible links.

Two historical files were not valid JSON and could not be inspected:
`results/p2-agent-cold-20261017.json` and `results/p2-qasper-index-build.json`.
Their contents are not used to assert absence of additional question exposure.
Only exact paper/question matches were used to recover IDs where outputs lacked
question IDs. There were no unmatched real-paper query strings in parsed files.

The annotation design is a separate decision: P3 builds the data and mapping;
P2 supplies retrieval outputs; P6 coordinates assignment/evaluation, with P5
helping define relevance. Candidate-pool construction and any change to the
shared held-out protocol need agreement by those affected owners. A BM25-only
pool does not replace the project's BM25+dense hybrid retrieval system.
