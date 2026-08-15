# DAY 32: Production System Management
**Week:** 5 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Aggregating several independent health checks into one overall system-health verdict
- Building an alert path that only fires on real degradation, verified by forcing a failure
- Why HTTP Request nodes need explicit error handling to inspect a bad status instead of just crashing

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — Production system management section. Pay attention to how "overall health" is computed as an AND across every monitored system — one failure should degrade the whole verdict.

## 🛠️ Build It: Step-by-Step
1. Create a workflow named **Production Health Control Center**. Add a **Schedule Trigger** node — set it to every 2 minutes (temporarily use every 1 minute for faster testing).
2. Add three **HTTP Request** nodes checking real endpoints: "Check n8n Health" (GET your own instance's `/healthz`), "Check Webhook Endpoint" (GET your [webhook.site](https://webhook.site) URL), and "Check External Dependency" (GET `https://httpstat.us/200`). On each, enable **Options → Response → Never Error** so a bad status code is returned as data instead of throwing.
3. Add a **Code** node "Aggregate System Status" that reads the status code from all three prior nodes (via `$('Check n8n Health').item.json` etc.) and sets `overall_health = "healthy"` only if all three returned a 2xx code, otherwise `"degraded"`.
4. Add an **IF** node "Check for Issues" branching on `overall_health !== 'healthy'`.
5. On the true (degraded) branch, add an **HTTP Request** node "Send Incident Alert" POSTing the full status detail to your webhook.site URL, and a **Set** node "Log Incident" recording a timestamped `incident_id`.
6. Force a failure to prove the alert path works: temporarily change "Check External Dependency" to `https://httpstat.us/500`, then click **Execute Workflow**. Confirm the IF node's true branch fires and the incident alert lands in your webhook.site inbox.
7. Revert the URL to `https://httpstat.us/200`, re-run, and confirm the IF node's false branch fires instead (`overall_health` stays `"healthy"`).
8. Activate the workflow and let it run for 3 full cycles. Check Execution History shows 3 automatic runs, each completing in under 5 seconds (check the Duration column), then set the interval back to every 2 minutes if you'd changed it.

**Stuck?** Import `WEEK_05_WORKFLOWS/EXAMPLES/maintenance_automation_system.json` (Menu → Import from File in n8n) — its multi-check-then-aggregate-then-alert pattern is the same shape, applied to maintenance tasks instead of live health checks.

## 🔑 Credentials Needed
None — no external services today. A free webhook.site capture URL is optional.

## ✅ Definition of Done
- [ ] "Production Health Control Center" checks at least 3 real endpoints and computes a single `overall_health` value
- [ ] You've proven the true branch fires by forcing a 500 response, evidenced by the alert payload in your webhook.site inbox
- [ ] You've proven the false branch fires on a healthy pass
- [ ] Execution History shows 3+ automatic scheduled runs, each with Duration under 5 seconds

## 🐛 Common Pitfalls
- **HTTP Request node stops the whole workflow on a non-2xx response:** without "Never Error" enabled in Options, one bad status kills the execution before you can even inspect it.
- **Strict type comparison on status codes:** a status code can arrive as a string in some response formats — verify the actual type in the Code node before comparing.
- **Forgetting to revert the 1-minute test interval:** leaving it running eats unnecessary requests against `httpstat.us` and your own instance long after you're done testing.

## 🏭 Industry Track Application
Add a fourth check specific to your industry track's critical dependency (e.g., a payment gateway status endpoint for FinTech, an EHR/lab API for HealthTech, an inventory API for E-commerce). Note in a Set node comment which of the four checks would be the most business-critical to page a human about immediately versus just log.
