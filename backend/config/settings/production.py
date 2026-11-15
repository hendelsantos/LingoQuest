from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403

DEBUG = False

if not SECRET_KEY:  # noqa: F405
    raise ImproperlyConfigured("DJANGO_SECRET_KEY é obrigatória em produção.")

if not env("DJANGO_ALLOWED_HOSTS", default="").strip():  # noqa: F405
    raise ImproperlyConfigured("DJANGO_ALLOWED_HOSTS é obrigatório em produção.")

if not env("DJANGO_CSRF_TRUSTED_ORIGINS", default="").strip():  # noqa: F405
    raise ImproperlyConfigured("DJANGO_CSRF_TRUSTED_ORIGINS é obrigatória em produção.")

if not env("DATABASE_URL", default="").strip():  # noqa: F405
    raise ImproperlyConfigured("DATABASE_URL é obrigatória em produção.")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
# Railway probes the container over its private HTTP network. Only liveness is exempt.
SECURE_REDIRECT_EXEMPT = [r"^health/$"]
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

