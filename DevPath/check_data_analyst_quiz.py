#!/usr/bin/env python
"""
Check Data Analyst role and quiz setup
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, RoadmapStep, LevelQuiz
from roadmaps.practice_quizzes import get_all_role_quizzes

# Check Data Analyst role
role = Role.objects.filter(name__contains='Data Analyst').first()
if role:
    print(f'Role: {role.name}')
    steps = RoadmapStep.objects.filter(role=role).order_by('order')
    print('Steps:')
    for step in steps:
        quiz = LevelQuiz.objects.filter(role=role, level=step.level).first()
        print(f'  {step.level} - {step.title} -> Quiz: {quiz.title if quiz else "None"}')
else:
    print('Data Analyst role not found')
    
    # Check all available roles
    print('\nAvailable roles:')
    all_roles = Role.objects.all()
    for r in all_roles:
        print(f'  - {r.name}')

# Check if Data Analyst has questions in practice_quizzes
print('\n' + '='*50)
print('Checking practice quizzes for Data Analyst...')

all_quizzes = get_all_role_quizzes()
data_analyst_quizzes = all_quizzes.get('Data Analyst', {})

if data_analyst_quizzes:
    print('Data Analyst quizzes found in practice_quizzes:')
    for level, questions in data_analyst_quizzes.items():
        print(f'  {level}: {len(questions)} questions')
        if questions:
            print(f'    Sample question: {questions[0]["question"][:50]}...')
            print(f'    Has explanation: {"explanation" in questions[0]}')
else:
    print('No Data Analyst quizzes found in practice_quizzes')

# Check the quiz submission process
print('\n' + '='*50)
print('Checking quiz submission data structure...')

# Check if the practice quiz view can handle Data Analyst
from roadmaps.practice_quiz_views import _get_selection

# Simulate getting a user (we'll check the structure)
print('Practice quiz view structure:')
print('  - Uses get_all_role_quizzes() for questions')
print('  - Stores questions in session')
print('  - Processes form submission')
print('  - Renders results with explanations')
