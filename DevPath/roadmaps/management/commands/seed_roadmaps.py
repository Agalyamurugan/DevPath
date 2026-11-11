from django.core.management.base import BaseCommand
from django.db import transaction

from roadmaps.models import (
    CertificationRecommendation,
    CourseRecommendation,
    CourseResource,
    LevelQuiz,
    Role,
    RoadmapStep,
    StepResource,
    UserLevelQuiz,
)
from roadmaps.seed_data import SEED_ROLES


def upsert_role(role_payload: dict) -> Role:
    role, _ = Role.objects.update_or_create(
        slug=role_payload["slug"],
        defaults={
            "name": role_payload["name"],
            "summary": role_payload.get("summary", ""),
            "description": role_payload.get("description", ""),
        },
    )
    return role


def upsert_resource(resource_payload: dict) -> CourseResource:
    # Unique constraint is (resource_type, url), so that defines idempotency.
    resource, _ = CourseResource.objects.update_or_create(
        resource_type=resource_payload["resource_type"],
        url=resource_payload["url"],
        defaults={
            "title": resource_payload["title"],
            "estimated_minutes": resource_payload.get("estimated_minutes"),
        },
    )
    return resource


def upsert_course_recommendation(step, rec_payload: dict):
    """Create or update a course recommendation"""
    recommendation, _ = CourseRecommendation.objects.update_or_create(
        step=step,
        url=rec_payload["url"],
        defaults={
            "platform": rec_payload["platform"],
            "title": rec_payload["title"],
            "description": rec_payload["description"],
            "difficulty_level": rec_payload.get("difficulty_level", ""),
            "duration": rec_payload.get("duration", ""),
            "rating": rec_payload.get("rating"),
            "is_paid": rec_payload.get("is_paid", False),
            "price": rec_payload.get("price", ""),
            "instructor": rec_payload.get("instructor", ""),
            "order": rec_payload.get("order", 0),
        },
    )
    return recommendation


def upsert_certification_recommendation(role, cert_payload: dict):
    """Create or update a certification recommendation"""
    certification, _ = CertificationRecommendation.objects.update_or_create(
        role=role,
        url=cert_payload["url"],
        defaults={
            "platform": cert_payload["platform"],
            "title": cert_payload["title"],
            "description": cert_payload["description"],
            "difficulty_level": cert_payload.get("difficulty_level", ""),
            "duration": cert_payload.get("duration", ""),
            "rating": cert_payload.get("rating"),
            "is_paid": cert_payload.get("is_paid", False),
            "price": cert_payload.get("price", ""),
            "provider": cert_payload.get("provider", ""),
            "prerequisites": cert_payload.get("prerequisites", ""),
            "order": cert_payload.get("order", 0),
        },
    )
    return certification


def upsert_level_quiz(role, quiz_payload: dict):
    """Create or update a level quiz"""
    quiz, _ = LevelQuiz.objects.update_or_create(
        role=role,
        level=quiz_payload["level"],
        defaults={
            "title": quiz_payload["title"],
            "description": quiz_payload.get("description", ""),
            "passing_score": quiz_payload.get("passing_score", 70),
            "order": quiz_payload.get("order", 0),
        },
    )
    return quiz


def upsert_user_level_quiz(user, role, quiz_payload: dict):
    """Create or update a user level quiz completion"""
    quiz = LevelQuiz.objects.get(role=role, level=quiz_payload["level"])
    UserLevelQuiz.objects.update_or_create(
        user=user,
        level_quiz=quiz,
        defaults={
            "score": 0,  # Will be updated when user takes quiz
            "passed": False,
        },
    )
    return quiz


class Command(BaseCommand):
    help = "Seed initial roles/roadmaps/resources for the gamified course recommendation system."

    @transaction.atomic
    def handle(self, *args, **options):
        seeded_roles = 0
        seeded_steps = 0
        seeded_resources = 0
        seeded_links = 0
        seeded_recommendations = 0
        seeded_certifications = 0

        seeded_level_quizzes = 0

        for role_payload in SEED_ROLES:
            role = upsert_role(role_payload)
            seeded_roles += 1

            for step_payload in role_payload["steps"]:
                step, _ = RoadmapStep.objects.update_or_create(
                    role=role,
                    level=step_payload["level"],
                    order=step_payload["order"],
                    defaults={
                        "title": step_payload["title"],
                        "description": step_payload.get("description", ""),
                    },
                )
                seeded_steps += 1
                
                # Create required resources for this step
                required_resources = step_payload.get("required_resources", [])
                for resource_payload in required_resources:
                    resource = upsert_resource(resource_payload)
                    StepResource.objects.update_or_create(
                        step=step,
                        resource=resource,
                        is_required=True,
                        defaults={
                            "order": resource_payload.get("order", 0),
                        }
                    )
                    seeded_resources += 1

            # Seed level quizzes for this role (outside the step loop)
            level_quizzes = role_payload.get("level_quizzes", [])
            for quiz_payload in level_quizzes:
                upsert_level_quiz(role, quiz_payload)
                seeded_level_quizzes += 1

            # Seed course recommendations for the role
            course_recommendations = role_payload.get("course_recommendations", [])
            for course_payload in course_recommendations:
                upsert_course_recommendation(role, course_payload)
                seeded_recommendations += 1

            # Seed certification recommendations for the role
            certification_recommendations = role_payload.get("certification_recommendations", [])
            for cert_payload in certification_recommendations:
                upsert_certification_recommendation(role, cert_payload)
                seeded_certifications += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded roles={seeded_roles}, steps={seeded_steps}, resources={seeded_resources}, links={seeded_links}, recommendations={seeded_recommendations}, certifications={seeded_certifications}, level_quizzes={seeded_level_quizzes}"
            )
        )
