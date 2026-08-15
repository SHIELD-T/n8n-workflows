# DAY 53: AI Workflow Scaling
**Week:** 8 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Where AI workflow scaling bottlenecks actually live: webhook concurrency, downstream HTTP calls, and — most often — your AI provider's rate limit
- How to batch large input sets with Split In Batches so a workflow doesn't choke on high volume
- How to throttle requests so batch processing stays under your provider's requests-per-minute limit

## 🎥 Watch First
- [N8N Tutorial: Building N8N AI Agents (Beginner to Pro)](https://www.youtube.com/watch?v=lSwMtsm6oDU) — watch the "Scaling AI workflows" section; pay attention to how they handle batch processing without hitting rate limits.

## 🛠️ Build It: Step-by-Step
1. Take a Day 51/52 AI workflow (or your Week 7 candidate) and feed it a batch input: a webhook body containing an array of 20+ items, e.g. `{"items":[{"text":"..."},...]}`.
2. Add a **Split In Batches** node right after your Set/Init node, with Batch Size set to 5, so the AI node processes 5 items per loop iteration instead of all 20 at once.
3. Wire the AI node's output back into Split In Batches' loop input so it keeps looping until every batch is processed (the standard n8n loop pattern).
4. Add a **Wait** node (1-2 seconds) inside the loop before the AI call. Check your AI provider's dashboard for its requests-per-minute limit, and calculate whether 5 items per 2 seconds stays under it.
5. Run the workflow with the 20-item payload. In Executions, check total execution time and confirm no items failed due to rate-limiting (look for 429 errors in any HTTP Request/AI node output).
6. Add a final aggregation step (Merge or Set node) collecting all loop outputs into one array, and a "Generate Report" Set node summarizing: total items, success count, failure count, total processing time.
7. Temporarily push the batch size to 20 (no batching) and re-run to observe what breaks or slows down — then revert to the batched, throttled version and note the difference in your maintenance log.

**Stuck?** Import `WEEK_08_AI_AGENTS/EXAMPLES/intelligent_automation_system.json` for a working multi-step AI processing chain (decision → learning → adaptation) you can adapt by inserting a Split In Batches node before the AI call.

## 🔑 Credentials Needed
Your AI provider credential — today, its rate limit is the whole point, so check your plan's requests-per-minute before you start.

## ✅ Definition of Done
- [ ] A workflow processes a 20+ item batch using Split In Batches with a batch size smaller than the full input
- [ ] A Wait/throttle step exists between AI calls, and you've calculated it stays under your provider's rate limit
- [ ] The unbatched vs. batched run comparison is documented (what failed or slowed at full volume)
- [ ] A final aggregation step reports success/failure counts across the whole batch

## 🐛 Common Pitfalls
- **Missing the loop-back connection:** on Split In Batches, this makes the workflow process only the first batch and silently stop — it looks "done" when it isn't.
- **Not checking rate limits before scaling:** hitting 429 Too Many Requests mid-batch can silently drop items if the AI node has no retry/error handling.
- **Scaling n8n concurrency instead of the real bottleneck:** increasing execution concurrency without addressing the AI API's rate limit just moves the failure point, it doesn't fix it.

## 🏭 Industry Track Application
Simulate the realistic peak volume for your industry track (e.g. 500 transactions/hour for Fintech, 100 concurrent student submissions for EdTech) and calculate the batch size + throttle delay your workflow would need to handle that volume without exceeding your AI provider's rate limit — show the math, not just the final numbers.
