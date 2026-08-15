# DAY 8: Understanding Triggers Deep Dive
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- The difference between Webhook, Schedule, and Manual triggers, and when to reach for each
- How to add conditions inside a trigger's downstream IF node so a workflow only proceeds on valid data
- How to combine two trigger types into one workflow using a shared IF node to route by source
- How to read Execution History to tell whether a trigger workflow behaved as expected

## 🎥 Watch First
- [n8n Triggers Explained & Demo](https://www.youtube.com/watch?v=4cQWJViybAQ) — Focus on webhooks & triggers section (14m47s). Watch for how the presenter tests a webhook with an external tool before wiring up downstream nodes — you'll do the same today.

## 🛠️ Build It: Step-by-Step
1. New workflow. Add a **Webhook** node named "Conditional Webhook" — HTTP Method `POST`, Path `advanced-webhook`. Copy its Test URL.
2. Add an **IF** node "Validate Data" connected to it. Conditions (String, combinator AND): `{{ $json.type }}` "is not empty", and `{{ $json.data }}` "is not empty".
3. On the true branch, add a **Set/Edit Fields** node "Process Valid Data" with fields: `processed_type` = `{{ $json.type }}`, `processed_data` = `{{ $json.data }}`, `processed_at` = `{{ $now }}`, `status` = `processed`.
4. Add a **Respond to Webhook** node after it: Respond With = JSON, Response Body = `{{ { "status": "success", "processed_at": $json.processed_at } } }}`.
5. Click **Execute Workflow** (so it listens for a test call), then from a terminal run:
   `curl -X POST <your-webhook-test-url> -H "Content-Type: application/json" -d '{"type":"order","data":"test-payload"}'`
   Confirm you get back `{"status":"success","processed_at":"..."}`.
6. Re-run the curl with `-d '{"type":"order"}'` (missing `data`) and confirm in Execution History that the IF node's false branch fired instead of the success path.
7. Build a second, separate workflow: **Schedule Trigger** (Interval: every 2 hours) → **IF** node "Check Business Hours" (Number: `{{ $now.hour() }}` ≥ 9 AND `{{ $now.hour() }}` < 17) → **Set** node with `task_type`, `executed_at`, `is_business_hours`. Trigger it manually and confirm the branch taken matches the current hour.
8. Build a third workflow where **both** a Manual Trigger and the Webhook node from step 1 feed into the same "Validate Data" IF node. Execute once manually and once via curl, and confirm both runs appear in Execution History with the same downstream logic applied.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/advanced_triggers_debugging.json` (Menu → Import from File in n8n) to see a working version with all three trigger types wired to shared validation and processing logic, then compare it to what you built.

## 🔑 Credentials Needed
None — Webhook, Schedule Trigger, Manual Trigger, IF, and Set nodes require no external credentials today.

## ✅ Definition of Done
- [ ] Your webhook returns `{"status":"success",...}` when tested with curl and a valid JSON payload
- [ ] Your webhook's IF node routes an incomplete payload down a different branch than a complete one, confirmed in Execution History
- [ ] Your Schedule Trigger workflow's business-hours IF node evaluates correctly for the current time
- [ ] You've triggered the same downstream logic from two different trigger types in one workflow and confirmed both executions in history

## 🐛 Common Pitfalls
- **Testing before listening:** n8n only captures test webhook calls while it's actively listening (after clicking Execute Workflow) — a curl sent before that shows nothing.
- **Test URL vs Production URL:** the Test URL only works while the editor is open and listening; the workflow must be Activated (toggle top-right) before its Production URL responds.
- **Assumed OR logic:** IF node conditions default to AND — if you want "either field empty routes to error," check each condition individually rather than assuming it.

## 🏭 Industry Track Application
Sarah's photo organizer needs to accept photos from multiple input sources — a phone app that pushes instantly and a desktop folder that syncs on a schedule. Build the "two triggers into one IF node" workflow from step 8 as this system: rename the fields to `source` (`"phone"` or `"desktop"`) and `filename`, and route both sources into the same "Process Valid Data" logic. Test by sending a fake phone upload via curl and a fake desktop sync via Manual Trigger, then confirm both appear correctly in Execution History.
