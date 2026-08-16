# Day 01 Notes: What is Automation?

*This day's deliverable is written content, not an n8n workflow — see `DAILY_TASKS/DAY_01_Automation_Basics.md` for the full lesson.*

## Model Answer

### My Automation Opportunities (10 real, repetitive tasks)

| # | Current process | Proposed automation | Impact |
|---|---|---|---|
| 1 | Manually copying leads from a form into a spreadsheet | Webhook trigger → Set node → Google Sheets append | Saves ~30 min/day, removes copy-paste errors |
| 2 | Manually replying to the same 5 support questions | Trigger on new ticket → IF match FAQ → auto-reply | Faster response time, frees up support hours |
| 3 | Manually posting the same content to 3 social platforms | One trigger fans out to 3 API calls | Saves ~20 min/post |
| 4 | Manually checking inventory levels each morning | Scheduled trigger checks stock API, alerts if low | Prevents stockouts |
| 5 | Manually sending invoice reminders | Scheduled trigger → check due dates → send email | Improves cash flow, saves admin time |
| 6 | Manually compiling a weekly report from 3 tools | Scheduled trigger pulls from each API, merges, emails PDF | Saves ~2 hrs/week |
| 7 | Manually onboarding new clients with the same email sequence | New-client webhook → timed email sequence | Consistent onboarding, saves time |
| 8 | Manually tagging expenses by category | New-expense trigger → rules-based category Set node | Cleaner books, less manual entry |
| 9 | Manually backing up important files weekly | Scheduled trigger copies files to backup storage | Reduces risk of data loss |
| 10 | Manually notifying the team when a deploy finishes | CI webhook → Slack notification | Keeps team in sync without manual pings |

### 5 Companies and What They Automate

| Company | Automates | Likely approach |
|---|---|---|
| Zapier | App-to-app data transfer | No-code trigger/action connectors |
| Shopify | Order fulfillment and inventory sync | Event-driven webhooks to warehouse systems |
| HubSpot | Marketing email sequences and lead scoring | Workflow builder with trigger-based journeys |
| Slack | Notifications from connected tools | Webhooks and app integrations |
| Airbnb | Booking confirmations and host payouts | Event-driven backend automation |

### Automation Goals

**Personal**
- Automate my monthly budget tracking
- Automate reminders for recurring bills

**Professional**
- Automate weekly status report generation
- Automate meeting note distribution

**Business**
- Automate lead capture from website to CRM
- Automate customer onboarding emails

### Industry Track Application — Fintech

| Opportunity | Pain point |
|---|---|
| Manual fraud-flag review | Analysts manually eyeball flagged transactions |
| Manual reconciliation of bank statements | Hours spent matching transactions by hand |
| Manual KYC document checks | Slow onboarding, inconsistent review |
| Manual late-payment reminders | Missed reminders hurt collections |
| Manual monthly investor reporting | Time-consuming data pulls from multiple systems |

## Your Version

- **Your "My Automation Opportunities" list (10 items):** _______ (Current process / Proposed automation / Impact for each)
- **Your 5 company examples:** _______
- **Your Automation Goals (2+ each — Personal / Professional / Business):** _______
- **Community introduction posted (yes/no, link):** _______
- **Your chosen industry track and its 5 opportunities:** _______
