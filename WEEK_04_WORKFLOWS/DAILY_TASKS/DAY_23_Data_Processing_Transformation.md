# DAY 23: Data Processing and Transformation
**Week:** 4 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- How to validate an array of JSON records before transforming it
- How to filter out invalid/incomplete records with a JS expression inside a Set node
- How to convert a JSON array into CSV rows using `.map()` and `.join()`
- How to enhance individual records with derived fields while looping through them

## 🎥 Watch First
- [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) — data processing section. Note the warning about validating data shape before transforming it, not after.

## 🛠️ Build It: Step-by-Step
1. Manual Trigger → Set node "Set Sample JSON Data" with `json_data` = the array literal: `[{"id":1,"name":"John Doe","email":"john@example.com","age":30,"city":"New York"}, {"id":2,"name":"Jane Smith","email":"jane@example.com","age":25,"city":"Los Angeles"}, {"id":3,"name":"Bob Johnson","email":"bob@example.com","age":35,"city":"Chicago"}]`.
2. Add IF node "Validate JSON Data" checking `{{ $json.json_data }}` array is not empty; wire the false branch to a "Handle Validation Error" Set node.
3. Add Set node "Clean and Validate Data": `cleaned_data` = `{{ $json.json_data.filter(item => item.name && item.email && item.age) }}`, `cleaned_count` = the same filter's `.length`. Test this by adding a 4th record missing `email` and confirming `cleaned_count` still shows 3, not 4.
4. Add Set node "Transform to CSV Format": `csv_headers` = `"id,name,email,age,city"`, `csv_rows` = `{{ $json.cleaned_data.map(item => \`${item.id},${item.name},${item.email},${item.age},${item.city}\`).join('\n') }}`, `csv_content` = headers + rows joined.
5. Add SplitInBatches (batch size 1) → "Enhance Record Data" Set node computing `enhanced_record` with `age_group` = `{{ $json.age > 30 ? "adult" : "young_adult" }}` and normalized `email` = `{{ $json.email.toLowerCase().trim() }}`.
6. Add a final "Generate Final CSV" Set node building the complete CSV string with the header row plus all enhanced fields, and `csv_filename` = `processed_data_{{ $now.format('YYYYMMDDHHmmss') }}.csv`.
7. Execute the full workflow and verify the final `csv_content` field, copy-pasted into a text file, opens correctly as a 3-row CSV in a spreadsheet app with columns aligned.

**Stuck?** Import `WEEK_04_WORKFLOWS/EXAMPLES/data_processing_workflow.json` (Menu → Import from File in n8n) to see the working JSON-to-CSV pipeline (Clean → Transform → Enhance → Generate), then compare its `enhanced_record.age_group` ternary to your own.

## 🔑 Credentials Needed
None — all sample data is hardcoded in the Set node; no external service required.

## ✅ Definition of Done
- [ ] `cleaned_count` correctly excludes any record missing `name`, `email`, or `age`, tested by adding a deliberately incomplete 4th record
- [ ] `csv_content` is a valid CSV string — pasted into a `.csv` file, it opens with correct columns in a spreadsheet app
- [ ] `enhanced_record.age_group` correctly shows "adult" for age > 30 and "young_adult" for age ≤ 30, verified against at least 2 different records
- [ ] The IF node's validation branch is reachable, verified by testing with an empty `json_data` array

## 🐛 Common Pitfalls
- **Template literals must use backticks, not `+` concatenation** — mixing the two syntaxes inside a single expression silently breaks it.
- **This naive `.join(',')` approach doesn't escape commas inside field values** — a `name` like "Doe, John" would corrupt column alignment; note this as a known limitation rather than chasing it down today.
- **`.filter()` returns a new array without mutating the original** — downstream nodes referencing `$json.json_data` (not `$json.cleaned_data`) will still see the unfiltered records.

## 🏭 Industry Track Application
Build Alex's expense-report converter: take a JSON array of expense line items (vendor, amount, category, date), filter out any missing a `vendor` or `amount`, transform to CSV, and enhance each record with a `category_flag` that marks any expense over $500 as `"needs_approval"`.
