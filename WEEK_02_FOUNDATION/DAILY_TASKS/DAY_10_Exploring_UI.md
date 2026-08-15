# DAY 10: Exploring n8n UI
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- Where Execution History, workflow tags, and Pin Data live in the n8n UI
- How to read a failed execution's error detail versus a successful one
- How Manual, Webhook, and Schedule triggers each show up differently in Execution History
- How to toggle between Table and JSON views to inspect a node's raw output

## 🎥 Watch First
- [n8n Administrator UI Overview](https://www.youtube.com/watch?v=J2O4BlTulRg) — First 15 minutes on UI navigation and monitoring. Watch for where the presenter finds past executions and how they distinguish a successful run from a failed one at a glance.

## 🛠️ Build It: Step-by-Step
1. Create Workflow 1: **Manual Trigger** → **IF** "Input Validation" (String: `{{ $json.data }}` is not empty) → **Set** "Step 1: Data Cleaning" (`cleaned_data` = `{{ $json.data.trim().toLowerCase() }}`) → **Set** "Step 2: Data Processing" (`processed_data` = `{{ $json.cleaned_data.split(' ').length }}`). Add the tag "week2-day10" via workflow settings.
2. Execute it with no input — it should fail the IF check. Open Execution History and confirm you can see the failed run.
3. Use **Pin Data** on the Manual Trigger to pin `{"data": "hello world automation"}`, then re-execute and confirm `processed_data` = 3.
4. Create Workflow 2: **Webhook Trigger** (path `conditional-processing`) → **IF** "Route by Type" (String: `{{ $json.type }}` equals `urgent`) → two separate **Set** nodes ("Urgent Processing" sets `priority=HIGH`, "Normal Processing" sets `priority=NORMAL`). Activate it.
5. Test both branches:
   `curl -X POST <production-webhook-url> -H "Content-Type: application/json" -d '{"type":"urgent"}'`
   `curl -X POST <production-webhook-url> -H "Content-Type: application/json" -d '{"type":"other"}'`
   Confirm in Execution History that one run shows "Urgent Processing" executed and the other shows "Normal Processing".
6. Create Workflow 3: **Schedule Trigger** (every 1 minute, for testing) → **Set** node recording `{{ $now }}`. Let it run for 3 minutes, then filter Execution History by this workflow and confirm at least 2 automatic executions appear roughly 60 seconds apart. Deactivate it afterward.
7. In any run's Execution History, open a node's Output panel and toggle between Table view and JSON view.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/advanced_triggers_debugging.json` (Menu → Import from File in n8n) to see a working version that combines Webhook, Schedule, and Manual triggers with shared validation logic, then compare it to what you built.

## 🔑 Credentials Needed
None — all three workflows use only Manual/Webhook/Schedule triggers, IF, and Set nodes.

## ✅ Definition of Done
- [ ] Workflow 1 shows both a failed execution (empty input) and a successful one (pinned data) in Execution History
- [ ] Workflow 2's two curl calls produced two executions taking different branches, both visible in history
- [ ] Workflow 3 produced at least 2 automatic scheduled executions roughly 60 seconds apart, then was deactivated
- [ ] You can name, from memory, which panel (Table vs JSON) you'd use to inspect a node's raw output structure

## 🐛 Common Pitfalls
- **Not activating before testing:** the Test URL only works while the editor is open and listening; the Production URL only works once the workflow is Activated.
- **Leaving a fast schedule running:** a 1-minute Schedule Trigger left active after testing clutters Execution History (and burns resources) until deactivated.
- **Forgetting Pin Data is still on:** a pinned node ignores real trigger input, which is confusing days later when a "live" workflow inexplicably always returns the same result — unpin it once you're done testing.

## 🏭 Industry Track Application
Sarah wants a dashboard showing what her automations are actually doing. Using Workflow 3's scheduled execution history as the data source, identify what a real-time monitoring and analytics dashboard for Sarah would need to show: success/fail counts, time-of-day execution pattern, and last-run timestamp. Write down the specific n8n UI screen you'd point Sarah to for each of those three answers.
