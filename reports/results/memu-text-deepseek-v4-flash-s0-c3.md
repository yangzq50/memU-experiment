# Benchmark Report: memu-text / deepseek-v4-flash / sample=[0] / category=3

- Generated at: 2026-05-17T20:32:04+00:00
- Source JSON: `reports/results/memu-text-deepseek-v4-flash-s0-c3.json`
- Command: `locomo_test.py --memory-backend memu --memory-dir .tmp/runs/memu_rebuilt_flash_s0_c3_noemb --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --category 3 --max-workers 1 --force-resum --analyze-on none --disable-embeddings`
- Backend: `memu-text`
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
| Correct answers | 12/13 |
| Overall accuracy | 92.31% |
| Total time | 35.7m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 3 (multi-hop) | 12 | 13 | 92.31% |

## Wrong Examples

### Q59: Would Caroline be considered religious?

- Category: `3 (multi-hop)`
- Generated: No, the evidence is insufficient to consider Caroline religious.
- Expected: Somewhat, but not extremely religious
- Evaluation: Evaluation result: WRONG
