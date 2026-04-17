---
name: ktu-attendance-internals
description: Automate attendance percentage and internal marks entry for faculty-assigned courses on KTU e-Gov portal (app.ktu.edu.in). Use when user asks to enter attendance, submit internals, update marks, fill attendance data, or enter KTU attendance/internals for a subject. Triggers on phrases like "KTU attendance", "enter attendance KTU", "internal marks KTU", "submit internals", "KTU marks entry", "attendance entry", "fill attendance percentage".
---

# KTU Attendance & Internals Entry — Automation Skill

Automates the entry of **attendance percentage** and **internal marks** for faculty-assigned courses on the KTU e-Gov portal. Handles the full workflow from login to Save (NOT submit).

## ⚠️ CRITICAL SAFETY RULE

**NEVER click "Mark As Complete" button.** This submits/locks the data permanently. Always use the blue **Save** button only.

- **Save** = Blue button → data persisted, can edit later
- **Mark As Complete** = Green button → data locked, CANNOT undo

---

## Prerequisites

- **Playwright** with headless Chromium
- **Chromium path:** `/data/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome`
- **LD_LIBRARY_PATH:** `/data/.openclaw/browser-libs` (container environment)
- KTU faculty credentials (username + password)

---

## Credentials

Stored in: `workspace-critical/memory/credentials-secure.md`

| Field | Value |
|-------|-------|
| URL | `https://app.ktu.edu.in/login.htm` |
| Username Selector | `#login-username` |
| Password Selector | `#login-password` |
| Login Button | `#btn-login` |

---

## Input Format (CSV)

Student data must be provided as CSV with the following columns:

```csv
Course Code,Name,Register No,Attendance Percentage,Internal Marks,Avail Leave,Disciplinary Action,Lab Incomplete
CST428,ABHIJITH P P,NSS22CS001,84%,46,,,
CST428,ABHINANDA M S,NSS22CS002,75%,47,,,
CST428,MEGHA P H,MAC22CS044,91%,46,,,
```

**Required columns:**
- `Register No` — Registration number (NSS22CS###, MAC22CS###, PKD22CS###, LNSS##CS###)
- `Attendance Percentage` — Percentage value (0-100, % symbol optional)
- `Internal Marks` — Marks out of 50

**Note:** The script normalizes reg numbers automatically. `LNSS21CS065` → `LNSS22CS065` (lateral entry variation).

---

## Safety & Testing

### Dry-Run Mode
Before production use:
1. Test with 1-2 students only in a test CSV
2. Use screenshot verification (`/tmp/ktu_step*.png`) at each stage
3. Verify saved data on KTU portal manually before trusting automation
4. Always check that "Saved-Not Submitted" status appears

### Rate Limiting
- **Delays:** 2-3 seconds between student row operations
- **Max throughput:** ~10 students/minute to avoid bot detection
- **CAPTCHA:** If CAPTCHA appears, STOP immediately and complete manually
- **Session timeout:** KTU sessions expire after ~30 minutes; re-login if needed

### Rollback Procedure
- Data **CAN be edited** after Save as long as Mark As Complete is NOT clicked
- To correct mistakes: re-run script with corrected values
- To clear all data: manually delete on KTU portal (before submission only)

---

## The Flow (Step by Step)

### Step 1: Login

```python
await page.goto('https://app.ktu.edu.in/login.htm', wait_until='networkidle')
await page.fill('#login-username', USERNAME)
await page.fill('#login-password', PASSWORD)
await page.click('#btn-login')
await page.wait_for_timeout(5000)
```

After login, lands on Dashboard at `/eu/alt/dashboard.htm`.

---

### Step 2: Navigate to Faculty Assigned Courses

Direct URL navigation (faster than clicking tabs):

```python
await page.goto('https://app.ktu.edu.in/eu/ins/facultyAssigned.htm', wait_until='networkidle')
await page.wait_for_timeout(3000)
```

---

### Step 3: Set Filters and Search

**Filter dropdown IDs (verified):**

| Filter | Selector | Value for S8 2025-26 |
|--------|----------|---------------------|
| Academic Year | `#academicYearId` | `96` (2025-2026) |
| Program | `#programId` | `1` (B.Tech) |
| Program Type | `#programType` | `1` (Full Time) |
| Semester Type | `#semesterType` | `2` (Even) |
| Eligibility For | `#registrationAllowedStudentStatus` | `1` (Regular Students) |

**Important:** Values may differ for other batches. Use `select_option()` by value, not label.

```python
await page.select_option('#academicYearId', value='96')
await page.wait_for_timeout(500)
await page.select_option('#programId', value='1')
await page.wait_for_timeout(500)
await page.select_option('#programType', value='1')
await page.wait_for_timeout(500)
await page.select_option('#semesterType', value='2')
await page.wait_for_timeout(500)
await page.select_option('#registrationAllowedStudentStatus', value='1')
await page.wait_for_timeout(500)

# Click Search
await page.click('#facultyAssignedForm_search')
await page.wait_for_timeout(8000)  # Wait for AJAX table to load
```

---

### Step 4: Find Course and Click Attendance/Internals

**Course table columns (verified by Qwen 3.5 Plus):**
| # | Column |
|---|--------|
| 1 | Course (e.g., "BLOCK CHAIN TECHNOLOGIES-CST428") |
| 2 | Slot Name (e.g., "D(Regular)") |
| 3 | Program |
| 4 | Course Program |
| 5 | Branch |
| 6 | Batch |
| 7 | Scheme |
| 8 | Action |

**Link location:** Column 8 (Action), text = "Attendance/Internals"

```python
# Find the course row
rows = await page.query_selector_all('tr')
for row in rows:
    text = await row.inner_text()
    if COURSE_CODE in text:  # e.g., "CST428"
        link = await row.query_selector('a:has-text("Attendance"), a:has-text("Internal")')
        if link:
            await link.click()
            await page.wait_for_timeout(5000)
            break
```

---

### Step 5: Enter Attendance and Internal Marks

**Student table structure (verified by Qwen 3.5 Plus):**

| Column | Content | Input Type |
|--------|---------|------------|
| 1 | Student Name + Reg Number | Text display (not editable) |
| 2 | Attendance Percentage | `<input type="number">` |
| 3 | Internal Marks/50 | `<input type="number">` |
| 4 | Avail Long Leave | Checkbox (optional) |
| 5 | Avail Duty Leave | Checkbox (optional) |
| 6 | Eligible for Exam | Text (Yes/No) |
| 7 | Status | Text display |

**Reg number format:**
- Main NSSCE students: `NSS22CS###`
- MAC students: `MAC22CS###`
- PKD students: `PKD22CS###`
- Lateral entry: `LNSS21CS###` or `LNSS22CS###`

Reg number appears as: `NAME - REGNUMBER` in Column 1.

**Data entry pattern:**

```python
# Parse CSV data into dict keyed by reg number
STUDENT_DATA = {
    'NSS22CS001': {'attendance': '84', 'marks': '46'},
    'NSS22CS002': {'attendance': '75', 'marks': '47'},
    ...
}

# Find student rows
for row in await page.query_selector_all('tr'):
    inputs = await row.query_selector_all('input[type="number"]')
    
    if len(inputs) < 2:
        continue  # Not a student data row
    
    # Extract reg number from row text
    row_text = await row.inner_text()
    reg_match = re.search(r'(NSS|MAC|PKD|LNSS)\d*CS\d+', row_text, re.IGNORECASE)
    
    if not reg_match:
        continue
    
    reg_no = reg_match.group(0).upper()
    
    # Handle lateral entry variation (LNSS21CS -> LNSS22CS)
    if 'LNSS21CS' in reg_no:
        reg_no = reg_no.replace('LNSS21CS', 'LNSS22CS')
    
    if reg_no not in STUDENT_DATA:
        continue
    
    student = STUDENT_DATA[reg_no]
    
    # Fill attendance (input 0) and marks (input 1)
    await inputs[0].fill(student['attendance'])
    await inputs[1].fill(student['marks'])
```

---

### Step 6: Click Save (NOT Mark As Complete!)

**Buttons (verified by Qwen 3.5 Plus):**

| Button | Color | Text | CSS Class | Action |
|--------|-------|------|-----------|---------|
| Save | Blue | "Save" | `btn-primary` | ✓ Click this |
| Mark As Complete | Green | "Mark As Complete" | `btn-success` | ⚠️ NEVER click |
| Add | Green | "Add" | `btn-info` | For other branch students |

```python
# Scroll to bottom
await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
await page.wait_for_timeout(2000)

# Find Save button specifically
save_btn = await page.query_selector('button.btn-primary:has-text("Save")')

if save_btn:
    # SAFETY CHECK: verify text is exactly "Save"
    text = await save_btn.inner_text()
    if text.strip().lower() == 'save':
        await save_btn.click()
        await page.wait_for_timeout(5000)
    else:
        # DO NOT click if text contains "complete" or "submit"
        raise SafetyError("Button is not Save - aborting")
```

---

## Visual Verification Pattern

After each critical step, use **Qwen 3.5 Plus** to verify screenshot:

```python
await page.screenshot(path='/tmp/ktu_step.png')

# Spawn Qwen 3.5 Plus for verification
sessions_spawn(
    model='bailian/qwen3.5-plus',
    task='Analyze /tmp/ktu_step.png - verify X, Y, Z...',
    mode='run'
)
```

**Verification checkpoints:**
1. After login → Dashboard visible?
2. After Search → Course table loaded with correct rows?
3. After clicking Attendance/Internals → Student table visible with input fields?
4. After data entry → Values filled correctly?
5. After Save → Status shows "Saved-Not Submitted"?

---

## Complete Script Template

See: `scripts/ktu_attendance_entry.py` (reference implementation)

Key features:
- CSV parsing with reg number normalization
- Robust table detection (handles no tbody, AJAX loading)
- Safety checks to prevent accidental submit
- Screenshot at each step for debugging
- Detailed logging and error handling

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
| 2 | M.Tech |

### Program Type (`#programType`)
| Value | Type |
|-------|------|
| 1 | Full Time |
| 2 | Part Time |
| 3 | PhD |
| 4 | Working Professionals |

### Semester Type (`#semesterType`)
| Value | Type |
|-------|------|
| 1 | Odd |
| 2 | Even |

---

## Known Issues & Solutions

### Issue 1: Table doesn't load after Search
**Cause:** AJAX delay, filters not set correctly
**Solution:** Add longer wait (8+ seconds), verify filter values are correct

### Issue 2: Student reg numbers not matching CSV
**Cause:** LNSS21CS065 vs LNSS22CS065 variation for lateral entry
**Solution:** Normalize reg numbers - replace LNSS21CS with LNSS22CS

### Issue 3: Multiple input fields per row
**Cause:** Each row has ~23 inputs (including hidden, checkboxes)
**Solution:** Filter for `input[type="number"]` only, skip other types

### Issue 4: Save button not found
**Cause:** Many modal buttons on page (59+)
**Solution:** Use specific selector: `button.btn-primary:has-text("Save")`

---

## Output

- **Screenshots:** `/tmp/ktu_step*.png` for each stage
- **Log:** Printed to console with step-by-step progress
- **Result:** Data saved to KTU with status "Saved-Not Submitted"

---

## Related Skills

- **etlab-attendance:** Daily attendance from NSSCE ETLab (nssce.etlab.in)
- **ktu-activity-points:** Activity points download from KTU

---

## Changelog

- **2026-04-11:** Created skill based on live automation session with CST428
- Verified all selectors and structures using Qwen 3.5 Plus visual analysis