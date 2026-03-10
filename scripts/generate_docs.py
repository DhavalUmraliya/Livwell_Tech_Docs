import os
import json
import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract H1 title (e.g., # Authentication)
    title_match = re.search(r'^# (.*)', content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.basename(file_path).replace('.md', '').replace('_', ' ').capitalize()
    
    # Extract sections between H2s
    sections = re.split(r'^## (.*)', content, flags=re.MULTILINE)
    
    summary = ""
    tech_docs = ""
    code_block = ""
    lang = "javascript" # default
    
    # Process split sections (even indices are headers, odd indices are following text)
    for i in range(1, len(sections), 2):
        header = sections[i].lower()
        body = sections[i+1].strip()
        
        if "summary" in header:
            summary = body
        elif "details" in header or "tech" in header or "documentation" in header:
            tech_docs = body
        elif "implementation" in header or "example" in header:
            # Extract code block if it exists in implementation section
            code_match = re.search(r'```(\w+)?\n(.*?)\n```', body, re.DOTALL)
            if code_match:
                lang = code_match.group(1) if code_match.group(1) else "javascript"
                code_block = code_match.group(2)
            else:
                # If no code block, just take the text as tech docs
                tech_docs += "\n\n" + body
                
    # Fallback for summary if not found in H2
    if not summary:
        first_p = re.search(r'^[^#\n].*', content, re.MULTILINE)
        summary = first_p.group(0).strip() if first_p else ""

    return {
        "title": title,
        "summary": summary,
        "techDocs": tech_docs,
        "code": code_block,
        "lang": lang
    }

def generate():
    docs_root = 'docs'
    platforms = ['ios', 'android', 'web']
    result = {
        "ios": {"accent": "#007aff", "rgb": "0, 122, 255", "modules": []},
        "android": {"accent": "#3ddc84", "rgb": "61, 220, 132", "modules": []},
        "web": {"accent": "#a855f7", "rgb": "168, 85, 247", "modules": []}
    }

    for platform in platforms:
        platform_dir = os.path.join(docs_root, platform)
        if not os.path.exists(platform_dir):
            continue
            
        # Walk through subfolders (e.g., MonopolyDocs)
        for root, dirs, files in os.walk(platform_dir):
            category_name = os.path.basename(root)
            if category_name == platform:
                category_name = "Core Modules"
            else:
                category_name = category_name.replace('_', ' ').replace('-', ' ').title()
                
            for file in sorted(files):
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    module_data = parse_markdown(file_path)
                    
                    # Add ID and Category
                    module_data["id"] = file.replace('.md', '').lower().replace(' ', '-')
                    module_data["category"] = category_name
                    
                    result[platform]["modules"].append(module_data)

    # Wrap in JavaScript variable for easy loading in index.html
    js_content = f"const dynamicContent = {json.dumps(result, indent=4)};"
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("Documentation updated successfully in data.js")

if __name__ == "__main__":
    generate()
