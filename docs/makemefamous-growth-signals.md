# MakeMeFamous — Growth-signals phase (ads, pixels, analytics)

Run AFTER reindexing. Output = a short "what to do next for traffic/sales" suggestion list,
backed by numbers, appended to the site's findings log. Skip any source the site doesn't have.

## Applicability matrix
| Source | kiranvk.me | drpreetha.com |
|---|---|---|
| Google Search Console | yes (API token) | yes (URL-prefix `https://drpreetha.com/`, kiranvk2011; API token below) |
| Google Analytics 4 | check tag | yes `G-RW72H5NZ2R`, property a376088366p514377314 (authuser=1 kiranvk2011) |
| Meta Pixel | n/a | yes `919839944003926` (Events Manager, act 1209421041068162, mspreethadr FB login) |
| Microsoft Clarity | n/a unless tag found | yes `uc0cq7dhg9` (login pomi.04092110@outlook.in, MS Authenticator) |
| Google Ads | n/a | account KPSC Practice 144-267-7143 (kiranvk2011) — PMax paused |
| Facebook Ads | n/a | Ads Manager act 1209421041068162 |
| DB signups/payments | n/a | cPanel revirnmt MySQL (truth for revenue) |

Detect what's installed first: fetch homepage + one app page, grep `G-`, `fbq('init'`, `clarity`, `bat.bing`.

## How to pull (drpreetha: browser = neko-preetha, CDP 172.17.0.1:9225, helper /root/.hermes/cache/scratch/cdp.py)
- GSC: API first (`/root/brain/credentials/gsc-kiranvk2011-tokens.json`, `searchanalytics().query` dims query/page, 28d + 16mo). UI fallback: `search.google.com/u/1/search-console/performance/search-analytics?resource_id=https%3A%2F%2Fdrpreetha.com%2F&num_of_months=16`. Domain property `sc-domain:` is NOT accessible.
- GA4: `analytics.google.com/analytics/web/?authuser=1#/a376088366p514377314/reports/explorer?params=_u..nav%3Dmaui%26_u.date00%3DYYYYMMDD%26_u.date01%3DYYYYMMDD&r=lifecycle-user-acquisition` (+ `lifecycle-traffic-acquisition-v2`, `all-pages-and-screens`). Read users, avg engagement, key events by first-user source.
- Meta Pixel: `business.facebook.com/events_manager2/list/pixel/919839944003926/overview` → event counts (funnel).
- Clarity: `clarity.microsoft.com/projects/view/uc0cq7dhg9/dashboard?date=Last%2030%20days` → sessions, referrers (catches Reddit/app referrers GA4 misses), dead clicks, quick-backs, JS errors, LCP, top pages.
- Ads: Google Ads billing summary + campaigns; FB Ads Manager campaigns (spend, results). Note if anything is RUNNING.
- Logins expire: never type passwords; ask Kiran to complete auth in the neko.

## Analysis → suggestions (rules of thumb)
- Cost per useful action per channel (spend / key events). Kill channels > 10× the best one. Never Performance Max/Display for this niche (2025: ₹11.4k, 3-s visits).
- Engagement < 10 s from a paid source = junk traffic.
- Pixel funnel: biggest step drop = next fix (e.g. quiz answers → completes).
- Clarity dead clicks > 10% or JS error > 5% sessions = UX bug to fix this run.
- GSC: queries with impressions but 0 clicks → title/meta rewrite; queries outside current pages → new page.
- New referrers (reddit, chatgpt, gmail app) → seed/answer there, add UTM links (drpreetha/UTM-LINKS.md).
- Exam-cycle timing (KPSC dates) → time ads/emails 6 weeks before exam.

## Output
1. 5–8 bullet "Suggestions to grow traffic/sales", each with the number that justifies it.
2. Append dated section to the site's findings log (drpreetha: `/root/openclaw_master/drpreetha/FINDINGS-LOG.md`), tick/add items in `MASTER-CHECKLIST.md`, then `bash /root/openclaw_master/drpreetha/sync.sh "msg"` (openclaw_master + gbrain + command-hub).
