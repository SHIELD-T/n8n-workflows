# DAY 16: Built-in Nodes Mastery
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to configure the HTTP Request node for GET calls with a JSON response format
- How IF node conditions (string/number/array operators) control branching
- How Set node expressions transform and shape data between nodes
- How SplitInBatches processes a large data set in fixed-size chunks

## 🎥 Watch First
- [n8n Quick Start Tutorial: Build Your First Workflow](https://www.youtube.com/watch?v=4cQWJViybAQ) — focus on the sections demonstrating HTTP, IF, and SET node configuration (14m47s).

## 🛠️ Build It: Step-by-Step
1. Manual Trigger → Set node "Set API Configuration" with `api_url` = `https://jsonplaceholder.typicode.com/posts`, `batch_size` = 5.
2. Add HTTP Request node "Fetch Data via HTTP": Method GET, URL = `{{ $json.api_url }}`, Response Format JSON. Execute and confirm the output panel shows an array of ~100 post objects.
3. Add IF node "Check Data Validity": condition — array `{{ $json }}` is not empty. Leave the false branch for now; you'll wire an error handler there in step 6.
4. Add SplitInBatches node "Split Data into Batches": batchSize = `{{ $('Set API Configuration').item.json.batch_size }}`. This turns the ~100-item array into batches of 5.
5. After the batch loop, add a Set node "Process Each Batch" capturing `batch_size` = `{{ $json.length }}` and `batch_id` = `{{ $now.format('YYYYMMDDHHmmss') }}`.
6. Add a second IF node "Check Batch Content": number condition `{{ $json.batch_size }}` larger than 0. Wire its false branch to a Set node "Handle Empty Batch" with `warning_message` = "Batch contains no data".
7. Execute the whole workflow and confirm in Execution History that SplitInBatches ran multiple times (once per batch of 5) — check its output count across iterations.
8. Test the first IF node's false path deliberately: temporarily change the HTTP Request URL to `https://jsonplaceholder.typicode.com/invalid-endpoint` and confirm the empty response routes to your error-handling branch instead of the success path.

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/conditional_processing_workflow.json` (Menu → Import from File in n8n) to see a working IF-based branching pattern with dedicated success/error paths, then compare it to your "Check Data Validity" branch.

## 🔑 Credentials Needed
None — JSONPlaceholder is a free public test API with no authentication required.

## ✅ Definition of Done
- [ ] HTTP Request node successfully returns JSON data from `jsonplaceholder.typicode.com/posts` (~100 items)
- [ ] SplitInBatches visibly runs multiple times in Execution History, each batch containing exactly 5 items (except possibly the last)
- [ ] "Check Data Validity" routes an empty/invalid API response to a distinct error-handling Set node, verified by testing with a broken URL
- [ ] You can state, in your own words, when you'd use SplitInBatches instead of processing all items at once

## 🐛 Common Pitfalls
- **SplitInBatches needs a loop-back connection** in older n8n versions to process every batch — check that its connections form a loop back to itself, not a single pass-through.
- **Array IF conditions check the array itself, not item fields** — an array containing one empty object still passes "isNotEmpty."
- **Renaming a node breaks references silently** — `{{ $('Set API Configuration').item.json.batch_size }}` fails if you've since renamed that node.

## 🏭 Industry Track Application
Create Alex's inventory management system using all four core nodes: HTTP Request to pull stock levels from a (mock) supplier API, IF to flag items below a reorder threshold, Set to format the reorder request, and SplitInBatches to process the flagged items in batches of 3 so you don't overwhelm the supplier's API.
