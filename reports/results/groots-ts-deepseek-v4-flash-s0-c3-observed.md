# Benchmark Report: groots-ts / deepseek-v4-flash / sample=[0] / category=3

- Generated at: 2026-05-18T10:05:58+00:00
- Source JSON: `reports/results/groots-ts-deepseek-v4-flash-s0-c3-observed.json`
- Command: `locomo_test.py --memory-backend groots-ts --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/groots/.tmp/runs/groots_observed_flash_s0_c3_v3 --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --category 3 --max-workers 1 --force-resum --analyze-on none`
- Backend: `groots-ts`
- Chat model: `deepseek-v4-flash`
- Eval model: `deepseek-v4-flash`
- Data file: `data/locomo10.json`
- Sample: `[0]`
- Category: `3 (multi-hop)`

## Summary

| Metric | Value |
| --- | --- |
| Successful samples | 1 |
| Sessions processed | 19 |
| Sessions skipped | 0 |
| Questions available before filter | 199 |
| Questions skipped by filter | 186 |
| Questions evaluated | 13 |
| Correct answers | 11/13 |
| Overall accuracy | 84.62% |
| Total time | 22.9m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 3 (multi-hop) | 11 | 13 | 84.62% |

## Wrong Examples

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: No, evidence is insufficient to consider Caroline religious.
- Expected: Somewhat, but not extremely religious
- Evaluation: The generated answer directly contradicts the gold answer by stating "No" instead of acknowledging a moderate level of religiousness.

### Q69: What personality traits might Melanie say Caroline has?

- Category: `3 (multi-hop)`
- Generated: Courageous, vulnerable, and open about sharing her story.
- Expected: Thoughtful, authentic, driven
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.retrieve.query_plan | 13 | 40.7s | 3.1s | 3.1s | 3.8s | 3.8s | 0 |
| memory.retrieve.search_documents | 13 | 0.0s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 2 | yes | 3.3s | 3.3s | 0.0s | What fields would Caroline be likely to pursue in her educaton? |
| 14 | yes | 2.7s | 2.7s | 0.0s | Would Caroline still want to pursue counseling as a career if she hadn't received support growin |
| 22 | yes | 3.1s | 3.1s | 0.0s | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 27 | yes | 2.7s | 2.7s | 0.0s | Would Caroline pursue writing as a career option? |
| 30 | yes | 3.8s | 3.8s | 0.0s | Would Melanie be considered a member of the LGBTQ community? |
| 42 | yes | 2.9s | 2.9s | 0.0s | Would Melanie be more interested in going to a national park or a theme park? |
| 46 | yes | 3.0s | 3.0s | 0.0s | Would Melanie be considered an ally to the transgender community? |
| 50 | yes | 3.2s | 3.1s | 0.0s | What would Caroline's political leaning likely be? |
| 59 | no | 3.0s | 3.0s | 0.0s | Would Caroline be considered religious? |
| 64 | yes | 3.4s | 3.4s | 0.0s | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 69 | no | 3.3s | 3.3s | 0.0s | What personality traits might Melanie say Caroline has? |
| 77 | yes | 2.8s | 2.8s | 0.0s | Would Melanie go on another roadtrip soon? |
| 81 | yes | 3.4s | 3.4s | 0.0s | Would Caroline want to move back to her home country soon? |
