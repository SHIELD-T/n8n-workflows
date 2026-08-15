# DAY 20: Cloning and Modifying Pre-built Workflows
**Week:** 3 — Workflows  |  **Time:** 3-4 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to duplicate an existing workflow in n8n without disturbing the original
- How to safely swap API endpoints and field mappings in a cloned workflow
- The pattern behind automated clone-and-customize logic (as shown in the cloning-system example)
- How to verify a customized clone still executes correctly after modification

## 🎥 Watch First
- [n8n Quick Start Tutorial: Build Your First Workflow](https://www.youtube.com/watch?v=4cQWJViybAQ) — focus on the workflow cloning and modification section (14m47s).

## 🛠️ Build It: Step-by-Step
1. Take your Day 16 "Complete Node Mastery Workflow" (HTTP + IF + SET + SplitInBatches). In the n8n workflow list, use ⋮ → **Duplicate** to clone it. Rename the clone to "Custom API Integration (Cloned)".
2. In the clone, change the HTTP Request node's URL from `jsonplaceholder.typicode.com/posts` to `jsonplaceholder.typicode.com/users`, and update the downstream Set node's field mappings to match the new response shape (`name`, `email`, `company.name` instead of `title`/`body`).
3. Execute the modified clone and confirm the output now reflects user data (name/email), not post data — proving the clone is genuinely independent of the original.
4. Clone a second workflow (your Day 15 webhook workflow or Day 17 expression workflow) and modify at least 2 field names plus 1 expression to serve a different purpose — e.g. change the webhook path from `trigger-actions` to `custom-data-processing`, and change `.toUpperCase()` to `.split(' ').reverse().join(' ')`.
5. Test the second clone with curl against its new webhook path and confirm the new expression behavior (reversed word order) shows up in the response.
6. Write a 2-3 sentence changelog for each clone describing exactly what you changed and why, and keep it in a Sticky Note on the workflow's canvas.

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/workflow_cloning_system.json` (Menu → Import from File in n8n) to see a workflow that programmatically fetches a source workflow, clones its nodes with new IDs (`node.id + '_cloned_' + clone_id`), and re-saves it as a new workflow — then compare its "Modify Cloned Workflow" node's renaming pattern to your manual clone-and-rename process.

## 🔑 Credentials Needed
None — jsonplaceholder.typicode.com stays free/no-auth for the API swap; the cloning process itself only needs your own n8n instance access.

## ✅ Definition of Done
- [ ] The original Day 16 workflow is untouched and still runs correctly after cloning
- [ ] Clone #1 successfully returns user data (not post data) after the API endpoint and field mapping changes
- [ ] Clone #2's webhook responds at its new path (`custom-data-processing`) and demonstrates the modified expression's different output vs. the original
- [ ] Each clone has a short Sticky Note changelog describing the specific changes made

## 🐛 Common Pitfalls
- **Duplicating a workflow can produce internal node ID collisions** in some n8n versions — if you see "node already exists" errors when re-importing, check for ID collisions.
- **Changing an API URL without updating downstream field references leaves you reading `undefined`** — the old field names (`title`, `body`) don't exist on the new API's response shape.
- **Forgetting to rename a clone** leaves two workflows with identical names in your list, making it easy to edit the wrong one later.

## 🏭 Industry Track Application
Clone and customize business workflows for Alex's specific industry: take your Day 15 lead-capture webhook workflow, clone it, and modify it into an "Alex Inventory Reorder" workflow — change the webhook path to `inventory-reorder`, swap the Set node fields to `sku`, `current_stock`, `reorder_threshold`, and add an IF node that only proceeds when `current_stock < reorder_threshold`.
