from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from .models import User
from .permissions import IsAdminRole
from .serializers import (
    InvitationAcceptSerializer,
    InvitationCreateSerializer,
    InvitationSerializer,
    LoginSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetRequestSerializer,
    UserSerializer,
)
from .services import create_invitation, send_password_reset


def auth_payload(request, user):
    return {"user": UserSerializer(user).data, "csrfToken": get_token(request)}


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CsrfTokenView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)

    @extend_schema(responses={200: dict})
    def get(self, request):
        return Response({"csrfToken": get_token(request)})


@method_decorator(csrf_protect, name="dispatch")
class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "login"

    @extend_schema(request=LoginSerializer, responses={200: UserSerializer})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = User.objects.normalize_email(serializer.validated_data["email"]).lower()
        user = authenticate(
            request,
            email=email,
            password=serializer.validated_data["password"],
        )
        if user is None:
            return Response(
                {"detail": "E-mail ou senha inválidos."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login(request, user)
        return Response(auth_payload(request, user))


@method_decorator(csrf_protect, name="dispatch")
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(request=None, responses={200: dict})
    def post(self, request):
        logout(request)
        return Response({"csrfToken": get_token(request)})


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses=UserSerializer)
    def get(self, request):
        return Response(UserSerializer(request.user).data)


@method_decorator(csrf_protect, name="dispatch")
class InvitationCreateView(APIView):
    permission_classes = (IsAdminRole,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "invitation"

    @extend_schema(request=InvitationCreateSerializer, responses={201: InvitationSerializer})
    def post(self, request):
        serializer = InvitationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invitation = create_invitation(
            email=serializer.validated_data["email"],
            role=serializer.validated_data["role"],
            invited_by=request.user,
        )
        return Response(InvitationSerializer(invitation).data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_protect, name="dispatch")
class InvitationAcceptView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "invitation_accept"

    @extend_schema(request=InvitationAcceptSerializer, responses={201: UserSerializer})
    def post(self, request):
        serializer = InvitationAcceptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)
        return Response(auth_payload(request, user), status=status.HTTP_201_CREATED)


@method_decorator(csrf_protect, name="dispatch")
class PasswordResetRequestView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "password_reset"

    @extend_schema(request=PasswordResetRequestSerializer, responses={200: dict})
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = User.objects.normalize_email(serializer.validated_data["email"]).lower()
        user = User.objects.filter(email__iexact=email, is_active=True).first()
        if user is not None:
            send_password_reset(user)
        return Response(
            {"detail": "Se a conta existir, enviaremos as instruções para o e-mail informado."}
        )


@method_decorator(csrf_protect, name="dispatch")
class PasswordResetConfirmView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    throttle_classes = (ScopedRateThrottle,)
    throttle_scope = "password_reset_confirm"

    @extend_schema(request=PasswordResetConfirmSerializer, responses={200: dict})
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Senha atualizada. Você já pode entrar."})
