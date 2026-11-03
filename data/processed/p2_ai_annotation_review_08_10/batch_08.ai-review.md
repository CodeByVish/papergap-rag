# Batch 08 — AI comparison notes

These are AI judgments, not ground truth or a second human annotation. No other annotator labels or gold answers were consulted. Disagreements need human review.

All 191 labels are filled in batch_08.md. Complete record-level reasons are in batch_08.ai-review.json. The original template is `data/processed/annotation_common_v3_markdown/annotator_A/batch_08.md` at the source commit in manifest.json.

Cases worth reviewing:

- Question 0141, record 1291, label 1: The citation marker does not reveal an actual download address. Review whether this partial publication pointer is sufficient.
- Question 0141, record 1295, label 0: The game URL is not explicitly a dataset-download location; assigned 0.
- Question 0142, record 1307, label 1: Seq2seq is discussed with their experimental failures but not listed in the final comparison table in this passage.
- Question 0144, record 1322, label 0: Metric identities were replaced by INLINEFORM placeholders. Assigned 0 rather than guessing missing names.
- Question 0144, record 1326, label 0: Refers to four measures, but none is readable by name. Assigned 0.
- Question 0145, record 1333, label 1: This is a loss-function baseline rather than one of the four architecture baselines. Included as partial evidence for the broad question.
- Question 0145, record 1340, label 0: Reports loss and pooling ablations rather than the explicitly designated baseline systems. Assigned 0; review if baseline is meant broadly.
- Question 0145, record 1335, label 0: Discusses pooling comparisons and the proposed architecture, not the explicitly designated baseline methods. Assigned 0.
- Question 0151, record 1385, label 1: Question has a potentially false premise: this is a survey organized by objective function, not a new objective that teaches literature.
- Question 0151, record 1386, label 1: Same premise ambiguity: relevant to explaining survey organization, not a literature-understanding training objective.
- Question 0151, record 1387, label 1: Same premise ambiguity: conclusion explains the survey purpose.
- Question 0152, record 1399, label 0: BIO conversion is described for HAREM, not a direct statement about discontiguous entities in SESAME. Assigned 0.
- Question 0152, record 1404, label 1: BIO format supports a contiguity inference, but does not explicitly state whether discontinuous entities exist or were flattened. Human review needed.
- Question 0153, record 1411, label 1: Prior baseline systems are named, but not every listed baseline is claimed to be SOTA.
- Question 0153, record 1414, label 1: Names prior Static-RNN, without explicitly claiming it was state of the art. Human review needed for the scope of this question.
- Question 0155, record 1428, label 0: Two annotations per instance is not the total number of annotators who participated. Assigned 0 for the total-participant interpretation.
- Question 0155, record 1430, label 1: Six trial experts and five agreement annotators refer to different subsets; do not present either as total crowdsourcing participation.
- Question 0156, record 1440, label 1: F metric subscript is missing; readable F-measure evidence is partial.
- Question 0158, record 1463, label 0: P@N ablation improvements over a selective-attention baseline are not the requested improvements over the named previous SOTA systems. Assigned 0.
- Question 0159, record 1470, label 0: Background defines dropout variants but does not establish they were used by this study. Assigned 0; passage 1468 states actual use.
- Question 0160, record 1474, label 1: Common Crawl is a crawl archive, not an individual crawled site. This passage gives inclusion criteria rather than a complete website list.
- Question 0160, record 1476, label 1: Identifies the archive/source, not specific crawled websites. Partial evidence only.
- Question 0160, record 1478, label 1: Gives domain-selection constraints, not named sites. Partial evidence only.
- Question 0160, record 1480, label 0: These are LID training sources, not the websites selected for the main web crawl. Assigned 0.
- Question 0160, record 1481, label 0: These are LID training/evaluation sources, not the websites selected for the main web crawl. Assigned 0.
