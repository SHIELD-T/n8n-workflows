# Day 19 Notes: Version Control & Backing Up

*This day's deliverable is written content and local scripting, not an n8n workflow — see `DAILY_TASKS/DAY_19_Version_Control_Backing_Up.md` for the full lesson.*

## Model Answer

### Naming Convention & Folder Structure

- **Naming convention:** `[category]-[function]-v1-[date].json`
- **Folder structure:** `n8n-backups/YYYYMMDD/`
- **Example filename:** `week3-triggers-v1-20260816.json`

### Backup Script (bash, run manually once to confirm output)

```bash
#!/bin/bash
now=$(date +%Y%m%d)
folder="n8n-backups/$now"
mkdir -p "$folder"
cp -r ~/.n8n/* "$folder"/
echo "Backed up to $folder"
```

Sample run output: `backup_folder: n8n-backups/20260816, files_backed_up: 2, ran_at: 2026-08-16T00:00:00Z`

### Documentation Note (for a teammate)

"Workflows are exported via menu → Download, named `[category]-[function]-v1-[date].json`, and stored under `n8n-backups/YYYYMMDD/` so any teammate can find the latest backup by date."

### Industry Track — Alex's Business Backup System

- Export all of Alex's lead-response and inventory workflows.
- Organize under `alex-business/[system-name]/` with dated backups.
- Disaster-recovery note: if the n8n instance were lost, restore by spinning up a fresh instance, re-importing the latest `alex-business/lead-capture/` JSON, and re-entering the CRM/email credentials (credentials are never included in exports and must be re-added manually).

## Your Version

- **Two workflows exported using the naming convention:** _______
- **Re-imported workflow confirmed to execute identically:** _______
- **Your backup script and where it was run:** _______
- **Your naming convention / folder structure note:** _______
- **Alex's disaster-recovery note (industry track):** _______
