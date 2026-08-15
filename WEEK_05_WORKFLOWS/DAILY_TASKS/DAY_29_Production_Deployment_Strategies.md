# DAY 29: Production Workflow Deployment Strategies
**Week:** 5 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Blue-green deployment: running two environments and switching traffic only after a health check passes
- Why every deployment needs a backup step and an automated rollback path, not just a "deploy" button
- How to compute and log deployment metadata (deployment ID, duration, version) for auditability

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — Production deployment strategies section. Pay attention to how they separate the "deploy" step from the "switch traffic" step — that gap is where health checks and rollback logic live.

## 🛠️ Build It: Step-by-Step
1. Get a free capture URL from [webhook.site](https://webhook.site) and copy your unique URL — it stands in for the external backup/monitoring services this pattern would normally call.
2. Create a new workflow named **Production Deployment Pipeline**. Add a **Webhook** node named "Deployment Trigger" — HTTP Method `POST`, Path `deploy-production`.
3. Add a **Set** node "Initialize Deployment" with fields: `deployment_id` = `{{ $now.format('yyyyMMddHHmmss') }}`, `deployment_type` = `blue_green`, `workflow_version` = `{{ $json.version }}`, `start_time` = `{{ $now }}`.
4. Add an **IF** node "Validate Deployment Request" checking `deployment_type` equals `blue_green` AND `workflow_version` is not empty.
5. On the true branch, add an **HTTP Request** node "Backup Current Production" — POST to your webhook.site URL with JSON body `{{ { deployment_id: $json.deployment_id, backup_type: "pre_deployment" } }}`.
6. Add a second **HTTP Request** node "Health Check Green Environment" — GET your webhook.site URL — then an **IF** node checking the returned HTTP status code is `200`. Wire the false branch to a **Set** node "Execute Rollback" logging a `rollback_reason`.
7. On the true branch, add an **HTTP Request** node "Switch Traffic to Green" (POST to webhook.site) followed by a **Set** node "Deployment Success" computing `deployment_duration` = `{{ $now.diff($json.start_time, 'milliseconds') }}`.
8. Activate the workflow and test it: `curl -X POST http://localhost:5678/webhook/deploy-production -H "Content-Type: application/json" -d '{"version":"1.0.3"}'`. Open your webhook.site inbox and confirm the backup, health check, and traffic-switch requests arrived in order with the same `deployment_id` — then check n8n's Execution History shows the run as Success with the IF node's true branch taken.

**Stuck?** Import `WEEK_05_WORKFLOWS/EXAMPLES/production_deployment_workflow.json` (Menu → Import from File in n8n) to see a working version, then compare it to what you built — note it uses the same webhook/Set/IF/HTTP Request pattern, just pointed at real (fictional) API URLs instead of webhook.site.

## 🔑 Credentials Needed
None — no external services today. A free webhook.site capture URL (no signup required) is all you need.

## ✅ Definition of Done
- [ ] "Production Deployment Pipeline" has Webhook → Set → IF → 3 HTTP Request nodes wired as above and the workflow is Active
- [ ] Triggering the curl command returns a response and Execution History shows a Success run with the correct branch taken
- [ ] Your webhook.site inbox shows all 3 requests (backup, health check, traffic switch) carrying the same `deployment_id`
- [ ] You've tested the failure path by pointing the health check at `https://httpstat.us/500` instead of webhook.site and confirmed the rollback branch fires

## 🐛 Common Pitfalls
- **Workflow saved but not activated:** the webhook only listens when the workflow's Active toggle is on — a saved-but-inactive workflow silently returns 404 on trigger.
- **Test URL vs. Production URL confusion:** n8n gives you a different webhook URL for manual testing (Test URL, shown while editing) versus the live Production URL (used once activated) — curling the wrong one is the #1 reason "nothing happens."
- **Type mismatch in the IF node:** an HTTP status code can arrive as a string `"200"` instead of a number — use the IF node's Number condition type, not String, or comparisons silently fail.

## 🏭 Industry Track Application
Prefix your `deployment_id` values with your chosen industry track (e.g., `fintech-20260815...`) and add a note field to the "Backup Current Production" payload describing the one deployment safeguard that matters most for that industry — e.g., an audit trail requirement for FinTech/HealthTech, or a maximum-downtime SLA for E-commerce during a traffic switch.
