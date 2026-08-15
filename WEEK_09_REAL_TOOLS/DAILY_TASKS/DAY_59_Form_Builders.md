# DAY 59: TUESDAY - Working with Form Builders
**Week:** 9 — Real-World Tools (Part 1)  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How Tally and Typeform deliver submissions to n8n via webhooks
- The shape of each platform's payload and how to normalize it into clean fields
- How to validate incoming form data before acting on it
- How to trigger a downstream action (email, storage) from a form submission

## 🎥 Watch First
**Watch:** [Form Builder Automation](https://www.youtube.com/watch?v=4cQWJViybAQ) - Complete 14 minute form automation tutorial

Pay attention to: how the webhook trigger node captures the raw payload, and the difference between Tally's flat `data` object and Typeform's nested `form_response.answers` array.

## 🛠️ Build It: Step-by-Step
1. Create a free Tally account and build a simple contact form (name, email, message).
2. In n8n, add a **Webhook** trigger node, copy its production URL, and paste it into Tally's integration/webhook settings.
3. Add a **Set** node after the webhook to pull out `name`, `email`, and `message` from the Tally payload into clean top-level fields.
4. Add an **IF** node that checks `email` and `name` are not empty — this is your validation gate before anything downstream runs.
5. Repeat steps 1-3 for Typeform: create a form, connect its webhook to a second n8n workflow, and extract the answers using `$json.form_response.answers.find(...)` expressions (Typeform nests answers by field ID, unlike Tally).
6. Wire both workflows to send a confirmation email (Gmail node) on successful validation, and log the submission to an Airtable base.
7. Submit a real test entry to each form and confirm the email arrives and the Airtable row appears — don't just check for a "success" in n8n's execution log.
8. Import `real_tools_integration_monitor.json` from this week's `EXAMPLES/` folder to see a more complete pattern for monitoring integration health, and compare it to what you just built.

## 🔑 Credentials Needed
- Tally account (free tier is fine)
- Typeform account (free tier is fine)
- Gmail credential (from Day 58)
- Airtable credential (from Day 58)

## ✅ Definition of Done
- [ ] A live Tally form whose submissions trigger an n8n workflow within seconds
- [ ] A live Typeform form whose submissions trigger a second n8n workflow
- [ ] Both workflows validate required fields before sending a confirmation email
- [ ] Both workflows write the cleaned submission to an Airtable table
- [ ] You tested each form with a real submission, not just a manual "execute workflow" click

## 🐛 Common Pitfalls
- Publishing the workflow with the webhook still in "test" mode — the webhook URL changes between test and production, and forms silently stop firing
- Typeform's payload nests answers by field ID, so a `.find()` expression that doesn't match the exact field ID returns `undefined` — double-check field IDs in a raw payload first
- Not handling multi-select or file-upload question types, which have a different structure than plain text answers

## 🏭 Industry Track Application
Form builders are usually the front door of client intake. A healthtech track might use forms for patient intake screening (mind data sensitivity when logging responses); an e-commerce track for customer feedback or return requests; a marketing track for lead magnets and gated content downloads. Build today's forms around a realistic intake scenario for your industry, not a generic contact form — you'll reuse this pattern when you start client work in Week 11.
