# DAY 39: AI Memory, Context & RAG
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between short-term (session) memory and long-term (retrieved) knowledge for an AI agent
- How n8n's **Window Buffer Memory** node gives an AI Agent conversational recall
- How Retrieval-Augmented Generation (RAG) works: embed documents, store them in a vector store, retrieve the closest matches, and feed them into the prompt
- How to add source citations to a RAG answer so it's verifiable

## 🎥 Watch First
- [N8N Tutorial: Building N8N AI Agents (Beginner to Pro)](https://www.youtube.com/watch?v=lSwMtsm6oDU) — watch for the memory node walkthrough; pay attention to how session/context IDs are used to keep separate conversations from bleeding into each other.

## 🛠️ Build It: Step-by-Step
1. **Conversation memory:** Build a **Webhook** trigger (Path `ai-memory`) → **AI Agent** node with an **OpenAI Chat Model** sub-node and a **Window Buffer Memory** sub-node. Set the Memory's Session Key to an expression: `{{ $json.conversation_id }}` so each `conversation_id` gets its own history.
2. Test memory: send `{"conversation_id": "conv1", "message": "My name is Alex."}`, then send a second request `{"conversation_id": "conv1", "message": "What's my name?"}`. Confirm the agent correctly answers "Alex" — that's memory working.
3. **RAG setup:** Add a new workflow. Use a **Set** node to hold 3-4 short paragraphs of text (your own "knowledge base," e.g. your industry's FAQ). Chain: **Default Data Loader** → **Recursive Character Text Splitter** (Chunk Size 200) → **Embeddings OpenAI** → **In-Memory Vector Store** (mode: Insert) to load the documents once.
4. Build the retrieval workflow: **Webhook** (Path `rag-query`) → **Question and Answer Chain** (or **AI Agent** with a **Vector Store Tool**) connected to the same **In-Memory Vector Store** (mode: Retrieve, Top K = 3) and an **OpenAI Chat Model**. System prompt: "Answer using only the retrieved context below. If the answer isn't in the context, say you don't know. Cite which chunk you used."
5. Test with a question whose answer is only in your loaded paragraphs (e.g. "What's our refund window?" if one paragraph mentions it). Confirm the answer is grounded in your text, not generic model knowledge, and includes a citation.
6. Try a question NOT covered by your documents and confirm the agent says it doesn't know rather than hallucinating.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_agent_with_tools.json` for the general agent+memory wiring pattern, then look at n8n's official RAG template in the node panel's template gallery for the vector-store-specific nodes if yours look different.

## 🔑 Credentials Needed
OpenAI API key (used for both the Chat Model and the Embeddings node).

## ✅ Definition of Done
- [ ] The conversation-memory test correctly recalls a fact ("Alex") from an earlier message in the same `conversation_id`
- [ ] A second `conversation_id` does NOT see the first conversation's history (memory is properly isolated per session)
- [ ] A RAG query about content that IS in your loaded documents returns a grounded, cited answer
- [ ] A RAG query about content NOT in your documents returns an "I don't know" style answer instead of a hallucination

## 🐛 Common Pitfalls
- **Memory bleeds across users:** Forgetting to key the Session ID off a real per-user/per-conversation field means every request shares one giant memory — always bind Session Key to an actual conversation identifier.
- **In-Memory Vector Store resets on every execution:** It only persists for the life of the workflow's active session in the editor — for a real deployment you'd swap it for a persistent store (Pinecone, Qdrant, Postgres pgvector); note this limitation rather than being surprised your data "disappeared."
- **Chunks too large:** Chunking at 2000+ characters dilutes retrieval relevance — start small (150-300 chars) and increase only if answers lack context.

## 🏭 Industry Track Application
Load your knowledge base with 3-4 real paragraphs from your industry: Fintech → your firm's fee schedule or a summary of an investment product's terms; HealthTech → a patient-history record's key entries or a simplified subset of an intake form so the agent can reference "customer transaction history" / "patient health records" style context; EdTech → a few paragraphs from a course syllabus so the agent can answer "student learning history"-style questions grounded in that content. Confirm the RAG answer cites the right paragraph.
