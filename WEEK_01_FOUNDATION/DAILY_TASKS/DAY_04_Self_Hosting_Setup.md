# 📅 DAY 4: THURSDAY - Self-Hosting Setup

## 🎯 TODAY'S OBJECTIVES
- Learn about self-hosting n8n with Docker
- Set up VPS account and domain
- Deploy n8n instance
- Configure SSL and security

## ⏰ TIME ALLOCATION
**Total Time:** 2-3 hours
- **Morning:** 1 hour (Learning)
- **Afternoon:** 1 hour (Hands-on Practice)
- **Evening:** 30 minutes (Community & Review)

---

## 🌅 MORNING SESSION (1 hour)

### **📹 Video Lesson: "Self-Hosting n8n with Docker"**
**Duration:** 45 minutes

#### **What You'll Learn:**
- Docker basics and containerization
- n8n Docker setup
- VPS selection and configuration
- Domain and SSL setup

#### **Key Concepts:**
- **Docker:** Containerization platform
- **VPS:** Virtual Private Server
- **SSL:** Secure Socket Layer
- **Domain:** Your n8n URL

#### **Take Notes On:**
- Docker installation steps
- n8n Docker configuration
- VPS requirements
- SSL certificate setup

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "Docker Basics for Beginners"**
- What is Docker
- Container vs Virtual Machine
- Docker commands
- Docker Compose

#### **Key Takeaways:**
- Docker makes deployment easier
- Containers are lightweight
- Docker Compose manages multiple containers
- n8n runs well in Docker

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Setting Up VPS and Domain"**
**Duration:** 30 minutes

#### **Task: Prepare Your Infrastructure**

**Step-by-Step Instructions:**

1. **Choose VPS Provider**
   - DigitalOcean, Hetzner, or AWS
   - Select Ubuntu 20.04+ server
   - Minimum 2GB RAM, 1 CPU
   - Create account and server

2. **Set Up Domain**
   - Purchase domain name
   - Point DNS to VPS IP
   - Wait for DNS propagation

3. **Connect to Server**
   - Use SSH to connect
   - Update system packages
   - Install Docker

---

### **🐳 Install Docker and n8n**
**Duration:** 30 minutes

#### **Task: Deploy n8n with Docker**

**Commands to Run:**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Create n8n directory
mkdir ~/n8n && cd ~/n8n

# Create docker-compose.yml
cat > docker-compose.yml << EOF
version: '3.8'
services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=your_password
      - WEBHOOK_URL=https://your-domain.com
    volumes:
      - n8n_data:/home/node/.n8n
volumes:
  n8n_data:
EOF

# Start n8n
docker-compose up -d
```

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
- VPS Provider: [Your provider]
- Domain: [Your domain]
- Docker: ✅ Installed
- n8n: ✅ Running

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

### **🎯 Main Task: Deploy n8n on VPS**

**Successfully deploy n8n on your VPS and access it via domain.**

#### **Step-by-Step Checklist:**

1. **VPS Setup**
   - [ ] Create VPS account
   - [ ] Launch Ubuntu server
   - [ ] Connect via SSH
   - [ ] Update system packages

2. **Docker Installation**
   - [ ] Install Docker
   - [ ] Add user to docker group
   - [ ] Test Docker installation

3. **Domain Setup**
   - [ ] Purchase domain name
   - [ ] Point DNS to VPS IP
   - [ ] Wait for DNS propagation

4. **n8n Deployment**
   - [ ] Create n8n directory
   - [ ] Create docker-compose.yml
   - [ ] Start n8n container
   - [ ] Access n8n via domain

5. **SSL Setup (Optional)**
   - [ ] Install Certbot
   - [ ] Generate SSL certificate
   - [ ] Configure HTTPS

#### **Expected Result:**
- n8n running on your domain
- Accessible via HTTPS
- Basic authentication enabled
- Ready for workflow creation

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Self-Hosting n8n with Docker" video
- [ ] Read Docker basics documentation
- [ ] Set up VPS account
- [ ] Purchase domain name
- [ ] Install Docker on VPS
- [ ] Deploy n8n with Docker
- [ ] Configure SSL certificate
- [ ] Test n8n access
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Have n8n running on your VPS
- Access n8n via your domain
- Understand Docker basics
- Know VPS management
- Have SSL certificate (optional)

---

## 💡 PRO TIPS

1. **Start Small:** Use a basic VPS first
2. **Secure Access:** Use SSH keys, not passwords
3. **Backup Data:** Set up regular backups
4. **Monitor Resources:** Watch CPU and memory usage
5. **Update Regularly:** Keep system and Docker updated

---

## 🚀 TOMORROW PREVIEW

**Day 5:** We'll explore the n8n UI in detail, learn about workflow management, and start building more complex workflows. Get ready to master the interface! 🖥️

---

*Remember: Self-hosting gives you full control! Master this setup! 🚀*
