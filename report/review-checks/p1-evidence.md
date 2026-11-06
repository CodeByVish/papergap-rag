# P1 report evidence and review status

Status: **P1 content approved by Junlin Yin on 6 November 2026; DONE FOR DRAFT - P1 scope only.** The user explicitly confirmed the current P1 draft as final and authorized the scoped completion markers. This approval covers the P1 report content and recorded checks listed below; it does not approve the whole Q3 section or team report, certify annotation independence, or replace other members' outstanding confirmations.

## Scope and versions

- Report base: PR #53, commit `e13abd3b0e841be1fe38b769e665d6a6e1cb47cc`.
- P1 revision branch: `p1/report-review-20261106`.
- Accepted label source: PR #50, commit `f70bf95593a6b9f705674770b8c3e833ca76290c`; merged into main at `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`.
- Frozen P3 rankings and pool: `1a1dc15b824590a39c80ea11a568fbe5814a926e`.
- P2 supplied scoring code: `ceeaca8718daa0bbd2e6a9a3409b3eab6c4aa153`; package `results/p2-final-retrieval-handoff/`.
- P1 independent comparison: `results/p1-bm25-vs-dense-verification-20261105/`, run once at main commit `ad02d5103e28dbca2230555dd90e36c5cdc70f4f`.

Repository-relative result paths refer to ignored evidence supplied separately. They are not expected to exist in every checkout. Copying or rebuilding these inputs is not required to compile the checked-in report tables.

## Method evidence

`src/retrieval/bm25_retriever.py` defines BM25Okapi with `k1=1.5`, `b=0.75`, and `epsilon=0.25`. `_tokenize` extracts Unicode word tokens using `\w+` after `casefold()` for both queries and passages. This representation does not rewrite the stored passage. The ordinary `retrieve` method ranks within a selected paper and breaks score ties by passage ID.

`src/retrieval/dense_retriever.py` uses `BAAI/bge-small-en-v1.5`; the reproducible configuration in the repository README pins revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`. Only queries receive `Represent this sentence for searching relevant passages: `, including the trailing space. Both vector types are L2-normalized before exact inner-product search with per-paper FAISS `IndexFlatIP`. The implementation also has a separate corpus-wide interface; the report's evaluation scope is selected-paper retrieval.

The Dense encoder applies its own tokenizer and a 512-token input limit: `src/retrieval/dense_retriever.py` sets `max_seq_length=512` on the model, and the delivered index at `results/p1-365-40-handoff-20261102/p1-365-40-all-paper-text/p1-365-40-all-paper-text-dense/metadata.json` records the same limit and revision. Passing the passage text without BM25 preprocessing does not imply that its full content is encoded. Stored evidence remains unchanged. Chunk size is measured in words, which are not equivalent to model tokens. No isolated retrieval-effect experiment or truncation-rate estimate is added in this revision; the reranker and generator have separate input budgets.

The agent's current top-eight setting and the retrieval scoring cutoffs are different quantities. P2 supplies K=1/3/5 results, and this P1 comparison uses K=5. No agent configuration, retrieval implementation, label or ranking was changed for this revision.

## Quantitative evidence

Means come from `results/p2-final-retrieval-handoff/scored/retrieval.csv`. Differences and intervals come from `results/p1-bm25-vs-dense-verification-20261105/comparison/ablation.csv`, which matched the supplied P2 comparison CSV byte for byte. All differences use unrounded input scores.

| Metric at K=5 | BM25 | Dense | Dense minus BM25 | 95% interval | Paired questions |
| --- | ---: | ---: | ---: | --- | ---: |
| Precision | 0.4820 | 0.5270 | +0.0450 | [0.0171, 0.0728] | 200 |
| Pool recall | 0.6067 | 0.6976 | +0.0909 | [0.0419, 0.1421] | 199 |
| MRR | 0.7296 | 0.7992 | +0.0696 | [0.0168, 0.1222] | 200 |
| Pool nDCG | 0.6355 | 0.7188 | +0.0833 | [0.0366, 0.1314] | 199 |

All comparisons cover 174 papers and use 1,000 paper-cluster bootstrap resamples with seed 42. Question `06cc8fcafc0880cf69a2514bb7341642b9833041` (paper `1809.06537`) has no positive pool label: precision/MRR are zero, while pool recall/nDCG are null and excluded. Both methods have all 200 question IDs, with no unmatched question.

The pool was checked as a set: the 800 saved ranking rows (four methods times 200 questions, each with five results) yield 1,853 unique `(question_id, passage_id)` pairs, exactly matching `inputs/pairs.jsonl`. All scored top-five entries are judged. Relevance outside that union is unknown; other methods or deeper cutoffs may need additional judgments.

`src/evaluation/retrieval.py` computes an arithmetic mean over valid question scores. `src/evaluation/comparison.py` resamples 174 papers with replacement, retaining all valid paired questions from each selected paper, and averages their differences with equal weight per question occurrence. The reported percentile interval uses the 2.5th and 97.5th percentiles, with interpolation from `src/evaluation/performance.py`. Papers are resampling units, not equally weighted units of the final metric mean. These are descriptions of the existing implementation, not a new scoring or bootstrap execution.

The independent check reproduced the paired comparison from saved scores. It did not rerun retrieval, original scoring, annotation, answer generation, RAGAS or latency evaluation. Pool recall/nDCG do not measure exhaustive relevance in the full paper. The four-method table's existing rounded values are unchanged; its source and label-status caption were updated to the accepted-label delivery.

## Case D1: ConceptNet evidence retrieved by Dense

- Question ID: `042800c3336ed5f4826203616a39747c61382ba6`.
- Paper ID: `1709.05453`, *Augmenting End-to-End Dialog Systems with Commonsense Knowledge*.
- Question: "Which commonsense knowledge base are they using?"
- Final pool: nine judged passages, two relevant. Dense retrieves both at ranks 1 and 5; BM25 retrieves neither in its saved top five.
- Dense rank 1 passage: `qasper-passage-v1-8f0d9f0b0e1f9b5b23c84d5a6cb09cf020101de955945b91107a231a1050df77`.
- Dense rank 5 passage: `qasper-passage-v1-3e96b5d49a4906fb1acf4826ff2cd63fd2a5d50d2df943eee4596a547a869d04`.
- Exact rank-5 excerpt: "In our experiment, ConceptNet is used as the commonsense knowledge base."
- Saved BM25/Dense precision: 0.0/0.4; pool recall: 0.0/1.0; reciprocal rank: 0.0/1.0; pool nDCG: 0.0/0.8503449055347546.
- Evidence within the supplied package: `inputs/questions.jsonl:36`, `inputs/final_labels.jsonl:5`, `inputs/rankings.jsonl:141-142`, `inputs/pairs.jsonl:328,331`, `scored/scores.jsonl:108,708`.

## Case B1: Baseline descriptions retrieved by BM25

- Question ID: `dd81f58c782169886235c48b8f9a08e0954dd3ae`.
- Paper ID: `2003.12660`, *Towards Supervised and Unsupervised Neural Machine Translation Baselines for Nigerian Pidgin*.
- Question: "What baselines do they propose?"
- Final pool: ten judged passages, four relevant. BM25 retrieves relevant passages at ranks 3 and 5; Dense retrieves none in its saved top five.
- BM25 rank 3 passage: `qasper-passage-v1-3ec5b91ca34e75928714371868af416eec44ba86397aa6d6c5c9fa842ca70368`.
- BM25 rank 5 passage: `qasper-passage-v1-26847c6735e8f26f26ae7ab61c9485c97525600886e8fa701ae4ebca2528802a`.
- Exact rank-5 excerpt: "All baseline models were trained using the Transformer architecture".
- Saved BM25/Dense precision: 0.4/0.0; pool recall: 0.5/0.0; reciprocal rank: 0.3333333333333333/0.0; pool nDCG: 0.34620964322385606/0.0.
- Evidence within the supplied package: `inputs/questions.jsonl:8`, `inputs/final_labels.jsonl:163`, `inputs/rankings.jsonl:29-30`, `inputs/pairs.jsonl:62,64`, `scored/scores.jsonl:24,624`.

B1 qualification confirmed by the user: Dense rank 4 (`inputs/pairs.jsonl:67`) and rank 5 (`:60`) mention supervised and unsupervised models, despite being labelled non-relevant in the supplied gold. The report therefore describes performance under the recorded relevance judgments, not a complete absence of baseline-related information. Dense rank 5 is also BM25 rank 1; any future label review must handle that shared passage consistently. No label or score was changed for this clarification.

Both examples originate in the official test split; that fact alone does not establish independent project-held-out status. Every saved top-five entry is judged. Relevance comes from `inputs/final_labels.jsonl`, not the original pool `label` field. Selection was purposive, and no causal explanation or generated-answer quality is established. The full ranking beyond the saved cutoff is unknown. B1's qualified interpretation and the remaining P1 report content were approved by Junlin Yin on 6 November 2026.

## Accepted-label status and remaining ownership

The accepted manifest records 102 `human_reviewed` and 86 `human_spot_checked` disagreement resolutions. The 86 include the 66 previously unchecked suggestions, confirmed without label changes or new written reasons. The reviewer was also an annotator for 73 of 188 disagreements. AI visibility, revised-file agreement, absent reasons and prior question exposure remain material limitations. This report update does not convert those records into independent third-person adjudication or confirm any annotator's personal process.

The user authorized factual status/source updates in the shared abstract, table, annotation prose and report documentation. P2 retains ownership of hybrid/reranking conclusions and remaining paired comparisons; P3/P6 retain annotation and gold-review ownership. P4/P5 own agent, generation, performance and answer-quality evidence. Existing experiment conclusions outside P1 were retained.

Junlin Yin has approved the P1 method wording, numerical interpretation and both examples. Any new personal annotation-process statement still requires direct confirmation before insertion. The P1 approval does not mark the whole Q3 section complete.

## Primary-source citation check (6 November 2026)

The user approved the four scoped refinements: Dense input limits, pool construction, statistical definitions and primary citations. Existing experimental values, labels, case interpretations and other owners' conclusions are retained. That earlier approval authorized revision; the later P1 sign-off is recorded below.

| Citation key | Verified primary source | Supported scope |
| --- | --- | --- |
| `robertson2009bm25` | [Robertson and Zaragoza's original paper](https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf), 2009, volume 3(4), pages 333-389, DOI `10.1561/1500000019` | BM25 method background; project tokenization and parameter choices remain grounded in local code. |
| `baai2023bgesmallv15` | [BAAI model card at the pinned revision](https://huggingface.co/BAAI/bge-small-en-v1.5/blob/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/README.md) and [encoder configuration](https://huggingface.co/BAAI/bge-small-en-v1.5/blob/5c38ec7c405ec4b44b94cc5a9bb96e735b38267a/sentence_bert_config.json) | Model identity, query instruction, normalization usage and 512-token limit. |
| `young2017dialog` | [arXiv abstract record 1709.05453](https://arxiv.org/abs/1709.05453) | D1 paper identity; title, author order and first-submission year follow this record as explicitly selected by the user. |
| `ahia2020pidgin` | [arXiv abstract record 2003.12660](https://arxiv.org/abs/2003.12660) and its original paper | B1 paper identity and baseline descriptions; acceptance is for the AfricaNLP Workshop at ICLR 2020. |

D1 bibliographic qualification: the arXiv abstract record uses *Dialog* and lists Minlie Huang before Hao Zhou and Subham Biswas. The [AAAI 2018 record](https://ojs.aaai.org/index.php/AAAI/article/view/11923) and current arXiv PDF use *Dialogue* and list Minlie Huang last. Following the user's explicit choice, the report cites the arXiv abstract record with year 2017; its note records the v3 revision date in 2018. The locally supplied QASPER paper ID does not establish which PDF version was extracted. This bibliographic choice changes no paper/passage ID, quote, label or rank. The case papers support the quoted content, while retrieval ranks and relevance judgments remain supported by the local evaluation package.

## Approved explanation and diagram refinements (6 November 2026)

The user authorized five refinements: explain the BM25/Dense principles before configuration, interpret the paired effect sizes, explain project-specific preprocessing, add the Dense input limit to the offline diagram, and clarify the online critic retry path and its separate retrieval cutoff. The existing method parameters, model revision, query instruction, statistical protocol and bibliography are retained.

The saved comparison CSV gives Dense minus BM25 precision as `0.04500000000000001` and pool recall as `0.09087519125207565`. Multiplying by 100 gives 4.50 and approximately 9.09 percentage points. Since `src/evaluation/retrieval.py` defines precision as the number of relevant returned entries divided by the fixed cutoff, multiplying the mean precision difference by five gives 0.225 additional gold-positive entries per question on average. These are arithmetic interpretations of existing results, not new scoring or experimental runs. The baseline conclusion is restricted to this fixed evaluation at K=5 and does not claim better downstream answers.

The offline diagram retains the model, revision, L2 normalization and per-paper exact index while adding the 512-token input limit. The online loop starts at the generator view, matching `src/agent/generator_view.py`, and its caption distinguishes the agent's top-eight setting from retrieval evaluation at K=5. Both PNG/PDF pairs were regenerated from `scripts/draw_pipeline_charts.py`; their text and route geometry were checked. The retry annotation was split into two lines to avoid covering the revised route, with no font-size reduction.

Independent review found no required content correction. The two case passages and caveats, both result tables, the bootstrap protocol, annotation wording and the three generation-side preprocessing sentences were unchanged in that five-item revision. Its excluded optional items were not implemented at that stage. That revision preceded the P1 sign-off recorded below.

## Final two-point text polish (6 November 2026)

The user approved one sentence after the B1 Transformer quotation and paragraph breaks before `Dense retrieval uses` and `The evaluation ranks`. The new sentence states that the rank-five BM25 hit has score zero and uses passage-ID ordering among ties, so it is not evidence of a strong lexical match. `inputs/rankings.jsonl:29` and `inputs/pairs.jsonl:64` record the zero score; `src/retrieval/bm25_retriever.py:68-73,99-109` documents and implements eligibility of zero-scoring passages and passage-ID tie-breaking. The accepted relevance label, scores and original Dense qualification are retained.

The first build exposed an overfull line containing the complete model revision after the paragraph split. The user explicitly approved adding `\allowbreak` markers inside that revision, with no change to its characters, font size, parameters or prose. The final PDF retains all 40 revision characters and fits the text within the margin. No dependency was added. This is a formatting repair, not a model or configuration change.

An exact source comparison removed only the new sentence, two paragraph breaks and approved break markers to recover the preceding section byte for byte. D1, tables, statistical protocol, annotation wording, RRF symbols and both figures remained unchanged. That polish did not add an owner-completion marker; the later approval is recorded below.

## P1 owner approval (6 November 2026)

Junlin Yin explicitly accepted the current P1 report content as final and approved adding the scoped completion markers. The accepted content baseline is the 21-page PDF with SHA-256 `348880f367bda000cb6062087edf55ee26a509597a922b4eae45575ff85170b8`, produced after the two-point polish. Its sources and PDF were preserved before adding the status markers. The approval date uses Asia/Shanghai time.

| Review location | Approved P1 scope |
| --- | --- |
| Q1.1 | Consistency of the indexing diagram with the BM25/Dense implementation |
| Q3 | BM25/Dense methods, paired comparison and both contrasting examples |
| Q4.2 | Lexical and Dense preprocessing |
| Q4.6 | Sources and report wording for historical retrieval measurements |

This records acceptance of the current wording and recorded evidence; it does not claim a new timing run, final GPU performance validation or fresh manual inspection of every original record. Other owners' reviews, personal annotation-process confirmation, the group AI-use disclosure and missing member information remain open. No claim is made that all of Q3 or the team report is finished. Previous audit logs retain their revision-time status; this dated approval is the current P1 status.

## Draft verification

- Member information update (6 November 2026): Junlin Yin's matriculation number is `G2604768B`, supplied explicitly by the owner. It is entered on the cover; the README now records four remaining missing matriculation numbers. Other member details and the P1 approval baseline above are unchanged.
- Independent source reviews matched the Dense limit, pool construction, statistical definitions, unchanged table values and both case interpretations. Four primary references were checked; D1 follows the user's explicit arXiv-metadata choice.
- LaTeX compiled successfully using only the existing Tectonic 0.17.0 cache: exit code 0, 22 PDF pages. The current PDF SHA-256 is `6c7a654f9c0d95f3fc52dfc102406e0b59eb043659a9ea07285dd6f10c3cc1da`. The earlier addition of four scoped completion markers changed pagination from the approved 21-page content baseline; the member-information update preserves the resulting 22-page layout and technical content.
- No overfull/underfull boxes, undefined references, undefined citations or missing characters were reported. Non-blocking Fontconfig default-configuration and shell-escape-disabled messages remain.
- All 22 pages were rendered with PyMuPDF 2.1. Compared with the preceding owner-signoff PDF, only viewer page 1 changed; rendered pages 2-22 are byte-identical. Visual inspection confirmed the cover name/number pairing, four remaining member-number placeholders and normal table layout. The four P1 markers remain on viewer pages 3, 12, 14 and 17 (printed pages 2, 11, 13 and 16). Both diagram assets, AI-use and team-review statements remain unchanged; no whole-team completion claim was added.
- This revision changes only the cover's Junlin Yin entry, the README's member-information status and this verification record. All report sections, technical prose, D1/B1 case explanations, statistical definitions, tables, figures, citations, annotation wording and source-audit approval records retain their previous content. All 33 protected input/result files and all 286 original main-checkout files retain their previous hashes. Main's tracked content, branch heads and worktree registrations are unchanged. The pre-existing untracked root `tmp/` directory was retained. No evaluation, staging, commit, push or PR action was performed.
- The generic source-table refresh script was not executed. The local review patch and verification record were refreshed for this draft.

The P1 owner confirmation is complete for the scope above. The four highlighted completion markers identify that scope in the shared review draft; other owners' review boxes and unfinished evidence remain. Delivery through a commit, push or PR is still a separate step and was not performed by this update.
