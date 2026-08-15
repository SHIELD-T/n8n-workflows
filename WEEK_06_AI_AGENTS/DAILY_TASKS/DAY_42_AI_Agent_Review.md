# DAY 42: AI Agent Review
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to combine everything from this week (chat integration, agents+tools, memory/RAG, feedback loops, multi-modal) into one coherent system
- How to document an AI system's architecture so someone else (or future-you) can understand it
- How to do a final pass checking every AI call has error handling
- How to package and demo a multi-step AI workflow

## 🎥 Watch First
No new video today — this is a review and build day. If any of this week's builds didn't fully click, re-watch the relevant segment: [How to Build AI Agents with n8n in 2025! (Full Course)](https://www.youtube.com/watch?v=geR9PeCuHK4) covers the whole arc in one pass and is the best single re-watch if you're consolidating.

## 🛠️ Build It: Step-by-Step
1. Pick ONE real use case for your industry track that needs at least 3 of this week's techniques (e.g. an agent with a tool, memory, and a feedback step).
2. Start from your Day 38 (Agents with Tools) workflow as the base — it already has an **AI Agent** node with a **Chat Model**, **Window Buffer Memory**, and a Tool.
3. Add a RAG-style knowledge lookup from Day 39: connect a **Vector Store Tool** (backed by the same **In-Memory Vector Store** you built) to the AI Agent so it can cite your industry knowledge base alongside its other tools.
4. Add a lightweight feedback step from Day 40: after the agent responds, a **Set** node collects a mock `rating` field and an **If** node routes low ratings to a logging step (Sheets or file).
5. Wrap every external call (OpenAI, HTTP Request Tool, Google Sheets) with n8n's built-in error output (right-click the node → "On Error" → "Continue Using Error Output") so a single failed call doesn't crash the whole run — connect error outputs to a shared **Set** node that builds a friendly `error_response`.
6. Run the complete workflow end-to-end with 2 different test inputs and confirm: the agent uses its tool(s), memory persists across the two calls if they share a `conversation_id`, and the feedback branch fires correctly on at least one low-rated test.
7. Write a short README block (as a **Sticky Note** on the canvas) describing what the workflow does, its inputs, and its tools — this is your system documentation.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_performance_monitor.json` and `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_with_tools.json` side by side to see how monitoring and tool-use patterns are typically wired together, then adapt both into your single combined workflow.

## 🔑 Credentials Needed
OpenAI API key; Google Sheets OAuth2 (or the CSV fallback) from Day 40; whatever Tool-specific credentials you chose in Day 38 (public APIs need none).

## ✅ Definition of Done
- [ ] One workflow combines an AI Agent, at least one Tool, memory, and a feedback/logging branch
- [ ] Every OpenAI/HTTP node has error output handling connected to something other than "let it crash"
- [ ] You've run 2 test inputs end-to-end and both completed without an unhandled failure
- [ ] A Sticky Note on the canvas explains the workflow's purpose, inputs, and tools in 3-5 sentences
- [ ] You can name, out loud or in writing, all 5 Week 6 concepts (integration, multi-model, agents+tools, memory/RAG, feedback loops) and point to where each lives in your final workflow

## 🐛 Common Pitfalls
- **"On Error: Continue" silently swallows real bugs:** Route error outputs somewhere visible (a log row, a Slack message) rather than a dead-end — otherwise you'll ship broken behavior without noticing.
- **Combining too much at once breaks debugging:** If the full workflow fails, temporarily disable the later nodes (right-click → Deactivate) and test the agent + memory in isolation first, then re-enable pieces one at a time.
- **Forgetting to reuse the SAME memory/vector store instance:** Copy-pasting nodes between workflows can create a second, empty vector store or memory bucket — verify your final workflow points at the same data you loaded earlier in the week.

## 🏭 Industry Track Application
Complete your Week 6 AI-powered industry project end-to-end: package the combined agent (tools + memory + RAG + feedback) around the specific problem you chose at the start of the week (fraud detection, health coaching, tutoring, etc.), test it with 3 realistic inputs from that domain, and note in your Sticky Note documentation exactly which industry problem it solves.
