# DAY 49: AI Agent Review
**Week:** 7 — AI Agents  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to audit a week's worth of workflows for what actually still runs vs. what only ever worked in theory
- How to chain multiple n8n workflows together into one working system using Execute Workflow / webhook handoffs
- How to write a short technical report that documents what you built, not just that you "built something"

## 🎥 Watch First
No new video today — this is a review/consolidation day. If any of Week 7's videos are still unclear, this is the day to go back and re-watch the specific 5-10 minute section that covers it, rather than the whole thing again.

## 🛠️ Build It: Step-by-Step
1. In n8n, open every workflow you built or imported this week (check `WEEK_07_AI_AGENTS/EXAMPLES/advanced_ai_agent_system.json`, `agent_communication_system.json`, `agent_learning_system.json`, and `ai_agent_learning_system.json` if you didn't finish your own versions) and execute each one manually once.
2. For each, note in a simple table: workflow name, does it still run without errors, and which nodes (if any) fail because a credential or placeholder URL was never replaced.
3. Pick your single most complete workflow from the week. Add a Webhook trigger to it if it doesn't have one, so it can be called from another workflow.
4. Build one new "orchestrator" workflow: Manual Trigger → Execute Workflow node pointing at the workflow from step 3 → a Set node that captures its output → an IF node that checks whether the result looks successful (e.g. a `status` field equals `"success"`) → two branches: one that logs success, one that logs failure with the error detail.
5. Run the orchestrator twice: once with valid input so it takes the success branch, once with input designed to fail (e.g. missing a required field) so it takes the failure branch. Screenshot both runs.
6. Write a half-page "Week 7 System Status" note: what you built, what's actually working end-to-end today, and what's still a placeholder that would need a real API key/service before it works outside the course.

## 🔑 Credentials Needed
Whatever your chosen workflow already needs (commonly an OpenAI API credential) — no new credentials required for the orchestrator itself.

## ✅ Definition of Done
- [ ] You have a table listing every Week 7 workflow and its current working/broken status
- [ ] You have one orchestrator workflow that calls another workflow via Execute Workflow and branches on success/failure
- [ ] You've captured a screenshot of both the success run and the failure run
- [ ] Your "Week 7 System Status" note names at least one thing that's genuinely working and at least one thing that's still a placeholder

## 🐛 Common Pitfalls
- **Execute Workflow node can't find the target workflow** — it references workflows by ID, not name; if you re-imported a workflow it may have a new ID, so re-select it in the node's dropdown rather than assuming the old link still resolves.
- **"Success" branch always triggers even on failure** — this usually means your IF node is checking the wrong field, or the failing node was skipped instead of throwing, so the data never reached the check. Add a Set node right after the risky node so you can see exactly what shape the data is in.
- **Treating "no red X in the canvas" as proof it works** — a workflow that calls a placeholder API (like the ones flagged with a ⚠️ sticky note in this week's EXAMPLES files) will "succeed" by n8n's standards while doing nothing real. Read the actual output data, not just the execution status icon.

## 🏭 Industry Track Application
Apply this same audit-and-chain exercise to whichever industry-specific AI workflow you've been building all week (fraud detection for Fintech, patient triage for HealthTech, etc.) — the goal is the same regardless of industry: know exactly what's real and working versus what's still a stand-in, and have one chained system to show for the week.

---

*Week 7 complete. Carry your "Week 7 System Status" note into Week 8 — you'll be extending this same system with deployment, monitoring, and documentation.*
