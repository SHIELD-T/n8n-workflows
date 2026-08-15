# DAY 18: Error Handling and Retry Logic
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to configure the HTTP Request node's built-in retry options (max tries, delay, timeout)
- How "Continue On Fail" plus an IF check replaces a workflow-halting error with a controlled branch
- The difference between transient errors (worth retrying) and validation errors (not worth retrying)
- How to log and notify on both the success path and the failure path

## 🎥 Watch First
- [Mastering Error Handling in n8n: A Pro Guide](https://www.linkedin.com/posts/satyendra-mourya_n8n-workflowautomation-errorhandling-activity-7369948983038791680-bFKX) — ~10 minute error handling guide. Note the distinction it draws between node-level retry settings and workflow-level Error Trigger workflows.

## 🛠️ Build It: Step-by-Step
1. Manual Trigger → Set node "Set API Configuration": `api_url` = `https://api.example.com/data` (deliberately unreachable, to force a real error), `max_retries` = 3, `retry_delay` = 2000.
2. Add HTTP Request node "API Request with Retry": Method GET, URL `{{ $json.api_url }}`. Under Options → Retry On Fail, set Max Tries = 3, Wait Between Tries = 2000ms, Timeout = 10000ms.
3. Execute the workflow and open the node's execution log — confirm it shows 3 retry attempts before finally failing.
4. Enable **Continue On Fail** in the HTTP Request node's Settings so the workflow doesn't halt. Add an IF node "Check API Response" testing whether `{{ $json.error !== undefined }}` — true routes to failure, false to success.
5. On the failure branch, add a Set node "Handle Final Error" building an `error_notification` string with the error type, message, and retry count.
6. On the success branch — test this by temporarily pointing the URL to `https://jsonplaceholder.typicode.com/posts/1` — add a Set node "Log Success" with `success_log` = `✅ API request successful after {{ $json.processing_time }}ms`.
7. Run the workflow twice: once with the broken URL (confirm it reaches "Handle Final Error") and once with the working URL (confirm it reaches "Log Success") — proving both paths function correctly.

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/conditional_processing_workflow.json` (Menu → Import from File in n8n) to see a complete success/error dual-path pattern (Validate → Format Output vs. Handle Error → Send Error Notification), then compare its branching structure to your "Check API Response" node.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com is a free public API for the success-path test; no auth required.

## ✅ Definition of Done
- [ ] HTTP Request node's execution log shows exactly 3 retry attempts when pointed at an unreachable URL
- [ ] The failure branch produces a populated `error_notification` string containing the real error message, not blank/undefined
- [ ] The success branch, tested against a working URL, correctly reaches "Log Success" and skips the error branch
- [ ] Continue On Fail is enabled so a single node failure doesn't halt the entire workflow execution

## 🐛 Common Pitfalls
- **Continue On Fail without a downstream IF check silently swallows errors** — you must explicitly branch on `$json.error` or the workflow reports success even when the API call failed.
- **Retry settings live under the node's Options panel, not a separate node** — many learners look for a dedicated "Retry" node that doesn't exist for most nodes.
- **Testing against a URL that returns instantly (like a real 404) won't show retry delay** — use a genuinely unreachable host/timeout scenario to observe the wait between attempts.

## 🏭 Industry Track Application
Make Alex's lead response system bulletproof — wrap the CRM API call (or a mock endpoint) in retry logic (3 tries, 2s delay), and on final failure, use a Set node to build a fallback notification to Alex's team so no lead is silently lost even when the CRM is temporarily down.
