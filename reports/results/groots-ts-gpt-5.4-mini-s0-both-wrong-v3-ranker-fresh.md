# Benchmark Report: groots-ts / gpt-5.4-mini / sample=[0] / category=None / qa_set=benchmark_sets/locomo-s0-both-wrong-v1.json

- Generated at: 2026-05-19T11:26:40+00:00
- Source JSON: `enhanced_memory_test_results_20260519_192042.json`
- Command: `locomo_test.py --memory-backend groots-ts --sample-use [0] --qa-index-set benchmark_sets/locomo-s0-both-wrong-v1.json --chat-deployment gpt-5.4-mini --eval-deployment gpt-5.4-mini --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/memU-experiment/.tmp/memory/groots-s0-both-wrong-gpt54mini-iter3-ranker-fresh2 --build-workers 1 --qa-workers 3 --force-resum --analyze-on none`
- Backend: `groots-ts`
- Chat model: `gpt-5.4-mini`
- Eval model: `gpt-5.4-mini`
- Data file: `data/locomo10.json`
- Sample: `[0]`
- QA index set: `benchmark_sets/locomo-s0-both-wrong-v1.json`
- Category: `all`

## Summary

| Metric | Value |
| --- | --- |
| Successful samples | 1 |
| Sessions processed | 19 |
| Sessions skipped | 0 |
| Questions available before filter | 199 |
| Questions skipped by filter | 168 |
| Questions evaluated | 31 |
| Correct answers | 22/31 |
| Overall accuracy | 70.97% |
| Total time | 6.0m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 10 | 14 | 71.43% |
| 2 (temporal) | 2 | 4 | 50.00% |
| 3 (multi-hop) | 2 | 2 | 100.00% |
| 4 (open-domain) | 8 | 11 | 72.73% |

## Wrong Examples

### Q11: Where did Caroline move from 4 years ago?

- Category: `1 (single-hop)`
- Generated: Caroline moved from her home country.
- Expected: Sweden
- Evaluation: Evaluation result: WRONG

### Q43: What kind of art does Caroline make?

- Category: `1 (single-hop)`
- Generated: Caroline makes paintings and drawings, often of flowers, self-portraits, and trans identity-themed art.
- Expected: abstract art
- Evaluation: Evaluation result: WRONG

### Q49: When did Caroline and Melanie go to a pride fesetival together?

- Category: `2 (temporal)`
- Generated: They went together at last year’s Pride festival — in 2021.
- Expected: 2022
- Evaluation: Evaluation result: WRONG

### Q55: What subject have Caroline and Melanie both painted?

- Category: `1 (single-hop)`
- Generated: No specific subject is stated for both; they only both helped make a painting together.
- Expected: Sunsets
- Evaluation: Evaluation result: WRONG

### Q58: When did Melanie make a plate in pottery class?

- Category: `2 (temporal)`
- Generated: Melanie made the flower-decorated pottery plate on August 23, 2023.
- Expected: 24 August 2023
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.index_source | 19 | 5.1m | 16.2s | 14.8s | 26.7s | 26.7s | 0 |
| memory.index_source.contextualize_chunk | 79 | 2.1m | 1.6s | 1.6s | 2.3s | 3.0s | 0 |
| memory.index_source.extract_chunk | 79 | 7.0m | 5.3s | 5.1s | 8.0s | 10.5s | 0 |
| memory.retrieve.query_plan | 31 | 58.0s | 1.9s | 1.7s | 2.6s | 5.0s | 0 |
| memory.retrieve.search_documents | 31 | 1.0s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 5 | yes | 1.7s | 1.7s | 0.0s | When did Melanie run a charity race? |
| 11 | no | 1.7s | 1.7s | 0.0s | Where did Caroline move from 4 years ago? |
| 13 | yes | 1.8s | 1.8s | 0.0s | What career path has Caroline decided to persue? |
| 15 | yes | 1.9s | 1.9s | 0.0s | What activities does Melanie partake in? |
| 23 | yes | 1.7s | 1.7s | 0.0s | What books has Melanie read? |
| 38 | yes | 1.9s | 1.8s | 0.0s | What activities has Melanie done with her family? |
| 43 | no | 1.7s | 1.7s | 0.0s | What kind of art does Caroline make? |
| 48 | yes | 1.9s | 1.9s | 0.0s | What types of pottery have Melanie and her kids made? |
| 49 | no | 1.9s | 1.9s | 0.0s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 1.7s | 1.6s | 0.0s | What are Melanie's pets' names? |
| 55 | no | 5.0s | 5.0s | 0.0s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 1.8s | 1.8s | 0.0s | What symbols are important to Caroline? |
| 57 | yes | 1.9s | 1.9s | 0.0s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 2.0s | 2.0s | 0.0s | When did Melanie make a plate in pottery class? |
| 59 | yes | 1.7s | 1.7s | 0.0s | Would Caroline be considered religious? |
| 60 | yes | 2.6s | 2.5s | 0.0s | What instruments does Melanie play? |
| 66 | no | 1.7s | 1.6s | 0.0s | What does Melanie do with her family on hikes? |
| 69 | yes | 2.6s | 2.6s | 0.0s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 2.0s | 2.0s | 0.0s | What transgender-specific events has Caroline attended? |
| 78 | yes | 1.5s | 1.5s | 0.0s | What items has Melanie bought? |
| 85 | no | 1.9s | 1.9s | 0.0s | What are Caroline's plans for the summer? |
| 112 | no | 1.8s | 1.8s | 0.0s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 1.7s | 1.7s | 0.0s | How did Melanie feel while watching the meteor shower? |
| 122 | yes | 1.6s | 1.6s | 0.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 1.8s | 1.7s | 0.0s | What did Caroline make for a local church? |
| 128 | yes | 1.2s | 1.2s | 0.0s | What did Caroline find in her neighborhood during her walk? |
| 135 | yes | 1.6s | 1.5s | 0.0s | What setback did Melanie face in October 2023? |
| 138 | no | 1.7s | 1.7s | 0.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 1.6s | 1.6s | 0.0s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 1.5s | 1.5s | 0.0s | How did Melanie's son handle the accident? |
| 148 | yes | 1.7s | 1.7s | 0.0s | What was Melanie's reaction to her children enjoying the Grand Canyon? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | yes | 5.0s | 4.0s | 1.0s | 1.8s | 2.2s | When did Melanie run a charity race? |
| 11 | no | 5.1s | 4.0s | 1.1s | 1.8s | 2.2s | Where did Caroline move from 4 years ago? |
| 13 | yes | 5.1s | 4.0s | 1.1s | 1.9s | 2.1s | What career path has Caroline decided to persue? |
| 15 | yes | 4.5s | 3.8s | 0.7s | 2.0s | 1.8s | What activities does Melanie partake in? |
| 23 | yes | 4.3s | 3.5s | 0.8s | 1.7s | 1.8s | What books has Melanie read? |
| 38 | yes | 4.8s | 3.7s | 1.0s | 1.9s | 1.8s | What activities has Melanie done with her family? |
| 43 | no | 4.1s | 3.4s | 0.7s | 1.8s | 1.6s | What kind of art does Caroline make? |
| 48 | yes | 4.3s | 3.6s | 0.7s | 2.0s | 1.7s | What types of pottery have Melanie and her kids made? |
| 49 | no | 4.4s | 3.7s | 0.7s | 2.0s | 1.7s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 4.3s | 3.6s | 0.7s | 1.7s | 1.8s | What are Melanie's pets' names? |
| 55 | no | 7.5s | 6.5s | 1.0s | 5.1s | 1.4s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 4.7s | 3.6s | 1.1s | 1.9s | 1.7s | What symbols are important to Caroline? |
| 57 | yes | 4.7s | 3.8s | 0.9s | 2.0s | 1.8s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 4.7s | 3.8s | 0.9s | 2.1s | 1.7s | When did Melanie make a plate in pottery class? |
| 59 | yes | 4.7s | 3.8s | 0.9s | 1.8s | 2.0s | Would Caroline be considered religious? |
| 60 | yes | 4.6s | 4.0s | 0.5s | 2.6s | 1.4s | What instruments does Melanie play? |
| 66 | no | 5.5s | 3.4s | 2.1s | 1.7s | 1.7s | What does Melanie do with her family on hikes? |
| 69 | yes | 5.0s | 4.1s | 0.9s | 2.7s | 1.4s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 5.7s | 4.5s | 1.2s | 2.1s | 2.4s | What transgender-specific events has Caroline attended? |
| 78 | yes | 3.7s | 3.0s | 0.6s | 1.6s | 1.4s | What items has Melanie bought? |
| 85 | no | 4.3s | 3.6s | 0.7s | 2.0s | 1.6s | What are Caroline's plans for the summer? |
| 112 | no | 5.8s | 5.1s | 0.7s | 1.9s | 3.2s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 4.2s | 3.5s | 0.7s | 1.8s | 1.7s | How did Melanie feel while watching the meteor shower? |
| 122 | yes | 4.4s | 3.2s | 1.1s | 1.7s | 1.5s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 3.7s | 3.1s | 0.6s | 1.8s | 1.3s | What did Caroline make for a local church? |
| 128 | yes | 3.8s | 3.0s | 0.8s | 1.3s | 1.7s | What did Caroline find in her neighborhood during her walk? |
| 135 | yes | 4.3s | 3.5s | 0.9s | 1.6s | 1.8s | What setback did Melanie face in October 2023? |
| 138 | no | 4.3s | 3.5s | 0.8s | 1.7s | 1.8s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 5.1s | 4.3s | 0.8s | 1.7s | 2.6s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 4.3s | 3.5s | 0.8s | 1.6s | 1.9s | How did Melanie's son handle the accident? |
| 148 | yes | 4.3s | 3.6s | 0.6s | 1.8s | 1.8s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
