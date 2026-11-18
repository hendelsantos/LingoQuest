import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower

from .managers import UserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        TEACHER = "TEACHER", "Professor"
        STUDENT = "STUDENT", "Aluno"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField("e-mail", unique=True)
    name = models.CharField("nome", max_length=150)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STUDENT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(Lower("email"), name="accounts_user_email_ci_unique"),
        ]

    def save(self, *args, **kwargs):
        self.email = self.__class__.objects.normalize_email(self.email).lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class StudentProfile(models.Model):
    class Level(models.TextChoices):
        A1 = "A1", "A1"
        A2 = "A2", "A2"
        B1 = "B1", "B1"
        B2 = "B2", "B2"
        C1 = "C1", "C1"
        C2 = "C2", "C2"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    target_level = models.CharField(max_length=2, choices=Level.choices, blank=True)
    placement_level = models.CharField(max_length=2, choices=Level.choices, blank=True)
    timezone = models.CharField(max_length=64, default="America/Sao_Paulo")
    learning_goal = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.email}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
    )
    bio = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Perfil de {self.user.email}"


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient_email = models.EmailField("e-mail do convidado")
    role = models.CharField(max_length=10, choices=User.Role.choices)
    token_hash = models.CharField(max_length=64, unique=True, editable=False)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="sent_invitations",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [models.Index(fields=("recipient_email", "expires_at"))]

    def __str__(self):
        return f"{self.recipient_email} ({self.get_role_display()})"

    def save(self, *args, **kwargs):
        self.recipient_email = User.objects.normalize_email(self.recipient_email).lower()
        super().save(*args, **kwargs)

