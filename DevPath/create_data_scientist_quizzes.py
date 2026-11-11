#!/usr/bin/env python
"""
Create quizzes for Data Scientist role
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, LevelQuiz

# Get Data Scientist role
role = Role.objects.filter(name__contains='Data Scientist').first()
if role:
    print(f'Creating quizzes for Data Scientist role: {role.name}')
    
    # Create quizzes for each level
    levels = ['Beginner', 'Intermediate', 'Advanced']
    
    for level in levels:
        quiz, created = LevelQuiz.objects.get_or_create(
            role=role,
            level=level,
            defaults={
                'title': f'{level} Data Science Quiz',
                'description': f'Test your knowledge of data science concepts at the {level.lower()} level.',
                'passing_score': 70
            }
        )
        
        if created:
            print(f'  Created {level} quiz: {quiz.title}')
        else:
            print(f'  {level} quiz already exists: {quiz.title}')
    
    print('\nData Scientist quizzes are ready!')
else:
    print('Data Scientist role not found')
