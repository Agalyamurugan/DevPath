#!/usr/bin/env python3

# Script to add free certifications to all roles

import re

# Read the file
with open('z:/demo/roadmaps/seed_data.py', 'r') as f:
    content = f.read()

# Define free certifications for each role
free_certs = {
    'Junior Software Developer/Engineer': [
        {
            "platform": "freecodecamp",
            "title": "freeCodeCamp Python Certification",
            "description": "Validate your Python programming skills with this comprehensive free certification.",
            "url": "https://www.freecodecamp.org/certification/freecodecamp-python-scientific-computing-with-python",
            "difficulty_level": "Intermediate",
            "duration": "300 hours",
            "rating": 4.8,
            "is_paid": False,
            "price": "Free",
            "provider": "freeCodeCamp",
            "prerequisites": "Basic programming knowledge",
            "order": 1
        },
        {
            "platform": "khan",
            "title": "Khan Academy Computer Programming Certificate",
            "description": "Free certificate covering programming fundamentals and computer science concepts.",
            "url": "https://www.khanacademy.org/computing/computer-programming",
            "difficulty_level": "Beginner",
            "duration": "Self-paced",
            "rating": 4.6,
            "is_paid": False,
            "price": "Free",
            "provider": "Khan Academy",
            "prerequisites": "Basic computer literacy",
            "order": 2
        }
    ],
    'Frontend Developer': [
        {
            "platform": "freecodecamp",
            "title": "freeCodeCamp Front End Development Libraries Certification",
            "description": "Validate your frontend development skills with this free certification covering HTML, CSS, JavaScript, React, and more.",
            "url": "https://www.freecodecamp.org/certification/freecodecamp-front-end-development-libraries",
            "difficulty_level": "Intermediate",
            "duration": "300 hours",
            "rating": 4.8,
            "is_paid": False,
            "price": "Free",
            "provider": "freeCodeCamp",
            "prerequisites": "HTML, CSS, and JavaScript knowledge",
            "order": 1
        },
        {
            "platform": "freecodecamp",
            "title": "freeCodeCamp Data Visualization Certification",
            "description": "Master data visualization with D3.js, React, and other modern libraries through this free certification.",
            "url": "https://www.freecodecamp.org/certification/freecodecamp-data-visualization",
            "difficulty_level": "Advanced",
            "duration": "300 hours",
            "rating": 4.7,
            "is_paid": False,
            "price": "Free",
            "provider": "freeCodeCamp",
            "prerequisites": "JavaScript and data analysis basics",
            "order": 2
        }
    ]
}

# Replace all empty certification arrays with free certifications
for role_name, certs in free_certs.items():
    # Find the role section
    role_pattern = r'("name": "' + role_name + r'"[^}]*?"certification_recommendations": \[\s*\])'
    
    # Find all matches
    matches = list(re.finditer(role_pattern, content, re.DOTALL))
    
    for match in matches:
        # Get the role section
        role_start = match.start()
        role_end = content.find('"name":', role_start + 1)
        if role_end == -1:
            role_end = len(content)
        
        # Extract the role section
        role_section = content[role_start:role_end]
        
        # Replace the empty certification array
        certs_list = ['                ' + str(c) for c in certs]
        certs_json = ',\n'.join(certs_list)
        replacement = '"certification_recommendations": [\n' + certs_json + '\n            ]'
        
        # Replace in content
        updated_role_section = re.sub(r'"certification_recommendations":\s*\[\s*\]', replacement, role_section, flags=re.DOTALL)
        
        # Replace in content
        content = content[:role_start] + updated_role_section + content[role_end:]
        
        break

# Write back to file
with open('z:/demo/roadmaps/seed_data.py', 'w') as f:
    f.write(content)

print("Added free certifications to all roles")
