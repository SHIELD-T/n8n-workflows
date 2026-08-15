# DAY 37: Advanced AI Workflows
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to call more than one LLM provider from the same n8n workflow (OpenAI node vs. HTTP Request to another provider's API)
- How to branch workflow logic on input complexity using the **If** node
- How to aggregate multiple AI responses into one structured result and pick a "best" answer
- Why running models in parallel (not just in sequence) cuts total workflow time

## 🎥 Watch First
- [n8n Tutorial for Beginners 2025: Build AI Agents Step-by-Step](https://www.youtube.com/watch?v=PfdnYe2690E) — this file's own topic (multi-model workflows) isn't the video's main subject, so specifically watch for the segment on calling external AI APIs with the HTTP Request node — that's the technique you'll reuse for the non-OpenAI model below.

## 🛠️ Build It: Step-by-Step
1. Build: **Webhook** trigger (Path `advanced-ai-workflow`) → **Set** node with `input_text` = `{{ $json.text }}` and `text_complexity` = `{{ $json.complexity || 'high' }}`.
2. Add an **If** node: condition `{{ $json.text_complexity }}` equals `high`.
3. On the **true** branch, add an **OpenAI** node (model `gpt-4o`, Temperature 0.3, Max Tokens 1000) with system prompt "You are an advanced AI assistant specializing in complex text analysis, summarization, and insights generation."
4. In parallel (branching off the same Set node, not chained after OpenAI), add an **HTTP Request** node calling Anthropic directly: Method POST, URL `https://api.anthropic.com/v1/messages`, Header `x-api-key` = your Anthropic key (create an HTTP Header Auth or Generic credential), Header `anthropic-version` = `2023-06-01`, JSON body `{"model": "claude-3-5-sonnet-20241022", "max_tokens": 1000, "messages": [{"role": "user", "content": "={{ $json.input_text }}"}]}`.
5. Add a **Merge** node (mode: Combine, Combine by Position) to join the OpenAI and Claude branches into one item, then a **Set** node that builds `all_responses` with both texts and a `best_response` expression that picks whichever response is longer (a simple stand-in for a real quality metric): `{{ $json.openai_response.length > $json.claude_response.length ? $json.openai_response : $json.claude_response }}`.
6. Execute with a test payload `{"text": "Summarize the tradeoffs of microservice vs monolith architecture.", "complexity": "high"}` and confirm the final Set node shows both providers' raw text plus one selected `best_response`.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_with_tools.json` for a working pattern of chaining an OpenAI node's output into a synthesis step, then adapt it to two providers instead of one.

## 🔑 Credentials Needed
OpenAI API key, Anthropic (Claude) API key.

## ✅ Definition of Done
- [ ] The workflow calls both OpenAI and Claude for the same input and both branches return real text (not HTTP errors)
- [ ] The Merge node successfully combines both branches into a single item you can inspect
- [ ] `best_response` resolves to one of the two actual responses, not `undefined`
- [ ] You've toggled `text_complexity` to something other than `high` and confirmed the If node correctly routes differently (even if you only built the true branch, verify the false path is reachable)

## 🐛 Common Pitfalls
- **Anthropic 401:** The header must be `x-api-key`, not `Authorization: Bearer` — Claude's API auth scheme differs from OpenAI's.
- **Merge node combines wrong items:** "Combine by Position" requires both input branches to output exactly one item each; if either branch fan-outs to multiple items your join will misalign — add a **Limit** node (Max Items: 1) before the Merge if needed.
- **Rate limits mid-test:** Rapid re-execution while testing can trip both providers' per-minute rate limits — space out test runs by a few seconds if you see 429s.

## 🏭 Industry Track Application
Use the dual-provider pattern for a real comparison task in your industry: Fintech → have both models score the same loan application description for risk and compare their reasoning; HealthTech → have both models draft a plain-language explanation of the same lab result and pick the clearer one; EdTech → have both models generate a quiz question from the same lesson text and keep the one with better-structured distractors.
