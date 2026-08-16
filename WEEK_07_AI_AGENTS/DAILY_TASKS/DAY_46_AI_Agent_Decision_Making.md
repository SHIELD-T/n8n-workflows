# DAY 46: AI Agent Decision Making
**Week:** 7 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to turn a decision between multiple options into a real weighted score instead of an LLM's gut feeling
- How to pair an LLM's qualitative risk assessment with your own quantitative scoring for a more defensible recommendation
- How to structure an n8n workflow so the "optimal choice" is computed by a formula you can audit, not hidden inside a prompt

## 🎥 Watch First
[How to Build AI Automations & Agents (Step-by-Step)](https://www.youtube.com/watch?v=bKX8t3QA04s)
Watch for how the decision logic is broken into separate scoring steps before a final recommendation — resist the urge to let one LLM call do all of it.

## 🛠️ Build It: Step-by-Step
1. Create a workflow with a **Webhook** trigger (path `decision-agent`) accepting `scenario` (text) and `options` (an array of 2-4 named choices).
2. Add an **OpenAI** node ("Risk Assessment") that, for each option, returns a risk score 0-100 and a one-line justification, as structured JSON output.
3. Add an **OpenAI** node ("Strategic Analysis") that returns a reward/opportunity score 0-100 per option, also as structured JSON.
4. Add a **Code** node ("Calculate Weighted Scores") that computes a real weighted score per option, e.g. `score = reward*0.5 + (100-risk)*0.3 + feasibility*0.2`, using the actual numbers returned in steps 2-3 (not `Math.random()`).
5. Add a **Set** node that picks the option with the highest computed score as `optimal_choice`.
6. Add a final **OpenAI** node ("Generate Recommendation") that takes the scenario, all scores, and `optimal_choice`, and writes a short justification a human could act on.
7. Add a **Respond to Webhook** node returning `{scenario, scores, optimal_choice, recommendation}` and test with a real 3-option business scenario relevant to your industry track.

## 🔑 Credentials Needed
OpenAI API key.

## ✅ Definition of Done
- [ ] Risk and reward scores come from actual LLM output fields, not randomly generated placeholders
- [ ] The weighted score formula is implemented in a Code/Set node you can point to and explain
- [ ] The workflow correctly identifies the highest-scoring option as `optimal_choice`
- [ ] You tested with a real, specific scenario (not the generic "Strategy A/B/C" placeholder) and got a sensible recommendation

## 🐛 Common Pitfalls
- **Random scores instead of real ones** — the original pattern for this day generated risk/reward scores with `Math.random()`; that produces a different "optimal" answer every run, which defeats the point of a decision system. Use the LLM's actual returned numbers.
- **Weights that don't sum to something sensible** — if your weighted formula's coefficients don't add to 1 (or a consistent total), scores across options become hard to compare; keep the weighting simple and consistent.
- **Letting the final LLM call override the computed score** — the recommendation step should justify `optimal_choice`, not silently pick a different option because it "feels" better; if it disagrees, that's a bug to fix, not a feature.

## 🏭 Industry Track Application
For a Real Estate track, score options like "list now," "renovate first," or "rent instead" using real local market inputs (days-on-market, renovation ROI estimate, rental yield) rather than generic reward/risk placeholders.
