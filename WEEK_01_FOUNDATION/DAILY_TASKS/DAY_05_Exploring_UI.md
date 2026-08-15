# DAY 5: Exploring n8n UI
**Week:** 1 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to navigate Workflows, Execution History, and Credentials sections
- How to read execution logs to debug a failed run
- How the IF node creates branching logic based on conditions
- Basic performance signals to watch (execution time, node-by-node duration)

## 🎥 Watch First
- [Deep Dive: n8n Interface Walkthrough (2025)](https://www.youtube.com/watch?v=J2O4BlTulRg) — first 15 minutes, this time focused on the Execution History and Credentials screens rather than the canvas basics you already know from Day 2.

## 🛠️ Build It: Step-by-Step
1. Build **Workflow 1 (Data Processing):** Manual Trigger → Set node (`name`, `email`, `timestamp`) → second Set node that transforms them: `processed_name = {{ $json.name.toUpperCase() }}`, `processed_email = {{ $json.email.toLowerCase() }}`. Execute and verify the transformation in the output.
2. Build **Workflow 2 (Webhook + Branch):** Webhook node → **IF** node checking `{{ $json.name }}` `is not empty` → true branch: Set node with `status = "processed"`; false branch left unconnected for now. Add a **Respond to Webhook** node after the true branch returning `{{ {"status":"success","data":$json} }}`.
3. Test Workflow 2 twice with curl: once with a payload containing `name`, once without it — confirm the IF node routes each execution down the correct branch (check the node's color/highlight after execution).
4. Build **Workflow 3 (Scheduled Report):** Schedule Trigger (every 1 hour) → Set node generating `report_id = {{ $now.format('YYYY-MM-DD-HH') }}` and `status = "Completed"`.
5. Intentionally break Workflow 1: change `$json.name` to `$json.namee` (typo) in the Set node, execute, and read the red error banner — note exactly what error message n8n shows.
6. Open **Executions** in the left sidebar, find the failed run from step 5, click into it, and confirm you can see exactly which node failed and why. Fix the typo and re-run to confirm it goes green.

**Stuck?** Import `WEEK_01_FOUNDATION/EXAMPLES/example_workflow_2.json` and `WEEK_01_FOUNDATION/EXAMPLES/foundation_learning_progress_tracker.json` for two more complete reference workflows to explore in the canvas.

## 🔑 Credentials Needed
None — today's three workflows use only Manual/Webhook/Schedule triggers and built-in Set/IF/Respond nodes.

## ✅ Definition of Done
- [ ] All three workflows execute successfully at least once, visible in Execution History
- [ ] You've deliberately caused and then read one failed execution's error detail (not just seen the red X)
- [ ] Your IF node correctly routes at least one true and one false case to different branches
- [ ] You can name where Credentials, Executions, and Workflows live in the left-hand navigation without looking

## 🐛 Common Pitfalls
- **IF node false branch left dead-ending:** n8n won't error on an unconnected branch, but nothing happens on that path — for real workflows, always terminate both branches (e.g., an error-response node on false).
- **Confusing "workflow saved" with "workflow active":** A saved but inactive workflow won't respond to real webhook calls outside the editor — check the Active toggle in the top-right if a webhook you expect to fire doesn't.
- **Execution History filter hiding runs:** By default it may filter to "this workflow only" — if you can't find a run, check you're looking at the correct workflow's execution list, not the global one.

## 🏭 Industry Track Application
Rebuild Workflow 2's IF condition around an industry-relevant rule — e.g., Fintech: route transactions over $1,000 to a "flagged" branch vs. auto-approve; HealthTech: route appointment requests marked "urgent" to a different branch than routine ones. Test both branches with sample payloads.
