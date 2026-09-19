# DAY 2: Intro to n8n Core Concepts
**Week:** 1 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- The n8n interface: canvas, node library, execution history, credentials
- Core vocabulary: nodes, triggers, actions, data flow between nodes
- How to add, configure, and connect nodes on the canvas
- The 10 most common node types and when to reach for each

## 🎥 Watch First
- [Master n8n in 2 Hours: Complete Beginner's Guide for 2025](https://www.youtube.com/watch?v=AURnISajubk) — first 15 minutes cover the interface and navigation. Watch for where the node library, execution log, and credentials menu live — you'll use all three today.

## 🛠️ Build It: Step-by-Step
1. Open your n8n instance and click **New Workflow**.
2. Click the **+** button (or drag from the node panel) to add a **Manual Trigger** node — this becomes your workflow's starting point.
3. Add a **Set** node (search "Edit Fields (Set)" in the node panel) and connect it to the Manual Trigger by dragging from the trigger's output dot to the Set node's input dot.
4. Open the Set node and add a field named `message` with the value `Hello from n8n!` (use "Add Field" → String).
5. Add an **HTTP Request** node after the Set node. Configure: Method = `POST`, URL = `https://httpbin.org/post`, Body Content Type = JSON, and in the body use the expression `{{ $json.message }}`.
6. Click **Execute Workflow**. Click each node in turn and check its **Output** panel (Table/JSON view) to confirm the message flowed through correctly and httpbin echoed it back.
7. Now build a second, separate workflow: Manual Trigger → Set node (field `text` = `"This is my first n8n workflow!"`) → **Write Binary File** / **Read/Write Files from Disk** node (File Name: `output.txt`, Data: `{{ $json.text }}`). Execute it and confirm the file was written.

**Stuck?** Import `WEEK_01_FOUNDATION/EXAMPLES/manual_trigger_to_api_request.json` (Menu → Import from File in n8n) to see a working baseline, then compare its node structure to what you built.

## 🔑 Credentials Needed
None — Manual Trigger, Set, HTTP Request (to a public test endpoint), and file nodes don't require API credentials today.

## ✅ Definition of Done
- [ ] Your first workflow executes with a green checkmark on every node and the HTTP Request node's output shows your message echoed back from httpbin.org
- [ ] Your second workflow creates `output.txt` and you've opened it to confirm it contains your exact text
- [ ] You can explain, in one sentence each, what a Manual Trigger, a Set node, and an HTTP Request node do
- [ ] You've opened Execution History and located the run for at least one of today's workflows

## 🐛 Common Pitfalls
- **Nodes not connecting:** Drag precisely from the small dot on the node's right edge to the dot on the next node's left edge — dropping it on the node body itself won't create a connection.
- **Expression not resolving:** Forgetting the `=` prefix or `{{ }}` wrapper in a field means n8n treats it as literal text instead of an expression — the field turns red/shows an error if the syntax is malformed.
- **"Execute Workflow" only runs to the last node clicked:** If you added new nodes after testing, click Execute Workflow again from scratch (not just the last node) to re-run the full chain.

## 🏭 Industry Track Application
Rebuild the text-to-file workflow using data relevant to your industry track — e.g., a Fintech expense line item, a HealthTech patient note, or an EdTech course-progress entry. Swap the `Set` node's fields for 3-4 industry-relevant fields (e.g., `amount`, `category`, `date` for Fintech) and confirm they all appear correctly in the output file.
