# DAY 12: Webhooks & APIs 101
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- The difference between API Key auth and OAuth2 auth in the HTTP Request node, and when each applies
- How to configure automatic retries and timeouts on an HTTP Request node
- How to detect a 4xx/5xx response code and route it instead of letting the workflow silently fail
- How to batch multiple items through Split In Batches instead of one request per item

## 🎥 Watch First
- [n8n Webhook & API tutorial](https://www.youtube.com/watch?v=IvUYJQkf6sA) — Complete 15-minute advanced API tutorial. Watch for how the presenter reads a real API's documentation to figure out which authentication method and headers it needs before building the node.

## 🛠️ Build It: Step-by-Step
1. New workflow. **Manual Trigger** → **HTTP Request** node "Get Public Data": Method `GET`, URL `https://jsonplaceholder.typicode.com/users/1`, no auth. Execute and confirm you get a JSON object with a `name` field.
2. Add a second **HTTP Request** node "Get With Retry": Method `GET`, URL `https://httpbin.org/status/500` (deliberately always errors). Under Options → Retry On Fail, set Max Tries = 3, Wait Between Tries = 2000ms. Execute and confirm the node's error output/execution time shows multiple attempts (3 tries at 2s apart takes 4+ seconds) before finally failing.
3. Add a third **HTTP Request** node "Get With API Key" against a free API key service you can sign up for quickly (e.g., OpenWeatherMap's free tier). Authentication = "Generic Credential Type" → "Header Auth" with your API key header. Execute and confirm you get real data back, not a 401.
4. Add an **IF** node "Handle Rate Limit" after an HTTP Request node, checking `{{ $json.statusCode }}` equals `429`. On true, add a **Set** node logging "rate limited, would retry" — this documents the detection pattern even without a full retry loop.
5. Add a **Split In Batches** node (Batch Size = 2) feeding 4-5 manually-entered items (via a Set node emitting an array, or a Code node) through an HTTP Request node one batch at a time. Execute and confirm in Execution History that the HTTP Request node ran multiple times — once per batch, not once for the whole set.
6. Deliberately introduce a typo into step 1's URL and re-execute — open the node's error output and read the actual error message n8n surfaces, so you know what a real API failure looks like versus a validation failure.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/error_handling_workflow.json` (Menu → Import from File in n8n) to see a working version of the "check a status/severity field with an IF node and branch accordingly" pattern used in step 4, then compare it to what you built.

## 🔑 Credentials Needed
One free-tier API key from a service like OpenWeatherMap (for header auth practice). No paid credentials required.

## ✅ Definition of Done
- [ ] Your GET request to jsonplaceholder.typicode.com returns real JSON with a `name` field, confirmed in the node's Output panel
- [ ] Your retry-configured node shows 3 attempts in its behavior/error detail before failing
- [ ] Your API-key-authenticated request returns a 200, not a 401
- [ ] Your Split In Batches workflow shows the HTTP Request node executing once per batch (not once total) in Execution History
- [ ] You've read one real API error message directly from a broken node's output

## 🐛 Common Pitfalls
- **200 with an error inside:** some APIs return HTTP 200 with an error message in the body rather than an HTTP error code — always check the actual response content, not just that the node didn't turn red.
- **Retry doesn't cover everything:** Retry On Fail triggers on request failures (timeouts, 5xx by default) — a 429 or 401 is technically a "successful" HTTP response with an error status code, so it needs explicit IF-node handling instead.
- **Burning your quota while debugging:** hammering a free-tier API with repeated manual executions can exhaust your daily limit — space out test runs once the happy path is confirmed.

## 🏭 Industry Track Application
Sarah wants her expense tracker talking to banking APIs, receipt scanning services, and budgeting apps. Using today's API-key HTTP Request node as a template, configure a second HTTP Request node pointed at a free receipt-OCR or banking sandbox API (or a mock endpoint like `https://jsonplaceholder.typicode.com/posts` standing in for one), and chain it after step 1's node so data from one "service" feeds into the request to the next — mirroring how Sarah's real system would pull a receipt, then post its parsed amount to a budgeting API.
