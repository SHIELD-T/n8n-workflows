# DAY 67: WEDNESDAY - Data Synchronization
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- The difference between one-way and bidirectional data sync, and when each is appropriate
- How to detect a data conflict (the same record changed in two places)
- A simple, defensible conflict-resolution rule (e.g., "most recent update wins")
- How to log sync activity so you can audit what changed and when

## 🎥 Watch First
**Watch:** [How I 100% Automated Long Form Content with n8n](https://www.youtube.com/watch?v=lF2bvXoV-Zg) - Data synchronization strategies section

Pay attention to: how the creator handles keeping one source of truth updated across multiple destinations without creating duplicate records on repeated runs.

## 🛠️ Build It: Step-by-Step
1. Set up two real destinations you already have access to: an Airtable base and a Notion database, each with matching fields (e.g., Name, Email, Last Updated).
2. Build a one-way sync workflow: a Schedule trigger (every 15 minutes) reads new/changed rows from Airtable and writes/updates the matching Notion pages.
3. To detect "changed" rows without re-syncing everything every run, filter on a `Last Updated` timestamp field that's newer than the last successful sync time (store that timestamp somewhere retrievable, like a dedicated Airtable "Sync State" record).
4. Add a lookup step before each write that checks whether a matching Notion page already exists (by email or ID) — update it if so, create it if not. This prevents duplicate records on every run.
5. Now make it bidirectional: add a second scheduled workflow that reads Notion changes back into Airtable, using the same "last updated wins" rule if both sides changed the same record.
6. Deliberately create a conflict: edit the same record in both Airtable and Notion within one sync interval, then run both sync directions and confirm your resolution rule behaves predictably (log which value won and why).
7. Log every sync run (records synced, conflicts found, resolution taken) to a dedicated "Sync Log" table.

## 🔑 Credentials Needed
- Airtable credential (from Week 9)
- Notion credential (from Week 9)

## ✅ Definition of Done
- [ ] A one-way sync workflow that updates existing records instead of creating duplicates on repeat runs
- [ ] A bidirectional sync with a documented conflict-resolution rule
- [ ] A real conflict was created and resolved predictably, with the outcome logged
- [ ] A sync log exists showing records processed and any conflicts per run

## 🐛 Common Pitfalls
- Syncing on every run without a "changed since" filter — this re-processes your entire dataset every time and doesn't scale
- Matching records by name instead of a stable unique ID/email — names collide and change
- No conflict rule at all — bidirectional sync without one will silently overwrite data unpredictably

## 🏭 Industry Track Application
Sync problems show up whenever a client uses two systems that don't talk to each other natively — a common paid engagement. A marketing track might sync leads between a CRM and an email tool; an e-commerce track might sync inventory between a storefront and a spreadsheet; a real-estate track might sync listings between an MLS export and a client-facing site. Frame today's build around your industry's most likely "two systems, one truth" scenario.
