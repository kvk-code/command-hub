# drpreetha.com — Master growth checklist
Created 2026-10-17. Sources: growth-analysis-2026-10-17.md (§8–10), seo-geo-hitlist-2026-10-17.md.
Status: [ ] todo · [~] in progress · [x] done. Work one item at a time; Kiran approves each section.

## A. Measurement & tracking (do first — everything else is judged by it)
- [x] A1 GA4 tag: verified already on all 19 public+app pages (earlier 'missing' claim was wrong — curl hit login redirect)
- [~] A2 GA4 events mirrored from Meta Pixel (2026-10-17): sign_up, generate_lead, begin_checkout, payment_submitted, payment_pending, practice_session_start/complete, sample_quiz_complete, start_trial. TODO: mark as Key events in GA4 once they arrive; payment_approved (admin side) pending
- [ ] A3 UTM tags on every social/WhatsApp/LinkedIn/YouTube link
- [ ] A4 Link Search Console ↔ GA4
- [ ] A5 Weekly 1-page dashboard (users by channel, signups, payments)

## B. Retention & revenue recovery (biggest money leak)
- [ ] B1 List expired / unpaid / expiring-in-7-days users from DB
- [ ] B2 Win-back email to ~16 lapsed/unpaid accounts (Gmail draft → Kiran OK → send)
- [ ] B3 Automated renewal reminders (7 days, 1 day, expired) + UPI pay link
- [ ] B4 Exam-countdown email to all users before 12 Nov 2026
- [ ] B5 WhatsApp broadcast opt-in at signup

## C. Google Search SEO (expander: seo-geo-hitlist §1–7)
- [ ] C1 Search Console: sitemap submit, index 11 PYQ URLs, fix /sitemap.xml 404
- [ ] C2 Syllabus & exam-pattern 2026 page
- [ ] C3 Cat 34/2026 (exam 12 Nov) "what to study" page with subject weightage from 913 Qs
- [ ] C4 Hub + paper pages: answer-first summary, FAQ + FAQPage schema, last-updated, reviewer byline, official source links
- [ ] C5 Subject-wise PYQ pages (Medicine, Surgery, OBG, Paeds, PSM, …)
- [ ] C6 Printable PDF per paper
- [ ] C7 Track 10 target queries weekly

## D. AI search optimisation / GEO (expander: seo-geo-hitlist §8–10)
- [ ] D1 Expand llms.txt + add llms-full.txt
- [ ] D2 Unique statistics + citations on every key page (Princeton GEO tactics)
- [ ] D3 Off-site mentions: Quora, Reddit r/KeralaPSC, Telegram channels
- [ ] D4 Weekly check: ChatGPT / Perplexity / Gemini / Google AI Mode answer for target queries

## E. Paid acquisition policy
- [x] E0 Audit done: Google PMax ₹11.4k wasted (3-sec visits); FB ₹302 best (₹17/action)
- [ ] E1 Rule: no Performance Max / Display ever; Search-only if Google
- [ ] E2 Meta test ₹2–3k, Kerala MBBS doctors, → sample quiz, UTM'd, before 12 Nov
- [ ] E3 Stop rule: pause if cost per signup > ₹150 after ₹1k

## F. Content & social
- [ ] F1 YouTube short per PYQ paper → link to page
- [ ] F2 Instagram reels from Dr Preetha's videos
- [ ] F3 LinkedIn: deprioritise (641 impressions, ~0 signups); keep profile for credibility
- [ ] F4 Testimonials from paying users on site

## G. Pricing & AI Mentor tier
- [ ] G1 Keep ₹299 base plan
- [ ] G2 "AI Mentor" waitlist button (demand test) before building
- [ ] G3 Build AI Mentor (per-user progress → topic guidance over question-bank wiki)
- [ ] G4 Launch ₹2,499/exam-cycle premium tier; measure take-rate

## Tracker audit (2026-10-17)
- Meta Pixel 919839944003926 (19 Sep–16 Oct): PageView 719, ViewContent 403, QuizQuestionAnswered 170, AIDeepDiveClicked 136, PracticeSessionStarted 76, SampleQuizCompleted 18, StartTrial 6, PaymentPending 5, InitiateCheckout 2, CompleteRegistration 2, Lead 2, Purchase 1. 3 diagnostics open. No ads running → pixel is a funnel counter only, not attribution.
- Microsoft Clarity uc0cq7dhg9: session expired; needs login (A6).
- Microsoft UET/Bing: NOT installed.
- [x] A6 Clarity logged in (pomi.04092110@outlook.in, neko-preetha). Last 30d: 177 sessions/109 users, 30% returning, 1.7 min active, 2.81 pages/session. Referrers: google.com 65, chatgpt 5, reddit 5 (+3 app), Gmail app 3. Top pages: home 58+25, PYQ hub 52, sample-quiz 46, practice 45, 162/2025 20.
- [ ] A7 Fix JS error "querySelector '#' is not a valid selector" (82% of 23 errors; likely href="#" anchor handler)
- [ ] A8 Investigate dead clicks (33% of sessions) + quick-backs (28%) via Clarity heatmaps
- [ ] A9 Reddit is a referrer — find the thread(s); seed D3 there
- [ ] A10 LCP 3.1s → <2.5s (performance 78/100)
