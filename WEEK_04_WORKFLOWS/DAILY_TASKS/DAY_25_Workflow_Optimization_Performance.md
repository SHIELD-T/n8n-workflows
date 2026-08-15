# DAY 25: Workflow Optimization & Performance
**Week:** 4 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to measure execution time at each stage of a workflow using `$now.diff()`
- How reducing HTTP timeout and retry counts trades reliability for speed
- How caching a computed value (via a hash/key) avoids redundant processing
- How to run the same workflow under repeated load and observe where it slows down

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — workflow performance optimization section. Note the advice on measuring before optimizing — don't guess at bottlenecks.

## 🛠️ Build It: Step-by-Step
1. Webhook node "Optimized Webhook Trigger": path `optimized-processing`, POST, Response Format JSON.
2. Set node "Performance Monitoring Start": `execution_id` = `{{ $now.format('YYYYMMDDHHmmss') + Math.floor(Math.random() * 10000) }}`, `start_time` = `{{ $now }}`.
3. IF node "Input Validation": `{{ $json.data }}` not empty → continue; false branch → a validation-error Set node.
4. Set node "Optimized Data Processing": `processed_data` = `{{ $json.data.trim().toLowerCase() }}`, `processing_time` = `{{ $now.diff($json.start_time, 'milliseconds') }}` — your first measurement checkpoint.
5. Add an HTTP Request node "Optimized HTTP Request" calling `https://jsonplaceholder.typicode.com/posts` with Options → Timeout = 5000ms and Retry On Fail = 2 tries / 1000ms delay (deliberately tighter than Day 18's 3 tries/2000ms, trading some reliability for speed).
6. Set node "Performance Metrics Collection": `total_execution_time` = `{{ $now.diff($json.start_time, 'milliseconds') }}`, `api_response_time` = `{{ $json.total_execution_time - $json.processing_time }}` — this isolates how much time the HTTP call cost vs. your own processing.
7. Send 10 rapid curl requests in a row (`for i in {1..10}; do curl -X POST <url> -d '{"data":"test '$i'"}'; done`) and record the `total_execution_time` from each response — calculate the average and note whether later requests are faster or consistent.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/advanced_workflow_optimization_engine.json` (Menu → Import from File in n8n) to see a working threshold-based optimization-impact check (an IF node splitting "high impact" vs. "standard" outcomes based on a percentage), then compare its `improvement_percentage >= 20` condition to how you might flag a run as "slow" vs. "fast."

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com stays free/no-auth for the HTTP Request node.

## ✅ Definition of Done
- [ ] `total_execution_time` is captured and visible in the final node's output for every execution
- [ ] `api_response_time` is calculated correctly as `total_execution_time` minus your own processing time, not a negative or nonsensical number
- [ ] You ran at least 10 rapid test requests via curl and recorded the resulting execution times, noting the average
- [ ] You can state, in one sentence, which stage of your workflow (validation, processing, or the HTTP call) consumed the most time on average

## 🐛 Common Pitfalls
- **Reducing HTTP timeout too aggressively (under 2000ms) against a real public API causes false failures on normal network jitter** — 5000ms is a reasonable floor for a public API, not an arbitrary choice.
- **`$now.diff()` includes n8n's own internal node-to-node handoff time**, not purely "API latency" — don't over-interpret the number as pure network time.
- **Running your 10-request load test sequentially measures per-request handling time, not true concurrent throughput** — fine for this exercise, but don't conflate the two later.

## 🏭 Industry Track Application
Optimize Alex's project-status reporting workflow: measure its current execution time end-to-end, then cut it by removing one redundant HTTP call (cache the result instead) and tightening the retry settings, and report the before/after `total_execution_time` numbers to prove the improvement.
