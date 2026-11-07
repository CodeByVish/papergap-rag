Scored: held-out 200, 2500 chars (post-hoc) (200 questions, development)

| metric | static | adaptive | static-wide |
| --- | ---: | ---: | ---: |
| questions | 200 | 200 | 200 |
| errors | 0 | 0 | 0 |
| answer_errors | 0 | 0 | 0 |
| mean_rounds | 1.000 | 1.360 | 1.000 |
| mean_passages | 7.965 | 8.250 | 13.945 |
| questions_with_gold | 200 | 200 | 200 |
| recall_before_retries | 0.858 | 0.858 | 0.953 |
| recall_after_retries | 0.858 | 0.865 | 0.953 |
| full_recall_recovery_rate | 0.000 | 0.022 | 0.000 |
| gap_detected | 21 | 37 | 20 |
| critic_gap_recovery_rate | 0.000 | 0.108 | 0.000 |
| retries | 0 | 72 | 0 |
| unnecessary_retry_rate | n/a | 0.583 | n/a |
| ineffective_retry_rate | n/a | 0.958 | n/a |
| redundant_retry_rate | n/a | 0.389 | n/a |
| refusal_rate | 0.000 | 0.005 | 0.000 |
| correct_refusal_rate | n/a | n/a | n/a |
| false_refusal_rate | 0.000 | 0.005 | 0.000 |
| unsatisfied_rate_unanswerable | n/a | n/a | n/a |
| unsatisfied_rate_answerable | 0.105 | 0.165 | 0.100 |
| critic_reused_rate | 0.000 | 0.132 | 0.000 |
| critic_llm_rate | 0.000 | 0.953 | 0.000 |
| critic_fallback_rate | 0.000 | 0.047 | 0.000 |
| critic_thinking_drift_rate | 0.000 | 0.000 | 0.000 |
| mean_elapsed_s | 0.029 | 4.159 | 0.025 |
Plain retrieval (the question as the query) at each depth, from the static-wide arm:

| depth | mean recall | questions with full recall |
| ---: | ---: | ---: |
| 3 | 0.569 | 84/200 |
| 5 | 0.723 | 117/200 |
| 8 | 0.858 | 154/200 |
| 10 | 0.897 | 166/200 |
| 15 | 0.953 | 183/200 |
| adaptive, 8.25 passages on average | 0.865 | |

Refuse if the critic is still unsatisfied after the last round (not enabled): refuses n/a of unanswerable and 0.165 of answerable questions; meets the proposed gate (>= 0.5, <= 0.05): False.

Critic audit (adaptive arm):

| critic verdict / situation | count | reading |
| --- | ---: | --- |
| insufficient/gold complete | 41 | over-strict: all gold was in view |
| insufficient/gold missing | 28 | correct: gold not retrieved yet |
| sufficient/gold complete | 136 | correct |
| sufficient/gold missing | 31 | false accept: gold not retrieved |

verdicts asked of the model, with gold or unanswerable: 236
verdict sources: fallback 11, llm 225, reused 36
sufficient verdicts by what they cite: a gold passage 141, no gold passage 18
