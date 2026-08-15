# DAY 14: Foundation Review & Project
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to combine multiple triggers, validation, an external integration, and error handling into one coherent workflow
- How to branch a single workflow into two independent integration paths based on a condition
- How to confirm an end-to-end system works by deliberately testing both its success and failure paths
- How to summarize what a workflow does in documentation someone else could follow

## 🎥 Watch First
- [n8n Foundation Summary & Best Practices](https://www.youtube.com/watch?v=4cQWJViybAQ) — Select the relevant 15 minutes for foundation review. Watch specifically for how the moving pieces from Weeks 1-2 (triggers, HTTP Request, IF, error handling) combine into a single real workflow, since that's exactly today's task.

## 🛠️ Build It: Step-by-Step
1. New workflow. Add a **Webhook Trigger** (path `foundation-project`) — this is your primary input path for today's capstone.
2. Add **IF** node "Data Validation": String `{{ $json.data }}` is not empty.
3. On true, add **Set** node "Process Data": `processed_data` = `{{ $json.data.trim().toUpperCase() }}`, `processed_at` = `{{ $now }}`, `status` = `processed`.
4. Add **HTTP Request** node "API Integration": Method `POST`, URL `https://jsonplaceholder.typicode.com/posts` (stand-in external service), Body Content Type JSON, Body = `{{ { "data": $json.processed_data, "timestamp": $json.processed_at } } }}`, Options → Retry On Fail = 3 tries.
5. Add **IF** node "Handle API Errors": Number `{{ $json.statusCode }}` ≥ 400. (jsonplaceholder always returns 201, so to actually exercise this branch, temporarily point the URL at `https://httpbin.org/status/500`, confirm the branch fires, then switch it back.)
6. On the error branch, add **Set** node "Log Error" (`error_type`, `error_message`, `error_time`) feeding a **Slack/Telegram** node "Send Error Notification". On the success branch, add **Set** node "Log Success" feeding a **Slack/Telegram** node "Send Success Notification".
7. On the Data Validation IF node's false branch, add a **Respond to Webhook** returning a 400 with `{{ { "status": "error", "message": "Missing data field" } } }}`.
8. Activate the workflow and test all three paths independently:
   - Valid data: `curl -X POST <url> -d '{"data":"foundation project test"}'` → confirm a success notification arrives.
   - Missing data: `curl -X POST <url> -d '{}'` → confirm a 400 JSON response and no notification.
   - Forced API failure: temporarily swap the HTTP Request URL to the 500 endpoint, resend valid data, confirm the error notification arrives instead, then swap the URL back.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/advanced_foundation_skills_assessment.json` (Menu → Import from File in n8n) to see a working version of a webhook → validate → branch → two-integration-path structure, then compare it to what you built.

## 🔑 Credentials Needed
Slack API credential or Telegram Bot credential (reused from Day 11) for success/error notifications.

## ✅ Definition of Done
- [ ] A valid-data curl request produces a success notification in Slack/Telegram
- [ ] A missing-data curl request produces a 400 JSON response and no notification
- [ ] A forced API failure (via the swapped URL) produces an error notification, distinct in wording from the success one
- [ ] You've written a short (3-5 sentence) description of what this workflow does and saved or posted it as documentation
- [ ] You can point to which specific node corresponds to each of: a trigger, validation, an external integration, error handling, and a notification

## 🐛 Common Pitfalls
- **Forgetting to swap the URL back:** leaving the HTTP Request node pointed at the always-500 test URL after verifying the failure path means your "working" automation silently fails from then on.
- **Identical-looking notifications:** if the success and error Slack/Telegram messages look the same at a glance, the notification isn't actually useful for debugging later — make the wording and emoji clearly distinct.
- **Stopping at "it ran once":** the Definition of Done above requires exercising all three paths (success, validation failure, API failure) independently, not just the happy path.

## 🏭 Industry Track Application
This capstone is Sarah's production-ready digital life automation system: one workflow that accepts input, validates it, calls an external service, handles that service failing, and tells her what happened either way. Before moving to Week 3, write one paragraph (for your own notes or a community post) naming which specific piece of your Week 1-2 work — the photo organizer, the expense tracker, or something else — this exact pattern would now protect in production, and what still needs to change (real auth, a real API instead of jsonplaceholder, a real destination sheet/database) before it actually ships.
