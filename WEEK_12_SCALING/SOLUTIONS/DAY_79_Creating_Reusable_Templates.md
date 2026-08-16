# Day 79 Notes: Creating Reusable Templates

*This day's deliverable is a documented, templated n8n workflow plus written documentation — see `DAILY_TASKS/DAY_79_Creating_Reusable_Templates.md` for the full lesson. The actual template-building happens directly in n8n on your own chosen workflow, not in this notes file; use the checklist below to track it.*

## Model Answer

### Template 1 fully worked: Lead Generation Automation Template

**Template name:** Lead Generation Automation
**Description:** Complete lead capture and nurturing system, rebuilt as a reusable template.

**Customization variables (renamed to placeholders before re-export):**
- `{{FORM_SOURCE}}` — Tally, Typeform, or Google Forms
- `{{CRM_SYSTEM}}` — Airtable, HubSpot, or Salesforce
- `{{EMAIL_SERVICE}}` — Gmail, Mailchimp, or SendGrid
- `{{NOTIFICATION_CHANNEL}}` — Slack, Telegram, or Discord

**Components:** form webhook trigger → data validation/cleaning → CRM integration → email automation → notification.

**Documentation (Sticky Note on the actual template workflow):**
- *Setup guide:* step-by-step — connect `{{FORM_SOURCE}}` webhook, connect `{{CRM_SYSTEM}}` credential, set `{{NOTIFICATION_CHANNEL}}` webhook URL.
- *Customization guide:* swap any `{{PLACEHOLDER}}` node for the equivalent tool without touching the rest of the logic.
- *Troubleshooting:* most common issue is a mismatched field name between the form and CRM mapping.
- *Examples:* pre-filled with the Coastal Air HVAC lead-capture use case from Week 11.

**Remaining 4 template ideas (same documentation pattern, condensed):**
- **Customer Support** — ticket trigger → AI classification → automated response → escalation → performance tracking.
- **Content Management** — content trigger → AI generation → review/edit → multi-platform publish → analytics.
- **Inventory Management** — stock monitoring → reorder automation → supplier communication → reporting.
- **Sales Pipeline** — lead capture → qualification → follow-up sequence → proposal generation → deal tracking.

Each template has all client-specific values replaced with `{{PLACEHOLDER}}` variables and a setup Sticky Note, so any of them can be handed to a new client or a hire without asking five questions first.

## Your Version

- **Your chosen best-performing workflow (which one, from where in the course):** _______
- **Its config Set node with named placeholder variables (list them):** _______
- **Confirmation every downstream node references the config node, not a hardcoded value:** _______
- **Sticky Note text documenting what to change / credentials needed:** _______
- **Exported template JSON filename and location:** _______
- **Comparison against `WEEK_12_SCALING/EXAMPLES/workflow_template_management_system.json` — one thing done the same or differently:** _______
