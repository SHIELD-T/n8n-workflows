# DAY 68: THURSDAY - Workflow Orchestration
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between sequential, parallel, and conditional execution of sub-workflows
- How to call one n8n workflow from another using the Execute Workflow node
- How to aggregate results from multiple sub-workflow runs into one summary
- Why breaking a giant workflow into smaller orchestrated pieces is usually better than one massive canvas

## 🎥 Watch First
**Watch:** [n8n Beginner Course (1/9) - Introduction to Automation](https://www.youtube.com/watch?v=4BVTkqbn_tY) - Workflow orchestration patterns section

Pay attention to: how breaking work into named sub-workflows makes debugging easier — you can re-run just the piece that failed instead of the whole system.

## 🛠️ Build It: Step-by-Step
1. Build three small, independent "worker" workflows, each doing one clear thing (e.g., "Validate Lead," "Enrich Lead via AI," "Notify Sales Team"), each triggered by an Execute Workflow Trigger node so they can be called from elsewhere.
2. Build a parent "Orchestrator" workflow that calls Worker 1 using the **Execute Workflow** node, passing input data and receiving its output.
3. Chain Worker 2 after Worker 1 in the orchestrator, passing Worker 1's output as Worker 2's input (sequential orchestration).
4. Add a branch where two more worker calls run in parallel (e.g., simultaneously logging to Airtable and posting to Slack) rather than sequentially — use n8n's ability to fan out to multiple nodes from one point and let them run concurrently.
5. Add an IF node in the orchestrator that conditionally calls a 4th worker only if a certain condition is met (e.g., only notify sales if the lead score is above a threshold) — this is your conditional orchestration pattern.
6. Aggregate all worker outputs into one final Set node summarizing what ran, what succeeded, and total execution time.
7. Deliberately make one worker workflow fail (e.g., point it at a bad Airtable base ID) and confirm the orchestrator still reports which piece failed rather than crashing without explanation.

## 🔑 Credentials Needed
- Airtable credential (from Week 9)
- Slack credential (from Week 9)
- OpenAI credential (from Week 9), if your enrichment worker uses AI

## ✅ Definition of Done
- [ ] At least 3 separate, independently-triggerable worker workflows exist
- [ ] One orchestrator workflow demonstrates sequential, parallel, and conditional calling of those workers
- [ ] The orchestrator aggregates and reports on all worker results in one place
- [ ] A deliberately broken worker produces a clear, attributable failure message, not a silent crash

## 🐛 Common Pitfalls
- Building "orchestration" as one giant flat workflow instead of actually separating concerns into callable sub-workflows — this defeats the purpose
- Forgetting that Execute Workflow calls are synchronous by default (the orchestrator waits) — plan around this if you need true parallelism
- Not passing enough context (like a request ID) between orchestrator and workers, making it hard to trace one run through logs

## 🏭 Industry Track Application
Orchestration patterns matter most once a client system has grown past a single simple workflow — which will happen fast in a real engagement. Sketch your 3 workers around a realistic industry pipeline (e.g., for logistics: "Validate Shipment," "Calculate Route," "Notify Customer") instead of the generic lead example, so this becomes a directly reusable pattern for client work.
