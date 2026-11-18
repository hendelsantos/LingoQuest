"""Sincroniza o currículo definido em ``apps.learning.content`` com o banco.

O seed é idempotente: unidades e lições são atualizadas por identidade
estável (título/slug), perguntas são recriadas a cada execução e o que
saiu do catálogo é removido. Posições são "estacionadas" em valores altos
antes da reatribuição para evitar conflitos de unicidade transitórios.
"""

import re

from django.db import transaction

from .content import load_catalog
from .models import Choice, Course, Lesson, Question, Unit

# Posições temporárias altas para liberar as posições finais durante a sincronização.
TEMP_POSITION = 20_000


def _strip_final_punctuation(word: str) -> str:
    return re.sub(r"[.?!]+$", "", word)


def _scramble_tokens(sentence: str) -> list[str]:
    """Gera o banco de palavras embaralhado de uma questão ORDERING."""
    words = [_strip_final_punctuation(word) for word in sentence.split() if word.strip()]
    if len(words) < 2:
        return words
    pivot = len(words) // 2
    tokens = words[pivot:] + words[:pivot]
    if tokens == words:
        tokens = list(reversed(words))
    return tokens


def _park_positions(queryset) -> None:
    for index, obj in enumerate(queryset):
        if obj.position < TEMP_POSITION:
            obj.position = TEMP_POSITION + index
            obj.save(update_fields=["position"])


def _delete_questions(lesson: Lesson) -> None:
    """Remove o gabarito respeitando os FKs protegidos do domínio."""
    question_ids = list(lesson.questions.values_list("id", flat=True))
    if not question_ids:
        return
    # IDs materializados evitam que o PostgreSQL planeje um JOIN caro para cada lição.
    Choice.objects.filter(question_id__in=question_ids).delete()
    Question.objects.filter(id__in=question_ids).delete()


def _sync_lesson(unit: Unit, lesson_data: dict, position: int) -> None:
    lesson = unit.lessons.filter(slug=lesson_data["slug"]).first()
    if lesson is None:
        lesson = Lesson(unit=unit, slug=lesson_data["slug"], position=TEMP_POSITION)
    lesson.unit = unit
    lesson.title = lesson_data["title"]
    lesson.skill = lesson_data["skill"]
    lesson.summary = lesson_data["summary"]
    lesson.theory = lesson_data["theory"]
    lesson.example = lesson_data["example"]
    lesson.key_points = lesson_data["key_points"]
    lesson.dialogue = lesson_data.get("dialogue", [])
    lesson.pedagogy = lesson_data.get("pedagogy", {})
    lesson.estimated_minutes = lesson_data.get("estimated_minutes", 8)
    lesson.position = position
    lesson.xp_reward = lesson_data.get("xp_reward", 60)
    lesson.passing_percent = lesson_data.get("passing_percent", 66)
    lesson.required = lesson_data.get("required", True)
    lesson.status = Lesson.Status.PUBLISHED
    lesson.save()

    # Perguntas não têm identidade estável: recria a cada sincronização.
    _delete_questions(lesson)
    for question_position, question_data in enumerate(lesson_data["questions"], start=1):
        _create_question(lesson, question_data, question_position)


def _create_question(lesson: Lesson, question_data: dict, position: int) -> None:
    question_type = question_data["type"]
    answer_data: dict = {}

    if question_type != Question.Type.MCQ:
        answer_data["correct"] = question_data["correct"]
        if question_data.get("accepted"):
            answer_data["accepted"] = question_data["accepted"]
        if question_type == Question.Type.ORDERING:
            answer_data["tokens"] = _scramble_tokens(question_data["correct"])

    question = Question.objects.create(
        lesson=lesson,
        type=question_type,
        prompt=question_data["prompt"],
        position=position,
        explanation=question_data["explanation"],
        weight=question_data.get("weight", 1),
        answer_data=answer_data,
    )

    if question_type == Question.Type.MCQ:
        choices = question_data["choices"]
        for choice_position, choice_text in enumerate(choices, start=1):
            Choice.objects.create(
                question=question,
                text=choice_text,
                position=choice_position,
                is_correct=choice_position - 1 == question_data["correct_index"],
            )


def _sync_unit(course: Course, unit_data: dict) -> None:
    unit = course.units.filter(title=unit_data["title"]).first()
    if unit is None:
        unit = Unit(course=course, title=unit_data["title"], position=TEMP_POSITION)
    unit.course = course
    unit.title = unit_data["title"]
    unit.description = unit_data["description"]
    unit.position = unit_data["position"]
    unit.save()

    _park_positions(unit.lessons.all())
    kept_lesson_ids = []
    for position, lesson_data in enumerate(unit_data["lessons"], start=1):
        _sync_lesson(unit, lesson_data, position)
        kept_lesson_ids.append(unit.lessons.get(slug=lesson_data["slug"]).id)

    for lesson in unit.lessons.exclude(id__in=kept_lesson_ids):
        _delete_questions(lesson)
        lesson.delete()


def _remove_stale_units(course: Course, kept_unit_ids: list[int]) -> None:
    for unit in course.units.exclude(id__in=kept_unit_ids):
        for lesson in unit.lessons.all():
            _delete_questions(lesson)
        unit.lessons.all().delete()
        unit.delete()


@transaction.atomic
def seed_curriculum() -> dict[str, int]:
    totals = {"courses": 0, "units": 0, "lessons": 0, "questions": 0, "choices": 0}

    for course_data, units_data in load_catalog():
        course, _ = Course.objects.update_or_create(
            slug=course_data["slug"],
            defaults={**course_data, "status": Course.Status.PUBLISHED},
        )
        totals["courses"] += 1

        _park_positions(course.units.all())
        kept_unit_ids = []
        for unit_data in units_data:
            _sync_unit(course, unit_data)
            kept_unit_ids.append(course.units.get(title=unit_data["title"]).id)
            totals["units"] += 1
            totals["lessons"] += len(unit_data["lessons"])
            totals["questions"] += sum(len(lesson["questions"]) for lesson in unit_data["lessons"])
            totals["choices"] += sum(
                len(question.get("choices", []))
                for lesson in unit_data["lessons"]
                for question in lesson["questions"]
            )

        _remove_stale_units(course, kept_unit_ids)

    return totals
