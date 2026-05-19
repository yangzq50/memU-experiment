# Groots Memory vs memU Benchmark Report

- Generated at: 2026-05-18T13:19:57+00:00
- Evaluation uses the JSON result files listed in the table below.
- `Available` is the number of questions in the selected sample before category filtering.
- `Evaluated` is the number of questions actually answered and scored in this run.

## Headline

| Backend | Chat Model | Eval Model | Sample | Category | Available | Skipped | Evaluated | Correct | Accuracy | Time | JSON |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| groots-ts | deepseek-v4-flash | deepseek-v4-flash | [0] | all | 199 | 45 | 154 | 52/154 | 33.77% | 46.3m | groots-ts-deepseek-v4-flash-s0-all-observed.json |

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

## Groots Memory Observability

| Backend | Spans | Total Span Time | Errors | JSON |
| --- | --- | --- | --- | --- |
| groots-ts | 569 | 64.4m | 0 | groots-ts-deepseek-v4-flash-s0-all-observed.json |
