# DAY 26: Monitoring & Maintenance
**Week:** 4 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to build a scheduled health-check workflow that runs independently of your production workflows
- How to compute a simple health score from multiple signals (an activity ratio, a success rate, resource thresholds)
- How to branch into an alert path only when a computed status crosses a threshold
- How monitoring differs from error handling — monitoring watches the whole system, error handling reacts inside one workflow

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — workflow monitoring and maintenance section. Note the distinction between "is this one execution failing" and "is the whole system healthy."

## 🛠️ Build It: Step-by-Step
1. Schedule Trigger "Monitoring Schedule Trigger": every 5 minutes.
2. Set node "Initialize Monitoring": `monitoring_id` = `{{ $now.format('YYYYMMDDHHmmss') }}`, `check_time` = `{{ $now }}`.
3. Since you likely don't have n8n's own management API exposed, simulate "Check Workflow Health" with an HTTP Request to `https://jsonplaceholder.typicode.com/todos` and treat the response's `completed: true` ratio as a stand-in for "active workflow" ratio: Set node "Analyze Workflow Status" computing `health_score` = `{{ Math.round(($json.filter(t => t.completed).length / $json.length) * 100) }}`.
4. Set node "Analyze Execution Metrics" (simulated): hardcode `total_executions` = 50, and vary `failed_executions` between test runs (e.g. 2 vs. 15). Compute `success_rate` = `{{ Math.round(($json.total_executions - $json.failed_executions) / $json.total_executions * 100) }}`.
5. Set node "Generate Health Report" combining both signals: `overall_health` = `{{ $json.health_score > 80 && $json.success_rate > 90 ? 'healthy' : 'needs_attention' }}`.
6. IF node "Check for Alerts": `{{ $json.overall_health }}` equals `needs_attention` → true branch goes to a "Send Alert Notification" Set node (build the alert message string now; wire it to a real Slack node later once you have credentials).
7. Run the workflow twice with different `failed_executions` values (2 and 15) via manual execution with pinned data, and confirm the first run reaches a "healthy" report while the second reaches the alert branch.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/advanced_workflow_optimization_engine.json` (Menu → Import from File in n8n) — its `optimization-impact-check` IF node (branching on `improvement_percentage >= 20`) is structurally the same threshold-check pattern you need for "Check for Alerts"; compare the two conditions side by side.

## 🔑 Credentials Needed
None to complete the exercise as described. A Slack Bot Token (`chat:write` scope) is needed only if you wire the alert branch to a real Slack channel instead of just building the message string.

## ✅ Definition of Done
- [ ] The workflow is Active on a Schedule Trigger with at least 2 successful executions logged (wait 10 minutes or temporarily shorten the interval)
- [ ] `overall_health` correctly evaluates to "healthy" when `success_rate` > 90 and `health_score` > 80, tested with pinned data
- [ ] `overall_health` correctly evaluates to "needs_attention" and reaches the alert branch when `failed_executions` is raised to 15/50
- [ ] The alert message string contains the actual computed `health_score` and `success_rate` values, not placeholder text

## 🐛 Common Pitfalls
- **Scheduling a monitoring workflow too frequently (every 1 minute) against a real external API can itself look like abusive traffic** — 5 minutes is a reasonable floor for a learning exercise.
- **Computing `success_rate` with division before checking for zero can produce `NaN`** — guard against divide-by-zero even in a simulated exercise, since real systems will hit it.
- **An alert workflow that never de-escalates spams the same alert every 5 minutes forever** — note this as a known gap; a full solution would track "already alerted" state, which is beyond today's scope.

## 🏭 Industry Track Application
Build a health check for Alex's lead-response system: poll a simulated "leads processed in the last hour" count every 5 minutes, and if it drops to 0 during business hours (9am-6pm, checked via `{{ $now.hour() }}`), flag `overall_health` as `needs_attention` so Alex knows the lead pipeline silently stopped instead of finding out from a lost customer.
