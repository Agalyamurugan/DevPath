#!/usr/bin/env python3

import re

# Read the file
with open('z:/demo/roadmaps/seed_data.py', 'r') as f:
    content = f.read()

# Replace certification arrays for specific roles
roles_to_clear = ['Cybersecurity Analyst', 'Game Developer', 'Data Scientist', 'DevOps Engineer', 'IT Support Specialist', 'Database Administrator', 'System Administrator', 'QA Engineer', 'UX/UI Designer']

for role_name in roles_to_clear:
    # Find the role section and replace its certification array
    pattern = rf'(\"name\": \"{role_name}\".*?\"certification_recommendations\":\s*\[.*?\])'
    
    # Find the role start
    role_match = re.search(pattern, content, re.DOTALL)
    if role_match:
        # Find where the role ends (next role or end of file)
        role_start = role_match.start()
        role_end = content.find('\"name\":', role_start + 1)
        if role_end == -1:
            role_end = len(content)
        
        # Extract the role section
        role_section = content[role_start:role_end]
        
        # Replace certification array with empty
        updated_role_section = re.sub(r'\"certification_recommendations\":\s*\[.*?\]', '\"certification_recommendations\": []', role_section, flags=re.DOTALL)
        
        # Replace in content
        content = content[:role_start] + updated_role_section + content[role_end:]

# Write back to file
with open('z:/demo/roadmaps/seed_data.py', 'w') as f:
    f.write(content)

print('Updated certification arrays for specified roles')
