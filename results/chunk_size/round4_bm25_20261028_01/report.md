# Round 4 validation

Primary: complete evidence rate at $1000$ words, declared before retrieval. New questions are the main validation group; regression and combined groups are reported separately.

| Group | Size (words) | Budget | Evidence hit | Complete evidence | Mean actual words | Exhausted |
| --- | --- | --- | --- | --- | --- | --- |
| combined | $325$ | $500$ | $115/250$ | $91/250$ | $500.00$ | $0$ |
| combined | $325$ | $1000$ | $152/250$ | $129/250$ | $999.28$ | $1$ |
| combined | $325$ | $2000$ | $203/250$ | $186/250$ | $1959.52$ | $24$ |
| combined | $365$ | $500$ | $111/250$ | $86/250$ | $500.00$ | $0$ |
| combined | $365$ | $1000$ | $156/250$ | $128/250$ | $999.28$ | $1$ |
| combined | $365$ | $2000$ | $211/250$ | $191/250$ | $1958.56$ | $24$ |
| combined | $375$ | $500$ | $112/250$ | $87/250$ | $500.00$ | $0$ |
| combined | $375$ | $1000$ | $156/250$ | $129/250$ | $999.28$ | $1$ |
| combined | $375$ | $2000$ | $208/250$ | $191/250$ | $1958.40$ | $24$ |
| new | $325$ | $500$ | $98/200$ | $75/200$ | $500.00$ | $0$ |
| new | $325$ | $1000$ | $123/200$ | $104/200$ | $999.10$ | $1$ |
| new | $325$ | $2000$ | $166/200$ | $152/200$ | $1957.38$ | $18$ |
| new | $365$ | $500$ | $97/200$ | $73/200$ | $500.00$ | $0$ |
| new | $365$ | $1000$ | $131/200$ | $106/200$ | $999.10$ | $1$ |
| new | $365$ | $2000$ | $171/200$ | $154/200$ | $1956.58$ | $18$ |
| new | $375$ | $500$ | $97/200$ | $74/200$ | $500.00$ | $0$ |
| new | $375$ | $1000$ | $131/200$ | $108/200$ | $999.10$ | $1$ |
| new | $375$ | $2000$ | $170/200$ | $155/200$ | $1956.58$ | $18$ |
| regression | $325$ | $500$ | $17/50$ | $16/50$ | $500.00$ | $0$ |
| regression | $325$ | $1000$ | $29/50$ | $25/50$ | $1000.00$ | $0$ |
| regression | $325$ | $2000$ | $37/50$ | $34/50$ | $1968.10$ | $6$ |
| regression | $365$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| regression | $365$ | $1000$ | $25/50$ | $22/50$ | $1000.00$ | $0$ |
| regression | $365$ | $2000$ | $40/50$ | $37/50$ | $1966.50$ | $6$ |
| regression | $375$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| regression | $375$ | $1000$ | $25/50$ | $21/50$ | $1000.00$ | $0$ |
| regression | $375$ | $2000$ | $38/50$ | $36/50$ | $1965.70$ | $6$ |

| New questions: left / right | View | Metric | Left only | Right only |
| --- | --- | --- | --- | --- |
| 325 / 365 | top_5 | `evidence_hit_at_5` | $6$ | $15$ |
| 325 / 365 | top_5 | `complete_evidence_at_5` | $7$ | $14$ |
| 325 / 365 | 500 | `evidence_hit` | $10$ | $9$ |
| 325 / 365 | 500 | `complete_evidence` | $8$ | $6$ |
| 325 / 365 | 1000 | `evidence_hit` | $3$ | $11$ |
| 325 / 365 | 1000 | `complete_evidence` | $7$ | $9$ |
| 325 / 365 | 2000 | `evidence_hit` | $2$ | $7$ |
| 325 / 365 | 2000 | `complete_evidence` | $6$ | $8$ |
| 325 / 375 | top_5 | `evidence_hit_at_5` | $8$ | $15$ |
| 325 / 375 | top_5 | `complete_evidence_at_5` | $9$ | $14$ |
| 325 / 375 | 500 | `evidence_hit` | $10$ | $9$ |
| 325 / 375 | 500 | `complete_evidence` | $8$ | $7$ |
| 325 / 375 | 1000 | `evidence_hit` | $3$ | $11$ |
| 325 / 375 | 1000 | `complete_evidence` | $7$ | $11$ |
| 325 / 375 | 2000 | `evidence_hit` | $4$ | $8$ |
| 325 / 375 | 2000 | `complete_evidence` | $7$ | $10$ |
| 365 / 375 | top_5 | `evidence_hit_at_5` | $4$ | $2$ |
| 365 / 375 | top_5 | `complete_evidence_at_5` | $4$ | $2$ |
| 365 / 375 | 500 | `evidence_hit` | $1$ | $1$ |
| 365 / 375 | 500 | `complete_evidence` | $1$ | $2$ |
| 365 / 375 | 1000 | `evidence_hit` | $3$ | $3$ |
| 365 / 375 | 1000 | `complete_evidence` | $3$ | $5$ |
| 365 / 375 | 2000 | `evidence_hit` | $4$ | $3$ |
| 365 / 375 | 2000 | `complete_evidence` | $4$ | $5$ |

Top-5 metrics, exact paired question IDs, group paper IDs and split counts are in `summary.json`; `summary.html` shows all group aggregates. New questions may share papers with regression questions. Small differences do not establish significance or a stable optimum. Do not redraw the sample or continue a dense search on these questions. Readability review and final configuration selection remain pending; conclusions apply to BM25 only. Shared interfaces remain `v0-proposed`.
