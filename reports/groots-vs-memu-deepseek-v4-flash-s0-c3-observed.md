# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-18T10:05:58+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 11/13 | 84.62% | 22.9m | groots-ts-deepseek-v4-flash-s0-c3-observed.json |
| memu-text | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 12/13 | 92.31% | 35.7m | memu-text-deepseek-v4-flash-s0-c3.json |

## Error Overlap

| Metric | Value |
| --- | --- |
| Shared evaluated questions | 13 |
| Wrong only in groots-ts | 1 |
| Wrong only in memu-text | 0 |
| Wrong in both | 1 |

## Per-Backend Wrong Examples

### groots-ts

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: No, evidence is insufficient to consider Caroline religious.
  - Expected: Somewhat, but not extremely religious
- Q69 / 3 (multi-hop): What personality traits might Melanie say Caroline has?
  - Generated: Courageous, vulnerable, and open about sharing her story.
  - Expected: Thoughtful, authentic, driven

### memu-text

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: No, the evidence is insufficient to consider Caroline religious.
  - Expected: Somewhat, but not extremely religious

## Groots Memory Observability

| Backend | Spans | Total Span Time | Errors | JSON |
| --- | --- | --- | --- | --- |
| groots-ts | 26 | 40.7s | 0 | groots-ts-deepseek-v4-flash-s0-c3-observed.json |
