# DAY 21: Workflow Building Review
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to combine multiple triggers, core nodes, expressions, and error handling into one cohesive workflow
- How to sketch a multi-branch workflow's architecture before building it
- How to validate a multi-branch workflow end-to-end, including its error paths
- How to write a short technical summary of a system you built

## 🎥 Watch First
- [n8n Quick Start Tutorial (Workflow sections)](https://www.youtube.com/watch?v=4cQWJViybAQ) — re-watch the trigger and node-chaining sections relevant to a multi-part workflow review (14m47s).

## 🛠️ Build It: Step-by-Step
1. Sketch (on paper or in a note) your Week 3 capstone workflow's architecture before building: 2 trigger types (Webhook + Schedule), one HTTP API call, one IF validation, one SplitInBatches loop, and both a success and error path. Keep the sketch to compare against what you actually build.
2. Build the trigger layer: a Webhook node (path `advanced-workflow`, POST) and a Schedule Trigger (every 12 hours), both feeding a shared Set node "Advanced Data Processing" that normalizes both inputs into the same field names (`input_data`, `processing_type`).
3. Add an IF node "Complex Data Validation" with 2 conditions (data not empty AND `processing_type` equals `advanced_workflow`) — both must pass to continue.
4. Add an HTTP Request node calling `https://jsonplaceholder.typicode.com/posts` with retry (3 tries, 2000ms delay) configured in Options.
5. Add a SplitInBatches node (batch size 5) followed by a Set node computing at least 2 expressions from this week (e.g. a `complexity_score` using math + string length, and `processing_time` using `$now.diff()`).
6. Wire the IF node's false branch to a distinct error-handling Set node (reuse your Day 18 error-notification pattern), and wire the success path to a "Final Report Generation" Set node combining results into one readable multi-line report string.
7. Test the complete workflow twice: once via curl to the webhook with valid data (confirm it reaches "Final Report Generation"), and once with an empty payload (confirm it reaches the error branch instead).

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/workflow_performance_monitoring_system.json` (Menu → Import from File in n8n) to see a production-style workflow with a threshold-based IF branch and two distinct outcome paths (high-performance alert vs. standard log entry) — compare its branching structure to your success/error branches.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com stays free/no-auth for the HTTP Request node.

## ✅ Definition of Done
- [ ] Workflow accepts input from both the Webhook and Schedule triggers and normalizes them into the same downstream field names
- [ ] A curl POST with valid data reaches "Final Report Generation" and produces a report string containing at least 3 interpolated values
- [ ] A curl POST with an empty/invalid payload is correctly routed to the error-handling branch instead
- [ ] SplitInBatches visibly processes the API results in batches of 5, confirmed in Execution History
- [ ] Your original architecture sketch matches (or you can explain where/why it diverged from) what you actually built

## 🐛 Common Pitfalls
- **Two trigger types feeding one shared node need normalized field names** — if the Webhook payload uses `data` and the Schedule branch invents its own `input_data`, downstream validation will silently fail for one of the two paths.
- **This many nodes on one canvas gets tangled fast** — use Sticky Notes to label functional sections (Trigger Layer, Validation, Processing, Error Handling) so the flow stays readable.
- **Retry settings reset if you delete and re-add the HTTP Request node** — reconfigure them each time you rebuild that node.

## 🏭 Industry Track Application
Complete Alex's business automation system by combining this week's skills into one workflow: a Webhook for new leads AND a Schedule Trigger for a daily project-status pull, both validated, processed through retry-protected API calls, and reported via one unified "Alex Business Report" Set node — proving Alex can rely on a single dashboard-style workflow instead of juggling five separate ones.
