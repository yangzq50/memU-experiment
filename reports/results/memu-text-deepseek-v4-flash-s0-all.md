# Benchmark Report: memu-text / deepseek-v4-flash / sample=[0] / category=None

- Generated at: 2026-05-19T07:51:11+00:00
- Source JSON: `reports/results/memu-text-deepseek-v4-flash-s0-all.json`
- Command: `locomo_test.py --memory-backend memu --memory-dir .tmp/runs/memu_full_flash_s0_all_noemb --chat-deployment deepseek-v4-flash --eval-deployment deepseek-v4-flash --sample-use [0] --max-workers 1 --force-resum --analyze-on none --disable-embeddings`
- Backend: `memu-text`
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
| Correct answers | 117/154 |
| Overall accuracy | 75.97% |
| Total time | 126.0m |

## Category Accuracy

| Category | Correct | Total | Accuracy |
| --- | --- | --- | --- |
| 1 (single-hop) | 16 | 32 | 50.00% |
| 2 (temporal) | 32 | 37 | 86.49% |
| 3 (multi-hop) | 10 | 13 | 76.92% |
| 4 (open-domain) | 57 | 70 | 81.43% |
| 5 (adversarial) | 2 | 2 | 100.00% |

## Wrong Examples

### Q5: When did Melanie run a charity race?

- Category: `2 (temporal)`
- Generated: Around 20 May, 2023.
- Expected: The sunday before 25 May 2023
- Evaluation: 

### Q7: What is Caroline's relationship status?

- Category: `1 (single-hop)`
- Generated: Caroline is single, as she plans to adopt as a single parent.
- Expected: Single
- Evaluation: 

### Q11: Where did Caroline move from 4 years ago?

- Category: `1 (single-hop)`
- Generated: Caroline moved from her home country.
- Expected: Sweden
- Evaluation: Evaluation result: WRONG

### Q13: What career path has Caroline decided to persue?

- Category: `1 (single-hop)`
- Generated: Caroline is exploring counseling and mental health careers but has not yet decided.
- Expected: counseling or mental health for Transgender people
- Evaluation: Evaluation result: WRONG

### Q15: What activities does Melanie partake in?

- Category: `1 (single-hop)`
- Generated: Hiking, camping, running, painting, pottery, reading, beach trips, park visits, concerts, road trips, and Pride festivals.
- Expected: pottery, camping, painting, swimming
- Evaluation: The generated answer misses "swimming" which is listed in the gold answer, so it is incomplete.


## Benchmark QA Latency

| QA | Correct | Total | Answer | Eval | Groots retrieve | Answer generation | Question |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | yes | 7.8s | 6.5s | 1.3s | n/a | n/a | When did Caroline go to the LGBTQ support group? |
| 1 | yes | 33.9s | 32.2s | 1.7s | n/a | n/a | When did Melanie paint a sunrise? |
| 2 | yes | 19.5s | 17.5s | 1.9s | n/a | n/a | What fields would Caroline be likely to pursue in her educaton? |
| 3 | yes | 12.4s | 9.7s | 2.7s | n/a | n/a | What did Caroline research? |
| 4 | yes | 16.3s | 14.3s | 2.0s | n/a | n/a | What is Caroline's identity? |
| 5 | no | 12.7s | 5.7s | 7.0s | n/a | n/a | When did Melanie run a charity race? |
| 6 | yes | 32.8s | 31.6s | 1.2s | n/a | n/a | When is Melanie planning on going camping? |
| 7 | no | 16.3s | 9.8s | 6.6s | n/a | n/a | What is Caroline's relationship status? |
| 8 | yes | 34.4s | 32.5s | 1.9s | n/a | n/a | When did Caroline give a speech at a school? |
| 9 | yes | 42.3s | 40.4s | 1.8s | n/a | n/a | When did Caroline meet up with her friends, family, and mentors? |
| 10 | yes | 23.4s | 22.0s | 1.4s | n/a | n/a | How long has Caroline had her current group of friends for? |
| 11 | no | 30.7s | 28.9s | 1.8s | n/a | n/a | Where did Caroline move from 4 years ago? |
| 12 | yes | 52.4s | 50.9s | 1.6s | n/a | n/a | How long ago was Caroline's 18th birthday? |
| 13 | no | 16.3s | 11.9s | 4.4s | n/a | n/a | What career path has Caroline decided to persue? |
| 14 | yes | 45.0s | 43.6s | 1.3s | n/a | n/a | Would Caroline still want to pursue counseling as a career if she hadn't receive |
| 15 | no | 22.2s | 17.3s | 4.9s | n/a | n/a | What activities does Melanie partake in? |
| 16 | yes | 8.0s | 6.3s | 1.7s | n/a | n/a | When did Melanie sign up for a pottery class? |
| 17 | yes | 40.6s | 37.9s | 2.6s | n/a | n/a | When is Caroline going to the transgender conference? |
| 18 | yes | 42.5s | 40.3s | 2.1s | n/a | n/a | Where has Melanie camped? |
| 19 | no | 29.7s | 26.2s | 3.6s | n/a | n/a | What do Melanie's kids like? |
| 20 | yes | 6.0s | 4.7s | 1.3s | n/a | n/a | When did Melanie go to the museum? |
| 21 | yes | 40.0s | 38.5s | 1.5s | n/a | n/a | When did Caroline have a picnic? |
| 22 | yes | 35.6s | 34.2s | 1.4s | n/a | n/a | Would Caroline likely have Dr. Seuss books on her bookshelf? |
| 23 | no | 50.4s | 48.4s | 1.9s | n/a | n/a | What books has Melanie read? |
| 24 | yes | 14.4s | 11.9s | 2.5s | n/a | n/a | What does Melanie do to destress? |
| 25 | yes | 11.0s | 9.3s | 1.6s | n/a | n/a | When did Caroline go to the LGBTQ conference? |
| 26 | yes | 36.2s | 35.0s | 1.2s | n/a | n/a | When did Melanie read the book "nothing is impossible"? |
| 27 | yes | 30.2s | 28.7s | 1.5s | n/a | n/a | Would Caroline pursue writing as a career option? |
| 28 | yes | 28.2s | 26.1s | 2.1s | n/a | n/a | When did Caroline go to the adoption meeting? |
| 29 | yes | 7.7s | 5.8s | 1.9s | n/a | n/a | When did Melanie go to the pottery workshop? |
| 30 | no | 29.7s | 27.6s | 2.1s | n/a | n/a | Would Melanie be considered a member of the LGBTQ community? |
| 31 | yes | 44.0s | 42.5s | 1.5s | n/a | n/a | When did Melanie go camping in June? |
| 32 | yes | 21.8s | 17.9s | 4.0s | n/a | n/a | What LGBTQ+ events has Caroline participated in? |
| 33 | no | 69.2s | 61.1s | 8.1s | n/a | n/a | When did Caroline go to a pride parade during the summer? |
| 34 | yes | 45.6s | 42.9s | 2.7s | n/a | n/a | What events has Caroline participated in to help children? |
| 35 | yes | 112.6s | 110.1s | 2.5s | n/a | n/a | When did Melanie go camping in July? |
| 36 | yes | 16.8s | 14.3s | 2.5s | n/a | n/a | When did Caroline join a mentorship program? |
| 37 | yes | 32.1s | 30.0s | 2.1s | n/a | n/a | What did Melanie paint recently? |
| 38 | no | 41.5s | 35.7s | 5.9s | n/a | n/a | What activities has Melanie done with her family? |
| 39 | yes | 32.0s | 29.0s | 3.1s | n/a | n/a | In what ways is Caroline participating in the LGBTQ community? |
| 40 | yes | 38.1s | 36.8s | 1.4s | n/a | n/a | How many times has Melanie gone to the beach in 2023? |
| 41 | yes | 6.7s | 5.1s | 1.6s | n/a | n/a | When did Caroline join a new activist group? |
| 42 | yes | 14.3s | 12.8s | 1.5s | n/a | n/a | Would Melanie be more interested in going to a national park or a theme park? |
| 43 | no | 17.4s | 15.6s | 1.7s | n/a | n/a | What kind of art does Caroline make? |
| 44 | yes | 19.4s | 16.6s | 2.8s | n/a | n/a | When is Melanie's daughter's birthday? |
| 45 | yes | 12.1s | 10.0s | 2.1s | n/a | n/a | When did Caroline attend a pride parade in August? |
| 46 | yes | 14.4s | 13.1s | 1.3s | n/a | n/a | Would Melanie be considered an ally to the transgender community? |
| 47 | yes | 43.6s | 42.0s | 1.6s | n/a | n/a | Who supports Caroline when she has a negative experience? |
| 48 | no | 45.1s | 43.3s | 1.8s | n/a | n/a | What types of pottery have Melanie and her kids made? |
| 49 | no | 47.0s | 44.4s | 2.7s | n/a | n/a | When did Caroline and Melanie go to a pride fesetival together? |
| 50 | yes | 17.6s | 15.9s | 1.8s | n/a | n/a | What would Caroline's political leaning likely be? |
| 51 | yes | 44.5s | 38.3s | 6.1s | n/a | n/a | What has Melanie painted? |
| 52 | no | 9.6s | 6.1s | 3.6s | n/a | n/a | What are Melanie's pets' names? |
| 53 | yes | 35.7s | 34.1s | 1.6s | n/a | n/a | When did Caroline apply to adoption agencies? |
| 54 | yes | 43.4s | 41.4s | 2.0s | n/a | n/a | When did Caroline draw a self-portrait? |
| 55 | no | 2.0m | 119.3s | 1.4s | n/a | n/a | What subject have Caroline and Melanie both painted? |
| 56 | no | 20.6s | 18.2s | 2.4s | n/a | n/a | What symbols are important to Caroline? |
| 57 | no | 31.4s | 29.4s | 2.0s | n/a | n/a | When did Caroline encounter people on a hike and have a negative experience? |
| 58 | no | 32.2s | 29.6s | 2.5s | n/a | n/a | When did Melanie make a plate in pottery class? |
| 59 | no | 38.8s | 37.2s | 1.6s | n/a | n/a | Would Caroline be considered religious? |
| 60 | no | 9.6s | 8.1s | 1.5s | n/a | n/a | What instruments does Melanie play? |
| 61 | yes | 25.1s | 23.6s | 1.6s | n/a | n/a | What musical artists/bands has Melanie seen? |
| 62 | yes | 66.2s | 64.3s | 1.9s | n/a | n/a | When did Melanie go to the park? |
| 63 | yes | 32.0s | 29.6s | 2.4s | n/a | n/a | When is Caroline's youth center putting on a talent show? |
| 64 | yes | 41.0s | 38.5s | 2.4s | n/a | n/a | Would Melanie likely enjoy the song "The Four Seasons" by Vivaldi? |
| 65 | yes | 26.6s | 20.6s | 6.1s | n/a | n/a | What are some changes Caroline has faced during her transition journey? |
| 66 | no | 25.1s | 23.0s | 2.0s | n/a | n/a | What does Melanie do with her family on hikes? |
| 67 | yes | 41.1s | 39.5s | 1.5s | n/a | n/a | When did Caroline go biking with friends? |
| 68 | yes | 18.3s | 14.2s | 4.1s | n/a | n/a | How long has Melanie been practicing art? |
| 69 | no | 22.9s | 16.5s | 6.4s | n/a | n/a | What personality traits might Melanie say Caroline has? |
| 70 | no | 66.9s | 62.8s | 4.1s | n/a | n/a | What transgender-specific events has Caroline attended? |
| 71 | yes | 27.0s | 25.4s | 1.5s | n/a | n/a | What book did Melanie read from Caroline's suggestion? |
| 72 | yes | 36.6s | 35.2s | 1.3s | n/a | n/a | When did Melanie's friend adopt a child? |
| 73 | yes | 35.0s | 33.8s | 1.2s | n/a | n/a | When did Melanie get hurt? |
| 74 | yes | 16.0s | 14.2s | 1.7s | n/a | n/a | When did Melanie's family go on a roadtrip? |
| 75 | yes | 71.6s | 70.3s | 1.2s | n/a | n/a | How many children does Melanie have? |
| 76 | yes | 11.2s | 9.2s | 2.0s | n/a | n/a | When did Melanie go on a hike after the roadtrip? |
| 77 | yes | 41.6s | 39.9s | 1.7s | n/a | n/a | Would Melanie go on another roadtrip soon? |
| 78 | no | 60.3s | 52.8s | 7.5s | n/a | n/a | What items has Melanie bought? |
| 79 | yes | 8.2s | 6.3s | 2.0s | n/a | n/a | When did Caroline pass the adoption interview? |
| 80 | yes | 27.1s | 25.7s | 1.4s | n/a | n/a | When did Melanie buy the figurines? |
| 81 | yes | 37.1s | 33.8s | 3.3s | n/a | n/a | Would Caroline want to move back to her home country soon? |
| 82 | yes | 4.7s | 3.6s | 1.1s | n/a | n/a | What did the charity race raise awareness for? |
| 83 | yes | 6.8s | 5.4s | 1.4s | n/a | n/a | What did Melanie realize after the charity race? |
| 84 | yes | 27.9s | 25.9s | 2.0s | n/a | n/a | How does Melanie prioritize self-care? |
| 85 | no | 50.1s | 48.7s | 1.4s | n/a | n/a | What are Caroline's plans for the summer? |
| 86 | yes | 7.7s | 6.2s | 1.4s | n/a | n/a | What type of individuals does the adoption agency Caroline is considering suppor |
| 87 | yes | 7.8s | 6.3s | 1.4s | n/a | n/a | Why did Caroline choose the adoption agency? |
| 88 | no | 28.5s | 26.4s | 2.0s | n/a | n/a | What is Caroline excited about in the adoption process? |
| 89 | yes | 2.4m | 2.4m | 1.7s | n/a | n/a | What does Melanie think about Caroline's decision to adopt? |
| 90 | yes | 18.5s | 16.7s | 1.8s | n/a | n/a | How long have Mel and her husband been married? |
| 91 | yes | 7.7s | 5.8s | 2.0s | n/a | n/a | What does Caroline's necklace symbolize? |
| 92 | yes | 13.6s | 12.1s | 1.5s | n/a | n/a | What country is Caroline's grandma from? |
| 93 | yes | 6.9s | 5.1s | 1.8s | n/a | n/a | What was grandma's gift to Caroline? |
| 94 | yes | 78.0s | 76.3s | 1.7s | n/a | n/a | What is Melanie's hand-painted bowl a reminder of? |
| 95 | yes | 24.6s | 22.4s | 2.2s | n/a | n/a | What did Melanie and her family do while camping? |
| 96 | yes | 15.6s | 12.9s | 2.8s | n/a | n/a | What kind of counseling and mental health services is Caroline interested in pur |
| 97 | yes | 16.5s | 15.1s | 1.4s | n/a | n/a | What workshop did Caroline attend recently? |
| 98 | yes | 8.5s | 6.9s | 1.7s | n/a | n/a | What was discussed in the LGBTQ+ counseling workshop? |
| 99 | yes | 15.8s | 12.2s | 3.6s | n/a | n/a | What motivated Caroline to pursue counseling? |
| 100 | yes | 12.6s | 11.2s | 1.4s | n/a | n/a | What kind of place does Caroline want to create for people? |
| 101 | yes | 8.3s | 6.3s | 2.0s | n/a | n/a | Did Melanie make the black and white bowl in the photo? |
| 102 | yes | 9.2s | 7.7s | 1.5s | n/a | n/a | What kind of books does Caroline have in her library? |
| 103 | no | 24.4s | 22.2s | 2.2s | n/a | n/a | What was Melanie's favorite book from her childhood? |
| 104 | yes | 10.2s | 9.0s | 1.2s | n/a | n/a | What book did Caroline recommend to Melanie? |
| 105 | yes | 15.5s | 13.0s | 2.6s | n/a | n/a | What did Caroline take away from the book "Becoming Nicole"? |
| 106 | yes | 5.9s | 4.5s | 1.5s | n/a | n/a | What are the new shoes that Melanie got used for? |
| 107 | yes | 11.7s | 10.2s | 1.5s | n/a | n/a | What is Melanie's reason for getting into running? |
| 108 | yes | 7.7s | 6.4s | 1.3s | n/a | n/a | What does Melanie say running has been great for? |
| 109 | yes | 12.4s | 9.6s | 2.8s | n/a | n/a | What did Mel and her kids make during the pottery workshop? |
| 110 | yes | 16.5s | 15.0s | 1.5s | n/a | n/a | What kind of pot did Mel and her kids make with clay? |
| 111 | yes | 10.5s | 9.1s | 1.4s | n/a | n/a | What creative project do Mel and her kids do together besides pottery? |
| 112 | no | 40.2s | 38.5s | 1.6s | n/a | n/a | What did Mel and her kids paint in their latest project in July 2023? |
| 113 | yes | 18.5s | 16.8s | 1.7s | n/a | n/a | What did Caroline see at the council meeting for adoption? |
| 114 | yes | 5.6s | 4.4s | 1.2s | n/a | n/a | What do sunflowers represent according to Caroline? |
| 115 | yes | 42.6s | 40.9s | 1.6s | n/a | n/a | Why are flowers important to Melanie? |
| 116 | yes | 12.0s | 9.4s | 2.6s | n/a | n/a | What inspired Caroline's painting for the art show? |
| 117 | yes | 7.4s | 5.7s | 1.7s | n/a | n/a | How often does Melanie go to the beach with her kids? |
| 118 | yes | 11.6s | 9.9s | 1.7s | n/a | n/a | What did Melanie and her family see during their camping trip last year? |
| 119 | no | 40.4s | 37.5s | 2.9s | n/a | n/a | How did Melanie feel while watching the meteor shower? |
| 120 | yes | 7.0s | 5.5s | 1.5s | n/a | n/a | Whose birthday did Melanie celebrate recently? |
| 121 | yes | 7.2s | 5.9s | 1.2s | n/a | n/a | Who performed at the concert at Melanie's daughter's birthday? |
| 122 | no | 14.1s | 12.5s | 1.6s | n/a | n/a | Why did Melanie choose to use colors and patterns in her pottery project? |
| 123 | yes | 7.0s | 5.2s | 1.7s | n/a | n/a | What pet does Caroline have? |
| 124 | yes | 72.4s | 70.6s | 1.9s | n/a | n/a | What pets does Melanie have? |
| 125 | yes | 5.5s | 4.3s | 1.3s | n/a | n/a | Where did Oliver hide his bone once? |
| 126 | yes | 6.3s | 4.9s | 1.4s | n/a | n/a | What activity did Caroline used to do with her dad? |
| 127 | no | 26.3s | 24.5s | 1.8s | n/a | n/a | What did Caroline make for a local church? |
| 128 | no | 23.6s | 21.7s | 1.9s | n/a | n/a | What did Caroline find in her neighborhood during her walk? |
| 129 | yes | 5.5s | 3.9s | 1.7s | n/a | n/a | Which song motivates Caroline to be courageous? |
| 130 | yes | 7.1s | 6.0s | 1.1s | n/a | n/a | Which  classical musicians does Melanie enjoy listening to? |
| 131 | yes | 10.1s | 8.4s | 1.7s | n/a | n/a | Who is Melanie a fan of in terms of modern music? |
| 132 | yes | 11.4s | 9.9s | 1.5s | n/a | n/a | How long has Melanie been creating art? |
| 133 | yes | 30.8s | 29.1s | 1.7s | n/a | n/a | What precautionary sign did Melanie see at the café? |
| 134 | yes | 9.8s | 7.2s | 2.6s | n/a | n/a | What advice does Caroline give for getting started with adoption? |
| 135 | no | 34.1s | 31.3s | 2.8s | n/a | n/a | What setback did Melanie face in October 2023? |
| 136 | yes | 6.0s | 4.7s | 1.3s | n/a | n/a | What does Melanie do to keep herself busy during her pottery break? |
| 137 | yes | 21.5s | 19.2s | 2.3s | n/a | n/a | What painting did Melanie show to Caroline on October 13, 2023? |
| 138 | no | 50.5s | 49.2s | 1.3s | n/a | n/a | What kind of painting did Caroline share with Melanie on October 13, 2023? |
| 139 | yes | 9.0s | 6.4s | 2.6s | n/a | n/a | What was the poetry reading that Caroline attended about? |
| 140 | yes | 36.6s | 35.2s | 1.4s | n/a | n/a | What did the posters at the poetry reading say? |
| 141 | yes | 14.8s | 13.0s | 1.8s | n/a | n/a | What does Caroline's drawing symbolize for her? |
| 142 | no | 14.0s | 11.4s | 2.6s | n/a | n/a | How do Melanie and Caroline describe their journey through life together? |
| 143 | yes | 6.6s | 4.6s | 2.0s | n/a | n/a | What happened to Melanie's son on their road trip? |
| 144 | no | 34.5s | 32.2s | 2.4s | n/a | n/a | How did Melanie's son handle the accident? |
| 145 | yes | 8.5s | 6.8s | 1.7s | n/a | n/a | How did Melanie feel about her family after the accident? |
| 146 | yes | 7.6s | 5.2s | 2.4s | n/a | n/a | How did Melanie's children handle the accident? |
| 147 | yes | 10.8s | 8.0s | 2.7s | n/a | n/a | How did Melanie feel after the accident? |
| 148 | no | 16.8s | 12.7s | 4.1s | n/a | n/a | What was Melanie's reaction to her children enjoying the Grand Canyon? |
| 149 | yes | 13.0s | 11.8s | 1.3s | n/a | n/a | What do Melanie's family give her? |
| 150 | yes | 22.6s | 20.5s | 2.1s | n/a | n/a | How did Melanie feel about her family supporting her? |
| 151 | yes | 10.2s | 8.9s | 1.3s | n/a | n/a | What did Melanie do after the road trip to relax? |
| 167 | yes | 10.2s | 8.3s | 1.9s | n/a | n/a | Did Caroline make the black and white bowl in the photo? |
| 178 | yes | 5.8s | 4.0s | 1.7s | n/a | n/a | Is Oscar Melanie's pet? |
