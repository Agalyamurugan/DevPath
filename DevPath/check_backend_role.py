#!/usr/bin/env python
"""
Check Backend Developer role and quiz setup
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, RoadmapStep, LevelQuiz

# Get Backend Developer role and its steps
role = Role.objects.filter(name__contains='Backend Developer').first()
if role:
    print(f'Role: {role.name}')
    steps = RoadmapStep.objects.filter(role=role).order_by('order')
    print('Steps:')
    for step in steps:
        quiz = LevelQuiz.objects.filter(role=role, level=step.level).first()
        print(f'  {step.level} - {step.title} -> Quiz: {quiz.title if quiz else "None"}')
else:
    print('Backend Developer role not found')
    
    # Check all available roles
    print('\nAvailable roles:')
    all_roles = Role.objects.all()
    for r in all_roles:
        print(f'  - {r.name}')
