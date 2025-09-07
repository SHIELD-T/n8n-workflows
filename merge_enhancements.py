#!/usr/bin/env python3
"""
Merge enhanced metadata into original workflow files
"""

import json
import os
import shutil
from pathlib import Path

def merge_enhanced_workflows():
    """Merge enhanced metadata into original workflow files"""
    print("🔄 Merging enhanced metadata into original workflows...")
    
    enhanced_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('_enhanced.json'):
                enhanced_files.append(os.path.join(root, file))
    
    print(f"📊 Found {len(enhanced_files)} enhanced workflow files")
    
    merged_count = 0
    for enhanced_file in enhanced_files:
        try:
            # Read enhanced workflow
            with open(enhanced_file, 'r', encoding='utf-8') as f:
                enhanced = json.load(f)
            
            # Get original workflow path
            original_path = enhanced_file.replace('_enhanced.json', '.json')
            
            # Read original workflow
            with open(original_path, 'r', encoding='utf-8') as f:
                original = json.load(f)
            
            # Add metadata to original workflow
            enhanced_original = {
                "meta": {
                    "name": enhanced["name"],
                    "description": enhanced["description"],
                    "tags": enhanced["tags"],
                    "version": enhanced["version"],
                    "author": enhanced["author"],
                    "category": enhanced["category"],
                    "difficulty": enhanced["difficulty"],
                    "estimated_setup_time": enhanced["estimated_setup_time"],
                    "prerequisites": enhanced["prerequisites"],
                    "use_cases": enhanced["use_cases"],
                    "examples": enhanced["examples"],
                    "last_updated": "2024-12-19",
                    "workflow_id": os.path.basename(original_path).replace('.json', '')
                },
                "nodes": original.get("nodes", []),
                "connections": original.get("connections", {}),
                "active": original.get("active", False),
                "settings": original.get("settings", {}),
                "staticData": original.get("staticData", {}),
                "pinData": original.get("pinData", {}),
                "versionId": original.get("versionId", ""),
                "id": original.get("id", ""),
                "createdAt": original.get("createdAt", ""),
                "updatedAt": original.get("updatedAt", "")
            }
            
            # Write enhanced original workflow
            with open(original_path, 'w', encoding='utf-8') as f:
                json.dump(enhanced_original, f, indent=2, ensure_ascii=False)
            
            # Remove enhanced file
            os.remove(enhanced_file)
            merged_count += 1
            
            print(f"✅ Merged: {original_path}")
            
        except Exception as e:
            print(f"❌ Error merging {enhanced_file}: {e}")
    
    print(f"🎉 Successfully merged {merged_count} workflows!")
    return merged_count

def add_workflow_improvements():
    """Add additional improvements to workflows"""
    print("🔧 Adding workflow improvements...")
    
    improvements_added = 0
    
    # Find all workflow files
    workflow_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json') and 'workflow.json' in file:
                workflow_files.append(os.path.join(root, file))
    
    for workflow_file in workflow_files:
        try:
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow = json.load(f)
            
            # Add error handling to workflows
            if "nodes" in workflow:
                for node in workflow["nodes"]:
                    # Add error handling to HTTP Request nodes
                    if node.get("type") == "n8n-nodes-base.httpRequest":
                        if "continueOnFail" not in node.get("parameters", {}):
                            if "parameters" not in node:
                                node["parameters"] = {}
                            node["parameters"]["continueOnFail"] = True
                            improvements_added += 1
                    
                    # Add retry logic to critical nodes
                    if node.get("type") in ["n8n-nodes-base.httpRequest", "n8n-nodes-base.function"]:
                        if "retryOnFail" not in node:
                            node["retryOnFail"] = True
                            improvements_added += 1
            
            # Write improved workflow
            with open(workflow_file, 'w', encoding='utf-8') as f:
                json.dump(workflow, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"❌ Error improving {workflow_file}: {e}")
    
    print(f"🔧 Added {improvements_added} workflow improvements!")
    return improvements_added

def create_workflow_index():
    """Create a comprehensive workflow index"""
    print("📋 Creating comprehensive workflow index...")
    
    workflow_index = {
        "total_workflows": 0,
        "categories": {},
        "by_difficulty": {"Beginner": 0, "Intermediate": 0, "Advanced": 0},
        "by_tags": {},
        "recently_updated": [],
        "most_popular": []
    }
    
    # Find all workflow files
    workflow_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.json') and 'workflow.json' in file:
                workflow_files.append(os.path.join(root, file))
    
    for workflow_file in workflow_files:
        try:
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow = json.load(f)
            
            meta = workflow.get("meta", {})
            category = meta.get("category", "Unknown")
            difficulty = meta.get("difficulty", "Unknown")
            tags = meta.get("tags", [])
            
            # Update counts
            workflow_index["total_workflows"] += 1
            
            if category not in workflow_index["categories"]:
                workflow_index["categories"][category] = 0
            workflow_index["categories"][category] += 1
            
            if difficulty in workflow_index["by_difficulty"]:
                workflow_index["by_difficulty"][difficulty] += 1
            
            for tag in tags:
                if tag not in workflow_index["by_tags"]:
                    workflow_index["by_tags"][tag] = 0
                workflow_index["by_tags"][tag] += 1
            
        except Exception as e:
            print(f"❌ Error indexing {workflow_file}: {e}")
    
    # Sort tags by popularity
    workflow_index["by_tags"] = dict(sorted(workflow_index["by_tags"].items(), key=lambda x: x[1], reverse=True))
    
    # Write index
    with open('workflow_index.json', 'w', encoding='utf-8') as f:
        json.dump(workflow_index, f, indent=2, ensure_ascii=False)
    
    print("📋 Workflow index created successfully!")
    return workflow_index

def main():
    """Main function"""
    print("🚀 Starting workflow enhancement merge process...")
    
    # Merge enhanced workflows
    merged_count = merge_enhanced_workflows()
    
    # Add improvements
    improvements_count = add_workflow_improvements()
    
    # Create index
    index = create_workflow_index()
    
    print("\n🎉 Workflow Enhancement Complete!")
    print(f"✅ Merged {merged_count} enhanced workflows")
    print(f"🔧 Added {improvements_count} improvements")
    print(f"📋 Created workflow index with {index['total_workflows']} workflows")
    print(f"📊 Categories: {len(index['categories'])}")
    print(f"🏷️ Tags: {len(index['by_tags'])}")

if __name__ == "__main__":
    main()
