# DAY 11: Your First Real Automation
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to design a full pipeline: trigger → validate → transform → notify → log → respond
- How to send a formatted message via the Slack (or Telegram) node
- How to append a row to Google Sheets from workflow data using column mapping
- How to test an end-to-end automation with both realistic and deliberately-broken input

## 🎥 Watch First
- [n8n Quick Start: Build Workflow](https://www.youtube.com/watch?v=4cQWJViybAQ) — Complete 14m47s production automation tutorial. Watch for how the presenter chains a trigger to a notification step and tests the whole thing live before calling it done.

## 🛠️ Build It: Step-by-Step
1. New workflow. Add a **Webhook** node "Form Submission Webhook" — Method `POST`, Path `form-submission`.
2. Add **IF** node "Validate Form Data": String conditions `{{ $json.name }}` is not empty AND `{{ $json.email }}` is not empty.
3. On the true branch, add **Set** node "Process Form Data": `submission_id` = `{{ $now.format('YYYYMMDDHHmmss') }}`, `processed_name` = `{{ $json.name.trim() }}`, `processed_email` = `{{ $json.email.toLowerCase().trim() }}`, `processed_message` = `{{ $json.message || 'No message provided' }}`, `submitted_at` = `{{ $now }}`.
4. Add **Set** node "Format Notification": `notification_message` = `*Name:* {{ $json.processed_name }}\n*Email:* {{ $json.processed_email }}\n*Message:* {{ $json.processed_message }}`.
5. Add a **Slack** (or **Telegram**) node "Send Notification": connect your credential, set the channel/chat, Text = `{{ $json.notification_message }}`.
6. Add a **Google Sheets** node "Log to Sheet": operation Append, pick your spreadsheet/sheet, map columns to `submission_id`, `processed_name`, `processed_email`, `processed_message`, `submitted_at`.
7. Add a **Respond to Webhook** node returning `{{ { "status": "success", "submission_id": $json.submission_id } } }}`. On the IF node's false branch, add a second Respond to Webhook returning `{{ { "status": "error", "message": "Invalid form data" } } }}`.
8. Activate the workflow. Test the full path:
   `curl -X POST <production-url> -H "Content-Type: application/json" -d '{"name":"Jane Doe","email":"jane@example.com","message":"Testing my automation"}'`
   Confirm: (a) curl gets back `{"status":"success",...}`, (b) a real message arrives in your Slack/Telegram, (c) a new row appears in your Google Sheet.
9. Now test the failure path: `curl -X POST <production-url> -H "Content-Type: application/json" -d '{"name":"Jane Doe"}'` (missing email) and confirm you get back the error JSON with no notification sent and no sheet row created.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/form_processing_workflow.json` (Menu → Import from File in n8n) to see a working version of this exact validate → process → notify → respond pipeline, then compare it to what you built.

## 🔑 Credentials Needed
Slack API credential (or Telegram Bot credential) for notifications; Google Sheets OAuth2 credential for logging.

## ✅ Definition of Done
- [ ] A curl POST with valid name+email produces a success JSON response, a real Slack/Telegram message, and a new Google Sheets row — all three
- [ ] A curl POST missing a required field produces the error JSON response and creates no notification or sheet row
- [ ] Your Google Sheet has at least one real row you can trace back to a specific curl test you ran
- [ ] You can point to the exact node where invalid data gets rejected and explain why

## 🐛 Common Pitfalls
- **Silent column mismatch:** if your sheet's header row doesn't match your mapping mode, data lands in the wrong columns — open the sheet after testing and visually confirm each column, don't just trust "success."
- **Credential scoped wrong:** a Slack/Telegram credential pointed at the wrong workspace, or a bot not invited to the channel, lets the node execute without error while the message never appears — check the channel directly, not just the execution status.
- **Missing the false branch:** without the IF node's false branch, invalid submissions either silently get processed anyway or the workflow errors out at the Set node when `$json.email` is undefined.

## 🏭 Industry Track Application
Sarah wants this exact pipeline for expense processing with smart notifications. Duplicate today's workflow and swap the form fields for `expense_amount`, `expense_category`, and `expense_date`; add a validation rule that also rejects amounts ≤ 0; change the notification text to `💰 New Expense: {{ category }} — ${{ amount }} on {{ date }}`. Test with one valid expense and one with a negative amount, and confirm the negative one is rejected the same way the missing-email case was.
