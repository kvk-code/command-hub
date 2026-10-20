## 1. Verdict

- SEO: **6.5/10**
- GEO/AI citation: **7/10**
- Agentic discovery: **6/10**
- User funnel: **7.5/10**

Directionally strong, but needs stricter canonicalisation, Assistant Surgeon handling, and machine-readable freshness.

## 2. What is right

- Separate notification/news hub from PYQ hub matches intent.
- Category pages can become citable primary sources if every fact has PDF citation and checked date.
- Status/timeline helps users, AI Overviews, and agents.
- Update posts create freshness/recrawl triggers.
- CTA to PYQ/quiz/subscribe is useful.

## 3. Problems / risks

- **Cannibalisation:** `/kpsc-medical-officer` may compete with PYQ hub. Split intent: new hub owns notification/exam date/syllabus/rank list; PYQ hub owns previous year questions.
- **Assistant Surgeon gap:** URLs ignore it. If valid, create combined or separate hub; do not target Assistant Surgeon with MO-only facts.
- **Duplicate category pages:** category + `/syllabus` + `/answer-key` + `/rank-list` can repeat tables. One canonical owner per fact; hubs should index, not copy.
- **Thin content:** `/notifications`, `/exam-date`, `/rank-list`, `/answer-key` may become link lists. Merge into timeline unless unique tables/status.
- **URL choices:** `/034-2026` is opaque; date-first updates can look stale. Use descriptive slug + stable category ID. Flat alternative: `/kpsc-medical-officer-recruitment-034-2026`.
- **Orphan risk:** pages need hub/breadcrumb/contextual links, not just sitemap.
- **Freshness:** show “Last verified against keralapsc.gov.in PDF” with source URL/notification no/date, not only “Last updated”.
- **E-E-A-T/YMYL:** career/exam info needs verification policy, reviewer author page, corrections, no speculation. Cite official PDF for every claim.
- **FAQ/schema:** use only genuine visible FAQs; schema alone won’t lift rankings.

## 4. Concrete changes to the hierarchy

Use one hub, one canonical category page, subpages only for distinct intent.

```text
/kpsc-medical-officer/                          # notification/news hub
/kpsc-medical-officer/recruitment/034-2026/     # canonical category page
/kpsc-medical-officer/recruitment/177-2025/
/kpsc-medical-officer/syllabus/                 # latest syllabus hub
/kpsc-medical-officer/exam-dates/               # calendar/status table
/kpsc-medical-officer/rank-lists/
/kpsc-medical-officer/answer-keys/              # links to PYQ papers
/kpsc-medical-officer/updates/
/kpsc-medical-officer/updates/admit-card-034-2026/
/kpsc-medical-officer-previous-year-questions   # unchanged
```

If flat slugs required: `/kpsc-medical-officer-recruitment-034-2026`, `/kpsc-medical-officer-syllabus`, etc. Drop `/notifications` if duplicate; 301/canonicalise thin variants.

## 5. Per-page must-haves

- **Hub:** title `Kerala PSC Medical Officer 2026: Notification, Exam Date, Syllabus, Rank List`; H1 same; `WebPage`, `CollectionPage`, `ItemList`, `BreadcrumbList`, optional `FAQPage`; links to categories, PYQ, quiz, subscribe.
- **Category:** title `Kerala PSC Medical Officer 034/2026: Notification, Admit Card, Exam Date, Syllabus`; H1 category name; `WebPage`, `Article`/`NewsArticle`, `Event`/`EducationEvent`, `FAQPage`, breadcrumbs; links to hub, syllabus, exam dates, PYQ, update.
- **Syllabus:** title `Kerala PSC Medical Officer Syllabus 2026: 11 Modules, Marks`; `WebPage`, `ItemList`, optional `Course`; links to category, subject PYQs, quiz.
- **Update:** title `Kerala PSC MO 034/2026 Admit Card Released: Date, Download, Exam Date`; `NewsArticle`, breadcrumbs; links to category, hub, PYQ.
- **Index pages:** `Kerala PSC Medical Officer [Exam Dates/Rank Lists/Answer Keys]`; `WebPage`, `ItemList`; links to relevant categories/PYQs.

All pages: answer-first 2 lines, official source link, “Last verified”, Dr Preetha byline/author page, correction policy, public HTML facts, contextual CTA.

## 6. Agentic/AI discovery layer

- `llms.txt`: list hub, categories, syllabus, feeds, author/verification policy, and official-source rule.
- JSON feed: `/feeds/kpsc-medical-officer-updates.json` with `id`, `url`, `title`, `published`, `modified`, `last_verified_at`, `category_id`, `official_source_pdf`, `status`, `summary`.
- RSS: `/feeds/kpsc-medical-officer-updates.xml`.
- Data endpoint: `/api/kpsc-medical-officer/status.json` for active categories, exam date, admit card status, syllabus modules/marks. Stable/cacheable.
- Robots: allow `GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`, `Bingbot` if citations are goal.
- Server-rendered HTML, semantic tables, no login/JS-only facts.
- IndexNow for Bing; Google via GSC sitemap/URL inspection. Don’t spam.
- Stable IDs: category/notification number, PDF URL, dates, `verified_at`.

## 7. Priority before 28 Oct

1. `/recruitment/034-2026/` — canonical page: notification, vacancies, eligibility, exam date, candidates, syllabus, admit card section, sources.
2. `/kpsc-medical-officer/` — status box: admit card 28 Oct, exam 12 Nov, link to 034/2026 and PYQ.
3. `/syllabus/` — 11 modules/marks, PYQ/quiz links.
4. `/updates/admit-card-034-2026/` — draft/scheduled; publish only after official verification on 28 Oct. If blocked, ship `/exam-dates/`, but update is freshness trigger.