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

## 2026-11-01 ~23:20 IST — Question-bank protection live (King)
- Uid 95 copied about 770/913 questions in 3 days, using rapid taps to reveal the key. Manual hold + mail at 21:57.
- Shipped:
  * watermark on question cards (name · last 4 phone · #uid · date);
  * 150 new questions/day cap (revision of seen questions unlimited);
  * auto-hold at 40 answers under 3 s within 1 h (SYSTEM_RAPID, mail, ⚡ alert to Telegram via the review cron);
  * Terms "Suspension for abnormal usage or misuse" + Privacy purpose.
- E2E on web (iPhone/desktop) + real APK on the emulator.
- Details: SESSION-TAKEAWAYS-2026-11-01-QUESTION-BANK-PROTECTION.md; command-hub docs/drpreetha/bank-protect/.

## 2026-11-02 ~00:30 IST — Clarity account-number tagging + PII leak fixed (King)
- Athira (uid 95): 0 Clarity recordings across ~950 sessions. Most likely a tracker blocker; server logs remain the evidence.
- LIVE: signed-in pages tag Clarity with `u<uid>` only (filter: Custom filters → Customised user ID).
- Fixed a pre-existing leak: e-mail went to Clarity via the avatar seed and the title attribute, and the name via profile text and the watermark attribute. Now hashed or masked; the display is unchanged.
- Privacy page updated.
- E2E: web 10/10 + emulator APK.
- Details: SESSION-TAKEAWAYS-2026-11-02-CLARITY-ID-PII-ATHIRA.md; command-hub docs/drpreetha/clarity-id/.

## 2026-11-02 Weekly (last7 vs prev7)
- Big Meta ad burst: GA4 users 1545 vs 87, Paid Social 1137 sessions (meta). Pixel ViewContent 2542 vs 157, PaymentPending 47 vs 4.
- Funnel: ~1545 visitors -> plans.php 285pv -> select_item 166 -> begin_checkout 158 -> payment_submitted 48 -> approved 15. Biggest drop: checkout->submitted (158->48, ~70% lost).
- Most-clicked plan: Monthly (77 clicks/69 checkouts) >> Exam Pass (17). DB: 15 monthly approved + 1 exam_pass = Rs 5185.
- Signups 51 vs 6; 35 signed-up-never-paid; active subs 24; expiring in 14d: 5. Clarity 1536 sess, 142 dead-click sess, 120 quick-backs, 123 JS errors (webview postmessage).
- Clarity prev7 unavailable (dashboard has no prev-period compare).

## 2026-11-02 MakeMeFamous — migraine reel back-link + reindex (17:00 IST)
- Migraine reel published @drpreetha.ms = /reel/DfOZkVPkrei/ (1 Nov, caption "തലയുടെ ഒരു വശത്ത്… മൈഗ്രേൻ", #Migraine). Added `<p class="vr-src">Also on Instagram</p>` to migraine card in index.php + videos.php (backup kpsc-cache/rollback/igmigraine-20261102-110705). Verified live, both end </html>.
- Audit fix: migraine VideoObject lacked `sameAs` (vertigo/adenoid had it). Added sameAs reel URL in videos.php schema (backup igmigraine-sameas-20261102-114220). All 3 ENT VideoObjects now have sameAs. Mobile 390px card renders OK.
- Crawler access: all 10 AI+search UAs 200 on / and /videos.php; key file + sitemap/llms/robots 200. IndexNow (api.indexnow.org+Bing+Yandex) 200. GSC sitemap resubmitted (0 warn/err). GSC Request Indexing done both URLs via raw CDP neko-preetha (/=on Google, /videos.php=not on Google yet — newer).
- GSC 28d (10-05→11-01): 204 clicks / 1896 impr / CTR 10.8% / pos 5.9. Top queries all "assistant surgeon/medical officer previous questions" (CTR 21-50%). Top page /kpsc-medical-officer-previous-year-questions (95 clicks). "dr preetha" pos 21.5 (brand not ranking).
- GA4 28d by channel: Paid Social 1200 sess / avgEng 15s (junk-level); Organic Search 280 sess / 125s; Referral 141 sess / 324s; AI Assistant 79 sess / 121s. Paid Social = 68% of sessions but shortest engagement.
- Meta Pixel 28d (server events): QuizAnswered 10, PageView 8, ViewContent 5, SampleQuizCompleted 1 — server-side pixel under-firing vs browser GA4 (4682 page_view).
- videos.php still "not on Google" (C12 open: needs unique 150-250 word Q&A/transcript per video; currently body ≈ home #videos).

## 2026-11-03 MakeMeFamous — cat34 Layout A + sample-quiz ₹299 bar (Hermes, ~14:30 IST)
- Crawl: 93 sitemap pages + 271 links, 0 internal broken. 55 keralapsc.gov.in links 403'd only due to Range/bot-UA filtering (not IP); all 55 = 200 in neko real navigation (44 PDF, 11 HTML) and from VPS with browser headers.
- Crawlers 200 (GPTBot 429 = host limit). IndexNow api/bing/yandex 200; GSC sitemap resubmitted; GSC Request Indexing for both URLs via neko.
- Blind audit (gemini-4-argon): cat34 51/70, sample-quiz 33/70. Verified true: cat34 H1 is countdown-only (no keyword/date; dynamic so not stale); syllabus shows 5 of 11 modules; kp-app-pay.js render-blocking on both; sample-quiz lang=en, robots lacks max-snippet, old nav with relative index.php# links, no author box, 0 links to /kpsc-cat-34-2026, Qs only in JS array. False: "hardcoded 9 days" (both server-computed).
- GA4 7d: Paid Social 1408 sess/39% eng/46s/74 key events; Organic 232/78%/552s/72; Referral 141/177 key; AI Assistant 65/82%. Signups 7d: 61 (26 paid-tagged). GSC 28d: PYQ hub 94 clicks/579 impr; 'kerala psc assistant surgeon next exam' 13 impr/1 click pos 7.2; 'dr preetha' pos 21.6.
- GSC Request Indexing done for /kpsc-cat-34-2026 and /sample-quiz.php (both already indexed). gsc_req.py waits fixed 8s; GSC slow -> poll for input; JS box() returns [0,0] early, fallback click 766,32.
- 2026-11-03 09:43 UTC MMF fixes shipped (Kiran OK for 1,2,6,7,8; 3–5 held for app safety — fix 3 "render-blocking script" = kp-app-pay.js app payment guard, must stay early): cat34 H1 now "Kerala PSC Assistant Surgeon Exam (Cat. 34/2026): 12 Nov 2026" + days-left pill + bold first sentence with full date; full 11-module table (from `_kpsc-papers.php` syllabus, total 100). sample-quiz: lang en-IN, robots max-snippet:-1/max-image-preview:large, collapsed "Preview the 10 questions with answers" (server-rendered from $sampleQuestions), Dr Preetha author box. Backups `kpsc-cache/rollback/{kpsc-cat-34-2026,sample-quiz}.php.pre-mmffix-20261103`. php -l OK; page-designer verify pass both; 390px eyeball OK; linkcheck 60 ok / 4 external false positives; IndexNow 200. Pending: fixes 4 (nav, needs app-mode hide) and 5 (bar link) after Play review; app-mode emulator check of both pages.
- 2026-11-03 22:05 IST APK→Play switch (Kiran "change all app links to the playstore link"): /app rebuilt (Play how-to v2 video, subscriber-only note, plans CTA); nav "📱 App" on 14 pages, home app strip, features, PYQ hub, llms.txt, features-mail.json → https://play.google.com/apps/testing/com.drpreetha.kpsc. Auto new-subscriber mail kpsc-cron/app-mail.json = campaign 2026-11-03-app-mail-play (app-mail.php gained {{EMAIL}}); test sent uid 66. Rollbacks: kpsc-cache/rollback/*.pre-play-20261103. APK files kept in /downloads.
- 2026-11-03 22:17 IST App mail +video section (/app, howto-video.jpg); features.php #14 'Timed mock test, from Saturday 7 November' (loop images/features/loops/mock-test.mp4), app item → #15, group G 'Mock test and the app'. Rollback features.php.pre-mock-20261103.
- 2026-11-03 22:35 IST Both mails: video section + 3 video-frame screenshot pairs (step1-uninstall/step2-tester-install/step3-open-mock). play-testers rebuilt 27 drafts (reviewer+paypaid drafts removed). app-mail.json redeployed, test to uid66.
- 2026-11-03 23:00 IST Play Console closed-test list "Paid subscribers Nov 2026" audited vs DB: removed 4 expired (lekshmicr07, prsuryanath, theheartbreakkidnitin, msvishnupriya1991) → 29 = all active paid (incl. sanikasanjithdr, kiranvk2011, itsmarket09, mspreethadr); excluded test accts drpreetha.reviewer, itsmarket09+paypaid; Athira uid95 suspended. Rule: tester list = active paid only, no expired. Note: neko-preetha egresses via phone SOCKS 172.17.0.1:1080 — Play Console shows ERR_PROXY when phone tunnel down.
- 2026-11-03 23:09 IST play-testers campaign SENT (Kiran OK): 27/27 from progress@updates, preflight OK, closed test 'Available to selected testers'. Incl. sanikasanjithdr (Sandra swap). Sandra transfer confirmation also sent (Cc sister).

## 2026-11-04 MakeMeFamous — /app + 4 Nov sitewide edits (Hermes, ~17:45 IST)
- Changed on server (last 24h): app.php 03:07, features.php 03:47, sitewide header/footer batch 03:34 (index, PYQ hub, sample-quiz, videos, legal pages, upsc-sample, kpsc-practice, llms.txt), WDGW pages 04:12.
- Crawler files current: sitemap 91 URLs (/app lastmod 11-03), llms.txt has /app (Play testing link, mock test 7 Nov), robots unchanged. WDGW = noindex (intended, not in sitemap).
- Crawlers: all UAs 200 on /app, /, features, PYQ hub; GPTBot 429 (shared-host limit, known). All 16 pages end </html>.
- /app: 1 H1, MobileApplication+VideoObject+FAQPage+Breadcrumb JSON-LD, links to /features.php#app. Gaps: no dateModified, no robots meta max-snippet.
- IndexNow 16 URLs: indexnow.org 200, bing 200, yandex 202. GSC sitemap resubmitted. URL Inspection: /app, /, features, PYQ hub, sample-quiz all indexed. gsc_req.py failed (neko tab id stale) — not needed, all already indexed.
- GSC 28d: 238 clicks / 2036 impr / CTR 11.7% / pos 5.9 (up from 204/1896). PYQ hub 118 clicks; /app 2 impr.
- Signups 7d: 17 untagged; chatgpt.com referrals now landing on PYQ hub (2).
- 2026-11-04 Meta: A2 ₹540/day; A3 warm ON ₹150/day with mock-7-Nov subscribers reel (ad 120250337772620716), no price shown.

## 2026-11-04 /app SEO tidy + new share banner (Hermes, ~13:45 IST)
- app.php: robots meta `max-snippet:-1, max-image-preview:large, max-video-preview:-1`; MobileApplication JSON-LD += dateModified (PHP filemtime, auto) + image; og:title/description now say Google Play + 7 Nov mock test.
- New share banner /images/app/psc-app-og-play.png (1200x630, logo app-512 + mock-test screen, "Now on Google Play"); old psc-app-og.png kept. Source app-banner/psc-app-og-play.html (headless chromium).
- FIXED pre-existing bug: FAQPage JSON-LD was invalid JSON (raw <a href="..."> in iPhone answer) → Google ignored the whole FAQ. Now all 3 JSON-LD blocks parse.
- Deploy md5 verified (app.php 0b98c7b3…, png 9f217a9f…). Rollback kpsc-cache/rollback/app-og-20261104-081402. page-designer verify pass, eyeballed full page. IndexNow 200.

## 2026-11-04 WDGW nightly failure (3 Nov 00:15 IST run) — fixed
- Cause: rsql.py upload to cPanel Fileman timed out (curl exit 28) during pull(); no retry, so the whole nightly died. cPanel answers fine now (1.2 s) → transient host slowness at midnight.
- Fix rsql.py (shared by many jobs): 4 tries w/ backoff 15/30/45 s, --connect-timeout 20, -m 90, error text never includes the auth header.
- Fix wdgw_batch.py: whole run retried once after 5 min; failure messages redact `cpanel <token>` (the Telegram alert had leaked the full cPanel API token).
- DRY run OK: 62 candidates, +5 queued, no release due (batch 2 of 6 live). Next real run tonight 00:15 IST.
- TODO (Kiran OK): rotate the cPanel API token — it was posted in the Telegram thread.
- 2026-11-04 later: retry recording. rsql.RETRIES logs every retry (rsql-upload ×4, new rsql-exec ×3 on the GET step); cp_up (traps/batches publish) now 4 tries + md5 check each; whole-run retry recorded. Nightly Telegram summary ends with "retries N: …"; failure alert includes them. Every run appends one line to where-doctors-go-wrong/batch/state/retries.jsonl (status ok/failed + retries) → measure real rate. Forced-failure test: 4 rsql-upload retries recorded, curl 28. DRY run: "retries 0", jsonl written. Kiran: no key rotation (Telegram is private).

- 2026-11-04: Play closed test email list "Paid subscribers Nov 2026": + vineethvinayanofficial@gmail.com (new subscriber) → 30, verified after reload. Pitfall: Save changes opens a 2nd "Save changes to email list?" confirm — must click its Save too.
- 2026-11-05 IST Play tester list "Paid subscribers Nov 2026" 31→34: added abhilash.archana, parukrpz, abhiramimr1995 (gauthu038 already on). Verified after reload. Note harithak.k6@gmail.com on list but no active paid plan in DB. Pitfall: email-list ess-table renders only after scrollIntoView; add emails via CDP focus + Input.insertText + keyDown Enter with text '\r' (one per entry).
- 2026-11-05 IST Removed harithak.k6@gmail.com (uid 54, plan expired 2026-11-04) from Play list → 33 = active paid only (Kiran: only paid users). Verified after reload.
- 2026-11-05 IST Campaign 2026-11-05-new-testers (from 2026-11-03-play-testers, hold=true): 4 drafts in progress@updates Drafts (uids 393-396) for gauthu038, abhilash.archana, parukrpz, abhiramimr1995; pixel + no placeholders verified. NOT sent. Note: automatic app-mail already went to 161/162/163 today before list add; uid 155 (Gautham) never got app mail.
- 2026-11-05 IST SENT campaign 2026-11-05-new-testers to 4 (abhiramimr1995, parukrpz, abhilash.archana, gauthu038) on Kiran's OK; open pixel (mo.php) in each. 0 drafts left.
- 2026-11-05 IST Win-back campaign 2026-11-05-winback (hold): 5 drafts (uids 402-406) to lapsed paid users 8,14,22,46,54 in progress@updates Drafts; pixel + custom 'plan ended' footer via drpreetha/winback/winback.py (render override; stock footer says 'active until'). Review copy mailed to kiranvk2011. NOT sent.
- 2026-11-05 IST SENT win-back 2026-11-05-winback to 2 (msvishnupriya1991, harithak.k6) on Kiran's OK; drafts for lekshmicr07, prsuryanath, theheartbreakkidnitin deleted (Kiran: skip). Pixel in each. Sent via winback/send.py (allow-list over stock active-plan preflight). Promise: renewers added to Play tester list same day.
- 2026-11-05 18:19 IST Added msvishnupriya1991 (uid 46, renewed) + drtamjeedahmed (uid 153) to Play list 'Paid subscribers Nov 2026' → 35 (verified after reload); SENT 2026-11-05-new-testers to both (progress@updates, pixel).
- 2026-11-05 19:18 IST Added dr.rohithsj (uid 167) to Play list → 36 (verified after reload); SENT 2026-11-05-new-testers to him.
- 2026-11-05 IST app-bridge.php identity hardening LIVE: match by Cognito sub (users.google_id) first; email match with different sub → 403 account_mismatch + tah auth.sub_mismatch + alert mail to mail@; exempt test uids 148/149. Pre-check: 118/118 real users' google_id == Cognito sub. Rollback kpsc-cache/rollback/bridge-sub-20261105-172600. Tests: signed bridge A ok/B mismatch 403/C exempt ok/D no_account/E sub-first ok; neko PKCE E2E (uid 85) → Worker /v1/me 200 + /v1/practice 200 (serve item deleted). Script native-app/e2e_sub.py (Fetch.enable intercepts localhost redirect). Rule: account moves must update users.google_id in the same step.
- 2026-11-05 23:38 IST Added drspv@outlook.com (uid 168, Sanu Prasad) to Play list → 37. Non-Gmail: works only if that address is a Google account. No mail sent (not asked).
- 2026-11-05 23:39 IST SENT 2026-11-05-new-testers to drspv@outlook.com (uid 168).
- 2026-11-06 IST Play list "Paid subscribers Nov 2026" 37→38: +bharadwajvs24@gmail.com (uid 171, monthly approved 6 Nov→6 Dec, reviewed by mspreethadr). New-tester app mail (campaign 2026-11-05-new-testers, pixel mo.php) sent from progress@updates. Script /root/.hermes/cache/scratch/pt11.py (one-email add+save+verify).
- 2026-11-06 IST per-user notice banner LIVE on kpsc-practice.php (user-notice/: _user_notice.php, notice-track.php, deploy.py). Tables user_notices (active=1 → shown every load until off) + user_notice_events (seen pixel / click redirect), also tah notice.seen/notice.click. Rollback kpsc-cache/rollback/user-notice-20261106-060258. Neko E2E uid 85: shown, persists on reloads, click → logged + 302 Play tester link, still shown after click, OFF → gone. Note: neko phone-size emulation = new device → device-choose.
- 2026-11-06 12:06 IST notice id 2 ON for uid 162 Kripa Parvin (Gmail full 452 4.2.2) — same text as test notice 1, link Play tester. Off: UPDATE user_notices SET active=0,off_at=NOW() WHERE id=2. Watch: user_notice_events notice_id=2.
- 2026-11-06 ~17:45 IST mock-switch banner ON for 22 paid users without play6/native app (18 web-only + 4 on Play v5: 154,167,56,99): 'Mock tests start tomorrow (Sat 7 Nov), in the Android app only' → button /app?src=banner-mock (4-step Play page). Kripa (uid 162) keeps Gmail-full banner + appended mock line. created_by=kiran-mock-switch. Off all: UPDATE user_notices SET active=0,off_at=NOW() WHERE created_by='kiran-mock-switch' AND active=1. iOS users 141/161/163 cannot use Android app — flagged to Kiran. Sanu + Vishnupriya confirmed already on Play list (38).
- 2026-11-07 IST Google Ads (acct 144-267-7143): REMOVED 'KPSC Search - exact (test)' (24433646815; ₹611.77, 94 impr, 18 clicks, 2 free signups, 0 paid) and PMax draft 'Subscription Tracker'. 'Fifty Flash' + 'Campaign #1' remain as unpublished PMax drafts-in-progress (Paused, ₹0 spent); table Edit→Remove doesn't apply to them and Drafts tab is empty. Account budget now ₹0/day. Scripts: scratch/gads.py, gads_rm2.py.
- 2026-11-07 IST Meta (Kiran 'go'): PAUSED ad set M100 ₹100 Mock Pass (120250382056580716, was ₹500/day, ₹352 spent, 0 sales). A2 (120250237764790716) daily_budget ₹690→₹300; only 'features IG' + 'Riya VO feature tour' (cat34-2026) active, landing unchanged (website). Meta now ~₹300/day to 11 Nov end.
- 2026-11-07 11:11 IST (Kiran): WEBSITE PRACTICE CLOSED for normal subscribers -> Android app. app-only/ (deploy.py, src/_app_only.php+.css, design via page-designer :7777 compose). Gate in kpsc-practice.php (page) + next-batch.php (API, non-KP_NATIVE only). Allowed on web: owner + iOS-only accounts on an iPhone/iPad (8 accounts: 95,98,135,141,149(test),161,163,168). Rollback kpsc-cache/rollback/app-only-20261107-054114 (`python3 deploy.py rollback <dir>`). Events tah_events type=practice.refused {why,where}. E2E: uid 85 web desktop+iPhone-UA -> app-only page + API 403 app_only; native app served uid 85 11:22; Soorya (81, Android web) refused. Test acct uid 85 monthly(₹0) extended to 2026-11-12 for testing.
- 2026-11-07 13:18 IST SENT threaded reply 'Re: Regarding app' to Kripa Parvin (uid 162, parukrpz) from mail@drpreetha.com: plan active till 5 Dec, Android practice moved to app, Gmail-account-switch walkthrough with images (mail-assets/reply-kripa-1107/), fresh pixel ref kripa-app-fe3c58a9. Draft deleted, copy in INBOX.Sent.
- 2026-11-07 ~20:45 IST Kripa (uid 162): NONE of our tracked mails were opened by her (opens on the reply tokens = Kiran's reviews only; appmail/welcome/payment 0 opens; Gmail 452 inbox-full). Her banner (notice id 2) IS seen in the app (3× seen, last 20:32 IST). Reply walkthrough converted to private gist https://gist.github.com/kiranvk-2011/d7da48f73d357778a74434c03fd56c59 (copy play-howto/kripa-gist-2026-11-07.md). Notice 2 retitled "Have you made space in your Gmail?" asking her to free space + reply to mail@, link → gist. Off: UPDATE user_notices SET active=0,off_at=NOW() WHERE id=2.
- 2026-11-07 21:00 IST App vs Web stale: since the native app (v7.0.6/play7, via app-bridge.php) took over, record-attempt got no `client` field, so app answers were logged as client='unknown', which the dashboard ignores (today: 12 app users / 363 answers missing). Fix: _client.php kp_req_client() returns 'app' when KP_NATIVE is defined; backfilled 31 'unknown' rows into 'app' (backup table client_daily_bak_20261107). The dashboard #app-vs-web and #kp-banner-panel now refresh every 30 s. Rollbacks kpsc-cache/rollback/client-native-20261107-210023, appvsweb-live-20261107-210037, banner-live-20261107-205250.
- 2026-11-07 IST: app-only subscriber mail 2026-11-07-app-only — 30 drafts in progress@updates Drafts (iOS-only + test excluded), incl. v7 update ask; NOT sent, awaiting Kiran. Takeaways drpreetha/SESSION-TAKEAWAYS-2026-11-07-ADS-CLEANUP-WEB-PRACTICE-APP-ONLY-MAIL.md.
- 2026-11-08 IST MMF run (Hermes, pkd11): crawlers all 200 (GPTBot/Claude/Perplexity/OAI/Google/Bing); 93 sitemap URLs all 200; llms.txt current (5 Nov, covers KPSC+UPSC). IndexNow 94 URLs 200/200 + GSC sitemap resubmitted. URL Inspection: 58 indexed, 17 Discovered-not-indexed, 17 unknown (all UPSC paper pages except /videos.php), /subscribe.php Crawled-not-indexed. GSC 28d: 374 clicks/3328 impr pos 5.7; top /kpsc-medical-officer-previous-year-questions 182/1060. plans.php is noindex (intentional?). No change made.

## 2026-11-09 — Device slots: 2-device plans had 1 usable device on Android
- 5 Nov one-app-slot rule + 7 Nov web practice closed for Android → Monthly users with phone+tablet signed each other out (Arsha uid 99). Fixed: app installs = plan device limit; Android web slots freed (27/25 users). See SESSION-TAKEAWAYS-2026-11-09-ARSHA-2APP-SLOTS-WEBSLOTS.md.

## 2026-11-09 — Weekly report (2–8 Nov vs 26 Oct–1 Nov)
- DB: signups 49 (51), active learners 41 (22), answers 8163 (2454), payments submitted 25 (16) / approved 23 (15), revenue ₹6279 (₹5185); 46 active subs, 8 expiring in 14d, 28 signed up never paid.
- GA4: 1850 users/2304 sessions (1449/1717); Meta paid 1407 sessions; view_item_list 81 users, select_item 38, begin_checkout 38, payment_submitted 20 (35 events); Monthly clicked 86 vs Exam Pass 3, Yearly 1.
- Clarity (7d): 1571 sessions, dead clicks 9.2%, rage 0.06%, quick-backs 8.1%, 147 JS errors (65% "java object is gone" in-app webview); begin_checkout_monthly 27 sessions, payment_submitted 6.
- Meta pixel: PageView 4549 (3534), ViewContent 2605, PaymentPending 20 (46); no AddToCart/InitiateCheckout/Purchase events firing.
- Biggest drop: visitors → saw plans (4%); GA4 cleaned via Data API (browser not needed); Clarity prev-7 unavailable.
- 2026-11-10 20:36 IST SENT threaded reply to Haritha K (uid 54 harithak.k6; wrote from husband's veeveedoctor = empty uid 100) To veeveedoctor Cc harithak.k6: plan active till 10 Dec, account-switch walkthrough (mail-assets/reply-haritha-1110/, mockups w/ her emails), fresh reply pixel. Build: scratch/har/build.py+send.py.
- 2026-11-10 22:00 IST 'Trusted by doctors' Riya EN reel LIVE on IG https://www.instagram.com/drpreetha.ms/reel/DfkVMVdErDb/ (IG only). Meta final-burst ad set 120250445397370716 (lifetime ₹2,500, ends 11 Nov 23:00 IST, FB+IG+WA Status, LPV, A2 targeting) ad 120250445402130716 ACTIVE -> drpreetha.com/plans utm_content=trusted-riya. Price ₹299 shown by Kiran's explicit OK. Files instagram/trusted-1111/.
- 2026-11-12 IST (pkd11): next-batch.php AB_NEW_PER_DAY back to 150 now (exam-week 300 lift ended a day early). Rollback kpsc-cache/rollback/next-batch.php.pre-newcap150-20261112-165249. md5 3838bd08→f1c89c73.
- 2026-11-13: Hub webmail tiles (mail-go, mail-go-updates) 502 'Could not open webmail' — ~/webmail-sso/config*.php held a revoked cPanel API token (403 Access denied). Swapped in current token from /root/.secrets/drpreetha/cpanel_auth; backups *.pre-tokenfix-*. Rule: on cPanel token rotation, also update ~/webmail-sso/config*.php.
- 2026-11-13 UPSC subscribe chooser live (national/upsc-subscribe-flow-2026-11-13). Rollback tag pre-upscsub-20261113120352.
- 2026-11-13 evening IST (pkd11): 8.0.3 build 26 (UPSC in app) published on Play ~17:35 IST, Worker MIN_VC=26 (24/25 -> 426, rollback setminvc.py 24). Rekha uid 85 mirrors Nishanth (Rs 0 test UPSC row). Phone SOCKS tunnel :1080 can listen yet be dead: test the handshake. See HANDOVER-2026-11-13-UPSC-APP-803-PLAY-GATE.md
- 2026-11-13 ~20:10 IST (pkd11): App Home cleanup: sv-banner ("How was today's exam?") and fb-testi-1 ("Share your feedback · unlocks Mock Tests 5 to 8") expired (until 19:55 IST), mocks[5].banner "Give feedback to unlock Mock Tests 5 to 8" removed. homecards backup 20261113-143654 (rollback: homecards.py rollback 20261113-143654). New card fb-help-1 (image, aud fb_none, /feedback, https://drpreetha.com/dl/feedback-help-banner.jpg, panel PASS 7.5) STAGED in scratch home-new.json, awaiting pkd11 artwork OK. Nishanth (uid 63) UPSC Doctor/MO Yearly approved (sid 173, to 13 Nov 2027); "UPSC live in app" reply drafted in mail@ INBOX.Drafts, test copy Primary + DKIM/SPF/DMARC pass, legibility OK at 390px; app screenshots' Rekha watermark faded to unreadable.

## 2026-11-13 22:20 IST — Make Me Famous after UPSC subscribe flow (pkd11)
- /upsc-subscribe added to sitemap.php + llms.txt; canonical/og/breadcrumb → bare slug; .php 301 → bare; subscribe.php?bank=upsc 301 → /upsc-subscribe; nav + /upsc-medical + plans.php "Change exam" link to bare slug.
- /upsc-subscribe: answer-first lead, card titles h2, full UPSC price table + All-Access ₹2,499, CollectionPage+ItemList(11 Offers)+dateModified IST JSON-LD. 390px visual QA passed.
- /upsc-medical: visible "last checked" = dateModified (IST timestamp); FAQ cost links to /upsc-subscribe. llms.txt CMS range 2021→2016–2026. subscribe.php Product offer url → subscribe.php.
- Submitted: IndexNow (Bing 200, Yandex 200), GSC sitemap resubmit (0 err), Brave 6/6.
- OPEN: site-wide Course JSON-LD (include) still offers url plans.php (noindex); growth list in session (CMS 2026 answer-key titles, /kerala-psc-medical-officer CTR 3.6%, Cat 034 post-exam, exam-calendar page).
- Rollback: national/mmf-2026-11-13/bk/*.pre (upload over live).
- 22:40 IST: duplicate #kpsc-course Course JSON-LD suppressed on subscribe.php + plans.php (FB_LD_DONE); Course offers url → subscribe.php site-wide (still on home/PYQ/quiz with reviews). /kerala-psc-medical-officer title+meta → post-exam (Cat. 034/2026 answer key, rank list, previous papers); IndexNow 200. CMS 2026 paper pages already had "Answer Key & PDF" titles + FAQ — no cut-off claims added (no source). Rollback: bk/*.pre2, bk/kerala-psc-medical-officer.php.pre.
- 2026-11-16 IST (pkd11): Replied to Dr Arun M.V (uid 202, free, arunmvnta@gmail.com) on DBMCI+Marrow vs KPSC prep, in his thread (In-Reply-To his Message-ID). Council-backed; '913 questions and counting'. Pixel ref arun-2026-11-16-send-*. Files drpreetha/support/2026-11-16-arun-dbmci-marrow/.

## 2026-11-16 — Weekly report (9–15 Nov vs 2–8 Nov)
- DB: signups 15 (49), active learners 36 (40), answers 13093 (8067, exam-week), payments submitted 12 (24) / approved 12 (23), revenue ₹4240 (₹6279): Monthly 9, UPSC Doctor Yearly 1 real + 1 ₹0 test, mock_early 1; 51 active subs, 12 expiring in 14d, 8 signed-up-never-paid, 0 pending.
- GA4 (Data API): 705 users/960 sessions (1855/2306); Organic 386, Meta paid 324 (1407, burst ended 11 Nov), Direct 93, ChatGPT 69, accounts.google 70. /plans top page 408 views/287 users. Funnel users: view_item_list 292 → select_item 17 → begin_checkout 17 → payment_submitted 10 (19 events). Clicks: Monthly 21, Exam Pass 2, Yearly 0, UPSC Doctor Yearly 4.
- Clarity 7d: 740 sessions (1571), dead clicks 11.5% (85 s), rage 0.54%, quick-backs 14%, 26 JS errors (73% in-app "java object is gone"); begin_checkout_monthly 6, exam_pass 1, yearly 1, payment_submitted 3 sessions. Prev-7 unavailable.
- Meta pixel (Graph stats): PageView 2052 (4549), ViewContent 778 (2605), PaymentPending 11 (20); AddToCart/InitiateCheckout/Purchase still not firing.
- Biggest drop: saw plans → clicked a plan (292 → 17, 94%); ad landed cold traffic on /plans. All sources OK; no browser tab left open (6 → 6).
- 2026-11-17 14:57 IST Reply SENT to Gautham (uid 155, gauthu038) on pkd11's OK: Cat 034/2026 provisional key not yet on keralapsc.gov.in (checked neko 17 Nov; ONLINE exam) + promise to upload provisional key in app + /kpsc-cat-34-2026; UPSC Doctor plans guide (plans.php?bank=upsc&cat=doctor, 3 plans, UTR form steps, app 8.0.3). Images mail-assets/reply-gautham-upsc-034-2026-11-17/. Pixel reply|reply-gautham-upsc-034-2026-11-17-send-efec8d. TODO: upload 034/2026 provisional key in app when KPSC publishes.

## 2026-11-18 — Make Me Famous after /kpsc-medical-education-jobs (subagent for pkd11)
- Changed today (live mtimes): kpsc-medical-education-jobs.php (new), kerala-psc-medical-officer.php (link card), upsc-medical-news.php (author line), sitemap.php. app-bridge.php/keycheck.php are non-pages.
- Crawler access: 12 UAs (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Googlebot, Google-Extended, bingbot, meta-externalagent) x 4 pages = all 200; robots/llms/sitemap/IndexNow key/css 200.
- Defects fixed on /kpsc-medical-education-jobs: (1) .php served 200 with no redirect -> in-script 301 to bare slug (query string kept; verified `?utm_source=mail` 301); (2) missing from llms.txt -> entry added; (3) lead claimed "every open" notification and "4 categories" while the news hub lists Cat 166 and 167 open too -> wording softened + pointer to news page (no unsourced PDF data added); (4) author line lacked Azeezia Health City -> added; (5) date format mixed -> unified "18 Nov 2026"; (6) title/H1 used only "KPSC" while demand is "kerala psc" -> "Kerala PSC Medical Education Assistant Professor jobs 2026".
- Open: add Cat 166/167 (+165?) cards after reading their PDFs; JobPosting JSON-LD (blind audit suggested; needs datePosted/validThrough sourced); hub anchor links from news items to /kpsc-medical-education-jobs#cat-NNN; page not yet in GA4 (new).
- Submitted: IndexNow api.indexnow.org 200, Bing 200, Yandex 202 success; GSC sitemap resubmit 0 errors; Brave 3/3.
- Rollback: kpsc-cache/rollback/kpsc-medical-education-jobs.php.pre-mmf-kmej-20261118-062208, llms.txt.pre-mmf-kmej-20261118-062210. Work files: drpreetha/makemefamous/kmej-2026-11-18/.
- Signals (7d to 17 Nov vs prior 7): GA4 760 sessions/636 users (1925/1678); Organic 359, Paid Social 230, AI Assistant 66. GSC 28d to 16 Nov: 725 clicks/7394 impr, pos 5.8; /kerala-psc-medical-officer CTR 3.7% on 2090 impr. DB 7d: signups 11 (33), payments approved 6 (19), revenue Rs 2695 (5432), 51 active subs, 21 expiring in 14d. Pixel 7d: PageView 1413, PaymentPending 6. Clarity/ads not pulled this run.
