# drpreetha.com — Findings log (append-only, newest at bottom)
Purpose: every discovery about where traffic, signups and revenue actually come from, with source + date.
Companion: MASTER-CHECKLIST.md (actions). Sync: `bash drpreetha/sync.sh "msg"` → openclaw_master + gbrain + command-hub.

## 2026-10-17 — Ads history
- Google Ads (kiranvk2011, KPSC Practice 144-267-7143): ₹11,395.92 net, all Nov 2025, 3 Performance Max campaigns (now paused). [Google Ads billing]
- Facebook Ads (personal acct 1209421041068162): 1 campaign 28 Nov 2025, ₹301.89, 15,917 impressions, 226 landing-page views. [Ads Manager]
- Total confirmed ad spend ₹11,697.81 (Kiran's estimate ~₹20k; gap unexplained — other months/accounts not found).

## 2026-10-17 — Google Analytics 4 (G-RW72H5NZ2R, property a376088366p514377314, authuser=1)
- Nov 2025–16 Oct 2026 by first-user source: Google Ads 5,113 users, avg 3 s engagement, 3 key events (0.06%) → PMax junk traffic.
- Facebook ad 206 users, 18 key events (7.8%) → ≈₹17/action vs ≈₹3,800/action Google.
- Direct 341 (56 s), Google organic 104 (2 min 26 s), ChatGPT 9 (3 min 21 s, 11% event rate).
- Last 7 days: organic 34, direct 17, ChatGPT 4. Cities: Kochi 22, Kozhikode, Thrissur, Thiruvananthapuram.
- Correction: GA4 tag IS on all 19 pages (earlier "missing" was a login-redirect artefact). Gap was events, not tag.

## 2026-10-17 — Subscriptions (DB) & timing
- 12 signups / 5 paid late Sep–Oct with ₹0 ad spend. Rise from 29 Sep ≈ 6 weeks before Cat 34/2026 exam (12 Nov 2026, SC/ST special recruitment, 44 vacancies). General Cat 177/2025 exam was 1 Dec 2025.
- No renewal / win-back mechanism exists → lapsed users lost silently.

## 2026-10-17 — LinkedIn (Dr Preetha, via neko-preetha)
- 6 followers; 28 days: 641 impressions, 466 reached, 1 reaction, 0 comments. 598 impressions from the single founder-story post. 98% non-network; audience Delhi/healthcare staff, not Kerala aspirants.
- Conclusion: LinkedIn ≈ 0 signups; profile useful only for credibility.

## 2026-10-17 — Google Search position
- Not in top 8 for "kerala psc medical officer previous year question paper", "kpsc assistant surgeon question paper pdf", "kpsc medical officer pyq", "assistant surgeon syllabus 2026". Winners: keralapsc.gov.in, entri, testbook, toppersexam, chiaxma, YouTube.
- /sitemap.xml 404 (sitemap.php works, 21 URLs). Search Console not linked to GA4.

## 2026-10-17 — Meta Pixel 919839944003926 (19 Sep–16 Oct)
- PageView 719, ViewContent 403, QuizQuestionAnswered 170, AIDeepDiveClicked 136, PracticeSessionStarted 76, SampleQuizCompleted 18, StartTrial 6, PaymentPending 5, InitiateCheckout 2, CompleteRegistration 2, Lead 2, Purchase 1. 3 diagnostics open.
- Insight: AI Deep Dive clicks ≈ 80% of quiz answers → strong demand signal for AI Mentor tier. Sample quiz completion low (18 completes vs 170 answers).
- Action taken: every Pixel funnel event now mirrored to GA4 (sign_up, generate_lead, begin_checkout, payment_submitted, payment_pending, practice_session_start/complete, sample_quiz_complete, start_trial). Backup: scratch/drp-backup-*.

## 2026-10-17 — Microsoft Clarity uc0cq7dhg9 (last 30 days)
- 177 sessions / 109 users, 30% returning, 1.7 min active, 2.81 pages/session, scroll 59%.
- Referrers: google.com 65, accounts.google 29, chatgpt 5, **reddit 8 (web 5 + app 3) — not visible in GA4**, Gmail app 3.
- Top pages: home 83, PYQ hub 52, sample-quiz 46, practice 45, 162/2025 20.
- Problems: dead clicks 33% sessions, quick-backs 28%, JS error "'#' is not a valid selector" = 82% of errors, LCP 3.1 s (score 78).
- Microsoft UET/Bing Ads: not installed (not needed unless Bing ads).

## 2026-10-17 — Search Console (URL-prefix property https://drpreetha.com/, kiranvk2011 = authuser 1)
- 16 months (25 Nov 2025–14 Oct 2026): 119 clicks, 1.76K impressions, CTR 6.8%, avg position 7.8.
- Top queries: "assistant surgeon kerala psc previous question papers" 2/7, "kerala psc assistant surgeon previous question papers with answers" 1/8, "dr preetha" 0/52, "psc ent" 0/16, "opsc medical officer free mock test" 0/15 (Odisha PSC — untapped intent).
- Top pages: home 74/891, PYQ hub 22/156, sample-quiz 9/157, 017-2021 4/51, contact 3/394 (high impr, low click), 162-2025 1/42.
- Indexing: 20 indexed, 4 not (2 noindex intentional, 1 canonical alternate, 1 discovered-not-indexed). sitemap.php submitted 1 Oct, read 15 Oct, 21 URLs OK. Domain property sc-domain:drpreetha.com NOT accessible from either account.
- Meaning: PYQ pages already earn Google clicks; volume is tiny — content depth + more pages (C2–C5) is the lever, not indexing.

## 2026-10-17 — Fixes shipped
- JS error "'#' is not a valid selector" (82% of Clarity errors): index.php smooth-scroll skips bare '#'.
- Dead click: "KPSC Practice ▾" menu was hover-only → tap did nothing on phones. Tap-to-open added on 13 pages; verified in neko (opens on tap, closes on outside tap).
- UTM link sheet drpreetha/UTM-LINKS.md (A3).
- Backups: /root/.hermes/cache/scratch/drp-backup-*.
