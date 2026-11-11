from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from datetime import date, timedelta

from .models import (
    Assessment,
    Choice,
    CertificationRecommendation,
    CompletedRole,
    CourseRecommendation,
    CourseResource,
    LevelQuiz,
    Question,
    Role,
    RoadmapStep,
    StepResource,
    UserAssessment,
    UserLevelQuiz,
    UserResourceCompletion,
    UserStats,
    UserRoleSelection,
)
from .dynamic_questions import get_level_questions, get_data_science_questions, get_database_administrator_questions
from .achievements import compute_achievements
from .chatbot import chatbot
from .ai_chatbot import get_ai_response


def _get_selection(user):
    try:
        return UserRoleSelection.objects.get(user=user)
    except UserRoleSelection.DoesNotExist:
        return None


def _get_or_create_stats(user):
    stats, created = UserStats.objects.get_or_create(user=user)
    return stats


def _check_level_quiz_completion(user, role, level):
    """Check if user has completed the level quiz for the specified level"""
    try:
        level_quiz = LevelQuiz.objects.get(role=role, level=level)
        user_quiz = UserLevelQuiz.objects.filter(user=user, level_quiz=level_quiz).first()
        return user_quiz and user_quiz.passed
    except LevelQuiz.DoesNotExist:
        return False


def update_user_stats(user, points_to_add=0):
    """Update user points and streak based on activity"""
    stats = _get_or_create_stats(user)
    today = date.today()
    
    # Award points if provided
    if points_to_add > 0:
        stats.total_points += points_to_add
    
    # Update streak based on daily activity
    if stats.last_completion_date:
        days_diff = (today - stats.last_completion_date).days
        if days_diff == 1:
            # Consecutive day
            stats.current_streak += 1
        elif days_diff > 1:
            # Streak broken
            stats.current_streak = 1
        # days_diff == 0 means same day, don't change streak
    else:
        # First activity
        stats.current_streak = 1
    
    # Update longest streak if needed
    if stats.current_streak > stats.longest_streak:
        stats.longest_streak = stats.current_streak
    
    stats.last_completion_date = today
    stats.save()
    
    return stats


def award_level_completion_points(user, role, level):
    """Award points for completing a level"""
    points_per_level = {
        'Beginner': 100,
        'Intermediate': 200,
        'Advanced': 300
    }
    
    points = points_per_level.get(level, 100)
    stats = update_user_stats(user, points)
    
    return stats


def compute_role_progress(user, role):
    """
    Returns a list of dicts:
      - step
      - unlocked (based on previous step completed)
      - completed (based on all required resources completed)
      - required_resources (StepResource objects, filtered to required only)
    """
    steps = (
        RoadmapStep.objects.filter(role=role)
        .order_by('order')
        .prefetch_related(
            Prefetch(
                'step_resources',
                queryset=StepResource.objects.filter(is_required=True).select_related('resource').order_by('order'),
                to_attr='required_resources',
            )
        )
    )

    required_resource_ids = set()
    required_resources_by_step = []
    for step in steps:
        required_resources = getattr(step, 'required_resources', [])
        required_resources_by_step.append(required_resources)
        required_resource_ids.update(sr.resource_id for sr in required_resources)

    completed_resource_ids = set(
        UserResourceCompletion.objects.filter(user=user, resource_id__in=required_resource_ids).values_list(
            'resource_id', flat=True
        )
    )

    progress = []
    prev_completed = True  # first step should be unlocked
    for idx, step in enumerate(steps):
        required_resources = required_resources_by_step[idx]

        completed = all(sr.resource_id in completed_resource_ids for sr in required_resources)
        unlocked = True if idx == 0 else prev_completed

        # Attach completion state to each required link for UI rendering.
        for sr in required_resources:
            sr.completed = sr.resource_id in completed_resource_ids

        progress.append(
            {
                'step': step,
                'unlocked': unlocked,
                'completed': completed,
                'required_resources': required_resources,
            }
        )
        prev_completed = completed

    completed_steps = sum(1 for p in progress if p['completed'])
    total_steps = len(progress)
    percent = 0 if total_steps == 0 else int((completed_steps / total_steps) * 100)

    return progress, percent, completed_steps, total_steps


def index(request):
    roles = Role.objects.all().order_by('name')
    
    # Show home page for all users - template will handle button display based on auth status
    return render(request, 'roadmaps/index.html', {'roles': roles})


@login_required
def role_select(request):
    # Get roles the user has already completed
    completed_role_ids = list(
        CompletedRole.objects.filter(user=request.user).values_list('role_id', flat=True)
    )
    
    # Get all available roles, excluding completed ones
    available_roles = Role.objects.exclude(id__in=completed_role_ids).order_by('name')
    
    selection = _get_selection(request.user)

    if request.method == 'POST':
        role_id = request.POST.get('role_id')
        role = get_object_or_404(Role, id=role_id)
        
        # Check if user has already completed this role
        if CompletedRole.objects.filter(user=request.user, role=role).exists():
            messages.error(request, f'You have already completed the {role.name} role!')
            return redirect('role_select')
        
        UserRoleSelection.objects.update_or_create(user=request.user, defaults={'role': role})
        return redirect('roadmap')

    current_role_id = selection.role_id if selection else None
    return render(
        request,
        'roadmaps/role_select.html',
        {
            'roles': available_roles,
            'current_role_id': current_role_id,
            'completed_roles': Role.objects.filter(id__in=completed_role_ids).order_by('name'),
        },
    )


@login_required
def roadmap(request):
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')

    role = selection.role
    progress, percent, completed_steps, total_steps = compute_role_progress(request.user, role)

    # Check if user has completed all steps and mark role as completed
    if percent == 100 and completed_steps == total_steps:
        # User has completed all steps for this role
        completed_role, created = CompletedRole.objects.get_or_create(
            user=request.user,
            role=role
        )
        if created:
            messages.success(request, f'Congratulations! You have completed the {role.name} role!')
    
    # Check if user can proceed to next level based on quiz completion
    current_level = None
    next_level_unlocked = False
    
    # Determine current level and check quiz completion
    for step in progress:
        if step['completed']:
            current_level = step['step'].level
            break
    
    if current_level:
        # Check if the quiz for current level is completed
        quiz_completed = _check_level_quiz_completion(request.user, role, current_level)
        
        # Determine next level
        level_order = {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}
        current_order = level_order.get(current_level, 0)
        next_order = current_order + 1
        next_level = None
        
        for level, order in level_order.items():
            if order == next_order:
                next_level = level
                break
        
        # Check if next level quiz is completed (if it exists)
        if next_level:
            next_level_quiz_completed = _check_level_quiz_completion(request.user, role, next_level)
            next_level_unlocked = next_level_quiz_completed

    # Get certification recommendations for this role
    certifications = CertificationRecommendation.objects.filter(role=role).order_by('order', 'id')

    return render(
        request,
        'roadmaps/roadmap.html',
        {
            'role': role,
            'progress': progress,
            'percent': percent,
            'completed_steps': completed_steps,
            'total_steps': total_steps,
            'certifications': certifications,
            'current_level': current_level,
            'next_level_unlocked': next_level_unlocked,
        },
    )


@login_required
def dashboard(request):
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')

    role = selection.role
    progress, percent, completed_steps, total_steps = compute_role_progress(request.user, role)

    next_step = next((p for p in progress if p['unlocked'] and not p['completed']), None)
    achievements = compute_achievements(request.user, role)
    user_stats = _get_or_create_stats(request.user)
    
    # Get completed roles for achievements section
    completed_roles = CompletedRole.objects.filter(user=request.user).select_related('role').order_by('role__name')
    
    # Calculate level progress data
    level_data = calculate_level_progress(request.user, role)

    return render(
        request,
        'roadmaps/dashboard.html',
        {
            'role': role,
            'percent': percent,
            'completed_steps': completed_steps,
            'total_steps': total_steps,
            'next_step': next_step,
            'progress': progress,
            'achievements': achievements,
            'user_stats': user_stats,
            'completed_roles': completed_roles,
            'level_data': level_data,
        },
    )


def calculate_level_progress(user, role):
    """Calculate progress data for each level"""
    from .models import RoadmapStep, UserResourceCompletion, UserLevelQuiz, StepResource
    
    levels = ['Beginner', 'Intermediate', 'Advanced']
    points_per_level = {'Beginner': 100, 'Intermediate': 200, 'Advanced': 300}
    level_data = {}
    
    for i, level in enumerate(levels):
        # Get all steps for this level
        level_steps = RoadmapStep.objects.filter(role=role, level=level)
        total_steps = level_steps.count()
        
        if total_steps == 0:
            level_data[level] = {
                'completed': False,
                'current': False,
                'started': False,
                'completed_steps': 0,
                'total_steps': 0,
                'points': 0
            }
            continue
        
        # Count completed steps by checking required resources
        completed_steps = 0
        for step in level_steps:
            # Get required resources for this step
            required_resources = StepResource.objects.filter(step=step, is_required=True)
            
            # Check if all required resources are completed
            step_completed = True
            for sr in required_resources:
                completion = UserResourceCompletion.objects.filter(user=user, resource=sr.resource).first()
                if not completion:
                    step_completed = False
                    break
            
            if step_completed:
                completed_steps += 1
        
        # Check if level quiz is passed (if exists)
        quiz_passed = True
        try:
            level_quiz = LevelQuiz.objects.get(role=role, level=level)
            user_quiz = UserLevelQuiz.objects.filter(user=user, level_quiz=level_quiz).first()
            if not user_quiz or not user_quiz.passed:
                quiz_passed = False
        except LevelQuiz.DoesNotExist:
            pass  # No quiz required for this level
        
        # Determine level status
        is_completed = (completed_steps == total_steps) and quiz_passed
        is_started = completed_steps > 0
        
        # Determine if this is the current level
        is_current = False
        if is_started and not is_completed:
            is_current = True
        elif i == 0 and not is_started:  # First level and not started
            is_current = True
        elif i > 0 and level_data.get(levels[i-1], {}).get('completed', False) and not is_started:
            is_current = True
        
        level_data[level] = {
            'completed': is_completed,
            'current': is_current,
            'started': is_started,
            'completed_steps': completed_steps,
            'total_steps': total_steps,
            'points': points_per_level.get(level, 0) if is_completed else 0
        }
    
    return level_data


def check_and_award_level_completion(user, role):
    """Check if user has completed any levels and award points accordingly"""
    from .models import RoadmapStep, UserResourceCompletion, UserLevelQuiz, StepResource
    
    for level in [RoadmapStep.LEVEL_BEGINNER, RoadmapStep.LEVEL_INTERMEDIATE, RoadmapStep.LEVEL_ADVANCED]:
        # Get all steps for this level
        level_steps = RoadmapStep.objects.filter(role=role, level=level)
        
        if not level_steps.exists():
            continue
            
        # Check if all steps in this level are completed
        all_completed = True
        for step in level_steps:
            # Get required resources for this step
            required_resources = StepResource.objects.filter(step=step, is_required=True)
            
            # Check if all required resources are completed
            step_completed = True
            for sr in required_resources:
                completion = UserResourceCompletion.objects.filter(user=user, resource=sr.resource).first()
                if not completion:
                    step_completed = False
                    break
            
            if not step_completed:
                all_completed = False
                break
        
        # Check if level quiz is passed (if exists)
        quiz_passed = True
        try:
            level_quiz = LevelQuiz.objects.get(role=role, level=level)
            user_quiz = UserLevelQuiz.objects.filter(user=user, level_quiz=level_quiz).first()
            if not user_quiz or not user_quiz.passed:
                quiz_passed = False
        except LevelQuiz.DoesNotExist:
            pass  # No quiz required for this level
        
        # Award points if level is completed and not already awarded
        if all_completed and quiz_passed:
            # Check if points for this level have already been awarded
            # We can use a simple approach: check if user has any progress in next level
            next_level_index = [RoadmapStep.LEVEL_BEGINNER, RoadmapStep.LEVEL_INTERMEDIATE, RoadmapStep.LEVEL_ADVANCED].index(level)
            if next_level_index < 2:  # Not the last level
                next_level = [RoadmapStep.LEVEL_BEGINNER, RoadmapStep.LEVEL_INTERMEDIATE, RoadmapStep.LEVEL_ADVANCED][next_level_index + 1]
                next_level_steps = RoadmapStep.objects.filter(role=role, level=next_level)
                
                # If user has started next level, they must have completed current level
                has_started_next_level = False
                for step in next_level_steps:
                    required_resources = StepResource.objects.filter(step=step, is_required=True)
                    for sr in required_resources:
                        completion = UserResourceCompletion.objects.filter(user=user, resource=sr.resource).first()
                        if completion:
                            has_started_next_level = True
                            break
                    if has_started_next_level:
                        break
                
                if not has_started_next_level:
                    # Award points for completing this level
                    award_level_completion_points(user, role, level)


@login_required
def complete_resource(request, resource_id: int):
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')

    role = selection.role
    resource = get_object_or_404(CourseResource, id=resource_id)

    # Only allow marking completion if this resource is required for an unlocked, not-yet-completed step.
    progress, _, _, _ = compute_role_progress(request.user, role)
    eligible_step = None
    for p in progress:
        if not p['unlocked'] or p['completed']:
            continue
        if any(sr.resource_id == resource.id for sr in p['required_resources']):
            eligible_step = p['step']
            break

    if eligible_step is None:
        # Silently ignore; keep UX simple.
        return redirect(reverse('roadmap'))

    # Create completion record and update stats for daily activity
    completion, created = UserResourceCompletion.objects.get_or_create(user=request.user, resource=resource)
    if created:
        # Update streak for daily activity (no points for resource completion)
        update_user_stats(request.user)
        
        # Check if this step completion leads to level completion
        check_and_award_level_completion(request.user, role)
    
    return redirect(reverse('roadmap'))


@login_required
def test_db_quiz(request):
    """Test view to directly show Database Administrator quiz"""
    from roadmaps.models import Role, LevelQuiz
    
    # Get Database Administrator role and beginner quiz
    role = Role.objects.filter(name__contains='Database Administrator').first()
    if role:
        quiz = LevelQuiz.objects.filter(role=role, level='Beginner').first()
        if quiz:
            return render(request, 'roadmaps/quiz_list.html', {
                'level': 'Beginner',
                'quiz': quiz,
                'user_quiz': None,
            })
    
    return render(request, 'roadmaps/quiz_list.html', {
        'level': 'Beginner',
        'quiz': None,
        'user_quiz': None,
    })


@login_required
def quiz_list(request, level: str):
    """List available quizzes for a level"""
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    role = selection.role
    quiz = LevelQuiz.objects.filter(role=role, level=level).first()
    
    if not quiz:
        return render(request, 'roadmaps/quiz_list.html', {
            'level': level,
            'quiz': None,
        })
    
    # Check if user has completed this quiz
    user_quiz = UserLevelQuiz.objects.filter(user=request.user, level_quiz=quiz).first()
    
    return render(request, 'roadmaps/take_quiz.html', {
        'level': level,
        'quiz': quiz,
        'user_quiz': user_quiz,
    })


@login_required
def take_quiz(request, quiz_id: int):
    """Take a level quiz"""
    quiz = get_object_or_404(LevelQuiz.objects.prefetch_related(), id=quiz_id)
    
    # Get user's role for specialized questions
    selection = _get_selection(request.user)
    role_name = selection.role.name if selection and selection.role else None
    
    # Define quiz questions based on quiz title and role
    quiz_questions = get_quiz_questions(quiz.title, role_name)
    
    if request.method == 'POST':
        score = 0
        total_points = len(quiz_questions) * 20  # 20 points per question
        
        for i, question in enumerate(quiz_questions):
            question_key = f'question_{i}'
            user_answer = request.POST.get(question_key)
            if user_answer and str(user_answer) == str(question['correct']):
                score += 20
        
        percentage_score = int((score / total_points * 100)) if total_points > 0 else 0
        passed = percentage_score >= quiz.passing_score
        
        # Save user quiz (update or create)
        user_quiz = UserLevelQuiz.objects.update_or_create(
            user=request.user,
            level_quiz=quiz,
            defaults={
                'score': percentage_score,
                'passed': passed,
            },
        )
        
        return redirect('quiz_result', quiz_id=quiz_id)
    
    return render(request, 'roadmaps/take_quiz.html', {
        'quiz': quiz,
        'questions': quiz_questions,
    })


def chatbot_api(request):
    """Chatbot API endpoint with real AI integration"""
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()
        if not user_message:
            return JsonResponse({'error': 'Message is required'}, status=400)
        
        try:
            # Get response from real AI
            ai_response = get_ai_response(user_message)
            return JsonResponse({'response': ai_response})
        except Exception as e:
            # Fallback to local chatbot if AI fails
            fallback_response = chatbot.get_response(user_message)
            return JsonResponse({'response': fallback_response})
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def get_quiz_questions(quiz_title, role_name=None):
    """Get quiz questions based on user level and role"""
    # Get the level from the quiz title or use default
    if 'Beginner' in quiz_title:
        level = 'Beginner'
    elif 'Intermediate' in quiz_title:
        level = 'Intermediate'
    elif 'Advanced' in quiz_title:
        level = 'Advanced'
    else:
        level = 'Beginner'  # Default to beginner
    
    # Use role-specific questions if available
    if role_name:
        if 'Data Scientist' in role_name or 'Data Analyst' in role_name:
            return get_data_science_questions(level)
        elif 'Database Administrator' in role_name:
            return get_database_administrator_questions(level)
    
    return get_level_questions(level)


@login_required
def quiz_result(request, quiz_id: int):
    """Show quiz result"""
    quiz = get_object_or_404(LevelQuiz.objects.prefetch_related(), id=quiz_id)
    user_quiz = UserLevelQuiz.objects.filter(user=request.user, level_quiz=quiz).first()
    
    # Get user's role selection
    selection = _get_selection(request.user)
    role_name = selection.role.name if selection and selection.role else None
    
    # Get questions using the same function as take_quiz
    questions = get_quiz_questions(quiz.title, role_name)
    
    return render(request, 'roadmaps/quiz_result.html', {
        'quiz': quiz,
        'user_quiz': user_quiz,
        'questions': questions,
    })


@login_required
def practice_hub(request):
    """Main practice hub page with level-based quizzes"""
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    role = selection.role
    user_stats = _get_or_create_stats(request.user)
    
    # Get available quizzes for each level
    levels = ['Beginner', 'Intermediate', 'Advanced']
    quiz_data = {}
    
    for level in levels:
        quiz = LevelQuiz.objects.filter(role=role, level=level).first()
        user_quiz = UserLevelQuiz.objects.filter(user=request.user, level_quiz=quiz).first() if quiz else None
        
        quiz_data[level] = {
            'quiz': quiz,
            'user_quiz': user_quiz,
            'can_take': user_quiz is None or not user_quiz.passed,
            'passed': user_quiz and user_quiz.passed,
            'score': user_quiz.score if user_quiz else 0,
        }
    
    return render(request, 'roadmaps/practice_hub.html', {
        'role': role,
        'quiz_data': quiz_data,
        'user_stats': user_stats,
    })


@login_required
def assessment_list(request, step_id: int):
    """List available assessments for a step"""
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    step = get_object_or_404(RoadmapStep, id=step_id, role=selection.role)
    
    # Check if step is completed
    progress, _, _, _ = compute_role_progress(request.user, selection.role)
    step_progress = next((p for p in progress if p['step'].id == step.id), None)
    
    if not step_progress or not step_progress['completed']:
        return redirect('roadmap')
    
    assessments = Assessment.objects.filter(step=step).prefetch_related('questions__choices')
    user_assessments = UserAssessment.objects.filter(user=request.user, assessment__in=assessments)
    completed_assessment_ids = set(ua.assessment_id for ua in user_assessments)
    
    return render(request, 'roadmaps/assessment_list.html', {
        'step': step,
        'assessments': assessments,
        'completed_assessment_ids': completed_assessment_ids,
        'user_assessments': user_assessments,
    })


@login_required
def take_assessment(request, assessment_id: int):
    """Take an assessment"""
    assessment = get_object_or_404(Assessment.objects.prefetch_related('questions__choices'), id=assessment_id)
    
    # Check if user has already completed this assessment
    existing = UserAssessment.objects.filter(user=request.user, assessment=assessment).first()
    if existing:
        return redirect('assessment_result', assessment_id=assessment_id)
    
    if request.method == 'POST':
        score = 0
        total_points = 0
        
        for question in assessment.questions.all():
            total_points += question.points
            question_key = f'question_{question.id}'
            
            if question.question_type == Question.QUESTION_TYPE_MULTIPLE_CHOICE:
                selected_choice_id = request.POST.get(question_key)
                if selected_choice_id:
                    try:
                        choice = Choice.objects.get(id=selected_choice_id, question=question)
                        if choice.is_correct:
                            score += question.points
                    except Choice.DoesNotExist:
                        pass
            elif question.question_type == Question.QUESTION_TYPE_TRUE_FALSE:
                answer = request.POST.get(question_key)
                if answer == 'true':
                    # For true/false, we'd need to store the correct answer in the question
                    # For now, assume first choice is correct
                    correct_choice = question.choices.filter(is_correct=True).first()
                    if correct_choice and correct_choice.choice_text.lower() == 'true':
                        score += question.points
        
        # Calculate percentage score
        percentage_score = int((score / total_points * 100)) if total_points > 0 else 0
        passed = percentage_score >= assessment.passing_score
        
        # Save user assessment
        user_assessment = UserAssessment.objects.create(
            user=request.user,
            assessment=assessment,
            score=percentage_score,
            passed=passed
        )
        
        # Award badge if passed
        if passed and assessment.badge_name:
            Badge.objects.get_or_create(
                user=request.user,
                assessment=assessment,
                defaults={
                    'name': assessment.badge_name,
                    'description': f'Completed {assessment.title} with {percentage_score}% score'
                }
            )
        
        # Award certificate if passed and has certificate title
        if passed and assessment.certificate_title:
            import uuid
            cert_id = f"CERT-{uuid.uuid4().hex[:12].upper()}"
            Certificate.objects.get_or_create(
                user=request.user,
                assessment=assessment,
                defaults={
                    'title': assessment.certificate_title,
                    'description': f'Successfully completed {assessment.title}',
                    'certificate_id': cert_id
                }
            )
        
        return redirect('assessment_result', assessment_id=assessment_id)
    
    return render(request, 'roadmaps/take_assessment.html', {
        'assessment': assessment,
    })


@login_required
def assessment_result(request, assessment_id: int):
    """Show assessment result"""
    assessment = get_object_or_404(Assessment, id=assessment_id)
    user_assessment = get_object_or_404(UserAssessment, user=request.user, assessment=assessment)
    
    badge = Badge.objects.filter(user=request.user, assessment=assessment).first()
    certificate = Certificate.objects.filter(user=request.user, assessment=assessment).first()
    
    return render(request, 'roadmaps/assessment_result.html', {
        'assessment': assessment,
        'user_assessment': user_assessment,
        'badge': badge,
        'certificate': certificate,
    })


@login_required
def badges_and_certificates(request):
    """Show all user badges and certificates"""
    selection = _get_selection(request.user)
    
    badges = Badge.objects.filter(user=request.user).select_related('assessment__step__role')
    certificates = Certificate.objects.filter(user=request.user).select_related('assessment__step__role')
    
    return render(request, 'roadmaps/badges_and_certificates.html', {
        'badges': badges,
        'certificates': certificates,
        'current_role': selection.role if selection else None,
    })


@login_required
def course_recommendations(request, step_id: int):
    """Show course recommendations for a step"""
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    step = get_object_or_404(RoadmapStep, id=step_id, role=selection.role)
    
    # Check if step is completed
    progress, _, _, _ = compute_role_progress(request.user, selection.role)
    step_progress = next((p for p in progress if p['step'].id == step.id), None)
    
    if not step_progress or not step_progress['completed']:
        return redirect('roadmap')
    
    recommendations = CourseRecommendation.objects.filter(step=step).order_by('order', 'platform')
    
    # Get YouTube recommendation with highest rating (as proxy for views)
    youtube_recommendation = recommendations.filter(platform='youtube').first()
    other_recommendations = recommendations.exclude(platform='youtube')
    
    # If YouTube recommendation exists, redirect directly to it
    if youtube_recommendation:
        return redirect(youtube_recommendation.url)
    
    return render(request, 'roadmaps/course_recommendations.html', {
        'step': step,
        'recommendations': recommendations,
        'youtube_recommendation': youtube_recommendation,
        'other_recommendations': other_recommendations,
        'current_role': selection.role,
    })


@login_required
def leaderboard(request):
    """Show leaderboard of all users"""
    period = request.GET.get('period', 'monthly')
    
    # Get all user stats with their user info and current role
    leaderboard_data = UserStats.objects.select_related('user').prefetch_related(
        Prefetch('user__role_selection', queryset=UserRoleSelection.objects.select_related('role'))
    ).order_by('-total_points', '-current_streak')[:50]  # Top 50 users
    
    leaderboard_list = []
    for rank, stats in enumerate(leaderboard_data, 1):
        user_selection = getattr(stats.user, 'role_selection', None)
        current_role = user_selection.role if user_selection else None
        
        # Calculate level and progress based on completed steps
        level = "Beginner"
        progress_percentage = 0
        completed_steps = 0
        total_steps = 0
        
        if current_role:
            completed_steps = RoadmapStep.objects.filter(
                role=current_role,
                step_resources__resource__completions__user=stats.user
            ).distinct().count()
            total_steps = RoadmapStep.objects.filter(role=current_role).count()
            
            if total_steps > 0:
                progress_percentage = int((completed_steps / total_steps) * 100)
                if progress_percentage >= 80:
                    level = "Expert"
                elif progress_percentage >= 60:
                    level = "Advanced"
                elif progress_percentage >= 40:
                    level = "Intermediate"
                elif progress_percentage >= 20:
                    level = "Junior"
        
        leaderboard_list.append({
            'rank': rank,
            'user': stats.user,
            'total_points': stats.total_points,
            'current_streak': stats.current_streak,
            'longest_streak': stats.longest_streak,
            'current_role': current_role,
            'level': level,
            'progress_percentage': progress_percentage,
            'completed_steps': completed_steps,
            'total_steps': total_steps,
        })
    
    return render(request, 'roadmaps/leaderboard.html', {
        'leaderboard': leaderboard_list,
        'period': period,
    })


@login_required
def practice_hub(request):
    """Show practice hub with quizzes and exercises"""
    selection = _get_selection(request.user)
    
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    # Get available quizzes for current role
    quizzes = LevelQuiz.objects.filter(role=selection.role).order_by('level', 'order')
    
    # Get user's quiz attempts
    user_quizzes = UserLevelQuiz.objects.filter(
        user=request.user, 
        level_quiz__role=selection.role
    ).select_related('level_quiz')
    
    # Mark which quizzes are completed/passed
    quiz_data = []
    for quiz in quizzes:
        user_quiz = user_quizzes.filter(level_quiz=quiz).first()
        quiz_data.append({
            'quiz': quiz,
            'attempted': user_quiz is not None,
            'passed': user_quiz.passed if user_quiz else False,
            'best_score': user_quiz.score if user_quiz else 0,
            'attempts': UserLevelQuiz.objects.filter(user=request.user, level_quiz=quiz).count()
        })
    
    # Calculate stats
    total_quizzes = quizzes.count()
    passed_quizzes = UserLevelQuiz.objects.filter(
        user=request.user, 
        level_quiz__role=selection.role,
        passed=True
    ).count()
    
    # Get user stats for streak and average score
    user_stats = getattr(request.user, 'stats', None)
    current_streak = user_stats.current_streak if user_stats else 0
    
    # Calculate average score
    user_quiz_scores = UserLevelQuiz.objects.filter(
        user=request.user, 
        level_quiz__role=selection.role
    ).values_list('score', flat=True)
    average_score = int(sum(user_quiz_scores) / len(user_quiz_scores)) if user_quiz_scores else 0
    
    # Group quiz data by level and calculate progress percentages
    from itertools import groupby
    quiz_data.sort(key=lambda x: x['quiz'].level)
    level_groups = []
    for level, group in groupby(quiz_data, key=lambda x: x['quiz'].level):
        group_list = list(group)
        # Calculate progress as percentage of quizzes completed in this level
        completed_in_level = sum(1 for q in group_list if q['passed'])
        progress_percentage = int((completed_in_level / len(group_list)) * 100) if group_list else 0
        
        level_groups.append({
            'level': level,
            'quizzes': group_list,
            'progress_percentage': progress_percentage,
            'total_in_level': len(group_list),
            'completed_in_level': completed_in_level
        })
    
    return render(request, 'roadmaps/practice_hub.html', {
        'quiz_data': quiz_data,
        'current_role': selection.role,
        'total_quizzes': total_quizzes,
        'passed_quizzes': passed_quizzes,
        'current_streak': current_streak,
        'average_score': average_score,
        'level_groups': level_groups,
    })


@login_required
def build_hub(request):
    """Jobs hub - show job postings for user's role"""
    selection = _get_selection(request.user)
    if not selection or not selection.role_id:
        return redirect('role_select')
    
    current_role = selection.role
    
    # Get job postings for the current role
    job_postings = get_job_postings(current_role.name)
    
    # Get user's completed steps for progress calculation
    completed_steps = RoadmapStep.objects.filter(
        role=current_role,
        step_resources__resource__completions__user=request.user
    ).distinct().count()
    
    total_steps = RoadmapStep.objects.filter(role=current_role).count()
    overall_progress = (completed_steps / total_steps * 100) if total_steps > 0 else 0
    
    context = {
        'current_role': current_role,
        'job_postings': job_postings,
        'overall_progress': overall_progress,
        'completed_steps': completed_steps,
        'total_steps': total_steps,
    }
    
    return render(request, 'roadmaps/build_hub.html', context)


def get_job_postings(role_name):
    """Get job postings based on role"""
    job_db = {
        'Frontend Developer': [
            {
                'title': 'Senior Frontend Developer',
                'company': 'TechCorp Solutions',
                'location': 'San Francisco, CA',
                'type': 'Full-time',
                'experience': '5+ years',
                'salary': '$120k - $160k',
                'description': 'We are looking for an experienced Frontend Developer to join our dynamic team and build amazing user experiences.',
                'requirements': [
                    'Expert knowledge of HTML, CSS, JavaScript',
                    'Strong experience with React.js',
                    'Experience with modern frontend tools (Webpack, Babel)',
                    'Understanding of responsive design principles',
                    'Knowledge of accessibility standards'
                ],
                'skills': ['React', 'TypeScript', 'CSS3', 'JavaScript', 'Git'],
                'posted_date': '2 days ago',
                'logo': '🏢',
                'apply_url': 'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=39084321'
            },
            {
                'title': 'React Developer',
                'company': 'Digital Innovations Inc',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$90k - $130k',
                'description': 'Join our remote team to build cutting-edge web applications using React and modern frontend technologies.',
                'requirements': [
                    '3+ years of React development experience',
                    'Strong JavaScript and ES6+ knowledge',
                    'Experience with state management (Redux, Context)',
                    'Familiarity with RESTful APIs',
                    'Understanding of testing frameworks'
                ],
                'skills': ['React', 'Redux', 'JavaScript', 'Node.js', 'Jest'],
                'posted_date': '1 week ago',
                'logo': '💻',
                'apply_url': 'https://www.indeed.com/jobs?q=react+developer&l=Remote&vjk=1f8d3c4a5b6e7f8g'
            },
            {
                'title': 'Frontend Engineer',
                'company': 'StartupHub',
                'location': 'New York, NY',
                'type': 'Full-time',
                'experience': '2-4 years',
                'salary': '$80k - $110k',
                'description': 'Help us build the future of web applications. Looking for passionate frontend engineers who love clean code.',
                'requirements': [
                    'Proficiency in HTML5, CSS3, JavaScript',
                    'Experience with at least one modern framework',
                    'Understanding of cross-browser compatibility',
                    'Knowledge of version control systems',
                    'Strong problem-solving skills'
                ],
                'skills': ['Vue.js', 'JavaScript', 'SASS', 'Webpack', 'Git'],
                'posted_date': '3 days ago',
                'logo': '🚀',
                'apply_url': 'https://www.glassdoor.com/Job/remote-frontend-engineer-jobs-SRCH_KO0,24.htm'
            },
            {
                'title': 'UI/UX Frontend Developer',
                'company': 'DesignTech Studios',
                'location': 'Los Angeles, CA',
                'type': 'Full-time',
                'experience': '3-6 years',
                'salary': '$95k - $135k',
                'description': 'Combine your design skills with frontend development to create beautiful, functional user interfaces.',
                'requirements': [
                    'Strong frontend development skills',
                    'Eye for design and user experience',
                    'Experience with Figma or similar design tools',
                    'Knowledge of CSS animations and transitions',
                    'Understanding of user-centered design principles'
                ],
                'skills': ['React', 'Figma', 'CSS3', 'JavaScript', 'UI/UX'],
                'posted_date': '4 days ago',
                'logo': '🎨',
                'apply_url': 'https://www.behance.net/jobboard?position=UI%2FUX+Frontend+Developer'
            },
            {
                'title': 'JavaScript Developer',
                'company': 'CodeCraft Solutions',
                'location': 'Austin, TX',
                'type': 'Full-time',
                'experience': '2-5 years',
                'salary': '$85k - $120k',
                'description': 'Join our team to build robust JavaScript applications and contribute to open-source projects.',
                'requirements': [
                    'Deep understanding of JavaScript core concepts',
                    'Experience with Node.js and Express',
                    'Knowledge of modern JavaScript frameworks',
                    'Understanding of asynchronous programming',
                    'Experience with database integration'
                ],
                'skills': ['JavaScript', 'Node.js', 'Express', 'MongoDB', 'Git'],
                'posted_date': '5 days ago',
                'logo': '⚡',
                'apply_url': 'https://stackoverflow.com/jobs/developer-jobs'
            },
            {
                'title': 'Frontend Developer - Remote',
                'company': 'GlobalTech Inc',
                'location': 'Remote (Worldwide)',
                'type': 'Full-time',
                'experience': '4+ years',
                'salary': '$100k - $140k',
                'description': 'Work remotely with our global team to build scalable frontend applications for enterprise clients.',
                'requirements': [
                    '4+ years of frontend development experience',
                    'Experience with React or Angular',
                    'Strong communication skills for remote collaboration',
                    'Self-motivated and independent worker',
                    'Experience with agile methodologies'
                ],
                'skills': ['React', 'TypeScript', 'Remote Work', 'Agile', 'English'],
                'posted_date': '1 week ago',
                'logo': '🌍',
                'apply_url': 'https://remote.co/remote-jobs/frontend-developer'
            }
        ],
        'Backend Developer': [
            {
                'title': 'Senior Backend Developer',
                'company': 'CloudTech Systems',
                'location': 'Seattle, WA',
                'type': 'Full-time',
                'experience': '5+ years',
                'salary': '$130k - $170k',
                'description': 'We are seeking a skilled Backend Developer to design and implement scalable server-side applications.',
                'requirements': [
                    'Strong experience with Python/Django',
                    'Experience with database design and optimization',
                    'Knowledge of cloud platforms (AWS, Azure)',
                    'Understanding of microservices architecture',
                    'Experience with RESTful API development'
                ],
                'skills': ['Python', 'Django', 'PostgreSQL', 'AWS', 'Docker'],
                'posted_date': '1 day ago',
                'logo': ''
            },
            {
                'title': 'Python Developer',
                'company': 'DataDriven Inc',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$95k - $135k',
                'description': 'Join our data-focused team to build robust backend systems and APIs that power our analytics platform.',
                'requirements': [
                    'Strong Python programming skills',
                    'Experience with Django or Flask',
                    'Knowledge of SQL and NoSQL databases',
                    'Understanding of data structures and algorithms',
                    'Experience with cloud services'
                ],
                'skills': ['Python', 'Django', 'Redis', 'PostgreSQL', 'AWS'],
                'posted_date': '4 days ago',
                'logo': ''
            },
            {
                'title': 'Backend Engineer',
                'company': 'FinTech Solutions',
                'location': 'Chicago, IL',
                'type': 'Full-time',
                'experience': '4-6 years',
                'salary': '$110k - $150k',
                'description': 'Build secure and scalable backend systems for our financial technology platform.',
                'requirements': [
                    'Experience with financial systems preferred',
                    'Strong knowledge of security best practices',
                    'Proficiency in Python and related frameworks',
                    'Experience with high-performance applications',
                    'Understanding of regulatory compliance'
                ],
                'skills': ['Python', 'Django', 'MySQL', 'Redis', 'Kubernetes'],
                'posted_date': '5 days ago',
                'logo': '💰'
            },
            {
                'title': 'API Developer',
                'company': 'ConnectSphere',
                'location': 'Denver, CO',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$90k - $125k',
                'description': 'Design and develop RESTful APIs that power our platform and integrate with third-party services.',
                'requirements': [
                    'Experience with API design and development',
                    'Strong knowledge of HTTP protocols',
                    'Understanding of authentication and security',
                    'Experience with API documentation tools',
                    'Knowledge of rate limiting and caching'
                ],
                'skills': ['REST APIs', 'PostgreSQL', 'Node.js', 'Docker', 'Swagger'],
                'posted_date': '3 days ago',
                'logo': '🔗'
            },
            {
                'title': 'Database Developer',
                'company': 'DataCore Systems',
                'location': 'Phoenix, AZ',
                'type': 'Full-time',
                'experience': '4+ years',
                'salary': '$100k - $140k',
                'description': 'Optimize and manage our database systems while developing data-driven applications.',
                'requirements': [
                    'Expert knowledge of SQL and database design',
                    'Experience with PostgreSQL, MySQL, or MongoDB',
                    'Understanding of database performance tuning',
                    'Knowledge of ETL processes',
                    'Experience with data modeling'
                ],
                'skills': ['SQL', 'PostgreSQL', 'MongoDB', 'ETL', 'Python'],
                'posted_date': '6 days ago',
                'logo': '🗄️'
            },
            {
                'title': 'Cloud Backend Developer',
                'company': 'SkyNet Technologies',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '5+ years',
                'salary': '$120k - $160k',
                'description': 'Build cloud-native backend services using modern technologies and DevOps practices.',
                'requirements': [
                    'Experience with cloud platforms (AWS, GCP, Azure)',
                    'Knowledge of containerization and orchestration',
                    'Understanding of microservices architecture',
                    'Experience with CI/CD pipelines',
                    'Strong programming skills in Python or Go'
                ],
                'skills': ['AWS', 'Kubernetes', 'Docker', 'Python', 'Go'],
                'posted_date': '2 weeks ago',
                'logo': '☁️'
            }
        ],
        'Full Stack Developer': [
            {
                'title': 'Full Stack Developer',
                'company': 'TechGrowth Labs',
                'location': 'Austin, TX',
                'type': 'Full-time',
                'experience': '4-6 years',
                'salary': '$100k - $140k',
                'description': 'Looking for versatile developers who can work across the entire stack and deliver end-to-end solutions.',
                'requirements': [
                    'Full-stack development experience',
                    'Strong frontend and backend skills',
                    'Experience with database design',
                    'Knowledge of cloud deployment',
                    'Understanding of DevOps practices'
                ],
                'skills': ['React', 'Node.js', 'Python', 'AWS', 'Docker'],
                'posted_date': '2 days ago',
                'logo': ''
            },
            {
                'title': 'Senior Full Stack Engineer',
                'company': 'Enterprise Solutions Co',
                'location': 'Boston, MA',
                'type': 'Full-time',
                'experience': '6+ years',
                'salary': '$130k - $180k',
                'description': 'Lead the development of our enterprise applications and mentor junior developers.',
                'requirements': [
                    '8+ years of software development experience',
                    'Expertise in multiple programming languages',
                    'Experience with system architecture',
                    'Strong leadership and communication skills',
                    'Knowledge of agile methodologies'
                ],
                'skills': ['React', 'Java', 'Spring Boot', 'PostgreSQL', 'Azure'],
                'posted_date': '1 week ago',
                'logo': ''
            },
            {
                'title': 'Full Stack Developer',
                'company': 'StartupForge',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$85k - $125k',
                'description': 'Join our fast-growing startup and help build innovative products from the ground up.',
                'requirements': [
                    'Experience with modern web frameworks',
                    'Ability to work independently',
                    'Strong problem-solving skills',
                    'Experience with agile development',
                    'Good communication skills'
                ],
                'skills': ['Vue.js', 'Express.js', 'MongoDB', 'Heroku', 'Git'],
                'posted_date': '6 days ago',
                'logo': ''
            }
        ],
        'Web Developer': [
            {
                'title': 'Full Stack Web Developer',
                'company': 'Digital Agency Pro',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$80k - $120k',
                'description': 'Create amazing websites and web applications for our diverse client base.',
                'requirements': [
                    'Strong web development skills',
                    'Experience with modern frameworks',
                    'Understanding of responsive design',
                    'Knowledge of SEO best practices',
                    'Good communication with clients'
                ],
                'skills': ['React', 'Node.js', 'CSS3', 'JavaScript', 'SEO'],
                'posted_date': '2 days ago',
                'logo': '🌐',
                'apply_url': 'https://www.linkedin.com/jobs/view/full-stack-developer-at-google-3984721'
            },
            {
                'title': 'WordPress Developer',
                'company': 'WP Masters',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '2-4 years',
                'salary': '$65k - $95k',
                'description': 'Develop custom WordPress themes and plugins for our clients.',
                'requirements': [
                    'Deep knowledge of WordPress',
                    'Experience with PHP and MySQL',
                    'Understanding of WordPress hooks and filters',
                    'Knowledge of page builders',
                    'Frontend development skills'
                ],
                'skills': ['WordPress', 'PHP', 'MySQL', 'CSS', 'JavaScript'],
                'posted_date': '4 days ago',
                'logo': '📝',
                'apply_url': 'https://www.indeed.com/jobs?q=wordpress+developer&vjk=2h9e4d5b6c7f8h9i'
            },
            {
                'title': 'Web Application Developer',
                'company': 'AppWorks Studio',
                'location': 'Miami, FL',
                'type': 'Full-time',
                'experience': '3-6 years',
                'salary': '$85k - $125k',
                'description': 'Build interactive web applications with modern JavaScript frameworks.',
                'requirements': [
                    'Experience with modern JavaScript frameworks',
                    'Understanding of web application architecture',
                    'Knowledge of API integration',
                    'Frontend and backend development skills',
                    'Experience with testing frameworks'
                ],
                'skills': ['React', 'Vue.js', 'Node.js', 'MongoDB', 'Jest'],
                'posted_date': '5 days ago',
                'logo': '⚙️',
                'apply_url': 'https://www.indeed.com/jobs?q=web+application+developer&l=Miami%2C+FL'
            },
            {
                'title': 'E-commerce Web Developer',
                'company': 'RetailTech Solutions',
                'location': 'Chicago, IL',
                'type': 'Full-time',
                'experience': '4+ years',
                'salary': '$90k - $130k',
                'description': 'Develop and maintain e-commerce websites using various platforms.',
                'requirements': [
                    'Experience with Shopify, Magento, or WooCommerce',
                    'Understanding of e-commerce workflows',
                    'Knowledge of payment integration',
                    'Frontend development expertise',
                    'SEO and conversion optimization'
                ],
                'skills': ['Shopify', 'PHP', 'JavaScript', 'CSS', 'SEO'],
                'posted_date': '1 week ago',
                'logo': '🏪',
                'apply_url': 'https://www.shopify.com/careers'
            },
            {
                'title': 'Web Developer - Marketing Focus',
                'company': 'GrowthHackers Inc',
                'location': 'Los Angeles, CA',
                'type': 'Full-time',
                'experience': '2-5 years',
                'salary': '$75k - $110k',
                'description': 'Build landing pages and marketing websites that drive conversions.',
                'requirements': [
                    'Strong frontend development skills',
                    'Understanding of marketing principles',
                    'Experience with A/B testing tools',
                    'Knowledge of analytics and tracking',
                    'Creative problem-solving abilities'
                ],
                'skills': ['HTML', 'CSS', 'JavaScript', 'Google Analytics', 'SEO'],
                'posted_date': '3 days ago',
                'logo': '📈',
                'apply_url': 'https://www.growthhackers.com/jobs'
            },
            {
                'title': 'Full Stack Web Developer',
                'company': 'TechStart Solutions',
                'location': 'Austin, TX',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$85k - $120k',
                'description': 'Join our startup to build innovative web applications from scratch.',
                'requirements': [
                    'Experience with full-stack development',
                    'Ability to work in fast-paced environment',
                    'Strong problem-solving skills',
                    'Knowledge of modern web technologies',
                    'Experience with agile development'
                ],
                'skills': ['React', 'Python', 'PostgreSQL', 'Docker', 'Git'],
                'posted_date': '6 days ago',
                'logo': '🚀',
                'apply_url': 'https://www.builtinaustin.com/jobs'
            }
        ],
        'Data Scientist': [
            {
                'title': 'Data Scientist',
                'company': 'AI Analytics Inc',
                'location': 'San Francisco, CA',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$120k - $160k',
                'description': 'Apply machine learning and statistical analysis to solve complex business problems.',
                'requirements': [
                    'Strong background in statistics and mathematics',
                    'Experience with machine learning frameworks',
                    'Proficiency in Python or R',
                    'Knowledge of data visualization tools',
                    'Experience with big data technologies'
                ],
                'skills': ['Python', 'TensorFlow', 'Pandas', 'SQL', 'Tableau'],
                'posted_date': '1 week ago',
                'logo': '',
                'apply_url': 'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4012389'
            },
            {
                'title': 'Senior Data Scientist',
                'company': 'Predictive Insights',
                'location': 'New York, NY',
                'type': 'Full-time',
                'experience': '5+ years',
                'salary': '$140k - $190k',
                'description': 'Lead data science projects and develop innovative ML solutions for enterprise clients.',
                'requirements': [
                    'Advanced degree in quantitative field',
                    'Experience with deep learning',
                    'Strong programming skills',
                    'Business acumen and communication skills',
                    'Publication record preferred'
                ],
                'skills': ['Python', 'PyTorch', 'Scikit-learn', 'AWS', 'Docker'],
                'posted_date': '1 week ago',
                'logo': '',
                'apply_url': 'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4012345'
            }
        ],
        'DevOps Engineer': [
            {
                'title': 'DevOps Engineer',
                'company': 'CloudOps Solutions',
                'location': 'Remote',
                'type': 'Full-time',
                'experience': '3-5 years',
                'salary': '$110k - $150k',
                'description': 'Build and maintain CI/CD pipelines and cloud infrastructure for our growing platform.',
                'requirements': [
                    'Experience with cloud platforms (AWS, Azure, GCP)',
                    'Knowledge of containerization technologies',
                    'Understanding of infrastructure as code',
                    'Experience with monitoring and logging',
                    'Strong scripting skills'
                ],
                'skills': ['AWS', 'Docker', 'Kubernetes', 'Jenkins', 'Terraform'],
                'posted_date': '2 days ago',
                'logo': ''
            },
            {
                'title': 'Senior DevOps Engineer',
                'company': 'ScaleTech Systems',
                'location': 'Seattle, WA',
                'type': 'Full-time',
                'experience': '5+ years',
                'salary': '$130k - $170k',
                'description': 'Lead our DevOps initiatives and design scalable infrastructure solutions.',
                'requirements': [
                    'Extensive cloud infrastructure experience',
                    'Expertise in automation and orchestration',
                    'Strong security knowledge',
                    'Experience with microservices',
                    'Leadership and mentoring skills'
                ],
                'skills': ['Kubernetes', 'AWS', 'Ansible', 'Prometheus', 'GitLab'],
                'posted_date': '4 days ago',
                'logo': ''
            }
        ]
    }
    
    # Default job postings for roles not specifically listed
    default_jobs = [
        {
            'title': 'Software Developer',
            'company': 'Tech Company',
            'location': 'Remote',
            'type': 'Full-time',
            'experience': '2-4 years',
            'salary': '$80k - $120k',
            'description': 'Join our team to build innovative software solutions.',
            'requirements': [
                'Programming experience',
                'Problem-solving skills',
                'Team collaboration',
                'Continuous learning mindset'
            ],
            'skills': ['JavaScript', 'Python', 'Git', 'SQL', 'Agile'],
            'posted_date': '1 week ago',
            'logo': '',
            'apply_url': 'https://www.linkedin.com/jobs/view/software-developer-at-amazon-4012389'
        },
        {
            'title': 'Junior Developer',
            'company': 'StartUp Inc',
            'location': 'San Francisco, CA',
            'type': 'Full-time',
            'experience': '0-2 years',
            'salary': '$60k - $85k',
            'description': 'Looking for passionate junior developers to join our growing team.',
            'requirements': [
                'Basic programming knowledge',
                'Eagerness to learn',
                'Good communication skills',
                'Team player attitude'
            ],
            'skills': ['JavaScript', 'HTML', 'CSS', 'Git', 'Learning'],
            'posted_date': '3 days ago',
            'logo': '🌱',
            'apply_url': 'https://www.angel.co/jobs/junior-developer'
        },
        {
            'title': 'Software Engineer',
            'company': 'Enterprise Corp',
            'location': 'New York, NY',
            'type': 'Full-time',
            'experience': '3-5 years',
            'salary': '$95k - $135k',
            'description': 'Develop enterprise software solutions for Fortune 500 companies.',
            'requirements': [
                'Software engineering experience',
                'Database knowledge',
                'System design understanding',
                'Professional communication'
            ],
            'skills': ['Java', 'Spring', 'SQL', 'AWS', 'Agile'],
            'posted_date': '4 days ago',
            'logo': '🏢',
            'apply_url': 'https://www.indeed.com/jobs?q=software+engineer&l=New+York%2C+NY'
        },
        {
            'title': 'Full Stack Developer',
            'company': 'Innovation Labs',
            'location': 'Remote',
            'type': 'Full-time',
            'experience': '3-6 years',
            'salary': '$90k - $130k',
            'description': 'Build end-to-end web applications using modern technologies.',
            'requirements': [
                'Full-stack development experience',
                'Modern framework knowledge',
                'Database design skills',
                'Cloud deployment experience'
            ],
            'skills': ['React', 'Node.js', 'Python', 'AWS', 'Docker'],
            'posted_date': '5 days ago',
            'logo': '🚀',
            'apply_url': 'https://stackoverflow.com/jobs/developer-jobs'
        },
        {
            'title': 'Frontend Developer',
            'company': 'Design First Agency',
            'location': 'Los Angeles, CA',
            'type': 'Full-time',
            'experience': '2-4 years',
            'salary': '$75k - $110k',
            'description': 'Create beautiful, responsive user interfaces for client projects.',
            'requirements': [
                'Strong HTML/CSS/JavaScript skills',
                'Modern framework experience',
                'Design sensibility',
                'Cross-browser compatibility knowledge'
            ],
            'skills': ['React', 'CSS3', 'JavaScript', 'UI/UX', 'Responsive'],
            'posted_date': '6 days ago',
            'logo': '🎨',
            'apply_url': 'https://www.dribbble.com/jobs/frontend-developer'
        },
        {
            'title': 'Backend Developer',
            'company': 'Data Systems Pro',
            'location': 'Chicago, IL',
            'type': 'Full-time',
            'experience': '3-5 years',
            'salary': '$85k - $125k',
            'description': 'Develop robust backend systems and APIs for data-driven applications.',
            'requirements': [
                'Server-side development experience',
                'Database expertise',
                'API design knowledge',
                'Security best practices'
            ],
            'skills': ['Python', 'Django', 'PostgreSQL', 'REST APIs', 'Security'],
            'posted_date': '1 week ago',
            'logo': '⚙️',
            'apply_url': 'https://www.glassdoor.com/job-listing/backend-developer'
        }
    ]
    
    return job_db.get(role_name, default_jobs)
