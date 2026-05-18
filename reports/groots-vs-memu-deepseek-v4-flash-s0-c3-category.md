# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-18T08:03:08+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 8/13 | 61.54% | 46.9m | groots-ts-deepseek-v4-flash-s0-c3-category.json |
| memu-text | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 12/13 | 92.31% | 35.7m | memu-text-deepseek-v4-flash-s0-c3.json |

## Error Overlap

| Metric | Value |
| --- | --- |
| Shared evaluated questions | 13 |
| Wrong only in groots-ts | 4 |
| Wrong only in memu-text | 0 |
| Wrong in both | 1 |

## Per-Backend Wrong Examples

### groots-ts

- Q14 / 3 (multi-hop): Would Caroline still want to pursue counseling as a career if she hadn't received support growing up?
  - Generated: The context does not provide enough information to determine Caroline's hypothetical decision.
  - Expected: Likely no
- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: 基于现有信息，无法判断Caroline是否宗教。
  - Expected: Somewhat, but not extremely religious
- Q64 / 3 (multi-hop): Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi?
  - Generated: Insufficient information to determine Melanie's likely enjoyment of Vivaldi's "The Four Seasons."
  - Expected: Yes; it's classical music
- Q69 / 3 (multi-hop): What personality traits might Melanie say Caroline has?
  - Generated: Supportive, brave, compassionate, and advocacy-oriented.
  - Expected: Thoughtful, authentic, driven
- Q77 / 3 (multi-hop): Would Melanie go on another roadtrip soon?
  - Generated: Insufficient information. No roadtrip events are mentioned in the provided context.
  - Expected: Likely no; since this one went badly

### memu-text

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: No, the evidence is insufficient to consider Caroline religious.
  - Expected: Somewhat, but not extremely religious
