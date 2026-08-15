# DAY 58: MONDAY - OAuth 2.0 vs API Keys
**Week:** 9 — Real-World Tools (Part 1)  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- The practical difference between OAuth 2.0 and API key authentication, and when to use each
- How to register an OAuth app and generate credentials for Gmail, Slack, and Notion
- How to store and reference credentials securely inside n8n instead of hardcoding them
- How to test that an authenticated connection actually works before building on top of it

## 🎥 Watch First
**Watch:** [OAuth2 vs API Keys](https://www.youtube.com/watch?v=4cQWJViybAQ) - Complete 10 minute authentication tutorial

Pay attention to: the exact screens used to create OAuth client IDs/secrets and redirect URIs, and how n8n's built-in Credentials panel (not the workflow canvas) is where auth actually lives.

## 🛠️ Build It: Step-by-Step
1. In n8n, go to **Credentials → New** and create an OAuth2 credential for **Gmail**: create a Google Cloud project, enable the Gmail API, configure the OAuth consent screen, and generate a client ID/secret. Use the redirect URI n8n shows you in the credential setup screen.
2. Repeat step 1 for **Slack**: create a Slack app at api.slack.com, add the `channels:read` and `chat:write` scopes, install it to a workspace, and connect it as an OAuth2 credential in n8n.
3. Repeat step 1 for **Notion**: create a Notion integration at notion.so/my-integrations, share at least one page/database with it, and connect it as an OAuth2 credential in n8n.
4. Create an **API key** credential for **Airtable**: generate a personal access token, create a base, and connect it in n8n.
5. Create an **API key** credential for **OpenAI**: generate an API key from platform.openai.com and connect it in n8n.
6. Build one throwaway test workflow per service (a single node hitting each API — e.g. "List Channels" for Slack, "Get Base Schema" for Airtable) and execute it manually to confirm each credential actually authenticates, not just that it saved without error.
7. Write down, in a note or doc, which method (OAuth vs API key) you used for each of the 6 services and why — you'll reuse this reasoning throughout the rest of the course.

## 🔑 Credentials Needed
- Google account (for Gmail OAuth + Google Cloud project)
- Slack workspace (owner or admin access to install an app)
- Notion account
- Airtable account
- OpenAI account with API access

## ✅ Definition of Done
- [ ] 3 OAuth 2.0 credentials (Gmail, Slack, Notion) saved in n8n and each one passes a test execution
- [ ] 2 API key credentials (Airtable, OpenAI) saved in n8n and each one passes a test execution
- [ ] You can explain, in one sentence each, why OAuth suits user-data access and API keys suit service-to-service calls
- [ ] No credential values are hardcoded in a workflow node — everything routes through n8n's Credentials panel

## 🐛 Common Pitfalls
- Using the wrong redirect URI (must match exactly what your n8n instance shows, including http vs https) — this is the #1 cause of OAuth failures
- Forgetting to actually share a Notion page/database with your integration — the API key working is not the same as the integration having access
- Requesting overly broad OAuth scopes "just in case" — request only the scopes each workflow actually needs

## 🏭 Industry Track Application
Whichever industry track you chose, today's authentication work is the plumbing every later automation depends on. A fintech track will lean heavily on OAuth for banking/payment APIs with strict scope requirements; a healthtech track needs to be especially disciplined about credential scoping given compliance concerns; an e-commerce or marketing track will use more API keys (ad platforms, storefronts) than OAuth. Note which pattern dominates your industry — you'll set up more of that type in the coming weeks.
