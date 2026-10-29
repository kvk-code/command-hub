# drpreetha.com — 29 Oct 2026: ads ROI, signup attribution, stop rule, Athani in Google

## 1. Ads ROI (live DB + Meta API, not the dashboard total)
- Meta spend so far ₹749 (only 25–29 Oct; 26 Oct ₹328, 27 Oct ₹139, 28 Oct ₹0 card-pending, 29 Oct ₹281 partial). 12.1k impr, 440 clicks, 225 LPV, 2 PaymentPending pixel conversions.
- Approved payments since Dr Soumya's first (15 Sep), excl. kiranvk2011 test: 10 payments / 9 people / ₹3,690.
  - Pre-ads 15 Sep–25 Oct: 8 × ₹299 = ₹2,392 (organic/word of mouth/mail).
  - During ads: uid 74 (Kozhikode) signup+₹999 Exam Pass 26 Oct; uid 80 (Kollam) ₹299 28 Oct → ₹1,298.
- Verdict: plausibly paid back (the ₹999 alone > spend), but NOT provable — users table had no source column. Full run to 11 Nov ≈ ₹4.5k → needs ~5 more attributed payers.

## 2. E4 first-touch attribution (LIVE)
- `_attrib.php` (required at end of `config.php`) sets 90-day HttpOnly cookie `kp_src` = JSON {utm_*, fbclid/gclid (truncated), ref host, land path, t} on first external/UTM visit.
- `db_config.php::createUser()` writes it to new column `users.signup_src` (VARCHAR 600).
- Verified: ad URL sets cookie; home/upsc-sample/plans still 200; php -l clean. Not yet seen on a real signup.
- Rollback: `/home/revirnmt/kpsc-cache/rollback/attrib-20261029-191526/` (config.php, db_config.php).
- Ads land on `sample-quiz.php?utm_source=meta&utm_medium=paid&utm_campaign=cat34-2026&utm_content=features|igwa`.

## 3. E3 stop rule (LIVE)
- Hermes no-agent cron `680d43ffc2fc`, `0 */3 * * *`, script `/root/.hermes/scripts/drpreetha-ads-stoprule.py`.
- Spend counted from 29 Oct 19:15 IST (subtracts ₹281.01 pre-tracking same-day spend). If ≥ ₹1,000 and ₹/meta-signup > ₹150 → POST status=PAUSED on ad set A2 `120250237764790716` and alert to origin topic; silent otherwise. Pause path untested.

## 4. "Athani Hospital" still in Google
- Site audit: all 84 sitemap URLs + robots/llms/llms-full/sitemap.xml fetched as Googlebot. Current-employer = Azeezia everywhere (title, meta, OG, JSON-LD worksFor). Athani only as "May–Oct 2026" history; Parabrahma only as video recording place. Site is NOT the cause.
- Found + fixed: public docroot folder `backups/pre-azeezia-20261024/` (llms.txt with old Athani text was 200) → moved to `kpsc-cache/rollback/docroot-backups-pre-azeezia-20261024/`, now 404. Other `*.bak-*`/`*.pre-*` copies return 403 (SEC-4 .htaccess).
- External causes: Google's stale snippet of home page; Azeezia profile lists "Athani Hospital" with no end date; athani.hospital/doctors-2 still lists her; LinkedIn still shows Parabrahma.
- GSC (URL-prefix property https://drpreetha.com/, kiranvk2011 = authuser 1, neko-preetha): Request indexing ACCEPTED for `/` (last crawl 28 Oct 22:57 IST), `/videos.php` (was never indexed — "discovered via sitemap"), `/llms.txt`.
- Open: ask Azeezia to add "(May–Oct 2026)" to Athani line; ask Athani to remove her; update LinkedIn; thumbs-down feedback on the AI answer.

## 5. Clean videos live
- Homepage + videos.php swapped to dp-*-clean.mp4 (no Parabrahma logo/phone/name/spoken mention); note sentence removed. Rollback kpsc-cache/rollback/cleanvids-20261029-203506.

## 6. Instagram links on video cards
- Vertigo card → instagram.com/reel/De-8ynmj2AX/ (was Parabrahma FB). Adenoid + migraine Parabrahma YouTube links removed; IG links auto-added by one-shot crons 05ffa3e79a6e (30 Oct 11:00 IST) and 7d9280520d9e (2 Nov 11:00 IST) after the scheduled reels go live. Rollback kpsc-cache/rollback/igvertigo-*.
- Graph API IG media read fails (#10 no permission) — use the neko browser on the profile.

## Pitfalls
- GSC in neko-preetha renders mobile layout: the inspect bar is the search icon at (135,28); `/search-console/inspect?...&id=<url>` deep links 404 — use the bar. "REQUEST INDEXING" click must target the SPAN element's rect (fixed coords hit a sign-in link once).
- `rsql.py` import needs `PYTHONPATH=drpreetha/weekly-insights` when run from a scratch script.
- Security: `db_config.php` holds DB password in plaintext — rotation still pending Kiran.
