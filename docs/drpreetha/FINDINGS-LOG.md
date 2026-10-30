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

## 2026-10-17 — MakeMeFamous run: tag audit (live HTML, 23 public pages + 5 app pages)
- All 21 sitemap pages + subscribe/special-offer: title, description, canonical, OG, Twitter card, GA4, Meta Pixel, Clarity all present. No tag gaps.
- App pages (plans, kpsc-practice, profile, subscription-status): GA4 (via config GA4_MEASUREMENT_ID), Pixel, Clarity in source; login-gated so crawlers see Google sign-in (correct).
- coverage.php, mail-prefs.php: no trackers — internal/robots-disallowed, intentionally left.
- JSON-LD missing on sample-quiz, features, blog, legal pages → added Quiz (sample-quiz) + Product/Offer ₹299 (features).
- llms.txt lacked subscribe page → added.
- Reindex: IndexNow 23 URLs (indexnow.org/Bing/Yandex 200), GSC sitemap resubmitted.
- GSC 28d: "opsc medical officer free mock test" 15 impr @7.5 + "...mock test free" 6 @8.2, 0 clicks → Odisha intent we rank for but don't serve.

## 2026-10-18 — A4 done: Search Console ↔ GA4 linked (end-to-end verified)
- Link: GSC https://drpreetha.com/ (URL-prefix) → GA4 stream drpreetha.com (13049052249), by kiranvk2011. Reports > Search Console > Queries / Google organic search traffic now populated (data back to Sep 2025).
- Organic landing pages (Sep 2025–16 Oct 2026; clicks / impr / engagement / avg time / key events):
  - / : 76 / 904 / 65% / 1m19s / 2
  - PYQ hub: 25 / 166 / 76% / 2m48s / 2  ← best page: highest CTR (15%), engagement, time
  - sample-quiz: 9 / 159 / 53% / 1m37s / 2
  - 048-2024: 2 / 27 / 75% / 1m29s / 2
  - contact.php: 3 / 399 / 67% / 7s / 0  ← 399 impressions, 0.75% CTR: ENT-patient intent landing on wrong page
  - Total organic: 129 clicks, 110 users, 10 key events.
- Meaning: PYQ hub converts best per click → push internal links/titles toward it; contact.php needs an ENT-clinic landing (Palakkad) or better title/description.

## 2026-10-19 — MakeMeFamous over pricing/policy pages + full funnel tracking
- Pages: subscribe, plans, refund-policy, shipping, terms. All carry GA4 G-RW72H5NZ2R + Meta Pixel + Clarity (verified by live network capture in neko-preetha).
- New events: GA4 ecommerce view_item_list / select_item / begin_checkout (value, upgrade credit) / add_payment_info / payment_submitted; policy_view; free_sample_click. Pixel AddToCart on public plan buttons, FreeSampleClick. Clarity tags page_type, plan_selected, is_upgrade, current_plan, identify(u<id>), upgrade on payment submit.
- subscribe.php: Product JSON-LD with 3 Offers (299/999/1999) from pricing.php. sitemap.php + subscribe.php; llms.txt plan/refund/shipping facts.
- IndexNow (indexnow.org 200, Bing 200, Yandex 202), GSC sitemap resubmitted.

- 2026-10-19: GA4 key events now: payment_submitted, sign_up, begin_checkout (+ existing subscription_submitted, ads_conversion_PURCHASE_1). Meta pixel Purchase/InitiateCheckout are standard events (usable as ad optimisation goal). Cron eff43c099a54 2 Nov 10:00 IST plan-click review.

- 2026-10-19: weekly batch sent 09:10 IST from pre-pixel drafts (opens untracked); takeaways drpreetha/SESSION-TAKEAWAYS-2026-10-19-pricing-tracking.md

## 2026-10-24 — LinkedIn link-card audit (Dr Preetha, 20 posts)
- Card present where expected: Azeezia announcement (24 Oct), Athani thank-you (16 Oct), platform intro (17 Oct).
- Video/image posts (10, plus the 2025 image posts) have no card by design; links stay in the text.
- MISSING: post 13 "All 10 Kerala PSC Medical Officer papers" (22 Oct, 174 impressions). Cause: "keralapsc.gov.in" appeared before
  our link, so LinkedIn tried to card that site, which has no og:image. Edit cannot add a card ("Cannot display preview").
- Fix: corrected text (drpreetha link first, "the KPSC website") shows a full thumbnail card in the composer; repost awaits Kiran's OK.
- Workflow: li_card_lint.py + composer gate in sched.py (command-hub), rule in skill linkedin-profile-ops + gbrain social-post-preview-check.
- 2026-10-24 follow-up: PYQ post reposted with card, original deleted. Mobile "blank cards" on video posts were connectivity (posters all valid, 200 image/*); no further reposts.
- 2026-10-24 makemefamous run (Azeezia move + preview image):
  * Preview image `og-card-v4.jpg` (served on every page via `DEFAULT_OG_IMAGE` in `config.php`) still said "ENT Consultant, Athani Hospital". Regenerated as `og-card-v5.jpg` with Azeezia Health City, uploaded to `/images/`, `config.php` edited to point at it. Rollback: `config.php.pre-og5-20261024`.
  * All 24 sitemap pages now serve `og-card-v5.jpg` (verified 200 + `</html>` on each).
  * LinkedIn Post Inspector re-scraped homepage, PYQ hub, features.php — all three show the large card with "Azeezia Health City".
  * IndexNow batch: 24 URLs → api.indexnow.org 200, bing 200, yandex 202.
  * GSC sitemap resubmitted (204). URL Inspection: 22 of 24 already indexed; `/videos.php` (not on Google) and `/subscribe.php` (crawled - not indexed) are the only gaps.
  * Google "Request indexing" accepted for all 6 changed pages (home, privacy, terms, contact, features, videos) via pr45866 Playwright.
  * Stray `</div>` in `privacy.php` (introduced by this morning's rewrite) removed. Rollback: `privacy.php.pre-div-20261024`. Verified: no nesting problems, ends `</html>`.
  * GSC 28-day totals (24 Sep–21 Oct): 72 clicks / 757 impressions / 6.5 avg position, up from 13 / 216 / 15.9 in the previous 28 days.
  * Site's own Matomo (stats.drpreetha.com, Oct 1–24): 1,001 visits, 83% bounce, 52 s avg time, 1.9 actions/visit. Channels: Direct 762, Search 124, Websites 93, AI Assistants 19, Social 3. Top pages: home 578, PYQ hub 96, sample-quiz 60, features 39.
  * Gemini-4-argon blind audit (home 50/70, privacy 49/70): "must" fix on privacy (the stray `</div>`) is done. Remaining audit suggestions: add `sameAs` links to Azeezia profile + videos to JSON-LD; add visible "Assistant Surgeon" to homepage body; add prominent above-the-fold links to `kerala-psc-medical-officer` and `where-am-i`. None shipped this run.
  * Trends agent site brief (`trends-research/drpreetha.com/FOCUS.md`) updated to name Azeezia.
  * Trends cron (`trends-research/trends_daily.py`) `gsc()` rewritten to stdlib-only (`urllib`): the previous `googleapiclient` import silently failed under `python3 -I`, so the daily log was reporting "Search Console data unavailable" for the last week. Verified live: 17 rows returned for drpreetha.com.

## 2026-10-24: GSC structured-data mails (Merchant listings + Product snippets)
- Fixed: Product `image` added on subscribe.php + features.php; features.php brand Person→Brand. Live JSON-LD verified; GSC indexing requested for both.
- Left as-is (honest): aggregateRating/review (no real reviews, no fabrication), shippingDetails/hasMerchantReturnPolicy (non-critical, digital product).
- Pitfall: gws needs `--account kiranvk2011@gmail.com` or it silently reads kiranvk@nssce.ac.in.
- Details: SESSION-TAKEAWAYS-2026-10-24-gsc-structured-data.md

## 2026-10-26 — Weekly visitor & purchase report (19–25 Oct IST vs 12–18 Oct)
- Traffic up: GA4 87 users / 116 sessions (prev 48 / 58); but 36 "referral" sessions are accounts.google.com sign-in returns and Kochi = 64 sessions (own testing incl. features-impact-mock.php), so real growth is smaller. ChatGPT 17 sessions (prev 6), Google organic 24 (prev 35), Facebook (paid 4 + referral 6) new.
- Funnel: plans seen by 10 users → plan clicked 5 (Monthly 3, Exam Pass 2, Yearly 0) → begin_checkout 8 → payment_submitted 2 (prev 4) → approved 3, ₹598 (prev ₹897). Biggest drop: checkout started → payment submitted (8 → 2). 6 signups, all 6 unpaid so far; 10 active subscribers, 2 expire within 14 d.
- Learning: 114 questions answered by 3 learners (prev 30). Mails: 29 sent / 13 opened; campaign opens at "0 min" look like draft-preview pixel hits, not real opens; 14 weekly-progress mails (7 uids) built, 0 opens yet.
- Clarity 99 sessions: 0 rage, 20 dead-click sessions (20%), 22% quick backs, 0 JS errors, perf 76/100 (LCP 3.1 s). Smart events: begin_checkout_monthly 5, begin_checkout_exam_pass 1, payment_submitted 1. Pixel (Graph API): PageView 547, ViewContent 157, PaymentPending 4; AddToCart/InitiateCheckout/Purchase 0 — pixel AddToCart added 19 Oct is NOT arriving.
- Fixes this run: db_week.py depended on pruned scratch rsql.py → rebuilt beside it (weekly-insights/rsql.py); GA4 read via Data API token (ga4_pull.run), not the browser; pixel via Graph /stats. Clarity prev-7 custom range did not apply (skipped). One tab opened and closed in neko-preetha.

## 2026-10-28 ~23:00 IST — makemefamous run (post PSC/UPSC launch)
- Health: 88 sitemap URLs all 200, end `</html>`, one H1, index/follow, self-canonical. 7 crawler UAs 200 on sampled pages; robots/llms fine (llms has UPSC section).
- IndexNow 88 URLs: api.indexnow.org/bing/yandex 200. GSC sitemap PUT 204.
- URL Inspection: 28 indexed (all KPSC + core pages), 31 Discovered-not-indexed, 28 unknown — all UPSC (1 inspect 500). Request-indexing script failed: Playwright connect_over_cdp to neko :9223 timed out.
- GSC 28d: 95 clicks / 1,129 impr / pos 6.3 (prev 28d 20 / 237 / 12.5). Top: PYQ hub 33 clicks, home 20, sample-quiz 10. "opsc medical officer free mock test" 33 impr 0 clicks; contact.php 109 impr 0 clicks; features 66 impr 0 clicks.
- Gemini blind audit (home 51, UPSC hub 51, CMS paper 44 /70), verified on live HTML:
  * UPSC hub + paper pages carry KPSC copy: "answer key published by the Kerala Public Service Commission" + "Not affiliated with the Kerala PSC" (wrong, YMYL trust).
  * Home meta/og description has double-escaped `&amp;amp;`.
  * UPSC hub links 0 paper pages directly; paper pages only prev/next (deep crawl chain) → likely cause of non-indexing. Home links only /upsc-medical.
  * Suggested: full CMS paper grid on hub + all-papers nav on each paper, titles with "UPSC CMS ... PDF", short rationale per sample answer.
- Not shipped this run (needs Kiran OK).
- SHIPPED 28 Oct ~22:45 IST (Kiran OK), rollback /home/revirnmt/kpsc-cache/rollback/mmfseo-202610281710/, md5 verified:
  * _pyq-layout.php: author box + footer disclaimer bank-aware ($GLOBALS['PYQ_BANK']='upsc' → UPSC wording); footer + PSC menu link to /upsc-medical/doctor.
  * upsc-medical.php: "All UPSC medical question papers" list (56 links); title "UPSC CMS & Medical Previous Year Question Papers 2016–2026…".
  * upsc-question-paper.php: all-papers-in-category nav + links to hub/KPSC; titles "UPSC CMS 2025 Paper I Question Paper with Answers & PDF".
  * index.php: &amp;amp; fixed; UPSC quick links (CMS hub, CMS 2026/2025, AYUSH, Nursing) under the UPSC door.
  * 88/88 URLs 200 + </html>; IndexNow re-pinged. Copies in makemefamous/seo-20261028/.

## 2026-10-30 ~11:40 IST — Adenoid reel link + makemefamous run (/ and /videos.php)
- Adenoid reel published 09:30 IST: https://www.instagram.com/reel/DfGrNOTgf6X/ — "Also on Instagram" line added to the adenoid card on index.php + videos.php (rollback kpsc-cache/rollback/igadenoid-20261030-053522/, php -l clean, curl-verified).
- Crawlers: Googlebot, bingbot, GPTBot, ChatGPT-User, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended all 200 on both URLs (cache-busted). Sitemap lastmod 2026-10-30 for both; llms.txt already lists adenoids under Videos. Pages end `</html>`.
- IndexNow (api.indexnow.org, bing) 200 ×2 runs; Yandex success:true. GSC sitemap resubmitted (API). URL Inspection: / = Submitted and indexed, lastCrawl 30 Oct 05:44Z; videos.php = Discovered – currently not indexed. Request indexing via raw CDP on neko-preetha (/u/1/) → both REQUESTED ("priority crawl queue"); created tab closed.
- Blind Gemini audit (home 53/70, videos 37/70), verified on live HTML then shipped (rollback mmfseo-20261030-113803, md5 before/after logged, php -l clean, JSON-LD re-parsed live):
  * canonical/og:url were `https://drpreetha.com` (no slash) → now `https://drpreetha.com/`.
  * Physician JSON-LD lacked root telephone/image/address/sameAs → added (Azeezia + @drpreetha.ms).
  * VideoObject graph: added author (Physician) + sameAs reel URLs (vertigo, adenoid). .jpg thumbnails verified 200 image/jpeg (audit's mismatch claim = false positive).
  * Rejected: "2026 dates are typos" (they are real); heading/transcript/nav rewrites for videos.php logged as C12 (content, needs OK).
- Signals (GA4 23–29 Oct vs 16–22 Oct): users 545 vs 38, sessions 639 vs 70 — driven by Paid Social/meta 425 sessions (ad set A2). Organic google 97 (prev wk n/a in pull), chatgpt.com 28, accounts.google.com 40 (discount), Kochi 239 (includes own testing). Key events: start_trial 50, sign_up 24, payment_submitted 28, ads_conversion_PURCHASE 31, video_play 4. videos.php: 3 sessions (2 google-signin, 1 welcome_mail); instagram landing 1 (sample-quiz).
- Pixel 23–29 Oct vs prev: PageView 1470/398, ViewContent 894/113, QuizQuestionAnswered 362/20, SampleQuizCompleted 31/2, PaymentPending 34/4.
- GSC 28d (30 Sep–27 Oct vs prev): 106 clicks / 1,258 impr / pos 6.2 (prev 19 / 225 / 12.8). Top: PYQ hub 39, home 21, sample-quiz 11. Zero-click: contact.php 111 impr, features 75, "opsc medical officer free mock test" 25+9 impr, "dr preetha" 23 impr pos 22.7 (brand query not ranking — Athani/Azeezia confusion, C11). videos.php: 0 impressions.
