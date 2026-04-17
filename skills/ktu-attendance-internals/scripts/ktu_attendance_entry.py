#!/usr/bin/env python3
"""
KTU Attendance & Internals Entry — Reference Implementation
Automates the documented flow using Playwright with safety checks.

Usage:
    python ktu_attendance_entry.py --csv <path> --course <code> [--filters <json>]

Example:
    python ktu_attendance_entry.py \
        --csv /path/to/CST428_marks.csv \
        --course CST428 \
        --filters '{"academicYearId": "96", "semesterType": "2"}'
"""
import asyncio
import argparse
import csv
import re
import sys
from pathlib import Path

# Default credentials (should be loaded from secure storage)
USERNAME = 'KTU-F3938'
PASSWORD = 'Ktu@23_45'

# Browser paths
CHROMIUM_PATH = '/data/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'
LD_LIBRARY_PATH = '/data/.openclaw/browser-libs'

# Default filter values for S8 B.Tech 2025-26
DEFAULT_FILTERS = {
    'academicYearId': '96',      # 2025-2026
    'programId': '1',            # B.Tech
    'programType': '1',          # Full Time
    'semesterType': '2',         # Even
    'registrationAllowedStudentStatus': '1'  # Regular Students
}

def load_student_data(csv_path: str) -> dict:
    """Load CSV and return dict keyed by normalized reg number."""
    students = {}
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            reg_no = row.get('Register No', row.get('Reg No', '')).strip()
            att = row.get('Attendance Percentage', row.get('Attendance', '')).strip().replace('%', '')
            marks = row.get('Internal Marks', row.get('Marks', '')).strip()
            
            if not reg_no:
                continue
            
            # Store both original and normalized
            students[reg_no.upper()] = {'attendance': att, 'marks': marks}
            students[reg_no] = {'attendance': att, 'marks': marks}
            
            # Handle lateral entry variation
            if 'LNSS21CS' in reg_no:
                normalized = reg_no.replace('LNSS21CS', 'LNSS22CS')
                students[normalized.upper()] = {'attendance': att, 'marks': marks}
                students[normalized] = {'attendance': att, 'marks': marks}
    
    return students

async def wait_for_table(page, timeout: int = 15000) -> bool:
    """Wait for AJAX-loaded table to appear."""
    for _ in range(timeout // 500):
        tables = await page.query_selector_all('table')
        for table in tables:
            rows = await table.query_selector_all('tr')
            if len(rows) > 1:  # Has data rows
                return True
        await asyncio.sleep(0.5)
    return False

async def save_screenshot(page, name: str):
    """Save screenshot with consistent naming."""
    path = f'/tmp/ktu_{name}.png'
    await page.screenshot(path=path)
    print(f"  Screenshot: {path}")
    return path

async def main(csv_path: str, course_code: str, filters: dict = None):
    from playwright.async_api import async_playwright
    
    filters = filters or DEFAULT_FILTERS
    students = load_student_data(csv_path)
    print(f"Loaded {len(students)//2} students from CSV")
    
    if not students:
        print("ERROR: No student data in CSV")
        return False
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            executable_path=CHROMIUM_PATH,
            args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
        )
        page = await browser.new_page(viewport={'width': 1280, 'height': 900})
        
        try:
            # ===== STEP 1: LOGIN =====
            print("\nStep 1: Login...")
            await page.goto('https://app.ktu.edu.in/login.htm', wait_until='networkidle', timeout=60000)
            await page.fill('#login-username', USERNAME)
            await page.fill('#login-password', PASSWORD)
            await page.click('#btn-login')
            await page.wait_for_timeout(5000)
            
            if 'dashboard' not in page.url.lower():
                print("  ERROR: Login failed")
                await save_screenshot(page, 'login_failed')
                return False
            
            print(f"  Logged in: {page.url}")
            await save_screenshot(page, 'step1_login')
            
            # ===== STEP 2: FACULTY ASSIGNED =====
            print("\nStep 2: Faculty Assigned Courses...")
            await page.goto('https://app.ktu.edu.in/eu/ins/facultyAssigned.htm', wait_until='networkidle')
            await page.wait_for_timeout(3000)
            await save_screenshot(page, 'step2_faculty_assigned')
            
            # ===== STEP 3: FILTERS =====
            print("\nStep 3: Setting filters...")
            for selector, value in filters.items():
                await page.select_option(f'#{selector}', value=value)
                await page.wait_for_timeout(500)
                print(f"  {selector} = {value}")
            
            print("  Clicking Search...")
            await page.click('#facultyAssignedForm_search')
            await page.wait_for_timeout(8000)
            
            if not await wait_for_table(page):
                print("  ERROR: Course table not loaded")
                await save_screenshot(page, 'step3_no_table')
                return False
            
            await save_screenshot(page, 'step3_course_table')
            
            # ===== STEP 4: FIND COURSE =====
            print(f"\nStep 4: Finding {course_code}...")
            rows = await page.query_selector_all('tr')
            found = False
            
            for row in rows:
                text = await row.inner_text()
                if course_code in text:
                    print(f"  Found: {text[:80]}")
                    link = await row.query_selector('a:has-text("Attendance"), a:has-text("Internal")')
                    if link:
                        await link.click()
                        await page.wait_for_timeout(5000)
                        found = True
                        break
            
            if not found:
                print(f"  ERROR: {course_code} not found")
                await save_screenshot(page, 'step4_no_course')
                return False
            
            await save_screenshot(page, 'step4_student_page')
            print(f"  Student page: {page.url}")
            
            # ===== STEP 5: ENTER DATA =====
            print("\nStep 5: Entering attendance and marks...")
            await page.wait_for_timeout(5000)
            
            filled = 0
            skipped = []
            
            rows = await page.query_selector_all('tr')
            for row in rows:
                inputs = await row.query_selector_all('input[type="number"]')
                
                if len(inputs) < 2:
                    continue
                
                row_text = await row.inner_text()
                reg_match = re.search(r'(NSS|MAC|PKD|LNSS)\d*CS\d+', row_text, re.IGNORECASE)
                
                if not reg_match:
                    continue
                
                reg_no = reg_match.group(0).upper()
                
                # Normalize lateral entry
                if 'LNSS21CS' in reg_no:
                    reg_no = reg_no.replace('LNSS21CS', 'LNSS22CS')
                
                if reg_no not in students:
                    skipped.append(reg_no)
                    continue
                
                student = students[reg_no]
                
                try:
                    await inputs[0].fill(student['attendance'])
                    await inputs[1].fill(student['marks'])
                    filled += 1
                    if filled % 10 == 0:
                        print(f"    {filled} filled...")
                except Exception as e:
                    skipped.append(f"{reg_no}: {e}")
            
            print(f"\n  === RESULTS ===")
            print(f"  Filled: {filled}")
            print(f"  Skipped: {len(skipped)}")
            if skipped[:5]:
                for s in skipped[:5]:
                    print(f"    - {s}")
            
            await save_screenshot(page, 'step5_filled')
            
            # ===== STEP 6: SAVE =====
            print("\nStep 6: Clicking Save...")
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.wait_for_timeout(3000)
            
            # Find Save button with safety check
            buttons = await page.query_selector_all('button')
            save_btn = None
            
            for btn in buttons:
                text = await btn.inner_text()
                cls = await btn.get_attribute('class') or ''
                
                if text.strip().lower() == 'save' and 'btn-primary' in cls:
                    save_btn = btn
                    break
            
            if not save_btn:
                print("  ERROR: Save button not found!")
                print("  Buttons found:")
                for btn in buttons[:10]:
                    text = await btn.inner_text()
                    cls = await btn.get_attribute('class') or ''
                    print(f"    '{text.strip()}' [{cls[:30]}]")
                await save_screenshot(page, 'step6_no_save')
                return False
            
            # FINAL SAFETY CHECK
            text = await save_btn.inner_text()
            if 'complete' in text.lower() or 'submit' in text.lower():
                print("  ⚠️ SAFETY ABORT: Button is not Save!")
                return False
            
            print(f"  Clicking '{text.strip()}'...")
            await save_btn.click()
            await page.wait_for_timeout(5000)
            
            await save_screenshot(page, 'step6_saved')
            
            # Verify result
            content = await page.content()
            if 'saved' in content.lower() or 'success' in content.lower():
                print("  ✓ Save successful!")
            else:
                print("  Save status unclear - verify manually")
            
            print("\n===== COMPLETE =====")
            return True
            
        except Exception as e:
            print(f"ERROR: {e}")
            await save_screenshot(page, 'error')
            return False
        
        finally:
            await browser.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KTU Attendance & Internals Entry')
    parser.add_argument('--csv', required=True, help='Path to CSV file with student data')
    parser.add_argument('--course', required=True, help='Course code (e.g., CST428)')
    parser.add_argument('--filters', type=str, help='JSON string with custom filter values')
    
    args = parser.parse_args()
    
    filters = DEFAULT_FILTERS
    if args.filters:
        import json
        filters = json.loads(args.filters)
    
    success = asyncio.run(main(args.csv, args.course, filters))
    sys.exit(0 if success else 1)