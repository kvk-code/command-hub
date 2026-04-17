---
description: "Create Gmail drafts with attachments using gws CLI. Use when user wants to draft an email, save email to drafts, or prepare an email for later review. Triggers on phrases like 'create draft', 'save as draft', 'draft email', 'gmail draft'."
---

# Gmail Draft Skill

Create Gmail drafts with attachments using the gws CLI wrapper.

## ⚠️ IMPORTANT

**ALWAYS use `/data/.openclaw/bin/gws` for Gmail operations.**

Do NOT use Python google-api-python-client directly. gws CLI is the priority.

## Prerequisites

- Token with Gmail scopes (`gmail.compose`, `gmail.readonly`, `gmail.send`, `gmail.modify`) — authorized 2026-04-01
- Account: kiranvk@nssce.ac.in
- Wrapper: `/data/.openclaw/bin/gws` (auto-refreshes token)

## Quick Commands

### Check Gmail Access
```bash
/data/.openclaw/bin/gws gmail users getProfile --params '{"userId": "me"}'
```

### List Drafts
```bash
/data/.openclaw/bin/gws gmail users drafts list --params '{"userId": "me"}'
```

### Create Draft (Simple)
```bash
/data/.openclaw/bin/gws gmail users drafts create \
  --params '{"userId": "me"}' \
  --json '{"message": {"raw": "BASE64_ENCODED_MESSAGE"}}'
```

## Helper Script

For complex drafts with attachments, use:
```
/data/.openclaw/workspace-critical/scripts/gmail_draft_gws.py
```

Usage:
```bash
python3 /data/.openclaw/workspace-critical/scripts/gmail_draft_gws.py \
  "recipient@example.com" \
  "Subject Line" \
  "Email body text here" \
  "/path/to/attachment1.pdf" \
  "/path/to/attachment2.docx"
```

## Message Encoding

The raw message must be base64url-encoded RFC 2822 message:

```python
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Subject'
msg.attach(MIMEText('Body text', 'plain'))

# Add attachment
with open('file.pdf', 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="file.pdf"')
msg.attach(part)

# Encode for Gmail API
raw = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
```

## gws CLI Reference

Full documentation: `/data/.openclaw/shared/command-hub/openclaw/docs/gws-cli.md`

### Schema Discovery
```bash
# See what parameters a method accepts
gws schema gmail.users.drafts.create
```

## Troubleshooting

### "Insufficient authentication scopes"
- Token may have lost Gmail scopes during a Classroom-only re-auth
- See re-authorization protocol in `/data/.openclaw/shared/command-hub/openclaw/docs/gws-cli.md`
- **redirect_uri MUST be `http://localhost`** (not localhost:1 or urn:ietf:wg:oauth:2.0:oob)
- Always re-authorize with ALL 29 scopes, not just the missing ones

### "Invalid client_secret.json format"
- Fixed by adding `project_id` field to `/data/.config/gws/client_secret.json`

## Token Info

- Location: `/data/.openclaw/config/google-classroom-tokens.json`
- Has 29 Google API scopes (re-authorized 2026-04-01) including full Gmail access
- Account: kiranvk@nssce.ac.in
- Wrapper auto-refreshes access token
- Full scope list & re-auth protocol: `/data/.openclaw/shared/command-hub/openclaw/docs/gws-cli.md`

## Email Encoding Best Practices

**CRITICAL:** When sending emails via gws CLI with `MIMEText`:

1. **Subject line: ASCII only.** Do NOT use em dashes (`\u2014`), curly quotes, or emojis in the subject. Use regular hyphens (`-`) instead. Gmail double-encodes Unicode in subjects, producing garbled text like `\u00c3\u0192\u00c2\u00a2`.
2. **Body: UTF-8 is fine.** Set `MIMEText(body, 'plain', 'utf-8')` for the body. Emojis and special characters work in the body.
3. **Example:**
```python
from email.mime.text import MIMEText
msg = MIMEText(body, 'plain', 'utf-8')  # UTF-8 body
msg['subject'] = 'Status Report - April 16, 2026'  # ASCII hyphens only
```