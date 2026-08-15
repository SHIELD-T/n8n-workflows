# DAY 24: End-to-End Automation Systems
**Week:** 4 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to design a workflow spanning capture → validation → enrichment → duplicate-check → integration → notification
- How to use an IF node to branch on a "record already exists" check before creating a new record
- How to fan a single successful outcome out into multiple downstream actions
- How to keep a system testable end-to-end even when some steps call external services you don't have credentials for yet

## 🎥 Watch First
- [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) — building end-to-end systems section. Note how the instructor keeps "capture," "process," and "notify" as visually distinct sections of the canvas.

## 🛠️ Build It: Step-by-Step
1. Webhook node "Multi-Source Lead Capture": path `lead-capture`, method POST.
2. IF node "Lead Data Validation": both `{{ $json.email }}` and `{{ $json.name }}` not empty.
3. Set node "Enrich Lead Data": `lead_id` = `{{ $now.format('YYYYMMDDHHmmss') + Math.floor(Math.random() * 1000) }}`, `lead_score` = `{{ Math.floor(Math.random() * 100) }}`, `priority` = `{{ $json.lead_score > 70 ? 'high' : $json.lead_score > 40 ? 'medium' : 'low' }}`.
4. Since you likely don't have a real CRM API, simulate the duplicate check with a Set node: `is_duplicate` = `{{ $json.email === 'duplicate@test.com' }}` — this lets you test both branches deterministically without a real backend.
5. IF node "Process New Lead": false branch of `is_duplicate` → "Create CRM Lead" (a mocked HTTP Request to `https://jsonplaceholder.typicode.com/posts` standing in for the real CRM write — it accepts any POST body and echoes it back); true branch → "Handle Duplicate Lead" Set node.
6. Set node "Assign to Sales Team": `assigned_rep` = `{{ $json.priority === 'high' ? 'senior-sales@company.com' : 'sales-team@company.com' }}`, `follow_up_time` = `{{ $now.add(1, 'hour') }}`.
7. Test end-to-end twice with curl: `curl -X POST <webhook-url> -d '{"name":"Ana Lee","email":"ana@test.com"}'` should reach "Assign to Sales Team" with the CRM write succeeding; `curl -X POST <webhook-url> -d '{"name":"Dup Test","email":"duplicate@test.com"}'` should route to "Handle Duplicate Lead" instead.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/end_to_end_system_workflow.json` (Menu → Import from File in n8n) to see a working input → validate → process → output → notify pipeline, then compare its "Final System Report" node's structure to your own lead-management system's summary.

## 🔑 Credentials Needed
None if you follow the mocked-CRM approach above using jsonplaceholder.typicode.com. If you want a real Slack notification, you'll need a Slack Bot Token with `chat:write` scope.

## ✅ Definition of Done
- [ ] A curl POST with a new, valid lead reaches "Assign to Sales Team" and shows the correct `assigned_rep` based on `priority`
- [ ] A curl POST with `email: "duplicate@test.com"` correctly routes to "Handle Duplicate Lead" instead of creating a new record
- [ ] A curl POST missing `name` or `email` is correctly rejected by the "Lead Data Validation" IF node
- [ ] The mocked "Create CRM Lead" HTTP Request node successfully echoes back the posted lead data, visible in its output

## 🐛 Common Pitfalls
- **Building against real third-party APIs before you have credentials stalls the exercise** — mock the external call first with jsonplaceholder.typicode.com, then swap in the real endpoint once credentials exist.
- **`priority` depends on `lead_score`, which is randomly generated** — for deterministic tests, temporarily hardcode `lead_score` instead of using `Math.random()`.
- **Forgetting to configure the webhook's response mode** ("Immediately" vs. "Using Respond to Webhook Node") can leave your curl call hanging waiting for a response you never send.

## 🏭 Industry Track Application
Build Alex's complete order-processing system end-to-end: a webhook captures a new order, an IF node validates required fields (customer, items, total), a Set node enriches it with an `order_id` and `priority` based on total value, a mocked inventory-check IF node branches on stock availability, and the success path writes to a mocked fulfillment API while the failure path notifies Alex's ops team.
