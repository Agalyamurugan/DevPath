from django.urls import path

from . import views
from . import practice_quiz_views as quiz_views

urlpatterns = [
    path('', views.index, name='home'),
    path('choose-role/', views.role_select, name='role_select'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complete/<int:resource_id>/', views.complete_resource, name='complete_resource'),
    path('assessments/step/<int:step_id>/', views.assessment_list, name='assessment_list'),
    path('assessments/take/<int:assessment_id>/', views.take_assessment, name='take_assessment'),
    path('assessments/result/<int:assessment_id>/', views.assessment_result, name='assessment_result'),
    path('badges-and-certificates/', views.badges_and_certificates, name='badges_and_certificates'),
    path('quiz/level/<str:level>/', views.quiz_list, name='quiz_list'),
    path('quiz/take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('quiz/result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    path('test-db-quiz/', views.test_db_quiz, name='test_db_quiz'),
    path('chatbot/', views.chatbot_api, name='chatbot_api'),
    
    # New hub pages
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('practice/', views.practice_hub, name='practice_hub'),
    path('build/', views.build_hub, name='build_hub'),
    
    # Practice quiz system
    path('practice-quiz/', quiz_views.practice_quiz_hub, name='practice_quiz_hub'),
    path('practice-quiz/<str:role>/<str:level>/', quiz_views.take_practice_quiz, name='take_practice_quiz'),
    path('submit-practice-quiz/', quiz_views.submit_practice_quiz, name='submit_practice_quiz'),
]

