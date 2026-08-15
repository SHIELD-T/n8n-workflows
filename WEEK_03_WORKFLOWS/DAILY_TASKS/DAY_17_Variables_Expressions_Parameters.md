# DAY 17: Variables, Expressions, and Parameters
**Week:** 3 — Workflows  |  **Time:** 2-3 hours  |  **Difficulty:** Intermediate

## 🎯 What You'll Learn
- n8n expression syntax (`{{ }}`) and how to access `$json`, `$now`, and node references like `$('Node Name')`
- String, date, and math functions available inside expressions
- Ternary conditional expressions for inline decision logic
- How to build a multi-step Set-node chain where each step's output feeds the next expression

## 🎥 Watch First
- [Using Expressions in n8n](https://www.youtube.com/watch?v=4cQWJViybAQ) — complete ~12 minute expression tutorial. Pay attention to how `$json` changes context between nodes, and how date functions like `.format()` and `.diff()` chain together.

## 🛠️ Build It: Step-by-Step
1. Manual Trigger → Set node "Set Dynamic Data": `user_input` = `{{ $json.input || 'Sample User Data' }}`, `start_time` = `{{ $now }}`.
2. Add Set node "Expression 1: String Processing": `processed_text` = `{{ $json.user_input.trim().toUpperCase() }}`, `text_length` = `{{ $json.user_input.length }}`, `word_count` = `{{ $json.user_input.split(' ').length }}`.
3. Add Set node "Expression 2: Date Calculations": `current_date` = `{{ $now.format('YYYY-MM-DD') }}`, `processing_duration` = `{{ $now.diff($json.start_time, 'milliseconds') }}`, `future_date` = `{{ $now.add(7, 'days').format('YYYY-MM-DD') }}`.
4. Add Set node "Expression 3: Math Operations": `random_number` = `{{ Math.floor(Math.random() * 100) }}`, `percentage` = `{{ Math.round(($json.word_count / $json.text_length) * 100) }}`.
5. Add Set node "Expression 4: Conditional Logic": `text_category` = `{{ $json.text_length > 50 ? 'long' : 'short' }}`, `complexity_level` = `{{ $json.word_count > 10 ? 'complex' : 'simple' }}`.
6. Add a final Set node "Format Final Results" concatenating all five expressions into one readable multi-line report string, e.g. `Text Category: {{ $json.text_category }}\nComplexity: {{ $json.complexity_level }}`.
7. Execute once with the default "Sample User Data" input, then execute again with `input` manually set to a 60+ character sentence with 12+ words, and verify `text_category` flips from "short" to "long" and `complexity_level` flips from "simple" to "complex".

**Stuck?** Import `WEEK_03_WORKFLOWS/EXAMPLES/advanced_data_processing.json` (Menu → Import from File in n8n) to see a working 5-stage Set-node expression pipeline (Data Cleaning → Transformation → Analysis → Format Results), then compare its `average_word_length` calculation to your `percentage` expression.

## 🔑 Credentials Needed
None — all expressions run inside n8n's own expression engine.

## ✅ Definition of Done
- [ ] Running with the default input, `processed_text` shows the trimmed, uppercased version of `user_input`
- [ ] `text_category` correctly evaluates to "short" for input under 50 characters and "long" for input over 50 characters, tested with both
- [ ] `processing_duration` (Expression 2) shows a small positive millisecond value, not `undefined` or `NaN`
- [ ] The final report string correctly interpolates at least 5 different expression outputs into one readable message

## 🐛 Common Pitfalls
- **`$now` is a snapshot, not a live clock:** to measure elapsed time you must store an earlier `$now` value and `.diff()` against it later — recomputing `$now` twice and subtracting won't work reliably.
- **Ternary expressions need the full `{{ condition ? 'a' : 'b' }}` on one line** — line breaks inside the expression editor can break parsing.
- **`.split(' ').length` on a string with no spaces returns 1, not 0** — don't assume it validates "has multiple words."

## 🏭 Industry Track Application
Build Alex's dynamic pricing system using expressions: set a `base_price`, apply a ternary discount when `{{ $json.quantity > 50 }}`, flag Friday promos with `{{ $now.format('dddd') === 'Friday' ? 'weekend_promo' : 'standard' }}`, and round the final price to 2 decimals with `Math.round(price * 100) / 100`.
