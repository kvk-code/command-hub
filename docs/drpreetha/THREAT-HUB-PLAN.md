# drpreetha.com — Threat Analysis Hub (TAH): build plan

Status: PLAN v1 (2026-11-04). Owner: Kiran. Builder: Hermes.
Resume line for a new context: "Load drpreetha context, then read docs/drpreetha/THREAT-HUB-PLAN.md in kvk-code/command-hub and continue at the first unchecked phase."

## 0. Goal
One central system that takes every signal from **the website (PHP)** and **the app (TWA now, native Flutter/React Native later)**, builds a profile per subscriber, compares it with normal subscribers, and uses AI to triage. Actions above "flag" always wait for Kiran's OK until the system has a proven track record.

Business model it protects: **users pay on the website → get an entitlement → the app checks the entitlement.** The app never takes payments, and it never decides on its own whether someone has paid.

## 1. Current signals (inventory, build on these, don't duplicate them)
| Source | Where today | What |
|---|---|---|
| Practice answers | MySQL `user_question_attempts` (cPanel) | qid, chosen, correct, time |
| Question serves | `question_serves` | anti-oracle check (SEC-1) |
| Bank progress + misuse flags | admin panel "📚 Question bank progress" (`drpreetha/admin-bank-progress/`) | % of 913 answered, fast/burst/guess |
| WDGW AI tutor | `kpsc-cache/wdgw/ask.sqlite` (asks, refusals, `tt` pick/dwell ms, credits ledger) | AI use, off-topic, time on card |
| App build | `user_app_build` via `/app-build.php` (kp-app-pay.js v13) | last build, play5/old |
| Device slots | users/devices tables + `isOwnerUser` exemptions | device count, slot changes |
| Attribution | `users.signup_src` (kp_src cookie) | first touch |
| Payments | payments table + screenshots (`admin/payment-shot.php`) | plan, amount, approval |
| Mail | tracking pixels (send/open per address) | engagement |
| Prompt guard | Fleet GW key `drpreetha-wdgw` guard log | jailbreak/abuse asks |
| Matomo | VPS Matomo (site id for drpreetha) | visits, sources, campaigns, /app, APK downloads |
| GA4 / Clarity / Meta Pixel | external | funnel only, not per-user security |

Gap: these live in 5+ stores with different user keys → no single timeline per user.

## 2. Architecture
```
 Website PHP (cPanel)         TWA app (= website)       Native app (later)
        │ emit()                     │ emit()                   │ POST /v1/events (batched)
        ▼                            ▼                          ▼
   ┌───────────────── Ingest API (VPS, HTTPS, HMAC-signed) ─────────────────┐
   │  tah.revisemachine.com/ingest  (Caddy → FastAPI)                      │
   └───────────────┬───────────────────────────────────────────────────────┘
                   ▼
        PostgreSQL `tah` (VPS)  ── events (raw, append-only, partitioned by month)
                   │            ── users_map (uid ↔ device keys ↔ emails)
                   │            ── features_daily, scores, cases, verdicts, rules
                   ├── nightly: feature builder (Python) → PyOD scores → rules
                   ├── hourly: hot rules (device sharing, impossible travel, burst)
                   ├── AI triage: Qwen (proposer, night window) → Sonnet (judge)
                   ├── optional mirror → tirreno (sessions/IP/device UI)
                   └── outputs: admin "Risk" panel, Telegram digest, draft mails
 Matomo (VPS) ── nightly pull via Reporting API, joined on uid/visitorId
```
Why the VPS and not cPanel: cPanel = shared PHP/MySQL and can't run Postgres/Python jobs. The VPS already hosts Matomo, kpsc-tracker and the Fleet GW. The site pushes events out, so it never depends on the VPS being up (fire-and-forget, with a local spool if delivery fails).

## 3. Event schema (one format for every source)
```json
{
  "v": 1,
  "id": "uuid-v7",            // dedupe key
  "ts": "2026-11-04T13:05:22.481Z",
  "src": "web|twa|android|ios|server|matomo",
  "uid": 123,                 // null if signed out
  "sid": "session id",
  "dev": "device key (native: Keystore id; web: kp_dev cookie hash)",
  "ip": "x.x.x.x", "ua": "…", "build": "play5|web|native-1.0.0",
  "type": "auth.login|practice.answer|wdgw.ask|pay.submit|…",
  "props": { … type-specific … }
}
```
Core types (v1):
- `auth.login`, `auth.logout`, `auth.fail`, `device.slot_add`, `device.slot_remove`, `device.limit_hit`
- `practice.session_start/end`, `practice.serve` {qid,bank}, `practice.answer` {qid, choice, correct, ms_to_answer, position}
- `wdgw.ask` {chars, refused, guard_score, credits_after}, `wdgw.card` {pick_ms, dwell_ms}
- `pay.submit`, `pay.approved`, `pay.rejected`, `entitlement.change`
- `app.launch` {build}, `app.integrity` {verdict…} (native), `app.screenshot_attempt` (native)
- `mail.open`, `page.view` (signed-in only), `matomo.visit` (nightly import)
- `admin.action` (hold, unhold, message): the audit trail

Privacy: no answer text, no chat text in `events` (chat stays in ask.sqlite and is linked by id). IPs are kept 180 days, then truncated to /24. Never put roll numbers or reg nos in events.

## 4. Detection layers
1. **Rules** (SQL/Python, versioned in `rules/`, each with a test fixture):
   - R1 device sharing: same `dev` on ≥2 uids
   - R2 too many devices: >N distinct devs in 30 days
   - R3 impossible travel / concurrent sessions in 2 cities
   - R4 fast-guess: ≥40% answers <3 s with accuracy within 10 pts of random (the Athira pattern)
   - R5 position bias: one option chosen >60% over ≥50 answers
   - R6 bank harvesting: serves ≫ answers, or sequential qid sweep at bot pace
   - R7 AI-tutor abuse: guard flags, off-topic ratio, credit burn rate
   - R8 paired accounts: two uids answering the same qids within ±2 min, repeatedly
   - R9 payment: reused screenshot hash, same UTR on two uids
   - R10 old/tampered build, or (native) integrity fail
2. **Statistical** (nightly): ~30 features per user per day → PyOD (IForest + ECOD ensemble) against the cohort of paying users; score 0–1.
3. **AI triage** (only top-K, max ~10/day): Qwen proposes {verdict: benign/watch/misuse, evidence[], action}; Sonnet judges and confirms or overturns. Both are recorded with the prompt version.
4. **Drift** (weekly): feature-distribution shift + new clusters → "possible new pattern" note to Kiran; once confirmed it becomes a new rule plus a fixture.
5. **Feedback**: Kiran's decisions → `verdicts.label` → threshold tuning and a replay check (false-positive rate per rule).

## 5. Actions (risk ladder)
| Level | Trigger | Action | Needs Kiran? |
|---|---|---|---|
| 0 | none | — | — |
| 1 watch | score > p95 or 1 soft rule | Risk panel row | no |
| 2 soft | 2+ rules or AI "watch" | throttle WDGW credits, force re-login, device re-verify | no (auto, reversible, logged) |
| 3 hold | AI "misuse" + judge agrees | **draft** hold mail (house template + pixel) + Telegram card | **yes** |
| 4 block | Kiran OK | suspend entitlement (existing suspended redirect) | yes |
Auto level 3+ only after a sustained precision of ≥90% on labelled cases.

## 6. Phases (deploy order)
- [ ] **P0 Setup**: Postgres db `tah`, FastAPI ingest on VPS (systemd), Caddy host + HMAC key in cred-broker, Hub tile. Rollback = stop the unit.
- [ ] **P1 Website stream**: `_tah.php` (`tah_emit($type,$props)`, non-blocking curl with a 300 ms timeout, file spool `kpsc-cache/tah-spool/` + cron flush). Hook into login, device slot, practice serve/answer, record-attempt, WDGW ask/time, payment submit/approve, admin actions. md5-guarded deploy with rollbacks under `kpsc-cache/rollback/tah-*`.
- [ ] **P2 Current app stream (TWA)**: TWA = website, so P1 covers it; additionally tag `src=twa` + `build` from kp-app-pay.js and `app.launch` via app-build.php.
- [ ] **P3 Backfill**: import 90 days from MySQL attempts, ask.sqlite, user_app_build, payments, mail pixels and Matomo (Reporting API `Live.getLastVisitsDetails` joined by userId). Then verify counts per source.
- [ ] **P4 Rules R1–R10 + Risk panel** in admin (reads the VPS via a signed JSON endpoint). Golden fixtures: Athira (uid 95) must hit R4/R5; the demo account (uid 85) and the reviewer (uid 150) are allow-listed.
- [ ] **P5 Profiles + PyOD** nightly; scores shown in the panel.
- [ ] **P6 AI triage + Telegram digest** (Qwen night window → Sonnet judge); draft mails only.
- [ ] **P7 tirreno (optional)**: mirror auth/page/device events, compare it with our rules for 2 weeks; keep it or drop it.
- [ ] **P8 Native app stream**: `/v1/events` batch endpoint + Play Integrity verdicts (see §7).
- [ ] **P9 Drift + feedback loop**, monthly precision report.

## 7. Native app: backend API design (v1)
Principle: the **phone is untrusted**. It only displays things. Entitlement, scoring, correct answers and AI credits are decided on the server.

Auth / entitlement
- `POST /v1/auth/google` {id_token, device_pubkey, integrity_token} → {access_jwt (15 min), refresh (30 d, bound to device)}
- `POST /v1/auth/refresh` {refresh, integrity_token?} → new access token
- `GET  /v1/me` → profile, plan, valid_until, banks[], device slots
- `GET  /v1/entitlement` → {active, banks, valid_until, min_build}. Purchased on the website only; the app shows "Renew on drpreetha.com" (a link opened in the browser; that also keeps Play billing rules simple, see the note below)
- `POST /v1/devices/register` / `DELETE /v1/devices/{id}`

Practice
- `POST /v1/practice/sessions` {bank, mode} → session_id
- `GET  /v1/practice/sessions/{id}/next` → one question **without the answer** (records `question_serves`)
- `POST /v1/practice/sessions/{id}/answer` {qid, choice, client_ms} → {correct, explanation}; the server measures `server_ms` (serve→answer) and ignores client claims for scoring
- `GET  /v1/progress` → per-subject stats, bank %
- `POST /v1/bookmarks`, `POST /v1/reports` (question error reports)

AI tutor
- `POST /v1/tutor/ask` {qid, message} → streamed answer; prompt guard + credits enforced server-side
- `GET  /v1/tutor/credits`

Content / misc
- `GET /v1/news`, `GET /v1/where-am-i/...` (existing tracker), `GET /v1/config` {min_build, flags, kill_switch}

Telemetry
- `POST /v1/events` (batch ≤100, signed by the device key) → into TAH ingest

Security for every call: TLS, short JWT + refresh bound to the device key, Play Integrity on login/refresh plus a random sample of requests, rate limits per uid/device/IP, a request-signing nonce against replays, no bulk endpoints (one question at a time), and audit logs for everything.

Play billing note: Google requires Play Billing for digital content bought *inside* the app. "Pay on the website, app only checks entitlement" is allowed if the app does not steer users to buy inside the app, beyond what Play's current policy permits for India (user-choice billing / external-offers rules change). Check the policy before launch; safest is that the app shows no price and no buy button.

## 8. Opinion: PHP endpoint vs Flask vs other
("TSP" read as PHP.)
- **PHP itself is not unsafe.** Safety comes from auth, validation, rate limiting and secrets handling, not from the language. The problem is *our current* PHP: it is session/cookie based and built for web pages, it runs on shared cPanel (no long-lived workers, no streaming control, no proper rate limiting, secrets in the docroot, 107 exposed .bak files in Oct), and the logic is spread across page scripts.
- **Recommendation: a new API service on the VPS in Python FastAPI** (not Flask):
  - async + streaming (AI tutor), automatic OpenAPI docs → the Flutter/RN client can be generated from them
  - typed validation (Pydantic) on every input
  - same language as the TAH jobs/PyOD/AI → one codebase for API plus monitoring
  - Flask works too, but is sync-first and needs more add-ons for the same result
- **Database**: the API reads the existing MySQL on cPanel (remote MySQL, IP-allow-listed to the VPS, a read/write user limited to the needed tables), so website and app share one source of truth for users, payments and entitlements. Later move the DB to the VPS (or managed) if latency hurts.
- **Website stays PHP** for pages and payments; it calls the same rules (entitlement) through shared DB tables, so the two never disagree.
- Exposure: only `api.drpreetha.com` → Caddy (TLS, rate limits) → FastAPI on loopback. No admin routes on the public host. Secrets in `/root/.secrets/drpreetha/` + cred-broker.

## 9. Ops
- Backups: nightly pg_dump of `tah` → existing backup path; 13-month event retention, IPs truncated after 180 days.
- Health: Hub tile + watchdog (ingest 5xx, spool backlog >1k, nightly job missed).
- Cost: Qwen night window ≈ tiny; Sonnet judge ≤10 calls/day.
- Docs: this file + `drpreetha/threat-hub/` in openclaw_master; gbrain `personal/drpreetha-threat-hub`.

## 10. Open decisions for Kiran
1. Approve FastAPI on VPS + `api.drpreetha.com` subdomain?
2. Level-2 automatic soft actions allowed (credit throttle / re-login)?
3. Include tirreno trial (P7) or skip?
4. Privacy page line "usage is monitored for fair use and security" before P1.
5. Native framework: Flutter (recommended: one UI codebase, good offline, simple secure-storage plugins) vs React Native.
