# DAY 82: Productized Services
**Week:** 12 — Scaling  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between a custom client project and a productized service you can sell repeatedly at a fixed price
- How to price a productized offer using real setup effort and delivery time, not a guess
- How to write a one-page service sheet a prospect could actually buy from

## 🎥 Watch First
[n8n Beginner Course (1/9) - Introduction to Automation](https://www.youtube.com/watch?v=4BVTkqbn_tY)
Watch for the kind of workflow that's generic enough to sell to many businesses without heavy customization — that's a productization candidate.

## 🛠️ Build It: Step-by-Step
1. Review the templates you built on Day 79. Pick the one most generic across different client types (least custom logic per client).
2. Write a real product sheet for it: product name, one-sentence description, a bullet list of exactly what's included (be specific about integrations, e.g. "Airtable + Gmail + Slack," not "CRM integration"), what's excluded, and turnaround time.
3. Price it using real math: estimate your actual setup hours × your hourly rate = setup fee; estimate ongoing maintenance time × rate = monthly fee. Write both numbers down, not round guesses.
4. Build the actual delivery checklist as an n8n **Sticky Note** or a Notion checklist: discovery call → configure template variables (from Day 79) → test with client's real data → handover call → 30-day support window.
5. Create one intake form (Tally, Typeform, or a Google Form) that would collect exactly the information you'd need from a client to configure this product — build it for real, don't just describe it.
6. Import `WEEK_12_SCALING/EXAMPLES/aaas_service_management_system.json` and compare its tiering/pricing structure to your one-product sheet; note anything your pricing is missing (setup fee vs. recurring, what's in scope).

## 🔑 Credentials Needed
Whichever form tool you use (Tally/Typeform/Google Forms) — free tier is enough.

## ✅ Definition of Done
- [ ] You have one real product sheet with a specific name, scope, and price (not a range like "$X-$Y depending")
- [ ] Your pricing math is shown, not just a final number
- [ ] You have a real, working intake form a prospect could fill out today
- [ ] You have a written delivery checklist from discovery call to handover

## 🐛 Common Pitfalls
- **Scope so vague it can't be quoted** — "automation setup" isn't a product; a buyer needs to know exactly which integrations and how many workflows are included before they'll pay a fixed price.
- **Underpricing based on your first, fastest delivery** — the first time you build something is usually faster than average due to familiarity; price around a realistic repeat-delivery time, not your best case.
- **No excluded-scope list** — without stating what's NOT included, every client will ask for "just one more thing" for free; write the boundary down now.

## 🏭 Industry Track Application
For an E-commerce track, productize an "abandoned cart recovery" package with a fixed integration list (Shopify + Klaviyo/Gmail + a discount-code generator) rather than a generic "marketing automation" offer.
