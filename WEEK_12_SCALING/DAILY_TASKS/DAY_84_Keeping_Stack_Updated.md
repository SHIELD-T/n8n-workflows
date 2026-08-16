# DAY 84: Keeping Your Stack Updated
**Week:** 12 — Scaling  |  **Time:** 3-4 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- Why "I'll keep up with updates eventually" fails, and what a real, scheduled update-check habit looks like
- How to safely test a new n8n version or AI model against your existing workflows before switching everything over
- How to build a lightweight system that actually surfaces relevant updates instead of you doom-scrolling changelogs

## 🎥 Watch First
[What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc)
Watch for any mention of things that broke or changed over time — that's exactly the risk this day's system is built to catch early.

## 🛠️ Build It: Step-by-Step
1. Pick 3 real sources relevant to your stack: the n8n release notes/changelog, your primary LLM provider's changelog (e.g. OpenAI), and one community source (n8n forum, a relevant subreddit, or a newsletter).
2. Build an n8n workflow with an **RSS Feed Read** node (or **HTTP Request** if a source has no RSS) pointed at one real changelog/feed URL, on a **Schedule Trigger** (daily).
3. Add an **OpenAI** node that summarizes new entries into 2-3 lines and flags whether anything looks relevant to workflows you're running (mention specific node types you use, e.g. "OpenAI node," "Airtable node").
4. Add a **Slack** or **Email** node that sends yourself this daily digest — a real, working notification, not a description of one.
5. Pick one workflow you built earlier in the course. Duplicate it, and in the duplicate, swap one component for a newer alternative (e.g. bump the OpenAI model version, or swap a deprecated node for its current replacement) and run both versions side by side with the same test input.
6. Write a 5-line comparison: output quality, cost/latency difference if visible, and whether you'd actually migrate production traffic to the new version.
7. Import `WEEK_12_SCALING/EXAMPLES/scaling_operations_management.json` if it references version/update handling, and note any practice worth adopting into your own digest workflow.

## 🔑 Credentials Needed
Slack or Email credential for the digest; OpenAI API key for summarization; no credential needed for public RSS feeds.

## ✅ Definition of Done
- [ ] You have a working scheduled workflow that pulls from at least one real changelog/feed source
- [ ] You've received at least one real digest message (not a hypothetical description)
- [ ] You ran an old-vs-new component comparison on a real workflow and wrote down what changed
- [ ] You have a documented decision (migrate now / wait) based on that comparison, not a vague "will look into it"

## 🐛 Common Pitfalls
- **Digest workflow nobody reads** — sending it to a channel or inbox you check daily matters more than the workflow's cleverness; put it somewhere you'll actually see it.
- **Swapping a component in production before testing** — always duplicate the workflow first; comparing side by side is the entire point of this exercise, and skipping it defeats the purpose.
- **Treating every update as urgent** — most changelog entries don't affect you; the AI summarization step exists specifically to filter noise, so don't manually re-read everything anyway.

## 🏭 Industry Track Application
For a Fintech/HealthTech track, weight your digest toward security/compliance-relevant changes (auth changes, deprecated encryption methods) over general feature announcements, since those carry real risk if missed.
