# DAY 47: AI Agent Optimization
**Week:** 7 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to measure a workflow's actual performance (execution time, token usage, error rate) instead of assuming it's fine
- How to set a concrete threshold that triggers an optimization action instead of "optimizing" on a hunch
- How n8n's own execution data (via the Executions list / API) can be your real performance metrics source instead of a fake external API

## 🎥 Watch First
[n8n Tutorial for Beginners: Complete AI Automation Guide](https://www.youtube.com/watch?v=CfD17vBCPEU)
Watch for any mention of execution time or node-level timing — that's the real data you'll use today instead of a placeholder metrics API.

## 🛠️ Build It: Step-by-Step
1. Pick one workflow you've already built this week (e.g. Day 43's orchestrator or Day 46's decision agent) and execute it 3-5 times with varied inputs so you have real execution history.
2. In n8n, open the **Executions** view for that workflow and record, for each run: total duration, and whether any node errored.
3. Build a new workflow with a **Schedule Trigger** (or Manual Trigger for testing) that calls the n8n REST API's executions endpoint (`GET /api/v1/executions?workflowId=...`) via an **HTTP Request** node, using your n8n API key credential.
4. Add a **Code** node that computes real aggregate stats from the returned executions: average duration, error rate, and slowest run.
5. Add an **IF** node checking whether average duration exceeds a threshold you choose (e.g. 5 seconds) or error rate exceeds 10%.
6. On the "needs optimization" branch, add a **Set** node listing concrete next actions (e.g. "reduce OpenAI maxTokens," "add caching before the HTTP Request node," "split into sub-workflows") — real suggestions tied to what you actually saw slow down.
7. On the "healthy" branch, add a **Set** node logging "no action needed" with the actual stats.
8. Run this optimization-check workflow against the target workflow's real execution history and confirm the branch it takes matches what you'd expect from the numbers.

## 🔑 Credentials Needed
n8n API key (Settings → API in your n8n instance) for the HTTP Request node calling the Executions API.

## ✅ Definition of Done
- [ ] You have real execution-time data for at least 3 runs of a chosen workflow, not simulated numbers
- [ ] Your aggregate stats (avg duration, error rate) are computed in a Code node from that real data
- [ ] The IF branch threshold is a specific number you chose and can justify
- [ ] The "needs optimization" branch names concrete, workflow-specific actions, not generic advice

## 🐛 Common Pitfalls
- **No n8n API credential set up** — the Executions API requires an API key generated in your n8n instance settings; without it the HTTP Request node will 401.
- **Optimizing based on one run** — a single execution's duration is noise, not a trend; use at least 3-5 runs before drawing conclusions.
- **Generic "optimize performance" output** — if your Set node's suggestions don't reference the actual node names or numbers from your workflow, they're not useful; tie every suggestion back to real data.

## 🏭 Industry Track Application
For a SaaS/Tech track, treat this as literally what you'd do before scaling a client's automation — real execution data first, then targeted fixes (usually reducing LLM calls or adding caching), never a guess-based rewrite.
