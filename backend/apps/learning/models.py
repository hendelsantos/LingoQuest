import uuid

from django.conf import settings
from django.db import models


class Course(models.Model):
    class Level(models.TextChoices):
        A1 = "A1", "A1"
        A2 = "A2", "A2"
        B1 = "B1", "B1"
        B2 = "B2", "B2"
        C1 = "C1", "C1"
        C2 = "C2", "C2"

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Rascunho"
        PUBLISHED = "PUBLISHED", "Publicado"
        ARCHIVED = "ARCHIVED", "Arquivado"

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=160)
    description = models.TextField()
    level = models.CharField(max_length=2, choices=Level.choices)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    version = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ("level", "title")

    def __str__(self):
        return self.title


class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="units")
    title = models.CharField(max_length=160)
    position = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("position",)
        constraints = [
            models.UniqueConstraint(
                fields=("course", "position"), name="unit_course_position_unique"
            ),
        ]

    def __str__(self):
        return f"{self.course.title} · {self.title}"


class Lesson(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Rascunho"
        PUBLISHED = "PUBLISHED", "Publicada"
        ARCHIVED = "ARCHIVED", "Arquivada"

    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name="lessons")
    slug = models.SlugField()
    title = models.CharField(max_length=160)
    skill = models.CharField(max_length=30)
    summary = models.CharField(max_length=240)
    theory = models.TextField()
    example = models.TextField()
    key_points = models.JSONField(default=list)
    dialogue = models.JSONField(default=list, blank=True)
    pedagogy = models.JSONField(default=dict, blank=True)
    estimated_minutes = models.PositiveSmallIntegerField(default=8)
    position = models.PositiveSmallIntegerField()
    xp_reward = models.PositiveSmallIntegerField(default=60)
    passing_percent = models.PositiveSmallIntegerField(default=66)
    required = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ("unit__position", "position")
        constraints = [
            models.UniqueConstraint(fields=("unit", "slug"), name="lesson_unit_slug_unique"),
            models.UniqueConstraint(
                fields=("unit", "position"), name="lesson_unit_position_unique"
            ),
            models.CheckConstraint(
                condition=models.Q(passing_percent__gte=0, passing_percent__lte=100),
                name="lesson_passing_percent_range",
            ),
        ]

    def __str__(self):
        return self.title


class Question(models.Model):
    class Type(models.TextChoices):
        MCQ = "MCQ", "Múltipla escolha"
        FILL_IN = "FILL_IN", "Completar lacuna"
        ORDERING = "ORDERING", "Ordenar palavras"
        LISTENING = "LISTENING", "Ditado"

    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT, related_name="questions")
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.MCQ)
    prompt = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField()
    explanation = models.CharField(max_length=300)
    weight = models.PositiveSmallIntegerField(default=1)
    answer_data = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("position",)
        constraints = [
            models.UniqueConstraint(
                fields=("lesson", "position"), name="question_lesson_position_unique"
            ),
            models.CheckConstraint(
                condition=models.Q(weight__gt=0), name="question_weight_positive"
            ),
        ]

    def __str__(self):
        return self.prompt


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="choices")
    text = models.CharField(max_length=240)
    position = models.PositiveSmallIntegerField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ("position",)
        constraints = [
            models.UniqueConstraint(
                fields=("question", "position"), name="choice_question_position_unique"
            ),
        ]

    def __str__(self):
        return self.text


class Enrollment(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Ativa"
        PAUSED = "PAUSED", "Pausada"
        COMPLETED = "COMPLETED", "Concluída"
        CANCELLED = "CANCELLED", "Cancelada"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="enrollments",
    )
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("-enrolled_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("student", "course"), name="enrollment_student_course_unique"
            ),
        ]
        indexes = [models.Index(fields=("student", "status"))]

    def __str__(self):
        return f"{self.student.email} · {self.course.title}"


class LessonAttempt(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "IN_PROGRESS", "Em andamento"
        SUBMITTED = "SUBMITTED", "Finalizada"
        ABANDONED = "ABANDONED", "Abandonada"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="lesson_attempts",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name="attempts",
    )
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.IN_PROGRESS,
    )
    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    correct_count = models.PositiveSmallIntegerField(default=0)
    total_questions = models.PositiveSmallIntegerField(default=0)
    score_percent = models.PositiveSmallIntegerField(default=0)
    passed = models.BooleanField(default=False)
    xp_awarded = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("-started_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("student", "lesson"),
                condition=models.Q(status="IN_PROGRESS"),
                name="attempt_one_in_progress_per_lesson",
            ),
            models.CheckConstraint(
                condition=models.Q(score_percent__gte=0, score_percent__lte=100),
                name="attempt_score_percent_range",
            ),
        ]
        indexes = [models.Index(fields=("student", "status", "started_at"))]

    def __str__(self):
        return f"{self.student.email} · {self.lesson.title} · {self.status}"


class AttemptAnswer(models.Model):
    attempt = models.ForeignKey(
        LessonAttempt,
        on_delete=models.PROTECT,
        related_name="answers",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.PROTECT,
        related_name="attempt_answers",
    )
    selected_choice = models.ForeignKey(
        Choice,
        on_delete=models.PROTECT,
        related_name="attempt_answers",
        null=True,
        blank=True,
    )
    response_data = models.JSONField(default=dict)
    feedback = models.JSONField(default=dict)
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("question__position",)
        constraints = [
            models.UniqueConstraint(
                fields=("attempt", "question"),
                name="attempt_answer_question_unique",
            ),
        ]

    def __str__(self):
        return f"{self.attempt_id} · questão {self.question_id}"


class LessonProgress(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="lesson_progress",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.PROTECT,
        related_name="student_progress",
    )
    best_score = models.PositiveSmallIntegerField(default=0)
    first_passed_at = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    last_attempt_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("student", "lesson"),
                name="lesson_progress_student_lesson_unique",
            ),
            models.CheckConstraint(
                condition=models.Q(best_score__gte=0, best_score__lte=100),
                name="lesson_progress_best_score_range",
            ),
        ]
        indexes = [models.Index(fields=("student", "completed", "last_attempt_at"))]

    def __str__(self):
        return f"{self.student.email} · {self.lesson.title} · {self.best_score}%"
