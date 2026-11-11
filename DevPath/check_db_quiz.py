from roadmaps.models import Role, RoadmapStep, LevelQuiz

# Get Database Administrator role and its steps
role = Role.objects.filter(name__contains='Database Administrator').first()
if role:
    print(f'Role: {role.name}')
    steps = RoadmapStep.objects.filter(role=role).order_by('order')
    print('Steps:')
    for step in steps:
        quiz = LevelQuiz.objects.filter(role=role, level=step.level).first()
        print(f'  {step.level} - {step.title} -> Quiz: {quiz.title if quiz else "None"}')
else:
    print('Database Administrator role not found')
