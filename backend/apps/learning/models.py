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
