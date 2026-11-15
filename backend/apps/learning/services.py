from django.db import transaction

from .catalog import COURSE, UNITS
from .models import Choice, Course, Lesson, Question, Unit


@transaction.atomic
def seed_a1_foundations() -> dict[str, int]:
    course, _ = Course.objects.update_or_create(
        slug=COURSE["slug"],
        defaults={
            **COURSE,
            "status": Course.Status.PUBLISHED,
            "version": 1,
        },
    )

    totals = {"courses": 1, "units": 0, "lessons": 0, "questions": 0, "choices": 0}
    for unit_data in UNITS:
        unit, _ = Unit.objects.update_or_create(
            course=course,
            position=unit_data["position"],
            defaults={
                "title": unit_data["title"],
                "description": unit_data["description"],
            },
        )
        totals["units"] += 1

        for lesson_position, lesson_data in enumerate(unit_data["lessons"], start=1):
            lesson, _ = Lesson.objects.update_or_create(
                unit=unit,
                slug=lesson_data["slug"],
                defaults={
                    "title": lesson_data["title"],
                    "skill": lesson_data["skill"],
                    "summary": lesson_data["summary"],
                    "theory": lesson_data["theory"],
                    "example": lesson_data["example"],
                    "key_points": lesson_data["key_points"],
                    "estimated_minutes": 8,
                    "position": lesson_position,
                    "xp_reward": 60,
                    "passing_percent": 66,
                    "required": True,
                    "status": Lesson.Status.PUBLISHED,
                },
            )
            totals["lessons"] += 1

            for question_position, question_data in enumerate(lesson_data["questions"], start=1):
                prompt, choices, correct_index, explanation = question_data
                question, _ = Question.objects.update_or_create(
                    lesson=lesson,
                    position=question_position,
                    defaults={
                        "type": Question.Type.MCQ,
                        "prompt": prompt,
                        "explanation": explanation,
                        "weight": 1,
                    },
                )
                totals["questions"] += 1

                for choice_position, choice_text in enumerate(choices, start=1):
                    Choice.objects.update_or_create(
                        question=question,
                        position=choice_position,
                        defaults={
                            "text": choice_text,
                            "is_correct": choice_position - 1 == correct_index,
                        },
                    )
                    totals["choices"] += 1

    return totals
