# DAY 43: Advanced AI Agent Patterns
**Week:** 7 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How a "master agent" can coordinate several specialized worker agents instead of one giant prompt trying to do everything
- The difference between hierarchical, collaborative, and adaptive agent patterns — and when each one actually helps
- How to pass structured results between agents so a final "synthesis" step has real data to work with, not just prose

## 🎥 Watch First
[How to Build AI Agents with n8n in 2025! (Full Course)](https://www.youtube.com/watch?v=geR9PeCuHK4)
Pay attention to how the course splits a single request into sub-tasks handled by separate branches — that's the pattern you're building today.

## 🛠️ Build It: Step-by-Step
1. In n8n, create a new workflow with a **Webhook** trigger (path `advanced-ai-agent`) that accepts a JSON body with a `request` field.
2. Add a **Set** node to initialize a run: generate an `agent_system_id` (`={{ $now.format('yyyyMMddHHmmss') }}`), and a `required_agents` array listing the roles you'll simulate (e.g. `research`, `analysis`, `decision`).
3. Add an **OpenAI** node ("Master Agent Analysis") with a system prompt telling it to act as an orchestrator: given the request, it should output which sub-tasks are needed and in what order, as JSON.
4. Add three more **OpenAI** nodes (or one node run via **Split In Batches** over your roles array) that each take the master plan plus the original request and produce one worker's output — this simulates the "research agent", "analysis agent", and "decision agent" without needing three separate services.
5. Add a **Merge** node (or a final **Set** node using `$('Master Agent Analysis')`, `$('Research Agent')`, etc.) to collect all worker outputs into one object.
6. Add a final **OpenAI** node ("Master Agent Synthesis") that takes the combined worker outputs and produces one integrated recommendation.
7. Add a **Respond to Webhook** node returning the synthesis as JSON, and test the whole chain with a real request like `"Recommend an automation strategy for a 5-person marketing agency."`
8. Import `WEEK_07_AI_AGENTS/EXAMPLES/advanced_ai_agent_system.json` and compare its node structure to what you built — note where it uses placeholder HTTP calls (`api.agent-deployer.com`) instead of real OpenAI calls, and why that matters for a real deployment.

## 🔑 Credentials Needed
OpenAI API key (or your preferred LLM provider credential in n8n).

## ✅ Definition of Done
- [ ] Your workflow accepts a webhook request and runs a master-agent planning step before any worker step
- [ ] At least two distinct "worker agent" steps produce separate, structured outputs
- [ ] A synthesis step combines worker outputs into one final recommendation
- [ ] You tested the workflow end-to-end with a real request and got a coherent, non-generic response back

## 🐛 Common Pitfalls
- **One giant prompt pretending to be "multiple agents"** — if a single OpenAI call just role-plays all the agents in one response, you haven't actually built orchestration; use separate nodes/calls so each step's output can be inspected and reused independently.
- **Losing data between nodes** — n8n only keeps the previous node's output in `$json` by default; use `$('Node Name').item.json` to reach back to an earlier worker's result in your synthesis step.
- **Treating a placeholder API call as "done"** — the EXAMPLES file's `api.agent-deployer.com` calls will fail outside this course; replace them with real OpenAI/HTTP calls before considering the pattern production-ready.

## 🏭 Industry Track Application
For a Fintech track, make the "workers" fraud-signal research, transaction-risk analysis, and an escalation decision; for HealthTech, make them symptom intake, triage analysis, and a routing decision — the orchestration pattern stays identical, only the worker prompts change.
