# DAY 15: Triggers vs. Actions
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- The distinction between trigger nodes (start a workflow) and action nodes (do work within it)
- How Manual, Webhook, and Schedule triggers differ in real automation use cases
- How to chain action nodes (Set, IF, HTTP Request) after a trigger to build a working pipeline
- How to test each trigger type end-to-end and confirm execution

## 🎥 Watch First
- [n8n Quick Start Tutorial: Build Your First Workflow](https://www.youtube.com/watch?v=4cQWJViybAQ) — full 14m47s tutorial. Watch the trigger walkthrough closely: note how the webhook Test URL differs from the production URL, and how the Schedule Trigger's interval settings work.

## 🛠️ Build It: Step-by-Step
1. Build **Workflow 1 (Manual → Action chain):** Manual Trigger → Set node "Set Sample Data" with `user_name`="John Doe", `user_email`="john@example.com", `action_type`="manual_trigger" → second Set node "Process Data" with `processed_name` = `{{ $json.user_name.toUpperCase() }}`, `processed_email` = `{{ $json.user_email.toLowerCase() }}`, `processed_at` = `{{ $now }}`. Execute and confirm `processed_name` shows "JOHN DOE".
2. Build **Workflow 2 (Webhook → Action chain):** Webhook node, HTTP Method POST, Path `trigger-actions`. Add IF node "Validate Input" condition: `{{ $json.data }}` is not empty. True branch → Set node "Process Input" with `processed_data` = `{{ $json.data.trim() }}`, `action_type`="webhook_trigger". Add a Respond to Webhook node returning JSON `{ "status": "success", "processed_data": "{{ $json.processed_data }}" }`.
3. Test with curl: `curl -X POST <your-test-url> -H "Content-Type: application/json" -d '{"data":"  hello world  "}'` and confirm the response shows `"processed_data":"hello world"` (trimmed).
4. Send an empty-data payload too: `curl -X POST <your-test-url> -d '{"data":""}'`. Confirm it routes to the IF node's false branch instead (add a simple Set node there with an error status) — this proves triggers only start execution, while the IF action node controls the branch.
5. Build **Workflow 3 (Schedule → Action chain):** Schedule Trigger set to every 5 minutes → Set node "Collect Data" with `report_type`, `generated_at` = `{{ $now }}`, `status` = "Completed". Activate the workflow and wait for at least one execution to appear in Execution History (or temporarily drop to 1 minute to see it fire faster, then reset to something reasonable).
6. In your notes, write one sentence distinguishing "trigger" from "action" using your own three workflows as examples.

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/conditional_processing_workflow.json` (Menu → Import from File in n8n) to see a working multi-branch IF pattern, then compare its Detect Source → Validate → Format/Error branches to your Workflow 2.

## 🔑 Credentials Needed
None — all three trigger types and their actions work without external service credentials. You'll need curl or Postman installed locally to send test requests.

## ✅ Definition of Done
- [ ] Workflow 1 executes and "Process Data" output shows `processed_name` in uppercase and `processed_email` in lowercase
- [ ] Workflow 2's webhook returns `"processed_data":"hello world"` when tested with the curl command above, trimmed of whitespace
- [ ] Workflow 2 correctly routes an empty `data` payload to a separate error/false branch, not the success path
- [ ] Workflow 3 is Active with at least one successful execution logged in Execution History
- [ ] You can explain, in one sentence, the difference between a trigger and an action using your own workflows

## 🐛 Common Pitfalls
- **Test mode vs. Active mode:** The webhook Test URL only responds once while you're actively listening in the editor — you must **Activate** the workflow to get a stable production URL that responds anytime.
- **Missing `.trim()`:** Expressions like `$json.data` return the raw string including leading/trailing spaces; the Set node won't auto-trim it for you.
- **Whitespace passes "isNotEmpty":** The IF node's "isNotEmpty" treats a string of only spaces as non-empty — trim before validating if you want to catch whitespace-only submissions.

## 🏭 Industry Track Application
Build Alex's lead capture system with multiple trigger types for different lead sources: a Webhook for website form submissions, a Schedule Trigger for a daily CRM sync pull, and a Manual Trigger for re-processing a lead by hand. Send a realistic lead payload (name, email, source) via curl to the webhook and confirm it's captured correctly.
