# DAY 44: AI Agent Communication
**Week:** 7 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- The three core inter-agent messaging patterns: request-response, publish-subscribe, and broadcast
- How to validate a message's shape before routing it, so a malformed message fails loudly instead of silently
- How to use n8n's **Switch**/**IF** nodes to route a message to different handling logic based on its type

## 🎥 Watch First
[Build AI Agents & Automate Workflows (Zero to Hero)](https://www.youtube.com/watch?v=DkV7ztrhLh8)
Watch for how the workflow separates "receiving a message" from "deciding what to do with it" — that separation is exactly what you're building today.

## 🛠️ Build It: Step-by-Step
1. Create a new workflow with a **Webhook** trigger (path `agent-communication`) that accepts `sender`, `receiver`, `message_type` (`request`/`response`/`broadcast`), and `content`.
2. Add an **IF** node ("Validate Message") that checks `sender`, `receiver`, and `content` are all non-empty. Route the false branch to a **Set** node producing a clear `{"status":"error","reason":"..."}` payload.
3. On the valid branch, add a **Switch** node keyed on `message_type` with three outputs: `request`, `response`, `broadcast`.
4. For the `request` output, add an **OpenAI** node that treats `content` as a task and produces a reply, then a **Set** node that packages it as a "response" message back to `sender`.
5. For the `broadcast` output, add a **Set** node that fans the message out to a `participating_agents` array (hardcode 3-4 example agent names) instead of one receiver.
6. Add a shared **Set** node after the Switch branches merge back together ("Generate Communication Report") that logs `sender`, `receiver`, `message_type`, and a timestamp into one object.
7. Add a **Respond to Webhook** node and test all three message types by sending three different POST bodies to the webhook URL from n8n's built-in test panel or curl.
8. Import `WEEK_07_AI_AGENTS/EXAMPLES/agent_communication_system.json` and compare its routing logic (`Route Message` IF node) to your Switch-based version — note which approach scales better as you add more message types.

## 🔑 Credentials Needed
OpenAI API key for the request-handling branch. None required for the broadcast/validation branches.

## ✅ Definition of Done
- [ ] Invalid messages (missing sender/receiver/content) are rejected with a clear error, not silently processed
- [ ] Your Switch node correctly routes `request`, `response`, and `broadcast` message types to different logic
- [ ] You tested all three message types and captured each one's output
- [ ] Your final report/log object records sender, receiver, type, and timestamp for every message processed

## 🐛 Common Pitfalls
- **Switch node falls through to a default when the type doesn't match exactly** — `message_type` is case- and whitespace-sensitive; normalize it with a Set node (`.trim().toLowerCase()`) before the Switch.
- **Broadcast logic sending to only one receiver** — broadcast means fan-out; if you're not using **Split In Batches** or looping over `participating_agents`, you're really just doing another request-response.
- **No validation branch tested** — it's easy to only test the happy path; deliberately send one malformed request and confirm your error branch actually fires.

## 🏭 Industry Track Application
In a Logistics track, a "broadcast" might be a shipment-delay alert going to warehouse, dispatch, and customer-service agents simultaneously — build your broadcast branch around that real fan-out scenario instead of a generic placeholder message.
