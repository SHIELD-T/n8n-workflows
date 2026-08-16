# DAY 79: Creating Reusable Templates
**Week:** 12 — Scaling  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- What actually separates a "workflow" from a "template" — placeholders, documentation, and no hardcoded secrets
- How to design customization points so someone else can adapt your workflow without editing its core logic
- How to package a template with enough documentation that you (or a hire) can deploy it without re-explaining it

## 🎥 Watch First
[N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U)
Skim for any section on workflow organization or environment variables — that's the mechanism you'll use for the placeholder pattern below.

## 🛠️ Build It: Step-by-Step
1. Pick your best-performing workflow from anywhere in the course so far (lead gen, support bot, content pipeline — your choice).
2. Open it in n8n and replace every hardcoded value that's specific to one client/use-case (a Slack channel name, an email address, a spreadsheet ID) with an n8n **Set** node at the top called "Template Config" holding named variables like `{{TARGET_SHEET_ID}}`, `{{NOTIFY_CHANNEL}}`.
3. Update every downstream node to reference `$('Template Config').item.json.target_sheet_id` etc. instead of the hardcoded value, so changing the template only requires editing one node.
4. Add a **Sticky Note** at the top of the canvas listing exactly what to change before reuse, what credentials are required, and one sentence on what the workflow does.
5. Export the workflow as JSON (Download) and save it to your own templates folder — name the file descriptively (e.g. `lead_capture_template_v1.json`).
6. Import `WEEK_12_SCALING/EXAMPLES/workflow_template_management_system.json` and compare: does your template match its conventions (clear naming, sticky-note instructions, a defined set of customization variables)?
7. Write a 5-line "how to deploy this template" doc (in a Notion page, README, or plain text file) that names every variable to change and every credential to connect.

## 🔑 Credentials Needed
Whatever your chosen source workflow already uses (commonly Google Sheets/Airtable, Slack, and an email or CRM credential) — no new credentials required for templating itself.

## ✅ Definition of Done
- [ ] Your chosen workflow has zero hardcoded client-specific values left — all routed through one config Set node
- [ ] A Sticky Note documents what to change and what credentials are needed
- [ ] You exported the templated workflow as its own JSON file
- [ ] You compared it against `workflow_template_management_system.json` and can name one thing you did the same or differently

## 🐛 Common Pitfalls
- **"Template" that's really just a renamed copy** — if someone else would need to ask you five questions before running it, the templating isn't finished; the config Set node and Sticky Note are the actual deliverable.
- **Credentials baked into the exported JSON** — n8n excludes credential values from exports by default, but double-check no API key ended up typed directly into a URL or header field.
- **Config variables that don't actually get used everywhere** — after adding the config node, grep through every remaining node's parameters for the old hardcoded value to make sure you replaced all of them, not just the first one you noticed.

## 🏭 Industry Track Application
For a Real Estate track, your config variables would be things like `LISTING_SHEET_ID` and `AGENT_NOTIFY_CHANNEL`; for Healthcare, focus the Sticky Note on which fields carry PHI so a future deployer knows exactly what needs compliance review before reuse.
