# Benchmark Report: groots-ts / deepseek-v4-flash / sample=[0] / category=None

- Generated at: 2026-05-19T07:51:11+00:00
- Source JSON: `reports/results/groots-ts-deepseek-v4-flash-s0-all-observed.json`
- Command: `locomo_test.py --memory-backend groots-ts --memory-dir /Users/zhiqiangyang/GitHub/groots-mem/groots/.tmp/runs/groots_full_observed_flash_s0_all_v1 --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --max-workers 1 --force-resum --analyze-on none`
- Backend: `groots-ts`
- Chat model: `deepseek-v4-flash`
- Eval model: `deepseek-v4-flash`
- Data file: `data/locomo10.json`
- Sample: `[0]`
- Category: `all`

## Summary

| Metric | Value |
| --- | --- |
| Successful samples | 1 |
| Sessions processed | 19 |
| Sessions skipped | 0 |
| Questions available before filter | 199 |
| Questions skipped by filter | 45 |
| Questions evaluated | 154 |
| Correct answers | 52/154 |
| Overall accuracy | 33.77% |
| Total time | 46.3m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 6 | 32 | 18.75% |
| 2 (temporal) | 11 | 37 | 29.73% |
| 3 (multi-hop) | 9 | 13 | 69.23% |
| 4 (open-domain) | 24 | 70 | 34.29% |
| 5 (adversarial) | 2 | 2 | 100.00% |

## Wrong Examples

### Q3: What did Caroline research?

- Category: `1 (single-hop)`
- Generated: The context does not specify what Caroline researched.
- Expected: Adoption agencies
- Evaluation: Evaluation result: WRONG

### Q4: What is Caroline's identity?

- Category: `1 (single-hop)`
- Generated: Caroline is a transgender advocate and member of the LGBTQ community.
- Expected: Transgender woman
- Evaluation: The generated answer describes Caroline as a "transgender advocate" rather than identifying her as a "transgender woman", which does not match the gold standard answer for her identity.

### Q5: When did Melanie run a charity race?

- Category: `2 (temporal)`
- Generated: 2023年5月20日。
- Expected: The sunday before 25 May 2023
- Evaluation: Evaluation result: WRONG

### Q9: When did Caroline meet up with her friends, family, and mentors?

- Category: `2 (temporal)`
- Generated: Caroline met with friends and family at a picnic last week.
- Expected: The week before 9 June 2023
- Evaluation: The generated answer refers to "last week," which is a relative time period and does not match the specific week referenced in the gold answer ("the week before 9 June 2023").

### Q10: How long has Caroline had her current group of friends for?

- Category: `2 (temporal)`
- Generated: 信息不足，无法确定Caroline拥有当前朋友群体的具体时长。
- Expected: 4 years
- Evaluation: Evaluation result: WRONG


## Groots Memory Observability

| Span | Calls | Total | Average | p50 | p95 | Max | Errors |
| --- | --- | --- | --- | --- | --- | --- | --- |
| memory.index_source | 19 | 19.2m | 60.7s | 55.7s | 102.4s | 102.4s | 0 |
| memory.index_source.contextualize_chunk | 64 | 3.1m | 2.9s | 2.7s | 4.3s | 5.6s | 0 |
| memory.index_source.extract_chunk | 64 | 13.0m | 12.2s | 11.2s | 19.9s | 28.2s | 0 |
| memory.retrieve.query_plan | 154 | 7.8m | 3.0s | 2.8s | 5.0s | 7.9s | 0 |
| memory.retrieve.search_documents | 154 | 0.3s | 0.0s | 0.0s | 0.0s | 0.0s | 0 |
| memory.summary.build_category | 114 | 21.3m | 11.2s | 6.8s | 33.5s | 73.9s | 0 |

## Groots Memory Per-Question Retrieve Latency

| QA | Correct | Retrieve | Query plan | Search | Question |
| --- | --- | --- | --- | --- | --- |
| 0 | yes | 2.4s | 2.4s | 0.0s | When did Caroline go to the LGBTQ support group? |
| 1 | yes | 2.3s | 2.3s | 0.0s | When did Melanie paint a sunrise? |
| 2 | yes | 3.1s | 3.1s | 0.0s | What fields would Caroline be likely to pursue in her educaton? |
| 3 | no | 6.0s | 6.0s | 0.0s | What did Caroline research? |
| 4 | no | 2.9s | 2.9s | 0.0s | What is Caroline's identity? |
| 5 | no | 2.6s | 2.6s | 0.0s | When did Melanie run a charity race? |
| 6 | yes | 4.2s | 4.2s | 0.0s | When is Melanie planning on going camping? |
| 7 | yes | 2.5s | 2.5s | 0.0s | What is Caroline's relationship status? |
| 8 | yes | 2.2s | 2.2s | 0.0s | When did Caroline give a speech at a school? |
| 9 | no | 1.6s | 1.6s | 0.0s | When did Caroline meet up with her friends, family, and mentors? |
| 10 | no | 4.2s | 4.2s | 0.0s | How long has Caroline had her current group of friends for? |
| 11 | no | 2.8s | 2.8s | 0.0s | Where did Caroline move from 4 years ago? |
| 12 | yes | 2.6s | 2.6s | 0.0s | How long ago was Caroline's 18th birthday? |
| 13 | no | 3.2s | 3.2s | 0.0s | What career path has Caroline decided to persue? |
| 14 | yes | 2.3s | 2.3s | 0.0s | Would Caroline still want to pursue counseling as a career if she hadn't received support growin |
| 15 | no | 2.1s | 2.1s | 0.0s | What activities does Melanie partake in? |
| 16 | yes | 2.3s | 2.3s | 0.0s | When did Melanie sign up for a pottery class? |
| 17 | yes | 2.8s | 2.8s | 0.0s | When is Caroline going to the transgender conference? |
| 18 | yes | 2.4s | 2.4s | 0.0s | Where has Melanie camped? |
| 19 | yes | 2.4s | 2.4s | 0.0s | What do Melanie's kids like? |
| 20 | yes | 2.7s | 2.7s | 0.0s | When did Melanie go to the museum? |
| 21 | no | 2.9s | 2.9s | 0.0s | When did Caroline have a picnic? |
| 22 | yes | 2.9s | 2.9s | 0.0s | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 23 | no | 2.2s | 2.2s | 0.0s | What books has Melanie read? |
| 24 | no | 2.6s | 2.6s | 0.0s | What does Melanie do to destress? |
| 25 | yes | 4.6s | 4.6s | 0.0s | When did Caroline go to the LGBTQ conference? |
| 26 | no | 3.5s | 3.5s | 0.0s | When did Melanie read the book "nothing is impossible"? |
| 27 | yes | 3.3s | 3.3s | 0.0s | Would Caroline pursue writing as a career option? |
| 28 | no | 3.6s | 3.6s | 0.0s | When did Caroline go to the adoption meeting? |
| 29 | no | 2.2s | 2.2s | 0.0s | When did Melanie go to the pottery workshop? |
| 30 | yes | 5.7s | 5.7s | 0.0s | Would Melanie be considered a member of the LGBTQ community? |
| 31 | yes | 2.9s | 2.9s | 0.0s | When did Melanie go camping in June? |
| 32 | yes | 2.7s | 2.7s | 0.0s | What LGBTQ+ events has Caroline participated in? |
| 33 | yes | 2.7s | 2.7s | 0.0s | When did Caroline go to a pride parade during the summer? |
| 34 | no | 2.6s | 2.6s | 0.0s | What events has Caroline participated in to help children? |
| 35 | no | 3.8s | 3.7s | 0.0s | When did Melanie go camping in July? |
| 36 | no | 3.7s | 3.7s | 0.0s | When did Caroline join a mentorship program? |
| 37 | no | 2.5s | 2.5s | 0.0s | What did Melanie paint recently? |
| 38 | no | 2.5s | 2.5s | 0.0s | What activities has Melanie done with her family? |
| 39 | no | 2.3s | 2.3s | 0.0s | In what ways is Caroline participating in the LGBTQ community? |
| 40 | no | 2.6s | 2.6s | 0.0s | How many times has Melanie gone to the beach in 2023? |
| 41 | no | 2.4s | 2.4s | 0.0s | When did Caroline join a new activist group? |
| 42 | yes | 3.0s | 2.9s | 0.0s | Would Melanie be more interested in going to a national park or a theme park? |
| 43 | no | 2.2s | 2.2s | 0.0s | What kind of art does Caroline make? |
| 44 | no | 3.2s | 3.2s | 0.0s | When is Melanie's daughter's birthday? |
| 45 | no | 4.7s | 4.7s | 0.0s | When did Caroline attend a pride parade in August? |
| 46 | yes | 3.1s | 3.1s | 0.0s | Would Melanie be considered an ally to the transgender community? |
| 47 | yes | 2.8s | 2.8s | 0.0s | Who supports Caroline when she has a negative experience? |
| 48 | no | 2.7s | 2.7s | 0.0s | What types of pottery have Melanie and her kids made? |
| 49 | no | 4.3s | 4.3s | 0.0s | When did Caroline and Melanie go to a pride fesetival together? |
| 50 | yes | 5.3s | 5.3s | 0.0s | What would Caroline's political leaning likely be? |
| 51 | no | 2.9s | 2.9s | 0.0s | What has Melanie painted? |
| 52 | no | 3.2s | 3.2s | 0.0s | What are Melanie's pets' names? |
| 53 | no | 4.8s | 4.8s | 0.0s | When did Caroline apply to adoption agencies? |
| 54 | no | 3.2s | 3.2s | 0.0s | When did Caroline draw a self-portrait? |
| 55 | no | 2.7s | 2.7s | 0.0s | What subject have Caroline and Melanie both painted? |
| 56 | no | 2.5s | 2.5s | 0.0s | What symbols are important to Caroline? |
| 57 | no | 4.9s | 4.9s | 0.0s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 3.8s | 3.8s | 0.0s | When did Melanie make a plate in pottery class? |
| 59 | no | 2.7s | 2.7s | 0.0s | Would Caroline be considered religious? |
| 60 | no | 3.1s | 3.1s | 0.0s | What instruments does Melanie play? |
| 61 | no | 2.3s | 2.3s | 0.0s | What musical artists/bands has Melanie seen? |
| 62 | no | 2.6s | 2.6s | 0.0s | When did Melanie go to the park? |
| 63 | no | 2.7s | 2.7s | 0.0s | When is Caroline's youth center putting on a talent show? |
| 64 | no | 7.9s | 7.9s | 0.0s | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 65 | no | 3.4s | 3.4s | 0.0s | What are some changes Caroline has faced during her transition journey? |
| 66 | no | 2.9s | 2.9s | 0.0s | What does Melanie do with her family on hikes? |
| 67 | no | 2.5s | 2.5s | 0.0s | When did Caroline go biking with friends? |
| 68 | no | 3.2s | 3.2s | 0.0s | How long has Melanie been practicing art? |
| 69 | no | 2.7s | 2.7s | 0.0s | What personality traits might Melanie say Caroline has? |
| 70 | no | 5.0s | 5.0s | 0.0s | What transgender-specific events has Caroline attended? |
| 71 | yes | 2.6s | 2.6s | 0.0s | What book did Melanie read from Caroline's suggestion? |
| 72 | no | 2.7s | 2.7s | 0.0s | When did Melanie's friend adopt a child? |
| 73 | no | 2.0s | 2.0s | 0.0s | When did Melanie get hurt? |
| 74 | no | 2.5s | 2.5s | 0.0s | When did Melanie's family go on a roadtrip? |
| 75 | no | 2.6s | 2.6s | 0.0s | How many children does Melanie have? |
| 76 | no | 2.9s | 2.9s | 0.0s | When did Melanie go on a hike after the roadtrip? |
| 77 | no | 3.6s | 3.6s | 0.0s | Would Melanie go on another roadtrip soon? |
| 78 | no | 2.8s | 2.8s | 0.0s | What items has Melanie bought? |
| 79 | no | 3.3s | 3.3s | 0.0s | When did Caroline pass the adoption interview? |
| 80 | no | 2.3s | 2.3s | 0.0s | When did Melanie buy the figurines? |
| 81 | yes | 5.8s | 5.8s | 0.0s | Would Caroline want to move back to her home country soon? |
| 82 | yes | 2.3s | 2.3s | 0.0s | What did the charity race raise awareness for? |
| 83 | yes | 2.9s | 2.9s | 0.0s | What did Melanie realize after the charity race? |
| 84 | yes | 2.2s | 2.2s | 0.0s | How does Melanie prioritize self-care? |
| 85 | no | 3.1s | 3.1s | 0.0s | What are Caroline's plans for the summer? |
| 86 | yes | 3.0s | 3.0s | 0.0s | What type of individuals does the adoption agency Caroline is considering support? |
| 87 | yes | 6.5s | 6.5s | 0.0s | Why did Caroline choose the adoption agency? |
| 88 | yes | 3.0s | 3.0s | 0.0s | What is Caroline excited about in the adoption process? |
| 89 | yes | 2.7s | 2.7s | 0.0s | What does Melanie think about Caroline's decision to adopt? |
| 90 | yes | 2.5s | 2.5s | 0.0s | How long have Mel and her husband been married? |
| 91 | yes | 2.9s | 2.9s | 0.0s | What does Caroline's necklace symbolize? |
| 92 | yes | 2.0s | 2.0s | 0.0s | What country is Caroline's grandma from? |
| 93 | yes | 2.5s | 2.5s | 0.0s | What was grandma's gift to Caroline? |
| 94 | no | 2.7s | 2.7s | 0.0s | What is Melanie's hand-painted bowl a reminder of? |
| 95 | yes | 2.6s | 2.6s | 0.0s | What did Melanie and her family do while camping? |
| 96 | yes | 3.2s | 3.2s | 0.0s | What kind of counseling and mental health services is Caroline interested in pursuing? |
| 97 | yes | 3.4s | 3.4s | 0.0s | What workshop did Caroline attend recently? |
| 98 | yes | 2.8s | 2.8s | 0.0s | What was discussed in the LGBTQ+ counseling workshop? |
| 99 | no | 2.9s | 2.9s | 0.0s | What motivated Caroline to pursue counseling? |
| 100 | yes | 3.1s | 3.1s | 0.0s | What kind of place does Caroline want to create for people? |
| 101 | yes | 3.0s | 3.0s | 0.0s | Did Melanie make the black and white bowl in the photo? |
| 102 | yes | 2.6s | 2.6s | 0.0s | What kind of books does Caroline have in her library? |
| 103 | yes | 3.3s | 3.3s | 0.0s | What was Melanie's favorite book from her childhood? |
| 104 | yes | 2.6s | 2.6s | 0.0s | What book did Caroline recommend to Melanie? |
| 105 | no | 2.6s | 2.6s | 0.0s | What did Caroline take away from the book "Becoming Nicole"? |
| 106 | yes | 2.6s | 2.6s | 0.0s | What are the new shoes that Melanie got used for? |
| 107 | yes | 3.5s | 3.5s | 0.0s | What is Melanie's reason for getting into running? |
| 108 | yes | 2.8s | 2.8s | 0.0s | What does Melanie say running has been great for? |
| 109 | no | 3.3s | 3.3s | 0.0s | What did Mel and her kids make during the pottery workshop? |
| 110 | no | 2.5s | 2.5s | 0.0s | What kind of pot did Mel and her kids make with clay? |
| 111 | no | 3.1s | 3.1s | 0.0s | What creative project do Mel and her kids do together besides pottery? |
| 112 | no | 1.9s | 1.9s | 0.0s | What did Mel and her kids paint in their latest project in July 2023? |
| 113 | no | 3.2s | 3.2s | 0.0s | What did Caroline see at the council meeting for adoption? |
| 114 | no | 4.2s | 4.2s | 0.0s | What do sunflowers represent according to Caroline? |
| 115 | no | 2.2s | 2.2s | 0.0s | Why are flowers important to Melanie? |
| 116 | no | 2.8s | 2.8s | 0.0s | What inspired Caroline's painting for the art show? |
| 117 | no | 3.2s | 3.2s | 0.0s | How often does Melanie go to the beach with her kids? |
| 118 | no | 2.7s | 2.7s | 0.0s | What did Melanie and her family see during their camping trip last year? |
| 119 | no | 2.7s | 2.7s | 0.0s | How did Melanie feel while watching the meteor shower? |
| 120 | no | 2.9s | 2.9s | 0.0s | Whose birthday did Melanie celebrate recently? |
| 121 | no | 3.4s | 3.4s | 0.0s | Who performed at the concert at Melanie's daughter's birthday? |
| 122 | no | 2.5s | 2.5s | 0.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 123 | no | 2.3s | 2.3s | 0.0s | What pet does Caroline have? |
| 124 | no | 2.4s | 2.4s | 0.0s | What pets does Melanie have? |
| 125 | no | 2.8s | 2.8s | 0.0s | Where did Oliver hide his bone once? |
| 126 | no | 5.2s | 5.2s | 0.0s | What activity did Caroline used to do with her dad? |
| 127 | no | 1.9s | 1.9s | 0.0s | What did Caroline make for a local church? |
| 128 | no | 3.6s | 3.6s | 0.0s | What did Caroline find in her neighborhood during her walk? |
| 129 | no | 2.8s | 2.8s | 0.0s | Which song motivates Caroline to be courageous? |
| 130 | no | 3.1s | 3.1s | 0.0s | Which  classical musicians does Melanie enjoy listening to? |
| 131 | no | 3.5s | 3.5s | 0.0s | Who is Melanie a fan of in terms of modern music? |
| 132 | no | 3.1s | 3.1s | 0.0s | How long has Melanie been creating art? |
| 133 | no | 2.5s | 2.5s | 0.0s | What precautionary sign did Melanie see at the café? |
| 134 | no | 2.8s | 2.8s | 0.0s | What advice does Caroline give for getting started with adoption? |
| 135 | no | 2.2s | 2.2s | 0.0s | What setback did Melanie face in October 2023? |
| 136 | no | 3.1s | 3.1s | 0.0s | What does Melanie do to keep herself busy during her pottery break? |
| 137 | no | 4.2s | 4.2s | 0.0s | What painting did Melanie show to Caroline on October 13, 2023? |
| 138 | no | 2.9s | 2.9s | 0.0s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 139 | no | 2.1s | 2.1s | 0.0s | What was the poetry reading that Caroline attended about? |
| 140 | no | 2.6s | 2.6s | 0.0s | What did the posters at the poetry reading say? |
| 141 | no | 4.1s | 4.1s | 0.0s | What does Caroline's drawing symbolize for her? |
| 142 | no | 2.4s | 2.4s | 0.0s | How do Melanie and Caroline describe their journey through life together? |
| 143 | no | 2.6s | 2.6s | 0.0s | What happened to Melanie's son on their road trip? |
| 144 | no | 2.5s | 2.5s | 0.0s | How did Melanie's son handle the accident? |
| 145 | no | 2.8s | 2.8s | 0.0s | How did Melanie feel about her family after the accident? |
| 146 | no | 2.3s | 2.3s | 0.0s | How did Melanie's children handle the accident? |
| 147 | no | 2.1s | 2.1s | 0.0s | How did Melanie feel after the accident? |
| 148 | no | 2.3s | 2.3s | 0.0s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
| 149 | no | 3.5s | 3.5s | 0.0s | What do Melanie's family give her? |
| 150 | yes | 3.3s | 3.3s | 0.0s | How did Melanie feel about her family supporting her? |
| 151 | no | 2.6s | 2.6s | 0.0s | What did Melanie do after the road trip to relax? |
| 167 | yes | 2.7s | 2.7s | 0.0s | Did Caroline make the black and white bowl in the photo? |
| 178 | yes | 3.0s | 3.0s | 0.0s | Is Oscar Melanie's pet? |

## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | yes | 6.9s | 5.3s | 1.6s | 2.4s | 2.9s | When did Caroline go to the LGBTQ support group? |
| 1 | yes | 8.7s | 4.8s | 3.9s | 2.4s | 2.4s | When did Melanie paint a sunrise? |
| 2 | yes | 7.6s | 5.6s | 1.9s | 3.2s | 2.5s | What fields would Caroline be likely to pursue in her educaton? |
| 3 | no | 11.7s | 9.9s | 1.7s | 6.1s | 3.9s | What did Caroline research? |
| 4 | no | 10.0s | 6.4s | 3.6s | 3.0s | 3.4s | What is Caroline's identity? |
| 5 | no | 7.3s | 5.6s | 1.7s | 2.7s | 2.9s | When did Melanie run a charity race? |
| 6 | yes | 13.9s | 12.7s | 1.2s | 4.3s | 8.4s | When is Melanie planning on going camping? |
| 7 | yes | 5.9s | 4.3s | 1.6s | 2.6s | 1.8s | What is Caroline's relationship status? |
| 8 | yes | 8.4s | 6.5s | 1.9s | 2.3s | 4.2s | When did Caroline give a speech at a school? |
| 9 | no | 12.6s | 9.2s | 3.4s | 1.7s | 7.6s | When did Caroline meet up with her friends, family, and mentors? |
| 10 | no | 12.7s | 11.0s | 1.7s | 4.2s | 6.7s | How long has Caroline had her current group of friends for? |
| 11 | no | 7.1s | 5.0s | 2.0s | 2.9s | 2.1s | Where did Caroline move from 4 years ago? |
| 12 | yes | 16.0s | 14.5s | 1.4s | 2.7s | 11.9s | How long ago was Caroline's 18th birthday? |
| 13 | no | 13.3s | 10.0s | 3.4s | 3.3s | 6.7s | What career path has Caroline decided to persue? |
| 14 | yes | 11.9s | 10.4s | 1.5s | 2.4s | 8.0s | Would Caroline still want to pursue counseling as a career if she hadn't receive |
| 15 | no | 8.7s | 6.5s | 2.1s | 2.2s | 4.3s | What activities does Melanie partake in? |
| 16 | yes | 5.7s | 4.7s | 1.0s | 2.4s | 2.3s | When did Melanie sign up for a pottery class? |
| 17 | yes | 6.1s | 4.7s | 1.4s | 2.9s | 1.8s | When is Caroline going to the transgender conference? |
| 18 | yes | 11.2s | 4.6s | 6.6s | 2.4s | 2.2s | Where has Melanie camped? |
| 19 | yes | 5.2s | 3.6s | 1.6s | 2.4s | 1.2s | What do Melanie's kids like? |
| 20 | yes | 6.3s | 4.7s | 1.5s | 2.8s | 2.0s | When did Melanie go to the museum? |
| 21 | no | 12.6s | 9.9s | 2.7s | 3.0s | 6.9s | When did Caroline have a picnic? |
| 22 | yes | 11.9s | 9.1s | 2.8s | 3.0s | 6.1s | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 23 | no | 10.5s | 6.5s | 4.1s | 2.3s | 4.2s | What books has Melanie read? |
| 24 | no | 15.6s | 8.3s | 7.3s | 2.6s | 5.6s | What does Melanie do to destress? |
| 25 | yes | 10.0s | 8.4s | 1.6s | 4.6s | 3.8s | When did Caroline go to the LGBTQ conference? |
| 26 | no | 11.3s | 8.9s | 2.5s | 3.6s | 5.3s | When did Melanie read the book "nothing is impossible"? |
| 27 | yes | 6.8s | 5.0s | 1.8s | 3.4s | 1.6s | Would Caroline pursue writing as a career option? |
| 28 | no | 13.6s | 12.0s | 1.6s | 3.6s | 8.4s | When did Caroline go to the adoption meeting? |
| 29 | no | 22.8s | 18.1s | 4.7s | 2.3s | 15.8s | When did Melanie go to the pottery workshop? |
| 30 | yes | 10.3s | 8.7s | 1.6s | 5.8s | 2.9s | Would Melanie be considered a member of the LGBTQ community? |
| 31 | yes | 10.7s | 6.1s | 4.5s | 3.0s | 3.1s | When did Melanie go camping in June? |
| 32 | yes | 16.3s | 8.8s | 7.5s | 2.8s | 6.0s | What LGBTQ+ events has Caroline participated in? |
| 33 | yes | 12.1s | 10.4s | 1.6s | 2.8s | 7.7s | When did Caroline go to a pride parade during the summer? |
| 34 | no | 21.4s | 19.5s | 1.9s | 2.7s | 16.8s | What events has Caroline participated in to help children? |
| 35 | no | 8.9s | 7.2s | 1.7s | 3.8s | 3.4s | When did Melanie go camping in July? |
| 36 | no | 8.6s | 6.9s | 1.7s | 3.8s | 3.0s | When did Caroline join a mentorship program? |
| 37 | no | 11.1s | 9.4s | 1.7s | 2.6s | 6.8s | What did Melanie paint recently? |
| 38 | no | 13.5s | 9.4s | 4.1s | 2.6s | 6.8s | What activities has Melanie done with her family? |
| 39 | no | 16.5s | 14.6s | 2.0s | 2.3s | 12.2s | In what ways is Caroline participating in the LGBTQ community? |
| 40 | no | 27.4s | 25.1s | 2.3s | 2.7s | 22.4s | How many times has Melanie gone to the beach in 2023? |
| 41 | no | 14.2s | 10.4s | 3.8s | 2.5s | 8.0s | When did Caroline join a new activist group? |
| 42 | yes | 8.0s | 6.3s | 1.7s | 3.0s | 3.3s | Would Melanie be more interested in going to a national park or a theme park? |
| 43 | no | 10.1s | 7.8s | 2.4s | 2.3s | 5.5s | What kind of art does Caroline make? |
| 44 | no | 9.4s | 7.8s | 1.6s | 3.3s | 4.6s | When is Melanie's daughter's birthday? |
| 45 | no | 11.6s | 9.4s | 2.2s | 4.7s | 4.6s | When did Caroline attend a pride parade in August? |
| 46 | yes | 7.1s | 4.8s | 2.3s | 3.2s | 1.6s | Would Melanie be considered an ally to the transgender community? |
| 47 | yes | 11.6s | 7.1s | 4.5s | 2.9s | 4.2s | Who supports Caroline when she has a negative experience? |
| 48 | no | 11.2s | 5.5s | 5.7s | 2.8s | 2.7s | What types of pottery have Melanie and her kids made? |
| 49 | no | 10.1s | 8.1s | 2.0s | 4.4s | 3.7s | When did Caroline and Melanie go to a pride fesetival together? |
| 50 | yes | 13.0s | 11.5s | 1.5s | 5.4s | 6.1s | What would Caroline's political leaning likely be? |
| 51 | no | 12.0s | 4.6s | 7.3s | 3.0s | 1.6s | What has Melanie painted? |
| 52 | no | 9.4s | 5.5s | 4.0s | 3.2s | 2.2s | What are Melanie's pets' names? |
| 53 | no | 11.2s | 8.8s | 2.4s | 4.8s | 4.0s | When did Caroline apply to adoption agencies? |
| 54 | no | 10.2s | 7.7s | 2.5s | 3.3s | 4.4s | When did Caroline draw a self-portrait? |
| 55 | no | 9.1s | 6.7s | 2.4s | 2.8s | 3.9s | What subject have Caroline and Melanie both painted? |
| 56 | no | 21.3s | 19.7s | 1.6s | 2.5s | 17.2s | What symbols are important to Caroline? |
| 57 | no | 10.3s | 8.7s | 1.6s | 5.0s | 3.7s | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 8.9s | 7.2s | 1.8s | 3.8s | 3.4s | When did Melanie make a plate in pottery class? |
| 59 | no | 11.0s | 8.3s | 2.8s | 2.8s | 5.5s | Would Caroline be considered religious? |
| 60 | no | 8.9s | 6.0s | 2.9s | 3.2s | 2.8s | What instruments does Melanie play? |
| 61 | no | 9.8s | 7.9s | 2.0s | 2.4s | 5.5s | What musical artists/bands has Melanie seen? |
| 62 | no | 8.1s | 6.0s | 2.1s | 2.7s | 3.3s | When did Melanie go to the park? |
| 63 | no | 9.7s | 6.6s | 3.2s | 2.8s | 3.8s | When is Caroline's youth center putting on a talent show? |
| 64 | no | 14.6s | 11.8s | 2.9s | 8.0s | 3.8s | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 65 | no | 21.6s | 17.5s | 4.0s | 3.5s | 14.0s | What are some changes Caroline has faced during her transition journey? |
| 66 | no | 11.6s | 9.0s | 2.6s | 3.0s | 6.0s | What does Melanie do with her family on hikes? |
| 67 | no | 9.8s | 7.6s | 2.1s | 2.6s | 5.1s | When did Caroline go biking with friends? |
| 68 | no | 8.9s | 6.9s | 2.0s | 3.3s | 3.6s | How long has Melanie been practicing art? |
| 69 | no | 27.6s | 22.9s | 4.7s | 2.8s | 20.1s | What personality traits might Melanie say Caroline has? |
| 70 | no | 17.2s | 14.6s | 2.7s | 5.2s | 9.4s | What transgender-specific events has Caroline attended? |
| 71 | yes | 7.8s | 6.3s | 1.4s | 2.6s | 3.7s | What book did Melanie read from Caroline's suggestion? |
| 72 | no | 8.3s | 5.9s | 2.3s | 2.8s | 3.1s | When did Melanie's friend adopt a child? |
| 73 | no | 6.7s | 4.6s | 2.1s | 2.1s | 2.5s | When did Melanie get hurt? |
| 74 | no | 14.3s | 12.5s | 1.8s | 2.6s | 9.9s | When did Melanie's family go on a roadtrip? |
| 75 | no | 11.3s | 8.8s | 2.5s | 2.7s | 6.1s | How many children does Melanie have? |
| 76 | no | 7.4s | 5.7s | 1.7s | 3.0s | 2.7s | When did Melanie go on a hike after the roadtrip? |
| 77 | no | 10.2s | 7.8s | 2.5s | 3.7s | 4.1s | Would Melanie go on another roadtrip soon? |
| 78 | no | 9.9s | 5.1s | 4.8s | 2.9s | 2.2s | What items has Melanie bought? |
| 79 | no | 8.3s | 6.5s | 1.8s | 3.3s | 3.2s | When did Caroline pass the adoption interview? |
| 80 | no | 6.3s | 4.5s | 1.8s | 2.4s | 2.2s | When did Melanie buy the figurines? |
| 81 | yes | 14.6s | 11.7s | 3.0s | 5.9s | 5.8s | Would Caroline want to move back to her home country soon? |
| 82 | yes | 6.1s | 4.9s | 1.2s | 2.4s | 2.5s | What did the charity race raise awareness for? |
| 83 | yes | 8.1s | 6.8s | 1.3s | 2.9s | 3.8s | What did Melanie realize after the charity race? |
| 84 | yes | 12.9s | 10.1s | 2.8s | 2.3s | 7.8s | How does Melanie prioritize self-care? |
| 85 | no | 8.7s | 7.0s | 1.7s | 3.2s | 3.8s | What are Caroline's plans for the summer? |
| 86 | yes | 6.7s | 5.2s | 1.4s | 3.1s | 2.1s | What type of individuals does the adoption agency Caroline is considering suppor |
| 87 | yes | 13.7s | 12.0s | 1.7s | 6.6s | 5.5s | Why did Caroline choose the adoption agency? |
| 88 | yes | 13.4s | 12.0s | 1.4s | 3.1s | 8.9s | What is Caroline excited about in the adoption process? |
| 89 | yes | 13.1s | 11.6s | 1.5s | 2.8s | 8.8s | What does Melanie think about Caroline's decision to adopt? |
| 90 | yes | 6.5s | 5.2s | 1.3s | 2.6s | 2.6s | How long have Mel and her husband been married? |
| 91 | yes | 6.9s | 5.5s | 1.3s | 3.0s | 2.5s | What does Caroline's necklace symbolize? |
| 92 | yes | 6.5s | 5.1s | 1.3s | 2.1s | 3.0s | What country is Caroline's grandma from? |
| 93 | yes | 6.2s | 4.9s | 1.3s | 2.6s | 2.3s | What was grandma's gift to Caroline? |
| 94 | no | 36.9s | 34.2s | 2.7s | 2.8s | 31.4s | What is Melanie's hand-painted bowl a reminder of? |
| 95 | yes | 7.9s | 6.2s | 1.6s | 2.7s | 3.6s | What did Melanie and her family do while camping? |
| 96 | yes | 11.1s | 9.1s | 1.9s | 3.3s | 5.8s | What kind of counseling and mental health services is Caroline interested in pur |
| 97 | yes | 8.3s | 6.6s | 1.7s | 3.4s | 3.1s | What workshop did Caroline attend recently? |
| 98 | yes | 7.3s | 5.6s | 1.6s | 2.9s | 2.7s | What was discussed in the LGBTQ+ counseling workshop? |
| 99 | no | 17.9s | 10.9s | 7.0s | 3.0s | 7.9s | What motivated Caroline to pursue counseling? |
| 100 | yes | 8.8s | 6.8s | 1.9s | 3.2s | 3.7s | What kind of place does Caroline want to create for people? |
| 101 | yes | 8.3s | 6.8s | 1.4s | 3.1s | 3.7s | Did Melanie make the black and white bowl in the photo? |
| 102 | yes | 5.9s | 4.1s | 1.8s | 2.6s | 1.4s | What kind of books does Caroline have in her library? |
| 103 | yes | 7.4s | 5.8s | 1.5s | 3.4s | 2.4s | What was Melanie's favorite book from her childhood? |
| 104 | yes | 10.2s | 8.9s | 1.3s | 2.7s | 6.2s | What book did Caroline recommend to Melanie? |
| 105 | no | 9.5s | 7.9s | 1.5s | 2.7s | 5.2s | What did Caroline take away from the book "Becoming Nicole"? |
| 106 | yes | 6.1s | 4.8s | 1.3s | 2.7s | 2.1s | What are the new shoes that Melanie got used for? |
| 107 | yes | 8.7s | 7.1s | 1.6s | 3.6s | 3.5s | What is Melanie's reason for getting into running? |
| 108 | yes | 7.0s | 5.3s | 1.7s | 2.9s | 2.4s | What does Melanie say running has been great for? |
| 109 | no | 8.8s | 7.4s | 1.5s | 3.4s | 4.0s | What did Mel and her kids make during the pottery workshop? |
| 110 | no | 8.8s | 6.9s | 1.8s | 2.6s | 4.4s | What kind of pot did Mel and her kids make with clay? |
| 111 | no | 10.7s | 8.8s | 1.9s | 3.2s | 5.6s | What creative project do Mel and her kids do together besides pottery? |
| 112 | no | 8.1s | 5.7s | 2.4s | 2.0s | 3.7s | What did Mel and her kids paint in their latest project in July 2023? |
| 113 | no | 8.8s | 6.9s | 1.9s | 3.3s | 3.6s | What did Caroline see at the council meeting for adoption? |
| 114 | no | 8.9s | 7.2s | 1.7s | 4.3s | 2.9s | What do sunflowers represent according to Caroline? |
| 115 | no | 11.4s | 9.6s | 1.8s | 2.2s | 7.4s | Why are flowers important to Melanie? |
| 116 | no | 18.8s | 17.0s | 1.8s | 2.8s | 14.1s | What inspired Caroline's painting for the art show? |
| 117 | no | 10.8s | 9.1s | 1.6s | 3.3s | 5.8s | How often does Melanie go to the beach with her kids? |
| 118 | no | 9.4s | 7.3s | 2.1s | 2.8s | 4.5s | What did Melanie and her family see during their camping trip last year? |
| 119 | no | 7.3s | 5.5s | 1.8s | 2.8s | 2.7s | How did Melanie feel while watching the meteor shower? |
| 120 | no | 12.1s | 10.4s | 1.6s | 3.0s | 7.5s | Whose birthday did Melanie celebrate recently? |
| 121 | no | 11.4s | 8.6s | 2.8s | 3.5s | 5.1s | Who performed at the concert at Melanie's daughter's birthday? |
| 122 | no | 9.5s | 7.6s | 1.8s | 2.6s | 5.0s | Why did Melanie choose to use colors and patterns in her pottery project? |
| 123 | no | 7.4s | 5.6s | 1.7s | 2.4s | 3.2s | What pet does Caroline have? |
| 124 | no | 7.1s | 4.1s | 3.0s | 2.5s | 1.6s | What pets does Melanie have? |
| 125 | no | 8.1s | 6.1s | 2.0s | 2.9s | 3.2s | Where did Oliver hide his bone once? |
| 126 | no | 10.4s | 8.2s | 2.2s | 5.3s | 2.9s | What activity did Caroline used to do with her dad? |
| 127 | no | 7.3s | 5.4s | 1.9s | 2.0s | 3.4s | What did Caroline make for a local church? |
| 128 | no | 9.5s | 7.7s | 1.8s | 3.6s | 4.1s | What did Caroline find in her neighborhood during her walk? |
| 129 | no | 7.2s | 5.6s | 1.5s | 2.9s | 2.7s | Which song motivates Caroline to be courageous? |
| 130 | no | 8.4s | 6.1s | 2.3s | 3.2s | 2.9s | Which  classical musicians does Melanie enjoy listening to? |
| 131 | no | 7.8s | 6.3s | 1.5s | 3.6s | 2.8s | Who is Melanie a fan of in terms of modern music? |
| 132 | no | 7.9s | 6.4s | 1.5s | 3.2s | 3.3s | How long has Melanie been creating art? |
| 133 | no | 7.4s | 5.4s | 2.0s | 2.6s | 2.8s | What precautionary sign did Melanie see at the café? |
| 134 | no | 9.2s | 7.2s | 2.0s | 2.9s | 4.3s | What advice does Caroline give for getting started with adoption? |
| 135 | no | 6.7s | 5.0s | 1.7s | 2.2s | 2.7s | What setback did Melanie face in October 2023? |
| 136 | no | 14.0s | 11.9s | 2.1s | 3.2s | 8.7s | What does Melanie do to keep herself busy during her pottery break? |
| 137 | no | 8.9s | 7.5s | 1.4s | 4.3s | 3.2s | What painting did Melanie show to Caroline on October 13, 2023? |
| 138 | no | 7.9s | 5.8s | 2.1s | 3.0s | 2.8s | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 139 | no | 7.1s | 5.2s | 1.9s | 2.2s | 3.0s | What was the poetry reading that Caroline attended about? |
| 140 | no | 8.2s | 5.3s | 2.9s | 2.6s | 2.7s | What did the posters at the poetry reading say? |
| 141 | no | 9.8s | 7.9s | 1.9s | 4.1s | 3.8s | What does Caroline's drawing symbolize for her? |
| 142 | no | 21.2s | 19.5s | 1.7s | 2.5s | 17.0s | How do Melanie and Caroline describe their journey through life together? |
| 143 | no | 8.8s | 6.7s | 2.1s | 2.7s | 4.1s | What happened to Melanie's son on their road trip? |
| 144 | no | 9.5s | 7.3s | 2.3s | 2.6s | 4.7s | How did Melanie's son handle the accident? |
| 145 | no | 7.7s | 5.7s | 2.0s | 2.9s | 2.8s | How did Melanie feel about her family after the accident? |
| 146 | no | 7.4s | 5.7s | 1.6s | 2.3s | 3.4s | How did Melanie's children handle the accident? |
| 147 | no | 11.3s | 4.6s | 6.7s | 2.2s | 2.4s | How did Melanie feel after the accident? |
| 148 | no | 6.9s | 5.0s | 1.9s | 2.4s | 2.6s | What was Melanie's reaction to her children enjoying the Grand Canyon? |
| 149 | no | 9.8s | 5.7s | 4.1s | 3.6s | 2.2s | What do Melanie's family give her? |
| 150 | yes | 8.1s | 6.6s | 1.5s | 3.4s | 3.2s | How did Melanie feel about her family supporting her? |
| 151 | no | 14.6s | 12.7s | 1.9s | 2.7s | 10.0s | What did Melanie do after the road trip to relax? |
| 167 | yes | 7.0s | 5.2s | 1.7s | 2.8s | 2.5s | Did Caroline make the black and white bowl in the photo? |
| 178 | yes | 7.7s | 6.3s | 1.4s | 3.1s | 3.3s | Is Oscar Melanie's pet? |
