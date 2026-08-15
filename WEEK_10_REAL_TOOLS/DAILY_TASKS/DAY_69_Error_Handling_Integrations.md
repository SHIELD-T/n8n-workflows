# DAY 69: FRIDAY - Error Handling in Integrations
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to add automatic retry with a delay to a flaky API call
- How to build a fallback path that uses a second service when the primary one fails
- How to log every error with enough detail to actually diagnose it later
- How to distinguish errors worth retrying (timeouts) from errors that never will succeed on retry (bad auth, bad request)

## 🎥 Watch First
**Watch:** [N8N FULL COURSE 5 HOURS (Build & Automate Anything)](https://www.youtube.com/watch?v=7WsbtZwOx_U) - Error handling for integrations section

Pay attention to: which error types the instructor treats as retryable vs. not — that distinction is the core skill for today.

## 🛠️ Build It: Step-by-Step
1. Take one of your existing integrations from earlier this week (e.g., the weather or news API from Day 66) and enable n8n's built-in retry option on the HTTP Request node (set max retries and a retry delay in the node's Settings tab).
2. Add an IF node after the call that checks the HTTP status: 2xx = success, 5xx or timeout = retryable, 4xx = not retryable (bad request/auth — retrying won't help).
3. Build a fallback path: if the primary API fails after retries are exhausted, call a second, different API that can serve a similar (even if lower-quality) result — or fall back to a cached/default value.
4. Add a dedicated "Error Log" Airtable table and log every failure with: which service failed, the error type, the retry count, and whether a fallback was used.
5. Send a Slack alert only when a fallback was triggered or all retries were exhausted — not on every individual retry, which would be noisy.
6. Test all three paths deliberately: (a) a call that succeeds immediately, (b) a call that fails but succeeds on retry (simulate with a temporarily-wrong-then-fixed URL), (c) a call that fails completely and triggers the fallback.
7. Review your Day 63 (Week 9) complete system and add this same retry/fallback/logging pattern to at least one of its risky steps.

## 🔑 Credentials Needed
- Whichever API credentials you're adding error handling to (from Days 65-66)
- Slack credential (from Week 9)
- Airtable credential (from Week 9)

## ✅ Definition of Done
- [ ] A workflow with configured retry (max attempts + delay) on at least one real API call
- [ ] A working fallback path that engages only after retries are exhausted
- [ ] An Error Log table capturing service, error type, retry count, and fallback status
- [ ] All three test scenarios (immediate success, retry-then-success, total failure) were run and behaved correctly
- [ ] Slack alerts fire only on fallback/total failure, not on every retry attempt

## 🐛 Common Pitfalls
- Retrying non-retryable errors (like a 401 auth failure) — this wastes time and can trigger rate limiting or account lockouts
- Setting retry delay too short, hammering a struggling API and making things worse
- Alerting on every retry attempt instead of only meaningful failures, which trains your team to ignore the channel

## 🏭 Industry Track Application
Reliability expectations vary sharply by industry — a fintech or healthtech client will expect near-zero silent failures given compliance stakes, while a marketing automation might tolerate an occasional dropped run. Set your retry counts, alert thresholds, and fallback strategy to match what your industry track's clients would realistically require, and note that reasoning in your workflow's sticky notes.
