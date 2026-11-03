# Google Play reviewer account — drpreetha.com app

Created 2026-11-03 for Google Play review of **Dr. Preetha PSC Practice** (`com.drpreetha.kpsc`).

- **Email:** drpreetha.reviewer@gmail.com
- **Password:** Kapuma@23
- **Name on account:** Preetha App Reviewer
- **Birthday / gender (Google signup only):** 14 March 1992 · Rather not say
- **Recovery email:** kiranvk2011@gmail.com
- **Phone verification:** done by Kiran via QR on his phone
- **2-step verification:** OFF (reviewers must be able to sign in from Google's devices)
- **Selfie:** skipped

## On drpreetha.com
- users.id **150** (created on first Google sign-in, 2026-11-03)
- plan_subscriptions: **yearly**, approved, ₹0, reviewed_by `hermes`, valid 2026-11-03 → 2027-11-03, note "Google Play app reviewer account (no payment)"
- Not one of the 29 closed-test testers.

## Where it is used
- Play Console → App content → **Sign in details** (App access): email + password + note "Tap Continue with Google and choose this account".
- Play Console URL: https://play.google.com/console/u/4/developers/6226695448324030911/app/4974705903362418715/app-content/testing-credentials

## Removing it later
1. drpreetha DB: set its plan_subscriptions row to `status='expired'` (or delete user 150).
2. Delete the Google account at https://myaccount.google.com/delete-services-or-account while signed in as it.
3. Remove the credentials from Play Console App access (only after the app is approved and no review is pending).
