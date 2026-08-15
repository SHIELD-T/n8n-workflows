# DAY 65: MONDAY - Advanced Tool Integrations
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to chain multiple external services where each call depends on the previous one's result
- How to pass data between HTTP Request nodes using n8n's `$('Node Name').item.json` reference syntax
- How to compute a rolling data-quality score across chained service calls
- How to report a multi-service integration's outcome to a team channel

## 🎥 Watch First
**Watch:** [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) - Advanced tool integration patterns section

Pay attention to: how the instructor references output from an earlier node further down the chain — this is the exact `$('Node Name')` pattern you'll use today.

## 🛠️ Build It: Step-by-Step
1. Pick 3 real HTTP APIs you can actually call for free (e.g., a public REST API like open-meteo.com for weather, a currency exchange API, and a public quotes API) — avoid fictional placeholder URLs.
2. Build a workflow: Webhook trigger → HTTP Request to Service A → HTTP Request to Service B, where Service B's request body includes a value pulled from Service A's response via `={{ $('Service A').item.json.someField }}`.
3. Add a third HTTP Request to Service C that depends on Service B's output the same way, so you have a true 3-deep dependency chain.
4. Add a Set node that computes a simple "integration health score" from the three responses (e.g., 100 minus 20 for each service that returned an error or empty result).
5. Add an IF node that branches on that score — above a threshold sends a success summary to Slack, below it sends an alert.
6. Run the workflow with all 3 services healthy, then deliberately point one URL at something invalid and re-run — confirm the health score drops and the alert branch fires.
7. Import `advanced_integration_orchestration_system.json` and `advanced_real_tools_automation.json` from this week's `EXAMPLES/` folder and compare their chaining pattern to yours.

## 🔑 Credentials Needed
- API keys/access for whichever 3 real services you choose (many public APIs are free with no key required)
- Slack credential (from Week 9)

## ✅ Definition of Done
- [ ] A workflow with a real 3-service dependency chain (not simulated/placeholder URLs)
- [ ] Data from each earlier node is referenced in the next node's request, not re-fetched or hardcoded
- [ ] A computed health score reflects actual service success/failure
- [ ] You tested both the all-healthy path and the deliberately-broken path

## 🐛 Common Pitfalls
- Using `$json` instead of `$('Node Name').item.json` when you need data from a node that isn't immediately upstream — `$json` only refers to the previous node's output
- Chaining synchronous calls that don't need to be sequential, adding unnecessary latency — only chain what actually depends on prior output
- Not handling the case where an earlier service in the chain fails — later nodes will throw on `undefined` field access

## 🏭 Industry Track Application
Real dependency chains show up constantly in industry work: a fintech workflow might need a currency conversion before a payment API call; a logistics workflow might need a geocoding lookup before a shipping-rate API call. Build your 3-service chain around a plausible sequence from your industry track rather than arbitrary public APIs, if you can find free ones that fit.
