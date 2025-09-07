#!/usr/bin/env python3
"""
Course Workflow Enhancement Script
Enhances n8n workflows for the Automator Pro course with proper metadata
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime

def enhance_course_workflows():
    """Enhance all course workflow files with proper metadata"""
    print("🚀 Starting Course Workflow Enhancement...")
    
    # Find all JSON workflow files in course structure
    workflow_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json') and 'WEEK_' in root:
                workflow_files.append(os.path.join(root, file))
    
    print(f"📊 Found {len(workflow_files)} course workflow files to enhance")
    
    enhanced_count = 0
    for workflow_file in workflow_files:
        print(f"🔧 Enhancing: {workflow_file}")
        enhanced = enhance_single_workflow(workflow_file)
        if enhanced:
            enhanced_count += 1
            # Save enhanced workflow
            with open(workflow_file, 'w', encoding='utf-8') as f:
                json.dump(enhanced, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Enhanced {enhanced_count} workflows successfully!")
    return enhanced_count

def enhance_single_workflow(workflow_path):
    """Enhance a single workflow file with course-specific metadata"""
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = json.load(f)
        
        # Extract course context
        week_info = extract_week_info(workflow_path)
        workflow_name = os.path.basename(workflow_path).replace('.json', '')
        
        # Create enhanced workflow with course metadata
        enhanced_workflow = {
            "name": workflow.get("name", format_workflow_name(workflow_name)),
            "description": generate_course_description(workflow_name, week_info),
            "tags": generate_course_tags(workflow_name, week_info),
            "version": "1.0.0",
            "author": "Automator Pro Course",
            "course_metadata": {
                "week": week_info["week"],
                "phase": week_info["phase"],
                "difficulty": determine_course_difficulty(week_info["week"]),
                "learning_objectives": get_learning_objectives(week_info["week"]),
                "prerequisites": get_course_prerequisites(week_info["week"]),
                "estimated_setup_time": estimate_course_setup_time(workflow),
                "use_cases": generate_course_use_cases(workflow_name, week_info),
                "examples": generate_course_examples(workflow_name, week_info),
                "next_steps": get_next_steps(week_info["week"]),
                "related_workflows": get_related_workflows(week_info["week"])
            },
            "meta": {
                "templateCredsSetupCompleted": True,
                "instanceId": f"course-{week_info['week']}-{workflow_name}",
                "course_version": "1.0",
                "last_updated": datetime.now().isoformat()
            },
            "nodes": workflow.get("nodes", []),
            "connections": workflow.get("connections", {}),
            "active": workflow.get("active", False),
            "settings": workflow.get("settings", {}),
            "pinData": workflow.get("pinData", {}),
            "versionId": workflow.get("versionId", "1"),
            "id": workflow.get("id", workflow_name)
        }
        
        return enhanced_workflow
        
    except Exception as e:
        print(f"Error enhancing {workflow_path}: {e}")
        return None

def extract_week_info(workflow_path):
    """Extract week and phase information from file path"""
    path_parts = workflow_path.split('/')
    
    # Find week directory
    week_dir = None
    for part in path_parts:
        if part.startswith('WEEK_'):
            week_dir = part
            break
    
    if not week_dir:
        return {"week": "Unknown", "phase": "Unknown"}
    
    # Extract week number
    week_num = week_dir.split('_')[1]
    
    # Determine phase based on week
    phases = {
        "01": "Foundation", "02": "Foundation",
        "03": "Workflow Building", "04": "Workflow Building", "05": "Workflow Building",
        "06": "AI Integration", "07": "AI Integration", "08": "AI Integration",
        "09": "Real-World Tools", "10": "Real-World Tools",
        "11": "Client Acquisition", "12": "Scaling",
        "13": "Advanced Business", "14": "Final Optimization", "15": "Graduation"
    }
    
    return {
        "week": f"Week {week_num}",
        "phase": phases.get(week_num, "Unknown")
    }

def format_workflow_name(name):
    """Format workflow name for display"""
    return name.replace('_', ' ').replace('-', ' ').title()

def generate_course_description(workflow_name, week_info):
    """Generate course-specific description"""
    descriptions = {
        "foundation_learning_progress_tracker": "Track learning progress throughout the foundation phase with automated progress monitoring and milestone celebrations.",
        "advanced_foundation_skills_assessment": "Assess and validate foundation skills with automated skill evaluation and progress tracking.",
        "workflow_performance_monitoring_system": "Monitor workflow performance with real-time metrics, error tracking, and optimization recommendations.",
        "advanced_workflow_optimization_engine": "Optimize workflow performance with automated analysis, bottleneck detection, and improvement suggestions.",
        "workflow_scaling_management_system": "Manage workflow scaling with automated resource allocation and performance monitoring.",
        "ai_agent_performance_monitor": "Monitor AI agent performance with metrics tracking, quality assessment, and optimization insights.",
        "ai_agent_learning_system": "Enable AI agent learning with automated training, feedback loops, and continuous improvement.",
        "ai_agent_quality_assurance_system": "Ensure AI agent quality with automated testing, validation, and quality metrics.",
        "real_tools_integration_monitor": "Monitor real-world tool integrations with automated health checks and performance tracking.",
        "advanced_real_tools_automation": "Automate complex real-world tool workflows with advanced integration patterns.",
        "client_acquisition_tracking_system": "Track client acquisition with automated lead management and conversion monitoring.",
        "scaling_operations_management": "Manage scaling operations with automated resource allocation and performance optimization.",
        "advanced_business_strategy_system": "Implement advanced business strategies with automated analysis and decision support.",
        "final_optimization_management_system": "Manage final optimization with comprehensive performance analysis and improvement recommendations.",
        "graduation_achievement_celebration_system": "Celebrate graduation achievements with automated milestone tracking and celebration workflows."
    }
    
    return descriptions.get(workflow_name, f"Automated workflow for {week_info['phase']} phase learning objectives with intelligent processing and error handling.")

def generate_course_tags(workflow_name, week_info):
    """Generate course-specific tags"""
    base_tags = {
        "Foundation": ["foundation", "basics", "learning", "progress-tracking"],
        "Workflow Building": ["workflows", "automation", "optimization", "performance"],
        "AI Integration": ["ai", "agents", "machine-learning", "intelligence"],
        "Real-World Tools": ["integration", "tools", "apis", "real-world"],
        "Client Acquisition": ["business", "clients", "acquisition", "marketing"],
        "Scaling": ["scaling", "growth", "operations", "management"],
        "Advanced Business": ["strategy", "advanced", "business", "optimization"],
        "Final Optimization": ["optimization", "final", "performance", "efficiency"],
        "Graduation": ["graduation", "celebration", "achievement", "completion"]
    }
    
    tags = base_tags.get(week_info["phase"], ["automation", "workflow"])
    
    # Add specific tags based on workflow name
    if "ai" in workflow_name.lower():
        tags.extend(["artificial-intelligence", "machine-learning", "automation"])
    if "monitor" in workflow_name.lower():
        tags.extend(["monitoring", "analytics", "tracking"])
    if "optimization" in workflow_name.lower():
        tags.extend(["optimization", "performance", "efficiency"])
    if "business" in workflow_name.lower():
        tags.extend(["business", "strategy", "management"])
    if "graduation" in workflow_name.lower():
        tags.extend(["graduation", "celebration", "achievement"])
    
    return list(set(tags))  # Remove duplicates

def determine_course_difficulty(week):
    """Determine difficulty based on course week"""
    week_num = int(week.split()[1])
    
    if week_num <= 2:
        return "Beginner"
    elif week_num <= 8:
        return "Intermediate"
    else:
        return "Advanced"

def get_learning_objectives(week):
    """Get learning objectives for specific week"""
    objectives = {
        "Week 01": ["Understand automation basics", "Learn n8n interface", "Build first workflows"],
        "Week 02": ["Master self-hosting", "Understand webhooks", "Work with APIs"],
        "Week 03": ["Advanced nodes usage", "Expression writing", "Error handling"],
        "Week 04": ["Data processing", "Workflow optimization", "Documentation"],
        "Week 05": ["Production deployment", "Monitoring", "Maintenance"],
        "Week 06": ["AI agent basics", "ChatGPT integration", "LLM providers"],
        "Week 07": ["Advanced AI patterns", "AI optimization", "Intelligent systems"],
        "Week 08": ["AI deployment", "AI maintenance", "AI scaling"],
        "Week 09": ["OAuth integration", "Form builders", "Email/calendar triggers"],
        "Week 10": ["Advanced integrations", "Custom APIs", "Orchestration"],
        "Week 11": ["Client acquisition", "Service packaging", "Portfolio building"],
        "Week 12": ["Scaling strategies", "Template creation", "Team building"],
        "Week 13": ["Advanced strategies", "Partnerships", "Brand building"],
        "Week 14": ["Final optimization", "Exit strategies", "Legacy building"],
        "Week 15": ["Graduation preparation", "Ongoing success", "Celebration"]
    }
    
    return objectives.get(week, ["Complete course objectives", "Build automation skills", "Prepare for business"])

def get_course_prerequisites(week):
    """Get prerequisites for specific week"""
    week_num = int(week.split()[1])
    
    if week_num == 1:
        return ["Basic computer skills", "Internet access", "Willingness to learn"]
    elif week_num <= 5:
        return ["Completed previous weeks", "n8n instance", "Basic automation knowledge"]
    elif week_num <= 8:
        return ["Workflow building skills", "AI/ML interest", "API knowledge"]
    elif week_num <= 10:
        return ["AI integration skills", "Real-world tool access", "Integration experience"]
    elif week_num <= 12:
        return ["Technical skills", "Business interest", "Client interaction skills"]
    else:
        return ["Complete course foundation", "Business experience", "Strategic thinking"]

def estimate_course_setup_time(workflow):
    """Estimate setup time based on workflow complexity"""
    node_count = len(workflow.get('nodes', []))
    
    if node_count <= 5:
        return "5-10 minutes"
    elif node_count <= 10:
        return "10-20 minutes"
    else:
        return "20-30 minutes"

def generate_course_use_cases(workflow_name, week_info):
    """Generate course-specific use cases"""
    return [
        f"Practice {week_info['phase']} concepts",
        "Build real-world automation skills",
        "Prepare for business applications",
        "Demonstrate course learning objectives"
    ]

def generate_course_examples(workflow_name, week_info):
    """Generate course-specific examples"""
    return [
        f"Use this workflow to practice {week_info['phase']} skills",
        "Customize for your specific learning needs",
        "Apply concepts to real business scenarios",
        "Build upon for advanced implementations"
    ]

def get_next_steps(week):
    """Get next steps for specific week"""
    week_num = int(week.split()[1])
    
    if week_num < 15:
        return [f"Complete Week {week_num + 1} objectives", "Practice with additional examples", "Apply skills to real projects"]
    else:
        return ["Launch your automation business", "Continue learning and growing", "Share your success with the community"]

def get_related_workflows(week):
    """Get related workflows for specific week"""
    week_num = int(week.split()[1])
    
    if week_num < 15:
        return [f"Week {week_num + 1} workflows", "Previous week workflows", "Course example workflows"]
    else:
        return ["All course workflows", "Graduation projects", "Business implementation workflows"]

def create_course_workflow_index():
    """Create comprehensive course workflow index"""
    print("📋 Creating course workflow index...")
    
    workflow_index = {
        "course_info": {
            "name": "Automator Pro: Master n8n + AI to Build Your Own Automation Business",
            "total_weeks": 15,
            "total_workflows": 0,
            "last_updated": datetime.now().isoformat()
        },
        "phases": {
            "Foundation": {"weeks": ["01", "02"], "workflows": 0},
            "Workflow Building": {"weeks": ["03", "04", "05"], "workflows": 0},
            "AI Integration": {"weeks": ["06", "07", "08"], "workflows": 0},
            "Real-World Tools": {"weeks": ["09", "10"], "workflows": 0},
            "Client Acquisition": {"weeks": ["11"], "workflows": 0},
            "Scaling": {"weeks": ["12"], "workflows": 0},
            "Advanced Business": {"weeks": ["13"], "workflows": 0},
            "Final Optimization": {"weeks": ["14"], "workflows": 0},
            "Graduation": {"weeks": ["15"], "workflows": 0}
        },
        "by_difficulty": {"Beginner": 0, "Intermediate": 0, "Advanced": 0},
        "by_tags": {},
        "workflows": []
    }
    
    # Find all workflow files
    workflow_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json') and 'WEEK_' in root:
                workflow_files.append(os.path.join(root, file))
    
    for workflow_file in workflow_files:
        try:
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow = json.load(f)
            
            course_meta = workflow.get("course_metadata", {})
            week = course_meta.get("week", "Unknown")
            phase = course_meta.get("phase", "Unknown")
            difficulty = course_meta.get("difficulty", "Unknown")
            tags = workflow.get("tags", [])
            
            # Update counts
            workflow_index["course_info"]["total_workflows"] += 1
            
            if phase in workflow_index["phases"]:
                workflow_index["phases"][phase]["workflows"] += 1
            
            if difficulty in workflow_index["by_difficulty"]:
                workflow_index["by_difficulty"][difficulty] += 1
            
            for tag in tags:
                if tag not in workflow_index["by_tags"]:
                    workflow_index["by_tags"][tag] = 0
                workflow_index["by_tags"][tag] += 1
            
            # Add workflow info
            workflow_index["workflows"].append({
                "name": workflow.get("name", ""),
                "week": week,
                "phase": phase,
                "difficulty": difficulty,
                "file_path": workflow_file,
                "tags": tags
            })
            
        except Exception as e:
            print(f"❌ Error indexing {workflow_file}: {e}")
    
    # Sort tags by popularity
    workflow_index["by_tags"] = dict(sorted(workflow_index["by_tags"].items(), key=lambda x: x[1], reverse=True))
    
    # Write index
    with open('course_workflow_index.json', 'w', encoding='utf-8') as f:
        json.dump(workflow_index, f, indent=2, ensure_ascii=False)
    
    print("📋 Course workflow index created successfully!")
    return workflow_index

def main():
    """Main function"""
    print("🚀 Starting Course Workflow Enhancement...")
    
    # Enhance all course workflows
    enhanced_count = enhance_course_workflows()
    
    # Create course index
    index = create_course_workflow_index()
    
    print("\n🎉 Course Workflow Enhancement Complete!")
    print(f"✅ Enhanced {enhanced_count} course workflows")
    print(f"📋 Created course index with {index['course_info']['total_workflows']} workflows")
    print(f"📊 Phases: {len(index['phases'])}")
    print(f"🏷️ Tags: {len(index['by_tags'])}")
    print(f"📚 Course: {index['course_info']['name']}")

if __name__ == "__main__":
    main()
