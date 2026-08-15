# DAY 6: Your First Real Automation
**Week:** 1 — Foundation  |  **Time:** 3-4 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to design an end-to-end automation before building it (trigger → process → action)
- How to connect a Google Form to n8n via webhook
- How to create a Telegram bot and send it messages from a workflow
- How to format dynamic data into a readable notification message

## 🎥 Watch First
- [Build Your First Workflow: n8n Quick Start](https://www.youtube.com/watch?v=4cQWJViybAQ) — full 14m47s tutorial. Pay attention to how the instructor formats the outgoing message using expressions that reference multiple upstream fields at once.

## 🛠️ Build It: Step-by-Step
1. Create a Google Form with fields: Name, Email, Message. In Google Forms, go to the responses spreadsheet (or use a form-to-webhook connector/Apps Script) so submissions can reach an external URL — alternatively, simulate this by sending curl requests shaped like form data if you don't want to configure Google Apps Script today.
2. In n8n, create a new workflow with a **Webhook** node (path: `google-form-submission`, method POST). Activate the workflow and copy the production webhook URL.
3. Message **@BotFather** on Telegram, run `/newbot`, follow the prompts, and copy the bot token it gives you.
4. In n8n, add **Telegram** credentials (Credentials → New → Telegram API) and paste your bot token. Start a chat with your new bot in Telegram first (bots can't message you until you've messaged them).
5. Add a Set node after the Webhook to normalize incoming fields: `name = {{ $json.name || 'Anonymous' }}`, `email = {{ $json.email || 'No email provided' }}`, `message = {{ $json.message || 'No message provided' }}`, `submitted_at = {{ $now }}`.
6. Add a second Set node that builds the Telegram text: `telegram_message` combining name/email/message/timestamp with line breaks (`\n`) and Markdown bold (`*Name:*`).
7. Add a **Telegram** node (operation: Send Message), select your credential, set Chat ID (your own chat ID from the bot conversation), Text = `{{ $json.telegram_message }}`, Parse Mode = Markdown.
8. Test end-to-end: send a curl POST to your webhook URL with `name`, `email`, `message` fields and confirm the formatted message arrives in your Telegram chat within a few seconds.

**Stuck?** Import `WEEK_01_FOUNDATION/EXAMPLES/webhook_processing_workflow.json` (Menu → Import from File) to see a working webhook-to-notification pattern, then compare it to your Telegram flow.

## 🔑 Credentials Needed
- Telegram Bot API token (free, via @BotFather)
- (Optional) Google account if wiring an actual Google Form rather than simulating with curl

## ✅ Definition of Done
- [ ] A curl POST to your production webhook URL results in a real Telegram message arriving in your chat within ~5 seconds
- [ ] The Telegram message correctly displays all three submitted fields (name, email, message) plus a timestamp
- [ ] Your workflow is Active (not just saved) so it responds outside the n8n editor
- [ ] You've tested at least one edge case — an empty field — and confirmed the fallback text ("Anonymous", "No message provided") appears instead of a blank or error

## 🐛 Common Pitfalls
- **Telegram "chat not found" error:** You must message your bot first before it can message you back — Telegram bots cannot initiate conversations.
- **Markdown parse errors:** Special characters like `_`, `*`, or `[` in user-submitted text can break Telegram's Markdown parser mid-message — for production use, consider Parse Mode "HTML" or escaping special characters.
- **Webhook not firing outside the editor:** Remember to click the workflow's Active toggle — the "Listen for Test Event" URL only works while the editor is open and listening.

## 🏭 Industry Track Application
Adapt the notification content for your industry track — e.g., Fintech: a payment-received Telegram alert with amount/sender/timestamp; HealthTech: an appointment-booked alert; EdTech: a course-enrollment alert. Swap the Google Form's fields and the Set-node formatting to match, then re-test end-to-end with a curl payload shaped like your industry's real data.
