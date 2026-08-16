# DAY 88: Advanced Pricing Strategies
**Week:** 13 — Advanced Business  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to calculate value-based pricing from real numbers (hours saved × hourly rate) instead of picking a round number
- The tradeoffs between flat monthly tiers, usage-based pricing, and outcome-based pricing for an automation business specifically
- How to write pricing a prospect can actually understand and justify to their own boss

## 🎥 Watch First
[What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc)
Listen for any mention of what clients were willing to pay for vs. what they weren't — that's real pricing signal, use it.

## 🛠️ Build It: Step-by-Step
1. Take your Week 12 AaaS tiers (Day 83) as your starting point. For each tier, calculate a real value-based justification: estimate hours saved per month for a typical client at that tier × a reasonable hourly rate for their industry = value delivered.
2. Compare that value number against your current price — if your price is less than roughly 10-20% of the value delivered, you likely have room to raise it; write down the actual math, not a feeling.
3. Design one alternative pricing model for the same service — e.g. convert your flat Professional tier into a usage-based model (price per workflow execution or per automated task) — and calculate what a typical client's actual monthly bill would be under each model side by side.
4. Pick which model (flat tier vs. usage-based) you'd actually use and write 2-3 sentences justifying the choice based on your target client's likely preference for predictability vs. pay-for-what-you-use.
5. Write the actual pricing page copy you'd publish: tier names, price, 4-5 bullet features per tier, and one sentence connecting price to value ("Save 20+ hours/month for $797").
6. Import `WEEK_13_ADVANCED_BUSINESS/EXAMPLES/advanced_pricing_brand_system.json` and reconcile: does its pricing structure match what you set in Week 12, or has it drifted? Fix any mismatch now.

## 🔑 Credentials Needed
None required for this exercise.

## ✅ Definition of Done
- [ ] Each tier's price is backed by a real value-delivered calculation, not a round number picked by feel
- [ ] You compared at least two pricing models (e.g. flat vs. usage-based) with real example numbers for a typical client
- [ ] You have final, publishable pricing page copy with real dollar amounts
- [ ] Your pricing reconciles with (or explicitly updates) what you set in Week 12 — no silent drift

## 🐛 Common Pitfalls
- **Pricing based on cost-plus instead of value** — "my time costs $50/hour so I'll charge $75" ignores what the automation is actually worth to the client; anchor on value delivered, then sanity-check against your costs.
- **Too many pricing models tested with no real numbers** — comparing flat vs. usage-based is only useful with an actual example client's numbers run through both; skip the comparison and you're just listing options.
- **Letting pricing drift silently between weeks** — if this week's number doesn't match Week 12's, that's not necessarily wrong, but it needs to be a deliberate decision you can explain, not an accident.

## 🏭 Industry Track Application
For a Fintech/HealthTech track where compliance overhead is real, your value calculation should include compliance risk reduction as a line item, not just hours saved — that's often the stronger pricing lever in regulated industries.
