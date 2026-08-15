# DAY 30: Scaling Automation Systems
**Week:** 5 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Horizontal scaling patterns: routing a decision (scale up / down / maintain) off a load metric
- How to persist state across separate executions using n8n's workflow static data (a real caching mechanism, not a fake field)
- How to prove a workflow can actually handle concurrent load, instead of assuming it can

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — Scaling automation systems section. Pay attention to how the scaling decision is made from a load *percentage*, not a raw count — that threshold logic is what you'll rebuild.

## 🛠️ Build It: Step-by-Step
1. Create a workflow named **Scalable Load Handler**. Add a **Webhook** node "Load Balancer Trigger" — HTTP Method `POST`, Path `scalable-processing`.
2. Add a **Set** node "Initialize Scaling System" with `request_id` = `{{ $now.format('yyyyMMddHHmmss') }}`, `current_load` = `{{ $json.load_percentage }}`.
3. Add a **Switch** node "Scaling Decision" with three routing rules: `current_load > 80` → output "scale_up", `current_load < 20` → output "scale_down", fallback output → "maintain".
4. Wire "scale_up" to an **HTTP Request** node "Scale Up Instances" (POST to a [webhook.site](https://webhook.site) URL noting the target instance count); wire "scale_down" to a similar "Scale Down Instances" node; wire "maintain" straight through.
5. Add a **Code** node "Process With Caching" that uses `$getWorkflowStaticData('global')` to keep a real running counter (e.g. `staticData.requestsServed = (staticData.requestsServed || 0) + 1`) — this demonstrates actual state persisted across executions, not just a fake per-run field.
6. Activate the workflow. Fire 10 concurrent requests from a terminal: `for i in {1..10}; do curl -s -X POST http://localhost:5678/webhook/scalable-processing -H "Content-Type: application/json" -d "{\"load_percentage\": $((RANDOM % 100))}" & done; wait`.
7. Open n8n's Execution History, filter to the last few minutes, and confirm 10 separate Success executions with zero failures. Open the most recent one and check the Code node's `requestsServed` value reflects a cumulative count of at least 10.
8. Note the average execution Duration shown in Execution History for those 10 runs — that number is your baseline for tomorrow's optimization work.

**Stuck?** Import `WEEK_05_WORKFLOWS/EXAMPLES/workflow_scaling_management_system.json` (Menu → Import from File in n8n) to see a working version, then compare it to what you built — it logs each scaling action to Notion and Slack instead of webhook.site, a simpler real-world pattern worth studying.

## 🔑 Credentials Needed
None — no external services today. A free webhook.site capture URL is optional.

## ✅ Definition of Done
- [ ] "Scalable Load Handler" is Active with Webhook → Set → Switch (3 branches) → HTTP Request/Code nodes wired
- [ ] The 10-concurrent-curl loop produces 10 Success entries in Execution History with 0 failures
- [ ] The Code node's static-data counter in the last execution's output is 10 or higher
- [ ] You recorded the average execution Duration from Execution History for the 10 test runs

## 🐛 Common Pitfalls
- **Static data isn't a true atomic counter:** under heavy concurrency the count can drift slightly (two executions reading before either writes) — that's expected behavior worth noting, not a bug to chase down today.
- **Switch node fallback output left unwired:** the "maintain" case then has nowhere to go and the execution errors out — every Switch output needs a destination.
- **Forgetting `&` and `wait` in the curl loop:** without them the 10 requests fire one after another instead of concurrently, and you're not actually testing what you think you are.

## 🏭 Industry Track Application
Set the scale-up/scale-down thresholds (currently 80% / 20%) to values that make sense for your industry's traffic pattern — e.g., a lower scale-up threshold (60%) for E-commerce to handle flash-sale spikes, or a stricter never-scale-down-below-2 floor for HealthTech where availability can't dip. Document your chosen thresholds and why in a note on the Switch node.
