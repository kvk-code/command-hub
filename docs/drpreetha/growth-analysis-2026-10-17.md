# drpreetha.com: what is driving subscriptions, and what to do next (17 Oct 2026)

Sources: production DB (read-only probe, deleted, confirmed 404), Oct-2026 Apache logs, Google Ads billing, FB Ads Manager, public KPSC notices, competitor pricing. Totals only. No personal data.

## 1. The numbers

- 28 accounts in total. 12 approved paid subscriptions, plus 1 owner grant.
- **Nov 2025 wave** (26–30 Nov): 6 signups and 4 paid (3 at ₹299, 1 at the ₹50 flash price). Google Ads ₹11,396 and FB ₹302 ran in the same days. The KPSC Assistant Surgeon OMR test (177/2025) was on **1 Dec 2025**. So the ads ran into peak exam demand.
- **Dec 2025 – Aug 2026**: 6 signups and 1 paid. Ads were off and there was no exam close by.
- **Current wave** (29 Sep – 16 Oct 2026): 12 signups and 5 paid (42% conversion), plus 1 earlier signup who paid on 15 Oct. **₹0 ad spend.** All Google Ads campaigns have been paused since Nov 2025.
- No renewals so far. None of the four Nov-2025 subscribers renewed after their month ended. Two current subscriptions expired on 15 Oct 2026, and both users were active within the past week.

## 2. Traffic sources for October (logs, bots removed)

- About 90% of visits have no referrer. Typical sources are WhatsApp, Telegram, the LinkedIn and Facebook apps, typed URLs, and bookmarks.
- Google organic: 118. Google sign-in return: 68. Gmail app: 7. ChatGPT (`utm_source=chatgpt.com`): 4. Reddit: 3.
- Most-visited pages: `/`, the PYQ hub (84), kpsc-practice (82), features (56), sample-quiz (44), plans (24), videos (22), and the individual paper pages 162-2025, 048-2024, and so on. **The SEO PYQ pages are now working as an entry point.**
- **There is no Google Analytics, gtag, or Meta pixel on the site.** No GA data exists for kiranvk2011, so attribution can only come from logs and the DB.

## 3. What probably caused the current wave, ranked by evidence

1. **Word of mouth and messaging-app sharing** (strong evidence). Most traffic has no referrer, signups come from all over Kerala (TVM, Kottayam, Thrissur, Kozhikode, Kasaragod, Idukki), and there is no paid traffic.
2. **Credibility from a real person** (medium). The Videos page, the doctor's profile, and the LinkedIn refresh give the site a face. In the Nov 2025 wave 2 of 6 signups did not pay; in this wave 7 of 12 did not pay. But the users who do pay now stay and keep using the site (last activity within the past 1–2 days). That is consistent with trust, but it cannot be proven without UTM or GA data.
3. **PYQ / SEO content** (medium). The pages for papers 162-2025, 048-2024 and others are landing pages, and Google organic is the largest *named* source.
4. **Low ₹299 price** (helps, but is not the trigger). The price was also ₹299 during the quiet Dec–Aug months. Price lowers friction; demand comes from the exam cycle and from trust.
5. **LinkedIn posts** (weak so far). Posts went out daily from 10/11 Oct. Signups were already rising from 29 Sep, before the posts. The LinkedIn app hides referrers, so its effect may sit inside the "direct" bucket. UTM tags are needed to measure it.
6. **Exam cycle** (strong external factor). KPSC Assistant Surgeon notifications for 2026 (including NCA SC/ST vacancies) are out, so aspirants are active again.

## 4. Retention: the biggest gap

- **0% renewal so far.** On ₹299/month that is the main revenue problem.
- To build:
  - Expiry reminder mails at D-5, D-1, and D+3, with a one-tap UPI renewal link. The PHP mailer and IMAP Sent already work.
  - A "Your access ends in N days" banner inside the app.
  - A win-back mail to everyone with an expired subscription or with signup but no payment (about 16 accounts): new videos and PYQs, plus a short "₹299 → 3 months for ₹699" offer.
  - Encourage a **3-month or exam-cycle plan** (for example ₹699 / 3 months, ₹1,499 until the exam) so people are not churning every month.

## 5. Raising to ~₹2,500 with a personal AI tutor

- Market reference: Marrow and PrepLadder NEET-PG plans cost about ₹5,000–₹20,000 per year *for national-level content*. A KPSC-only niche at ₹2,500/month is high for a monthly plan. ₹2,500 **per exam cycle (≈3–6 months)** sits in the accepted range.
- Recommendation: **a tier on top, not a replacement**:
  - ₹299/mo Basic (question bank and PYQs). Keep the entry price low; that is what converts.
  - ₹2,499 per cycle **"AI Mentor"**: a per-user agent that knows the question-bank wiki, tracks weak topics from their attempt history (`ai learning tracking` already exists), sets a daily plan, explains every wrong answer with citations to the bank, and runs mock tests tuned to the user.
- Expected effect: replacing ₹299 outright with ₹2,500 would probably cut new conversions sharply (the current buyers are price-sensitive young MBBS graduates). As a tier, it should bring in a few high-intent users. Even 1 in 10 upgrading roughly doubles revenue per user.
- Build the model cheaply: RAG over the bank plus the user's attempt log, on an existing LLM. Do not fine-tune first; fine-tuning only becomes worthwhile once there are hundreds of explanation pairs.
- Test before building: put the tier on `/plans.php` as "AI Mentor — join waitlist (₹2,499)" and count the clicks over 2 weeks.

## 6. Measurement fixes (cheap, do first)

- Add GA4 plus a Meta pixel, or at least log `utm_*` on signup into a `users.source` column.
- Put UTM tags on every LinkedIn, FB, and WhatsApp link (`?utm_source=linkedin&utm_campaign=post05`).
- Add a "How did you hear about us?" dropdown to profile completion.

## 7. Ads, if spent again

- Run them only in the ~6 weeks before a KPSC MO exam date. Target PYQ pages and sample-quiz, and set conversion = paid subscription (the Nov 2025 campaigns optimised for clicks).
- Cost per paid user in Nov 2025 was roughly ₹11,700 / 4 ≈ **₹2,900**, against ₹299 revenue. Ads only pay off if retention or the higher tier is in place.

## 8. UPDATE: Google Analytics (GA4 G-RW72H5NZ2R, kiranvk2011, property 514377314), 1 Nov 2025 – 16 Oct 2026

Correction: GA4 *is* installed on `/`, features and videos. It is missing from kpsc-practice and plans, so conversion tracking is partial.

Users by first-user medium:
- **cpc (Google Ads): 5,113 users (83% of all users), 3 s avg engagement, 0.23 engaged sessions/user, 3 key events, 0.06% key-event rate.**
- (none)/direct: 341 users, 56 s, 32 key events, 2.65%.
- paid (FB ad): 206 users, 9 s, 18 key events, **7.77%**.
- organic: 104 users, **2 m 26 s**, 6 key events, 2.88%.
- referral: 75 users, 1 m 10 s, 2.67%.
- ai-assistant (ChatGPT): 9 users, 3 m 21 s, 11.1%.
- Last 7 days: google organic 34, direct 17, chatgpt 4. Cities: Kochi 22, Kozhikode 6, Thrissur 4, TVM 3.

Verdict:
- The ₹11,396 Google Ads (Performance Max) spend bought ~5,100 low-quality visitors. With 3 s engagement, this is almost certainly display/partner placements, i.e. junk clicks. Cost was ~₹2.2 per user and ~₹3,800 per key event.
- The ₹302 FB ad produced 18 key events from 206 users, about **₹17 per key event**: >200× more efficient than Google Ads.
- The current wave is organic and direct (SEO PYQ pages + sharing), plus a small but high-intent ChatGPT referral stream.
- Next time: FB/IG (Meta) ads for Kerala MBBS graduates, or Google *Search*-only campaigns on "KPSC assistant surgeon questions" keywords. **Never PMax/Display.**
- TODO: add the GA tag to kpsc-practice and plans, mark `purchase`/`subscription_submitted` as a key event, and link Search Console (GA recommends it; you're a verified owner).

## 9. UPDATE: LinkedIn (Preetha NEKO, logged in via her Google account), 20 Sep – 17 Oct 2026

- 6 followers. Posts: 641 impressions in total, 466 members reached, 1 reaction, 0 comments, 0 reposts.
- 98% of impressions went to people outside her network. Top audience: Greater Delhi 12%, Hospitals & Health Care 29%. That is not Kerala MBBS aspirants.
- The founder-story post reached 598 impressions. Every feature post got fewer than 20.
- Profile views: 3 in the past 90 days, plus 6 private viewers.
- Verdict: **LinkedIn contributed close to zero signups.** It works as a credibility page (people who Google her find a real doctor) but not as an acquisition channel.

## 10. REVISED ATTRIBUTION (all sources combined)

| Driver | Evidence | Weight now |
|---|---|---|
| Google organic / PYQ SEO pages | GA: largest source in the last 7 days (34 users), 2m26s engagement; PYQ pages in top landings | **High** |
| Direct / word of mouth (WhatsApp, Telegram groups) | GA direct 17 users/7d, 56s avg; logs ~90% no referrer; signups spread over 10+ districts | **High** |
| Exam cycle (Cat 34/2026 SC/ST, exam 12 Nov 2026) | signups climb from 29 Sep, about 6 weeks before the exam | **Medium-high** |
| Credibility (videos, doctor profile) | paid users stay active; videos page in top landings; unprovable without UTMs | **Medium** |
| ChatGPT referrals | 9 users, 11% action rate; growing | Low volume, high quality |
| ₹299 price | same price in the quiet months | Enabler, not the trigger |
| LinkedIn posts | 641 impressions, 1 engagement, mostly outside Kerala | ~None |
| Google Ads PMax (Nov 2025) | 5,113 users at 3s, 0.06% action rate | Wasted |
| FB ad (Nov 2025) | 206 users, 7.8% action rate, ₹17/action | Best paid channel |

### Priority actions
1. Renewal and win-back mails, about 16 lapsed or unpaid accounts. This is the biggest revenue gap.
2. A ₹2,000–3,000 Meta ad test aimed at Kerala MBBS / medical officers in the 3 weeks before 12 Nov, pointing to sample-quiz with UTM tags.
3. Put GA on kpsc-practice and plans, add a subscription key event, and link Search Console.
4. Grow the SEO PYQ pages (one page per paper and topic), which is the channel that is actually working.
5. Keep LinkedIn only as a profile and credibility page. Move the content effort to WhatsApp/Telegram groups for KPSC MO aspirants and Instagram reels of her videos.
6. AI Mentor tier at ₹2,499 per exam cycle, on top of ₹299. Validate it with a waitlist button first.
