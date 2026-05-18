# Benchmark Report: groots-ts / deepseek-v4-flash / sample=[0] / category=3

- Generated at: 2026-05-18T02:45:13+00:00
- Source JSON: `reports/results/groots-ts-deepseek-v4-flash-s0-c3-memory-items.json`
- Command: `locomo_test.py --memory-backend groots-ts --memory-dir .tmp/runs/groots_items_flash_s0_c3_v3 --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --category 3 --max-workers 1 --force-resum --analyze-on none`
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
| Total time | 11.0m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 3 (multi-hop) | 9 | 13 | 69.23% |

## Wrong Examples

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: Cannot be determined from provided context.
- Expected: Somewhat, but not extremely religious
- Evaluation: Evaluation result: WRONG

### Q64: Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi?

- Category: `3 (multi-hop)`
- Generated: Insufficient information to determine; no data on musical preferences in provided context.
- Expected: Yes; it's classical music
- Evaluation: Evaluation result: WRONG

### Q69: What personality traits might Melanie say Caroline has?

- Category: `3 (multi-hop)`
- Generated: Caring, empathetic, and understanding.
- Expected: Thoughtful, authentic, driven
- Evaluation: Evaluation result: WRONG

### Q77: Would Melanie go on another roadtrip soon?

- Category: `3 (multi-hop)`
- Generated: No information about roadtrips is available in the context.
- Expected: Likely no; since this one went badly
- Evaluation: Evaluation result: WRONG
