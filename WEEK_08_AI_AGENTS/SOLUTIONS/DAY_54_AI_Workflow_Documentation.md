# Day 54 Notes: AI Workflow Documentation

*This day's deliverable is written documentation, not a new n8n workflow — see `DAILY_TASKS/DAY_54_AI_Workflow_Documentation.md` for the full lesson.*

## Model Answer

### Example: "Documented AI Agent" Workflow

**Purpose:** A fully-documented AI agent workflow — every node explained inline instead of left to guesswork.

**Trigger contract:** POST webhook at `/ai-workflow-documented-demo` expecting:
```json
{ "request_text": "string", "priority": "low|medium|high" }
```

**AI model used:** OpenAI gpt-4o-mini, temperature 0.3, max 400 tokens — chosen for low latency/cost on a single-turn decision task.

**Per-node rationale:**
- *Prepare Request* — `request_id` uses `$now.format('yyyyLLddHHmmss')` for a sortable, unique log-correlation ID without a database. `request_text`/`priority` fall back to sample values so the workflow is safely testable with an empty POST body.
- *AI Decision Node* — single-turn chat completion producing a short, direct decision.
- *Extract AI Decision* — the one place downstream nodes read the AI's answer from, so a prompt/model change is reconciled in one spot. `request_id`/`priority` are re-pulled from *Prepare Request* by name since the OpenAI node replaces the item's JSON entirely.
- *Build Final Report* — the single documented output shape, kept stable even if the AI prompt changes later.

**Output contract (success):**
```json
{ "status": "success", "request_id": "20260815120000", "decision": "...", "priority": "medium" }
```

**Runbook — if this workflow fails, check in order:**
1. Webhook payload — confirm `request_text` is present and a string (most common failure).
2. AI credential — a 401/403 in the AI node's error output means the OpenAI credential expired or was rotated.
3. Response shape — if `choices[0].message.content` is empty/truncated, max_tokens may be too low or the model returned a refusal.

## Your Version

- **5 workflows, each with a top-level purpose/trigger/AI-model note:** _______
- **Input/output contract (exact JSON) for each of the 5:** _______
- **Runbook entry for your most complex workflow (3 concrete failure checks):** _______
- **"Stranger test" result — what gap did you find and fix?:** _______
- **Compliance-relevant gap for your industry track:** _______
