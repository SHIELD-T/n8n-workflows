# Day 104 Notes: Legacy Finalization

*This day's deliverable is a published playbook, not an n8n workflow — see `DAILY_TASKS/DAY_104_Legacy_Finalization.md` for the full lesson.*

## Model Answer

### Published Automation Playbook (rewritten from Day 97's draft)

**5 Lessons Learned (each standalone, no course-specific references)**

1. **Situation:** A client's SMS provider account wasn't set up before go-live. **What went wrong:** the launch date slipped 3 days. **Fix:** always confirm every third-party account exists and is authenticated during the discovery phase, not the build phase.
2. **Situation:** A workflow relied on a hardcoded spreadsheet ID. **What went wrong:** it broke the moment the client duplicated their sheet. **Fix:** always route client-specific values through one named config node.
3. **Situation:** An AI agent had no error branch. **What went wrong:** a malformed webhook payload silently failed the whole run. **Fix:** always add an explicit error-output branch before calling anything "done."
4. **Situation:** Pricing was set by "feel" early on. **What went wrong:** it left real money on the table relative to value delivered. **Fix:** calculate value-based pricing from hours saved × hourly rate, every time.
5. **Situation:** A portfolio sat in draft for weeks. **What went wrong:** no outreach could start without it. **Fix:** set a hard stop time for polishing and publish something imperfect but real.

**New section — "3 things I'd tell someone starting from zero":**
1. Build one real, working automation before you read another tutorial.
2. Talk to a real business owner about their actual pain before you build anything for them.
3. Send the imperfect outreach message today instead of the perfect one next week.

**Published at:** a public blog post / Notion page (real URL, verified accessible outside login).
**Standalone post:** lesson #4 (pricing) posted standalone on LinkedIn today.
**Links back to:** Day 101 portfolio and Day 103 contact info.

## Your Version

- **Your playbook's public URL (verified accessible logged out):** _______
- **Your 5 rewritten, standalone lesson entries:** _______
- **Your "3 things I'd tell someone starting from zero" section:** _______
- **The standalone post you published today, and where:** _______
