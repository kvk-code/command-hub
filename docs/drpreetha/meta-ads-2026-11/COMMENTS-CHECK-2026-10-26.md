# Meta ad/post comments check + API block, 26 Oct 2026 (Hermes Forum topic 14266, pkd11)

## Findings
- **Only one comment across FB + IG.** Ibnu Nasir, "Enna exam" (Manglish: "which/when exam?"), ~11:52 IST 26 Oct, on the
  FB ad post of `features IG | cat34-2026` ("KPSC Assistant Surgeon / CMO exam on 12 November. 913 real past KPSC questions…",
  story 849346781603237_122150785059140732). Unreplied. Draft reply proposed, NOT posted (awaiting Kiran):
  "Kerala PSC Assistant Surgeon / Casualty Medical Officer exam, 12 November 2026. You can try 10 real past questions free at drpreetha.com/free (no login needed)."
- Per-ad (insights date_preset=maximum, 22:10 IST):
  - features IG [ACTIVE] ₹262.33, 1,672 impr, comment 1, reaction 1
  - features [PAUSED] ₹32.93, 303 impr, 0 comments
  - igwa indicf5 v1 [ACTIVE] no spend yet; IG media 17880462564651777 comments_count 0
  - stamp / explore / quiz [PAUSED] never spent
  - old "Promoting Website: sample-quiz.php" [CAMPAIGN_PAUSED] ₹301.89, 15,917 impr, 27 reactions, 0 comments (FB + IG media 18062505032626986)
- Business Suite IG comments inbox: "No comments". @drpreetha.ms 0 followers; FB Page 5 followers.

## Incident: "API access blocked" (transient)
- ~21:50 IST every Graph call (system-user token, app drpreetha-ads-api 2205623319995197) returned
  `OAuthException code 200 "API access blocked."`. neko-preetha had a tab on developers.facebook.com/r/user/error/:
  "Account confirmation needed — We've noticed unusual activity on this developer account. Please complete the confirmation steps to regain access." [Confirm Account] (account Preetha M S).
- Nothing clicked by the agent (owner-only checkpoint).
- By 22:10 IST (16:40 UTC) the same token worked again: debug_token is_valid, expires 2026-12-24, account_status 1. Unknown whether
  someone pressed Confirm or Meta lifted it. If it recurs: owner presses Confirm Account in neko-preetha; daily 21:00 report would fail meanwhile.

## Gaps / lessons
- Token can COUNT FB comments (insights `actions.comment`) but cannot READ them: `/<story>/comments` needs `pages_read_user_content`
  (page token) — system-user token returns "Invalid OAuth 2.0 Access Token". Read text in Business Suite inbox (Facebook comments tab) until the permission is added.
- `features IG` creative has no `effective_instagram_media_id` via API, so IG comments on it can't be checked by API.
- Fast comment sweep: Business Suite Home "To-do → Comments" + inbox tabs `/latest/inbox/facebook|instagram?asset_id=849346781603237&business_id=1300457372100054&mailbox_id=849346781603237` (CDP screenshot + vision; no clicks needed).
- Ads Manager in neko may redirect to the developers error page when the checkpoint is active — check `/json/list` tab URLs first.
