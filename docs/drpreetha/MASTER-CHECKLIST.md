# drpreetha.com — Master growth checklist

> **SENDER RULE:** subscriber/bulk mail is sent From progress@updates.drpreetha.com (Reply-To mail@), never mail@. See INCIDENT-2026-10-23-MAIL-SENDER.md.
Created 2026-10-17. Sources: growth-analysis-2026-10-17.md (§8–10), seo-geo-hitlist-2026-10-17.md.
> **NOW (2 Nov):** IMMEDIATE-PRIORITIES-2026-11-02.md (P1–P8)
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
- [x] C4 Hub + paper pages: answer-first summary, FAQ + FAQPage schema, last-updated, reviewer byline, official source links
- [ ] C5 Subject-wise PYQ pages (Medicine, Surgery, OBG, Paeds, PSM, …)
- [ ] C6 Printable PDF per paper
- [ ] C7 Track 10 target queries weekly

## D. AI search optimisation / GEO (expander: seo-geo-hitlist §8–10)
- [x] D1 Expand llms.txt + add llms-full.txt
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
- [~] F2 Instagram reels from Dr Preetha's videos — schedule: drpreetha/instagram/SCHEDULE.md (12 posts Oct27–Nov7 09:30 IST). Site back-links live: vertigo reel De-8ynmj2AX (29 Oct), adenoid reel DfGrNOTgf6X (30 Oct), migraine reel DfOZkVPkrei (1 Nov, published, linked 2 Nov) on / and /videos.php + VideoObject sameAs. All 3 ENT reels now back-linked.
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
- [ ] C12 (30 Oct audit) videos.php "Discovered – not indexed", 0 impr: body ≈ home #videos section. Needs 150–250 words unique Q&A/transcript per video, H1 with keywords, nav "Videos" → videos.php (not #videos), footer-links. Needs Kiran OK (content).
- [x] C13 (30 Oct) Shipped: canonical/og:url "https://drpreetha.com/" (trailing slash), Physician JSON-LD telephone/image/address/sameAs (hospital + Instagram), VideoObject author + sameAs reel URLs. Rollback kpsc-cache/rollback/mmfseo-20261030-113803

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

- [x] E2b (30 Oct 23:00 IST): A2 swap — ML igwa ad 120250237773740716 PAUSED; new EN Riya-voice (OmniVoice clone, "Kerala PSC") feature tour ad 120250268745990716 ACTIVE (video 2465661377574348, creative 2431620110702235, utm_content=en-riya). Existing EN features ad untouched. A/B round ads-envo-20261030, Kiran picked B.

## MMF /app follow-up — 2026-11-01 (Hermes)
- Done: GSC submit, IndexNow (3 engines), schema validator, blind audit, img width/height + .journey img CSS fix (backup app.php.orig), uploaded, headless verify 390/1366 light+dark, linkcheck clean.
- Signal (Matomo, 1 Nov): /app 9 visits + ?src=video 3 + ?src=video2 3; APK downloads 5 (31 Oct–1 Nov). Sample-quiz ad traffic bounces 77–81%.
- Gap: /app has Matomo only, no GA4/Clarity/Pixel tag; app installs can't be attributed to ads.
- [x] E2c (3 Nov, Kiran OK): cat34-page ads 0 signups/~110 LPV vs sample-quiz Riya 5 signups/2 payers → REACTIVATED Riya→sample-quiz 120250268745990716; PAUSED AI-fast+WDGW 120250309146900716; kept Riya→cat34 120250303379070716 as A/B until ~6 Nov.
- [x] E2d (3 Nov, Kiran OK): no-compete split. A2 (₹300/d, cold) now EXCLUDES custom audience 120250314762380716 "site visitors 30d" (pixel); runs Riya→sample-quiz + Riya→cat34. NEW ad set A3 120250314760120716 (₹150/d, same targeting INCLUDING only that audience = warm retargeting) runs AI-fast+WDGW ad copy 120250314764860716 (Exam Pass ₹999). Backup ads/adset-*-pre-a3-*.json. Watch: audience ~20+ people → A3 may under-deliver.
- [x] E2e (3 Nov ~15:15 IST, Kiran OK): 3 Nov ads gave 0 payers. Cause: "features IG→sample-quiz" (6/9 Meta payers in the last week) got almost no budget on 2 Nov, then was paused in the 3 Nov changes. REACTIVATED 120250237770450716; PAUSED Riya→cat34-page 120250303379070716 (0 signups). Re-check tomorrow evening by payer source (users.signup_src).
- [x] H14 (3 Nov, Hermes) Admin Subscribers card: "WDGW tutor" strip with a credits ring (used of granted, same ledger as wdgw-chat.php: +100 per batch every 2 days, carry forward) + Details sheet (admin/wdgw-usage.php: ledger, time on trap questions, every tutor conversation, refused asks). Rollback kpsc-cache/rollback/wdgw-admin-20261103-165535. Src drpreetha/wdgw-admin/. Gap: WDGW page answers are not written to user_question_attempts, so "time on trap questions" stays empty unless the doctor met that question in practice.
- [x] H15 (3 Nov, Hermes) WDGW time tracking LIVE: wdgw-time.php → ask.sqlite `tt` (pick = ms card shown→option, dwell = visible ms per visit, sendBeacon). Admin sheet shows To answer / On card / In AI / Asked + full tutor chat expanded. New Subscribers tab "Top AI users" (?filter=top_ai) ranks by credits used since 2 Nov. Rollback kpsc-cache/rollback/wdgw-time-20261103-171223. Note: uid 85 = itsmarket09 demo account (its off-topic asks were internal tests); uids 137/139 no longer in users table.
- [x] E2f (3 Nov late, Kiran OK): ad analysis since 29 Oct: ₹1,690 spend → 25 meta signups (₹68), 10 payers ₹2,990 (₹169/payer, ~1.8x). Features IG→sample-quiz 7 payers; Riya→sample-quiz 3; all cat34-page ads 0 signups; A3 warm ₹193/561 imp/0 signups. A3 120250314760120716 PAUSED; A2 budget ₹300→₹450/day (ends 11 Nov). Backup ads/adsets-pre-a3pause-*.json

- [x] **E2g (2026-11-04)** Google Search campaign "KPSC Search - exact (test)" LIVE, id 24433646815, acct 144-267-7143. ₹200/day, Max clicks cap ₹40, Search only (no partners/display), India presence-only, AI Max/text-custom/URL-expansion OFF, auto assets off. 10 exact/phrase kws (kerala psc assistant surgeon etc). LP /sample-quiz.php + suffix utm_source=google&utm_medium=cpc&utm_campaign=kpsc_search. 10 headlines/2 desc. Ends 2026-11-11. Old PMax (Fifty Flash/Campaign #1/Subscription Tracker) remain paused/draft. TODO: Google Ads conversion (sign_up) + GSTIN.

- [~] **C14 (2026-11-04)** Google Business Profile CREATED (unverified) in neko-preetha, owner mspreethadr@gmail.com: "Dr. Preetha M S", ENT Specialist, Azeezia Health City, Erattakulam PO, Alathur 678682, 04922 351111, drpreetha.com, Mon–Sat 9:00–16:30, description (no URL; Google rejects URLs). Location id 03763399837277852266. Only verification option = VIDEO (onsite by Kiran, via Google Maps/Business app as mspreethadr). Then: photos, sameAs in Physician JSON-LD, ask Azeezia to fix 8:30→9:00.
- [x] **APP-LOCK (2026-11-04)** Play v5 (vc5, startUrl `?src=twa&b=play5`) approved 11:32 IST on closed track. Old website APK (no `b=play5`, remembered in localStorage kp_build) → 11:53 IST switched back to dismissible "Update to the latest version" banner (Update → Play app page, market:// + web fallback; tester join link) because Play v4 installs looked stuck under the lock (kp-app-pay.js v6, MODE banner; rollback apkbanner-20261104-115331). Emulator E2E flow `apklock` in drpreetha-android. Paid users 33 vs Play list 32: only test/reviewer accounts missing. Rollback kpsc-cache/rollback/apklock-on-20261104-114610 (and apklock-20261104-102106). Known: right after a Play update a warm Chrome tab keeps the old URL → lock tells user to close & reopen app. TODO: versionName still 1.0.2.
- [x] APP-LOCK v2 (4 Nov 12:00 IST): every app launch re-marks build (app-welcome.php → kpsc-practice.php?kb=playN|old; launch w/o marker clears kp_build). Old builds (website APK + Play v4) get full-screen "Update to the latest version" lock, only exit = Update (market:// + web) / Join tester. kp-app-pay.js v9. Rollback apklock2-20261104-115937.
- [x] APP-LOCK v3 (12:34 IST): MIN_BUILD in kp-app-pay.js v11. **Next version: drpreetha/app-lockout/RUNBOOK-NEXT-VERSION.md, then `bump-min-build.py N`.**
- [x] ADMIN bank progress (4 Nov 19:00 IST): dashboard panel "📚 Question bank progress", subscribers sorted by % of the 913-question bank answered, misuse flags fast/burst/guess. `drpreetha/admin-bank-progress/`.
- [~] **Play closed test (4 Nov)**: ≥12 testers opted-in requirement COMPLETED; 14-day clock running → apply for production ~18 Nov. Next app on this personal account needs its own 12×14 test (org account w/ D-U-N-S exempt).

- 2026-11-10 D1+C4 done (geo-d1c4/): _faq.php shared FAQ+FAQPage on 82/93 sitemap URLs (all KPSC/UPSC paper+category pages, cat-34, home); llms.txt UPSC section regenerated from data + llms-full.txt (24.8KB, .htaccess allow); IndexNow 95 URLs. Rollback: kpsc-cache/rollback/geo-d1c4-20261110-geo/. Generators: geo-d1c4/new/gen-llms-*.php — rerun when papers change.
- 2026-11-10 remaining steps: GSC sitemap resubmitted, Brave 8/8 accepted, crawler UA matrix 200 for 14 AI/search bots (Bytespider 403 by design), E2E AI-agent test 4 models (Claude Sonnet, GPT-6.1, Gemini 4, Grok 4.7) answered 5/5 factual questions correctly from live pages.
- 2026-11-10 step 2: schema.org validator 0 errors on 6 samples (fixed home Physician medicalSpecialty enum); FAQ added to sample-quiz + upsc-sample (84/93); blind Gemini audit in geo-d1c4/blind-audit-20261110.txt, fixed 24/25 subjects mismatch + radiogroup label. Open: defer kp-app-pay.js, nav dropdown <button>, paywall isAccessibleForFree:false on paper pages, ISO dates, Quiz hasPart, title length on cat-34.

### 2026-11-10 paysafe + nav + e2e
- v7.0.8 (vc20, MIN_VC=20) is native Flutter, no WebView, never loads kp-app-pay.js. Do NOT defer kp-app-pay.js (old TWA flash risk).
- app-bridge.php: br_paysafe() strips plans/subscribe/pay/UPI routes from home/me/config/notices/page payloads. Unit-tested live. Backup kpsc-cache/rollback/paysafe-20261110/.
- Nav dropdowns: aria-expanded/button role on _pyq-layout + index etc. md5 ok, 93/93 pages 200.
- Emulator v708 run 42670172089: 25/28 pass. Fails = test-account state (unlock card, Rekha id 85 already has Mock 5 attempt) + weekly push notification (also failed in baseline run). Fewer fails than baseline run 42590162963 (13).
- iPhone web: nav, FAQ, prices OK; TWA mode guard=2 hides prices/plan links on all pages.
- 2026-11-10 audit 4-6 live (rollback kpsc-cache/rollback/geo-step3-20261110): KPSC paper dates "1 Dec 2025" + <time datetime>; Cat34 title 122→~85 chars; sample-quiz Quiz schema hasPart = 10 question stems (no answers). Item 3 paywall markup SKIPPED (no hidden paid content in pages). Deploy dir is /home/revirnmt/drpreetha.com (NOT public_html; stray copies removed).

- [ ] **App 7.0.9 (build 21):** running feedback banner on Home + "Share your feedback" button (spec native-app/V709-FEATURES.md, mock V709-feedback-banner-mock.png). After 12 Nov.
- [ ] **App 7.0.9 UI kit:** 15 new server-driven card types + hidden /ui-kit test page (native-app/V709-UI-KIT.md). Tool: native-app/homecards.py.

## H. Medical Education faculty jobs page (2026-11-18)
- [x] H1 /kpsc-medical-education-jobs live on shared layout, crawler files + IndexNow/GSC/Brave done, .php 301
- [ ] H2 Add Cat 166/167 cards after reading PDFs; hub item anchors; check GSC for 'assistant professor' queries in 2 weeks
