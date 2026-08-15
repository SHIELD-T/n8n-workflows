# DAY 13: Error Handling & Debugging
**Week:** 2 — Foundation  |  **Time:** 3-4 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to intentionally break a workflow so you can practice reading n8n's error output
- How to branch on error severity so different failures trigger different responses
- How to add retry logic and timeouts directly on nodes that call external services
- How to use Execution History to trace exactly which node failed and why

## 🎥 Watch First
- [Mastering Error Handling in n8n: A Pro Guide](https://www.linkedin.com/posts/satyendra-mourya_n8n-workflowautomation-errorhandling-activity-7369948983038791680-bFKX) — ~10 minute professional error handling guide. Watch for the specific pattern used to separate "expected, recoverable" errors from "unexpected, needs a human" errors — that distinction drives today's build.

## 🛠️ Build It: Step-by-Step
1. New workflow. Add **Webhook** node "API Error Webhook" — Method `POST`, Path `api-error`.
2. Add **Set** node "Analyze Error": `error_type` = `{{ $json.error_type || 'UNKNOWN' }}`, `error_message` = `{{ $json.error_message || 'No error message provided' }}`, `error_code` = `{{ $json.error_code || 'N/A' }}`, `severity` = `{{ $json.severity || 'MEDIUM' }}`.
3. Add **IF** node "Check Severity": String `{{ $json.severity }}` equals `HIGH`.
4. On true, add **Set** node "High Severity Alert" with `alert_message` = `🚨 HIGH SEVERITY ERROR: {{ $json.error_message }}`. On false, add **Set** node "Medium Severity Alert" with `alert_message` = `⚠️ MEDIUM SEVERITY: {{ $json.error_message }}`.
5. Connect both branches into a single **Set** node "Log Error" recording `logged_at` = `{{ $now }}`.
6. Activate the workflow and test both severities:
   `curl -X POST <production-url> -H "Content-Type: application/json" -d '{"error_type":"API_TIMEOUT","error_message":"Connection timed out","severity":"HIGH"}'`
   `curl -X POST <production-url> -H "Content-Type: application/json" -d '{"error_type":"VALIDATION","error_message":"Missing field","severity":"LOW"}'`
   Confirm in Execution History that the HIGH call ran through "High Severity Alert" and the other through "Medium Severity Alert".
7. Build a second, deliberately broken workflow: **Manual Trigger** → **HTTP Request** node pointed at `https://httpbin.org/status/500`, with Timeout = 5000ms and Retry On Fail = 3 tries. Execute it, let it fail, then open the failed execution and read the exact error message n8n shows.
8. Add an **IF** node after the HTTP Request checking `{{ $json.statusCode }}` ≥ 400, routing the true branch to a **Set** node "Handle API Error" logging `error_type`, `error_code`, `error_time`. Re-execute and confirm this branch fires and captures the 500.

**Stuck?** Import `WEEK_02_FOUNDATION/EXAMPLES/error_handling_workflow.json` (Menu → Import from File in n8n) to see a working version of the severity-branching pattern from steps 1-6, then compare it to what you built.

## 🔑 Credentials Needed
None — today's workflows use only Webhook, HTTP Request (to public test endpoints), IF, and Set nodes.

## ✅ Definition of Done
- [ ] A curl call with `"severity":"HIGH"` visibly routes through "High Severity Alert" in Execution History; a non-HIGH call routes through "Medium Severity Alert"
- [ ] Your intentionally-broken HTTP Request node has produced at least one real failed execution, and you've read its specific error message (not just its red status)
- [ ] Your status-code IF node correctly identifies a 500 response as an error and routes it to "Handle API Error"
- [ ] You can explain, in your own words, the difference between a node turning red (a technical failure) and an IF node routing to an "error" branch (a business-logic decision)

## 🐛 Common Pitfalls
- **Treating every red node the same:** a timeout, an auth failure, and a malformed expression all show red but need completely different fixes — read the specific error text, not just the color.
- **No workflow-level Error Trigger:** today's IF-based branching only catches errors reflected in response data (like a status code field) — it won't catch the workflow itself crashing (e.g., an unhandled expression error), which needs a dedicated Error Trigger node on a separate error-handling workflow.
- **Retries masking a real problem:** if a node "succeeds" on the 3rd retry, you may be hiding a flaky dependency instead of fixing it — note retry counts so a pattern doesn't turn into a production incident.

## 🏭 Industry Track Application
Sarah's photo organizer needs to survive bad input without losing photos or crashing silently. Take the severity-branching workflow from steps 1-6 and adapt it: replace `error_type`/`error_message` with `upload_source` and `failure_reason` (e.g., `corrupt_file`, `unsupported_format`, `storage_full`), and route `storage_full` to its own HIGH-severity path since it needs immediate action, while `unsupported_format` routes to MEDIUM since it can wait. Test both with curl and confirm each hits the correct branch.
