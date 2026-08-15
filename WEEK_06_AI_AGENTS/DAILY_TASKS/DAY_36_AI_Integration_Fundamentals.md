# DAY 36: AI Integration Fundamentals
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- What an LLM API is and how n8n's OpenAI node turns a chat completion into a workflow step
- How to create and test an OpenAI credential in n8n, including billing setup
- How to build a prompt that accepts dynamic input and a "mode" switch (summarize/classify/enhance/analyze)
- How temperature and max tokens shape AI output, and how to chain two AI calls together

## 🎥 Watch First
- [Integrate OpenAI with n8n](https://www.youtube.com/watch?v=4cQWJViybAQ) — watch for exactly how the OpenAI credential is created and which fields (model, message role, temperature) are configured on the node.

## 🛠️ Build It: Step-by-Step
1. Go to platform.openai.com/api-keys, create a new secret key, and add a payment method under Billing (the API returns 429 errors with no funded account, even with a free trial).
2. In n8n, open Credentials → New → search "OpenAi", paste the key, and click **Test**.
3. Build workflow: **Webhook** trigger (HTTP Method POST, Path `ai-workflow`) → **Edit Fields (Set)** node with fields `input_text` = `{{ $json.text }}` and `processing_mode` = `{{ $json.mode || 'summarize' }}`.
4. Add an **OpenAI** node (Resource: Text, Operation: Message a Model / Chat). Model: `gpt-4o-mini`. System message: "You are a helpful assistant that processes text based on the requested mode. Available modes: summarize, classify, enhance, analyze." User message (expression): `Mode: {{ $json.processing_mode }}\nText: {{ $json.input_text }}`. Set Temperature = 0.7, Max Tokens = 500.
5. Add a second **OpenAI** node after it, same model, System message: "You are an AI analyst that provides insights and recommendations based on processed text." User message referencing the first node's output (`{{ $json.message.content }}`) plus the original input. Temperature = 0.5.
6. Activate the workflow (or use "Listen for Test Event"), then send a test POST with `{"text": "Our Q3 support tickets are up 40% with no staffing change.", "mode": "analyze"}` via the webhook's test URL (curl or a REST client). Confirm both OpenAI nodes' output panels show real generated text, not an error.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/ai_text_processing_workflow.json` (Menu → Import from File in n8n) to see a working version, then compare it to what you built.

## 🔑 Credentials Needed
OpenAI API key (with a funded/billing-enabled account).

## ✅ Definition of Done
- [ ] Your OpenAI credential passes n8n's "Test" connection check
- [ ] A POST to your webhook with a `text` and `mode` field returns real AI-generated content in both OpenAI nodes' output (not a 401/429 error)
- [ ] You've tried at least 2 different `mode` values (e.g. `summarize` and `classify`) and confirmed the output changes accordingly
- [ ] You can explain in one sentence what `temperature` does and why the second node uses a lower value than the first

## 🐛 Common Pitfalls
- **401/429 errors:** A brand-new OpenAI account without a payment method on file will reject API calls even though the key looks valid — add billing before testing.
- **Expression returns `undefined`:** Referencing `$json.message.content` before confirming the OpenAI node's actual output field name (check the node's Output panel — the field name changes between "Message a Model" and legacy "Chat" operations).
- **Prompt bleeds mode into output:** If you don't clearly separate "Mode:" and "Text:" in the user message, the model sometimes echoes the mode label back — tighten the system prompt to instruct it not to repeat the mode.

## 🏭 Industry Track Application
Rebuild the mode-switch pattern for your industry: Fintech → mode `fraud_risk` scores a transaction description as low/medium/high risk; HealthTech → mode `symptom_triage` suggests urgency level from a patient-reported symptom string; EdTech → mode `assess` grades a short student answer against a rubric you provide in the system prompt. Swap the system prompt and test with 3 realistic inputs from your industry.
