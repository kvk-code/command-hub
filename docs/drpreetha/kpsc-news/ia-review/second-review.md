### Scores
* **SEO: 5/10** — Fatal keyword mismatch ("Medical Officer" vs "Assistant Surgeon") and massive index bloat for a 22-URL site.
* **GEO (AI Citation): 8/10** — HTML-extracted PDF facts + answer-first summaries + `Source: <pdf>, checked <date>` is elite RAG bait.
* **Agentic Discovery: 6/10** — `llms.txt` is passive. Agents need machine-readable data endpoints and semantic HTML tables, not micro-blog URLs.
* **Funnel: 7/10** — Module-to-PYQ linking is great, but informational pages lack an immediate interactive hook (embedded questions).

---

### Top 5 Problems
1. **Fatal Keyword Mismatch:** You don't rank for *"kerala psc assistant surgeon"* because your URLs and architecture use *"medical-officer"*. KPSC notifications officially use **Assistant Surgeon / Casualty Medical Officer**. Your main slug is targeting the lower-volume synonym.
2. **Severe Cannibalization & Crawl Bloat:** A 177-session site cannot support 15+ overlapping hubs. `/updates/2026-10-28-admit-card-034-2026`, `/exam-date`, and `/034-2026` all compete for the exact same admit card query. Delete `/updates/*`, `/notifications`, and `/answer-key`.
3. **Siloed URL Architecture:** Your existing authority is on `/kpsc-medical-officer-previous-year-questions` and `/...-question-paper/<cat>`. Creating a disconnected `/kpsc-medical-officer/` tree splits link equity. 301-redirect legacy `.php` URLs (`sample-quiz.php`) to clean slugs.
4. **Agents Don't Want News Stubs:** AI agents (ChatGPT/Perplexity) hate clicking through thin `/updates/` pages. They want a single canonical source per entity (`Cat 034/2026`) + a clean JSON endpoint (`/api/kpsc-assistant-surgeon-status.json`) referenced in `llms.txt`.
5. **Wasted Schema Effort:** Google killed `FAQPage` rich results for non-gov/health-authority sites, and as your notes say, LLMs ignore JSON-LD in favor of visible Markdown/HTML tables. Drop `FAQPage` and `NewsArticle`; use clean `<table>`, `<dl>`, and `Dataset` schema.

---

### Revised Hierarchy
Use **assistant-surgeon** as the primary slug (put "Medical Officer" in H1/Title alongside it). Consolidate into 1 Hub, 3 Evergreen Intent Pages, and Category Pages.

```text
/kpsc-assistant-surgeon  (HUB: Live status table of all active categories, exam calendar, notification tracker, 2-line summary, CTA)
  ├── /kpsc-assistant-surgeon/syllabus        (11 modules table, mark distribution, direct links to PYQ topic banks + 1 free interactive MCQ per module)
  ├── /kpsc-assistant-surgeon/rank-list       (Live advice tracker, 177/2025 cutoff, rotation chart, historical rank lists in HTML tables)
  ├── /kpsc-assistant-surgeon/cat-034-2026    (Canonical entity page: timeline, admit card instructions, 974 candidate stat, exam date, syllabus, post-exam answer key)
  ├── /kpsc-assistant-surgeon/cat-177-2025    (General recruitment entity: shortlist, ranked list wef 30 Apr 2026, advice batches Jul/Oct 2026)
  └── /kpsc-assistant-surgeon/cat-401-2024    (Build later)

/api/kpsc-assistant-surgeon.json              (Agentic feed: structured JSON of all active categories, dates, PDF source hashes, linked in llms.txt)
```
*Note: Keep your existing `/kpsc-medical-officer-previous-year-questions` URLs if they have backlinks, but cross-link them heavily from the `/syllabus` and `/cat-*` answer key sections.*

---

### The 4 Pages to Build Before 28 Oct (Admit Card Drop)
1. **`/kpsc-assistant-surgeon/cat-034-2026` (Priority #1):** Captures urgent 28 Oct admit card & 12 Nov exam searches. Must have an HTML `<table>` with Cat No, Post Name (Assistant Surgeon / Medical Officer), Vacancies, Exam Date (12 Nov 2026), Admit Card Date (28 Oct 2026), Registered Candidates (974), and exact KPSC PDF citations. Embed a 3-question mini-quiz right below the admit card instructions.
2. **`/kpsc-assistant-surgeon/syllabus`:** The highest-converting funnel page for the 974 candidates cramming between 28 Oct and 12 Nov. HTML table of the 11 modules + marks + exact count of PYQs in your bank per module -> clicking a module opens a sample quiz filtered to that subject.
3. **`/kpsc-assistant-surgeon` (Main Hub):** Replaces `/exam-date` and `/notifications`. Houses the live comparison matrix of all categories (`034/2026`, `177/2025`, `401/2024`) and the countdown timer.
4. **`/kpsc-assistant-surgeon/rank-list` (incorporating `177/2025` data):** Captures high-volume daily checks from candidates waiting on Jul/Oct 2026 advice batches. Translates KPSC's terrible PDF rank/advice lists into searchable, sortable HTML tables.