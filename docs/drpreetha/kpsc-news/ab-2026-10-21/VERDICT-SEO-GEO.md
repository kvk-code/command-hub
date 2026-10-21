# KPSC news A/B: design + SEO + AI/agent search verdict (21 Oct 2026)

Design review = page-designer `ab` (Gemini 4 Argon, blind, from 390/1366 screenshots, out of 70).
SEO/GEO/agent review = hard HTML checks (`seo_audit.py`) + blind Gemini 4 Argon review of the HTML (`seo_review.js`), 7 criteria x 10 = out of 70.

## cat-034-2026

| | A | B |
|---|---|---|
| Design (/70) | 51 | 51 |
| SEO + AI search + agents (/70) | 41 | 25 |
| technical_seo | 7 | 1 |
| structured_data | 0 | 0 |
| answer_first | 7 | 5 |
| ai_citation | 8 | 4 |
| agentic_readiness | 6 | 2 |
| eeat_ymyl | 9 | 6 |
| funnel_links | 4 | 7 |

**A issues**
- CRITICAL BROKEN LINK: All 4 links to the past-paper hub point to '/kerala-psc-medical-officer-previous-year-questions' instead of the only valid hub URL '/kpsc-medical-officer-previous-year-questions'.
- Zero JSON-LD structured data (<script type="application/ld+json"> is completely missing).
- Title is 72 characters (exceeds ~60 char display limit) and meta description is 201 characters (will truncate at ~155-160 chars).
- FAQ relies on JavaScript onclick="toggleFaq(this)" with <button> tags instead of native, JS-free <details>/<summary> elements or semantic H3 question headings.
- H2 headings are generic ('Exam Details', 'Recruitment Lifecycle') rather than high-intent search queries ('Kerala PSC Cat 034/2026 Exam Date & Admit Card').
- Only 2 <time> tags used; key dates like '12 November 2026', '28 October 2026', and '14 August 2026' lack machine-readable <time datetime="..."> markup.
- External links to Kerala PSC PDFs only link to the root domain (https://www.keralapsc.gov.in) rather than specific PDF/notification endpoints, and Open Graph/Twitter meta tags are missing.

**B issues**
- FATAL SEO ERROR: Contains <meta name="robots" content="noindex">, completely blocking search engines and AI search crawlers from indexing the page.
- Missing <meta name="description"> and missing <link rel="canonical">.
- Broken heading hierarchy: jumps directly from <h1> to <h3> with zero <h2> tags.
- Breadcrumbs are non-clickable <span> tags instead of <a href="..."> links.
- Zero IDs or anchor links (anchors_ids: 0); updates log entries cannot be deep-linked.
- Semantic HTML abuse: <time> tags wrap stage names ('Notification', 'Apply', 'Answer key') without datetime attributes instead of actual dates.
- Syllabus is rendered as confusing progress bars ('20/20 · 100%', '14/14 · 100%') in a <ul> rather than a semantic <table>, distorting the meaning of mark weightage for AI extractors.
- Zero external source links (<a href>) to Kerala PSC.

**Fixes for the winner**
- Fix the broken past-paper hub URL in all 4 locations (header nav, CTA band, sidebar quick links, footer): replace href="/kerala-psc-medical-officer-previous-year-questions" with href="/kpsc-medical-officer-previous-year-questions".
- Trim <title> and <meta name="description"> and add OpenGraph tags in <head>:
<title>Kerala PSC Cat 034/2026 Assistant Surgeon (SC/ST) Exam Date</title>
<meta name="description" content="Kerala PSC Cat 034/2026 Assistant Surgeon / CMO (SC/ST) exam is on 12 Nov 2026 (100 marks, 974 candidates). Check admit card date, 11-module syllabus & status.">
<meta property="og:title" content="Kerala PSC Cat 034/2026 Assistant Surgeon (SC/ST) Exam Tracker">
<meta property="og:description" content="Online exam: 12 Nov 2026. Admit card: 28 Oct 2026. 974 candidates, 100 marks across 11 modules.">
<meta property="og:url" content="https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon/cat-034-2026">
<meta property="og:type" content="article">
- Add comprehensive JSON-LD (<script type="application/ld+json">) in <head> combining WebPage/Article (with reviewedBy, dateModified), BreadcrumbList, Event (for the 12 Nov 2026 exam), and FAQPage:
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://drpreetha.com/"},
        {"@type": "ListItem", "position": 2, "name": "Kerala PSC Medical Officer", "item": "https://drpreetha.com/kerala-psc-medical-officer"},
        {"@type": "ListItem", "position": 3, "name": "Assistant Surgeon", "item": "https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon"},
        {"@type": "ListItem", "position": 4, "name": "Cat 034/2026", "item": "https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon/cat-034-2026"}
      ]
    },
    {
      "@type": "Article",
      "headline": "Cat 034/2026 — Assistant Surgeon / Casualty Medical Officer (SC/ST) Kerala PSC Tracker",
      "datePublished": "2026-08-15",
      "dateModified": "2026-08-15",
      "author": {"@type": "Person", "name": "Dr Preetha", "hasCredential": "MBBS, MS ENT"},
      "reviewedBy": {"@type": "Person", "name": "Dr Preetha", "hasCredential": "MBBS, MS ENT"},
      "mainEntityOfPage": "https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon/cat-034-2026"
    },
    {
      "@type": "EducationEvent",
      "name": "Kerala PSC Cat 034/2026 Assistant Surgeon / CMO Online Exam",
      "description": "Special recruitment examination for SC/ST candidates to the post of Assistant Surgeon / Casualty Medical Officer in Health Services Department (100 marks, 974 candidates).",
      "startDate": "2026-11-12",
      "endDate": "2026-11-12",
      "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventScheduled",
      "organizer": {"@type": "GovernmentOrganization", "name": "Kerala Public Service Commission", "url": "https://www.keralapsc.gov.in"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type": "Question", "name": "When is the Kerala PSC Cat 034/2026 Assistant Surgeon exam and admit card release date?", "acceptedAnswer": {"@type": "Answer", "text": "The online examination is scheduled for 12 November 2026 (100 marks). Admit cards are available from 28 October 2026 in the Kerala PSC OTR profile."}},
        {"@type": "Question", "name": "When will the Cat 034/2026 answer key, shortlist, ranked list, and advice be published?", "acceptedAnswer": {"@type": "Answer", "text": "Stages after the 12 November 2026 exam—including answer key, shortlist, DV/interview, ranked list, addendum, and advice—are not yet published by Kerala PSC."}}
      ]
    }
  ]
}
</script>
- Replace JS-dependent FAQ <button onclick="toggleFaq(this)"> with native HTML <details open><summary><h3>...</h3></summary><div class="faq-a">...</div></details> so answers are unconditionally crawlable and work without JavaScript.
- Rewrite H2 headings to capture explicit search queries while keeping stable anchor IDs:
<h2 id="lifecycle-heading" class="sect">Cat 034/2026 Recruitment Lifecycle (Notification to Rank List &amp; Advice)</h2>
<h2 id="exam-heading" class="sect">Kerala PSC Assistant Surgeon (Cat 034/2026) Exam Date &amp; Admit Card</h2>
<h2 id="syllabus-heading" class="sect">Cat 034/2026 Syllabus &amp; Module-Wise Mark Distribution (100 Marks)</h2>
- Wrap all dates in semantic <time> elements across the hero, lifecycle, dl, and syllabus sections: <time datetime="2026-11-12">12 November 2026</time>, <time datetime="2026-10-28">28 October 2026</time>, and <time datetime="2026-08-14">14 August 2026</time>.
- Add stable IDs to each of the 12 lifecycle stages (e.g., id="stage-notification", id="stage-admit-card", id="stage-exam", id="stage-ranked-list", id="stage-advice") and convert the lifecycle container from <div role="list"> to an ordered list <ol class="lifecycle-track">.

**Agent layer**
- Add machine-readable discovery links in <head> for AI agents and crawlers:
<link rel="alternate" type="application/json" href="https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon/cat-034-2026.json" title="Cat 034/2026 Structured Status JSON">
<link rel="help" type="text/plain" href="https://drpreetha.com/llms.txt" title="LLM & Agent Site Guide">
- Expose deterministic data-* attributes on the 12 lifecycle items so autonomous agents can parse stage state without CSS/visual heuristics:
<li id="stage-exam" class="lifecycle-stage" data-stage-index="5" data-stage-slug="exam" data-status="upcoming" data-date="2026-11-12">
- Convert the Syllabus table footer into a proper <tfoot><tr><th scope="row">Total</th><td>100</td></tr></tfoot> and add a <caption>Kerala PSC Cat 034/2026 Assistant Surgeon Syllabus Weightage (100 Marks)</caption> for unambiguous table extraction.
- Add direct anchor links on every Updates Log entry (e.g., <a href="#update-2026-08-15" aria-label="Permalink to 15 August 2026 update">#</a>) and add chronological entries for <li id="update-2026-08-14"><time datetime="2026-08-14">14 August 2026</time>: Official 11-module syllabus PDF published by Kerala PSC.</li>.

## advice-tracker

| | A | B |
|---|---|---|
| Design (/70) | 61 | 42 |
| SEO + AI search + agents (/70) | 44 | 27 |
| technical_seo | 7 | 1 |
| structured_data | 0 | 0 |
| answer_first | 8 | 5 |
| ai_citation | 9 | 4 |
| agentic_readiness | 6 | 2 |
| eeat_ymyl | 9 | 7 |
| funnel_links | 5 | 8 |

**A issues**
- CRITICAL BROKEN LINK: Links to '/kerala-psc-medical-officer-previous-year-questions' in 3 places (header, CTA, footer) instead of the verified '/kpsc-medical-officer-previous-year-questions'.
- Missing JSON-LD structured data entirely (no Article, BreadcrumbList, FAQPage, or Dataset).
- Missing required internal link to category pages (e.g., '/kerala-psc-medical-officer/assistant-surgeon/categories').
- Zero <time datetime='...'> tags used for dates (30 Apr 2026, 25 May 2026, 9 Jun 2026, 16 Jul 2026, 21 Oct 2026).
- Title tag is 90 characters (will truncate in SERPs) and omits 'Kerala PSC'.
- H2 headings are topical labels ('Advice Timeline', 'Ranked List Validity') rather than search-intent questions ('When was the last Kerala PSC Assistant Surgeon advice?', 'How long is the Cat 177/2025 rank list valid?').
- External source links point to generic 'https://www.keralapsc.gov.in' while anchor text falsely claims '(PDF)'.

**B issues**
- FATAL SEO ERROR: Contains <meta name="robots" content="noindex">, completely blocking search indexing.
- Missing <meta name="description"> and <link rel="canonical">.
- Failed prompt requirement to render a 'community table': used a <ul> of text chips instead of a semantic <table>, separating the S/L and 'Within OC' notes from their respective ranks.
- Broken heading hierarchy: jumps directly from <h1> to <h3> with zero <h2> elements.
- Breadcrumbs use dead <span> tags instead of crawlable <a href> links.
- Used <time> tags without the machine-readable 'datetime' attribute.
- Zero external links to the official source (keralapsc.gov.in) and zero section IDs/anchors.

**Fixes for the winner**
- Fix the broken Past Papers hub link in header, CTA bar, and footer: replace href="/kerala-psc-medical-officer-previous-year-questions" with href="/kpsc-medical-officer-previous-year-questions".
- Add the missing link to category pages in the CTA bar or community section: <a href="/kerala-psc-medical-officer/assistant-surgeon/categories" class="btn btn-outline">Category-wise Analysis</a>.
- Shorten and optimize <title> to ~60-65 chars: <title>Kerala PSC Assistant Surgeon Advice Tracker (Cat 177/2025)</title>.
- Add OpenGraph and Twitter Card meta tags in <head>: <meta property="og:title" content="...">, <meta property="og:description" content="...">, <meta property="og:url" content="https://drpreetha.com/kerala-psc-medical-officer/assistant-surgeon/advice">, <meta property="og:type" content="article">, <meta name="twitter:card" content="summary">.
- Wrap all dates in semantic <time> tags with ISO-8601 datetime attributes: e.g., <time datetime="2026-04-30">30 Apr 2026</time>, <time datetime="2026-05-25">25 May 2026</time>, <time datetime="2026-06-09">9 Jun 2026</time>, <time datetime="2026-07-16">16 Jul 2026</time>, <time datetime="2026-10-21">21 Oct 2026</time>, <time datetime="2025-11-28">28 Nov 2025</time>, <time datetime="2025-12-20">20 Dec 2025</time>.
- Rewrite H2s to capture natural-language search queries while keeping existing IDs: <h2 id="community-heading" class="sect">What is the Last Rank Reached by Community (Cat 177/2025)?</h2>, <h2 id="timeline-heading" class="sect">When Were the Kerala PSC Assistant Surgeon Advice Dates?</h2>, <h2 id="validity-heading" class="sect">How Long is the Cat 177/2025 Ranked List Valid?</h2>.
- Inject a comprehensive JSON-LD <script type="application/ld+json"> block in <head> combining @graph with BreadcrumbList, MedicalWebPage/Article (with dateModified: '2026-10-21', author/reviewedBy: Dr Preetha), FAQPage (mapping the 6 <details> items), and Dataset (describing the Cat 177/2025 community cutoff table).
- Update external link anchor text from 'Official PDF link' to 'Official Kerala PSC Advice Page (keralapsc.gov.in)' or link directly to the specific Kerala PSC advice portal URL.

**Agent layer**
- Add machine-readable discovery links in <head>: <link rel="alternate" type="application/json" href="/kerala-psc-medical-officer/assistant-surgeon/advice.json" title="Advice Tracker Data (JSON)"> and <link rel="llms-txt" href="/llms.txt">.
- Add stable row IDs and data-* attributes to the community <table> rows for deterministic agent extraction: e.g., <tr id="rank-oc" data-community="OC" data-rank="310" data-list="main">, <tr id="rank-st" data-community="ST" data-rank="11" data-list="supplementary">.
- Wrap the main content inside <main> with <article itemscope itemtype="https://schema.org/Article"> so DOM-parsers can cleanly isolate the core document from site chrome.

## Hard checks (seo_audit.json)
```
{
 "cat-034-2026_A": {
  "title": "Cat 034/2026 \u2013 Assistant Surgeon / CMO (SC/ST) | Kerala PSC Exam Tracker",
  "title_len": 72,
  "meta_desc_len": 201,
  "noindex": false,
  "canonical": true,
  "lang": true,
  "og": 0,
  "twitter_card": false,
  "h1": 1,
  "h2": 5,
  "question_headings": 0,
  "jsonld_types": [],
  "jsonld_valid": true,
  "time_tags": 2,
  "tables": 1,
  "th_scope": 2,
  "details_faq": 0,
  "psc_pdf_links": 4,
  "internal_links": [
   "/",
   "/kerala-psc-medical-officer",
   "/kerala-psc-medical-officer-previous-year-questions",
   "/kerala-psc-medical-officer/assistant-surgeon",
   "/sample-quiz.php",
   "/subscribe.php"
  ],
  "html_ext_links": [],
  "anchors_ids": 14,
  "breadcrumb_nav": true,
  "main_landmark": true,
  "article": false,
  "js_required_text": true,
  "author_byline": true,
  "last_updated": true,
  "disclaimer": true,
  "pii_like": false,
  "bytes": 27183
 },
 "cat-034-2026_B": {
  "title": "Cat 034/2026 Assistant Surgeon",
  "title_len": 30,
  "meta_desc_len": 0,
  "noindex": true,
  "canonical": false,
  "lang": true,
  "og": 0,
  "twitter_card": false,
  "h1": 1,
  "h2": 0,
  "question_headings": 0,
  "jsonld_types": [],
  "jsonld_valid": true,
  "time_tags": 0,
  "tables": 0,
  "th_scope": 0,
  "details_faq": 0,
  "psc_pdf_links": 0,
  "internal_links": [
   "/kpsc-medical-officer-previous-year-questions",
   "/sample-quiz.php",
   "/subscribe.php"
  ],
  "html_ext_links": [],
  "anchors_ids": 0,
  "breadcrumb_nav": true,
  "main_landmark": true,
  "article": false,
  "js_required_text": false,
  "author_byline": true,
  "last_updated": true,
  "disclaimer": true,
  "pii_like": false,
  "bytes": 16814
 },
 "advice-tracker_A": {
  "title": "Assistant Surgeon Advice Tracker \u2014 Will My Rank Be Reached? | Cat 177/2025 | drpreetha.com",
  "title_len": 90,
  "meta_desc_len": 164,
  "noindex": false,
  "canonical": true,
  "lang": true,
  "og": 0,
  "twitter_card": false,
  "h1": 1,
  "h2": 7,
  "question_headings": 0,
  "jsonld_types": [],
  "jsonld_valid": true,
  "time_tags": 0,
  "tables": 1,
  "th_scope": 3,
  "details_faq": 6,
  "psc_pdf_links": 5,
  "internal_links": [
   "/",
   "/kerala-psc-medical-officer",
   "/kerala-psc-medical-officer-previous-year-questions",
   "/kerala-psc-medical-officer/assistant-surgeon",
   "/sample-quiz.php",
   "/subscribe.php"
  ],
  "html_ext_links": [],
  "anchors_ids": 9,
  "breadcrumb_nav": true,
  "main_landmark": true,
  "article": false,
  "js_required_text": false,
  "author_byline": true,
  "last_updated": true,
  "disclaimer": true,
  "pii_like": false,
  "bytes": 20154
 },
 "advice-tracker_B": {
  "title": "Assistant Surgeon Advice Tracker",
  "title_len": 32,
  "meta_desc_len": 0,
  "noindex": true,
  "canonical": false,
  "lang": true,
  "og": 0,
  "twitter_card": false,
  "h1": 1,
  "h2": 0,
  "question_headings": 0,
  "jsonld_types": [],
  "jsonld_valid": true,
  "time_tags": 0,
  "tables": 0,
  "th_scope": 0,
  "details_faq": 0,
  "psc_pdf_links": 0,
  "internal_links": [
   "/kerala-psc-medical-officer/assistant-surgeon/categories",
   "/kpsc-medical-officer-previous-year-questions",
   "/sample-quiz.php",
   "/subscribe.php"
  ],
  "html_ext_links": [],
  "anchors_ids": 0,
  "breadcrumb_nav": true,
  "main_landmark": true,
  "article": false,
  "js_required_text": false,
  "author_byline": true,
  "last_updated": true,
  "disclaimer": true,
  "pii_like": false,
  "bytes": 15391
 }
}
```