#!/usr/bin/env python3
"""
KTU Internals/Attendance Upload — Tutor View Status Check
Checks which faculty have submitted internals for S8 CSE 2022 batch.

Output: Formatted table + JSON at /tmp/ktu_internals_status.json
Screenshots: /tmp/ktu_tv_*.png
"""
import asyncio
import json
import os
import sys

# Credentials are loaded from environment variables to avoid committing secrets.
USERNAME = os.getenv('KTU_TUTOR_USERNAME', '')
PASSWORD = os.getenv('KTU_TUTOR_PASSWORD', '')

# Browser
CHROMIUM = '/data/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'

# Default filters for S8 CSE 2022 batch
FILTERS = {
    'academicYearId': {'value': '96', 'label': '2025-2026'},
    'programId': {'text_match': 'B.Tech'},
    'programType': {'value': '1', 'label': 'Full Time'},
    'semesterId': {'text_match': 'S8'},
    'registrationAllowedStudentStatus': {'value': '1', 'label': 'Regular Students'},
    'batch': {'text_match': ['COMPUTER SCIENCE', '2022']},
    'degreeType': {'value': '1', 'label': 'Regular'},
}


async def select_by_text(page, selector_id, match_texts):
    """Select dropdown option by matching text content."""
    sel = page.locator(f'#{selector_id}')
    if await sel.count() == 0:
        print(f"  ⚠ Select #{selector_id} not found")
        return False

    if isinstance(match_texts, str):
        match_texts = [match_texts]

    options = await sel.locator('option').all()
    for opt in options:
        text = (await opt.text_content() or '').strip()
        val = await opt.get_attribute('value')
        if all(m in text for m in match_texts):
            await sel.select_option(value=val)
            print(f"  ✓ #{selector_id}: {text} (val={val})")
            await asyncio.sleep(1.5)
            return True

    print(f"  ⚠ #{selector_id}: no match for {match_texts}")
    return False


async def select_by_value(page, selector_id, value, label=''):
    """Select dropdown option by value."""
    sel = page.locator(f'#{selector_id}')
    if await sel.count() == 0:
        print(f"  ⚠ Select #{selector_id} not found")
        return False

    await sel.select_option(value=value)
    print(f"  ✓ #{selector_id}: {label} (val={value})")
    await asyncio.sleep(1.5)
    return True


async def main():
    from playwright.async_api import async_playwright

    if not USERNAME or not PASSWORD:
        print('Missing KTU_TUTOR_USERNAME or KTU_TUTOR_PASSWORD environment variables')
        sys.exit(1)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=CHROMIUM,
            headless=True,
            args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
        )
        ctx = await browser.new_context(viewport={'width': 1280, 'height': 900})
        page = await ctx.new_page()

        # Step 1: Login
        print("1. Logging in...")
        await page.goto('https://app.ktu.edu.in/login.htm', wait_until='networkidle', timeout=60000)
        await page.fill('#login-username', USERNAME)
        await page.fill('#login-password', PASSWORD)
        await page.click('#btn-login')
        await page.wait_for_load_state('networkidle', timeout=30000)
        await asyncio.sleep(2)

        if 'dashboard' not in page.url and 'home' not in page.url:
            await page.screenshot(path='/tmp/ktu_tv_login_fail.png')
            print("  ✗ Login may have failed")
            await browser.close()
            return

        print("  ✓ Logged in")

        # Step 2: Navigate via Exam → Advisor's Batches
        print("2. Navigating to Advisor's Batches...")

        # Click Exam tab
        exam_link = page.locator('a[href="/eu/exm/viewObserverAttendanceListing.htm"]')
        if await exam_link.count() > 0:
            await exam_link.first.click()
        else:
            await page.click('text=Exam')
        await page.wait_for_load_state('networkidle', timeout=15000)
        await asyncio.sleep(1)

        # Click Advisor's Batches
        advisor_link = page.locator('a[href="/eu/exm/staffAdvisorBatches.htm"]')
        if await advisor_link.count() > 0:
            await advisor_link.first.click()
        else:
            await page.click('text=Advisor')
        await page.wait_for_load_state('networkidle', timeout=15000)
        await asyncio.sleep(2)

        print(f"  ✓ URL: {page.url}")
        await page.screenshot(path='/tmp/ktu_tv_page.png')

        # Step 3: Set filters
        print("3. Setting filters...")

        await select_by_value(page, 'academicYearId', '96', '2025-2026')
        await select_by_text(page, 'programId', 'B.Tech')
        await select_by_value(page, 'programType', '1', 'Full Time')
        await select_by_text(page, 'semesterId', 'S8')
        await select_by_value(page, 'registrationAllowedStudentStatus', '1', 'Regular Students')
        await select_by_text(page, 'batch', ['COMPUTER SCIENCE', '2022'])
        await select_by_value(page, 'degreeType', '1', 'Regular')

        await page.screenshot(path='/tmp/ktu_tv_filters.png')

        # Step 4: Search
        print("4. Searching...")
        search_btn = page.locator('button:has-text("Search")')
        if await search_btn.count() > 0:
            await search_btn.first.click()
        await page.wait_for_load_state('networkidle', timeout=30000)
        await asyncio.sleep(3)

        await page.screenshot(path='/tmp/ktu_tv_results.png')

        # Also take a tight screenshot of just the results table for visual analysis
        try:
            table_el = None
            for t in await page.query_selector_all('table'):
                header = await t.text_content()
                if 'Course' in header:
                    table_el = t
                    break
            if table_el:
                await table_el.screenshot(path='/tmp/ktu_tv_table_only.png')
                print('  Table screenshot saved: /tmp/ktu_tv_table_only.png')
        except Exception as e:
            print(f'  Table screenshot failed: {e}')

        # Step 5: Extract results
        print("5. Extracting results...")
        results = []

        tables = await page.query_selector_all('table')
        for table in tables:
            rows = await table.query_selector_all('tr')
            if len(rows) < 2:
                continue

            header = await rows[0].text_content()
            if 'Course' not in header:
                continue

            print(f"  Found table with {len(rows) - 1} course rows")

            for row in rows[1:]:
                cells = await row.query_selector_all('td')
                if len(cells) < 5:
                    continue

                texts = []
                for c in cells:
                    t = await c.text_content()
                    texts.append(t.strip() if t else '')

                # Check Action column for Export buttons
                action_cell = cells[-1]  # Last column = Action
                action_html = await action_cell.inner_html()
                action_text = await action_cell.text_content() or ''
                has_export = 'Export' in action_text or 'export' in action_html.lower()
                has_view = 'View' in action_text or 'Internals' in action_text

                status_text = texts[3]
                is_pending = 'Pending' in status_text
                is_submitted = 'Submitted' in status_text

                # Detect: pending but has Export = marks entered, not submitted
                if is_pending and has_export:
                    effective_status = 'Entered (not submitted)'
                elif is_submitted:
                    effective_status = 'Submitted by Faculty'
                else:
                    effective_status = status_text

                results.append({
                    'course': texts[0],
                    'slot': texts[1],
                    'faculty': texts[2],
                    'status': status_text,
                    'effective_status': effective_status,
                    'has_export': has_export,
                    'batch': texts[4] if len(texts) > 4 else '',
                })
            break  # Found the right table

        # Output
        print()
        print('=' * 70)
        print('INTERNALS UPLOAD STATUS — S8 CSE 2022 Batch')
        print('=' * 70)

        submitted = 0
        pending = 0

        entered_not_submitted = 0

        if results:
            for r in results:
                eff = r.get('effective_status', r['status'])
                if 'Submitted' in eff:
                    emoji = '✅'
                    submitted += 1
                elif 'Entered' in eff:
                    emoji = '⚡'
                    entered_not_submitted += 1
                else:
                    emoji = '⏳'
                    pending += 1

                export_note = ''
                if r.get('has_export') and 'Pending' in r['status']:
                    export_note = ' [Export available — marks entered but NOT submitted]'

                print(f"{emoji} {r['course']}")
                print(f"   Faculty: {r['faculty']}")
                print(f"   Status:  {r['status']}{export_note}")
                print(f"   Effective: {eff}")
                print()

            if entered_not_submitted > 0:
                print(f"Summary: {submitted} submitted, {entered_not_submitted} entered (not submitted), {pending} pending, {len(results)} total")
            else:
                print(f"Summary: {submitted} submitted, {pending} pending, {len(results)} total")

            # Save JSON
            with open('/tmp/ktu_internals_status.json', 'w') as f:
                json.dump({
                    'timestamp': __import__('datetime').datetime.now().isoformat(),
                    'courses': results,
                    'summary': {
                        'submitted': submitted,
                        'entered_not_submitted': entered_not_submitted,
                        'pending': pending,
                        'total': len(results)
                    }
                }, f, indent=2)
            print("\nJSON saved: /tmp/ktu_internals_status.json")
        else:
            print("No results found. Check screenshots.")

        await page.screenshot(path='/tmp/ktu_tv_final.png', full_page=True)
        await browser.close()
        print("\nDone.")


if __name__ == '__main__':
    asyncio.run(main())
