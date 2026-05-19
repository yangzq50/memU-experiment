# Benchmark Report: groots-ts / gpt-5.4-mini / sample=[0] / category=None / qa_set=benchmark_sets/locomo-s0-both-wrong-v1.json

- Generated at: 2026-05-19T11:14:59+00:00
- Source JSON: `enhanced_memory_test_results_20260519_191409.json`
- Command: `locomo_test.py --memory-backend groots-ts --sample-use [0] --qa-index-set benchmark_sets/locomo-s0-both-wrong-v1.json --chat-deployment gpt-5.4-mini --eval-deployment gpt-5.4-mini --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/memU-experiment/.tmp/memory/groots-s0-both-wrong-gpt54mini-iter2-visual-fresh --build-workers 1 --qa-workers 3 --analyze-on none`
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
| Sessions processed | 0 |
| Sessions skipped | 19 |
| Questions available before filter | 199 |
| Questions skipped by filter | 168 |
| Questions evaluated | 31 |
| Correct answers | 23/31 |
| Overall accuracy | 74.19% |
| Total time | 49.2s |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 12 | 14 | 85.71% |
| 2 (temporal) | 3 | 4 | 75.00% |
| 3 (multi-hop) | 2 | 2 | 100.00% |
| 4 (open-domain) | 6 | 11 | 54.55% |

## Wrong Examples

### Q11: Where did Caroline move from 4 years ago?

- Category: `1 (single-hop)`
- Generated: Caroline moved from her home country 4 years ago; the specific country isn’t given.
- Expected: Sweden
- Evaluation: Evaluation result: WRONG

### Q58: When did Melanie make a plate in pottery class?

- Category: `2 (temporal)`
- Generated: Melanie made the plate in pottery class on August 23, 2023.
- Expected: 24 August 2023
- Evaluation: Evaluation result: WRONG

### Q66: What does Melanie do with her family on hikes?

- Category: `1 (single-hop)`
- Generated: She hikes and explores mountains and forests with her family, enjoying outdoor time together.
- Expected: Roast marshmallows, tell stories
- Evaluation: Evaluation result: WRONG

### Q85: What are Caroline's plans for the summer?

- Category: `4 (open-domain)`
- Generated: Caroline planned to do something special for summer with Melanie—either a family outing or just the two of them.
- Expected: researching adoption agencies
- Evaluation: Evaluation result: WRONG

### Q112: What did Mel and her kids paint in their latest project in July 2023?

- Category: `4 (open-domain)`
- Generated: They painted a nature-inspired canvas painting, specifically a sunflower.
- Expected: a sunset with a palm tree
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.retrieve.query_plan | 31 | 53.8s | 1.7s | 1.8s | 2.0s | 2.2s | 0 |
| memory.retrieve.search_documents | 31 | 1.0s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 5 | yes | 1.5s | 1.5s | 0.0s | When did Melanie run a charity race? |
| 11 | no | 2.0s | 1.9s | 0.0s | Where did Caroline move from 4 years ago? |
| 13 | yes | 2.2s | 2.2s | 0.0s | What career path has Caroline decided to persue? |
| 15 | yes | 1.8s | 1.8s | 0.0s | What activities does Melanie partake in? |
| 23 | yes | 1.7s | 1.6s | 0.0s | What books has Melanie read? |
| 38 | yes | 2.0s | 2.0s | 0.0s | What activities has Melanie done with her family? |
| 43 | yes | 1.8s | 1.8s | 0.0s | What kind of art does Caroline make? |
| 48 | yes | 2.0s | 1.9s | 0.0s | What types of pottery have Melanie and her kids made? |
| 49 | yes | 1.9s | 1.9s | 0.0s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 1.7s | 1.7s | 0.0s | What are Melanie's pets' names? |
| 55 | yes | 2.0s | 1.9s | 0.0s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 1.8s | 1.7s | 0.0s | What symbols are important to Caroline? |
| 57 | yes | 1.4s | 1.4s | 0.0s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 1.8s | 1.8s | 0.0s | When did Melanie make a plate in pottery class? |
| 59 | yes | 1.5s | 1.5s | 0.0s | Would Caroline be considered religious? |
| 60 | yes | 1.9s | 1.8s | 0.0s | What instruments does Melanie play? |
| 66 | no | 1.9s | 1.9s | 0.0s | What does Melanie do with her family on hikes? |
| 69 | yes | 1.9s | 1.9s | 0.0s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 2.0s | 2.0s | 0.0s | What transgender-specific events has Caroline attended? |
| 78 | yes | 1.8s | 1.8s | 0.0s | What items has Melanie bought? |
| 85 | no | 1.6s | 1.6s | 0.0s | What are Caroline's plans for the summer? |
| 112 | no | 1.8s | 1.8s | 0.0s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 1.5s | 1.4s | 0.0s | How did Melanie feel while watching the meteor shower? |
| 122 | no | 1.7s | 1.7s | 0.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 1.9s | 1.9s | 0.0s | What did Caroline make for a local church? |
| 128 | yes | 1.5s | 1.5s | 0.0s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 1.4s | 1.3s | 0.0s | What setback did Melanie face in October 2023? |
| 138 | no | 1.5s | 1.5s | 0.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 2.0s | 2.0s | 0.0s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 1.5s | 1.4s | 0.0s | How did Melanie's son handle the accident? |
| 148 | yes | 1.7s | 1.7s | 0.0s | What was Melanie's reaction to her children enjoying the Grand Canyon? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | yes | 5.2s | 3.9s | 1.2s | 1.6s | 2.4s | When did Melanie run a charity race? |
| 11 | no | 6.9s | 6.0s | 0.9s | 2.0s | 4.0s | Where did Caroline move from 4 years ago? |
| 13 | yes | 6.0s | 4.4s | 1.6s | 2.3s | 2.1s | What career path has Caroline decided to persue? |
| 15 | yes | 4.1s | 3.5s | 0.6s | 1.9s | 1.6s | What activities does Melanie partake in? |
| 23 | yes | 5.0s | 4.1s | 0.8s | 1.7s | 2.4s | What books has Melanie read? |
| 38 | yes | 4.8s | 4.0s | 0.9s | 2.1s | 1.9s | What activities has Melanie done with her family? |
| 43 | yes | 4.2s | 3.7s | 0.5s | 1.9s | 1.8s | What kind of art does Caroline make? |
| 48 | yes | 4.1s | 3.4s | 0.7s | 2.0s | 1.4s | What types of pottery have Melanie and her kids made? |
| 49 | yes | 4.5s | 3.6s | 0.8s | 2.0s | 1.7s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 5.5s | 3.7s | 1.8s | 1.8s | 1.9s | What are Melanie's pets' names? |
| 55 | yes | 6.1s | 4.9s | 1.2s | 2.0s | 2.9s | What subject have Caroline and Melanie both painted? |
| 56 | yes | 4.4s | 3.7s | 0.7s | 1.8s | 1.9s | What symbols are important to Caroline? |
| 57 | yes | 4.3s | 3.6s | 0.7s | 1.5s | 2.1s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 5.5s | 3.8s | 1.6s | 1.9s | 1.9s | When did Melanie make a plate in pottery class? |
| 59 | yes | 4.3s | 3.6s | 0.7s | 1.6s | 2.0s | Would Caroline be considered religious? |
| 60 | yes | 3.9s | 3.3s | 0.6s | 1.9s | 1.3s | What instruments does Melanie play? |
| 66 | no | 4.0s | 3.4s | 0.6s | 2.0s | 1.4s | What does Melanie do with her family on hikes? |
| 69 | yes | 4.2s | 3.5s | 0.7s | 2.0s | 1.5s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 6.0s | 5.2s | 0.8s | 2.1s | 3.1s | What transgender-specific events has Caroline attended? |
| 78 | yes | 4.3s | 3.1s | 1.1s | 1.9s | 1.3s | What items has Melanie bought? |
| 85 | no | 6.9s | 6.3s | 0.6s | 1.7s | 4.6s | What are Caroline's plans for the summer? |
| 112 | no | 4.3s | 3.7s | 0.6s | 1.9s | 1.8s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | yes | 4.2s | 3.2s | 1.0s | 1.5s | 1.7s | How did Melanie feel while watching the meteor shower? |
| 122 | no | 4.2s | 3.6s | 0.7s | 1.8s | 1.8s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | yes | 3.9s | 3.2s | 0.7s | 1.9s | 1.2s | What did Caroline make for a local church? |
| 128 | yes | 3.3s | 2.8s | 0.5s | 1.6s | 1.2s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 3.9s | 3.1s | 0.7s | 1.4s | 1.7s | What setback did Melanie face in October 2023? |
| 138 | no | 3.8s | 3.1s | 0.7s | 1.5s | 1.6s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 4.6s | 3.9s | 0.7s | 2.0s | 1.9s | How do Melanie and Caroline describe their journey through life together? |
| 144 | yes | 3.9s | 3.1s | 0.8s | 1.5s | 1.5s | How did Melanie's son handle the accident? |
| 148 | yes | 4.0s | 3.3s | 0.7s | 1.8s | 1.5s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
