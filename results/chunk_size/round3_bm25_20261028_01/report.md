# Round 3 分块评估 / chunk-size assessment

根据本轮 `summary.json` 整理。BM25，重叠 $40$ words，同一批 $50$ 题；仅评估证据命中、证据完整和读入词数，不使用可读性评分。历史配置见 `manifest.json`。

Based on this run's `summary.json`: BM25, $40$-word overlap and the same $50$ questions. Assess evidence hits, complete evidence and input words; readability is excluded. Historical settings are in `manifest.json`.

## 定量结果 / Results

| Size (words) | Top-$5$ hit | Top-$5$ complete | Mean words |
| --- | --- | --- | --- |
| $325$ | $30/50$ | $26/50$ | $1203.84$ |
| $335$ | $28/50$ | $25/50$ | $1199.52$ |
| $345$ | $27/50$ | $25/50$ | $1220.20$ |
| $350$ | $28/50$ | $26/50$ | $1231.52$ |
| $355$ | $28/50$ | $26/50$ | $1231.32$ |
| $365$ | $33/50$ | $29/50$ | $1278.50$ |
| $375$ | $32/50$ | $28/50$ | $1291.60$ |
| $385$ | $32/50$ | $27/50$ | $1305.88$ |
| $395$ | $30/50$ | $26/50$ | $1323.06$ |
| $400$ | $30/50$ | $26/50$ | $1332.72$ |

| Size (words) | Budget (words) | Evidence hit | Complete evidence | Mean actual words | Exhausted |
| --- | --- | --- | --- | --- | --- |
| $325$ | $500$ | $17/50$ | $16/50$ | $500.00$ | $0$ |
| $325$ | $1000$ | $29/50$ | $25/50$ | $1000.00$ | $0$ |
| $325$ | $2000$ | $37/50$ | $34/50$ | $1968.10$ | $6$ |
| $335$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| $335$ | $1000$ | $27/50$ | $23/50$ | $1000.00$ | $0$ |
| $335$ | $2000$ | $37/50$ | $34/50$ | $1968.10$ | $6$ |
| $345$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| $345$ | $1000$ | $26/50$ | $23/50$ | $1000.00$ | $0$ |
| $345$ | $2000$ | $37/50$ | $35/50$ | $1967.30$ | $6$ |
| $350$ | $500$ | $15/50$ | $14/50$ | $500.00$ | $0$ |
| $350$ | $1000$ | $27/50$ | $24/50$ | $1000.00$ | $0$ |
| $350$ | $2000$ | $38/50$ | $36/50$ | $1967.30$ | $6$ |
| $355$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| $355$ | $1000$ | $25/50$ | $22/50$ | $1000.00$ | $0$ |
| $355$ | $2000$ | $38/50$ | $36/50$ | $1967.30$ | $6$ |
| $365$ | $500$ | $14/50$ | $13/50$ | $500.00$ | $0$ |
| $365$ | $1000$ | $25/50$ | $22/50$ | $1000.00$ | $0$ |
| $365$ | $2000$ | $40/50$ | $37/50$ | $1966.50$ | $6$ |
| $375$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $375$ | $1000$ | $25/50$ | $21/50$ | $1000.00$ | $0$ |
| $375$ | $2000$ | $38/50$ | $36/50$ | $1965.70$ | $6$ |
| $385$ | $500$ | $14/50$ | $12/50$ | $500.00$ | $0$ |
| $385$ | $1000$ | $26/50$ | $22/50$ | $1000.00$ | $0$ |
| $385$ | $2000$ | $39/50$ | $36/50$ | $1965.70$ | $6$ |
| $395$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $395$ | $1000$ | $26/50$ | $22/50$ | $1000.00$ | $0$ |
| $395$ | $2000$ | $38/50$ | $36/50$ | $1965.70$ | $6$ |
| $400$ | $500$ | $15/50$ | $13/50$ | $500.00$ | $0$ |
| $400$ | $1000$ | $27/50$ | $23/50$ | $1000.00$ | $0$ |
| $400$ | $2000$ | $36/50$ | $34/50$ | $1964.90$ | $6$ |

“Exhausted” 表示论文的全部分块仍不足以填满预算的问题数。两个证据指标均给出成功题数／总题数。

“Exhausted” counts questions whose papers have too few chunk words to fill the budget. Evidence metrics show successful questions divided by all sampled questions.

## 判断 / Assessment

$365$ 的 top-$5$ 两项指标最高，为 $33/50$ 和 $29/50$，比 $375$ 各多 $1$ 题，平均词数也稍少。在 $2000$ words 下，$365$ 的两项指标也最高，为 $40/50$ 和 $37/50$。但 $325$ 在 $500/1000$ words 下的两项指标仍最高。保留 $325/365/375$，用新增题验证；不凭这 $50$ 题直接宣布最优。

$365$ leads both top-$5$ metrics at $33/50$ and $29/50$, only $1$ question ahead of $375$ on each, with slightly fewer words. It also leads both metrics at $2000$ words ($40/50$ and $37/50$). However, $325$ still leads both metrics at $500/1000$ words. Validate $325/365/375$ on new questions rather than declaring an optimum from these $50$ questions.

每题占 $2$ 个百分点，小差异不能证明稳定优于其他值。以上只支持当前 BM25 条件下的比较；本轮不冻结知识库。最终选值见 Round 4 的 `report.md` 和 `experiments/chunk_size/criteria_zn-CN.md`。

Each question represents $2$ percentage points. Small differences do not establish a stable advantage. These results apply to the current BM25 setup and do not freeze the knowledge base. See Round 4's `report.md` and `experiments/chunk_size/criteria.md` for the final selection.
