from .base import *  # noqa: F403

DEBUG = False
SECRET_KEY = "test-only-secret-key-not-for-production"
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
DATABASES["default"].setdefault("OPTIONS", {})  # noqa: F405
# O seed recria centenas de questões. Sem estatísticas nas tabelas temporárias de teste,
# o PostgreSQL pode gastar mais tempo compilando JIT do que executando as pequenas queries.
DATABASES["default"]["OPTIONS"]["options"] = "-c jit=off"  # noqa: F405
MIDDLEWARE = [
    middleware
    for middleware in MIDDLEWARE  # noqa: F405
    if middleware != "whitenoise.middleware.WhiteNoiseMiddleware"
]

