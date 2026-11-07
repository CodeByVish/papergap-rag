# Q4.5 evaluator and provenance notes

The numerical audit recomputed means and valid counts from saved per-question RAGAS scores and checked paired differences against the comparison CSV; no new judge run was performed.

The run-specific DashScope embedding wrapper sets `check_embedding_ctx_length=False`; the checked-in evaluator itself is unchanged and does not set this option. Preserve the wrapper with the delivery materials. Recorded settings: judge `qwen-plus-2025-12-01`, embedding `qwen3.7-text-embedding`, DashScope OpenAI-compatible endpoint, timeout 120 seconds, one worker and no automatic retries. The saved manifests retain `development` role; reconcile this metadata with the reviewed frozen-run record without implying that the observed scores change. Human sample validation and owner/evaluator review remain separate follow-ups, not missing numerical metrics.

Previous draft text retained for provenance:

```latex
\subsection{Answer-level RAG metrics (Q4.5)}
RAGAS \citep{es2024ragas} complements overlap scoring with judgments about grounding and relevance. The project runs RAGAS 0.2.15 with a live judge. Faithfulness asks whether answer claims are supported by the supplied contexts; response relevance asks whether the answer addresses the question; context precision assesses the usefulness and ordering of retrieved contexts. The judge scores the exact rendered contexts (8 passages x 1,200 characters), not the full retrieved chunks.
\begin{table}[htbp]\centering\small
\caption{Live RAGAS on the 200 held-out questions; values are means with valid-score counts. Refusals and parse-error failures are excluded from each denominator.}\label{tab:ragas}
\begin{tabularx}{\linewidth}{YYYY}\toprule
Arm & Faithfulness & Response relevance & Context precision\\\midrule
Static & 0.892 (194) & 0.854 (193) & 0.578 (194)\\
Adaptive & 0.907 (191) & 0.854 (189) & 0.577 (191)\\\bottomrule\end{tabularx}
\end{table}
Live judge. On 6 November 2026 the rendered contexts were scored with \texttt{qwen-plus-2025-12-01} as the judge and \texttt{qwen3.7-text-embedding} for response relevance, both through DashScope's OpenAI-compatible endpoint (timeout 120 s, one worker, no automatic retries). One static and two adaptive response-relevance scores were invalid. Paired differences over the 188--191 questions scored in both arms are $+0.012$ (95\% interval $-0.001$ to $0.026$) for faithfulness, $-0.003$ ($-0.008$ to $0.001$) for response relevance and $-0.002$ ($-0.015$ to $0.010$) for context precision (1,000 paper-cluster bootstrap resamples, seed 42). The intervals do not support an adaptive advantage. Judge scores are model judgments, not human verification.
\begin{review}{RAGAS prerequisites}
Record the judge \texttt{qwen-plus-2025-12-01}, embedding \texttt{qwen3.7-text-embedding}, DashScope endpoint, timeout, concurrency and retry policy. DashScope's embeddings endpoint requires \texttt{check\_embedding\_ctx\_length=False}; without it response relevance fails with a bad request, so the runner wrapper sets it. Valid-score counts are in the table; refusals, parse errors and invalid scores are excluded. These outputs still carry the \texttt{development} role label. Review a sample manually and confirm that the judge measures the intended property; P6's evaluator review remains pending.
\end{review}

```
