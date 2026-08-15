# DAY 28: Advanced Workflow Capstone Project
**Week:** 4 — Workflows  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to translate an architecture plan into an actual multi-branch, multi-stage n8n workflow
- How to combine parallel ingestion, validation, batch processing, and monitoring into one production-style system
- How to verify a complex system end-to-end rather than node-by-node
- How to write a short technical README for a system you built, suitable for a portfolio

## 🎥 Watch First
- [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) — advanced workflow review section. This time watch specifically for how the instructor structures a large canvas into readable sections — you'll need that discipline building today's larger system.

## 🛠️ Build It: Step-by-Step
Build directly from your Day 27 plan (based on the original "Multi-Channel Data Processing System"):
1. Pull up your Day 27 architecture sketch. Build the trigger layer first: a Webhook node "Multi-Source Data Ingestion" (path `advanced-data-ingestion`, POST) and a Schedule Trigger "Schedule Data Processing" (every 1 hour), both feeding a shared Set node "Initialize Advanced Processing" with `processing_id`, `data_sources` = `{{ ['API', 'Database', 'Files', 'Webhooks'] }}`, `start_time`.
2. Build **3 parallel ingestion branches** — this is the step Day 27's demo only did with 2: Branch 1 = HTTP Request to `https://jsonplaceholder.typicode.com/posts/1`; Branch 2 = HTTP Request to `https://jsonplaceholder.typicode.com/posts/2`; Branch 3 = Set node with hardcoded `file_data`.
3. Add IF node "Advanced Data Validation" checking `{{ $json.data || $json.file_data }}` is not empty; false branch → "Handle Validation Error" Set node.
4. Add Set node "Complex Data Transformation" computing a `transformed_data` object (original + processed + a `data_quality_score` = `{{ Math.floor(Math.random() * 100) }}`).
5. Add SplitInBatches "Split for Batch Processing" (batch size 3) → Set node "Optimized Batch Processing" capturing `batch_id` and `batch_processing_time` = `{{ $now.diff($json.start_time, 'milliseconds') }}` — reusing Day 25's performance-measurement pattern.
6. Add Set node "Performance Monitoring" bundling `processing_id`, `batch_id`, `processing_time`, `data_quality_score` into one `performance_metrics` object — reusing Day 26's monitoring pattern, now embedded inside the pipeline instead of run as a separate scheduled check.
7. Add HTTP Request "End-to-End Integration" (POST to `https://jsonplaceholder.typicode.com/posts`, standing in for the real destination system) with retry (3 tries, 2000ms) sending `processing_id`, `batch_id`, `transformed_data`, `performance_metrics`.
8. Add a final "Final System Report" Set node aggregating everything into one `system_report` object. Test the whole pipeline end-to-end: `curl -X POST <webhook-url> -d '{"data":"capstone test payload"}'` — confirm the response chain shows data flowing through all 3 ingestion branches, batch processing, and the final integration call succeeding.
9. Write a short README-style summary (4-6 sentences) of your capstone system: what it ingests, how it validates/transforms/batches, and how it reports back — this is your portfolio artifact for Week 4.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/end_to_end_system_workflow.json` (Menu → Import from File in n8n) to see the complete input → validate → process → output → notify shape this capstone is built around, then compare its "Final System Report" node to your own.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com covers every HTTP call in the mocked capstone. If you want a real integration, a Slack Bot Token (`chat:write` scope) can replace the mocked notification step.

## ✅ Definition of Done
- [ ] All 3 parallel ingestion branches execute and their data reaches the validation step, confirmed in Execution History
- [ ] A curl POST with valid data flows end-to-end through validation, transformation, batch processing (SplitInBatches visibly iterating), integration, and the final report
- [ ] A curl POST with empty/invalid data is correctly routed to "Handle Validation Error" instead of proceeding through the pipeline
- [ ] The 4-6 sentence system README accurately describes what you built, matching what actually executes
- [ ] Your build differs concretely from Day 27's demonstration workflow in at least the 3 ways you listed in yesterday's plan (3 sources not 2, a batch loop, a monitoring stage)

## 🐛 Common Pitfalls
- **Building this many stages in one sitting without testing incrementally hides one broken node behind ten working ones** — test after steps 1, 3, 5, and 7, not just once at the very end.
- **The Schedule Trigger and Webhook Trigger both feeding "Initialize Advanced Processing" need compatible field names** — confirm both paths actually produce a `data_sources` field before building further downstream.
- **A capstone this size gets visually unreadable fast** — group nodes with Sticky Notes into "Ingestion," "Validation & Transform," "Batch & Monitor," and "Integration & Report" sections so the canvas tells the story on its own.

## 🏭 Industry Track Application
Build Alex's — or your chosen industry track's — full production system using this capstone shape: 3 real ingestion sources for your track (e.g. Fintech: card transactions + bank feed + manual entry), validated and transformed together, batch-processed for efficiency, monitored for data quality, and integrated into one final system-of-record call — then write your 4-6 sentence README framed as a deliverable you'd hand to that client.
