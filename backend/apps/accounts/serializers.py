from django.contrib.auth import password_validation
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

from .models import Invitation, StudentProfile, TeacherProfile, User
from .services import hash_secret

INVITABLE_ROLE_CHOICES = (
    (User.Role.STUDENT, User.Role.STUDENT.label),
    (User.Role.TEACHER, User.Role.TEACHER.label),
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "role")
        read_only_fields = fields


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(trim_whitespace=False, write_only=True)


class InvitationCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=INVITABLE_ROLE_CHOICES)

    def validate_email(self, value):
        email = User.objects.normalize_email(value).lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Já existe uma conta com este e-mail.")
        return email


class InvitationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="recipient_email")

    class Meta:
        model = Invitation
        fields = ("id", "email", "role", "expires_at", "used_at", "created_at")
        read_only_fields = fields


class InvitationAcceptSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=150)
    password = serializers.CharField(trim_whitespace=False, write_only=True)

    def validate(self, attrs):
        invitation = Invitation.objects.filter(token_hash=hash_secret(attrs["token"])).first()
        if (
            invitation is None
            or invitation.used_at is not None
            or invitation.expires_at <= timezone.now()
        ):
            raise serializers.ValidationError(
                {"token": "Este convite é inválido, expirou ou já foi usado."}
            )
        if User.objects.filter(email__iexact=invitation.recipient_email).exists():
            raise serializers.ValidationError(
                {"token": "Este convite não pode mais ser usado."}
            )
        candidate = User(
            email=invitation.recipient_email,
            name=attrs["name"],
            role=invitation.role,
        )
        try:
            password_validation.validate_password(attrs["password"], candidate)
        except DjangoValidationError as exc:
            raise serializers.ValidationError({"password": list(exc.messages)}) from exc
        attrs["invitation"] = invitation
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        invitation = Invitation.objects.select_for_update().get(
            pk=validated_data["invitation"].pk
        )
        if invitation.used_at is not None or invitation.expires_at <= timezone.now():
            raise serializers.ValidationError(
                {"token": "Este convite é inválido, expirou ou já foi usado."}
            )
        user = User.objects.create_user(
            email=invitation.recipient_email,
            name=validated_data["name"],
            role=invitation.role,
            password=validated_data["password"],
        )
        if user.role == User.Role.STUDENT:
            StudentProfile.objects.create(user=user)
        elif user.role == User.Role.TEACHER:
            TeacherProfile.objects.create(user=user)
        invitation.used_at = timezone.now()
        invitation.save(update_fields=("used_at",))
        return user


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)
    password = serializers.CharField(trim_whitespace=False, write_only=True)

    def validate(self, attrs):
        try:
            user_id = force_str(urlsafe_base64_decode(attrs["uid"]))
            user = User.objects.get(pk=user_id, is_active=True)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is None or not default_token_generator.check_token(user, attrs["token"]):
            raise serializers.ValidationError(
                {"token": "Este link de redefinição é inválido ou expirou."}
            )
        try:
            password_validation.validate_password(attrs["password"], user)
        except DjangoValidationError as exc:
            raise serializers.ValidationError({"password": list(exc.messages)}) from exc
        attrs["user"] = user
        return attrs

    def save(self):
        user = self.validated_data["user"]
        user.set_password(self.validated_data["password"])
        user.save(update_fields=("password",))
        return user
