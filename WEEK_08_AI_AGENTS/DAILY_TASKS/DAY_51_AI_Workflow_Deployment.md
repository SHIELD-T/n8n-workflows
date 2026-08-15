# DAY 51: AI Workflow Deployment
**Week:** 8 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to move an AI workflow from manual/test execution to an always-on production webhook
- The difference between n8n's Test webhook URL and Production webhook URL, and why mixing them up is the #1 deployment bug
- How to build explicit success/error response paths instead of relying on n8n's default auto-response

## 🎥 Watch First
- [How to Build AI Agents with n8n in 2025! (Full Course)](https://www.youtube.com/watch?v=geR9PeCuHK4) — jump to the "Deploying AI workflows" section; pay attention to how they flip the workflow to Active and what changes about the webhook URL at that moment.

## 🛠️ Build It: Step-by-Step
1. Open (or rebuild) your Day 50 "deployment candidate" workflow. Give it explicit error handling: check the workflow's Settings → Error Workflow, or add a dedicated error branch on any node that can fail.
2. In the trigger's Webhook node, confirm the path is unique and descriptive (e.g. `ai-agent-deploy-yourname`), set HTTP Method to POST, and set Respond to "Using Respond to Webhook Node" so you control the response shape yourself.
3. Toggle the workflow to **Active** (top-right switch). Copy the **Production URL** shown in the Webhook node — not the Test URL.
4. From a terminal, hit the production URL with curl: `curl -X POST https://<your-n8n-domain>/webhook/<path> -H "Content-Type: application/json" -d '{"scenario":"test deployment"}'` — confirm you get a 200 response with the JSON payload you expect, not a "workflow not active" error.
5. Add a **Respond to Webhook** node at the end of the success path returning `{"status":"deployed","workflow":"<name>"}`, and a separate one on the error path returning Response Code 500 with a distinct error message.
6. Re-run the curl test with a deliberately malformed body (e.g. missing a required field) and confirm the error path triggers, returning your 500 response instead of a silent hang or a false 200.
7. Write a short deployment record: production URL (redact before sharing publicly), activation date, and rollback plan — exactly how you'd deactivate or revert this workflow if it misbehaves.

**Stuck?** Import `WEEK_08_AI_AGENTS/EXAMPLES/ai_workflow_orchestration_system.json` (Menu → Import from File in n8n) to see a working webhook-triggered, multi-step production workflow with success/error branches, then compare it to what you built.

## 🔑 Credentials Needed
Your AI provider credential (OpenAI or similar) already configured from Week 7. No new credentials unless your workflow calls a new external API.

## ✅ Definition of Done
- [ ] Workflow is toggled Active and the **production** webhook URL responds with 200 to a valid curl POST
- [ ] A deliberately malformed request triggers the error path and returns a non-200 status
- [ ] The workflow has an explicit Respond to Webhook node, not the default auto-response
- [ ] You have a written rollback note describing how to deactivate/revert the deployed workflow

## 🐛 Common Pitfalls
- **Testing against the Test URL:** it only listens while the editor is open and the workflow isn't active — always copy the Production URL after activating.
- **No explicit response node:** n8n's default webhook response can return before your AI node finishes, so callers get an empty or premature response.
- **No error branch:** an unhandled exception in an HTTP Request or AI node just shows as a failed execution in the n8n UI, with zero signal to whatever called the webhook.

## 🏭 Industry Track Application
Deploy your chosen workflow with a webhook path name that reflects your industry track (e.g. `/webhook/fintech-fraud-check`, `/webhook/healthtech-triage-agent`), and note in your deployment record which single point of failure would matter most to a real client in that industry if this webhook went down.
