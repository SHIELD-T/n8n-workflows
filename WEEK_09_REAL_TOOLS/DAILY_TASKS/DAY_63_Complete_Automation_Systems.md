# DAY 63: SATURDAY - Combine Tools into Full Systems
**Week:** 9 — Real-World Tools (Part 1)  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to design a multi-tool system on paper before touching n8n
- How to chain 5+ services into one end-to-end automation without losing track of data flow
- How to add error handling and monitoring around a system with multiple failure points
- How the individual pieces from this week (auth, forms, email/calendar, Notion, bots) combine into one deliverable

## 🎥 Watch First
**Watch:** [n8n Quick Start Tutorial (selected sections)](https://www.youtube.com/watch?v=4cQWJViybAQ) - Focus on system architecture (14m47s)

Pay attention to: how the video breaks a big automation into named, testable sub-steps rather than one giant node chain — you'll do the same today.

## 🛠️ Build It: Step-by-Step
1. On paper (or a doc), sketch the data flow for a lead-generation system: Form submission → lead enrichment (AI) → CRM storage → welcome email → sales team Slack alert → follow-up task in Notion. Mark each arrow with what data crosses it.
2. Build the workflow in n8n exactly as sketched: Webhook trigger → Set node (clean lead fields) → OpenAI node (score/enrich the lead) → Airtable node (store) → Gmail node (welcome email) → Slack node (notify sales) → Notion node (create follow-up task).
3. Add a Telegram notification step so the system uses at least 5 distinct external tools end-to-end (form source, AI, CRM/Airtable, email, Slack, Notion, Telegram all count).
4. Add error-handling: wrap the risky steps (API calls) with n8n's error output or an IF check on HTTP status, and route failures to a dedicated "system alerts" Slack channel instead of failing silently.
5. Submit a real test lead through the form and trace it through every step — confirm the Airtable row, the email, the Slack alert, and the Notion task all reflect the same lead consistently.
6. Deliberately break one step (e.g., temporarily disable the Airtable credential) and confirm your error handling catches it and alerts you, rather than the workflow just failing invisibly.
7. Import `lead_generation_automation_system.json` and `customer_support_automation_system.json` from this week's `EXAMPLES/` folder and compare their node structure to what you built — note anything they handle that yours doesn't.

## 🔑 Credentials Needed
- All credentials set up earlier this week: Gmail, Slack, Notion, Airtable, OpenAI, Telegram

## ✅ Definition of Done
- [ ] A written data-flow sketch exists before the workflow was built
- [ ] The workflow chains 5+ distinct tools in one end-to-end run
- [ ] A test lead flows correctly through every step, verified in each destination system (not just n8n's execution log)
- [ ] A deliberately broken step triggers a visible alert instead of a silent failure
- [ ] You compared your build against at least one EXAMPLES workflow and can name one difference

## 🐛 Common Pitfalls
- Skipping the design sketch and building node-by-node "as you go" — multi-tool systems get tangled fast without a plan
- One slow node (e.g. an AI call) blocking the whole chain — consider what should run in parallel vs. sequence
- Testing only the happy path — a system this complex needs at least one deliberate failure test before you trust it

## 🏭 Industry Track Application
This is the day your industry track's "hero workflow" starts taking shape. Sketch your system around a realistic end-to-end process for your chosen vertical — e.g., a healthtech intake-to-appointment pipeline, an e-commerce order-to-fulfillment-alert pipeline, or a real-estate lead-to-showing-scheduled pipeline — instead of the generic lead-gen example. You'll extend this system in Week 10.
