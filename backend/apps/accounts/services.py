import hashlib
import secrets
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import Invitation, User

INVITATION_LIFETIME = timedelta(days=3)


def hash_secret(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def create_invitation(*, email: str, role: str, invited_by: User) -> Invitation:
    token = secrets.token_urlsafe(32)
    invitation = Invitation.objects.create(
        recipient_email=email,
        role=role,
        token_hash=hash_secret(token),
        expires_at=timezone.now() + INVITATION_LIFETIME,
        invited_by=invited_by,
    )
    accept_url = f"{settings.APP_BASE_URL}/accept-invitation?token={token}"
    send_mail(
        "Seu convite para a LingoQuest",
        (
            "Você recebeu um convite para a LingoQuest. "
            f"Defina sua senha em: {accept_url}\n\n"
            "O link é pessoal, expira em 3 dias e pode ser usado uma única vez."
        ),
        settings.DEFAULT_FROM_EMAIL,
        [invitation.recipient_email],
    )
    return invitation


def send_password_reset(user: User) -> None:
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    confirm_url = (
        f"{settings.APP_BASE_URL}/reset-password/confirm?uid={uid}&token={token}"
    )
    send_mail(
        "Redefinição de senha da LingoQuest",
        (
            "Recebemos um pedido para redefinir sua senha. "
            f"Continue em: {confirm_url}\n\n"
            "Se você não fez esse pedido, ignore esta mensagem."
        ),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )
