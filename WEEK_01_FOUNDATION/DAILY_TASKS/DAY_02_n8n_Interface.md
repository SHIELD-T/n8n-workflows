# 📅 DAY 2: TUESDAY - Intro to n8n Core Concepts

## 🎯 TODAY'S OBJECTIVES
- Learn the n8n interface and navigation
- Understand core concepts (nodes, triggers, execution)
- Practice building your first workflow
- Get comfortable with the n8n canvas

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "n8n Interface Walkthrough"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- n8n interface overview
- Workflow canvas navigation
- Node library exploration
- Basic workflow creation

#### **Key Concepts:**
- **Workflow Canvas:** Main area for building workflows
- **Node Library:** Available nodes and their functions
- **Execution History:** Track workflow runs
- **Credentials:** Secure storage for API keys

#### **Take Notes On:**
- 5 essential n8n interface elements
- 3 types of nodes you'll use most
- How to navigate the workflow canvas

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "n8n Core Concepts Documentation"**
- Nodes and their purposes
- Triggers vs. actions
- Data flow between nodes
- Execution modes

#### **Key Takeaways:**
- Nodes are the building blocks of workflows
- Triggers start workflows, actions perform tasks
- Data flows from left to right
- Each execution creates a new run

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Your First Workflow"**
**Duration:** 30 minutes

#### **Task: Create a Simple Manual Workflow**

**Step-by-Step Instructions:**

1. **Open n8n Interface**
   - Navigate to your n8n instance
   - Click "New Workflow"

2. **Add Manual Trigger**
   - Drag "Manual Trigger" from node library
   - This starts your workflow manually

3. **Add Set Node**
   - Drag "Set" node from node library
   - Connect it to the Manual Trigger

4. **Configure Set Node**
   - Click on the Set node
   - Add a field: `message` = `"Hello from n8n!"`
   - Save the node

5. **Add HTTP Request Node**
   - Drag "HTTP Request" node
   - Connect it to the Set node
   - Configure: Method = POST, URL = `https://httpbin.org/post`
   - Body = `{{ $json.message }}`

6. **Execute Workflow**
   - Click "Execute Workflow"
   - Watch the data flow through nodes

---

### **🔍 Explore Node Library**
**Duration:** 30 minutes

#### **Task: Familiarize Yourself with Common Nodes**

**Nodes to Explore:**
1. **Manual Trigger** - Starts workflows manually
2. **Webhook** - Receives HTTP requests
3. **HTTP Request** - Makes API calls
4. **Set** - Manipulates data
5. **IF** - Conditional logic
6. **Code** - Custom JavaScript
7. **Email** - Sends emails
8. **Slack** - Slack integration
9. **Google Sheets** - Spreadsheet operations
10. **Telegram** - Telegram bot

#### **For Each Node, Note:**
- What it does
- When you'd use it
- Required parameters
- Example use cases

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Progress**
**Duration:** 20 minutes

#### **Community Post: "My First n8n Workflow"**

**Share:**
- Screenshot of your workflow
- What you learned
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 2 Complete! 🎉

**What I Built:**
[Screenshot of workflow]

**What I Learned:**
- How to add and connect nodes
- Basic data flow concepts
- HTTP Request node usage

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Looking forward to Day 3! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 3:**
- Understanding different trigger types
- Webhook setup and testing
- API integration basics

#### **Prepare:**
- Review HTTP basics
- Have Postman ready (if available)
- Clear your workspace

---

## 📝 DAILY TASK

### **🎯 Main Task: Build a Simple Workflow**

**Create a workflow that takes text input and outputs it to a file.**

#### **Step-by-Step Instructions:**

1. **Create New Workflow**
   - Open n8n
   - Click "New Workflow"

2. **Add Manual Trigger**
   - Drag "Manual Trigger" from library
   - This will start your workflow

3. **Add Set Node**
   - Drag "Set" node
   - Connect to Manual Trigger
   - Configure:
     - Field: `text`
     - Value: `"This is my first n8n workflow!"`

4. **Add Write Binary File Node**
   - Drag "Write Binary File" node
   - Connect to Set node
   - Configure:
     - File Name: `output.txt`
     - Data: `{{ $json.text }}`

5. **Execute and Test**
   - Click "Execute Workflow"
   - Check if file was created
   - Verify file contents

#### **Expected Result:**
- Workflow executes successfully
- File named `output.txt` is created
- File contains your text message

---

## ✅ DAILY CHECKLIST

- [ ] Watch "n8n Interface Walkthrough" video
- [ ] Read n8n core concepts documentation
- [ ] Create first manual workflow
- [ ] Explore node library
- [ ] Build text-to-file workflow
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Understand the n8n interface
- Know core concepts (nodes, triggers, execution)
- Have built your first workflow
- Be comfortable navigating the canvas
- Know common node types and their uses

---

## 💡 PRO TIPS

1. **Practice Regularly:** Build workflows daily to reinforce learning
2. **Explore Nodes:** Don't be afraid to try different nodes
3. **Use Documentation:** n8n docs are your best friend
4. **Take Screenshots:** Document your learning journey
5. **Ask Questions:** Community is there to help

---

## 🚀 TOMORROW PREVIEW

**Day 3:** We'll dive into triggers, learn about webhooks, and start building more dynamic workflows. Get ready to make your workflows respond to external events! 🔗

---

*Remember: Every expert was once a beginner. You're building the foundation for automation mastery! 🛠️*
