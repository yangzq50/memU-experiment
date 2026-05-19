# Benchmark Report: groots-ts / gpt-5.4-mini / sample=[0] / category=None / qa_set=benchmark_sets/locomo-s0-both-wrong-v1.json

- Generated at: 2026-05-19T10:44:00+00:00
- Source JSON: `enhanced_memory_test_results_20260519_184308.json`
- Command: `locomo_test.py --memory-backend groots-ts --sample-use [0] --qa-index-set benchmark_sets/locomo-s0-both-wrong-v1.json --chat-deployment gpt-5.4-mini --eval-deployment gpt-5.4-mini --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/memU-experiment/.tmp/memory/groots-s0-both-wrong-gpt54mini-fresh-no-summary --build-workers 1 --qa-workers 3 --analyze-on none`
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
| Correct answers | 13/31 |
| Overall accuracy | 41.94% |
| Total time | 52.1s |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 9 | 14 | 64.29% |
| 2 (temporal) | 1 | 4 | 25.00% |
| 3 (multi-hop) | 1 | 2 | 50.00% |
| 4 (open-domain) | 2 | 11 | 18.18% |

## Wrong Examples

### Q11: Where did Caroline move from 4 years ago?

- Category: `1 (single-hop)`
- Generated: Caroline moved from her home country; the specific country isn’t stated in the context.
- Expected: Sweden
- Evaluation: Evaluation result: WRONG

### Q43: What kind of art does Caroline make?

- Category: `1 (single-hop)`
- Generated: The context doesn’t say Caroline makes any specific kind of art; it only mentions she’s learning piano.
- Expected: abstract art
- Evaluation: Evaluation result: WRONG

### Q49: When did Caroline and Melanie go to a pride fesetival together?

- Category: `2 (temporal)`
- Generated: No event explicitly says Caroline and Melanie went to a pride festival together; the only joint event is their meetup on 2023-06-02.
- Expected: 2022
- Evaluation: Evaluation result: WRONG

### Q55: What subject have Caroline and Melanie both painted?

- Category: `1 (single-hop)`
- Generated: Only Melanie is shown painting a lake sunrise; no shared painted subject by Caroline is provided.
- Expected: Sunsets
- Evaluation: Evaluation result: WRONG

### Q56: What symbols are important to Caroline?

- Category: `1 (single-hop)`
- Generated: Caroline values a hand-painted bowl from a friend, symbolizing art, self-expression, and a meaningful friendship.
- Expected: Rainbow flag, transgender symbol
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.retrieve.query_plan | 31 | 56.5s | 1.8s | 1.7s | 3.4s | 3.8s | 0 |
| memory.retrieve.search_documents | 31 | 0.1s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 5 | yes | 1.6s | 1.6s | 0.0s | When did Melanie run a charity race? |
| 11 | no | 2.5s | 2.5s | 0.0s | Where did Caroline move from 4 years ago? |
| 13 | yes | 2.5s | 2.5s | 0.0s | What career path has Caroline decided to persue? |
| 15 | yes | 1.8s | 1.8s | 0.0s | What activities does Melanie partake in? |
| 23 | yes | 3.4s | 3.4s | 0.0s | What books has Melanie read? |
| 38 | yes | 1.9s | 1.9s | 0.0s | What activities has Melanie done with her family? |
| 43 | no | 1.8s | 1.8s | 0.0s | What kind of art does Caroline make? |
| 48 | yes | 1.6s | 1.6s | 0.0s | What types of pottery have Melanie and her kids made? |
| 49 | no | 1.5s | 1.5s | 0.0s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 2.3s | 2.3s | 0.0s | What are Melanie's pets' names? |
| 55 | no | 1.5s | 1.5s | 0.0s | What subject have Caroline and Melanie both painted? |
| 56 | no | 1.4s | 1.4s | 0.0s | What symbols are important to Caroline? |
| 57 | no | 1.5s | 1.5s | 0.0s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 1.4s | 1.4s | 0.0s | When did Melanie make a plate in pottery class? |
| 59 | yes | 1.3s | 1.3s | 0.0s | Would Caroline be considered religious? |
| 60 | yes | 3.8s | 3.8s | 0.0s | What instruments does Melanie play? |
| 66 | yes | 1.7s | 1.7s | 0.0s | What does Melanie do with her family on hikes? |
| 69 | no | 1.6s | 1.6s | 0.0s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 1.8s | 1.8s | 0.0s | What transgender-specific events has Caroline attended? |
| 78 | no | 1.7s | 1.7s | 0.0s | What items has Melanie bought? |
| 85 | no | 1.7s | 1.7s | 0.0s | What are Caroline's plans for the summer? |
| 112 | no | 1.8s | 1.8s | 0.0s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | no | 1.6s | 1.6s | 0.0s | How did Melanie feel while watching the meteor shower? |
| 122 | no | 1.7s | 1.7s | 0.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | no | 1.8s | 1.8s | 0.0s | What did Caroline make for a local church? |
| 128 | no | 1.5s | 1.5s | 0.0s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 1.7s | 1.7s | 0.0s | What setback did Melanie face in October 2023? |
| 138 | no | 1.4s | 1.4s | 0.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 1.7s | 1.7s | 0.0s | How do Melanie and Caroline describe their journey through life together? |
| 144 | no | 1.4s | 1.4s | 0.0s | How did Melanie's son handle the accident? |
| 148 | yes | 1.6s | 1.6s | 0.0s | What was Melanie's reaction to her children enjoying the Grand Canyon? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | yes | 4.8s | 3.7s | 1.2s | 1.7s | 2.0s | When did Melanie run a charity race? |
| 11 | no | 5.6s | 4.3s | 1.3s | 2.6s | 1.7s | Where did Caroline move from 4 years ago? |
| 13 | yes | 5.8s | 4.5s | 1.3s | 2.6s | 1.9s | What career path has Caroline decided to persue? |
| 15 | yes | 4.2s | 3.4s | 0.8s | 1.9s | 1.5s | What activities does Melanie partake in? |
| 23 | yes | 6.4s | 5.0s | 1.5s | 3.5s | 1.5s | What books has Melanie read? |
| 38 | yes | 4.7s | 3.7s | 1.0s | 1.9s | 1.8s | What activities has Melanie done with her family? |
| 43 | no | 5.0s | 4.3s | 0.7s | 1.9s | 2.4s | What kind of art does Caroline make? |
| 48 | yes | 4.3s | 3.7s | 0.6s | 1.7s | 1.9s | What types of pottery have Melanie and her kids made? |
| 49 | no | 5.3s | 4.1s | 1.2s | 1.6s | 2.5s | When did Caroline and Melanie go to a pride fesetival together? |
| 52 | yes | 4.5s | 3.6s | 0.9s | 2.4s | 1.2s | What are Melanie's pets' names? |
| 55 | no | 3.8s | 2.9s | 0.9s | 1.6s | 1.3s | What subject have Caroline and Melanie both painted? |
| 56 | no | 3.5s | 2.8s | 0.7s | 1.5s | 1.3s | What symbols are important to Caroline? |
| 57 | no | 3.9s | 3.3s | 0.7s | 1.6s | 1.7s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 4.4s | 3.6s | 0.8s | 1.5s | 2.1s | When did Melanie make a plate in pottery class? |
| 59 | yes | 4.0s | 3.3s | 0.7s | 1.4s | 1.9s | Would Caroline be considered religious? |
| 60 | yes | 5.9s | 5.2s | 0.7s | 3.8s | 1.4s | What instruments does Melanie play? |
| 66 | yes | 4.0s | 3.3s | 0.7s | 1.7s | 1.5s | What does Melanie do with her family on hikes? |
| 69 | no | 4.5s | 3.8s | 0.7s | 1.7s | 2.1s | What personality traits might Melanie say Caroline has? |
| 70 | yes | 4.5s | 3.8s | 0.8s | 1.9s | 1.9s | What transgender-specific events has Caroline attended? |
| 78 | no | 8.0s | 5.2s | 2.8s | 1.7s | 3.4s | What items has Melanie bought? |
| 85 | no | 4.4s | 3.3s | 1.1s | 1.7s | 1.5s | What are Caroline's plans for the summer? |
| 112 | no | 7.0s | 6.4s | 0.6s | 1.8s | 4.6s | What did Mel and her kids paint in their latest project in July 2023? |
| 119 | no | 4.0s | 3.3s | 0.7s | 1.7s | 1.6s | How did Melanie feel while watching the meteor shower? |
| 122 | no | 4.4s | 3.7s | 0.7s | 1.7s | 1.9s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 127 | no | 4.3s | 3.7s | 0.6s | 1.8s | 1.8s | What did Caroline make for a local church? |
| 128 | no | 4.9s | 3.6s | 1.4s | 1.6s | 2.0s | What did Caroline find in her neighborhood during her walk? |
| 135 | no | 4.1s | 3.5s | 0.6s | 1.8s | 1.7s | What setback did Melanie face in October 2023? |
| 138 | no | 4.4s | 3.5s | 0.9s | 1.5s | 2.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 142 | yes | 4.8s | 3.7s | 1.1s | 1.8s | 1.9s | How do Melanie and Caroline describe their journey through life together? |
| 144 | no | 3.9s | 2.8s | 1.1s | 1.5s | 1.3s | How did Melanie's son handle the accident? |
| 148 | yes | 5.7s | 4.4s | 1.4s | 1.6s | 2.7s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
