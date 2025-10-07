"""Development settings."""
from .base import *  # noqa

DEBUG = True

if not SECRET_KEY:
    SECRET_KEY = "django-insecure-change-me"

ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1", "[::1]"],
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
