---
name: ktu-tutor-view
description: Check internals/attendance upload status for all courses of a batch on KTU e-Gov portal (app.ktu.edu.in). Shows which faculty have submitted and which are still pending. Use when user asks to check internals status, see who uploaded, check attendance submission status, advisor batch status, or "tutor view". Triggers on phrases like "check internals status", "who uploaded internals", "tutor view", "advisor batches", "faculty submission status", "pending internals", "KTU upload status".
---

# KTU Internals Attendance Upload — Tutor View

Checks the **completion status** of internal marks/attendance upload for all courses in a batch. Shows which faculty have submitted ("Submitted by Faculty") and which are still pending.

## When To Use

- User asks: "Have the other teachers uploaded internals?"
- User asks: "Check KTU internals status"
- User asks: "Who hasn't submitted attendance yet?"
- Periodic monitoring before submission deadlines

## Prerequisites

- **Playwright** with headless Chromium
- **Chromium path:** `/data/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome`
- **LD_LIBRARY_PATH:** `/data/.openclaw/browser-libs` (container environment)
- KTU faculty credentials (staff advisor role)

## Credentials

Stored in: `workspace-critical/memory/credentials-secure.md`

| Field | Selector |
|-------|----------|
| URL | `https://app.ktu.edu.in/login.htm` |
| Username | `#login-username` |
| Password | `#login-password` |
| Login Button | `#btn-login` |

---

## The Flow

### Step 1: Login

```python
await page.goto('https://app.ktu.edu.in/login.htm', wait_until='networkidle')
await page.fill('#login-username', USERNAME)
await page.fill('#login-password', PASSWORD)
await page.click('#btn-login')
```

After login → Dashboard at `/eu/alt/dashboard.htm`.

### Step 2: Navigate to Exam → Advisor's Batches

**Do NOT use direct URL** — it causes 404. Navigate via menu:

1. Click **Exam** tab → goes to `/eu/exm/viewObserverAttendanceListing.htm`
2. In left sidebar, click **"Advisor's Batches"** → goes to `/eu/exm/staffAdvisorBatches.htm`

```python
# Click Exam in nav
await page.click('a[href="/eu/exm/viewObserverAttendanceListing.htm"]')
await page.wait_for_load_state('networkidle')

# Click Advisor's Batches in sidebar
await page.click('a[href="/eu/exm/staffAdvisorBatches.htm"]')
await page.wait_for_load_state('networkidle')
```

**Key URLs discovered:**
| Page | URL |
|------|-----|
| Exam tab (landing) | `/eu/exm/viewObserverAttendanceListing.htm` |
| Advisor's Batches | `/eu/exm/staffAdvisorBatches.htm` |

### Step 3: Set Filters

**Filter selectors (verified 2026-04-14):**

| Filter | Selector | Default Value (S8 CSE 2022) |
|--------|----------|----------------------------|
| Academic Year | `#academicYearId` | `96` (2025-2026) |
| Program | `#programId` | `1` (B.Tech) — loads via AJAX after AY |
| Program Type | `#programType` | `1` (Full Time) |
| Semester | `#semesterId` | Select option containing "S8" |
| Eligibility For | `#registrationAllowedStudentStatus` | `1` (Regular Students) |
| Batch | `#batch` | Select option containing "COMPUTER SCIENCE" and "2022" |
| Degree Type | `#degreeType` | `1` (Regular) |

**⚠️ Important:** Dropdowns load via AJAX — add 1.5s delay between each selection.

**⚠️ Batch selector:** This is a `<select>` dropdown (not a radio popup as it appears visually). Select by matching text containing "COMPUTER SCIENCE" and "2022".

### Step 4: Click Search

```python
await page.click('button:has-text("Search")')
await page.wait_for_load_state('networkidle')
await asyncio.sleep(3)
```

### Step 5: Extract Results Table

**Table structure (verified 2026-04-14):**

| Column | Content |
|--------|---------|
| Course | Course code + name (e.g., "CST428-BLOCK CHAIN TECHNOLOGIES") |
| Slot | Slot + regularity (e.g., "D(Regular)") |
| Faculty | Name + KTU ID (e.g., "KIRAN V K(KTU-F3938)") |
| Completion Status | **"Submitted by Faculty"** or **"Pending"** |
| Batch | Batch number (e.g., "1") |
| Action | View Internals/Attendance, Export PDF, Export XLS |

**Status values:**
- ✅ `Submitted by Faculty` — internals uploaded
- ⏳ `Pending` — not yet uploaded

### Step 6: Report Results

Format as a table showing course, faculty, and status with ✅/⏳ indicators.

---

## Filter Value Reference

### Academic Year (`#academicYearId`)
| Value | Year |
|-------|------|
| 97 | 2026-2027 |
| 96 | 2025-2026 |
| 95 | 2024-2025 |
| 94 | 2023-2024 |

### Program (`#programId`)
| Value | Program |
|-------|---------|
| 1 | B.Tech |

### Semester (`#semesterId`)
Select by visible text containing "S8", "S6", etc. Value IDs may vary.

### Degree Type (`#degreeType`)
| Value | Type |
|-------|------|
| 1 | Regular |
| 2 | Honours |
| 3 | Minor |

---

## Script

Ready-to-use script at: `scripts/ktu_tutor_view.py`

### Usage
```bash
bash scripts/run.sh
```

Or directly:
```bash
export LD_LIBRARY_PATH=/data/.openclaw/browser-libs
python3 scripts/ktu_tutor_view.py
```

### Output
- Prints a formatted table with overview + drill-down results
- Saves JSON to `/tmp/ktu_internals_status.json`
- Screenshots: `/tmp/ktu_tv_*.png` (overview), `/tmp/ktu_tv_drill_<COURSE>.png` (drill-down)

---

## Drill-Down: Student-Level Completeness (v2)

For target courses (currently Usha K's CST414, CSD416), the script can **click into the View Internals/Attendance page** and extract per-student data.

### When Drill-Down Triggers
- Course status is ⚡ **Entered (not submitted)** — Export buttons visible
- Course status is ✅ **Submitted by Faculty**
- Does NOT drill into ⏳ **Pending** courses (no data to check)

### What It Extracts

**Page URL:** `/eu/exm/semesterAttendanceInternalListing.htm?urlParams=...`

**Table structure (View Internals page):**

| Column | Content | Input Name |
|--------|---------|------------|
| Student Name | Name + Reg No (e.g., "ABHIJITH P P - NSS22CS001") | — |
| Attendance % | Text input | `attendance` |
| Internal Marks/50 | Text input | `internalMarks` |
| Avail Long Leave | Checkbox | `leave` |
| Avail Duty Leave | Checkbox | `dutyLeave` |
| Disciplinary Action | Hidden | `disciplinary` |
| Eligible for Written Exam | Text (Yes/No) | `eligibility` |
| Status | Hidden input | `sessionalEntryStatus` |
| In-eligibility Type | Hidden | `reason` |

**Key inputs per row:**
- `attendance` — text input, value is percentage (e.g., "93")
- `internalMarks` — text input, value is marks out of 50 (e.g., "42")
- `studentId` — hidden, unique student ID
- `sessionalEntryStatus` — hidden, "Saved-Not Submitted" or empty

### Drill-Down Output
```
📋 DRILL-DOWN: 35/73 students complete
   Attendance filled: 35/73
   Marks filled: 35/73
   Blank: 38 students
   Entry status: Saved-Not Submitted
   First blanks: KANISHKA C, KEERTHANA S, MERIN P R...
```

### Configuring Drill-Down Targets

In `ktu_tutor_view.py`, modify these constants:
```python
DRILL_DOWN_COURSES = ['CST414', 'CSD416']  # Course codes to drill into
```

### Course-Specific Completeness Rules

| Course | Attendance Required | Marks Required | Notes |
|--------|-------------------|----------------|-------|
| CST414 | Yes | Yes | Standard course — both fields needed |
| CSD416 | Yes | **No** | Project Phase II — only attendance matters |
|
When reporting drill-down for CSD416, evaluate completeness on attendance count only. Missing marks should be reported as "N/A" not as incomplete.

### Navigation After Drill-Down

After extracting student data, the script calls `page.go_back()` to return to the Advisor's Batches results. If navigation fails, it re-navigates to the saved URL.

---

## Courses for S8 CSE 2022 Batch (as of 2026-04-14)

| Course Code | Course Name | Faculty | KTU ID |
|-------------|-------------|---------|--------|
| CST428 | Block Chain Technologies | KIRAN V K | KTU-F3938 |
| CST476 | Mobile Computing | Vishnu Shankar V | KTU-F51254 |
| CST402 | Distributed Computing | Shilpa S | KTU-F46545 |
| CST414 | Deep Learning | USHA K | KTU-F5220 |
| CST404 | Comprehensive Viva Voce | KIRAN V K | KTU-F3938 |
| CSD416 | Project Phase II | USHA K | KTU-F5220 | **Attendance only** (marks N/A) |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|---------|
| 404 on Advisor's Batches | Wrong URL (`advisorBatches.htm`) | Use `/eu/exm/staffAdvisorBatches.htm` via menu nav |
| No table after Search | Filters not set / AJAX delay | Add 1.5s between each filter, 3s after Search |
| Batch dropdown empty | Program not yet set (AJAX dependency) | Set AY → Program → wait → then Batch |
| Login timeout / connection error | KTU site busy or down | Script auto-retries up to 4 attempts with 2/4/8 min backoff; check `/tmp/ktu_monitor_retries.log` |
| Drill-down page doesn't load | Encrypted URL params expired | Must navigate from overview — URLs are session-specific |
| Back navigation fails after drill-down | KTU AJAX state lost | Script auto-detects and re-navigates to saved URL |
| Empty trailing row in student table | KTU adds blank row at end | Script filters out rows with empty name |
| Garbled email subject (e.g., `ÃƒÂ¢`) | Unicode chars (em dash, emojis) in subject line | Use ASCII hyphens only in subject; set `charset='utf-8'` on MIMEText body |

---

## Cron Job: Automated Monitoring

**Schedule:** Every 30 minutes
**Model:** Qwen 3.5+ (vision-capable for screenshot verification)
**Notifications:** Telegram DM + Email (kiranvk@nssce.ac.in via gws CLI)

**What the cron does:**
1. Runs `ktu_tutor_view.py` → login, scrape overview, drill-down if applicable
2. **Retry on failure:** If the script fails (login timeout, connection error), retries up to 4 attempts with exponential backoff (2/4/8 min delays). Total worst-case: ~14 min of retries, safely within the 30-min window.
3. Qwen 3.5+ reads screenshots for visual verification
4. Sends Telegram + Email with:
   - Overview status for all 6 courses
   - Drill-down details for target courses (student-level completeness)
   - Change detection from previous check
   - Retry count if retries were needed
5. If ALL 4 attempts fail: sends "site unreachable" notification (no stale data)

**Retry log:** `/tmp/ktu_monitor_retries.log`
**Timeout:** 25 min (1500s) to accommodate retries

**To disable:** `cron update jobId=<id> patch={"enabled": false}`
**To trigger:** `cron run jobId=<id>`

---

## Changelog

- **2026-04-16:** v2.2 — CSD416 attendance-only rule
  - Project Phase II (CSD416) only requires attendance entry, not internal marks
  - Cron reports CSD416 completeness based on attendance fill count only
  - Marks column flagged as N/A for this course
- **2026-04-16:** v2.1 — Added retry-with-backoff to cron job
  - 4 attempts with exponential backoff (2/4/8 min delays)
  - Timeout increased to 25 min (1500s) to accommodate retries
  - Failure detection: exit code, timeout keywords, login page in screenshot
  - Clean failure: "site unreachable" notification instead of stale data
  - Retry log at `/tmp/ktu_monitor_retries.log`
- **2026-04-16:** v2 — Added drill-down into student-level data for target courses
  - Clicks View Internals/Attendance for Usha K's courses (CST414, CSD416)
  - Extracts per-student attendance % and internal marks from input fields
  - Reports X/Y filled, blank count, first blank student names
  - Takes drill-down screenshots for Qwen 3.5+ visual verification
  - Only drills when course shows entered/submitted (skips pure Pending)
  - Discovered View Internals page structure: `semesterAttendanceInternalListing.htm`
  - Input names: `attendance`, `internalMarks`, `sessionalEntryStatus`
- **2026-04-14:** v1 — Created skill from live workflow analysis
  - Discovered correct URL: `/eu/exm/staffAdvisorBatches.htm`
  - Verified all filter selectors and table structure
  - Course code correction: Mobile Computing is CST476 (not CST473)
  - Three-state detection: Submitted / Entered (not submitted) / Pending
