# Q4.4 scoring and run provenance

Revised prose makes best-reference scoring, macro aggregation and zero scores for refusals/errors explicit. Numerical results were checked against saved per-question scores; original answer records are external artifacts, so this was not a generation rerun or a fresh rescore of raw answers.

The earlier run-provenance text is retained below.

```latex
\subsection{Answer quality (Q4.4)}
The implemented scorer uses a proposed project policy, project QA policy, version 0 (proposed), rather than the official QASPER evaluator. It lowercases text, removes ASCII punctuation and English articles, and normalizes whitespace. Exact match compares normalized strings; token F1 uses multiset token overlap. Reference extraction supports yes/no, free-form and extractive-span annotations; mixed answerability uses available answerable references.

For scientific generative answers, overlap scores can penalize correct paraphrases and reward incomplete wording. We therefore report them with refusal behavior, failures and RAG metrics rather than treating either as a complete quality measure. Relevance labels alone do not supply answer references; QA scoring also needs the linked QASPER reference answers.

Final held-out records. Job 51585 produced 200 records for each arm. Under the project QA policy, static answered 194 questions, refused 4 and failed 2; adaptive answered 191, refused 7 and failed 2; static-wide answered 194, refused 4 and failed 2. The two failures per arm are responses downgraded after a parse error; the P5 status count records them as refusals. All 200 held-out questions have at least one answerable QASPER reference annotation, so the unanswerable subset is empty. Exact match is 0.005 for every arm; token F1 is 0.368 (static), 0.366 (adaptive) and 0.368 (static-wide). On the 160 questions P4 did not annotate, F1 is 0.369 for both static and adaptive. The point estimates show no adaptive answer-quality gain.
\begin{table}[htbp]\centering\small
\caption{Final QA on the 200 held-out questions under the project policy \texttt{p6-qa-v0-proposed}. Coverage is answered questions over the subset; parse-error failures are not counted as answered.}\label{tab:qa}
\begin{tabularx}{\linewidth}{>{\hsize=1.8\hsize\linewidth=\hsize}Y>{\hsize=0.8\hsize\linewidth=\hsize}Y>{\hsize=0.8\hsize\linewidth=\hsize}Y>{\hsize=0.8\hsize\linewidth=\hsize}Y>{\hsize=0.8\hsize\linewidth=\hsize}Y}\toprule
Arm / subset & EM & Token F1 & Unanswerable correct & Coverage\\\midrule
Static / all 200 & 0.005 & 0.368 & n/a & 194/200 (0.970)\\
Adaptive / all 200 & 0.005 & 0.366 & n/a & 191/200 (0.955)\\
Static / remaining 160 & 0.006 & 0.369 & n/a & 155/160 (0.969)\\
Adaptive / remaining 160 & 0.006 & 0.369 & n/a & 152/160 (0.950)\\\bottomrule\end{tabularx}
\end{table}
\begin{review}{Final QA run}
Scores above use job 51585 and P3's \texttt{qa.jsonl} (SHA-256 \texttt{1515fc58...}), rerun with the \texttt{held\_out} role after the team sign-off of 6 November; the numbers did not change. Paired uncertainty is in Section~\ref{sec:agent-heldout}. The agent developer saw 40 evaluation questions while annotating, hence both all 200 and the remaining 160. The review file \texttt{results/final/p4/held-out/review/final-evaluation-review.json} records, as relayed by P4, that every member confirmed no held-out question was used beyond reading it for annotation. Every question was still read by its annotators, so do not call the 160 independently held out.
\end{review}

```
