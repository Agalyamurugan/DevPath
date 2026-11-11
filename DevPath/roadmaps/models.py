from django.conf import settings
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    # Used when user says they “don’t know” what they want to become.
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class RoadmapStep(models.Model):
    LEVEL_BEGINNER = 'Beginner'
    LEVEL_INTERMEDIATE = 'Intermediate'
    LEVEL_ADVANCED = 'Advanced'

    LEVEL_CHOICES = [
        (LEVEL_BEGINNER, LEVEL_BEGINNER),
        (LEVEL_INTERMEDIATE, LEVEL_INTERMEDIATE),
        (LEVEL_ADVANCED, LEVEL_ADVANCED),
    ]

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='steps')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, db_index=True)

    # Controls progression order within the role.
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['role', 'order'], name='unique_step_order_per_role'),
        ]
        ordering = ['role_id', 'order']

    def __str__(self) -> str:
        return f'{self.role.name} - {self.level} - {self.title}'


class CourseResource(models.Model):
    RESOURCE_YOUTUBE = 'youtube'
    RESOURCE_DOCS = 'docs'
    RESOURCE_ARTICLE = 'article'
    RESOURCE_COURSE = 'course'
    
    RESOURCE_CHOICES = [
        (RESOURCE_YOUTUBE, 'YouTube'),
        (RESOURCE_DOCS, 'Documentation'),
        (RESOURCE_ARTICLE, 'Article'),
        (RESOURCE_COURSE, 'Course'),
    ]
    
    resource_type = models.CharField(max_length=20, choices=RESOURCE_CHOICES)
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    estimated_minutes = models.PositiveIntegerField(help_text="Estimated time to complete this resource", default=0)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title


class LevelQuiz(models.Model):
    """Quiz that must be completed to progress to next level"""
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='level_quizzes')
    level = models.CharField(max_length=20, choices=RoadmapStep.LEVEL_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    passing_score = models.PositiveIntegerField(default=70, help_text="Minimum score to pass the quiz")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
        unique_together = ['role', 'level']
    
    def __str__(self) -> str:
        return f'{self.role.name} - {self.level} Quiz'


class UserLevelQuiz(models.Model):
    """Track user completion of level quizzes"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level_quiz = models.ForeignKey(LevelQuiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    passed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'level_quiz']

    def __str__(self) -> str:
        return f'{self.user.username} - {self.level_quiz.title}'


class StepResource(models.Model):
    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE, related_name='step_resources')
    resource = models.ForeignKey(CourseResource, on_delete=models.CASCADE, related_name='+')

    is_required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['step', 'resource'], name='unique_step_resource'),
        ]
        ordering = ['step_id', 'order']

    def __str__(self) -> str:
        return f'{self.step.title} -> {self.resource.title}'


class UserRoleSelection(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='role_selection')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    selected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} -> {self.role}'


class UserResourceCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resource_completions')
    resource = models.ForeignKey(CourseResource, on_delete=models.CASCADE, related_name='completions')
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'resource'], name='unique_user_resource_completion'),
        ]

    def __str__(self) -> str:
        return f'{self.user} completed {self.resource}'


class UserStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stats')
    total_points = models.PositiveIntegerField(default=0)
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_completion_date = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.total_points} points, {self.current_streak} streak'


class Assessment(models.Model):
    ASSESSMENT_TYPE_QUIZ = 'quiz'
    ASSESSMENT_TYPE_PROJECT = 'project'
    ASSESSMENT_TYPE_CERTIFICATION = 'certification'
    
    ASSESSMENT_TYPE_CHOICES = [
        (ASSESSMENT_TYPE_QUIZ, 'Quiz'),
        (ASSESSMENT_TYPE_PROJECT, 'Project'),
        (ASSESSMENT_TYPE_CERTIFICATION, 'Certification'),
    ]
    
    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPE_CHOICES, default=ASSESSMENT_TYPE_QUIZ)
    passing_score = models.PositiveIntegerField(default=70)  # percentage
    time_limit_minutes = models.PositiveIntegerField(null=True, blank=True)
    badge_name = models.CharField(max_length=100, blank=True)
    certificate_title = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['step__order', 'id']
    
    def __str__(self) -> str:
        return f'{self.step.title} - {self.title}'


class Question(models.Model):
    QUESTION_TYPE_MULTIPLE_CHOICE = 'multiple_choice'
    QUESTION_TYPE_TRUE_FALSE = 'true_false'
    QUESTION_TYPE_SHORT_ANSWER = 'short_answer'
    
    QUESTION_TYPE_CHOICES = [
        (QUESTION_TYPE_MULTIPLE_CHOICE, 'Multiple Choice'),
        (QUESTION_TYPE_TRUE_FALSE, 'True/False'),
        (QUESTION_TYPE_SHORT_ANSWER, 'Short Answer'),
    ]
    
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default=QUESTION_TYPE_MULTIPLE_CHOICE)
    points = models.PositiveIntegerField(default=1)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self) -> str:
        return f'Question {self.order}: {self.question_text[:50]}...'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self) -> str:
        return f'{self.choice_text} ({'Correct' if self.is_correct else 'Incorrect'})'


class UserAssessment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assessments')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='user_assessments')
    score = models.PositiveIntegerField()  # percentage
    passed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)
    time_taken_minutes = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'assessment'], name='unique_user_assessment'),
        ]
        ordering = ['-completed_at']
    
    def __str__(self) -> str:
        return f'{self.user} - {self.assessment} - {self.score}%'


class Badge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='badges')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='badges')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-earned_at']
        constraints = [
            models.UniqueConstraint(fields=['user', 'assessment'], name='unique_user_badge'),
        ]
    
    def __str__(self) -> str:
        return f'{self.user} - {self.name}'


class Certificate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certificates')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    certificate_id = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['-issued_date']
        constraints = [
            models.UniqueConstraint(fields=['user', 'assessment'], name='unique_user_certificate'),
        ]
    
    def __str__(self) -> str:
        return f'{self.user} - {self.title}'


class CertificationRecommendation(models.Model):
    PLATFORM_GOOGLE = 'google'
    PLATFORM_MICROSOFT = 'microsoft'
    PLATFORM_AWS = 'aws'
    PLATFORM_AZURE = 'azure'
    PLATFORM_COMPTIA = 'comptia'
    PLATFORM_CISCO = 'cisco'
    PLATFORM_ORACLE = 'oracle'
    PLATFORM_OTHER = 'other'
    
    PLATFORM_CHOICES = [
        (PLATFORM_GOOGLE, 'Google'),
        (PLATFORM_MICROSOFT, 'Microsoft'),
        (PLATFORM_AWS, 'AWS'),
        (PLATFORM_AZURE, 'Azure'),
        (PLATFORM_COMPTIA, 'CompTIA'),
        (PLATFORM_CISCO, 'Cisco'),
        (PLATFORM_ORACLE, 'Oracle'),
        (PLATFORM_OTHER, 'Other'),
    ]
    
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='certification_recommendations')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=500)
    difficulty_level = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    price = models.CharField(max_length=50, blank=True)
    provider = models.CharField(max_length=100, blank=True)
    prerequisites = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self) -> str:
        return f'{self.role.name} - {self.title}'


class CourseRecommendation(models.Model):
    PLATFORM_NASSCOM = 'nasscom'
    PLATFORM_UDEMY = 'udemy'
    PLATFORM_COURSERA = 'coursera'
    PLATFORM_OTHER = 'other'
    
    PLATFORM_CHOICES = [
        (PLATFORM_NASSCOM, 'NASSCOM'),
        (PLATFORM_UDEMY, 'Udemy'),
        (PLATFORM_COURSERA, 'Coursera'),
        (PLATFORM_OTHER, 'Other'),
    ]
    
    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE, related_name='course_recommendations')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=500)
    difficulty_level = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    price = models.CharField(max_length=50, blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self) -> str:
        return f'{self.step.title} - {self.title}'


class CompletedRole(models.Model):
    """Track which roles a user has completed"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='completed_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='completed_by_users')
    completed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'role']
        ordering = ['-completed_at']
