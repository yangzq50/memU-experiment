# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-17T20:32:04+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 6/13 | 46.15% | 54.0s | groots-ts-deepseek-v4-flash-s0-c3.json |
| memu-text | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 12/13 | 92.31% | 35.7m | memu-text-deepseek-v4-flash-s0-c3.json |

## Error Overlap

| Metric | Value |
| --- | --- |
| Shared evaluated questions | 13 |
| Wrong only in groots-ts | 6 |
| Wrong only in memu-text | 0 |
| Wrong in both | 1 |

## Per-Backend Wrong Examples

### groots-ts

- Q14 / 3 (multi-hop): Would Caroline still want to pursue counseling as a career if she hadn't received support growing up?
  - Generated: 信息不足，上下文未说明没有支持时Caroline的意愿。
  - Expected: Likely no
- Q27 / 3 (multi-hop): Would Caroline pursue writing as a career option?
  - Generated: Insufficient information; no mention of writing as a career option in the provided context.
  - Expected: LIkely no; though she likes reading, she wants to be a counselor
- Q42 / 3 (multi-hop): Would Melanie be more interested in going to a national park or a theme park?
  - Generated: Insufficient information to determine Melanie's preference.
  - Expected: National park; she likes the outdoors
- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: 无相关信息，无法判断。
  - Expected: Somewhat, but not extremely religious
- Q64 / 3 (multi-hop): Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi?
  - Generated: Insufficient information to determine Melanie's enjoyment of Vivaldi's "The Four Seasons."
  - Expected: Yes; it's classical music
- Q69 / 3 (multi-hop): What personality traits might Melanie say Caroline has?
  - Generated: Courageous, inspiring, and amazing.
  - Expected: Thoughtful, authentic, driven
- Q77 / 3 (multi-hop): Would Melanie go on another roadtrip soon?
  - Generated: Insufficient information about roadtrips in the provided context.
  - Expected: Likely no; since this one went badly

### memu-text

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: No, the evidence is insufficient to consider Caroline religious.
  - Expected: Somewhat, but not extremely religious
