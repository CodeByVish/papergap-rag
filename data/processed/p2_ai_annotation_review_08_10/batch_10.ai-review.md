# Batch 10 — AI review notes

These are AI judgments, not ground truth or a second human annotation. No other annotator labels or gold answers were consulted. Disagreements need human review.

All 195 labels are filled in batch_10.md. Complete record-level reasons are in batch_10.ai-review.json. The original template is `data/processed/annotation_common_v3_markdown/annotator_A/batch_10.md` at the source commit in manifest.json.

Cases worth reviewing:

- Question 0181, record 1664, label 1: Only identifies a supplementary stop-word dataset, not the main question corpus.
- Question 0181, record 1666, label 1: Split sizes identify part of the dataset setup, but the source/name of the question corpus is absent.
- Question 0183, record 1685, label 0: News/poetry counts describe prior work, not this study's training source; 0.
- Question 0183, record 1689, label 1: Useful negative evidence: contemporary-news pretraining is explicitly not used here. The cited prior-work corpus must not be reported as this study's.
- Question 0183, record 1684, label 1: CCPC1.0 is named in corpus statistics, without an explicit train/test split in this passage.
- Question 0183, record 1692, label 0: The entire visible passage is formatting debris ('1.1.1em'); no usable evidence, 0.
- Question 0186, record 1716, label 1: Fine-tuning datasets are named; their use for testing is established more directly in 1714/1717/1720.
- Question 0186, record 1719, label 1: The passage spells the dataset 'XLNI'; this appears to be a typo for XNLI.
- Question 0188, record 1732, label 1: Expert collection/annotation is provenance information but does not identify the news sites.
- Question 0188, record 1739, label 1: Describes expert-created data rather than naming its web sources; partial evidence.
- Question 0189, record 1747, label 0: Says lexical overlap connects sentences but does not define what overlap means; 0.
- Question 0189, record 1749, label 0: Describes visualizing lexical overlap, not its definition; 0.
- Question 0190, record 1760, label 1: Electronics refers to sentiment-model training data, while evaluation uses computers, routers and speakers.
- Question 0191, record 1766, label 1: Explains training innovations, not the structural changes to the document encoder. Review if the question is restricted to architecture.
- Question 0191, record 1768, label 1: Explains training innovations, not encoder structure; review the intended scope.
- Question 0194, record 1794, label 0: Lists translation unit granularities, not the underlying MT architecture. Assigned 0 for the model-type interpretation.
- Question 0194, record 1796, label 1: Identifies SMT with BPE units, but does not specify phrase-based architecture in the visible passage. Other passages about tokenization alone were marked 0; review if 'model' means tokenization variant.
- Question 0195, record 1802, label 0: These are downstream segmentation/clustering metrics, not the intrinsic representation measures requested; 0.
- Question 0197, record 1822, label 1: Relevant only to the broad interpretation of 'information' as training data. For hotel facts specifically, see 1821.
- Question 0197, record 1824, label 1: Training-data provenance; the question is ambiguous between training information and hotel facts.
- Question 0197, record 1828, label 1: Covers user input, supplier databases and agent feedback; distinguish these sources in any answer.
- Question 0199, record 1837, label 1: Split counts total 56,216. The 250,000+ archive links are not the number of examples.
- Question 0200, record 1850, label 1: Food.com source is clear; raw counts differ from passage 1851 and are not needed for this source question.
