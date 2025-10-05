from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ("ru", _("Russian")),
    ("en", _("English")),
]

CMS_LANGUAGES = {
    1: [
        {
            "code": "ru",
            "name": _("Russian"),
            "fallbacks": ["en"],  # если нет перевода на русском, использовать английский
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
