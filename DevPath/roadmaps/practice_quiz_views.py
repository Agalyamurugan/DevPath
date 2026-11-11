"""
Comprehensive Practice Quiz Views
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .practice_quizzes import get_all_role_quizzes

@login_required
def practice_quiz_hub(request):
    """Main hub for all practice quizzes"""
    user_selection = _get_selection(request.user)
    
    if not user_selection or not user_selection.role:
        return redirect('role_select')
    
    role_name = user_selection.role.name
    all_quizzes = get_all_role_quizzes()
    
    # Get quizzes for the user's role
    role_quizzes = all_quizzes.get(role_name, {})
    
    quiz_levels = []
    for level, questions in role_quizzes.items():
        quiz_levels.append({
            'level': level,
            'question_count': len(questions),
            'description': f"{level} level quiz with {len(questions)} questions"
        })
    
    context = {
        'role': role_name,
        'quiz_levels': quiz_levels,
        'total_questions': sum(len(q) for q in role_quizzes.values())
    }
    
    return render(request, 'roadmaps/practice_quiz_hub.html', context)

@login_required
def take_practice_quiz(request, role, level):
    """Take a practice quiz for a specific role and level"""
    all_quizzes = get_all_role_quizzes()
    
    # Get questions for this role and level
    role_quizzes = all_quizzes.get(role, {})
    questions = role_quizzes.get(level, [])
    
    if not questions:
        return redirect('practice_quiz_hub')
    
    # Store questions in session for result calculation
    request.session['quiz_questions'] = questions
    request.session['quiz_role'] = role
    request.session['quiz_level'] = level
    
    context = {
        'role': role,
        'level': level,
        'questions': questions,
        'total_questions': len(questions)
    }
    
    return render(request, 'roadmaps/take_practice_quiz.html', context)

@login_required
def submit_practice_quiz(request):
    """Submit and evaluate practice quiz"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    # Get quiz data from session
    questions = request.session.get('quiz_questions', [])
    role = request.session.get('quiz_role', '')
    level = request.session.get('quiz_level', '')
    
    if not questions:
        return JsonResponse({'error': 'Quiz not found'}, status=404)
    
    # Calculate results
    user_answers = []
    correct_count = 0
    results = []
    
    for i, question in enumerate(questions):
        user_answer = request.POST.get(f'question_{i}', '')
        is_correct = int(user_answer) == question['correct']
        
        if is_correct:
            correct_count += 1
        
        results.append({
            'question': question['question'],
            'options': question['options'],
            'user_answer': int(user_answer) if user_answer else None,
            'correct_answer': question['correct'],
            'is_correct': is_correct,
            'explanation': question['explanation']
        })
    
    score_percentage = (correct_count / len(questions)) * 100
    
    # Clear session data
    request.session.pop('quiz_questions', None)
    request.session.pop('quiz_role', None)
    request.session.pop('quiz_level', None)
    
    context = {
        'role': role,
        'level': level,
        'results': results,
        'correct_count': correct_count,
        'total_questions': len(questions),
        'score_percentage': score_percentage,
        'passed': score_percentage >= 60
    }
    
    return render(request, 'roadmaps/practice_quiz_result.html', context)

def _get_selection(user):
    """Get user's role selection"""
    try:
        from .models import UserRoleSelection
        return UserRoleSelection.objects.get(user=user)
    except UserRoleSelection.DoesNotExist:
        return None
