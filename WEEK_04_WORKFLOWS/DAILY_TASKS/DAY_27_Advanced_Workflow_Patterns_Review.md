# DAY 27: Advanced Workflow Patterns Review
**Week:** 4 — Workflows  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- A consolidated view of the 5 pattern families from this week: parallel branching, data transformation, end-to-end system design, performance measurement, and health monitoring
- How to pick which 2-3 patterns actually matter for a given real system, instead of using all of them everywhere
- How to sketch a multi-source, multi-branch system architecture before writing a single node
- How to size a "smaller" demonstration workflow that still proves you can combine patterns, without building the full capstone yet

## 🎥 Watch First
- [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) — advanced workflow review section. Skim back through the parallel-processing and system-integration segments specifically; you're consolidating today, not learning new material.

## 🛠️ Build It: Step-by-Step
1. **Recap:** for each of Days 22-26, write one sentence naming the single pattern you'd reuse from that day (e.g. Day 22 → "fan out into N branches, reconverge with node references"; Day 23 → "filter-then-transform with `.map()`/`.join()`"; Day 25 → "measure `$now.diff()` at each stage").
2. **Build a smaller demonstration workflow — not the full capstone** — combining exactly 2-3 of those patterns end-to-end: Webhook Trigger → fan out into 2 parallel branches (Day 22's pattern) → merge and filter/transform the combined array with `.filter()`/`.map()` (Day 23's pattern) → a final Set node that measures `total_time` with `$now.diff()` (Day 25's pattern).
3. Test the demonstration workflow with curl and confirm all patterns visibly execute: both branches run, the filter measurably drops at least one deliberately-bad record you include in the test payload, and `total_time` shows a real millisecond value.
4. **Switch to planning mode for Day 28:** on paper or in a doc, sketch the capstone's architecture around the "Multi-Channel Data Processing System" concept — 2 entry triggers (Webhook + Schedule), 3 parallel ingestion branches, one validation gate, a batch-processing loop, a performance-monitoring stage, and an end-to-end integration call. Label which Day 22-26 pattern powers each stage.
5. In your plan, explicitly list 3 things tomorrow's build will do that today's demonstration workflow does **not**: (a) 3 ingestion sources instead of 2, (b) a SplitInBatches-based batch loop instead of a single pass, (c) a monitoring/metrics stage bolted onto the pipeline.
6. Save your architecture sketch — you'll build directly from it tomorrow.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/advanced_pattern_workflow.json` and `WEEK_04_WORKFLOWS/EXAMPLES/data_processing_workflow.json` (Menu → Import from File in n8n) side by side to see the parallel-branching and filter/transform patterns in their original, isolated forms before you combine them into your own demonstration workflow.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com covers any API calls in the demonstration workflow.

## ✅ Definition of Done
- [ ] A written one-sentence recap exists for each of Days 22-26's core pattern
- [ ] The demonstration workflow executes successfully via curl and visibly exercises at least 2 distinct patterns (branching + transformation, or transformation + timing) in one run
- [ ] A written architecture plan for Day 28's capstone exists, with each stage explicitly labeled to the Day 22-26 pattern it reuses
- [ ] The plan lists at least 3 concrete differences between today's demonstration workflow and tomorrow's planned capstone scope

## 🐛 Common Pitfalls
- **Cramming all 5 days' patterns into today's "smaller" demonstration defeats the point of a review day** — cap yourself at 2-3 patterns and save the full combination for the capstone.
- **A vague plan like "build a data pipeline" isn't buildable tomorrow without re-thinking it from scratch** — your Day 28 plan needs specific node types and field names, not just stage names.
- **Skipping the recap and jumping straight to building loses the review's actual value** — the one-sentence-per-day recap is what makes tomorrow's capstone faster to build.

## 🏭 Industry Track Application
For your chosen industry track, write one sentence per Week 4 day naming the specific business process it would power — e.g. Fintech: Day 22's parallel branching → simultaneously checking 3 fraud-signal sources; Day 26's monitoring → watching failed-transaction rate. Use these sentences as the narrative thread for tomorrow's capstone's Industry Track Application section.
