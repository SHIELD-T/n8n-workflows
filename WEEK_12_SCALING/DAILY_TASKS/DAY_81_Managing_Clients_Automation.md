# DAY 81: Managing Clients with Automation
**Week:** 12 — Scaling  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to automate the repetitive parts of client management (status updates, FAQ answers) without losing the personal touch that keeps clients
- How to route a support message to a bot response vs. a real escalation based on real criteria, not guesswork
- How to build a recurring client report that pulls from real data instead of being written by hand each time

## 🎥 Watch First
[How I 100% Automated Long Form Content with n8n](https://www.youtube.com/watch?v=lF2bvXoV-Zg)
Watch for the pattern of "trigger → process → deliver on a schedule" — you'll reuse that exact shape for client reporting today.

## 🛠️ Build It: Step-by-Step
1. Build a workflow with a **Webhook** or **Email Trigger** node that receives an incoming client support message (subject + body).
2. Add an **OpenAI** node ("Classify Message") that categorizes the message into `faq`, `billing`, `technical_issue`, or `feature_request`, using a short list of your real FAQ topics in the prompt.
3. Add a **Switch** node keyed on that category. For `faq`, add an **OpenAI** node that answers using a system prompt containing your actual FAQ content (paste your real answers — not placeholders) and sends the reply via **Gmail**/**Slack**.
4. For the other three categories, add a **Slack** node that posts the message into the right internal channel for a human to handle — this is your escalation path.
5. Build a second workflow with a **Schedule Trigger** (weekly) that pulls real data from wherever your client's automation results live (Airtable, Google Sheets, or n8n's own Executions API) and generates a client-facing report: executions run, success rate, and one written observation via an **OpenAI** node.
6. Send that report via **Gmail** or **Slack** to a test address, and confirm it contains real numbers pulled from your data source, not filler text.
7. Import `WEEK_12_SCALING/EXAMPLES/scaling_operations_management.json` to compare how it structures escalation and reporting at scale.

## 🔑 Credentials Needed
OpenAI API key; Gmail or Email Trigger credential; Slack credential; Airtable/Google Sheets or n8n API credential for the reporting workflow.

## ✅ Definition of Done
- [ ] The classification step correctly routes at least one FAQ-type message to an automated reply and one other type to a human-escalation channel
- [ ] Your FAQ auto-reply uses real content you wrote, not generic placeholder answers
- [ ] The weekly report workflow pulls real numbers from a real data source
- [ ] You tested both workflows end-to-end with realistic sample input

## 🐛 Common Pitfalls
- **Auto-replying to everything, including things that need a human** — an automated FAQ bot that also tries to answer billing disputes will damage trust faster than no bot at all; keep the escalation categories genuinely routed to humans.
- **Reports with hardcoded or fake numbers** — a client-facing report that doesn't reflect real execution data is worse than no report; verify your data source query actually returns this week's real numbers.
- **No fallback when classification is uncertain** — add a default Switch branch that escalates to a human when the category doesn't clearly match any option, rather than guessing.

## 🏭 Industry Track Application
For a Professional Services track, the weekly report should speak in the client's terms (hours saved, tasks completed) rather than technical execution counts — translate the raw numbers into business language before sending.
