# Q4.6 performance provenance and historical notes

The report uses `results/final/p4/held-out/performance/latency-all-200/latency_all200.json`, which records linearly interpolated percentiles over all 200 records per arm. Generic `performance/<arm>/summary.json` files summarize 198 records after excluding technical errors. These denominator choices explain why the two sets of summaries differ; no new timing run was performed.

Removed the claim that the two downgraded responses each took approximately 33 seconds: the all-200 summary's static slowest-two values are 33.2 and 77.7 seconds and do not supply corresponding question IDs. Also removed an exact decomposition of median differences into retrieval time; aggregate medians alone do not establish that decomposition. Historical retrieval timing and debugging accounts are retained below rather than repeated in the performance narrative.

Producer-reported RAGAS cost is not a complete billing-ledger reconstruction. Generator tokens exclude critic use. GPU allocation duration is not a utilization measurement.

Previous text:

```latex
\subsection{Latency, cost and scaling (Q4.6)}
End-to-end timing comes from two settings that must not be combined: the five-query demonstration in Q2.2 (school GPU, all papers, one pass) and the frozen held-out run on one A40 reported below (1{,}200 characters, 200 questions per arm). Their laptop predecessors in Q2.2 used a different model. Historical retrieval measurements on 100 training questions and the older 200/40 corpus report RRF p50/p95 of 17.57/21.34 ms versus 2,387.34/3,768.72 ms with BGE reranking. Those measurements include first-use costs and three empty results, without warm-up; they exclude setup outside retrieval calls. They should not be combined with the Q2.2 timings or interpreted as a controlled final speedup.

Per-paper exact search depends mainly on the selected paper's passages. All-papers exact vector search grows with the indexed corpus. The current service permits one active answer request and returns HTTP 429 when busy; serial demonstration throughput does not establish concurrent capacity. Local and university model serving avoids per-call API charges, but compute and energy are not free. The paid judge cost is reported below.

Final generation timing. In job 51585, answer generation on one A40 (warm engine, serial calls) had p50/p95 latency of 10.5/23.6\,s for static, 11.1/24.0\,s for adaptive and 10.5/22.2\,s for static-wide (200 questions per arm, all records; generation only, excluding model load and, for adaptive, the agent loop). The agent loop added a mean 5.6\,s per adaptive question (p95 12.3\,s). The job completed 600 arm-question records in 2\,h\,23\,min. These are observed serial timings, not a controlled throughput benchmark; startup, concurrency and cache effects remain to be measured.
\begin{review}{Final performance measurements}
Wall time, counts, percentiles and judge cost are reported below. Startup and concurrent load remain unmeasured. The generation-only static p50 above (10.5\,s) and the end-to-end static p50 in \hyperref[tab:perf]{Table~\ref*{tab:perf}} (10.6\,s) now agree, the 0.04\,s difference being retrieval time: both cover all 200 records per arm, including the two answers the validator downgraded after a parse error. The 10.1\,s in an earlier version was computed over the 198 records without them, and the two downgraded answers are among the slowest, so excluding them lowered the median. Historical cluster timings summarized in the workbook lack raw local records and are not used here as final benchmark results.
\end{review}

End-to-end timing comes from the frozen held-out run (job 51585): 200 questions per arm, one NVIDIA A40, Qwen3-8B in bfloat16 through vLLM 0.11.0, retrieval on CPU, one request at a time with the engine warm and no score cache. Latency is agent time plus generation time per question; throughput divides the questions by the wall-clock time the runner measured for each arm, not by summed latencies (\hyperref[tab:perf]{Table~\ref*{tab:perf}}). Percentiles are over all 200 records per arm, including the two answers per arm that the validator downgraded after a parse error, which are among the slowest (about 33\,s of generation each).
\begin{table}[htbp]\centering\small
\caption{Held-out end-to-end performance, 200 questions per arm, serial requests on one A40. Percentiles are over all 200 records per arm. Tokens are the generator's totals.}\label{tab:perf}
\small\begin{tabularx}{\linewidth}{>{\hsize=1.9\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y>{\hsize=0.85\hsize\linewidth=\hsize}Y}\toprule
Arm & Wall time (s) & Questions\newline /s & p50 (s) & p95 (s) & Prompt tokens & Output tokens\\\midrule
Static (8 passages) & 2{,}519 & 0.079 & 10.6 & 23.7 & 934{,}334 & 73{,}586\\
Adaptive & 3{,}583 & 0.056 & 16.5 & 32.9 & 928{,}803 & 74{,}598\\
Static-wide (15 passages) & 2{,}456 & 0.081 & 10.6 & 22.3 & 934{,}460 & 73{,}573\\\bottomrule\end{tabularx}
\end{table}
\begin{figure}[htbp]\centering
\includegraphics[width=0.92\linewidth]{images/latency-by-arm.png}
\caption{Held-out latency per question (left; agent plus generation time, one A40, serial requests) and throughput (right) by arm, the values of \hyperref[tab:perf]{Table~\ref*{tab:perf}}. The retry loop raises median latency by about 56\% and lowers throughput by about 30\%.}\label{fig:latency}
\end{figure}
Generation dominates: retrieval and fusion take 0.04\,s per question on the cluster CPU, against about 12\,s for the answer. The agent loop adds a mean 5.6\,s per question, 251 critic calls over 200 questions, and raises median latency by about 56\% (16.5 against 10.6\,s) and lowers throughput by about 30\%, for a recall gain of 0.013 (Section~\ref{sec:agent-heldout}). The critic's own token use was not recorded, so the adaptive arm's token total is a lower bound. There is no per-call monetary cost, because the model is served locally; GPU time was 2\,h 23\,min for the three arms. The RAGAS judge (Q4.5) was a paid hosted model: scoring the two arms took about 2.5 hours and cost about 0.63 Singapore dollars, as reported by the member who ran it. Concurrent throughput was not measured: calls were serial, and these figures are not a scaling benchmark.

```
