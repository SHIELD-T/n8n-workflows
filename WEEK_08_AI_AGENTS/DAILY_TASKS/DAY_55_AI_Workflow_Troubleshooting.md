# DAY 55: AI Workflow Troubleshooting
**Week:** 8 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to read n8n's execution log (input/output per node) to isolate exactly which node failed and why
- Common AI-specific failure modes: rate limits (429), malformed JSON from the model, truncated responses, timeouts
- How to reproduce a bug on demand instead of guessing at a fix

## 🎥 Watch First
- [n8n Tutorial for Beginners: Complete AI Automation Guide](https://www.youtube.com/watch?v=CfD17vBCPEU) — watch the "Troubleshooting AI workflows" section; pay attention to how they use the execution data panel to trace a failure back to its source node.

## 🛠️ Build It: Step-by-Step
1. Deliberately break one of your deployed AI workflows in 3 different ways, one at a time, capturing what the execution log shows for each: (a) send a webhook payload missing a required field, (b) temporarily set an invalid/expired API key on the AI credential, (c) set the AI node's max tokens absurdly low (e.g. 5) so the response gets truncated mid-JSON.
2. For each break, open the failed execution, click the failing node, and read the exact error message and the input data it received — copy the raw error text into your troubleshooting notes.
3. Fix each break one at a time (restore the field, restore the valid API key, raise max tokens) and re-run to confirm the workflow returns to a healthy green execution after each fix.
4. Add a "self-check" IF node right after the AI node that validates the response isn't empty/malformed (e.g. `{{ $json.choices[0].message.content.length > 0 }}`) before passing it downstream, so malformed AI output fails fast with a clear error instead of corrupting downstream data silently.
5. Write a troubleshooting guide as a table with columns: Symptom | Likely Cause | Where to Look | Fix — populate it with the 3 failure modes you just reproduced, plus rate-limiting (429) and timeout scenarios from Day 53's scaling work.
6. Test your own guide: introduce a 4th deliberate failure you haven't written a row for (e.g. point the HTTP Request node at a wrong URL), and use only the guide to diagnose it. Time how long it takes and note whether the guide was actually sufficient.

**Stuck?** Import `WEEK_08_AI_AGENTS/EXAMPLES/ai_agent_quality_assurance_system.json` and deliberately misconfigure its Notion or Slack credential to see what n8n's error output looks like for a bad credential — good practice data for your guide's "invalid credential" row.

## 🔑 Credentials Needed
Your AI provider credential (you'll temporarily invalidate/restore it as part of the exercise) — no new credentials.

## ✅ Definition of Done
- [ ] You captured the exact error text for 3 deliberately-introduced failures (missing field, bad credential, truncated response)
- [ ] All 3 breaks were fixed and confirmed healthy again via a fresh execution
- [ ] A response-validation IF node exists on at least one workflow, catching malformed AI output before it propagates
- [ ] A Symptom/Cause/Where-to-Look/Fix table exists covering at least 5 failure modes
- [ ] You validated the guide against a 4th failure you hadn't written a row for, and updated the guide if it was missing

## 🐛 Common Pitfalls
- **Fixing the symptom without confirming the root cause:** restoring a workflow to green without reading the actual error can mask a recurring issue that resurfaces at higher volume.
- **Only re-testing the happy path after a fix:** always re-trigger with the exact payload that caused the original failure, not a fresh clean one.
- **Generic troubleshooting rows** ("check your API key") instead of specific ones ("if the error contains `invalid_api_key`, regenerate it in your provider's dashboard, update the n8n credential, then reactivate the workflow").

## 🏭 Industry Track Application
Add one industry-specific failure scenario to your troubleshooting guide that a real client in your track would actually hit (e.g. a Fintech workflow receiving a currency your fraud-check logic doesn't handle, or a HealthTech workflow receiving a malformed date-of-birth) and write the fix.
