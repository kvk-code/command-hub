# KPSC news — daily card workflow (state 2026-10-23)

Page: https://drpreetha.com/kerala-psc-medical-officer (live PHP `kerala-psc-medical-officer.php`, copy in `../tracker-live/`).

## Pipeline
1. Cron (root crontab) `45 17 * * *` UTC = **23:15 IST**: `flock /run/kpsc-news.lock python3 -I /root/kpsc-tracker/scripts/news_scan.py` → log `/var/log/hermes-cron/kpsc-news.log`.
   - Deployed script = `/root/kpsc-tracker/scripts/news_scan.py`; repo copy = `drpreetha/kpsc-tracker-scripts/news_scan.py`. **Keep them byte-identical** (`cmp`). Edit repo copy → `cp` → `py_compile` → DRY run.
2. Scans keralapsc.gov.in (notifications, exam programmes, ranked lists, shortlists), downloads each PDF and verifies cat/post/dates in it.
3. Local state `/root/kpsc-tracker/news/items.json` (all items, statuses). Uploads ONLY `status == verified` to site `/home/revirnmt/kpsc-cache/news/items.json` (cPanel Fileman, auth `/root/.secrets/drpreetha/cpanel_auth`).
4. Telegram cards (Hermes Forum `-1004448683936` topic 14266) with HMAC Publish/Reject links → `news-approve.php` → writes site `decisions.json` `{id: {a: publish|reject, ts}}`.
5. Page shows items that are in site items.json AND `a == publish`.

## Auto-filter rules (all in the per-item loop, before cards)
| Rule | status / check | Effect |
|---|---|---|
| Notification, last date to apply passed | `expired` / `last_date_passed` | no card; hidden on site even if published |
| Exam date passed (IST) | `expired` / `exam_date_passed` | no card; hidden on site (added 23 Oct) |
| Shortlist whose cat has a ranked list (scan or where-am-i `lists.json`) | `superseded` / `ranked_list_exists` | no card; hidden on site (added 23 Oct) |
| Ranked list already in where-am-i tracker | `dropped` / `already_tracked` | no card |
| Same kind+cat already decided (other PDF) | card header ⚠️ UPDATE / ↩️ REPEAT | |
| Ranked list whose cat's shortlist was published | card header 🔁 REPLACES | publish to keep the post visible |

Env: `DRY=1` (no upload/cards), `RESEND=1` (re-card undecided verified), `CAP=N` (max cards, default 10).

## Counting rule (lesson 22–23 Oct)
Report "published on site" from the **live page** (`grep -c 'class="nw-item"'`) — never from decisions.json, which can hold ids that are expired/superseded/not uploaded. Keep decisions.json pruned of ids no longer in site items.json; when a published shortlist is superseded, publish its ranked list instead (done for 683/684/685/686).

## State 2026-10-23
Site: 20 items published = 20 decisions, 0 pending. Local: 157 items (old 119, verified 20, superseded 8, expired 8, dropped 2).
Backups: `/root/kpsc-tracker/news/items.pre-*.json`, `/root/.hermes/cache/scratch/decisions.bak-*.json`, script `news_scan.py.bak-20261023`.
Commits: 5c839f5 (supersede), 15b3ebe (exam expiry), + this doc / REPLACES header.

## Publish-all + search-engine pings (added 2026-10-23)
- After the cards, the scan sends one summary message with a **✅ Publish all N** button (HMAC-signed over the id list, action `publishall`). Already-decided items are skipped, never overwritten. Individual cards still work; undo per item from its own card.
- Every publish (single or all) pings **IndexNow** from `news-approve.php` for `/kerala-psc-medical-officer` + `/where-am-i`.
- `kpsc-tracker-scripts/news_ping.py`, VPS cron hourly at :07: if live `decisions.json` changed, IndexNow + **GSC sitemap resubmit** (`https://drpreetha.com/sitemap.php`, token `/root/brain/credentials/gsc-kiranvk2011-tokens.json`). `FORCE=1` to ping now. Log `/var/log/hermes-cron/kpsc-news-ping.log`.
- Full make-me-famous is weekly, not per publish.
- Rollback: `kpsc-cache/rollback/news-approve.pre-publishall-20261023.php`.
