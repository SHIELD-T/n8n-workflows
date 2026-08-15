# DAY 19: Version Control & Backing Up
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to export a single workflow and a small collection from the n8n UI
- How to import a workflow from a JSON backup file and verify it restored correctly
- A practical folder/naming convention for organizing exported workflow JSON files
- How to write a simple backup script that copies your n8n data directory

## 🎥 Watch First
- [How To Set Up N8N Self Hosting In 3 Minutes](https://www.youtube.com/watch?v=kq5bmrjPPAY) — ~10 minute deployment and backup guide. Focus on the parts covering data persistence and where workflow data actually lives on disk.

## 🛠️ Build It: Step-by-Step
1. Open any 2 workflows you built earlier in Week 3. For each, use the n8n menu (⋮ top-right of the canvas) → **Download** to export it as a `.json` file to your local machine.
2. Create a local folder structure: `n8n-backups/YYYYMMDD/` (use today's actual date) and move both exported JSON files into it, renaming them using the convention `[category]-[function]-v1-[date].json`, e.g. `week3-triggers-v1-20260815.json`.
3. Open one exported JSON file in a text editor and confirm it contains a `"nodes"` array and a `"connections"` object — this is what n8n actually restores from.
4. Test restoration: create a brand-new empty workflow in n8n, then use menu → **Import from File** and select one of your exported JSONs. Confirm all nodes and connections reappear exactly as they were, then execute it to confirm it still runs.
5. Write a simple local backup script (bash or PowerShell) that copies your n8n data directory (`~/.n8n` if self-hosted) to a timestamped folder, and run it once manually to confirm it produces a non-empty backup folder.
6. Document your naming convention and folder structure in a short note (2-3 sentences) so a teammate could find any given workflow's latest backup.

## 🔑 Credentials Needed
None — export/import is entirely local to your n8n instance. If self-hosting, you'll need filesystem/SSH access to your server for the data-directory backup script.

## ✅ Definition of Done
- [ ] Two workflows successfully exported as `.json` files using the naming convention `[category]-[function]-v1-[date].json`
- [ ] At least one exported workflow successfully re-imported into a new empty workflow and confirmed to execute identically to the original
- [ ] A backup script exists and was run at least once, producing a timestamped folder with actual file contents (not empty)
- [ ] Folder structure and naming convention documented in a short note

## 🐛 Common Pitfalls
- **Export via "Download" does not include saved credentials** — they must be re-entered (or securely migrated separately) after import on a new instance.
- **Importing a workflow with the same name as an existing one creates a duplicate** rather than overwriting it — check your workflow list for accidental duplicates after testing import.
- **A backup script that copies the database file mid-write can produce a corrupted backup** — stop the n8n process, or use a proper DB dump command, for anything beyond this practice exercise.

## 🏭 Industry Track Application
Set up Alex's business automation backup system — export all of Alex's lead-response and inventory workflows, organize them under `alex-business/[system-name]/` with dated backups, and write a one-paragraph disaster-recovery note explaining how Alex's team would restore the lead capture system if the n8n instance were lost.
