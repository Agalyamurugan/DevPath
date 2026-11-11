#!/usr/bin/env python
"""
Check all roles and their quiz status
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, RoadmapStep, LevelQuiz

# All the roles you mentioned
all_roles_to_check = [
    'Full Stack Developer',
    'Frontend Developer', 
    'Backend Developer',
    'Python Developer',
    'Database Administrator',
    'Data Analyst',
    'Data Scientist',
    'DevOps Engineer',
    'Cybersecurity Analyst',
    'UI/UX Designer',
    'Game Developer',
    'Technical Support',
    'System Administrator',
    'QA Engineer',
    'Network Engineer',
    'IT Support Specialist'
]

print("Checking quiz status for all roles...")
print("=" * 60)

missing_quizzes = []

for role_name in all_roles_to_check:
    role = Role.objects.filter(name__contains=role_name).first()
    
    if role:
        print(f"\n[CHECK] {role.name}")
        steps = RoadmapStep.objects.filter(role=role).order_by('order')
        
        for step in steps:
            quiz = LevelQuiz.objects.filter(role=role, level=step.level).first()
            status = "[OK]" if quiz else "[MISSING]"
            print(f"  {status} {step.level} - {step.title} -> Quiz: {quiz.title if quiz else 'MISSING'}")
            
            if not quiz:
                missing_quizzes.append((role, step.level, step.title))
    else:
        print(f"\n[NOT FOUND] Role not found: {role_name}")
        # Check if there's a similar role
        all_roles = Role.objects.all()
        similar_roles = [r.name for r in all_roles if role_name.lower() in r.name.lower() or r.name.lower() in role_name.lower()]
        if similar_roles:
            print(f"   Similar roles found: {similar_roles}")

print("\n" + "=" * 60)
print(f"Summary: {len(missing_quizzes)} missing quizzes found")

if missing_quizzes:
    print("\nMissing quizzes:")
    for role, level, title in missing_quizzes:
        print(f"  - {role.name} - {level} - {title}")
else:
    print("\nAll roles have quizzes!")
