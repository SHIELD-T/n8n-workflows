# DAY 22: Advanced Workflow Patterns
**Week:** 4 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to fan a single trigger out into multiple parallel branches and reconverge them
- How to loop over aggregated results using SplitInBatches after a parallel-processing step
- How node references (`$('Node Name').item.json...`) pull data from any earlier branch, not just the immediately preceding node
- When conditional validation should run before vs. after parallel branches

## 🎥 Watch First
- [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) — advanced workflow patterns section. Watch how the parallel branches are wired from a single node and how their outputs are re-merged before the next step.

## 🛠️ Build It: Step-by-Step
1. Manual Trigger → Set node "Initialize Processing" with `processing_id` = `{{ $now.format('YYYYMMDDHHmmss') }}`, `data_sources` = `{{ ['API', 'Database', 'Files'] }}`, `start_time` = `{{ $now }}`.
2. From "Initialize Processing", drag 3 separate connections off its output to build 3 parallel branches: Branch 1 = HTTP Request GET `https://jsonplaceholder.typicode.com/posts/1`; Branch 2 = Set node with a hardcoded `db_data` object; Branch 3 = Set node with a hardcoded `file_data` object.
3. After each branch, add a dedicated "Process X Data" Set node that reshapes that branch's output into a common shape: `{ source, id, title/content, processed_at }`.
4. Add a downstream Set node "Aggregate Parallel Results" using 3 separate node references — `$('Process API Data').item.json...`, `$('Process Database Data').item.json...`, `$('Process File Data').item.json...` — to combine all 3 branches into one `aggregated_data` object. Execute and confirm the aggregated object contains all 3 sources simultaneously.
5. Add an IF node "Conditional Data Validation" checking `{{ $json.source }}` is not empty — wire its false branch to a distinct "Handle Validation Error" Set node.
6. Add a SplitInBatches node (batch size 1) after aggregation to loop through each source one at a time, followed by a "Process Each Data Source" Set node capturing `current_source` and `loop_iteration`.
7. Execute the full workflow and confirm in Execution History that all 3 branches ran before the aggregation step, and that the batch loop iterated exactly 3 times (once per source).

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/advanced_pattern_workflow.json` (Menu → Import from File in n8n) to see a working 3-branch parallel-then-aggregate-then-loop pattern, then compare its "Aggregate Results" node's use of `$('Process Branch 1').item.json...` to your own aggregation step.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com is free/no-auth for the API branch.

## ✅ Definition of Done
- [ ] All 3 parallel branches execute independently and their outputs appear separately in Execution History before aggregation
- [ ] The aggregated Set node's output object contains data from all 3 sources simultaneously, not just the last branch to finish
- [ ] The IF node's false branch is reachable — verified by temporarily blanking one branch's `source` field and confirming it routes to "Handle Validation Error"
- [ ] SplitInBatches iterates exactly 3 times over the aggregated sources, confirmed in Execution History

## 🐛 Common Pitfalls
- **Branch execution order is deterministic, not truly parallel** in n8n's default single-threaded execution — don't assume it's random; it follows the order the connections were wired.
- **Node references only work once the referenced node has actually executed** on the current run — `$('Process API Data').item.json` fails if used somewhere upstream of that node.
- **SplitInBatches loops over output items, not an array field inside one item** — to loop over 3 sources bundled inside `aggregated_data`, you need a node like Item Lists' "Split Out" first to turn that object into 3 separate items.

## 🏭 Industry Track Application
Build Alex's parallel data-collection pipeline: fan out from one trigger into 3 branches (new leads from the website form, new leads from a phone-call log, new leads from a trade-show CSV import), reshape each into the same lead schema, then aggregate and validate them together so Alex's sales team sees one unified lead queue regardless of source.
