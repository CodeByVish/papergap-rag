"""Refresh report tables and source provenance from local evaluation artifacts.

Run from the repository root. This script overwrites generated report tables,
copies the recorded UI image, and updates the report source audit.
"""

import json, pathlib, shutil, hashlib
r=pathlib.Path.cwd(); out=r/'report'
sources=['results/p2-final-retrieval-handoff/scored/summary.json','results/p2-final-retrieval-handoff/scored/run_manifest.json','results/p6/annotation-audit-verified-20261105/agreement.json','results/p6-local/five-queries-20261105.json','data/gold/p6/final/final_labels_manifest.json','docs/ASSIGNMENT_WORKBOOK.md','docs/P4_REPORT_CONTRIBUTION.md','configs/p4_freeze.json']
a=json.loads((r/sources[0]).read_text())
rows=[]
for x in a:
 if x['k']==5:
  name={'Hybrid RRF followed by BGE reranking':'RRF + reranker','Hybrid RRF':'Hybrid RRF'}.get(x['arm'],x['arm'])
  rows.append(name+' & '+' & '.join(f'{x[k]:.3f}' for k in ['precision_at_k','pool_recall_at_k','mrr_at_k','pool_ndcg_at_k'])+r'\\')
(out/'tables/retrieval.tex').write_text(r'''% Source: results/p2-final-retrieval-handoff/scored/summary.json; accepted label commit f70bf95593a6b9f705674770b8c3e833ca76290c.
\begin{table}[htbp]\centering
\caption{Retrieval at $K=5$ on accepted relevance labels. Recall and nDCG are relative to the judged pool. Precision and MRR use 200 questions; pool recall and nDCG use 199.}\label{tab:retrieval}
\begin{tabular}{lrrrr}\toprule
Method & P@5 & Pool R@5 & MRR@5 & Pool nDCG@5\\\midrule
'''+ '\n'.join(rows)+r'\bottomrule\end{tabular}\end{table}'+'\n')
a=json.loads((r/sources[2]).read_text())
names={'Maheshwari Vishakha Praveen':'Maheshwari','Changyan Xu':'Xu','HU JUNYU':'Hu','Ananya Redhu':'Redhu','Jingshuai Qian':'Qian','Junlin Yin':'Yin'}
rows=[' / '.join(names[n] for n in x['annotators'])+f" & {x['n']} & {100*x['agreement']:.2f}\\% & {x['kappa']:.3f}"+r'\\' for x in a['by_human_pair']]
(out/'tables/agreement.tex').write_text(r'''\begin{table}[htbp]\centering
\caption{Agreement on submitted labels; includes human-verified AI suggestions (Section~\ref{sec:annotation}).}\label{tab:agreement}
\begin{tabular}{lrrr}\toprule
Annotator pair & Records & Agreement & Kappa\\\midrule
'''+ '\n'.join(rows)+r'\bottomrule\end{tabular}\end{table}'+'\n')
a=json.loads((r/sources[3]).read_text())
summaries=['Yes; cross-language vector mapping, checked against Google Translate','Average classification accuracy','F1: 88\\% on OntoNotes, 53\\% on Wiki(gold)','BiLSTM with max pooling','Refused: insufficient evidence']
rows=[]
for i,(x,s) in enumerate(zip(a,summaries),1):
 rows.append(f"{i} & {s} & {x['result']['retrieval_rounds']} & {len(x['result']['citations'])} & {len(x['validation']['violations'])} & {x['_http_ms']/1000:.1f}"+r'\\')
(out/'tables/five-queries.tex').write_text(r'''\begin{table}[htbp]\small\centering
\caption{Summaries of generated outputs, not verified factual answers. Warning counts are validator diagnostics.}\label{tab:five-results}
\begin{tabularx}{\linewidth}{rYrrrr}\toprule
\# & Output summary & Rounds & Cites & Warnings & Seconds\\\midrule
'''+ '\n'.join(rows)+r'\bottomrule\end{tabularx}\end{table}'+'\n')
shutil.copyfile(r/'output/playwright/p6-local-answer.png',out/'figures/ui-answer.png')
previous_audit=json.loads((out/'source-audit.json').read_text()) if (out/'source-audit.json').exists() else {}
manifest={'note':'Report source audit, not an experiment manifest. Generated/raw results remain outside Git.','sources':{p:hashlib.sha256((r/p).read_bytes()).hexdigest() for p in sources},'handout_sha256':hashlib.sha256((r.parent/'Assignment.pdf').read_bytes()).hexdigest()}
if 'p1_review_update' in previous_audit:
 manifest['p1_review_update']=previous_audit['p1_review_update']
(out/'source-audit.json').write_text(json.dumps(manifest,indent=2)+'\n')
