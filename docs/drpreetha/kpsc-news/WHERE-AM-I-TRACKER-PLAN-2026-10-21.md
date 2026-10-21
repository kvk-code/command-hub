# "Where am I?" tracker + KPSC news: long-term plan (21 Oct 2026, awaiting Kiran's OK)

A search box on the KPSC news section: a doctor tells us their exam category, and we tell them where they are in the Kerala PSC process. Shortlist, rank, and how close their turn is for advice.

Status: **plan only**. Nothing built, nothing crawled at scale, nothing public.

---

## 1. What the candidate sees (the box)

One box on every KPSC news page, plus its own page, `/kerala-psc-medical-officer/where-am-i`.

```
Step 1  Which exam?   [ Assistant Surgeon / CMO – Cat 177/2025 ▼ ]   (pre-filled list)
                      or "My category isn't listed" → enter Cat no. + year
Step 2  Have you written this exam?    ( ) Yes   ( ) Not yet
          Not yet  → show the stage the category is at (exam date, admit card, syllabus) + practise link. No personal search.
          Yes      → Step 3
Step 3  Register number [_______]  +  Name [_______] or Date of birth [__/__/____]
          (both needed: proves it's the candidate's own record, blocks browsing others)
Result  Category stage today:   Notification → … → Shortlist ✔ → Interview ✔ → Ranked list ✔ → Advice (in progress)
        You:                    In shortlist ✔ · Rank 412 · Community OBC
        Advice for OBC so far:  up to rank 318 (last advice 16 Jul 2026)  → 94 ranks to go
        Pace:                   ~60 ranks per advice round in this list (indicative)
        Official sources:       shortlist PDF · ranked list PDF · advice page  (checked 21 Oct 2026)
        [ Tell me when advice moves for my community ]  ← opt-in alert (email/Telegram)
        ⚠ Indicative only. Turns follow PSC's community rotation, NJD and supplementary lists. Confirm on keralapsc.gov.in.
```

Rules:
- Only the candidate's own record is shown, and only to the person who typed matching register number + name/DOB. No list view, no "browse others".
- Never show other candidates, addresses or dates of birth. The DOB typed is used only to match, then discarded.
- Result pages are `noindex`; rate limit per IP (e.g. 20 searches/hour); no search is stored unless the person opts in to alerts.

## 2. Test case: Dr Preetha

Kiran will send Dr Preetha's register number, name and category. It is used as the **first end-to-end test** (golden record):
- Stored only in `/root/.secrets/drpreetha/test-candidates.json` (not in git, not in gbrain, not on the site).
- Test: the box must return the same shortlist/rank/advice status that a human reads from the official PDFs.
- Kept as a regression check every night: if her result changes, check whether PSC changed or our parser broke.

More golden records later: one per list format (OMR exam, online exam, NCA list, supplementary list), built only from documents, not from other people's data.

## 3. Data: fetch once, reuse for everyone

A search never fetches from PSC. It reads our own index, which the night job builds.

```
keralapsc.gov.in ──(night crawler)──▶ raw store (every PDF/HTML kept, hashed, dated)
                                          │
                                          ▼
                                  parser per document type
                                          │
                                          ▼
                    index (SQLite on VPS): categories, stages, list rows, advice-reached
                                          │
             ┌────────────────────────────┼─────────────────────────────┐
             ▼                            ▼                             ▼
     "Where am I?" box             news/category pages              JSON feeds + llms.txt
```

- **Raw store**: every document once, named by URL + SHA-256, with fetch date, `Last-Modified`/`ETag`, size. Never deleted (history matters: lists get addenda and corrections).
- **Index tables** (sketch):
  - `category(cat_no, year, post, department, discipline, gazette_date, last_date, status, sources)`
  - `stage(cat, stage_name, date, doc_hash, checked_at)` for the 12 stages
  - `shortlist_entry(cat, reg_no, list_type)` (main / supplementary)
  - `ranked_entry(cat, rank, name_norm, dob_hash, community, list_type)`; DOB is stored only as a salted hash for matching
  - `advice_state(cat, community, rank_reached, total_advised, last_advice_date, doc_hash)`
  - `advice_event(cat, date, count)` for the pace estimate
- Name matching: uppercase, strip titles/dots, compare tokens; on doubt, ask for DOB too.
- Known gap to solve first: shortlists carry **register numbers**, ranked lists carry **names + DOB + community** (as seen in Cat 401/2024). The join is register number → shortlist, then name + DOB → ranked list. Test this on 3 real lists before building the UI.

## 4. Freshness (recency)

| Source | How often | How we detect change |
|---|---|---|
| Notifications (gazette pages) | nightly | new rows on year filter page |
| Exam programmes, interview programmes | nightly | new/“Revised”/“Modified” PDFs |
| Answer keys (online + OMR) | nightly | new rows |
| Short Lists, Ranked List, Addendum/Erratum | nightly | new rows + new attachment links |
| **Details of Advice** (per post page) | **nightly, plus every 6 h on weekdays** for tracked posts | page hash + "date of last advice" field |
| A category a user just entered | on demand, once, then nightly | — |

- Conditional requests (`If-Modified-Since` / `ETag`) so unchanged files cost almost nothing; polite crawl (3 s between requests, browser UA, stop on 403 and retry next night). PSC's site blocked rapid requests once already.
- Every fact on the site and in the box carries **"checked on <date>"**; if a source hasn't been re-checked for 48 h the box shows "data may be out of date".
- Changes go to Kiran on Telegram (Publish/Reject) before they appear on news pages. The box's raw status (rank reached) updates automatically but shows its source and date; a parser failure blocks the update instead of guessing.

## 5. Which categories

1. **Pre-filled list (launch)**: every category we already have question papers for (the 10 paper pages + the bank's source codes: 177/2025, 401/2024, 018/2024, 536/2023, 002/2023, 034/2026 …), plus all Assistant Surgeon/CMO categories found on the shortlist/ranked list pages since 2022.
2. **"Not listed? Enter Cat no. + year"**: we look it up on the notification pages that night; if it's a medical post we add it, crawl all its stages and tell the user by alert when ready.
3. **Which posts count**: all health-related Kerala PSC posts, tagged by discipline:
   - MBBS: Assistant Surgeon/CMO, Assistant Insurance Medical Officer (ESI), Medical Officer (Factories & Boilers, Plantation Corp, Sports), Assistant Professor (Medical Education)
   - Dental: Dental Assistant Surgeon, Assistant Dental Surgeon
   - AYUSH: Medical Officer (Ayurveda/Homoeo/Siddha/Unani/Nature Cure/Netra/Marma), AIMO (Ayurveda/Homoeo)
   - Veterinary: Veterinary Surgeon Gr II
   - Later: nursing, pharmacist, lab technician (very large audiences)
   Every category a user types is logged (category only, not who) as **demand data**: it tells us which question bank to build next.

## 6. Roadmap (5–6 years)

| When | Step | Done when |
|---|---|---|
| **Now → 28 Oct 2026** | Cat 034/2026 page + advice tracker (A, with SEO fixes) live | pages indexed, linked from hub |
| **Nov 2026** | Letter to PSC; lawyer review (DPDP, linking policy); data check on 3 lists; Dr Preetha golden test | written OK or no objection; join works |
| **Dec 2026 – Jan 2027** | Night crawler + raw store + index for Assistant Surgeon only; "Where am I?" box v1 (status by category, no personal search) | 30 nights without parser failure |
| **Feb – Mar 2027** | Personal search v1 (reg no + name/DOB) for MBBS posts; opt-in advice alerts; consent notice + delete option | Dr Preetha test passes nightly; first 50 alert sign-ups |
| **Before 13 May 2027** | DPDP readiness: privacy notice, consent records, deletion flow, grievance contact | lawyer sign-off |
| **2027** | Add ESI, Dental, then AYUSH and Veterinary to tracker; question banks for the most-entered disciplines (from demand data) | each new discipline has its own page group |
| **2028** | Pace model per list (advice rate, expiry, rotation) with honest ranges; Malayalam version; WhatsApp/Telegram bot ("send your category") | — |
| **2029 – 2031** | Other Kerala recruiters (Medical Education Dept direct, KSEB/NHM where applicable); other states' medical PSCs if demand shows; open data API (aggregates only) for researchers/press | — |

Design for the long run:
- Parsers are versioned per document format; each PDF layout gets a test file. PSC changes formats every few years.
- Keep the raw store forever; a parser fix can rebuild the whole index.
- The model (Qwen overnight) only *finds* and *classifies* documents. Code extracts and verifies numbers. No model-written facts.

## 7. Measuring it publicly (for sponsors)

Same pattern as kiranvk.me (Matomo at kiranvk.me/analytics + daily stats JSON + live figures on the hub):
- Add drpreetha.com as a site in the same Matomo (pending Kiran's earlier decision on making figures public; this plan needs **yes** for the KPSC section only).
- Track: visits to the KPSC section, box searches (count only), results found, alert sign-ups, clicks to past papers/subscribe, crawl stats (documents fetched, categories tracked, last refresh).
- Public "Impact" strip on the KPSC main page: e.g. "1,240 doctors checked their status this month · 46 categories tracked · data checked last night 02:10 IST". Figures from Matomo API + crawler log, never typed by hand; visits, not "users".
- Monthly snapshot to `drpreetha/kpsc-news/metrics/` for a pitch deck.

## 8. Sponsorship

Once the numbers are real (rough bar: 6 months of data, a few thousand searches/month):
- **Crawl/AI infra** (Firecrawl, Browserbase, Apify, Bright Data, Exa, Tavily): credits in return for a "data refreshed nightly with ___" credit line + a public case study. Firecrawl and others run startup/open-source credit programmes; check terms when applying, none assumed now.
- **Model providers** (Alibaba Cloud/Qwen, Google for Startups, AWS Activate): the nightly agent is a clean "public-interest AI" story.
- **Health/education** (medical publishers, PG coaching for doctors, banks with doctor loans): sponsor the alerts; strict rule that sponsors never touch candidate data and ads stay off the result card.
- Pitch pack: live impact strip, Matomo export, crawl reliability log, privacy design, two short demo loops recorded in neko.

## 9. Legal and safety steps (before personal search goes live)

1. Letter to PSC (Secretary): describe the tool, ask permission for direct links per their hyperlinking policy, offer to remove anything on request. Never frame PSC pages.
2. Lawyer review: DPDP Act 3(c)(ii) "published under an obligation under law" exemption; our own processing of searches/alerts; PSC linking policy vs copyright page.
3. Privacy notice + consent for alerts; delete-my-data link; no search logs with register numbers by default.
4. Disclaimer on every result; "report an error" button routed to Kiran.

## 10. Decisions for Kiran

1. OK to make KPSC-section figures public (Matomo) for the impact strip and sponsors?
2. OK to send the letter to PSC in Kiran's/Dr Preetha's name (draft first, as Gmail draft)?
3. Scope of the first personal search: Assistant Surgeon only, or all MBBS posts at once?
4. Alerts channel first: email, Telegram, or WhatsApp?
5. Send Dr Preetha's register number + name + category privately (it will stay out of git).
