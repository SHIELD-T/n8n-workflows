# DAY 9: Advanced Self-Hosting Setup
**Week:** 2 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- Which environment variables control n8n's authentication, database, and webhook URL on Render
- How a `HEALTHCHECK` instruction and a Health Check Path keep your instance auto-recoverable
- Why SSL and connection pooling matter for a production PostgreSQL connection
- How to verify a live deployment is actually configured correctly, not just "running"

## 🎥 Watch First
- [How To Set Up N8N Self Hosting In 3 Minutes (6 Ways)](https://www.youtube.com/watch?v=kq5bmrjPPAY) — Complete 10-minute advanced deployment guide. Watch for how environment variables are set in the hosting dashboard versus baked into the Dockerfile — you'll do both today.

## 🛠️ Build It: Step-by-Step
1. In your Render dashboard, open your n8n web service from Week 1 (or create one) and go to Environment.
2. Add/confirm these variables: `N8N_BASIC_AUTH_ACTIVE=true`, `N8N_BASIC_AUTH_USER`, `N8N_BASIC_AUTH_PASSWORD`, `WEBHOOK_URL=https://<your-app>.onrender.com`, `GENERIC_TIMEZONE=UTC`, `N8N_ENCRYPTION_KEY` (generate a random 32+ character value and save it somewhere safe — losing it locks you out of existing credentials).
3. If you're using a Dockerfile, add: `HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD curl -f http://localhost:10000/healthz || exit 1`.
4. In `render.yaml` (or the dashboard's Health Check Path field), set `healthCheckPath: /healthz`.
5. Confirm your PostgreSQL database is connected, then add `DB_POSTGRESDB_SSL_ENABLED=true`, `DB_POSTGRESDB_CONNECTION_TIMEOUT=10000`, `DB_POSTGRESDB_POOL_SIZE=10`.
6. Deploy/redeploy. Once live, verify from your terminal:
   `curl -i https://<your-app>.onrender.com/healthz`
   Confirm you get an HTTP 200 response.
7. Sign into your n8n instance with the basic-auth credentials you set — confirm you're prompted for a username/password and that login succeeds.
8. Set up a free UptimeRobot (or similar) monitor pointed at your `/healthz` URL with a 5-minute check interval, and confirm it shows "Up" after its first check.

## 🔑 Credentials Needed
Render account, PostgreSQL database (Render add-on), UptimeRobot (or similar) account. No n8n node credentials are required today — this is infrastructure configuration, not a workflow.

## ✅ Definition of Done
- [ ] `curl -i https://<your-app>.onrender.com/healthz` returns HTTP 200
- [ ] Logging into your n8n URL requires the basic-auth username/password you configured
- [ ] Your PostgreSQL connection has SSL enabled and a pool size set (visible in your env vars)
- [ ] An external uptime monitor is actively checking your instance and reports it as up
- [ ] You've written down your `N8N_ENCRYPTION_KEY` somewhere outside of Render (a password manager or secure note)

## 🐛 Common Pitfalls
- **Regenerating the encryption key:** if `N8N_ENCRYPTION_KEY` regenerates on every redeploy instead of staying fixed, every saved credential becomes unreadable — set it explicitly once and never leave it on "generate on deploy."
- **Health check path mismatch:** if your Dockerfile checks `/healthz` but Render's Health Check Path field is blank or different, Render won't recognize the service as healthy and may restart it unnecessarily.
- **Free tier spin-down:** Render's free tier sleeps after inactivity — a healthcheck or uptime monitor hitting the URL every 5 minutes is what keeps it warm, not optional polish.

## 🏭 Industry Track Application
Sarah needs her automation server itself to be reliable before she trusts it with real data. Treat today's healthcheck and monitoring setup as upgrading Sarah's automation server with production monitoring and backup systems: after completing steps 1-8, additionally configure a scheduled backup — either Render's built-in PostgreSQL backup feature or a simple n8n workflow (Schedule Trigger → Postgres export node → write to disk) — and confirm one backup file actually exists with today's timestamp.
