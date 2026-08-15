# DAY 70: SATURDAY - Performance Optimization
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 3-4 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to measure a workflow's actual execution time per node, not just guess where it's slow
- How caching avoids redundant API calls for data that doesn't change often
- How batching reduces the number of round trips for bulk operations
- How to validate that an optimization actually improved something, with before/after numbers

## 🎥 Watch First
**Watch:** [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) - Optimizing integration performance section

Pay attention to: the specific before/after numbers the creator shows — you'll be producing your own version of that comparison today.

## 🛠️ Build It: Step-by-Step
1. Pick your 2-3 slowest workflows from this week (check execution times in n8n's execution list) and record their current total run time as your baseline.
2. For a workflow that repeatedly fetches the same slow-changing data (e.g., a lookup table), add a simple caching layer: store the result in a Static Data / Airtable "cache" record with a timestamp, and skip the API call if the cache is less than N minutes old.
3. For a workflow processing a list of items one at a time, convert it to use n8n's **Split In Batches** node to process items in batches instead of triggering a separate downstream call per item where the API supports bulk requests.
4. Remove or consolidate redundant nodes — look for cases where you compute or fetch the same value more than once in a single execution.
5. Re-run each optimized workflow and record the new execution time next to your Day 1 baseline.
6. Write a short before/after comparison (a table is fine) showing: workflow name, original time, optimized time, and percentage improvement.
7. Import `performance_optimization_system.json` from this week's `EXAMPLES/` folder and note one optimization technique it uses that you haven't tried yet.

## 🔑 Credentials Needed
- Whichever credentials your target workflows already use (Airtable, APIs from this week)

## ✅ Definition of Done
- [ ] Baseline execution times recorded for 2-3 workflows before any changes
- [ ] At least one caching optimization implemented and verified to skip redundant calls
- [ ] At least one batching optimization implemented for a per-item processing workflow
- [ ] A written before/after comparison with real numbers, not estimates

## 🐛 Common Pitfalls
- Optimizing without measuring first — you can't know if a change helped without a baseline
- Caching data that actually needs to be real-time (e.g., caching a stock price for 24 hours) — match cache duration to how often the data truly changes
- Over-engineering a workflow that only runs once a week — optimization effort should be proportional to actual runtime cost

## 🏭 Industry Track Application
Performance matters most where volume matters most. An e-commerce track processing hundreds of orders a day benefits enormously from batching; a professional-services track running a handful of workflows a day may not need heavy optimization at all. Be honest in your write-up about which of your industry track's workflows would actually benefit from today's techniques versus which are already fast enough.
