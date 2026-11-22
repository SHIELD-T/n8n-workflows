# DAY 39: AI Memory, Context & RAG
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between short-term (session) memory and long-term (retrieved) knowledge for an AI agent
- How n8n's **Simple Memory** node (called Window Buffer Memory in older versions) gives an AI Agent conversational recall
- How Retrieval-Augmented Generation (RAG) works: embed documents, store them in a vector store, retrieve the closest matches, and feed them into the prompt
- How to add source citations to a RAG answer so it's verifiable

## 🎥 Watch First
- [N8N Tutorial: Building N8N AI Agents (Beginner to Pro)](https://www.youtube.com/watch?v=lSwMtsm6oDU) — watch for the memory node walkthrough; pay attention to how session/context IDs are used to keep separate conversations from bleeding into each other.

## 🛠️ Build It: Step-by-Step
1. **Conversation memory:** Build a **Webhook** trigger (Path `ai-memory`) → **AI Agent** node with an **OpenAI Chat Model** sub-node and a **Simple Memory** sub-node. Set the Agent's Prompt to `{{ $json.body.message }}`, and in the Memory choose Session ID: Define below, Key `{{ $json.body.conversation_id }}` so each `conversation_id` gets its own history.
2. Test memory: send `{"conversation_id": "conv1", "message": "My name is Alex."}`, then send a second request `{"conversation_id": "conv1", "message": "What's my name?"}`. Confirm the agent correctly answers "Alex" — that's memory working.
3. **RAG setup:** Add a new workflow. Use a **Set** node to hold 3-4 short paragraphs of text (your own "knowledge base," e.g. your industry's FAQ). Connect it to an **In-Memory Vector Store** node (Operation Mode: Insert Documents, Memory Key: `course_knowledge_base`), then plug two sub-nodes into the vector store: **Embeddings OpenAI**, and a **Default Data Loader** (Type of Data: JSON, Mode: Load Specific Data, Data: `{{ $json.text }}`, Text Splitting: Custom) with a **Recursive Character Text Splitter** (Chunk Size 200) plugged into the loader. Run it once to load the documents.
4. Build the retrieval workflow: **Webhook** (Path `rag-query`) → **AI Agent** (Prompt: `{{ $json.body.question }}`) with an **OpenAI Chat Model** and, as its tool, a second **In-Memory Vector Store** node (Operation Mode: Retrieve Documents (As Tool for AI Agent), the same Memory Key `course_knowledge_base`, Limit 3) with its own **Embeddings OpenAI** sub-node. System prompt: "Answer using only the retrieved context below. If the answer isn't in the context, say you don't know. Cite which chunk you used."
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
- **In-Memory Vector Store is wiped when n8n restarts:** it lives in n8n's RAM, so it survives between requests but not a restart or a Render free-tier sleep — re-run your loader afterwards. For a real deployment you'd swap it for a persistent store (Pinecone, Qdrant, Postgres pgvector); note this limitation rather than being surprised your data "disappeared."
- **Chunks too large:** Chunking at 2000+ characters dilutes retrieval relevance — start small (150-300 chars) and increase only if answers lack context.

## 🏭 Industry Track Application
Load your knowledge base with 3-4 real paragraphs from your industry: Fintech → your firm's fee schedule or a summary of an investment product's terms; HealthTech → a patient-history record's key entries or a simplified subset of an intake form so the agent can reference "customer transaction history" / "patient health records" style context; EdTech → a few paragraphs from a course syllabus so the agent can answer "student learning history"-style questions grounded in that content. Confirm the RAG answer cites the right paragraph.
