# DAY 90: Content Marketing
**Week:** 13 — Advanced Business  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to pick content topics from real client pain points instead of generic "automation trends" filler
- How to build a genuinely automated content pipeline in n8n rather than just planning to "post regularly"
- The difference between a content calendar of titles and one finished, publishable piece

## 🎥 Watch First
[n8n Beginner Course (1/9) - Introduction to Automation](https://www.youtube.com/watch?v=4BVTkqbn_tY)
Watch with an eye toward how simple, reliable automation building blocks (trigger → process → output) apply to a content pipeline, not just business workflows.

## 🛠️ Build It: Step-by-Step
1. List 10 real questions or objections prospects/clients have actually asked you (or would plausibly ask) during this course's exercises — these are your content topics, not generic industry trend headlines.
2. Pick 4 of them and assign each a format: a how-to blog post, a case-study-style writeup (can be a composite/hypothetical client if you don't have a real one yet, clearly labeled as illustrative), a short LinkedIn/X post, and a one-page comparison ("us vs. doing it manually" or "us vs. a generic Zapier template").
3. Build an n8n workflow with a **Schedule Trigger** (weekly) → an **OpenAI** node that drafts a first-pass post for whichever topic is next in your queue (a **Google Sheets**/Airtable row with topic + status) → a **Set** node marking status "drafted."
4. Add a **Slack** or **Email** node that sends you the draft for review rather than auto-publishing — human review before anything public goes out.
5. Run the pipeline once for real, get one real draft out of it, then manually edit and finish it into a genuinely publishable piece (not a title, the actual full piece).
6. Import `WEEK_13_ADVANCED_BUSINESS/EXAMPLES/content_marketing_strategy_system.json` and compare its content calendar/theme structure against your 4 topics — adjust if you're missing a theme category (education, proof, comparison).

## 🔑 Credentials Needed
OpenAI API key; Google Sheets/Airtable credential for the topic queue; Slack or Email credential for draft delivery.

## ✅ Definition of Done
- [ ] Your 10 topics come from real questions/objections, not a generic trend list
- [ ] You have a working n8n draft-generation pipeline, not just a plan for one
- [ ] You ran the pipeline and it produced a real draft you then finished into a publishable piece
- [ ] At least one piece is genuinely done — not a title on a calendar

## 🐛 Common Pitfalls
- **Content calendar full of titles, zero finished pieces** — a calendar proves planning, not execution; this day's Definition of Done requires one real, finished piece to exist.
- **Auto-publishing AI drafts with no human review** — always route through a review step (Slack/email) before anything goes live publicly; unreviewed AI content damages the brand you just built on Day 89.
- **Generic industry-trend topics instead of real objections** — "5 Automation Trends for 2026" doesn't convert; a post answering "is this too complicated for a non-technical team?" (a real objection) does.

## 🏭 Industry Track Application
Your case-study-style piece should use language and metrics your industry track's buyers actually care about — "reduced patient no-shows by 18%" for HealthTech, not a generic "improved efficiency" claim.
