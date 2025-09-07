# 📅 DAY 16: TUESDAY - Built-in Nodes Mastery

## 🎯 TODAY'S OBJECTIVES
- Master HTTP, IF, SET, SplitInBatches nodes
- Learn node parameter configuration
- Practice advanced node usage
- Build complex workflows

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Mastering Built-in Nodes"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- HTTP Request node deep dive
- IF node conditions and logic
- SET node data manipulation
- SplitInBatches node processing

#### **Key Concepts:**
- **HTTP Request:** API calls, methods, headers
- **IF Node:** Conditions, operators, logic flow
- **SET Node:** Data transformation, expressions
- **SplitInBatches:** Batch processing, pagination

#### **Take Notes On:**
- HTTP request configuration options
- IF node condition types
- SET node expression syntax
- SplitInBatches use cases

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "n8n Built-in Nodes Documentation"**
- HTTP Request node guide
- IF node conditions
- SET node expressions
- SplitInBatches patterns

#### **Key Takeaways:**
- HTTP node is powerful for API integration
- IF node controls workflow flow
- SET node transforms data
- SplitInBatches handles large datasets

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Node Mastery"**
**Duration:** 30 minutes

#### **Task: Master Each Node Type**

**Step-by-Step Instructions:**

1. **HTTP Request Node**
   - Configure GET request
   - Add headers and authentication
   - Handle different response formats
   - Test error scenarios

2. **IF Node**
   - Create simple conditions
   - Use multiple conditions
   - Test different operators
   - Practice complex logic

3. **SET Node**
   - Basic data assignment
   - Use expressions
   - Transform data types
   - Practice advanced expressions

4. **SplitInBatches Node**
   - Configure batch size
   - Process large datasets
   - Handle batch results
   - Test with different data

---

### **🔍 Advanced Node Usage**
**Duration:** 30 minutes

#### **Task: Build Complex Node Workflows**

**Create These Workflows:**

1. **HTTP + IF + SET Workflow**
   - Make API call
   - Check response status
   - Transform data based on conditions
   - Format output

2. **SplitInBatches + Processing Workflow**
   - Split large dataset
   - Process each batch
   - Aggregate results
   - Handle errors

3. **Multi-Condition Workflow**
   - Multiple IF nodes
   - Complex logic flow
   - Different processing paths
   - Result aggregation

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Node Mastery**
**Duration:** 20 minutes

#### **Community Post: "My Built-in Node Workflows"**

**Share:**
- Screenshots of your node workflows
- What you learned about each node
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 16 Complete! 🎉

**Node Workflows I Built:**
[Screenshots of workflows]

**What I Mastered:**
- HTTP Request node
- IF node conditions
- SET node expressions
- SplitInBatches processing

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 17! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 17:**
- Variables, expressions, and parameters
- n8n expression syntax
- Dynamic data handling
- Advanced expressions

#### **Prepare:**
- Review expression syntax
- Plan expression experiments
- Set up test data

---

## 📝 DAILY TASK

### **🎯 Main Task: Build Workflow Using HTTP, IF, SET, and SplitInBatches**

**Create a sophisticated workflow using all four node types.**

#### **Complete Node Mastery Workflow:**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Set API Configuration",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "api_url",
              "value": "https://jsonplaceholder.typicode.com/posts"
            },
            {
              "name": "batch_size",
              "value": 5
            },
            {
              "name": "processing_type",
              "value": "batch_processing"
            }
          ]
        }
      }
    },
    {
      "name": "Fetch Data via HTTP",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "method": "GET",
        "url": "={{ $json.api_url }}",
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
      "name": "Check Data Validity",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "array": [
            {
              "value1": "={{ $json }}",
              "operation": "isNotEmpty"
            }
          ]
        }
      }
    },
    {
      "name": "Split Data into Batches",
      "type": "n8n-nodes-base.splitInBatches",
      "parameters": {
        "batchSize": "={{ $('Set API Configuration').item.json.batch_size }}",
        "options": {}
      }
    },
    {
      "name": "Process Each Batch",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "batch_data",
              "value": "={{ $json }}"
            },
            {
              "name": "batch_size",
              "value": "={{ $json.length }}"
            },
            {
              "name": "processed_at",
              "value": "={{ $now }}"
            },
            {
              "name": "batch_id",
              "value": "={{ $now.format('YYYYMMDDHHmmss') }}"
            }
          ]
        }
      }
    },
    {
      "name": "Check Batch Content",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{ $json.batch_size }}",
              "operation": "larger",
              "value2": 0
            }
          ]
        }
      }
    },
    {
      "name": "Format Batch Results",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "formatted_results",
              "value": "={{ { \"batch_id\": $json.batch_id, \"batch_size\": $json.batch_size, \"processed_at\": $json.processed_at, \"data\": $json.batch_data } }}"
            },
            {
              "name": "status",
              "value": "processed"
            }
          ]
        }
      }
    },
    {
      "name": "Log Batch Processing",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "log_entry",
              "value": "Batch {{ $json.batch_id }} processed successfully with {{ $json.batch_size }} items"
            },
            {
              "name": "logged_at",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Handle Invalid Data",
      "type": "n8n-nodes-base.set",
      "position": [500, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "error_type",
              "value": "invalid_data"
            },
            {
              "name": "error_message",
              "value": "No valid data received from API"
            },
            {
              "name": "error_time",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Handle Empty Batch",
      "type": "n8n-nodes-base.set",
      "position": [900, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "warning_type",
              "value": "empty_batch"
            },
            {
              "name": "warning_message",
              "value": "Batch contains no data"
            },
            {
              "name": "warning_time",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    }
  ]
}
```

#### **Expected Result:**
- Workflow fetches data via HTTP
- Validates data with IF node
- Splits data into batches
- Processes each batch
- Handles errors gracefully
- Logs all activities

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Mastering Built-in Nodes" video
- [ ] Read built-in nodes documentation
- [ ] Master HTTP Request node
- [ ] Master IF node conditions
- [ ] Master SET node expressions
- [ ] Master SplitInBatches node
- [ ] Build complex node workflow
- [ ] Test all node configurations
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Master HTTP Request node
- Understand IF node conditions
- Know SET node expressions
- Be able to use SplitInBatches
- Have built complex workflows
- Be ready for advanced expressions

---

## 💡 PRO TIPS

1. **HTTP Node:** Use for all API integrations
2. **IF Node:** Control workflow flow logically
3. **SET Node:** Transform data with expressions
4. **SplitInBatches:** Handle large datasets efficiently
5. **Test Thoroughly:** Always test node configurations

---

## 🚀 TOMORROW PREVIEW

**Day 17:** We'll dive into variables, expressions, and parameters, learn n8n expression syntax, and start building dynamic workflows. Get ready for expression mastery! 📝

---

*Remember: Built-in nodes are your automation toolkit! Master them all! 🚀*
