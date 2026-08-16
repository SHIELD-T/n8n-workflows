# DAY 45: AI Agent Learning
**Week:** 7 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- Why "learning" in an n8n agent usually means feeding recent outcomes back into the next prompt, not training a model
- How to store and reuse performance history so an agent's behavior can actually change run over run
- How to turn raw performance numbers into a concrete "what to change next time" instruction for an LLM

## 🎥 Watch First
[N8N Tutorial: Building N8N AI Agents (Beginner to Pro)](https://www.youtube.com/watch?v=lSwMtsm6oDU)
Watch for how memory/context gets passed into the agent between runs — that's the mechanism you're recreating.

## 🛠️ Build It: Step-by-Step
1. Create a workflow with a **Webhook** trigger (path `learning-agent`) accepting `training_data` (text) and `metrics` (an object like `{"accuracy":75,"efficiency":80}`).
2. Add an **Airtable** (or Google Sheets) node that reads the last 5 logged runs for this agent — this is your "learning history." If you don't have a base set up yet, use a **Set** node with a hardcoded array to simulate it, and note that as a TODO.
3. Add an **OpenAI** node ("Analyze Performance Trend") whose prompt includes both the current `metrics` and the historical rows, asking it to identify whether performance is improving, flat, or declining, and why.
4. Add a **Set** node ("Compute Improvement") that calculates a simple delta between this run's metrics and the average of the historical rows (real arithmetic, not a random number).
5. Add a second **OpenAI** node ("Generate Adaptation") that takes the trend analysis and improvement delta and outputs one concrete behavior change for the next run (e.g. "increase temperature," "add a validation step," "shorten prompts").
6. Add an **Airtable**/Google Sheets **Append** node that writes this run's `metrics`, trend summary, and adaptation back into your history table, so the next run has one more data point to learn from.
7. Run the workflow twice with different `metrics` values and confirm the second run's trend analysis references the first run's stored data.

## 🔑 Credentials Needed
OpenAI API key; Airtable or Google Sheets credential for the history log (a local Set-node array is an acceptable substitute if you don't have either set up).

## ✅ Definition of Done
- [ ] Each run reads real historical data (not hardcoded) before analyzing trend
- [ ] The improvement delta is calculated from actual numbers, not `Math.random()`
- [ ] The adaptation output names one specific, actionable change — not a generic "keep improving" statement
- [ ] Running the workflow twice shows the second run's analysis referencing the first run's stored result

## 🐛 Common Pitfalls
- **Faking "learning" with random numbers** — the original pattern for this day used `Math.random()` to simulate improvement; replace it with a real comparison against stored history or the exercise teaches nothing.
- **History table growing unbounded with no read-back** — logging without ever reading the log isn't learning, it's just record-keeping; make sure step 2 genuinely happens before step 3.
- **Adaptation suggestions too vague to act on** — "improve accuracy" isn't actionable; push the prompt in step 5 for a specific, testable change.

## 🏭 Industry Track Application
For an E-commerce track, log which product-recommendation prompts led to clicks vs. ignores, and let the adaptation step suggest concrete prompt changes (e.g. "lead with price" vs. "lead with reviews") based on that real history.
