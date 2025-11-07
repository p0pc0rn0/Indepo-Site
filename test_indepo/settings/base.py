"""Shared Django settings for all environments."""
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "test_indepo"

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
)

# Load environment variables from a .env file if present
env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(env_file)

SECRET_KEY = env("DJANGO_SECRET_KEY", default="")

DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    default=[],
)

SITE_ID = env.int("DJANGO_SITE_ID", default=1)

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "djangocms_simple_admin_style",
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "parler",
    "filer",
    "easy_thumbnails",
    "djangocms_text_ckeditor",
    "djangocms_link",
    "djangocms_alias",
    "djangocms_versioning",
    "djangocms_frontend",
    "djangocms_frontend.contrib.accordion",
    "djangocms_frontend.contrib.alert",
    "djangocms_frontend.contrib.badge",
    "djangocms_frontend.contrib.card",
    "djangocms_frontend.contrib.carousel",
    "djangocms_frontend.contrib.collapse",
    "djangocms_frontend.contrib.content",
    "djangocms_frontend.contrib.grid",
    "djangocms_frontend.contrib.icon",
    "djangocms_frontend.contrib.image",
    "djangocms_frontend.contrib.jumbotron",
    "djangocms_frontend.contrib.link",
    "djangocms_frontend.contrib.listgroup",
    "djangocms_frontend.contrib.media",
    "djangocms_frontend.contrib.navigation",
    "djangocms_frontend.contrib.tabs",
    "djangocms_frontend.contrib.utilities",
]

LOCAL_APPS = [
    "test_indepo",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

ROOT_URLCONF = "test_indepo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [APPS_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "test_indepo.wsgi.application"
ASGI_APPLICATION = "test_indepo.asgi.application"

DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

CMS_LANGUAGES = {
    SITE_ID: [
        {
            "code": "ru",
            "name": _("Russian"),
            "fallbacks": ["en"],
            "public": True,
            "hide_untranslated": False,
            "redirect_on_fallback": True,
        },
        {
            "code": "en",
            "name": _("English"),
            "fallbacks": ["ru"],
            "public": True,
            "hide_untranslated": False,
            "redirect_on_fallback": True,
        },
    ],
    "default": {
        "fallbacks": ["en"],
        "redirect_on_fallback": True,
        "public": True,
        "hide_untranslated": False,
    },
}

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
]

PARLER_LANGUAGES = {
    SITE_ID: (
        {"code": "ru"},
        {"code": "en"},
    ),
    "default": {
        "fallback": "en",
        "hide_untranslated": False,
    },
}

TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True

SESSION_COOKIE_AGE = env.int("DJANGO_SESSION_COOKIE_AGE", default=600)
SESSION_SAVE_EVERY_REQUEST = env.bool("DJANGO_SESSION_SAVE_EVERY_REQUEST", default=False)
SESSION_EXPIRE_AT_BROWSER_CLOSE = env.bool("DJANGO_SESSION_EXPIRE_AT_BROWSER_CLOSE", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=not DEBUG)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=not DEBUG)

STATIC_URL = "static/"
STATICFILES_DIRS = [APPS_DIR / "static"]
STATIC_ROOT = Path(env("DJANGO_STATIC_ROOT", default=str(BASE_DIR / "staticfiles")))

#MEDIA_URL = "media/"
MEDIA_URL = '/file/'
MEDIA_ROOT = Path(env("DJANGO_MEDIA_ROOT", default=str(BASE_DIR.parent / "media")))

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CMS_CONFIRM_VERSION4 = True
CMS_TEMPLATES = (
    ("base.html", _("Standard")),
    ("index.html", _("Indepo-Home_Page")),
)
CMS_PERMISSION = True

X_FRAME_OPTIONS = "SAMEORIGIN"
TEXT_INLINE_EDITING = True
DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True
INTERNAL_IPS = ["127.0.0.1"]
