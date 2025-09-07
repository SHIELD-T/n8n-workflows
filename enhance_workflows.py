#!/usr/bin/env python3
"""
n8n Workflow Enhancement Script
Adds metadata, tags, descriptions, and examples to n8n workflows
"""

import json
import os
import re
from pathlib import Path

def enhance_workflow(workflow_path):
    """Enhance a single workflow file with metadata"""
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = json.load(f)
        
        # Extract workflow info
        workflow_name = os.path.basename(workflow_path).replace('.json', '')
        category = os.path.basename(os.path.dirname(workflow_path))
        
        # Create enhanced metadata
        enhanced_workflow = {
            "name": workflow_name.replace('-', ' ').replace('_', ' ').title(),
            "description": generate_description(workflow_name, category),
            "tags": generate_tags(workflow_name, category),
            "version": "1.0.0",
            "author": "sagebeme",
            "category": category,
            "difficulty": determine_difficulty(workflow),
            "estimated_setup_time": estimate_setup_time(workflow),
            "prerequisites": generate_prerequisites(workflow),
            "use_cases": generate_use_cases(workflow_name, category),
            "examples": generate_examples(workflow_name, category),
            "workflow": workflow
        }
        
        return enhanced_workflow
        
    except Exception as e:
        print(f"Error enhancing {workflow_path}: {e}")
        return None

def generate_description(workflow_name, category):
    """Generate a description based on workflow name and category"""
    descriptions = {
        "github-repos-monitoring": "Monitor multiple GitHub repositories simultaneously using webhooks for real-time updates on commits, issues, and pull requests.",
        "instagram-stats-to-mattermost": "Automatically send Instagram analytics and statistics to Mattermost channels for team visibility.",
        "markdown-report-generator": "Generate comprehensive markdown reports from various data sources with automated formatting.",
        "ai-customer-feedback-sentiment": "Analyze customer feedback using AI to determine sentiment and categorize responses automatically.",
        "redis-rate-limiting-api": "Implement API rate limiting using Redis to control request frequency and prevent abuse.",
        "twitter-webhook-verification": "Verify and process Twitter webhook events securely with proper signature validation.",
        "strapi-testimonials-automation": "Automate testimonial collection and management in Strapi CMS with approval workflows.",
        "adobe-e-signature-webhooks": "Handle Adobe Acrobat e-signature events through webhooks for document workflow automation.",
        "custom-api-endpoint": "Create custom API endpoints for external integrations with proper authentication and validation.",
        "graphql-api-queries": "Execute GraphQL queries against various APIs with dynamic query building and response processing."
    }
    
    return descriptions.get(workflow_name, f"Automated workflow for {category.replace('-', ' ')} operations with intelligent processing and error handling.")

def generate_tags(workflow_name, category):
    """Generate relevant tags for the workflow"""
    base_tags = {
        "01-AI-Research-RAG-Data-Analysis": ["ai", "research", "rag", "data-analysis", "machine-learning"],
        "02-Airtable-Integration": ["airtable", "database", "crm", "project-management"],
        "03-Analytics-Reporting": ["analytics", "reporting", "data-visualization", "metrics"],
        "04-API-Webhooks": ["api", "webhooks", "integration", "automation"],
        "05-Automation-Workflows": ["automation", "productivity", "workflow", "efficiency"],
        "06-Communication-Tools": ["communication", "messaging", "notifications", "team-collaboration"],
        "07-Data-Integration": ["data-integration", "etl", "data-sync", "databases"],
        "08-Data-Transformation": ["data-transformation", "format-conversion", "data-processing"],
        "09-Database-Storage": ["database", "storage", "sql", "data-management"],
        "10-Discord-Integration": ["discord", "bot", "gaming", "community"],
        "11-Document-Processing": ["documents", "pdf", "text-processing", "file-management"],
        "12-Forms-Surveys": ["forms", "surveys", "data-collection", "feedback"],
        "13-Email-Automation": ["email", "automation", "marketing", "communication"],
        "14-Google-Workspace": ["google", "workspace", "gmail", "drive", "sheets"],
        "15-HR-Recruitment": ["hr", "recruitment", "hiring", "human-resources"],
        "16-Social-Media": ["social-media", "instagram", "twitter", "marketing"],
        "17-Notion-Integration": ["notion", "productivity", "documentation", "knowledge-management"],
        "18-AI-LLM-Integration": ["ai", "llm", "openai", "chatgpt", "machine-learning"],
        "19-Other-Tools": ["utilities", "tools", "miscellaneous"],
        "20-Additional-Integrations": ["integrations", "third-party", "apis", "automation"],
        "21-PDF-Document-Processing": ["pdf", "documents", "text-extraction", "file-processing"],
        "22-Slack-Integration": ["slack", "team-communication", "notifications", "collaboration"],
        "23-Telegram-Integration": ["telegram", "bot", "messaging", "automation"],
        "24-WhatsApp-Integration": ["whatsapp", "messaging", "business", "communication"],
        "25-WordPress-Integration": ["wordpress", "cms", "website", "content-management"]
    }
    
    tags = base_tags.get(category, ["automation", "workflow"])
    
    # Add specific tags based on workflow name
    if "github" in workflow_name.lower():
        tags.extend(["github", "version-control", "development"])
    if "ai" in workflow_name.lower() or "sentiment" in workflow_name.lower():
        tags.extend(["artificial-intelligence", "nlp", "machine-learning"])
    if "webhook" in workflow_name.lower():
        tags.extend(["webhooks", "real-time", "events"])
    if "api" in workflow_name.lower():
        tags.extend(["api", "integration", "rest"])
    if "email" in workflow_name.lower():
        tags.extend(["email", "communication", "notifications"])
    
    return list(set(tags))  # Remove duplicates

def determine_difficulty(workflow):
    """Determine workflow difficulty based on complexity"""
    node_count = len(workflow.get('nodes', []))
    
    if node_count <= 5:
        return "Beginner"
    elif node_count <= 15:
        return "Intermediate"
    else:
        return "Advanced"

def estimate_setup_time(workflow):
    """Estimate setup time based on workflow complexity"""
    node_count = len(workflow.get('nodes', []))
    
    if node_count <= 5:
        return "5-10 minutes"
    elif node_count <= 15:
        return "15-30 minutes"
    else:
        return "30-60 minutes"

def generate_prerequisites(workflow):
    """Generate prerequisites based on workflow nodes"""
    prerequisites = []
    nodes = workflow.get('nodes', [])
    
    for node in nodes:
        node_type = node.get('type', '')
        
        if 'github' in node_type.lower():
            prerequisites.append("GitHub account and API access")
        elif 'openai' in node_type.lower() or 'chatgpt' in node_type.lower():
            prerequisites.append("OpenAI API key")
        elif 'slack' in node_type.lower():
            prerequisites.append("Slack workspace and bot token")
        elif 'discord' in node_type.lower():
            prerequisites.append("Discord bot token")
        elif 'telegram' in node_type.lower():
            prerequisites.append("Telegram bot token")
        elif 'airtable' in node_type.lower():
            prerequisites.append("Airtable account and API key")
        elif 'notion' in node_type.lower():
            prerequisites.append("Notion account and integration token")
        elif 'google' in node_type.lower():
            prerequisites.append("Google account and API credentials")
        elif 'webhook' in node_type.lower():
            prerequisites.append("Webhook endpoint URL")
    
    return list(set(prerequisites)) if prerequisites else ["n8n instance", "Basic n8n knowledge"]

def generate_use_cases(workflow_name, category):
    """Generate use cases based on workflow purpose"""
    use_cases = {
        "github-repos-monitoring": [
            "Monitor multiple repositories for security updates",
            "Track development progress across teams",
            "Get notified of critical issues and pull requests",
            "Automate deployment triggers based on repository events"
        ],
        "instagram-stats-to-mattermost": [
            "Share social media performance with marketing team",
            "Monitor brand engagement metrics",
            "Track influencer campaign results",
            "Automate social media reporting"
        ],
        "ai-customer-feedback-sentiment": [
            "Automatically categorize customer support tickets",
            "Monitor brand sentiment across channels",
            "Prioritize urgent customer issues",
            "Generate sentiment reports for management"
        ]
    }
    
    return use_cases.get(workflow_name, [
        f"Automate {category.replace('-', ' ')} processes",
        "Improve operational efficiency",
        "Reduce manual work and errors",
        "Enable real-time data processing"
    ])

def generate_examples(workflow_name, category):
    """Generate usage examples"""
    examples = {
        "github-repos-monitoring": [
            "Monitor 10+ repositories for security vulnerabilities",
            "Get Slack notifications for critical issues",
            "Automate deployment when main branch is updated"
        ],
        "instagram-stats-to-mattermost": [
            "Daily Instagram metrics to marketing channel",
            "Weekly engagement reports for stakeholders",
            "Real-time follower growth notifications"
        ]
    }
    
    return examples.get(workflow_name, [
        f"Use this workflow to automate {category.replace('-', ' ')} tasks",
        "Integrate with your existing tools and processes",
        "Customize parameters for your specific needs"
    ])

def main():
    """Main function to enhance all workflows"""
    print("🚀 Starting n8n Workflow Enhancement...")
    
    # Find all JSON workflow files
    workflow_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json') and 'workflow.json' in file:
                workflow_files.append(os.path.join(root, file))
    
    print(f"📊 Found {len(workflow_files)} workflow files to enhance")
    
    enhanced_count = 0
    for workflow_file in workflow_files:
        print(f"🔧 Enhancing: {workflow_file}")
        enhanced = enhance_workflow(workflow_file)
        if enhanced:
            enhanced_count += 1
            # Save enhanced workflow
            output_path = workflow_file.replace('.json', '_enhanced.json')
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(enhanced, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Enhanced {enhanced_count} workflows successfully!")
    print("📁 Enhanced workflows saved with '_enhanced.json' suffix")

if __name__ == "__main__":
    main()
