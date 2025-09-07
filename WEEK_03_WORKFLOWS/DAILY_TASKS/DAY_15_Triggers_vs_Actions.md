# 📅 DAY 15: MONDAY - Triggers vs. Actions

## 🎯 TODAY'S OBJECTIVES
- Master the difference between triggers and actions
- Learn when to use each trigger type
- Practice building workflows with different triggers
- Understand trigger configuration options

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Understanding Triggers vs. Actions"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- Trigger vs. action concepts
- Different trigger types and their uses
- Action node types and configurations
- Workflow design patterns

#### **Key Concepts:**
- **Triggers:** Start workflows (webhook, schedule, manual)
- **Actions:** Perform tasks (HTTP, email, database)
- **Conditions:** Control workflow flow (IF, switch)
- **Transformations:** Modify data (SET, function)

#### **Take Notes On:**
- 5 main trigger types
- 10 common action nodes
- When to use each type
- Workflow design patterns

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "n8n Triggers and Actions Guide"**
- Trigger types overview
- Action node categories
- Best practices
- Common patterns

#### **Key Takeaways:**
- Triggers start workflows
- Actions perform tasks
- Choose the right tool for the job
- Design workflows logically

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Building Trigger Workflows"**
**Duration:** 30 minutes

#### **Task: Create Workflows with Different Triggers**

**Step-by-Step Instructions:**

1. **Manual Trigger Workflow**
   - Create workflow with manual trigger
   - Add data processing actions
   - Test execution
   - Document results

2. **Webhook Trigger Workflow**
   - Create webhook trigger
   - Add data validation
   - Process incoming data
   - Return response

3. **Schedule Trigger Workflow**
   - Create schedule trigger
   - Add data collection
   - Process and format data
   - Send notifications

---

### **🔍 Explore Action Nodes**
**Duration:** 30 minutes

#### **Task: Master Common Action Nodes**

**For Each Action Type:**
1. **HTTP Actions**
   - GET requests
   - POST requests
   - PUT/DELETE requests
   - Error handling

2. **Data Actions**
   - SET node for data manipulation
   - IF node for conditions
   - Function node for custom logic
   - Split/merge operations

3. **Integration Actions**
   - Email sending
   - Slack notifications
   - Database operations
   - File operations

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Trigger Workflows**
**Duration:** 20 minutes

#### **Community Post: "My Trigger vs. Action Workflows"**

**Share:**
- Screenshots of your workflows
- What you learned about triggers vs. actions
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 15 Complete! 🎉

**Trigger Workflows I Built:**
[Screenshots of workflows]

**What I Learned:**
- Triggers start workflows
- Actions perform tasks
- Different trigger types
- Action node categories

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 16! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 16:**
- Built-in nodes mastery
- HTTP, IF, SET, SplitInBatches nodes
- Node parameter configuration
- Advanced node usage

#### **Prepare:**
- Review node documentation
- Plan node experiments
- Set up test data

---

## 📝 DAILY TASK

### **🎯 Main Task: Create 3 Workflows with Different Triggers**

**Build workflows using different trigger types.**

#### **Workflow 1: Manual Trigger with Actions**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Set Sample Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "user_name",
              "value": "John Doe"
            },
            {
              "name": "user_email",
              "value": "john@example.com"
            },
            {
              "name": "action_type",
              "value": "manual_trigger"
            }
          ]
        }
      }
    },
    {
      "name": "Process Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "processed_name",
              "value": "={{ $json.user_name.toUpperCase() }}"
            },
            {
              "name": "processed_email",
              "value": "={{ $json.user_email.toLowerCase() }}"
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

#### **Workflow 2: Webhook Trigger with Actions**
```json
{
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "trigger-actions",
        "httpMethod": "POST"
      }
    },
    {
      "name": "Validate Input",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.data }}",
              "operation": "isNotEmpty"
            }
          ]
        }
      }
    },
    {
      "name": "Process Input",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "processed_data",
              "value": "={{ $json.data.trim() }}"
            },
            {
              "name": "action_type",
              "value": "webhook_trigger"
            },
            {
              "name": "processed_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Return Response",
      "type": "n8n-nodes-base.respondToWebhook",
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { \"status\": \"success\", \"processed_data\": $json.processed_data, \"action_type\": $json.action_type } }}"
      }
    }
  ]
}
```

#### **Workflow 3: Schedule Trigger with Actions**
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
              "field": "hours",
              "hoursInterval": 2
            }
          ]
        }
      }
    },
    {
      "name": "Collect Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "collection_time",
              "value": "={{ $now }}"
            },
            {
              "name": "data_source",
              "value": "scheduled_collection"
            },
            {
              "name": "action_type",
              "value": "schedule_trigger"
            }
          ]
        }
      }
    },
    {
      "name": "Process Collected Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "processed_data",
              "value": "={{ { \"collection_time\": $json.collection_time, \"data_source\": $json.data_source, \"action_type\": $json.action_type } }}"
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

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Understanding Triggers vs. Actions" video
- [ ] Read triggers and actions guide
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
- Understand triggers vs. actions
- Know when to use each trigger type
- Have built workflows with different triggers
- Be comfortable with action nodes
- Be ready for advanced node work

---

## 💡 PRO TIPS

1. **Start with Manual:** Use manual triggers for testing
2. **Test Webhooks:** Use tools like Postman to test
3. **Schedule Carefully:** Don't set schedules too frequent
4. **Use Actions Wisely:** Choose the right action for the task
5. **Document Everything:** Keep notes on your workflows

---

## 🚀 TOMORROW PREVIEW

**Day 16:** We'll dive into built-in nodes mastery, learn about HTTP, IF, SET, and SplitInBatches nodes, and start building more sophisticated workflows. Get ready for node mastery! 🛠️

---

*Remember: Triggers start the journey, actions do the work! Master both concepts! 🚀*
