# Benchmark Report: groots-ts / deepseek-v4-flash / sample=[0] / category=3

- Generated at: 2026-05-18T10:42:11+00:00
- Source JSON: `reports/results/groots-ts-deepseek-v4-flash-s0-c3-full-observed.json`
- Command: `locomo_test.py --memory-backend groots-ts --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/groots/.tmp/runs/groots_observed_flash_s0_c3_v5 --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --category 3 --max-workers 1 --force-resum --analyze-on none`
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
| Correct answers | 9/13 |
| Overall accuracy | 69.23% |
| Total time | 20.3m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 3 (multi-hop) | 9 | 13 | 69.23% |

## Wrong Examples

### Q14: Would Caroline still want to pursue counseling as a career if she hadn't received support growing up?

- Category: `3 (multi-hop)`
- Generated: The context does not provide enough information to answer this counterfactual.
- Expected: Likely no
- Evaluation: Evaluation result: WRONG

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: Insufficient context to determine Caroline's religiosity; only vague reference to "faith" in a necklace.
- Expected: Somewhat, but not extremely religious
- Evaluation: Evaluation result: WRONG

### Q69: What personality traits might Melanie say Caroline has?

- Category: `3 (multi-hop)`
- Generated: Courageous and an advocate for inclusivity and acceptance.
- Expected: Thoughtful, authentic, driven
- Evaluation: Evaluation result: WRONG

### Q77: Would Melanie go on another roadtrip soon?

- Category: `3 (multi-hop)`
- Generated: Insufficient information to determine if Melanie will go on another roadtrip soon.
- Expected: Likely no; since this one went badly
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.index_source | 19 | 18.4m | 58.1s | 58.8s | 92.2s | 92.2s | 0 |
| memory.index_source.contextualize_chunk | 64 | 2.9m | 2.8s | 2.7s | 4.1s | 4.9s | 0 |
| memory.index_source.extract_chunk | 64 | 12.5m | 11.7s | 11.3s | 23.4s | 32.6s | 0 |
| memory.retrieve.query_plan | 13 | 36.1s | 2.8s | 2.6s | 5.3s | 5.3s | 0 |
| memory.retrieve.search_documents | 13 | 0.0s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |
| memory.summary.build_category | 114 | 19.4m | 10.2s | 5.0s | 31.1s | 63.7s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 2 | yes | 2.7s | 2.7s | 0.0s | What fields would Caroline be likely to pursue in her educaton? |
| 14 | no | 3.8s | 3.8s | 0.0s | Would Caroline still want to pursue counseling as a career if she hadn't received support growin |
| 22 | yes | 3.3s | 3.3s | 0.0s | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 27 | yes | 2.6s | 2.6s | 0.0s | Would Caroline pursue writing as a career option? |
| 30 | yes | 3.1s | 3.1s | 0.0s | Would Melanie be considered a member of the LGBTQ community? |
| 42 | yes | 1.9s | 1.9s | 0.0s | Would Melanie be more interested in going to a national park or a theme park? |
| 46 | yes | 2.4s | 2.4s | 0.0s | Would Melanie be considered an ally to the transgender community? |
| 50 | yes | 1.9s | 1.9s | 0.0s | What would Caroline's political leaning likely be? |
| 59 | no | 2.0s | 2.0s | 0.0s | Would Caroline be considered religious? |
| 64 | yes | 2.2s | 2.2s | 0.0s | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 69 | no | 2.7s | 2.7s | 0.0s | What personality traits might Melanie say Caroline has? |
| 77 | no | 5.3s | 5.3s | 0.0s | Would Melanie go on another roadtrip soon? |
| 81 | yes | 2.3s | 2.3s | 0.0s | Would Caroline want to move back to her home country soon? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | yes | 6.4s | 5.3s | 1.1s | 2.7s | 2.5s | What fields would Caroline be likely to pursue in her educaton? |
| 14 | no | 17.9s | 16.1s | 1.8s | 3.9s | 12.2s | Would Caroline still want to pursue counseling as a career if she hadn't receive |
| 22 | yes | 7.3s | 5.9s | 1.4s | 3.4s | 2.5s | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 27 | yes | 7.0s | 5.3s | 1.7s | 2.6s | 2.6s | Would Caroline pursue writing as a career option? |
| 30 | yes | 7.9s | 6.6s | 1.3s | 3.2s | 3.4s | Would Melanie be considered a member of the LGBTQ community? |
| 42 | yes | 5.7s | 4.5s | 1.3s | 2.0s | 2.5s | Would Melanie be more interested in going to a national park or a theme park? |
| 46 | yes | 8.9s | 7.3s | 1.7s | 2.5s | 4.8s | Would Melanie be considered an ally to the transgender community? |
| 50 | yes | 5.3s | 3.5s | 1.7s | 1.9s | 1.6s | What would Caroline's political leaning likely be? |
| 59 | no | 7.7s | 5.3s | 2.4s | 2.1s | 3.3s | Would Caroline be considered religious? |
| 64 | yes | 6.9s | 5.2s | 1.7s | 2.2s | 3.0s | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 69 | no | 8.2s | 6.6s | 1.6s | 2.7s | 3.9s | What personality traits might Melanie say Caroline has? |
| 77 | no | 9.3s | 7.7s | 1.6s | 5.4s | 2.3s | Would Melanie go on another roadtrip soon? |
| 81 | yes | 11.3s | 7.5s | 3.8s | 2.3s | 5.1s | Would Caroline want to move back to her home country soon? |
