from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from django.db.models import Prefetch

from .models import CourseResource, RoadmapStep, StepResource, UserResourceCompletion, Role


@dataclass(frozen=True)
class Achievement:
    key: str
    title: str
    description: str
    unlocked: bool
    # Optional numeric progress (e.g. 1/5).
    progress_text: str = ""


def compute_required_resource_ids(role: Role) -> List[int]:
    return list(
        StepResource.objects.filter(step__role=role, is_required=True).values_list("resource_id", flat=True).distinct()
    )


def compute_step_completion_map(user, role: Role) -> Dict[int, bool]:
    """
    Returns: {roadmap_step_id: completed_bool}
    A step is completed when all required resources for that step are completed.
    """
    required_ids = set(compute_required_resource_ids(role))

    completed_required_resource_ids = set(
        UserResourceCompletion.objects.filter(user=user, resource_id__in=required_ids).values_list("resource_id", flat=True)
    )

    steps = (
        RoadmapStep.objects.filter(role=role)
        .order_by("order")
        .prefetch_related(
            Prefetch(
                "step_resources",
                queryset=StepResource.objects.filter(is_required=True).select_related("resource"),
                to_attr="required_resources",
            )
        )
    )

    completion = {}
    for step in steps:
        required_for_step = getattr(step, "required_resources", [])
        step_completed = all(sr.resource_id in completed_required_resource_ids for sr in required_for_step)
        completion[step.id] = step_completed

    return completion


def compute_achievements(user, role: Role) -> List[Achievement]:
    required_ids = set(compute_required_resource_ids(role))

    completed_required_resource_ids = set(
        UserResourceCompletion.objects.filter(user=user, resource_id__in=required_ids).values_list("resource_id", flat=True)
    )

    required_completed_count = len(completed_required_resource_ids)

    step_completion = compute_step_completion_map(user, role)

    steps = list(RoadmapStep.objects.filter(role=role).order_by("order"))
    completed_steps_count = sum(1 for s in steps if step_completion.get(s.id))

    beginner_steps = [s for s in steps if s.level == RoadmapStep.LEVEL_BEGINNER]
    beginner_completed = bool(beginner_steps) and all(step_completion.get(s.id) for s in beginner_steps)

    # Step chain = complete ALL steps in a row starting from the first step (by order).
    chain_len = 0
    for s in steps:
        if step_completion.get(s.id):
            chain_len += 1
        else:
            break
    total_steps = len(steps)
    step_chain_unlocked = chain_len >= total_steps

    achievements = [
        Achievement(
            key="first_resource",
            title="First Resource",
            description="Complete your first required learning resource for this role.",
            unlocked=required_completed_count >= 1,
            progress_text=f"{min(required_completed_count, 1)}/1",
        ),
        Achievement(
            key="first_step",
            title="First Step",
            description="Complete your first roadmap step.",
            unlocked=completed_steps_count >= 1,
            progress_text=f"{min(completed_steps_count, 1)}/1",
        ),
        Achievement(
            key="beginner_path",
            title="Beginner Path",
            description="Complete every Beginner step for this role.",
            unlocked=beginner_completed,
            progress_text=f"{'Done' if beginner_completed else 'In progress'}",
        ),
        Achievement(
            key="step_chain",
            title="Complete Path",
            description=f"Complete all {total_steps} steps in order.",
            unlocked=step_chain_unlocked,
            progress_text=f"{chain_len}/{total_steps}",
        ),
    ]

    return achievements

