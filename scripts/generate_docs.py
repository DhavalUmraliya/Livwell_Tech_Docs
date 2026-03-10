import os
import json
import re
import subprocess

def get_git_metadata(file_path):
    try:
        # Get last commit author and date
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%an|%ad', '--date=format:%b %d, %Y', file_path],
            capture_output=True, text=True, check=True
        )
        if result.stdout:
            author, date = result.stdout.strip().split('|')
            return author, date
    except Exception:
        pass
    return "Unknown", "Recent"

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    author, last_updated = get_git_metadata(file_path)
    
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
    processed_headers = []
    for i in range(1, len(sections), 2):
        header = sections[i].lower()
        body = sections[i+1].strip()
        processed_headers.append(header)
        
        if "summary" in header:
            summary = body
        elif any(kw in header for kw in ["details", "tech", "documentation", "feature", "flow", "rule", "management", "architecture", "state"]):
            tech_docs += f"\n\n### {sections[i]}\n{body}"
        elif any(kw in header for kw in ["implementation", "example", "code"]):
            # Extract code blocks
            code_blocks = re.findall(r'```(\w+)?\n(.*?)\n```', body, re.DOTALL)
            if code_blocks:
                for match in code_blocks:
                    lang = match[0] if match[0] else "javascript"
                    code_block += match[1] + "\n\n"
            else:
                tech_docs += f"\n\n### {sections[i]}\n{body}"
        else:
            # Catch all other sections as tech docs
            tech_docs += f"\n\n### {sections[i]}\n{body}"
                
    # Fallback for summary if not found in H2
    if not summary:
        first_p = re.search(r'^[^#\n].*', content, re.MULTILINE)
        summary = first_p.group(0).strip() if first_p else ""

    return {
        "title": title,
        "summary": summary,
        "techDocs": tech_docs,
        "code": code_block,
        "lang": lang,
        "author": author,
        "lastUpdated": last_updated
    }

def generate():
    docs_root = 'docs'
    platforms = ['ios', 'android', 'web']
    result = {
        "ios": {"accent": "#F03457", "rgb": "240, 52, 87", "modules": []},
        "android": {"accent": "#2AD189", "rgb": "42, 209, 137", "modules": []},
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
