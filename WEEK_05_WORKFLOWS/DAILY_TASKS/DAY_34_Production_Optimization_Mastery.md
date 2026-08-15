# DAY 34: Production Optimization Mastery
**Week:** 5 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Turning several raw metrics into a single weighted optimization score
- Branching a workflow so expensive optimization steps only run when they're actually needed
- Reading per-node execution time in n8n's execution view to find a real bottleneck

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — Production optimization mastery section. Pay attention to how the optimization score formula weights each metric differently — it's not a flat average.

## 🛠️ Build It: Step-by-Step
1. Create a workflow named **Advanced Optimization Engine**. Add a **Webhook** node "Optimization Trigger" — POST, path `advanced-optimization`.
2. Add a **Code** node "Compute Optimization Score" that reads `cpu_percentage`, `memory_percentage`, `disk_percentage`, `network_latency_ms`, and `avg_response_time_ms` from the incoming JSON and computes a weighted 0-100 score, guarding every division with `Math.max(1, value)` so a zero latency doesn't produce `NaN`.
3. Add an **IF** node "Below Threshold?" checking the score is less than 80.
4. On the true branch, add four **Set** nodes that each perform one real, measurable action rather than an HTTP call to a fake API: "Trim Payload" (uses `.slice()`/removes unused JSON keys to simulate a performance fix), "Dedupe Fields" (removes duplicate keys to simulate a resource fix), "Round Numbers" (simulates an efficiency fix), and "Flag for Scale Review" (simulates a scalability fix).
5. Converge both the true and false branches back onto a single **Set** node "Generate Optimization Report" that records whether optimization ran and what the final score was.
6. Test with a bad score: `curl -X POST http://localhost:5678/webhook/advanced-optimization -d '{"cpu_percentage":90,"memory_percentage":85,"disk_percentage":70,"network_latency_ms":800,"avg_response_time_ms":1200}'`. Confirm the score computes below 80 and, in Execution History's execution graph, all four optimization Set nodes show as executed.
7. Test with a good score (`cpu_percentage: 10, memory_percentage: 15, disk_percentage: 10, network_latency_ms: 20, avg_response_time_ms: 50`) and confirm those same four nodes are skipped (greyed out in the execution graph).
8. Compare the Duration column between the two test executions in Execution History — the "optimize" run should take measurably longer since it ran 4 extra nodes; note the difference in the report.

**Stuck?** Import `WEEK_05_WORKFLOWS/EXAMPLES/workflow_optimization_system.json` (Menu → Import from File in n8n) to see a working version of the score-then-branch-then-optimize pattern, then compare it to what you built.

## 🔑 Credentials Needed
None — no external services today.

## ✅ Definition of Done
- [ ] "Advanced Optimization Engine" correctly branches on a computed 0-100 score
- [ ] A bad-metrics test payload triggers all 4 optimization Set nodes (visible as executed in the execution graph)
- [ ] A good-metrics test payload skips those same 4 nodes
- [ ] You recorded and compared the Duration difference between the two test runs in Execution History

## 🐛 Common Pitfalls
- **IF node comparing a string score:** cast the computed score to a Number in the expression, or the "smaller than" comparison silently misbehaves.
- **Branches that never reconverge:** if the true and false paths don't both feed the same downstream "Generate Optimization Report" node, you end up needing two separate report nodes and duplicated logic — converge them instead.
- **Division by zero in the score formula:** `network_latency_ms` or `avg_response_time_ms` being `0` in a test payload produces `NaN` that silently propagates — guard every division.

## 🏭 Industry Track Application
Reweight the optimization score formula for your industry — e.g., weight `avg_response_time_ms` more heavily for E-commerce (checkout latency directly costs revenue), or weight `error_rate`/reliability metrics more heavily for HealthTech/FinTech where a wrong-but-fast result is worse than a slow-but-correct one. Document your reweighted formula and why in a note on the Code node.
