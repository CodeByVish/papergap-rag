# Batch 09 — AI review notes

These are AI judgments, not ground truth or a second human annotation. No other annotator labels or gold answers were consulted. Disagreements need human review.

All 177 labels are filled in batch_09.md. Complete record-level reasons are in batch_09.ai-review.json. The original template is `data/processed/annotation_common_v3_markdown/annotator_A/batch_09.md` at the source commit in manifest.json.

Cases worth reviewing:

- Question 0161, record 1487, label 1: Wikipedia is the corpus used for extracting patterns/embeddings; the labeled evaluation pairs come from WordNet/Wordnik (1484).
- Question 0163, record 1501, label 0: Describes approaches in prior literature, not explicit comparisons conducted in this study; 0.
- Question 0163, record 1502, label 0: Prior-work methods are not automatically procedures explored in this experiment; 0.
- Question 0163, record 1505, label 0: A background taxonomy of meta-learning is not evidence they experimentally tried all its methods; 0.
- Question 0163, record 1500, label 1: Names an evaluated alternative, MTL-NLG, but does not explain its training procedure.
- Question 0164, record 1515, label 1: Literature is proposed future work, not an evaluated domain.
- Question 0166, record 1530, label 1: Lists the selected languages rather than giving all typology names; useful partial evidence.
- Question 0166, record 1540, label 0: Lists dataset languages but does not specify their morphological typologies; 0 under the literal question.
- Question 0167, record 1543, label 1: MT-RNN is recurrent; the separately listed GRNN is recursive. Do not conflate them.
- Question 0168, record 1551, label 1: Summarizes linked information but does not give the nearest-patch matching rule; partial evidence.
- Question 0169, record 1555, label 0: Plans to expand to other languages do not identify the current language; 0.
- Question 0169, record 1563, label 0: English describes another study's tweets, not necessarily this study's dataset; 0.
- Question 0169, record 1564, label 1: English explicitly describes the Dabiq corpus. It does not establish the language inventory of all Twitter datasets.
- Question 0171, record 1579, label 1: Interpreted 'the other two' as the two Vietnamese datasets compared with English-sportball. The text does not establish two additional datasets besides UIT-ViIC.
- Question 0174, record 1600, label 0: Examples of tasks from prior work do not establish the five tasks evaluated here; 0.
- Question 0174, record 1602, label 1: Gives broad task categories/entailment, not the complete five-task list.
- Question 0176, record 1617, label 1: 130 initially collected; 110 retained. The answer depends on whether the question asks original collection or final corpus.
- Question 0176, record 1618, label 0: 574K is a count of lyric texts, not the collected audio songs asked about; 0.
- Question 0178, record 1636, label 0: Background describes related image-to-poem/style-transfer work; it does not explicitly establish the models selected in this study; 0.
