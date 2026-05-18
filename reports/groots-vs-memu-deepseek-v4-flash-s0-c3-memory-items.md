# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-18T02:45:13+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 9/13 | 69.23% | 11.0m | groots-ts-deepseek-v4-flash-s0-c3-memory-items.json |
| memu-text | deepseek-v4-flash | deepseek-v4-flash | [0] | 3 (multi-hop) | 199 | 186 | 13 | 12/13 | 92.31% | 35.7m | memu-text-deepseek-v4-flash-s0-c3.json |

## Error Overlap

| Metric | Value |
| --- | --- |
| Shared evaluated questions | 13 |
| Wrong only in groots-ts | 3 |
| Wrong only in memu-text | 0 |
| Wrong in both | 1 |

## Per-Backend Wrong Examples

### groots-ts

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: Cannot be determined from provided context.
  - Expected: Somewhat, but not extremely religious
- Q64 / 3 (multi-hop): Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi?
  - Generated: Insufficient information to determine; no data on musical preferences in provided context.
  - Expected: Yes; it's classical music
- Q69 / 3 (multi-hop): What personality traits might Melanie say Caroline has?
  - Generated: Caring, empathetic, and understanding.
  - Expected: Thoughtful, authentic, driven
- Q77 / 3 (multi-hop): Would Melanie go on another roadtrip soon?
  - Generated: No information about roadtrips is available in the context.
  - Expected: Likely no; since this one went badly

### memu-text

- Q59 / 3 (multi-hop): Would Caroline be considered religious?
  - Generated: No, the evidence is insufficient to consider Caroline religious.
  - Expected: Somewhat, but not extremely religious
