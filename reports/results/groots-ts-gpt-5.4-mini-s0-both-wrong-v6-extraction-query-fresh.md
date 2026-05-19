# Benchmark Report: groots-ts / gpt-5.4-mini / sample=[0] / category=None / qa_set=benchmark_sets/locomo-s0-both-wrong-v1.json

- Generated at: 2026-05-19T13:24:03+00:00
- Source JSON: `enhanced_memory_test_results_20260519_211747.json`
- Command: `locomo_test.py --memory-backend groots-ts --sample-use [0] --qa-index-set benchmark_sets/locomo-s0-both-wrong-v1.json --chat-deployment gpt-5.4-mini --eval-deployment gpt-5.4-mini --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/memU-experiment/.tmp/memory/groots-s0-v6-extraction-query-fresh --build-workers 1 --qa-workers 3 --analyze-on none`
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
| Correct answers | 24/31 |
| Overall accuracy | 77.42% |
| Total time | 6.3m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 12 | 14 | 85.71% |
| 2 (temporal) | 3 | 4 | 75.00% |
| 3 (multi-hop) | 1 | 2 | 50.00% |
| 4 (open-domain) | 8 | 11 | 72.73% |

## Wrong Examples

### Q5: When did Melanie run a charity race?

- Category: `2 (temporal)`
- Generated: Melanie ran the charity race on 2023-05-20, which was the previous Saturday.
- Expected: The sunday before 25 May 2023
- Evaluation: Evaluation result: WRONG

### Q11: Where did Caroline move from 4 years ago?

- Category: `1 (single-hop)`
- Generated: Caroline moved from her home country.
- Expected: Sweden
- Evaluation: Evaluation result: WRONG

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: Not clearly; Caroline mentions “faith,” but there’s no direct evidence she is religious.
- Expected: Somewhat, but not extremely religious
- Evaluation: Evaluation result: WRONG

### Q66: What does Melanie do with her family on hikes?

- Category: `1 (single-hop)`
- Generated: She hikes in the mountains and explores forests with her family, which brings them together and makes them happy.
- Expected: Roast marshmallows, tell stories
- Evaluation: Evaluation result: WRONG

### Q85: What are Caroline's plans for the summer?

- Category: `4 (open-domain)`
- Generated: Caroline wants to plan something special this summer—just the two of them—to catch up and explore nature.
- Expected: researching adoption agencies
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.index_source | 19 | 5.4m | 17.2s | 15.8s | 27.4s | 27.4s | 0 |
| memory.index_source.contextualize_chunk | 79 | 2.7m | 2.0s | 1.7s | 3.6s | 11.1s | 0 |
| memory.index_source.extract_chunk | 79 | 7.0m | 5.3s | 5.3s | 7.5s | 9.2s | 0 |
| memory.retrieve.query_plan | 31 | 56.4s | 1.8s | 1.8s | 2.7s | 2.7s | 0 |
| memory.retrieve.search_documents | 31 | 1.0s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 5 | no | 1.7s | 1.7s | 0.0s | When did Melanie run a charity race? |
| 11 | no | 1.8s | 1.8s | 0.0s | Where did Caroline move from 4 years ago? |
| 13 | yes | 2.1s | 2.0s | 0.0s | What career path has Caroline decided to persue? |
| 15 | yes | 2.8s | 2.7s | 0.0s | What activities does Melanie partake in? |
| 23 | yes | 1.7s | 1.7s | 0.0s | What books has Melanie read? |
| 38 | yes | 1.6s | 1.6s | 0.0s | What activities has Melanie done with her family? |
| 43 | yes | 2.0s | 2.0s | 0.0s | What kind of art does Caroline make? |
| 48 | yes | 1.5s | 1.5s | 0.0s | What types of pottery have Melanie and her kids made? |
| 49 | yes | 2.7s | 2.7s | 0.0s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 1.8s | 1.8s | 0.0s | What are Melanie's pets' names? |
| 55 | yes | 1.8s | 1.8s | 0.0s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 1.7s | 1.7s | 0.0s | What symbols are important to Caroline? |
| 57 | yes | 1.9s | 1.9s | 0.0s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | yes | 1.6s | 1.6s | 0.0s | When did Melanie make a plate in pottery class? |
| 59 | no | 1.9s | 1.9s | 0.0s | Would Caroline be considered religious? |
| 60 | yes | 1.5s | 1.5s | 0.0s | What instruments does Melanie play? |
| 66 | no | 1.5s | 1.4s | 0.0s | What does Melanie do with her family on hikes? |
| 69 | yes | 1.6s | 1.6s | 0.0s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 1.6s | 1.6s | 0.0s | What transgender-specific events has Caroline attended? |
| 78 | yes | 2.2s | 2.2s | 0.0s | What items has Melanie bought? |
| 85 | no | 1.8s | 1.8s | 0.0s | What are Caroline's plans for the summer? |
| 112 | no | 1.9s | 1.9s | 0.0s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 2.1s | 2.0s | 0.0s | How did Melanie feel while watching the meteor shower? |
| 122 | yes | 1.9s | 1.9s | 0.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 1.8s | 1.8s | 0.0s | What did Caroline make for a local church? |
| 128 | yes | 1.7s | 1.7s | 0.0s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 1.6s | 1.5s | 0.0s | What setback did Melanie face in October 2023? |
| 138 | yes | 1.7s | 1.7s | 0.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 1.9s | 1.9s | 0.0s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 1.7s | 1.7s | 0.0s | How did Melanie's son handle the accident? |
| 148 | yes | 2.0s | 2.0s | 0.0s | What was Melanie's reaction to her children enjoying the Grand Canyon? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | no | 5.0s | 3.9s | 1.2s | 1.8s | 2.1s | When did Melanie run a charity race? |
| 11 | no | 4.5s | 3.5s | 1.0s | 1.8s | 1.6s | Where did Caroline move from 4 years ago? |
| 13 | yes | 5.2s | 3.9s | 1.3s | 2.1s | 1.8s | What career path has Caroline decided to persue? |
| 15 | yes | 5.4s | 4.5s | 0.8s | 2.8s | 1.7s | What activities does Melanie partake in? |
| 23 | yes | 4.2s | 3.6s | 0.6s | 1.8s | 1.8s | What books has Melanie read? |
| 38 | yes | 4.3s | 3.4s | 0.9s | 1.7s | 1.7s | What activities has Melanie done with her family? |
| 43 | yes | 4.4s | 3.6s | 0.8s | 2.1s | 1.5s | What kind of art does Caroline make? |
| 48 | yes | 4.5s | 3.5s | 1.0s | 1.6s | 1.9s | What types of pottery have Melanie and her kids made? |
| 49 | yes | 4.7s | 4.0s | 0.7s | 2.8s | 1.3s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 4.2s | 3.4s | 0.9s | 1.9s | 1.5s | What are Melanie's pets' names? |
| 55 | yes | 3.7s | 3.0s | 0.7s | 1.9s | 1.1s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 4.4s | 3.6s | 0.8s | 1.8s | 1.8s | What symbols are important to Caroline? |
| 57 | yes | 7.8s | 6.5s | 1.3s | 2.0s | 4.5s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | yes | 4.0s | 3.3s | 0.7s | 1.7s | 1.6s | When did Melanie make a plate in pottery class? |
| 59 | no | 5.6s | 4.0s | 1.6s | 2.0s | 2.0s | Would Caroline be considered religious? |
| 60 | yes | 3.4s | 2.7s | 0.7s | 1.6s | 1.1s | What instruments does Melanie play? |
| 66 | no | 3.9s | 3.1s | 0.8s | 1.5s | 1.6s | What does Melanie do with her family on hikes? |
| 69 | yes | 4.2s | 3.5s | 0.7s | 1.7s | 1.8s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 4.4s | 3.8s | 0.6s | 1.7s | 2.1s | What transgender-specific events has Caroline attended? |
| 78 | yes | 4.2s | 3.5s | 0.7s | 2.3s | 1.2s | What items has Melanie bought? |
| 85 | no | 4.2s | 3.6s | 0.6s | 1.9s | 1.7s | What are Caroline's plans for the summer? |
| 112 | no | 4.5s | 3.5s | 1.1s | 2.0s | 1.5s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 4.5s | 3.7s | 0.8s | 2.1s | 1.6s | How did Melanie feel while watching the meteor shower? |
| 122 | yes | 4.6s | 3.8s | 0.8s | 2.0s | 1.9s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 4.1s | 3.2s | 0.8s | 1.9s | 1.4s | What did Caroline make for a local church? |
| 128 | yes | 3.9s | 3.3s | 0.7s | 1.8s | 1.5s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 4.6s | 4.0s | 0.6s | 1.6s | 2.4s | What setback did Melanie face in October 2023? |
| 138 | yes | 5.4s | 4.6s | 0.8s | 1.8s | 2.9s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 4.4s | 3.5s | 0.9s | 2.0s | 1.5s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 4.2s | 3.5s | 0.7s | 1.8s | 1.7s | How did Melanie's son handle the accident? |
| 148 | yes | 5.1s | 4.3s | 0.8s | 2.1s | 2.2s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
