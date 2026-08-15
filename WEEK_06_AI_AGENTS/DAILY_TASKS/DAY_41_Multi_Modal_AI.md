# DAY 41: Multi-Modal AI
**Week:** 6 — AI Agents  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to send an image to a vision-capable model and get a structured description back
- How to transcribe audio with Whisper inside n8n
- How to combine text, image, and audio analysis into one cross-modal summary
- Where multi-modal AI calls are most expensive (image/audio tokens) and how to budget for it

## 🎥 Watch First
- [Build AI Agents & Automate Workflows (Zero to Hero)](https://www.youtube.com/watch?v=DkV7ztrhLh8) — watch for any section that sends non-text input (image or audio) to an AI node; note exactly which node/operation is used, since multi-modal setup is easy to get subtly wrong.

## 🛠️ Build It: Step-by-Step
1. Build: **Webhook** trigger (Path `multi-modal-ai`) → **Set** node with `input_text`, `input_image_url`, and `input_audio_url` fields pulled from `$json`.
2. Add an **OpenAI** node (Resource: Text, model `gpt-4o` — vision-capable) for text analysis: system prompt "Analyze this text for sentiment, key topics, and insights," user message = `{{ $json.input_text }}`.
3. Add a second **OpenAI** node (Resource: Image / or Text with an image input attached via the message content array) pointing at `input_image_url`, prompt: "Describe this image in detail: objects, colors, composition, and any visible text."
4. Add an **OpenAI** node (Resource: Audio, Operation: Transcribe) with the audio file/URL as input, model `whisper-1`.
5. Add a **Merge** node (Combine by Position) to bring all three results together, then a final **OpenAI** node "Cross-Modal Analysis": system prompt "You analyze content across multiple modalities and provide integrated insights," user message concatenating the text analysis, image description, and audio transcript.
6. Test with a real small image URL (any publicly reachable .jpg) and a real short audio clip URL (a few seconds of speech). Confirm all three individual results are non-empty AND the final cross-modal node's output references content from at least two of the three modalities.

**Stuck?** Import `WEEK_06_AI_AGENTS/EXAMPLES/multimodal_ai_workflow.json` (Menu → Import from File in n8n) to see a working version, then compare it to what you built.

## 🔑 Credentials Needed
OpenAI API key (with access to a vision-capable model and Whisper — check your account's model access under platform.openai.com if a call 404s).

## ✅ Definition of Done
- [ ] The image analysis node returns a real description matching the actual image content (test by using an image you can visually verify, e.g. a photo of a specific object)
- [ ] The audio transcription node's output text matches what was actually said in your test clip
- [ ] The cross-modal analysis node's final output demonstrably references at least two of the three modalities (not just text)
- [ ] You've noted (in a comment or scratch note) the approximate token/dollar cost difference between the text-only call and the image call

## 🐛 Common Pitfalls
- **Image URL not publicly reachable:** OpenAI's API must be able to fetch the URL itself — a localhost or authenticated-only image URL will fail silently or 400; use a public test image host.
- **Audio file format rejected:** Whisper accepts specific formats (mp3, mp4, wav, m4a, etc.) under a 25MB size limit — a raw unsupported format returns a 400 error.
- **Vision costs spike fast:** Image inputs consume far more tokens than text — cap `detail` to `"low"` in the image content object while testing to avoid burning budget.

## 🏭 Industry Track Application
Apply multi-modal analysis to a real industry artifact: Fintech → analyze a photo of a receipt (image) plus a voice memo describing the expense (audio) and cross-reference them for an expense-report workflow; HealthTech → analyze a photo of a visible symptom (e.g. a rash, with appropriate care/disclaimers) alongside a patient's spoken description; EdTech → transcribe a student's spoken answer and analyze an accompanying photo of their handwritten work, then produce one combined assessment note.
