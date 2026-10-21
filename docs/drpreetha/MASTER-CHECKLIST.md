# drpreetha.com — Master growth checklist
Created 2026-10-17. Sources: growth-analysis-2026-10-17.md (§8–10), seo-geo-hitlist-2026-10-17.md.
Status: [ ] todo · [~] in progress · [x] done. Work one item at a time; Kiran approves each section.

## A. Measurement & tracking (do first — everything else is judged by it)
- [x] A1 GA4 tag: verified already on all 19 public+app pages (earlier 'missing' claim was wrong — curl hit login redirect)
- [~] A2 GA4 events mirrored from Meta Pixel (2026-10-17): sign_up, generate_lead, begin_checkout, payment_submitted, payment_pending, practice_session_start/complete, sample_quiz_complete, start_trial. TODO: mark as Key events in GA4 once they arrive; payment_approved (admin side) pending
- [x] A3 UTM link sheet: drpreetha/UTM-LINKS.md (use for every post/share)
- [x] A4 Search Console ↔ GA4 linked 2026-10-18; reports live under Reports > Search Console
- [ ] A5 Weekly 1-page dashboard (users by channel, signups, payments)

## B. Retention & revenue recovery (biggest money leak)
- [ ] B1 List expired / unpaid / expiring-in-7-days users from DB
- [ ] B2 Win-back email to ~16 lapsed/unpaid accounts (Gmail draft → Kiran OK → send). Offer decided 19 Oct: ₹699 for 3 months
- [ ] B3 Automated renewal reminders (7 days, 1 day, expired) + UPI pay link
- [ ] B4 Exam-countdown email to all users before 12 Nov 2026
- [ ] B5 WhatsApp broadcast opt-in at signup

## C. Google Search SEO (expander: seo-geo-hitlist §1–7)
- [x] C1 Search Console: sitemap.php submitted+read OK, 20/24 pages indexed (rest intentional). Optional: /sitemap.xml alias
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
- [x] A7 Fix JS error "querySelector '#' is not a valid selector" (82% of 23 errors; likely href="#" anchor handler)
- [~] A8 Dead clicks: nav dropdown tap-to-open shipped on 13 pages; re-check Clarity in 7 days. Investigate dead clicks (33% of sessions) + quick-backs (28%) via Clarity heatmaps
- [ ] A9 Reddit is a referrer — find the thread(s); seed D3 there
- [ ] A10 LCP 3.1s → <2.5s (performance 78/100)
- [ ] C8 OPSC (Odisha) Medical Officer: we rank ~#7.5 with 0 clicks — decide: dedicated landing page or adjust sample-quiz title to stop mismatch
- [ ] C9 Blog: add Article JSON-LD + real posts (currently thin)
- [ ] C10 contact.php gets 399 impr / 0.75% CTR / 7s — fix title+description for ENT patients or add clinic landing page

## H. Coach-mail system & subscriber flow (added 2026-10-19)
Done:
- [x] H0a Mail tracking pixels live (weekly reports, all MailerPA site mails, inform-subscribers campaigns) — send+open logged per address (29c12f9, bff8d0b)
- [x] H0b "1 questions" subject bug fixed
- [x] H0c Night quote top-up cron 23:00 IST tonight (Alibaba night window 19:30–05:30 IST, qwen3.8-max 60% off; 3.7-plus fallback); verbatim-verified before going live
- [x] H0d Test user kiranvk2011 (id 27) deleted (backup kpsc-cache/rollback/user27-*.json) and re-run as new subscriber; flow shots taken
Pending (exam news first — page + mail depend on it):
- [ ] H1 (21 Oct: Pattern B chosen, reviewer Dr Preetha OK; kpsc-news/SITE-PATTERN-CHOICE.md) (now: separate public section /kpsc-medical-officer, plan KPSC-NEWS-SEO-SOCIAL-PLAN-2026-10-20.md) Exams section on KPSC Practice Hub + nightly PSC-site scan (page-designer). Plan: KPSC-NEWS-PLAN-2026-10-19.md. Syllabus per category in kpsc-news/syllabus/ (Cat 34/2026 official copy saved 19 Oct)
- [ ] H2 Joining page for lapsed subscribers (page-designer)
- [ ] H3 Weekly exam-news mail to ALL ever-subscribed; lapsed = exam news + join link only, no practice details; active = inside weekly report
- [ ] H4 Quote DB with per-user usage log (no repeats) + auto top-up when pool runs low
- [ ] H5 Weekly subscriber profiles (feeds mails + future AI coach)
- [ ] H6 Qwen-written personalised mail wording (night window), with safety checks
- [ ] H7 Decide on TEST-AGENT-20261019 pending payment (approve to shoot approval flow, or reject)
Subscriber-flow fixes (page-designer review, 4–5.5/10):
- [ ] H8 Plans: false "Save ₹97" / "58% off" — longer plans cost MORE per month; fix prices or labels
- [ ] H9 Payment page: UPI-app deep link + copy-UPI button, clean large QR, prominent amount, correct heading
- [ ] H10 Under-review page: broken label/value table, mixed success/pending signals
- [ ] H11 Profile page: style select, generic placeholders
- [ ] H12 Public subscribe.php: clipped "Best Value" badge, all buttons "Coming Soon"


- [ ] H10 "Where am I?" tracker (KPSC stage + shortlist/rank/advice search, nightly crawl, alerts, public impact strip, sponsorship). Plan: kpsc-news/WHERE-AM-I-TRACKER-PLAN-2026-10-21.md. Gate: PSC letter + lawyer review + data-join check before personal search.

## I. Future scope — KPSC news beyond Assistant Surgeon (added 2026-10-19, not now)
- [ ] I1 Dental Assistant Surgeon (Cat 375/2024 ranked list live)
- [ ] I2 Medical Officer — Homoeo / ISM (Ayurveda)
- [ ] I3 Assistant Professor posts, Medical Education
- [ ] I4 Assistant Insurance Medical Officer (IMS/ESI)
