# DAY 62: FRIDAY - Slack & Telegram Bots
**Week:** 9 — Real-World Tools (Part 1)  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to receive and respond to messages from a Slack app and a Telegram bot
- How to route slash-commands/bot-commands to different logic branches
- How to generate AI-powered responses instead of hardcoded replies
- How to log every bot interaction for later reporting

## 🎥 Watch First
No dedicated video link is provided for this lesson in the course materials — treat this as a hands-on build day, and cross-reference the [n8n Beginner Course (1/9)](https://www.youtube.com/watch?v=4BVTkqbn_tY) if you need a refresher on webhook trigger basics before starting.

## 🛠️ Build It: Step-by-Step
1. Create a Slack app at api.slack.com, add bot permissions (`chat:write`, `channels:read`), install it to a workspace, and connect it in n8n (reuse your Day 58 credential if already set up).
2. Build a workflow with a Webhook trigger that receives Slack events, extracts `user_id`, `channel_id`, and `message_text`, and sends the text to an OpenAI node to determine intent.
3. Add a second OpenAI node (or extend the first) to generate a friendly, on-brand response, then send it back via the **Slack** node's "Post Message" operation, threaded to the original message.
4. Create a Telegram bot via BotFather, get its token, and connect it in n8n as a Telegram credential.
5. Build a Telegram workflow that checks whether an incoming message starts with `/` (a command) using an IF node, and routes `/start`, `/help`, and `/report` to different response branches with a Switch node.
6. Implement the `/report` command to call an OpenAI node that generates a short status summary, then sends it back via the Telegram node.
7. Log every bot interaction (platform, user, message, response) to an Airtable table so you have a record for client reporting later.
8. Test both bots with real messages, including at least one command and one free-text question, and confirm responses arrive within a few seconds.

## 🔑 Credentials Needed
- Slack credential (from Day 58, or newly created bot-scoped app)
- Telegram bot token (new — create via BotFather)
- OpenAI credential (from Day 58)
- Airtable credential (from Day 58)

## ✅ Definition of Done
- [ ] A Slack bot that responds to a real message in a channel with an AI-generated reply
- [ ] A Telegram bot that responds correctly to `/start`, `/help`, and at least one free-text message
- [ ] Every interaction (both platforms) is logged to Airtable with user, message, and response
- [ ] You tested both bots live, not just by executing the workflow manually with sample JSON

## 🐛 Common Pitfalls
- Slack requires you to respond to the initial event challenge/verification during webhook setup, or the app install will fail silently
- Telegram commands are case-sensitive and must match exactly (`/Start` ≠ `/start`) — normalize input text before routing
- Sending AI responses with no length limit can exceed Slack/Telegram message size limits or feel overwhelming to the user — cap response length in your prompt

## 🏭 Industry Track Application
Client-facing bots are a common productized deliverable. A logistics track might build a Telegram bot that gives drivers/dispatchers real-time delivery status on request; a fintech track might build a Slack bot for internal fraud-alert triage; a marketing track might build a bot that answers common client FAQ via Slack. Design today's `/report` command around a report your industry's clients would actually ask for.
