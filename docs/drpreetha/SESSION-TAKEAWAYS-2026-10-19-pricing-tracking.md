# drpreetha.com — session takeaways, 19 Oct 2026 (pricing, upgrades, tracking, weekly insights)

## Shipped (live)
- **One price list** `pricing.php` (Monthly ₹299/30d/2 devices, Exam Pass ₹999/3 devices, Yearly ₹1,999/12m/3 devices). plans.php, subscribe.php, admin dashboard/approve, db_config, terms, refund, shipping all read from it. Quarterly/Lifetime/false "Save" labels removed.
- **Exam Pass end** = customer's exam date or 4 months, whichever earlier. Form asks exam name + date (required, Exam Pass only); stored in `plan_subscriptions.exam_details/exam_date`; admin card shows it with "check against KPSC notification".
- **Pro-rata upgrade credit**: credit = price paid × days left ÷ total days (rounded); computed server-side and stored (`list_price, upgrade_from_id, credit_amount, credit_calc`). Admin card: "UPGRADE — Why ₹X?" + amount-match check. On approval the old plan ends the day before. No cash refunds.
- **Refund/shipping/terms** rewritten to the real process (UPI, approval ≤24h, no auto-renew, 1-month free Exam Pass extension if KPSC postpones).
- **Tracking**: GA4 ecommerce (view_item_list, select_item, begin_checkout w/ value+credit, add_payment_info, payment_submitted, policy_view, free_sample_click); Pixel AddToCart + FreeSampleClick; Clarity tags page_type/plan_selected/is_upgrade/current_plan/identify + upgrade on payment. Verified by live network capture in neko-preetha.
- **GA4 key events**: payment_submitted, sign_up, begin_checkout (+ subscription_submitted).
- **MakeMeFamous**: Product JSON-LD with 3 Offers on subscribe.php, subscribe.php in sitemap, llms.txt plan/refund facts; IndexNow 200/200/202; GSC sitemap resubmitted.
- **Weekly insights** cron `8354dbbe555c` (Mon 09:00 IST, this thread): DB funnel (`drpreetha/weekly-insights/db_week.py`) + GA4 + Clarity + Pixel. One-off plan-click review `eff43c099a54` 2 Nov 10:00 IST.

## Lessons
- Weekly drafts built before a template change keep the old body when "sent from drafts" — the 19 Oct batch (6 subscribers, 09:10 IST) went out without the open pixel and with the "1 questions" bug. Rebuild drafts after any template change before Kiran sends.
- GA4 admin deep links redirect to Home; navigate Admin → Events → Recent events and click the star (`toggle key event status`).
- Test on the real flow with a test account; compute money server-side, never trust posted amounts.
- neko-preetha is fail-closed on the phone tunnel; page-designer Chrome is a fallback for visuals only. Close every tab opened (leave one).
- Test account kiranvk2011 (user 66) is excluded from report counts; restore its plan after e2e tests.

## Commits (openclaw_master)
3bacad4, 814dcfe, 920fdc6, 277dcda, 2d11077, 31246ae. Code+shots: `drpreetha/pricing-2026-10-19/`.
