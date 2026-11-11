#!/usr/bin/env python
"""
Create all missing quizzes for all roles
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from roadmaps.models import Role, RoadmapStep, LevelQuiz

def create_missing_quizzes():
    """Create all missing quizzes"""
    
    print("Creating all missing quizzes...")
    print("=" * 50)
    
    # Get all roles
    all_roles = Role.objects.all()
    
    created_count = 0
    already_exists_count = 0
    
    for role in all_roles:
        print(f"\nProcessing role: {role.name}")
        steps = RoadmapStep.objects.filter(role=role).order_by('order')
        
        for step in steps:
            # Check if quiz already exists
            existing_quiz = LevelQuiz.objects.filter(role=role, level=step.level).first()
            
            if existing_quiz:
                print(f"  [EXISTS] {step.level} - {step.title}")
                already_exists_count += 1
            else:
                # Create new quiz
                quiz, created = LevelQuiz.objects.get_or_create(
                    role=role,
                    level=step.level,
                    defaults={
                        'title': f'{step.level} {role.name} Quiz',
                        'description': f'Test your knowledge of {role.name} concepts at the {step.level.lower()} level.',
                        'passing_score': 70
                    }
                )
                
                if created:
                    print(f"  [CREATED] {step.level} - {step.title}")
                    created_count += 1
                else:
                    print(f"  [EXISTS] {step.level} - {step.title}")
                    already_exists_count += 1
    
    print("\n" + "=" * 50)
    print(f"Summary:")
    print(f"  Created: {created_count} new quizzes")
    print(f"  Already existed: {already_exists_count} quizzes")
    print(f"  Total processed: {created_count + already_exists_count} quizzes")
    
    return created_count

if __name__ == "__main__":
    created = create_missing_quizzes()
    
    if created > 0:
        print(f"\nSuccess! Created {created} new quizzes.")
        print("All roles now have quizzes for their levels.")
    else:
        print("\nAll quizzes were already created.")
