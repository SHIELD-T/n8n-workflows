# DAY 31: Workflow Optimization & Maintenance
**Week:** 5 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to pull real execution data from n8n's own REST API instead of guessing at performance
- Turning raw execution history into a health score you can act on (error rate + average duration)
- Building a scheduled maintenance sweep that flags problems instead of just logging them

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — Workflow optimization and maintenance section. Pay attention to how "optimization candidates" are identified by a threshold (execution time or error rate), not a gut feeling.

## 🛠️ Build It: Step-by-Step
1. Go to **Settings → n8n API** in your n8n instance and create an API key (needed to query your own execution history).
2. Create a workflow named **Automated Maintenance Sweep**. Add a **Schedule Trigger** node — set the interval to Hours = 6 for production, but temporarily switch it to Minutes = 1 so you can observe it firing during testing.
3. Add an **HTTP Request** node "Get n8n Executions" — GET `{{your n8n host}}/api/v1/executions`, authenticated with the API key credential you just created (Header Auth or the built-in n8n API credential type).
4. Add a **Code** node "Compute Health Metrics" that loops over `$input.all()`, computing average execution duration and the percentage of executions with `status !== 'success'`, and tags any workflow whose error rate exceeds 10% or average duration exceeds 3000ms as `needsAttention`.
5. Add an **IF** node "Any Workflows Need Attention?" branching on whether the `needsAttention` array is non-empty.
6. On true, add a **Set** node "Flag For Optimization" building the list of flagged workflow names, then an **HTTP Request** node "Send Alert" POSTing that list to a free [webhook.site](https://webhook.site) URL.
7. Add a **Set** node "Health Score" computing `Math.max(0, Math.round(100 - errorRatePercent * 2 - avgDurationMs / 100))`.
8. Click **Execute Workflow** to run it manually once — open the "Compute Health Metrics" output and confirm it lists real workflow names and duration numbers pulled from your own instance. Then let the Schedule Trigger fire twice at the 1-minute test interval, confirm 2 automatic (non-manual) runs appear in Execution History, and set the interval back to Hours = 6.

**Stuck?** Import `WEEK_05_WORKFLOWS/EXAMPLES/workflow_optimization_system.json` and `WEEK_05_WORKFLOWS/EXAMPLES/maintenance_automation_system.json` (Menu → Import from File in n8n) to see working versions of the optimization-scoring and scheduled-maintenance patterns respectively.

## 🔑 Credentials Needed
- n8n API key (Settings → n8n API), used to query your own instance's execution history.

## ✅ Definition of Done
- [ ] "Automated Maintenance Sweep" runs on a real Schedule Trigger interval and Execution History shows at least 2 automatic (non-manual) executions
- [ ] "Compute Health Metrics" node output contains real data pulled from your n8n instance's `/executions` API — not placeholder text
- [ ] "Health Score" Set node returns a number between 0-100 for a real test run
- [ ] Schedule Trigger interval is reset back to every 6 hours (or a production-appropriate cadence) before you finish

## 🐛 Common Pitfalls
- **401 from the executions API:** the HTTP Request node's credential isn't attached, or the API key wasn't enabled under Settings → n8n API — check both.
- **Schedule Trigger left at the 1-minute test interval:** forgetting to reset it floods your Execution History and burns your instance's execution quota.
- **Code node TypeError on `.json`:** iterate with `$input.all()` and access `.json` on each item — looping over raw items without `.json` throws immediately.

## 🏭 Industry Track Application
Adjust the error-rate and duration thresholds (10% / 3000ms) to match your industry's tolerance — e.g., a stricter 2% error-rate threshold for FinTech payment workflows, or a longer allowed duration for HealthTech workflows that call slow external labs/EHR APIs. Document your chosen thresholds and the reasoning in a note on the Code node.
