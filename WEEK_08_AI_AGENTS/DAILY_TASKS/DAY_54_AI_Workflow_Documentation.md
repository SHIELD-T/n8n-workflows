# DAY 54: AI Workflow Documentation
**Week:** 8 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- What production AI workflow documentation actually needs: trigger contract, node-by-node purpose, credentials, failure modes
- How to use n8n's Sticky Note nodes to document a workflow directly on the canvas
- How to write a runbook entry a teammate could follow without you present

## 🎥 Watch First
- [How to Build AI Automations & Agents (Step-by-Step)](https://www.youtube.com/watch?v=bKX8t3QA04s) — watch the "Documenting AI workflows" section; note the fields they include in their documentation template.

## 🛠️ Build It: Step-by-Step
1. Pick 5 of your existing AI workflows (from Weeks 6-8). For each, add a **Sticky Note** node at top-left summarizing: purpose (1 sentence), trigger type + expected payload shape, and the AI model/provider used.
2. For each of the 5, write a doc (in your own notes) covering: the **input contract** (exact JSON shape the webhook expects), the **output contract** (exact JSON shape on success and on error), and every credential the workflow needs by name.
3. Add inline Sticky Notes next to any non-obvious node (a Set node doing a calculation, an IF node with a business rule) explaining what the expression does and why — target every node whose purpose isn't obvious from its name alone.
4. Write one runbook entry for your most complex workflow: "If this fails, first check X, then Y, then Z" — based on the actual failure modes you've hit in Days 51-53 (rate limits, malformed payloads, credential expiry).
5. Take a screenshot of one documented workflow's canvas (with Sticky Notes visible) and save it alongside your written docs as a visual reference.
6. Run the "stranger test" on your Day 51 deployment workflow's documentation: could you activate, test, and roll it back using only what you wrote? Fix any gap you find.

**Stuck?** Compare your documentation structure against the `course_metadata` block at the top of any `WEEK_08_AI_AGENTS/EXAMPLES/*.json` file (e.g. `ai_agent_quality_assurance_system.json`) — it models fields like `learning_objectives`, `prerequisites`, and `use_cases` that map onto a real documentation template.

## 🔑 Credentials Needed
None — no external services today. This is a documentation task built on workflows you've already created.

## ✅ Definition of Done
- [ ] 5 workflows each have a top-level Sticky Note describing purpose, trigger, and AI model used
- [ ] Each of the 5 has a written input/output contract (exact JSON shapes) outside n8n
- [ ] Your most complex workflow has a runbook entry listing 3 concrete failure checks
- [ ] You ran the "stranger test" on one workflow's docs and fixed at least one gap you found

## 🐛 Common Pitfalls
- **Documenting what "should" happen instead of what actually happens:** always verify against the live node configuration, not memory.
- **Skipping the error-case output contract:** most undocumented production incidents come from callers not knowing what an error response looks like.
- **Sticky Notes that restate the node name** ("This is a Set node") instead of explaining the why — document intent, not the obvious.

## 🏭 Industry Track Application
Write your Day 51 workflow's documentation as if handing it to a compliance reviewer for your industry track (e.g. what PII/PHI does a HealthTech workflow log, what audit trail does a Fintech workflow need) — call out one compliance-relevant gap you found while writing it.
