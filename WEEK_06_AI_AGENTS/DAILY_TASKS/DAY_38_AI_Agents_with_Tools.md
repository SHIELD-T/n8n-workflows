# DAY 38: AI Agents with Tools
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between a plain LLM call and a true **AI Agent** that can decide which tool to call
- How to attach Tool nodes (HTTP Request Tool, Code Tool) to n8n's **AI Agent** node
- How the agent's system prompt controls which tools it reaches for and when
- How to inspect the agent's intermediate tool calls in the execution log to debug its reasoning

## 🎥 Watch First
- [N8N Tutorial: Building N8N AI Agents (Beginner to Pro)](https://www.youtube.com/watch?v=lSwMtsm6oDU) — watch for the section on adding Tool nodes to the AI Agent node and how the agent decides which tool to invoke.

## 🛠️ Build It: Step-by-Step
1. Build: **Webhook** trigger (Path `ai-agent`) → **Set** node with `user_request` = `{{ $json.request }}`.
2. Add an **AI Agent** node (search "AI Agent" in the node panel — this is the LangChain-powered agent node, not the plain OpenAI node). Connect an **OpenAI Chat Model** sub-node as its Chat Model (model `gpt-4o-mini`).
3. Add a **Window Buffer Memory** sub-node to the AI Agent so it retains conversation turns within a session (Context Window Length: 5).
4. Add an **HTTP Request Tool** sub-node named "Wikipedia Search": Method GET, URL `https://en.wikipedia.org/w/api.php`, Query Params `action=query`, `list=search`, `srsearch={query}`, `format=json` — describe the tool as "Searches Wikipedia for background information on a topic."
5. Add a **Code Tool** sub-node named "Word Counter" that takes a string input and returns `{ "word_count": $input.split(' ').length }` — describe it as "Counts words in a block of text."
6. Set the Agent's system prompt: "You are a research assistant. Use the Wikipedia Search tool to look up unfamiliar topics before answering, and use the Word Counter tool if the user asks about text length. Always explain which tools you used."
7. Test with `{"request": "How many words are in the phrase 'artificial intelligence agents automate research' and what is n8n?"}` sent to the webhook. Open the AI Agent node's execution output and confirm you can see both tool calls logged in order, and that the final answer references both results.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_with_tools.json` (Menu → Import from File in n8n) to see a working version, then compare its tool-selection logic to what you built.

## 🔑 Credentials Needed
OpenAI API key. (Wikipedia's API is public and needs no credential.)

## ✅ Definition of Done
- [ ] The AI Agent node's execution log shows at least 2 distinct tool invocations for a single test request
- [ ] The final agent response correctly reflects data returned by both tools (not a hallucinated word count or a made-up Wikipedia summary)
- [ ] You've asked the agent a question that needs only one of the two tools and confirmed it skipped the irrelevant one
- [ ] You can point to the exact system prompt line that causes the agent to prefer Wikipedia lookups over guessing

## 🐛 Common Pitfalls
- **Agent never calls a tool:** If the tool's description field is vague ("does stuff"), the agent can't judge when to use it — write a specific one-sentence description for every tool.
- **HTTP Request Tool returns raw HTML instead of JSON:** Wikipedia defaults to a non-JSON response for some endpoints — double check `format=json` is present in the query string.
- **Memory grows unbounded:** Without a Window Buffer Memory (or with too high a context length), long test sessions blow past the model's context window — keep it small (5-10 turns) while testing.

## 🏭 Industry Track Application
Give your agent one industry-specific tool: Fintech → an HTTP Request Tool hitting a public exchange-rate API so the agent can answer currency-conversion questions; HealthTech → a Code Tool that calculates BMI or a dosage ratio from numbers in the request; EdTech → an HTTP Request Tool against a public dictionary/definitions API so the agent can define unfamiliar vocabulary in a student's question.
