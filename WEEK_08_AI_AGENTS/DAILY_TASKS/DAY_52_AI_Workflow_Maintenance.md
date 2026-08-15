# DAY 52: AI Workflow Maintenance
**Week:** 8 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- What ongoing maintenance a deployed AI workflow actually needs (credential rotation, health checks, version tracking)
- How to build a scheduled health-check workflow in n8n with the Schedule Trigger node
- How to keep a maintenance log so "we're maintaining it" is a checkable fact, not a claim

## 🎥 Watch First
- [Build AI Agents & Automate Workflows (Zero to Hero)](https://www.youtube.com/watch?v=DkV7ztrhLh8) — watch the "Maintaining AI workflows" section; note how they handle credential expiry/rotation and workflow versioning.

## 🛠️ Build It: Step-by-Step
1. Create a new workflow with a **Schedule Trigger** node set to run daily (Interval: Days, every 1 day) — this is your maintenance-check workflow, separate from your Day 51 production agent.
2. Add an **HTTP Request** node that calls your Day 51 workflow's production webhook with a lightweight "ping" test payload to confirm it's still responding.
3. Add an **IF** node checking the response status/`{{ $json.status }}` — route to a "Healthy" branch and an "Unhealthy" branch.
4. On the Unhealthy branch, add a **Set** node building an alert message (workflow name, timestamp, what failed). If you have Slack or Email credentials from earlier weeks, wire up a real notification node; otherwise simulate the alert payload with Set.
5. On both branches, add a Set node that appends a maintenance log entry — `{{ $now.toISO() }}`, workflow checked, and result — written to a Google Sheet, Airtable, or at minimum captured in the node's output so you build the habit of logging.
6. Manually execute the maintenance workflow once and confirm it correctly reaches the Healthy branch for your active Day 51 workflow.
7. Deliberately deactivate your Day 51 workflow, re-run the maintenance check, and confirm it now correctly routes to Unhealthy — then reactivate Day 51's workflow.

**Stuck?** Import `WEEK_08_AI_AGENTS/EXAMPLES/ai_system_integration_workflow.json` to see a working "Monitor Integration Status" HTTP call pattern you can adapt into your own health check.

## 🔑 Credentials Needed
Optional Slack or Email/SMTP credential for real alerting (reuse from earlier weeks). Otherwise none — you're only calling your own deployed webhook.

## ✅ Definition of Done
- [ ] A separate Schedule Trigger workflow exists that pings your Day 51 production webhook
- [ ] The health-check IF branch correctly distinguishes Healthy vs Unhealthy in a manual test of both cases
- [ ] At least one maintenance log entry has been recorded with a real timestamp
- [ ] You can state your maintenance schedule's actual interval and justify why it's frequent enough

## 🐛 Common Pitfalls
- **Scheduling too frequently:** on n8n Cloud free/starter tiers this silently burns your execution quota — daily or hourly is usually enough for a course-scale project.
- **Checking status code only:** a broken workflow can still return 200 with an empty or malformed body — check the payload shape, not just the HTTP status.
- **No log at all:** without a maintenance log, "we've been maintaining this" is just a claim, not a checkable fact.

## 🏭 Industry Track Application
Set your maintenance schedule's interval to match what a real client in your industry track would expect (e.g. every 15 minutes for a Fintech fraud-check agent vs. daily for an EdTech content-generation agent), and write one sentence justifying the interval you chose.
