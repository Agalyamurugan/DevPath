import re

# Read the seed data file
with open('z:/demo/roadmaps/seed_data.py', 'r') as f:
    content = f.read()

# Find the first role and add level_quizzes after the steps array
# Look for the pattern where the first role ends its steps array
pattern = r'(\s+],\s+},\s+),\s+("certification_recommendations": \[)'
replacement = r'\1,\n        "level_quizzes": [\n            {\n                "level": "Beginner",\n                "title": "Python Fundamentals Quiz",\n                "description": "Test your knowledge of Python basics, variables, and control flow.",\n                "passing_score": 70,\n                "order": 1\n            }\n        ],\n        \2'

# Apply the replacement only for the first occurrence
new_content = re.sub(pattern, replacement, content, count=1)

# Write back to file
with open('z:/demo/roadmaps/seed_data.py', 'w') as f:
    f.write(new_content)

print("Added level_quizzes to the first role")
