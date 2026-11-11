#!/usr/bin/env python
"""
Create quizzes for Backend Developer role
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, LevelQuiz

# Get Backend Developer role
role = Role.objects.filter(name__contains='Backend Developer').first()
if role:
    print(f'Creating quizzes for Backend Developer role: {role.name}')
    
    # Create quizzes for each level
    levels = ['Beginner', 'Intermediate', 'Advanced']
    
    for level in levels:
        quiz, created = LevelQuiz.objects.get_or_create(
            role=role,
            level=level,
            defaults={
                'title': f'{level} Backend Developer Quiz',
                'description': f'Test your knowledge of backend development concepts at the {level.lower()} level.',
                'passing_score': 70
            }
        )
        
        if created:
            print(f'  Created {level} quiz: {quiz.title}')
        else:
            print(f'  {level} quiz already exists: {quiz.title}')
    
    print('\nBackend Developer quizzes are ready!')
else:
    print('Backend Developer role not found')
