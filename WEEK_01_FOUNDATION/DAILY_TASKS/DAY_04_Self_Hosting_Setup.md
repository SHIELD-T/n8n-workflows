# 📅 DAY 4: THURSDAY - Self-Hosting Setup

## 🎯 TODAY'S OBJECTIVES
- Learn about self-hosting n8n on Render
- Set up Render account and deploy n8n
- Configure free hosting with cronjob keep-alive
- Set up custom domain and SSL

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Self-Hosting n8n on Render"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- Render platform basics
- n8n deployment on Render
- Free hosting limitations and solutions
- Cronjob keep-alive setup
- Custom domain configuration

#### **Key Concepts:**
- **Render:** Free cloud hosting platform
- **Web Service:** Containerized applications
- **Cronjob:** Automated keep-alive requests
- **Custom Domain:** Your n8n URL
- **SSL:** Automatic HTTPS certificates

#### **Take Notes On:**
- Render account setup
- n8n deployment process
- Free tier limitations
- Keep-alive strategies
- Domain configuration

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "Render Platform Guide"**
- What is Render
- Free tier limitations
- Web service deployment
- Custom domain setup
- Keep-alive strategies

#### **Key Takeaways:**
- Render offers free hosting
- Free tier sleeps after 15 minutes of inactivity
- Cronjobs can keep services awake
- Automatic SSL certificates
- Easy custom domain setup

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Setting Up Render Account"**
**Duration:** 30 minutes

#### **Task: Prepare Your Render Account**

**Step-by-Step Instructions:**

1. **Create Render Account**
   - Go to render.com
   - Sign up with GitHub/Google
   - Verify email address
   - Complete profile setup

2. **Prepare GitHub Repository**
   - Create new GitHub repo
   - Add n8n Dockerfile
   - Add render.yaml configuration
   - Push to GitHub

3. **Set Up Domain (Optional)**
   - Purchase domain name
   - Point DNS to Render
   - Wait for DNS propagation

---

### **🚀 Deploy n8n on Render**
**Duration:** 30 minutes

#### **Task: Deploy n8n with Render**

**Files to Create:**

1. **Dockerfile:**
```dockerfile
FROM n8nio/n8n

# Set environment variables
ENV N8N_BASIC_AUTH_ACTIVE=true
ENV N8N_BASIC_AUTH_USER=admin
ENV N8N_BASIC_AUTH_PASSWORD=your_secure_password
ENV WEBHOOK_URL=https://your-app-name.onrender.com
ENV N8N_PORT=10000

# Expose port
EXPOSE 10000

# Start n8n
CMD ["n8n"]
```

2. **render.yaml:**
```yaml
services:
  - type: web
    name: n8n-automation
    env: docker
    dockerfilePath: ./Dockerfile
    plan: free
    envVars:
      - key: N8N_BASIC_AUTH_ACTIVE
        value: true
      - key: N8N_BASIC_AUTH_USER
        value: admin
      - key: N8N_BASIC_AUTH_PASSWORD
        value: your_secure_password
      - key: WEBHOOK_URL
        value: https://your-app-name.onrender.com
```

3. **Deploy Steps:**
   - Push files to GitHub
   - Connect GitHub repo to Render
   - Deploy web service
   - Wait for deployment to complete

---

### **⏰ Set Up Cronjob Keep-Alive**
**Duration:** 15 minutes

#### **Task: Keep Your n8n Server Awake**

**The Problem:**
- Render free tier sleeps after 15 minutes of inactivity
- Your n8n instance will go to sleep
- Webhooks won't work when sleeping

**The Solution:**
Set up a cronjob to ping your server every 10 minutes.

**Step-by-Step Instructions:**

1. **Create Keep-Alive Script:**
```bash
# Create a simple HTML file for ping
echo "<!DOCTYPE html>
<html>
<head><title>n8n Keep-Alive</title></head>
<body><h1>n8n Server is Alive!</h1></body>
</html>" > keep-alive.html
```

2. **Set Up Cronjob Service:**
   - Use a free cronjob service like:
     - **cron-job.org** (free)
     - **EasyCron** (free tier)
     - **SetCronJob** (free tier)

3. **Configure Cronjob:**
   - **URL:** `https://your-app-name.onrender.com/`
   - **Schedule:** Every 10 minutes
   - **Method:** GET
   - **Timeout:** 30 seconds

4. **Alternative: Use UptimeRobot:**
   - Sign up at uptimerobot.com
   - Add your n8n URL
   - Set monitoring interval to 5 minutes
   - Free tier allows 50 monitors

**Pro Tip:** You can also create a simple n8n workflow that runs every 10 minutes to keep itself awake!

---

### **🗄️ Set Up Database Storage**
**Duration:** 15 minutes

#### **Task: Create Persistent Database for Workflows**

**The Problem:**
- Render free tier doesn't persist data between deployments
- Workflows and data are lost when container restarts
- Need reliable storage for production use

**The Solution:**
Set up Render PostgreSQL database with automated backups.

**Step-by-Step Instructions:**

1. **Create Render Database:**
   - Go to Render Dashboard
   - Click "New +" → "PostgreSQL"
   - Choose "Free" plan
   - Set database name (e.g., "n8n-workflows")
   - Note down connection details

2. **Configure n8n Database Connection:**
```yaml
# Update render.yaml
services:
  - type: web
    name: n8n-automation
    env: docker
    dockerfilePath: ./Dockerfile
    plan: free
    envVars:
      - key: N8N_BASIC_AUTH_ACTIVE
        value: true
      - key: N8N_BASIC_AUTH_USER
        value: admin
      - key: N8N_BASIC_AUTH_PASSWORD
        value: your_secure_password
      - key: WEBHOOK_URL
        value: https://your-app-name.onrender.com
      - key: DB_TYPE
        value: postgresdb
      - key: DB_POSTGRESDB_HOST
        value: your-db-host.onrender.com
      - key: DB_POSTGRESDB_PORT
        value: "5432"
      - key: DB_POSTGRESDB_DATABASE
        value: your-db-name
      - key: DB_POSTGRESDB_USER
        value: your-db-user
      - key: DB_POSTGRESDB_PASSWORD
        value: your-db-password
```

3. **Set Up Database Backup Cronjob:**
   - Use cron-job.org or similar service
   - **URL:** `https://your-db-host.onrender.com/backup`
   - **Schedule:** Daily at 2 AM
   - **Method:** POST
   - **Headers:** Include authentication

4. **Alternative: Use External Database:**
   - **Supabase** (free tier)
   - **PlanetScale** (free tier)
   - **Railway** (free tier)
   - **Neon** (free tier)

**Pro Tip:** Render's free PostgreSQL database includes automated backups, so you don't need to set up manual backups!

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Progress**
**Duration:** 20 minutes

#### **Community Post: "My n8n Deployment"**

**Share:**
- Screenshot of your n8n instance
- Your n8n URL (if comfortable)
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 4 Complete! 🎉

**What I Deployed:**
[Screenshot of n8n interface]

**My Setup:**
- Hosting: Render (Free Tier)
- URL: https://your-app-name.onrender.com
- Database: ✅ PostgreSQL (Free Tier)
- Cronjob: ✅ Set up (every 10 minutes)
- SSL: ✅ Automatic
- n8n: ✅ Running

**Keep-Alive Solution:**
- Service: [cron-job.org/UptimeRobot/etc.]
- Schedule: Every 10 minutes
- Status: ✅ Active

**Database Storage:**
- Type: Render PostgreSQL
- Backup: ✅ Automated
- Status: ✅ Connected

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 5! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 5:**
- Exploring n8n UI in detail
- Workflow management
- Execution monitoring
- Error handling

#### **Prepare:**
- Access your n8n instance
- Create test workflows
- Review UI elements

---

## 📝 DAILY TASK

### **🎯 Main Task: Deploy n8n on Render**

**Successfully deploy n8n on Render with cronjob keep-alive.**

#### **Step-by-Step Checklist:**

1. **Render Account Setup**
   - [ ] Create Render account
   - [ ] Connect GitHub account
   - [ ] Verify email address

2. **GitHub Repository Setup**
   - [ ] Create new GitHub repository
   - [ ] Add Dockerfile
   - [ ] Add render.yaml
   - [ ] Push to GitHub

3. **Render Deployment**
   - [ ] Connect GitHub repo to Render
   - [ ] Deploy web service
   - [ ] Wait for deployment
   - [ ] Test n8n access

4. **Database Storage Setup**
   - [ ] Create Render PostgreSQL database
   - [ ] Configure database connection
   - [ ] Update render.yaml with DB settings
   - [ ] Test database connection

5. **Cronjob Keep-Alive Setup**
   - [ ] Sign up for cronjob service
   - [ ] Configure ping URL
   - [ ] Set schedule (every 10 minutes)
   - [ ] Test keep-alive

6. **Custom Domain (Optional)**
   - [ ] Purchase domain name
   - [ ] Point DNS to Render
   - [ ] Configure custom domain
   - [ ] Test HTTPS access

#### **Expected Result:**
- n8n running on Render
- PostgreSQL database connected
- Accessible via HTTPS
- Cronjob keeping it awake
- Basic authentication enabled
- Persistent workflow storage
- Ready for workflow creation

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Self-Hosting n8n on Render" video
- [ ] Read Render platform documentation
- [ ] Create Render account
- [ ] Set up GitHub repository
- [ ] Deploy n8n on Render
- [ ] Set up PostgreSQL database
- [ ] Configure database connection
- [ ] Set up cronjob keep-alive
- [ ] Test n8n access
- [ ] Configure custom domain (optional)
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Have n8n running on Render
- PostgreSQL database connected
- Access n8n via your Render URL
- Understand Render platform basics
- Have cronjob keep-alive set up
- Know free hosting limitations
- Have automatic SSL certificate
- Have persistent workflow storage

---

## 💡 PRO TIPS

1. **Free Tier Limits:** Render sleeps after 15 minutes of inactivity
2. **Keep-Alive Essential:** Set up cronjob to ping every 10 minutes
3. **Database Storage:** Use Render PostgreSQL for persistent data
4. **Multiple Services:** Use UptimeRobot as backup keep-alive
5. **Custom Domain:** Easy to set up with automatic SSL
6. **Monitor Usage:** Watch Render dashboard for resource usage
7. **Backup Workflows:** Export workflows regularly
8. **Environment Variables:** Use Render's env vars for secrets
9. **Database Backups:** Render includes automated backups

---

## 🚀 TOMORROW PREVIEW

**Day 5:** We'll explore the n8n UI in detail, learn about workflow management, and start building more complex workflows. Get ready to master the interface! 🖥️

---

*Remember: Free hosting with cronjob keep-alive is perfect for beginners! Master this setup! 🚀*
