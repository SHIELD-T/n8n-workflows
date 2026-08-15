# DAY 4: Self-Hosting Setup
**Week:** 1 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- How to deploy n8n on Render's free tier using Docker
- Why free-tier services sleep after inactivity and how a cronjob keep-alive fixes it
- How to attach a persistent PostgreSQL database so workflows survive restarts
- Basic auth and SSL configuration for a publicly reachable n8n instance

## 🎥 Watch First
- [How To Self-Host N8N For FREE (In 4 Minutes)](https://www.youtube.com/watch?v=kk0nkfdmg5s) — watch for the exact Dockerfile/render.yaml structure and the moment they configure `WEBHOOK_URL`, since a wrong webhook URL is the #1 cause of "my webhooks don't work in production."

## 🛠️ Build It: Step-by-Step
1. Create a free account at render.com (sign up with GitHub) and verify your email.
2. Create a new GitHub repository and add a `Dockerfile` based on `n8nio/n8n`, setting `N8N_BASIC_AUTH_ACTIVE=true`, `N8N_BASIC_AUTH_USER`, `N8N_BASIC_AUTH_PASSWORD`, and `WEBHOOK_URL=https://<your-app-name>.onrender.com`.
3. Add a `render.yaml` declaring a `web` service of `env: docker`, `plan: free`, pointing at your Dockerfile, and push both files to GitHub.
4. In the Render dashboard, click **New +** → **Web Service**, connect your repo, and deploy. Wait for the build to go green, then open the Render-provided URL and confirm the n8n login screen appears.
5. Create a Render **PostgreSQL** database (New + → PostgreSQL, free plan). Copy its host/port/database/user/password into your `render.yaml` env vars (`DB_TYPE=postgresdb`, `DB_POSTGRESDB_HOST`, etc.) and redeploy.
6. Sign up for a free cron service (cron-job.org or UptimeRobot) and configure it to GET your Render URL every 10 minutes so the free instance doesn't sleep.
7. Log into your deployed n8n instance and confirm any workflow you create there is still present after triggering a manual redeploy (proves the database is actually persisting data, not the ephemeral filesystem).

**Stuck?** There's no EXAMPLES workflow for infrastructure setup — if the Docker deploy fails, check Render's build logs tab first; most failures are a missing/misnamed env var.

## 🔑 Credentials Needed
- Render account (free)
- GitHub account (free, for the repo Render deploys from)
- A cron/uptime service account (cron-job.org or UptimeRobot, free)

## ✅ Definition of Done
- [ ] Your n8n instance is reachable at a public `https://` URL and prompts for basic-auth login
- [ ] A workflow you create survives a manual redeploy (confirms PostgreSQL is connected, not just the container filesystem)
- [ ] Your cron/uptime service shows at least one successful ping to your n8n URL in its logs
- [ ] You can locate your `WEBHOOK_URL` env var and explain why it must match your public domain exactly

## 🐛 Common Pitfalls
- **`WEBHOOK_URL` left as localhost:** Webhooks will silently fail in production if this still points at `localhost` instead of your Render URL — always double check it after deploy.
- **Forgetting the keep-alive:** Without a cron ping, Render's free tier sleeps after ~15 minutes idle, so the *next* incoming webhook gets a cold-start delay or drops entirely.
- **Database env vars typo'd:** A single wrong character in `DB_POSTGRESDB_HOST` silently falls back to n8n's local SQLite, so your data looks fine until the container restarts and wipes it — verify by checking Render's Postgres connection string exactly.

## 🏭 Industry Track Application
Name your Render service and basic-auth username to reflect your chosen industry track's use case (e.g., `fintech-automation-prod`), and write two sentences in your notes on what production concern matters most for that industry — e.g., stricter access control for Fintech/HealthTech (consider changing the default basic-auth password to something strong now, not later), or uptime guarantees for E-commerce.
