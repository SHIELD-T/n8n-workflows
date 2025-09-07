# 📅 DAY 9: TUESDAY - Self-Hosting Setup

## 🎯 TODAY'S OBJECTIVES
- Master self-hosting n8n with Docker
- Learn VPS management and configuration
- Set up SSL certificates and security
- Deploy production-ready n8n instance

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
- Docker containerization basics
- n8n Docker deployment
- VPS configuration and management
- SSL certificate setup

#### **Key Concepts:**
- **Docker Compose:** Multi-container management
- **SSL/TLS:** Secure communication
- **Reverse Proxy:** Nginx configuration
- **Backup Strategy:** Data protection

#### **Take Notes On:**
- Docker Compose configuration
- SSL certificate generation
- Nginx reverse proxy setup
- Backup and restore procedures

---

### **📖 Reading Assignment**
**Duration:** 15 minutes

#### **Read: "Production n8n Deployment Guide"**
- Security best practices
- Performance optimization
- Monitoring and logging
- Maintenance procedures

#### **Key Takeaways:**
- Security is crucial for production
- Monitoring helps prevent issues
- Regular backups are essential
- Maintenance keeps systems running

---

## 🌞 AFTERNOON SESSION (1 hour)

### **🛠️ Hands-on Practice: "Production Deployment"**
**Duration:** 30 minutes

#### **Task: Deploy Production n8n Instance**

**Step-by-Step Instructions:**

1. **Server Preparation**
   - Update Ubuntu system
   - Install Docker and Docker Compose
   - Configure firewall rules
   - Set up SSH key authentication

2. **Domain and SSL Setup**
   - Configure DNS records
   - Install Certbot for SSL
   - Generate SSL certificates
   - Set up automatic renewal

3. **Nginx Configuration**
   - Install Nginx
   - Configure reverse proxy
   - Set up SSL termination
   - Test configuration

---

### **🐳 Docker Compose Setup**
**Duration:** 30 minutes

#### **Task: Create Production Docker Compose**

**Create docker-compose.yml:**
```yaml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=secure_password
      - WEBHOOK_URL=https://your-domain.com
      - GENERIC_TIMEZONE=UTC
      - N8N_LOG_LEVEL=info
    volumes:
      - n8n_data:/home/node/.n8n
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - n8n_network

  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - /etc/letsencrypt:/etc/letsencrypt
    depends_on:
      - n8n
    networks:
      - n8n_network

volumes:
  n8n_data:

networks:
  n8n_network:
    driver: bridge
```

---

## 🌙 EVENING SESSION (30 minutes)

### **📸 Share Your Production Setup**
**Duration:** 20 minutes

#### **Community Post: "My Production n8n Deployment"**

**Share:**
- Screenshot of your n8n instance
- Your deployment configuration
- Any challenges faced
- Questions for the community

#### **Post Template:**
```
Day 9 Complete! 🎉

**Production Setup:**
[Screenshot of n8n interface]

**My Configuration:**
- VPS: [Your provider]
- Domain: [Your domain]
- SSL: ✅ Enabled
- Docker: ✅ Running
- Nginx: ✅ Configured

**Challenges:**
- [Any issues you faced]

**Questions:**
- [Any questions for the community]

Ready for Day 10! 🚀
```

---

### **📋 Review Tomorrow's Materials**
**Duration:** 10 minutes

#### **Preview Day 10:**
- n8n UI deep dive and exploration
- Workflow management techniques
- Execution monitoring and debugging
- Performance optimization

#### **Prepare:**
- Access your production n8n
- Create test workflows
- Review UI elements

---

## 📝 DAILY TASK

### **🎯 Main Task: Deploy Production n8n Instance**

**Successfully deploy n8n on VPS with SSL and reverse proxy.**

#### **Complete Setup Checklist:**

1. **VPS Configuration**
   - [ ] Launch Ubuntu 20.04+ server
   - [ ] Update system packages
   - [ ] Configure firewall (ports 22, 80, 443)
   - [ ] Set up SSH key authentication

2. **Docker Installation**
   - [ ] Install Docker and Docker Compose
   - [ ] Add user to docker group
   - [ ] Test Docker installation

3. **Domain Setup**
   - [ ] Purchase domain name
   - [ ] Point DNS to VPS IP
   - [ ] Wait for DNS propagation

4. **SSL Certificate**
   - [ ] Install Certbot
   - [ ] Generate SSL certificate
   - [ ] Set up automatic renewal

5. **Nginx Configuration**
   - [ ] Install Nginx
   - [ ] Configure reverse proxy
   - [ ] Test SSL configuration

6. **n8n Deployment**
   - [ ] Create docker-compose.yml
   - [ ] Start n8n container
   - [ ] Test n8n access via domain
   - [ ] Configure basic authentication

#### **Expected Result:**
- n8n accessible via HTTPS
- SSL certificate valid
- Reverse proxy working
- Basic authentication enabled
- Production-ready deployment

---

## ✅ DAILY CHECKLIST

- [ ] Watch "Self-Hosting n8n with Docker" video
- [ ] Read production deployment guide
- [ ] Configure VPS server
- [ ] Install Docker and Docker Compose
- [ ] Set up domain and DNS
- [ ] Generate SSL certificate
- [ ] Configure Nginx reverse proxy
- [ ] Deploy n8n with Docker Compose
- [ ] Test production deployment
- [ ] Share progress in community
- [ ] Review tomorrow's materials
- [ ] Complete daily task

---

## 🎯 SUCCESS METRICS

**By the end of today, you should:**
- Have production n8n running
- Understand Docker deployment
- Know SSL certificate setup
- Have reverse proxy configured
- Be ready for advanced UI work

---

## 💡 PRO TIPS

1. **Security First:** Always use SSL in production
2. **Backup Early:** Set up backups from day one
3. **Monitor Resources:** Watch CPU and memory usage
4. **Update Regularly:** Keep system and Docker updated
5. **Document Everything:** Keep notes on your setup

---

## 🚀 TOMORROW PREVIEW

**Day 10:** We'll explore the n8n UI in detail, learn about workflow management, and start building more sophisticated workflows. Get ready to master the interface! 🖥️

---

*Remember: Production deployment is a milestone! You're building real infrastructure! 🚀*
