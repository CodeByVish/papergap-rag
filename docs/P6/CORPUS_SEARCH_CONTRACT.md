# Corpus-wide search extension — v0-proposed

User-requested product scope: default free questions search all indexed paper
text; a single-paper filter remains optional. This changes the local demo's
retrieval scope, not the dataset split policy. Review points for P1/P2/P4/P5:

| Boundary | Extension / compatibility |
| --- | --- |
| P1 | New `retrieve_corpus(query, top_k, section=None)` methods. BM25 uses global document frequencies; dense reconstructs one global FAISS space from validated persisted vectors and encodes the query once. Existing paper-scoped methods and saved-index format remain available. |
| P2 | `CorpusHybridRetriever` applies global top-20 per source, equal-weight RRF k=60, reranks the full fused union and returns top-5 by default. Real source paper/passage IDs are preserved. It never forces a quota of papers into the answer. |
| P4 | `AgentState.paper_id` is nullable: null means corpus-wide; a nonempty string means a paper filter. Corpus critic prompts identify each source's title and paper ID. Corpus retries search the corpus; the old per-paper exact section selector has no selection for null. Logs include scope and returned paper IDs. |
| P5 HTTP | `create_app(..., allow_corpus=True)` opts into omitted/null `paper_id`. The original CLI/default `allow_corpus=False` still rejects omission. Empty/invalid IDs are 400; an unknown nonempty filter returns no matches, never a corpus fallback. Authentication and the shared single-request lock cover both scopes. |
| P5 output | Canonical five-key result is unchanged. Additive wrapper `search` carries scope, filter and retrieved source-paper IDs. Citation lookup uses original passage IDs. The existing grounded prompt already renders source titles and paper IDs. |
| P6 | Local launcher opts into corpus search. Health reports `corpus_search=true`; UI defaults to All papers only for a capable API. One paper remains available. Older APIs retain the explicit paper selector. |

This is an uncommitted implementation/proposal for owner review before a shared
merge; no schema freeze is implied. No branch, commit or push is required to test.
Existing QASPER per-paper evaluation results are a different configuration from
corpus-wide retrieval. Do not compare them as if only the UI changed.

The indexed pool is the prepared development corpus: 21,360 passages from 1,168
papers. It is not the entire published literature or the all-splits text corpus.
Questions, answers and held-out labels are not part of the index. A relevant
answer may cite one or several papers; corpus-wide search does not guarantee
that every query retrieves multiple papers or that a generated claim is correct.
