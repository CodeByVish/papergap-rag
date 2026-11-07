# Q3 revision note

Q3 is reorganized around the retrieval problems, evaluation, illustrative queries, chunk/depth choices and resulting configuration. All numerical result tables and the pipeline/depth figures are retained. Shared bootstrap details are explained once. Wording presents reranking as a tested configuration with mixed query-level effects and lower aggregate scores, rather than emphasizing failure. Retrieval evidence gains remain distinct from generated-answer gains. Annotation limitations, pooling scope, denominators and evaluation exposure are retained or cross-referenced.

## Supporting implementation and provenance details

- Dense checkpoint: `BAAI/bge-small-en-v1.5`, revision `5c38ec7c405ec4b44b94cc5a9bb96e735b38267a`.
- Query-only prefix: `Represent this sentence for searching relevant passages: `, including its trailing space. Stored passage text is unchanged.
- BM25 uses BM25Okapi with epsilon 0.25, k1 1.5 and b 0.75; equal scores are resolved by passage ID.
- Reranking uses raw cross-encoder logits, maximum length 512 and batch size eight in the documented CPU setup.
- Dense truncation audit: 4,099/28,617 all-paper passages (14.3%), 3,142/21,360 development passages (14.7%), and 14/45 development gold passages (31%) exceed 512 tokens. The effect on retrieval was not isolated.
- Rankings: commit `1a1dc15`; accepted labels: `f70bf95` (PR #50). Prior BM25–Dense comparison verification reproduced the saved comparison CSV byte for byte; this was not a retrieval rerun or new annotation review.
- Chunk search: Round 1, 100/200/400 words; Round 2, nine sizes at 25-word intervals; Round 3, ten sizes within 325–400; final candidates 325/365/375. Overlap was fixed at 40.
- Depth example: rankings from development job 50977; generated answer from job 51690. Original P1/P2 case identifiers remain in `p1-evidence.md`, `p2-evidence.md` and source comments. Historical approvals retain their original scopes; no new owner approval is claimed.

## Short note for teammates

Revised Q3 to make each retrieval change's purpose, evidence and final design decision easier to follow. Kept the result tables and figures, consolidated repeated evaluation explanations, and moved detailed run/configuration provenance to review notes. Query examples now present both benefits and trade-offs in neutral language. The findings and numerical results are unchanged; recovered retrieval evidence is not presented as a demonstrated answer-quality gain. No experiments were rerun.
