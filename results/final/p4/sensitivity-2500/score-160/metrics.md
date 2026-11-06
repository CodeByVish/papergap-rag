Scored: 160 not annotated, 2500 (160 questions, development)

| metric | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| questions | 160 | 160 | 160 |
| errors | 0 | 0 | 0 |
| answer_errors | 0 | 0 | 0 |
| mean_rounds | 1.000 | 1.337 | 1.000 |
| mean_passages | 7.975 | 8.256 | 13.969 |
| questions_with_gold | 160 | 160 | 160 |
| recall_before_retries | 0.881 | 0.881 | 0.959 |
| recall_after_retries | 0.881 | 0.888 | 0.959 |
| full_recall_recovery_rate | 0.000 | 0.030 | 0.000 |
| gap_detected | 15 | 28 | 14 |
| critic_gap_recovery_rate | 0.000 | 0.107 | 0.000 |
| retries | 0 | 54 | 0 |
| unnecessary_retry_rate | n/a | 0.667 | n/a |
| ineffective_retry_rate | n/a | 0.981 | n/a |
| redundant_retry_rate | n/a | 0.370 | n/a |
| refusal_rate | 0.000 | 0.006 | 0.000 |
| correct_refusal_rate | n/a | n/a | n/a |
| false_refusal_rate | 0.000 | 0.006 | 0.000 |
| unsatisfied_rate_unanswerable | n/a | n/a | n/a |
| unsatisfied_rate_answerable | 0.094 | 0.156 | 0.087 |
| critic_reused_rate | 0.000 | 0.131 | 0.000 |
| critic_llm_rate | 0.000 | 0.946 | 0.000 |
| critic_fallback_rate | 0.000 | 0.054 | 0.000 |
| critic_thinking_drift_rate | 0.000 | 0.000 | 0.000 |
| mean_elapsed_s | 0.030 | 4.075 | 0.025 |
Plain retrieval (the question as the query) at each depth, from the static-wide arm:

| depth | mean recall | questions with full recall |
| ---: | ---: | ---: |
| 3 | 0.585 | 69/160 |
| 5 | 0.749 | 98/160 |
| 8 | 0.881 | 127/160 |
| 10 | 0.907 | 134/160 |
| 15 | 0.959 | 148/160 |
| adaptive, 8.26 passages on average | 0.888 | |

Refuse if the critic is still unsatisfied after the last round (not enabled): refuses n/a of unanswerable and 0.156 of answerable questions; meets the proposed gate (>= 0.5, <= 0.05): False.

Critic audit (adaptive arm):

| critic verdict / situation | count | reading |
| --- | ---: | --- |
| insufficient/gold complete | 35 | over-strict: all gold was in view |
| insufficient/gold missing | 16 | correct: gold not retrieved yet |
| sufficient/gold complete | 111 | correct |
| sufficient/gold missing | 24 | false accept: gold not retrieved |

verdicts asked of the model, with gold or unanswerable: 186
verdict sources: fallback 10, llm 176, reused 28
sufficient verdicts by what they cite: a gold passage 116, no gold passage 12
