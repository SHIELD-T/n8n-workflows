# DAY 40: AI Feedback Loops
**Week:** 6 — AI Agents  |  **Time:** 3-4 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to turn user ratings and performance metrics into structured feedback data
- How to store feedback so it can inform future prompt behavior (a practical stand-in for "learning")
- How to build conditional logic that reacts differently to good vs. poor feedback
- How to close the loop: feed a feedback summary back into the AI as few-shot guidance

## 🎥 Watch First
- [How to Build AI Automations & Agents (Step-by-Step)](https://www.youtube.com/watch?v=bKX8t3QA04s) — watch for any section on evaluating and iterating on AI outputs; note how the presenter decides a response needs improvement.

## 🛠️ Build It: Step-by-Step
1. Build: **Webhook** trigger (Path `ai-feedback`) → **Set** node with `user_rating` = `{{ $json.rating }}` (1-5), `response_time_ms` = `{{ $json.response_time_ms }}`, `had_error` = `{{ $json.had_error || false }}`.
2. Add an **If** node: `{{ $json.user_rating }}` is greater than or equal to `4` → true branch = "good", false branch = "needs improvement."
3. On the false branch, add a **Google Sheets** node (Append row) writing to a "Feedback Log" sheet with columns `timestamp`, `rating`, `response_time_ms`, `had_error`, `original_prompt`. (No Google account handy? Use an **Edit Fields (Set)** node + **Read/Write Files from Disk** to append to a local CSV instead.)
4. Add an **AI Agent** or **OpenAI** node named "Generate Improvement Note": system prompt "You analyze a poor AI response's feedback and produce one specific, actionable instruction to add to the system prompt next time." Feed it the rating, response time, and error flag.
5. Chain a final **Set** node that assembles `improvement_plan` from the AI's suggestion and logs `overall_status` as `"needs_improvement"` or `"excellent"` based on the branch taken.
6. Test twice: once with `{"rating": 5, "response_time_ms": 800, "had_error": false}` (should hit the "good" branch and skip logging) and once with `{"rating": 2, "response_time_ms": 4000, "had_error": true}` (should log a row and produce an improvement note). Open the Google Sheet (or CSV) and confirm the second run's row is there.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_performance_monitor.json` (Menu → Import from File in n8n) — it shows the same "log to Sheets/Notion and notify" pattern this build follows.

## 🔑 Credentials Needed
OpenAI API key; Google Sheets OAuth2 credential (or skip and use local file writes instead).

## ✅ Definition of Done
- [ ] A high-rating test run does NOT create a feedback log row
- [ ] A low-rating test run DOES create a feedback log row with all 5 columns populated correctly
- [ ] The "Generate Improvement Note" step produces a specific, non-generic suggestion tied to the actual rating/error data you sent (not a boilerplate response)
- [ ] You can explain which field in the workflow determines the "good" vs "needs improvement" branch

## 🐛 Common Pitfalls
- **Google Sheets auth loop:** OAuth2 credentials in n8n need the redirect URL registered in Google Cloud Console exactly matching your n8n instance's URL — mismatches cause a silent redirect failure. Use the CSV fallback if this blocks you.
- **If node comparing string vs number:** `user_rating` arriving as a string from a webhook JSON body ("4" vs `4`) can break numeric comparisons — add an explicit type-cast expression like `{{ Number($json.user_rating) }}`.
- **Improvement notes are too vague:** If the system prompt for the "Generate Improvement Note" step doesn't demand specificity, the model defaults to generic advice like "be more helpful" — explicitly instruct it to reference the actual numbers.

## 🏭 Industry Track Application
Point the feedback loop at your industry's failure mode: Fintech → log every case where a fraud-risk classification was rated wrong by a human reviewer, and generate an improvement note refining the risk criteria; HealthTech → log low-rated health recommendations and generate a note tightening the disclaimer/safety language; EdTech → log cases where an auto-graded answer was overridden by a teacher and generate a note adjusting the grading rubric description.
