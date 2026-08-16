# Day 88 Notes: Advanced Pricing Strategies

*This day's deliverable is a written value-based pricing analysis, not an n8n workflow — see `DAILY_TASKS/DAY_88_Advanced_Pricing_Strategies.md` for the full lesson.*

## Model Answer

### 3-Tier Pricing (starting point from Week 12's AaaS tiers)

| Tier | Price/mo | Included workflows | Support level |
|---|---|---|---|
| Starter | $297 | 5 | Email, 48h response |
| Professional | $797 | 25 | Email + chat, 24h response |
| Enterprise | $1,997 | Unlimited | Dedicated, same-day |

### Value-Based Justification (Professional tier example)

- Estimated hours saved per month for a typical client: ~25 hrs
- Reasonable hourly rate for their industry: $35/hr
- **Value delivered:** 25 × $35 = $875/month
- **Current price ($797) is ~91% of value delivered** — actually near the ceiling, not underpriced; if anything, consider trimming scope or moving upmarket rather than raising this tier further.

### Alternative Model: Usage-Based

Price per workflow execution: $8/100 executions. A typical Professional-tier client running ~6,000 executions/month would pay ~$480/mo under usage-based pricing — cheaper than the flat $797 tier, meaning usage-based would cannibalize revenue for a client this size, so **flat tiers stay the primary model**; usage-based is offered only as an opt-in for low-volume clients.

### Publishable Pricing Page Copy

"**Professional — $797/mo.** Save 20+ hours/month on repetitive work. Includes 25 automated workflows, chat support with 24-hour response, and a monthly performance report."

### Reconciliation with Week 12

Matches Day 83's Professional tier ($697/mo) with a deliberate $100 increase justified by the value calculation above — not silent drift.

## Your Version

- **Your value-delivered calculation per tier (hours saved × rate):** _______
- **Your flat-vs-usage-based comparison with real example numbers:** _______
- **Your chosen model and 2-3 sentence justification:** _______
- **Your final, publishable pricing page copy:** _______
- **Reconciliation with your Week 12 pricing (matches or deliberate change):** _______
