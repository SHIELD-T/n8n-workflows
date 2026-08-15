# DAY 60: WEDNESDAY - Email & Calendar Triggers
**Week:** 9 — Real-World Tools (Part 1)  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to trigger a workflow from an incoming Gmail message
- How to parse and categorize email content, including using AI to classify urgency
- How to trigger a workflow from a Google Calendar event (create/update)
- How to send automated meeting reminders based on calendar data

## 🎥 Watch First
**Watch:** [Email & Calendar Automation](https://www.youtube.com/watch?v=4cQWJViybAQ) - Complete 13 minute email and calendar tutorial

Pay attention to: the difference between polling triggers (n8n checks periodically) and true push webhooks (Gmail/Calendar notify you) — this affects both cost and latency.

## 🛠️ Build It: Step-by-Step
1. Set up a Gmail trigger workflow: use n8n's Gmail Trigger node (polling) or configure Gmail push notifications via Google Cloud Pub/Sub if you want true real-time delivery.
2. Add a node to extract `from`, `subject`, and `body` from the incoming email into clean fields.
3. Add an OpenAI node that classifies the email as urgent/normal and extracts a one-line summary — use the exact prompt pattern from the video as a starting point, then tighten it.
4. Add an IF node that routes urgent emails to a Slack alert channel, and log every email (urgent or not) to an Airtable "Email Log" table.
5. Set up a second workflow using n8n's Google Calendar Trigger node to fire on new/updated events.
6. Add a node that checks if the event type is a "meeting" and, if so, sends a reminder email to all attendees with the event title, start time, and end time.
7. Test both workflows end-to-end: send yourself a real test email and create a real test calendar event, and confirm both trigger correctly — including checking what happens if the email has no subject or the event has no attendees.

## 🔑 Credentials Needed
- Gmail credential (from Day 58)
- Google Calendar credential (OAuth, same Google Cloud project as Gmail)
- Slack credential (from Day 58)
- Airtable credential (from Day 58)
- OpenAI credential (from Day 58)

## ✅ Definition of Done
- [ ] A working Gmail-triggered workflow that classifies and logs incoming emails
- [ ] Urgent emails (per your AI classifier) post to a dedicated Slack channel
- [ ] A working Calendar-triggered workflow that sends meeting reminders to attendees
- [ ] Both workflows tested with real messages/events, not synthetic JSON pasted into the editor
- [ ] You can explain the tradeoff between polling and push triggers for at least one of the two workflows you built

## 🐛 Common Pitfalls
- Polling triggers set to check too frequently can hit Gmail/Calendar API rate limits — start with a reasonable interval (1-5 minutes) and adjust
- AI classification prompts that don't specify an output format will produce inconsistent text you can't reliably parse downstream — always request a structured response
- Calendar events without attendees (personal reminders) will break a reminder-email workflow if you don't check for an empty attendees list first

## 🏭 Industry Track Application
Email and calendar triggers map directly to client operations work. A logistics track might trigger delivery-exception alerts from incoming carrier emails; an EdTech track might auto-remind students of upcoming session calendar events; a professional-services track (law, accounting) might auto-log every client email into a case file. Pick one realistic trigger scenario from your industry and build it today instead of a generic inbox demo.
