# DAY 66: TUESDAY - Custom API Services
**Week:** 10 — Real-World Tools (Part 2)  |  **Time:** 2-3 hours  |  **Difficulty:** Advanced

## 🎯 What You'll Learn
- How to read unfamiliar API documentation and identify the pieces you need (auth, endpoint, params, response shape)
- How to configure n8n's HTTP Request node against a real third-party API from scratch
- How to debug a failing API call using the response status and body, not just the n8n error banner
- How to turn a raw API response into a usable, structured record

## 🎥 Watch First
**Watch:** [What I Wish I Had Known Before Building 100+ n8n Workflows](https://www.youtube.com/watch?v=VB0ANci--Dc) - Working with custom APIs section

Pay attention to: how the instructor reads a new API's docs live and translates auth/params directly into n8n node fields — mimic that process today rather than skipping straight to copying a working example.

## 🛠️ Build It: Step-by-Step
1. Sign up for a free tier of a real weather API (e.g., OpenWeatherMap or open-meteo.com — the latter needs no key) and read its docs to identify: base URL, required query params, and response format.
2. Build a workflow: Webhook trigger (accepting a city name) → HTTP Request node calling the weather API with the city as a query param → Set node extracting temperature, humidity, and description into clean fields.
3. Sign up for a free tier of a real news API (e.g., NewsAPI.org) and repeat the process: HTTP Request → Set node extracting article titles and URLs.
4. For each API, deliberately send a bad request (wrong param name, missing key) and read the actual error response body in n8n's execution panel — note what the API tells you vs. what n8n's generic error says.
5. Add basic error handling: an IF node checking the HTTP status code, routing failed calls to a Slack alert instead of letting the workflow crash silently.
6. Store each processed result (weather or news) into an Airtable table so you have a persistent record of successful calls.
7. Write a short note (in the workflow's sticky notes or a doc) on what you'd tell someone integrating this specific API for the first time — the "gotcha" you found.

## 🔑 Credentials Needed
- Weather API key (or none, if using a keyless API like open-meteo.com)
- News API key (free tier)
- Slack credential (from Week 9)
- Airtable credential (from Week 9)

## ✅ Definition of Done
- [ ] Two working integrations against real third-party APIs (not mocked URLs)
- [ ] At least one deliberate bad-request test performed and its real error response read
- [ ] Failed calls route to a Slack alert instead of failing the whole workflow invisibly
- [ ] Both APIs' results are stored in Airtable with clean, extracted fields (not raw JSON dumps)

## 🐛 Common Pitfalls
- Skipping the docs and guessing param names from an old tutorial — API params and auth methods change between versions
- Not checking whether an API expects the key in a header vs. a query string vs. a request body — this varies a lot between providers
- Treating a 200 status with an empty or error-shaped body as success — always inspect the actual payload, not just the HTTP status

## 🏭 Industry Track Application
Custom API skills are what separate a generalist automation builder from an industry specialist. A healthtech track might integrate a real clinic-scheduling API; a real-estate track might integrate an MLS listings API; a logistics track a carrier-tracking API. If a free public API exists for your industry, use it today instead of weather/news — it's directly reusable in your Week 11 portfolio.
