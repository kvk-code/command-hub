# drpreetha.com — Master growth checklist

> **SENDER RULE:** subscriber/bulk mail is sent From progress@updates.drpreetha.com (Reply-To mail@), never mail@. See INCIDENT-2026-10-23-MAIL-SENDER.md.
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
- [x] B2 Win-back wave 1 SENT 23 Oct 13:40 IST (3/3): EXCLUSIVE returning-customer pack ₹699 = 12 Nov exam + next cycle, past payers only, personal links, valid till 5 Nov. Workflow: WINBACK-WORKFLOW.md
- [ ] B2b Wave 2 (when Kiran decides): signed-up-never-paid → separate welcome/new-features mail (not the returning pack)
- [ ] B3 Automated renewal reminders (7 days, 1 day, expired) + UPI pay link
- [ ] B4 Exam-countdown email to all users before 12 Nov 2026
- [ ] B5 WhatsApp broadcast opt-in at signup

- [ ] B6 Exam Pass 'save ₹197 vs 4 months' misleading when exam <2 months away → compute from next exam date
- [ ] B7 subscribe.php 'Detailed Explanations' overclaim → reword

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
- [~] E2a 28 Oct 23:20 IST: cat34 ad set A (opt PaymentPending custom conv, 2 events total, starved) PAUSED; new ad set A2 120250237764790716 opt LANDING_PAGE_VIEWS (pixel, 1d click), same targeting/₹300/day/end 11 Nov, EN+ML ads copied (same creatives). Meta forbids changing goal/attribution in place. Backup ads/adset-*-pre-lpv-*.json
- [x] E3 (29 Oct) Stop rule LIVE: Hermes no-agent cron every 3h /root/.hermes/scripts/drpreetha-ads-stoprule.py — pauses ad set A2 if spend since 29 Oct 19:15 IST ≥ ₹1k and ₹/meta-signup > ₹150; silent otherwise
- [x] E4 (29 Oct) First-touch attribution LIVE: _attrib.php (via config.php) sets 90-day cookie kp_src (UTM/fbclid/referrer/landing); createUser() saves it to users.signup_src. Rollback kpsc-cache/rollback/attrib-20261029-191526. Baseline: ₹749 spent 25–29 Oct vs 2 new payers (₹1,298) unattributable

## F. Content & social
- [ ] F1 YouTube short per PYQ paper → link to page
- [ ] F2 Instagram reels from Dr Preetha's videos — schedule: drpreetha/instagram/SCHEDULE.md (12 posts Oct27–Nov7 09:30 IST)
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
- [~] C11 (29 Oct) Google still says Athani: site audited clean (84 URLs), public backups/ folder removed, GSC reindex requested for /, /videos.php, /llms.txt. Pending: Azeezia profile end-date, Athani doctors page, LinkedIn
- [ ] C10 contact.php gets 399 impr / 0.75% CTR / 7s — fix title+description for ENT patients or add clinic landing page

## H. Coach-mail system & subscriber flow (added 2026-10-19)
Done:
- [x] H0a Mail tracking pixels live (weekly reports, all MailerPA site mails, inform-subscribers campaigns) — send+open logged per address (29c12f9, bff8d0b)
- [x] H0b "1 questions" subject bug fixed
- [x] H0c Night quote top-up cron 23:00 IST tonight (Alibaba night window 19:30–05:30 IST, qwen3.8-max 60% off; 3.7-plus fallback); verbatim-verified before going live
- [x] H0d Test user kiranvk2011 (id 27) deleted (backup kpsc-cache/rollback/user27-*.json) and re-run as new subscriber; flow shots taken
Pending (exam news first — page + mail depend on it):
- [~] H1 (23 Oct: "🆕 New this week" badge+filter+SEO on news page and cards; news hub live, 20 items; daily card workflow + auto-filters documented in kpsc-news/NEWS-CARD-WORKFLOW.md) (21 Oct: Pattern B chosen, reviewer Dr Preetha OK; kpsc-news/SITE-PATTERN-CHOICE.md) (now: separate public section /kpsc-medical-officer, plan KPSC-NEWS-SEO-SOCIAL-PLAN-2026-10-20.md) Exams section on KPSC Practice Hub + nightly PSC-site scan (page-designer). Plan: KPSC-NEWS-PLAN-2026-10-19.md. Syllabus per category in kpsc-news/syllabus/ (Cat 34/2026 official copy saved 19 Oct)
- [ ] H2 Joining page for lapsed subscribers (page-designer)
- [ ] H3 Weekly exam-news mail to ALL ever-subscribed; lapsed = exam news + join link only, no practice details; active = inside weekly report
- [~] H4 (26 Oct: quote DB + per-user no-repeat LIVE, backfilled from 19 Oct sends; auto top-up NOT built yet — pool 288) Quote DB with per-user usage log (no repeats) + auto top-up when pool runs low
- [ ] H5 Weekly subscriber profiles (feeds mails + future AI coach)
- [x] H6 (26 Oct: wr-coach.py, Sun 17:30 IST OpenClaw cron, number whitelist + content checks, template fallback; first round 5/8 personalised) Qwen-written personalised mail wording (night window), with safety checks
- [ ] H7 Decide on TEST-AGENT-20261019 pending payment (approve to shoot approval flow, or reject)
Subscriber-flow fixes (page-designer review, 4–5.5/10):
- [x] H8 (live since 19 Oct; verified 23 Oct) Plans: false "Save ₹97" / "58% off" — longer plans cost MORE per month; fix prices or labels
- [ ] H9 Payment page: UPI-app deep link + copy-UPI button, clean large QR, prominent amount, correct heading
- [ ] H10 "Where am I?" tracker. Plan: kpsc-news/WHERE-AM-I-TRACKER-PLAN-2026-10-21.md (§11 access model, §12 fetch plan)
  - [x] Lookup engine + index + golden test (Dr Preetha 305/2019 + 092/2020): e2e 21/21
  - [x] Access tiers (free 1 check / Rs50 mo / Rs450 yr / free for QB subscribers), watches, alerts, delete, demand spike: e2e 19/19
  - [x] Letter to KPSC SENT 22 Oct 16:47 UTC to kpsc.psc@kerala.gov.in (Hyperlinking Policy permission). Reply-watch cron 1858071e94ef every 30m — no reply, no bounce as of 26 Oct. KPSC-LETTER-SENT.json
  - [~] Where-am-I page A: box on top LIVE, data-date line LIVE ("Based on PSC documents checked on <built_at>"), sample result LIVE 26 Oct (demo candidate, dashed box, figures read from the in-force list; never a real reg no). Nav link in the KPSC dropdown sitewide + home/news/features/practice. Remaining: impact strip
  - [ ] Payment plan (Rs50/mo UPI autopay, Rs450/yr) + QB-subscriber entitlement hook
  - [~] Nightly cron LIVE (`0 18 * * *` = 23:30 IST, /root/kpsc-tracker/scripts/nightly.py, log /var/log/hermes-cron/kpsc-tracker.log): index rebuilt nightly, golden 21/21, upload OK. Instant fetch (Qwen finder) + adaptive refresh NOT exercised yet — `hot categories []` every run, no real demand
  - [ ] Privacy notice + consent + delete link; lawyer review
  - [x] Copyright acknowledgement live on /where-am-i and sample-quiz.php footers
  - [ ] Demand loop: 0 real user lookups to date (check_log = only uid 66 test + uid 24 demo; queue = 1 test req 093/2019 `no_ranked_list`). 26 Oct: sample result + sample-quiz.php link added to convert the ~9/week organic sessions
- [ ] H11 Profile page: style select, generic placeholders
- [x] H13 (26 Oct, LIVE automatic) Welcome mail for every new subscriber ~10 min after first approval: all Features-page items with GIF loops, growing list synced nightly from features.php, sent from progress@updates; Hub tile drpreetha-updates-mailbox. drpreetha/welcome-mail/README.md
- [x] H12 (verified 23 Oct) Public subscribe.php: clipped "Best Value" badge, all buttons "Coming Soon"


- [ ] H10 "Where am I?" tracker (KPSC stage + shortlist/rank/advice search, nightly crawl, alerts, public impact strip, sponsorship). Plan: kpsc-news/WHERE-AM-I-TRACKER-PLAN-2026-10-21.md. Gate: PSC letter + lawyer review + data-join check before personal search.

## I. Future scope — KPSC news beyond Assistant Surgeon (added 2026-10-19, not now)
- [ ] I1 Dental Assistant Surgeon (Cat 375/2024 ranked list live)
- [ ] I2 Medical Officer — Homoeo / ISM (Ayurveda)
- [ ] I3 Assistant Professor posts, Medical Education
- [ ] I4 Assistant Insurance Medical Officer (IMS/ESI)

## Demo / test account (Kiran 2026-10-26)
- itsmarket09@gmail.com = internal demo account for neko-preetha workflow recordings (new-user flows, Reels). EXCLUDED from subscriber mail (inform_subscribers OWNER_EMAILS) and weekly reports (live kpsc-cron/weekly-report.php, rollback .pre-itsmarket-20261026). command-hub 16c68786.
