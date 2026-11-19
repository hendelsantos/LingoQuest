import uuid

from django.conf import settings
from django.db import models


class XPEvent(models.Model):
    class SourceType(models.TextChoices):
        LESSON_COMPLETION = "LESSON_COMPLETION", "Conclusão de missão"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="xp_events",
    )
    source_type = models.CharField(max_length=32, choices=SourceType.choices)
    source_id = models.CharField(max_length=64)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("student", "source_type", "source_id"),
                name="xp_event_student_source_unique",
            ),
            models.CheckConstraint(
                condition=models.Q(amount__gt=0),
                name="xp_event_amount_positive",
            ),
        ]
        indexes = [models.Index(fields=("student", "created_at"))]

    def __str__(self):
        return f"{self.student.email} · +{self.amount} XP"
