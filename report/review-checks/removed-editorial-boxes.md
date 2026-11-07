# Editorial boxes removed from the report

## Draft status

```latex
\begin{review}{Draft status}
The retrieval comparison uses accepted pooled relevance labels and questions excluded from recorded prior development use; the agent was evaluated on the frozen held-out question list in one pre-declared run (200 questions, 40 of which the agent developer read during annotation), plus one post-hoc sensitivity run at a larger context budget, and the UI measurements remain development results. This does not establish independently held-out downstream performance. Yellow review boxes identify missing evidence, unresolved decisions and suggestions. Submission-material links are provided at the end of this report; export the final file as \texttt{24.pdf}. Pending entries are not zero scores. Overlap QA scores (EM and token F1), live RAGAS scores and the development-slice factorial ablation are reported; no reranker arm exists on the held-out questions.
\end{review}
```

## Strength and provenance of agent evidence

```latex
\begin{review}{Strength and provenance of agent evidence}
The development table and intervals are transcribed from the agent experiment contribution (jobs 50701, 50977, 51172, 51521; the cluster outputs are in the team's delivery archives). The held-out tables below are scored from job 51585 with the frozen record \texttt{configs/p4\_freeze.json}; the scoring script refused any run whose manifest differed from the record. Each configuration was run once. The recall intervals resample questions (2{,}000 resamples, seed 0); the F1 and RAGAS intervals resample papers (1{,}000 resamples, seed 42), like the paired retrieval comparison above. Part of the held-out list (40 questions) was read by the agent developer before the freeze, hence the 160-question column.
\end{review}
```

The Q5 self-check remains in `q5.tex` and is no longer included in the report. Removing these boxes does not resolve any outstanding checks recorded in them.
