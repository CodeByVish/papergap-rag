# Week 4 Work Report

**English** | [简体中文](week-4-report-zn-CN.md)

Status as of 2026/11/04

## Dual relevance annotation and P6 handover

Both sets of question-passage relevance labels for the four-method evaluation pool are complete, and the statistical materials have been handed over to P6. The pool covers $200$ held-out questions and $1853$ unique pairs. All $10$ batches in each of sets A and B have been collected, providing $3706$ valid binary labels.

Collection checks confirm full question and pair coverage in both sets, with no missing or invalid labels, unknown record IDs or duplicate record IDs. Each pair has two distinct annotator identifiers, and questions, passages, sources and record IDs match the original export. File checks establish label completeness; they cannot establish that annotation was performed independently.

The handover includes completed files in `data/processed/annotation_common_v3_markdown/`, pair and native ranking mappings in `data/processed/annotation_common_v3/`, and verification results. P6 will aggregate labels and calculate pre-adjudication agreement and disagreement counts; those statistics are not yet available. Both original judgments remain preserved and joined by stable record ID. The relevant annotators will collaborate on disagreements, with the specific adjudication owner still to be confirmed.

## Four-method evaluation pool

Completed retrieval, union pooling and annotation export for BM25, Dense, Hybrid RRF and Hybrid RRF followed by BGE reranking. All four methods use the frozen `data/processed/qa_for_held_out_v2.jsonl`, the same $365/40$ passage corpus, original queries and paper-scoped retrieval, retaining each method's complete top-$5$ per question.

Each method produced $1000$ hits, with $800$ ranking rows overall and $6$–$14$ unique pairs per question after deduplication. The original three methods' $600$ passage-ID, rank and score lists match v2. BGE reranking was checked on the first $5$ saved development questions before its configuration was frozen. It scores the complete RRF union of BM25 top-$20$ and Dense top-$20$ before selecting top-$5$. No held-out content or results informed tuning, and questions were not resampled.

Annotation files contain $20$ complete questions per batch, with each set covering every unique pair. Common groups contain pairs retrieved by at least two methods; other sections show method-exclusive pairs. Sources are disclosed, while gold, scores and internal IDs are hidden. Labels were blank at export; the current files are completed.

The implementation reuses the existing pool and export entry points, adding `src/data/build_four_method_pool.py` to coordinate the fourth method's freeze and historical-rank comparison. Shared retrieval interfaces are unchanged. See the [data guide](../../data/README.md) for full configurations, fields and reproduction commands, and the [evaluation protocol](../../docs/EVALUATION.md#current-annotation-and-metric-protocol) for judging and metric definitions. Older statements there that annotation is pending are superseded by the collection status in this report.

## Held-out eligibility audit and version replacement

The pinned P1 $2593$, P2 $106$ and P3 $250$ selection questions were merged into $2654$ unique banned questions in `data/processed/qa_banned_for_held_out.jsonl`, retaining $3864$ qualifying source memberships. Source snapshots, purpose decisions and generation settings are recorded. The audit does not claim coverage of unrecorded external or P4–P6 use. Pure functional checks and normal frozen evaluation do not automatically exclude questions.

The original BM25 version was retired and a new $200$-question list was sampled and frozen. Of $3329$ gold-mapped questions, $1884$ were banned, leaving $1445$ eligible candidates. Sampling with the predeclared seed $2026102805$ produced $78$ validation and $122$ test questions across $174$ papers, with no overlap with the full ban list. Isolation is at question level; shared papers are allowed.

The three-method v2 pool contained $1532$ unique pairs and was subsequently replaced by four-method v3 for manual annotation. Old BM25 outputs, the three-method pool and related templates have been removed from the working directory; their historical bytes remain in Git. Old paths and export workflows are no longer current deliverables or instructions. Verification involving historical hashes requires a full Git clone containing the relevant commits; see the data guide.

## Paper catalog for UI selection

Completed `src/data/build_paper_catalog.py` and its CLI entry point `scripts/build_paper_catalog.py`, generating `data/processed/paper_catalog.json` from paper metadata and the actual passage corpus. The catalog contains $1168$ papers and $16187$ paper/section-name entries, covering $21360$ passages. It includes only papers and sections with passages and merges repeated section names in source order. UI integration is not yet complete.

The catalog records its `passages_file`; UI retrieval must use the same corpus, and changing the corpus requires rebuilding the catalog. Missing metadata is not inferred, and the schema remains `v0-proposed`. See the [catalog section of the data guide](../../data/README.md#dataprocessedpaper_catalogjson) for fields, build commands and data acquisition.

## Validation and remaining work

The validation record at pool completion reports $577$ passing tests and successful pool and Markdown export checks, covering frozen inputs, historical hashes, native rankings, pair mappings and blank labels at export. At catalog completion, $9$ new tests and independent count checks passed. These are saved stage-specific results; code tests were not rerun for this documentation revision.

P6 will aggregate labels and report pre-adjudication agreement and disagreement counts, followed by team adjudication and final evaluation. Metrics must join native algorithm rankings to shared final labels, never use Markdown display order. Unpooled passages remain unjudged, and pool recall is not exhaustive full-paper recall. No claim is made that the agreement requirement has been met or that final evaluation is complete.
