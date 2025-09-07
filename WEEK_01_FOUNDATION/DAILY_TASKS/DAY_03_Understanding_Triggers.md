# 📅 DAY 3: WEDNESDAY - Understanding Triggers

## 🎯 TODAY'S OBJECTIVES
- Learn about different trigger types
- Understand webhook vs schedule vs manual triggers
- Practice setting up each trigger type
- Build workflows with different triggers

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Understanding n8n Triggers"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- Different types of triggers
- When to use each trigger type
- Trigger configuration options
- Best practices for triggers

#### **Key Concepts:**
- **Manual Trigger:** Starts workflows manually
- **Webhook Trigger:** Receives HTTP requests
- **Schedule Trigger:** Runs on time intervals
- **Event Trigger:** Responds to external events

#### **Take Notes On:**
- 4 main trigger types and their uses
- Configuration options for each trigger
- When to use each trigger type

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "n8n Triggers Documentation"**
- Trigger types overview
- Configuration parameters
- Best practices
- Common use cases

#### **Key Takeaways:**
- Triggers are the starting point of workflows
- Each trigger has specific configuration options
- Choose triggers based on your use case
- Triggers can be combined with conditions

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Setting Up Different Triggers"**
**Duration:** 30 minutes

#### **Task: Create Workflows with Different Triggers**

**Step-by-Step Instructions:**

1. **Manual Trigger Workflow**
   - Create new workflow
   - Add Manual Trigger node
   - Add Set node with sample data
   - Test execution

2. **Webhook Trigger Workflow**
   - Create new workflow
   - Add Webhook node
   - Configure webhook path
   - Test with HTTP request

3. **Schedule Trigger Workflow**
   - Create new workflow
   - Add Schedule Trigger node
   - Set to run every 5 minutes
   - Add Set node with timestamp

---

### **🔍 Explore Trigger Configurations**
**Duration:** 30 minutes

#### **Task: Experiment with Trigger Settings**

**For Each Trigger Type:**
1. **Manual Trigger**
   - Test different execution modes
   - Try with and without input data

2. **Webhook Trigger**
   - Test different HTTP methods
   - Try with authentication
   - Test with different data formats

3. **Schedule Trigger**
   - Test different time intervals
   - Try cron expressions
   - Test with timezone settings

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Progress**
**Duration:** 20 minutes

#### **Community Post: "My Trigger Experiments"**

**Share:**
- Screenshots of your trigger workflows
- What you learned about each trigger type
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 3 Complete! 🎉

**What I Built:**
[Screenshots of trigger workflows]

**What I Learned:**
- Manual triggers for testing
- Webhook triggers for external events
- Schedule triggers for automation

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 4! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 4:**
- Self-hosting n8n with Docker
- VPS setup and configuration
- Domain and SSL setup

#### **Prepare:**
- Research VPS providers
- Have domain name ready
- Review Docker basics

---

## 📝 DAILY TASK

### **🎯 Main Task: Create Trigger Workflows**

**Create 3 workflows, each using a different trigger type.**

#### **Workflow 1: Manual Trigger**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Set Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "message",
              "value": "Manual trigger executed!"
            },
            {
              "name": "timestamp",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

#### **Workflow 2: Webhook Trigger**
```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "test-webhook",
        "httpMethod": "POST"
      }
    },
    {
      "name": "Process Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "received_data",
              "value": "={{ $json }}"
            },
            {
              "name": "processed_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

#### **Workflow 3: Schedule Trigger**
```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 5
            }
          ]
        }
      }
    },
    {
      "name": "Generate Report",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "report_type",
              "value": "Scheduled Report"
            },
            {
              "name": "generated_at",
              "value": "={{ $now }}"
            },
            {
              "name": "status",
              "value": "Completed"
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

- [ ] Watch "Understanding n8n Triggers" video
- [ ] Read n8n triggers documentation
- [ ] Create manual trigger workflow
- [ ] Create webhook trigger workflow
- [ ] Create schedule trigger workflow
- [ ] Test all trigger configurations
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Understand different trigger types
- Know when to use each trigger
- Have built workflows with all trigger types
- Be comfortable configuring triggers
- Know trigger best practices

---

## 💡 PRO TIPS

1. **Start Simple:** Begin with manual triggers for testing
2. **Test Webhooks:** Use tools like Postman to test webhooks
3. **Schedule Carefully:** Don't set schedules too frequent
4. **Document URLs:** Keep track of webhook URLs
5. **Use Conditions:** Combine triggers with IF nodes

---

## 🚀 TOMORROW PREVIEW

**Day 4:** We'll dive into self-hosting n8n, learn about Docker, and set up your production environment. Get ready to deploy! 🐳

---

*Remember: Triggers are the foundation of automation! Master these concepts! 🚀*
