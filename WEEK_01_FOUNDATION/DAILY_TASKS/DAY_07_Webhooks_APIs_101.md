# 📅 DAY 7: SUNDAY - Webhooks & APIs 101

## 🎯 TODAY'S OBJECTIVES
- Learn webhooks and APIs fundamentals
- Understand HTTP methods and status codes
- Practice reading API documentation
- Build API integration workflows

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 1 hour (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Webhooks & APIs for Beginners"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- What are webhooks and APIs
- HTTP methods and status codes
- API authentication methods
- Reading API documentation

#### **Key Concepts:**
- **API:** Application Programming Interface
- **Webhook:** HTTP callback for real-time events
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200, 404, 500, etc.

#### **Take Notes On:**
- 4 main HTTP methods
- Common status codes and meanings
- Authentication types
- API documentation structure

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "API Documentation Best Practices"**
- How to read API docs
- Common API patterns
- Authentication methods
- Error handling

#### **Key Takeaways:**
- API docs are your roadmap
- Authentication is crucial
- Error handling is important
- Rate limits exist for a reason

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Making API Calls"**
**Duration:** 30 minutes

#### **Task: Build API Integration Workflows**

**Step-by-Step Instructions:**

1. **Public API Test (JSONPlaceholder)**
   - Create workflow with HTTP Request node
   - Make GET request to JSONPlaceholder
   - Process response data
   - Test error handling

2. **Weather API Integration**
   - Sign up for OpenWeatherMap API
   - Create weather checking workflow
   - Process weather data
   - Format response

3. **News API Integration**
   - Use NewsAPI or similar
   - Create news fetching workflow
   - Process news articles
   - Format for display

---

### **🔍 Practice API Documentation Reading**
**Duration:** 30 minutes

#### **Task: Analyze Different APIs**

**For Each API:**
1. **Read Documentation**
   - Understand endpoints
   - Check authentication requirements
   - Review request/response formats
   - Note rate limits

2. **Test API Calls**
   - Make sample requests
   - Test different parameters
   - Handle different responses
   - Practice error scenarios

3. **Build Integration**
   - Create n8n workflow
   - Implement API calls
   - Process responses
   - Handle errors

---

## 🌙 EVENING SESSION (1 hour)

### **📸 Share Your API Work**
**Duration:** 30 minutes

#### **Community Post: "My API Integration Journey"**

**Share:**
- Screenshots of your API workflows
- APIs you integrated
- Challenges faced
- Questions for the community

#### **Post Template:**
```
Day 7 Complete! 🎉

**APIs I Integrated:**
[Screenshots of workflows]

**What I Learned:**
- HTTP methods and status codes
- API authentication
- Reading documentation
- Error handling

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Week 1 Complete! 🚀
```

---

### **📋 Week 1 Review**
**Duration:** 30 minutes

#### **Review Your Progress:**
- What you learned this week
- Workflows you built
- Challenges you overcame
- Goals for next week

#### **Prepare for Week 2:**
- Review Week 2 materials
- Set up any needed accounts
- Plan your learning schedule
- Connect with community

---

## 📝 DAILY TASK

### **🎯 Main Task: Integrate 3 Different APIs**

**Make successful API calls to 3 different services using n8n.**

#### **API Integration Examples:**

**1. JSONPlaceholder API (Public)**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Get Posts",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "https://jsonplaceholder.typicode.com/posts",
        "options": {
          "response": {
            "response": {
              "responseFormat": "json"
            }
          }
        }
      }
    },
    {
      "name": "Process Posts",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "total_posts",
              "value": "={{ $json.length }}"
            },
            {
              "name": "first_post_title",
              "value": "={{ $json[0].title }}"
            },
            {
              "name": "fetched_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

**2. Weather API Integration**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Get Weather",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "https://api.openweathermap.org/data/2.5/weather",
        "qs": {
          "q": "London",
          "appid": "YOUR_API_KEY",
          "units": "metric"
        }
      }
    },
    {
      "name": "Format Weather",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "city",
              "value": "={{ $json.name }}"
            },
            {
              "name": "temperature",
              "value": "={{ $json.main.temp }}°C"
            },
            {
              "name": "description",
              "value": "={{ $json.weather[0].description }}"
            },
            {
              "name": "fetched_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

**3. News API Integration**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Get News",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "https://newsapi.org/v2/top-headlines",
        "qs": {
          "country": "us",
          "apiKey": "YOUR_API_KEY"
        }
      }
    },
    {
      "name": "Process News",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "total_articles",
              "value": "={{ $json.totalResults }}"
            },
            {
              "name": "first_article_title",
              "value": "={{ $json.articles[0].title }}"
            },
            {
              "name": "first_article_url",
              "value": "={{ $json.articles[0].url }}"
            },
            {
              "name": "fetched_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Webhooks & APIs for Beginners" video
- [ ] Read API documentation guide
- [ ] Integrate JSONPlaceholder API
- [ ] Integrate Weather API
- [ ] Integrate News API
- [ ] Test all API integrations
- [ ] Practice error handling
- [ ] Share progress in community
- [ ] Review Week 1 progress
- [ ] Plan for Week 2
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Understand webhooks and APIs
- Know HTTP methods and status codes
- Be able to read API documentation
- Have integrated 3 different APIs
- Be ready for advanced workflow building

---

## 💡 PRO TIPS

1. **Start with Public APIs:** Use free APIs for learning
2. **Read Documentation:** Always check API docs first
3. **Handle Errors:** Implement proper error handling
4. **Respect Rate Limits:** Don't overwhelm APIs
5. **Test Thoroughly:** Validate all API responses

---

## 🎉 WEEK 1 COMPLETE!

**Congratulations! You've completed Week 1 of the Automator Pro course!**

### **What You've Achieved:**
- ✅ Learned automation basics
- ✅ Mastered n8n interface
- ✅ Built your first workflows
- ✅ Set up self-hosted n8n
- ✅ Created real-world automation
- ✅ Integrated multiple APIs

### **Your Automation Journey Continues:**
- **Week 2:** Advanced workflow building
- **Week 3:** Complex data processing
- **Week 4:** Production deployment
- **Week 5:** AI integration begins

---

*Remember: You're building the foundation for automation mastery! Keep going! 🚀*
