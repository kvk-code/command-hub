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
Prints a formatted table and saves JSON to `/tmp/ktu_internals_status.json`.

---

## Courses for S8 CSE 2022 Batch (as of 2026-04-14)

| Course Code | Course Name | Faculty | KTU ID |
|-------------|-------------|---------|--------|
| CST428 | Block Chain Technologies | KIRAN V K | KTU-F3938 |
| CST476 | Mobile Computing | Vishnu Shankar V | KTU-F51254 |
| CST402 | Distributed Computing | Shilpa S | KTU-F46545 |
| CST414 | Deep Learning | USHA K | KTU-F5220 |
| CST404 | Comprehensive Viva Voce | KIRAN V K | KTU-F3938 |
| CSD416 | Project Phase II | USHA K | KTU-F5220 |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|---------|
| 404 on Advisor's Batches | Wrong URL (`advisorBatches.htm`) | Use `/eu/exm/staffAdvisorBatches.htm` via menu nav |
| No table after Search | Filters not set / AJAX delay | Add 1.5s between each filter, 3s after Search |
| Batch dropdown empty | Program not yet set (AJAX dependency) | Set AY → Program → wait → then Batch |
| Login fails | Credentials changed | Check `memory/credentials-secure.md` |

---

## Changelog

- **2026-04-14:** Created skill from live workflow analysis (4 screenshots + automation)
- Discovered correct URL: `/eu/exm/staffAdvisorBatches.htm`
- Verified all filter selectors and table structure
- Course code correction: Mobile Computing is CST476 (not CST473)
