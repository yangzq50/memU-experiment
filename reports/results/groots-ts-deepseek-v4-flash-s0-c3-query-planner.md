# Benchmark Report: groots-ts / deepseek-v4-flash / sample=[0] / category=3

- Generated at: 2026-05-18T08:11:18+00:00
- Source JSON: `reports/results/groots-ts-deepseek-v4-flash-s0-c3-query-planner.json`
- Command: `locomo_test.py --memory-backend groots-ts --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/groots/.tmp/runs/groots_category_flash_s0_c3 --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --category 3 --max-workers 1 --analyze-on none`
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
| Sessions processed | 0 |
| Sessions skipped | 19 |
| Questions available before filter | 199 |
| Questions skipped by filter | 186 |
| Questions evaluated | 13 |
| Correct answers | 10/13 |
| Overall accuracy | 76.92% |
| Total time | 2.5m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 3 (multi-hop) | 10 | 13 | 76.92% |

## Wrong Examples

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: 没有足够信息判断Caroline是否宗教，仅项链象征信仰。
- Expected: Somewhat, but not extremely religious
- Evaluation: Evaluation result: WRONG

### Q69: What personality traits might Melanie say Caroline has?

- Category: `3 (multi-hop)`
- Generated: Brave, open, passionate about advocacy, and supportive.
- Expected: Thoughtful, authentic, driven
- Evaluation: Evaluation result: WRONG

### Q77: Would Melanie go on another roadtrip soon?

- Category: `3 (multi-hop)`
- Generated: No information available about Melanie going on a roadtrip soon.
- Expected: Likely no; since this one went badly
- Evaluation: Evaluation result: WRONG
