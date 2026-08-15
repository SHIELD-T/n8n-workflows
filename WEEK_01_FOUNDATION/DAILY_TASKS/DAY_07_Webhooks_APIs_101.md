# DAY 7: Webhooks & APIs 101
**Week:** 1 — Foundation  |  **Time:** 2-3 hours  |  **Difficulty:** Beginner

## 🎯 What You'll Learn
- HTTP methods (GET, POST, PUT, DELETE) and what each is for
- Common status codes (200, 404, 500) and what they tell you about a failed call
- How to read API documentation to find endpoints, auth requirements, and rate limits
- How to make authenticated and unauthenticated API calls from the HTTP Request node

## 🎥 Watch First
- [Using webhooks in n8n (parameters, responses and triggers)](https://www.youtube.com/watch?v=IvUYJQkf6sA) — full 15-minute tutorial. Note specifically how query parameters vs. path parameters vs. headers are each configured differently in the HTTP Request node.

## 🛠️ Build It: Step-by-Step
1. Build **Call 1 (no auth):** Manual Trigger → HTTP Request node, Method GET, URL `https://jsonplaceholder.typicode.com/posts`. Execute and confirm you get a JSON array back.
2. Add a Set node after it: `total_posts = {{ $json.length }}`, `first_post_title = {{ $json[0].title }}`. Confirm both values populate correctly.
3. Sign up for a free OpenWeatherMap API key. Build **Call 2 (query-param auth):** HTTP Request node, GET, URL `https://api.openweathermap.org/data/2.5/weather`, Query Parameters: `q=London`, `appid=<your key>`, `units=metric`. Execute and confirm you get real weather data.
4. Add a Set node to format the result: `city = {{ $json.name }}`, `temperature = {{ $json.main.temp }}°C`, `description = {{ $json.weather[0].description }}`.
5. Sign up for a free NewsAPI key. Build **Call 3:** HTTP Request node, GET, URL `https://newsapi.org/v2/top-headlines`, Query Parameters: `country=us`, `apiKey=<your key>`. Execute and confirm articles return.
6. Deliberately trigger a 401/403 by using a wrong or blank API key on one of the calls — read the exact status code and error body n8n shows you, and write down what it means.
7. Deliberately trigger a 404 by mistyping a URL path — compare that error to the 401 from step 6 so you can tell them apart at a glance in future debugging.

**Stuck?** Import `WEEK_01_FOUNDATION/EXAMPLES/example_workflow_1.json` or `example_workflow_2.json` for more HTTP Request node configuration examples.

## 🔑 Credentials Needed
- OpenWeatherMap API key (free tier)
- NewsAPI API key (free tier)
- No credential needed for JSONPlaceholder (public test API)

## ✅ Definition of Done
- [ ] All three API calls (JSONPlaceholder, OpenWeatherMap, NewsAPI) return real data visible in the node output
- [ ] You've reproduced and can explain the difference between a 401 (auth failure) and a 404 (wrong URL) using your own deliberately-broken tests
- [ ] You can state, without looking it up, what GET vs POST vs PUT vs DELETE are each typically used for
- [ ] You've located and read the "rate limits" section of at least one of these APIs' documentation

## 🐛 Common Pitfalls
- **API key placed in the wrong field:** Some APIs want the key in a query parameter (`appid=`), others in a header (`Authorization: Bearer`) — check the docs; putting it in the wrong place produces a 401 that looks like a "wrong key" error even when the key is correct.
- **Rate limit exhaustion:** Free tiers often cap at 60 calls/minute or 1000/day — if you suddenly start getting 429 errors, check the docs for your plan's limit before assuming your code is broken.
- **Trailing/missing slashes and typos in the URL path:** A single mismatched character produces a 404, not a helpful "did you mean" — copy-paste endpoint paths directly from documentation rather than retyping them.

## 🏭 Industry Track Application
Find one real, freely-available API relevant to your industry track (e.g., a public banking-sandbox API for Fintech, a public health-data API for HealthTech, an open courses API for EdTech) and repeat steps 1-2 against it: make a successful call and extract at least 2 fields into a Set node. Document the auth method it uses in your notes.
