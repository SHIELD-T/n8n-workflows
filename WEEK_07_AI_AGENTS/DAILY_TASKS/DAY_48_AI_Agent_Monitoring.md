# DAY 48: AI Agent Monitoring
**Week:** 7 — AI Agents  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to build a health-check workflow that actually tells you when something is broken, before a client notices
- How to turn raw execution/error data into a single health score you can glance at
- How to route a "needs attention" state into a real alert (Slack/email) instead of just a log entry no one reads

## 🎥 Watch First
[n8n Tutorial for Beginners 2025: Build AI Agents Step-by-Step](https://www.youtube.com/watch?v=PfdnYe2690E)
Watch for how errors and failures are surfaced — that's the piece you're building today: visibility, not just execution.

## 🛠️ Build It: Step-by-Step
1. Create a new workflow with a **Schedule Trigger** (e.g. every 15 minutes) as the entry point for your monitor.
2. Add an **HTTP Request** node calling your n8n instance's Executions API (`GET /api/v1/executions`) to pull recent runs across the workflows you built this week.
3. Add a **Code** node that computes, from real returned data: success rate, average duration, and a count of distinct error types seen in the last window.
4. Add a **Set** node ("Health Score") that combines those into one 0-100 score using a formula you define (e.g. `successRate*0.6 + (100 - avgDurationPenalty)*0.4`) — document the formula in a comment.
5. Add an **IF** node: if health score is below your chosen threshold (e.g. 80), route to an alert branch.
6. On the alert branch, add a **Slack** (or **Email Send**) node that posts the health score, the failing workflow name(s), and the most recent error message — a real, useful alert, not a placeholder log line.
7. On the healthy branch, add a **NoOp** or a **Set** node that just records "healthy" with the score and timestamp.
8. Add a **Google Sheets** or **Airtable** node at the end (both branches) that appends this check's score and status to a running history sheet, so you can see trend over time.
9. Trigger the workflow manually twice — once against your normal workflows, and once after deliberately breaking one (e.g. removing a credential) — and confirm the alert branch actually fires on the second run.

## 🔑 Credentials Needed
n8n API key (for Executions API), Slack or Email credential for alerts, Google Sheets/Airtable credential for the history log.

## ✅ Definition of Done
- [ ] Health score is computed from real execution data, not hardcoded or random values
- [ ] You've verified the alert branch fires under a real failure condition you created on purpose
- [ ] A Slack/email alert (or a message you can screenshot) actually contains the failing workflow name and error detail
- [ ] Check history is being appended to a sheet/table so you have more than one data point

## 🐛 Common Pitfalls
- **Alerting on every single failed execution** — a monitor that pages you for every transient error becomes noise you'll ignore; use an aggregate threshold (success rate over a window) instead of a single-run trigger.
- **Monitor workflow itself has no error handling** — if the Executions API call fails, your monitor should say so, not silently stop; add an error branch on the HTTP Request node too.
- **Never actually testing the failure path** — it's tempting to only run this against healthy workflows; deliberately break something and confirm the alert fires before calling this done.

## 🏭 Industry Track Application
For a HealthTech or Fintech track where downtime has compliance implications, make the alert message include exactly which workflow and data type was affected — "patient intake automation degraded" is actionable, "something is wrong" is not.
