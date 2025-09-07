# 📅 DAY 17: WEDNESDAY - Variables, Expressions, and Parameters

## 🎯 TODAY'S OBJECTIVES
- Master n8n expression syntax
- Learn variables and parameters
- Practice dynamic data handling
- Build expression-driven workflows

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "n8n Expression Syntax"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- Expression syntax basics
- Variables and data access
- Functions and operators
- Advanced expression patterns

#### **Key Concepts:**
- **Variables:** $json, $node, $workflow
- **Functions:** String, date, math functions
- **Operators:** Comparison, logical, arithmetic
- **Expressions:** Dynamic data manipulation

#### **Take Notes On:**
- 10 essential expression functions
- Variable access patterns
- Common expression errors
- Best practices

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "n8n Expression Guide"**
- Expression syntax reference
- Function documentation
- Variable access patterns
- Common patterns

#### **Key Takeaways:**
- Expressions make workflows dynamic
- Functions extend capabilities
- Variables access data
- Practice makes perfect

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Expression Mastery"**
**Duration:** 30 minutes

#### **Task: Master Expression Syntax**

**Step-by-Step Instructions:**

1. **Basic Variables**
   - Access $json data
   - Use $node references
   - Work with $workflow variables
   - Practice variable syntax

2. **String Functions**
   - toUpperCase(), toLowerCase()
   - trim(), split(), join()
   - substring(), replace()
   - Test string operations

3. **Date Functions**
   - $now, $today
   - format(), diff()
   - add(), subtract()
   - Practice date operations

4. **Math Functions**
   - Basic arithmetic
   - Math.round(), Math.floor()
   - Random numbers
   - Test math operations

---

### **🔍 Advanced Expression Patterns**
**Duration:** 30 minutes

#### **Task: Build Expression-Driven Workflows**

**Create These Workflows:**

1. **Dynamic Data Processing**
   - Use expressions for data transformation
   - Conditional logic with expressions
   - Dynamic field generation
   - Complex data manipulation

2. **Date and Time Workflows**
   - Dynamic date calculations
   - Time-based conditions
   - Date formatting
   - Time zone handling

3. **String Processing Workflows**
   - Text analysis with expressions
   - Dynamic string generation
   - Pattern matching
   - Text transformation

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Expression Work**
**Duration:** 20 minutes

#### **Community Post: "My Expression Mastery"**

**Share:**
- Screenshots of your expression workflows
- Complex expressions you created
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 17 Complete! 🎉

**Expression Workflows I Built:**
[Screenshots of workflows]

**What I Mastered:**
- Expression syntax
- Variables and functions
- Dynamic data handling
- Advanced patterns

**Complex Expressions:**
- [Share your most complex expression]

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 18! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 18:**
- Error handling and retry logic
- Workflow reliability
- Debugging techniques
- Production readiness

#### **Prepare:**
- Review error handling strategies
- Plan error scenarios
- Set up debugging tools

---

## 📝 DAILY TASK

### **🎯 Main Task: Create Workflow with 5 Different Expressions**

**Build a workflow demonstrating expression mastery.**

#### **Expression Mastery Workflow:**
```json
{
  "nodes": [
    {
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "parameters": {}
    },
    {
      "name": "Set Dynamic Data",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "user_input",
              "value": "={{ $json.input || 'Sample User Data' }}"
            },
            {
              "name": "processing_type",
              "value": "expression_demo"
            },
            {
              "name": "start_time",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Expression 1: String Processing",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "processed_text",
              "value": "={{ $json.user_input.trim().toUpperCase() }}"
            },
            {
              "name": "text_length",
              "value": "={{ $json.user_input.length }}"
            },
            {
              "name": "word_count",
              "value": "={{ $json.user_input.split(' ').length }}"
            },
            {
              "name": "expression_1_completed",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Expression 2: Date Calculations",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "current_date",
              "value": "={{ $now.format('YYYY-MM-DD') }}"
            },
            {
              "name": "current_time",
              "value": "={{ $now.format('HH:mm:ss') }}"
            },
            {
              "name": "processing_duration",
              "value": "={{ $now.diff($json.start_time, 'milliseconds') }}"
            },
            {
              "name": "future_date",
              "value": "={{ $now.add(7, 'days').format('YYYY-MM-DD') }}"
            },
            {
              "name": "expression_2_completed",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Expression 3: Math Operations",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "random_number",
              "value": "={{ Math.floor(Math.random() * 100) }}"
            },
            {
              "name": "calculated_value",
              "value": "={{ Math.round($json.text_length * 1.5) }}"
            },
            {
              "name": "percentage",
              "value": "={{ Math.round(($json.word_count / $json.text_length) * 100) }}"
            },
            {
              "name": "expression_3_completed",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Expression 4: Conditional Logic",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "text_category",
              "value": "={{ $json.text_length > 50 ? 'long' : 'short' }}"
            },
            {
              "name": "complexity_level",
              "value": "={{ $json.word_count > 10 ? 'complex' : 'simple' }}"
            },
            {
              "name": "processing_status",
              "value": "={{ $json.processing_duration > 1000 ? 'slow' : 'fast' }}"
            },
            {
              "name": "expression_4_completed",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Expression 5: Data Aggregation",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "summary_data",
              "value": "={{ { \"original_text\": $json.user_input, \"processed_text\": $json.processed_text, \"text_length\": $json.text_length, \"word_count\": $json.word_count, \"text_category\": $json.text_category, \"complexity_level\": $json.complexity_level, \"processing_status\": $json.processing_status, \"random_number\": $json.random_number, \"calculated_value\": $json.calculated_value, \"percentage\": $json.percentage, \"current_date\": $json.current_date, \"current_time\": $json.current_time, \"future_date\": $json.future_date, \"processing_duration\": $json.processing_duration } }}"
            },
            {
              "name": "total_processing_time",
              "value": "={{ $now.diff($json.start_time, 'milliseconds') }}"
            },
            {
              "name": "expression_5_completed",
              "value": "={{ $now }}"
            }
          ]
        }
      }
    },
    {
      "name": "Format Final Results",
      "type": "n8n-nodes-base.set",
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "final_report",
              "value": "📊 Expression Processing Report\n\n*Original Text:* {{ $json.user_input }}\n*Processed Text:* {{ $json.processed_text }}\n*Text Length:* {{ $json.text_length }} characters\n*Word Count:* {{ $json.word_count }} words\n*Text Category:* {{ $json.text_category }}\n*Complexity Level:* {{ $json.complexity_level }}\n*Processing Status:* {{ $json.processing_status }}\n*Random Number:* {{ $json.random_number }}\n*Calculated Value:* {{ $json.calculated_value }}\n*Percentage:* {{ $json.percentage }}%\n*Current Date:* {{ $json.current_date }}\n*Current Time:* {{ $json.current_time }}\n*Future Date:* {{ $json.future_date }}\n*Total Processing Time:* {{ $json.total_processing_time }}ms"
            },
            {
              "name": "report_generated",
              "value": "={{ $now }}"
            },
            {
              "name": "status",
              "value": "completed"
            }
          ]
        }
      }
    }
  ]
}
```

#### **Expected Result:**
- Workflow demonstrates 5 different expression types
- String processing with functions
- Date calculations and formatting
- Math operations and random numbers
- Conditional logic with ternary operators
- Data aggregation and formatting

---

## ✅ DAILY CHECKLIST

- [ ] Watch "n8n Expression Syntax" video
- [ ] Read expression guide
- [ ] Master basic variables
- [ ] Practice string functions
- [ ] Practice date functions
- [ ] Practice math functions
- [ ] Build expression-driven workflows
- [ ] Create complex expressions
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Understand expression syntax
- Know common functions
- Be able to use variables
- Have built expression-driven workflows
- Be comfortable with complex expressions
- Be ready for error handling

---

## 💡 PRO TIPS

1. **Start Simple:** Begin with basic expressions
2. **Use Functions:** Leverage built-in functions
3. **Test Expressions:** Always test complex expressions
4. **Document Logic:** Keep notes on complex expressions
5. **Practice Regularly:** Expressions improve with practice

---

## 🚀 TOMORROW PREVIEW

**Day 18:** We'll dive into error handling and retry logic, learn debugging techniques, and start building production-ready workflows. Get ready for reliability! 🔧

---

*Remember: Expressions make workflows dynamic! Master the syntax! 🚀*
