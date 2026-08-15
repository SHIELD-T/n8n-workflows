# DAY 3: Understanding Triggers
**Week:** 1 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- The four core trigger types: Manual, Webhook, Schedule, and Event-based
- When to choose each trigger type for a given automation
- How to configure and test a Webhook trigger with a real HTTP request
- How Cron-style scheduling works in the Schedule Trigger node

## 🎥 Watch First
- [n8n Quick Start Tutorial: Build Your First Workflow](https://www.youtube.com/watch?v=4cQWJViybAQ) — full 14m47s tutorial. Pay close attention to the section where the webhook Test URL is generated and how "Listen for Test Event" works.

## 🛠️ Build It: Step-by-Step
1. Build **Workflow 1 (Manual):** Manual Trigger → Set node with fields `message` = `"Manual trigger executed!"` and `timestamp` = `{{ $now }}`. Execute and confirm both fields appear in the output.
2. Build **Workflow 2 (Webhook):** Add a **Webhook** node, set HTTP Method to `POST` and Path to `test-webhook`. Click **Listen for Test Event** to activate the test URL.
3. Open a terminal (or Postman) and send: `curl -X POST <your-test-url> -H "Content-Type: application/json" -d '{"name":"test"}'`.
4. Confirm the payload `{"name":"test"}` appears in the Webhook node's output panel, then add a Set node after it that captures `received_data = {{ $json }}` and `processed_at = {{ $now }}`.
5. Build **Workflow 3 (Schedule):** Add a **Schedule Trigger** node, set the interval to every 5 minutes. Add a Set node with `report_type`, `generated_at = {{ $now }}`, and `status = "Completed"`. Activate the workflow and wait for one execution to appear in Execution History (or temporarily set it to every 1 minute to see it fire faster, then reset).
6. For the Webhook workflow, test with at least 2 different HTTP methods or payloads (e.g., send a GET to the POST-only webhook and confirm it's rejected) to see how method restrictions behave.

**Stuck?** Import `WEEK_01_FOUNDATION/EXAMPLES/webhook_processing_workflow.json` to see a complete webhook-based workflow, then compare its validation/response pattern to yours.

## 🔑 Credentials Needed
None — Manual, Webhook, and Schedule triggers all work without external service credentials. You'll just need curl or Postman installed locally to send test requests.

## ✅ Definition of Done
- [ ] Your webhook returns the posted JSON body visibly in the node's output panel when tested with curl/Postman
- [ ] Your Schedule Trigger workflow is Active and has at least one successful execution logged in Execution History
- [ ] You can state which trigger type you'd use for: "notify me when a customer submits a form" vs. "run a daily report at 8am" vs. "let me manually re-run this for testing"
- [ ] All three workflows show green (successful) executions

## 🐛 Common Pitfalls
- **Webhook test URL vs. production URL:** The "Test URL" only works while you're actively listening (or the workflow is open in test mode) — you must **Activate** the workflow and use the production URL for it to respond outside the editor.
- **Wrong HTTP method:** If you configured the webhook for POST but curl defaults to GET, you'll get a 404. Always match `-X POST` in curl to the method set in the node.
- **Schedule Trigger set too frequently:** A 1-minute interval is fine for testing but reset it to something reasonable (hourly/daily) before moving on — tight intervals can flood execution history and hosting resources.

## 🏭 Industry Track Application
Build a webhook for your chosen industry track — e.g., a payment-received webhook for Fintech, a health-metric-submitted webhook for HealthTech, or a course-progress webhook for EdTech. Send it a realistic sample payload (at least 3 fields) via curl and confirm the data lands correctly in the node output.
