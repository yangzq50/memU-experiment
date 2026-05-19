# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-19T07:51:11+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | all | 199 | 45 | 154 | 52/154 | 33.77% | 46.3m | groots-ts-deepseek-v4-flash-s0-all-observed.json |
| memu-text | deepseek-v4-flash | deepseek-v4-flash | [0] | all | 199 | 45 | 154 | 117/154 | 75.97% | 126.0m | memu-text-deepseek-v4-flash-s0-all.json |

## Error Overlap

| Metric | Value |
| --- | --- |
| Shared evaluated questions | 154 |
| Wrong only in groots-ts | 71 |
| Wrong only in memu-text | 6 |
| Wrong in both | 31 |

## Per-Backend Wrong Examples

### groots-ts

- Q3 / 1 (single-hop): What did Caroline research?
  - Generated: The context does not specify what Caroline researched.
  - Expected: Adoption agencies
- Q4 / 1 (single-hop): What is Caroline's identity?
  - Generated: Caroline is a transgender advocate and member of the LGBTQ community.
  - Expected: Transgender woman
- Q5 / 2 (temporal): When did Melanie run a charity race?
  - Generated: 2023年5月20日。
  - Expected: The sunday before 25 May 2023
- Q9 / 2 (temporal): When did Caroline meet up with her friends, family, and mentors?
  - Generated: Caroline met with friends and family at a picnic last week.
  - Expected: The week before 9 June 2023
- Q10 / 2 (temporal): How long has Caroline had her current group of friends for?
  - Generated: 信息不足，无法确定Caroline拥有当前朋友群体的具体时长。
  - Expected: 4 years
- Q11 / 1 (single-hop): Where did Caroline move from 4 years ago?
  - Generated: Caroline moved from her home country, but the specific country is not mentioned in the context.
  - Expected: Sweden
- Q13 / 1 (single-hop): What career path has Caroline decided to persue?
  - Generated: Caroline decided to pursue a career in mental health counseling.
  - Expected: counseling or mental health for Transgender people
- Q15 / 1 (single-hop): What activities does Melanie partake in?
  - Generated: Running, reading, playing violin, camping, pottery, and meeting Caroline.
  - Expected: pottery, camping, painting, swimming

### memu-text

- Q5 / 2 (temporal): When did Melanie run a charity race?
  - Generated: Around 20 May, 2023.
  - Expected: The sunday before 25 May 2023
- Q7 / 1 (single-hop): What is Caroline's relationship status?
  - Generated: Caroline is single, as she plans to adopt as a single parent.
  - Expected: Single
- Q11 / 1 (single-hop): Where did Caroline move from 4 years ago?
  - Generated: Caroline moved from her home country.
  - Expected: Sweden
- Q13 / 1 (single-hop): What career path has Caroline decided to persue?
  - Generated: Caroline is exploring counseling and mental health careers but has not yet decided.
  - Expected: counseling or mental health for Transgender people
- Q15 / 1 (single-hop): What activities does Melanie partake in?
  - Generated: Hiking, camping, running, painting, pottery, reading, beach trips, park visits, concerts, road trips, and Pride festivals.
  - Expected: pottery, camping, painting, swimming
- Q19 / 1 (single-hop): What do Melanie's kids like?
  - Generated: Melanie's kids like camping, hiking, painting, pottery, swimming, and exploring nature.
  - Expected: dinosaurs, nature
- Q23 / 1 (single-hop): What books has Melanie read?
  - Generated: Melanie读过《Becoming Nicole》和一本封面有金币的书。
  - Expected: "Nothing is Impossible", "Charlotte's Web"
- Q30 / 3 (multi-hop): Would Melanie be considered a member of the LGBTQ community?
  - Generated: Insufficient information to determine if Melanie is a member of the LGBTQ community.
  - Expected: Likely no, she does not refer to herself as part of it

## Groots Memory Observability

| Backend | Spans | Total Span Time | Errors | JSON |
| --- | --- | --- | --- | --- |
| groots-ts | 569 | 64.4m | 0 | groots-ts-deepseek-v4-flash-s0-all-observed.json |
