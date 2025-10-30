from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import NavigationIcon


ICON_CHOICES = [
    ("", _("Без иконки")),
    ("bi bi-house", _("Дом")),
    ("bi bi-journal-check", _("Журнал")),
    ("bi bi-folder2", _("Папка")),
    ("bi bi-mortarboard", _("Образование")),
    ("bi bi-shield-exclamation", _("Безопасность")),
    ("bi bi-people", _("Сообщество")),
    ("bi bi-people-heart", _("Поддержка")),
    ("bi bi-megaphone", _("Анонс")),
    ("bi bi-award", _("Награда")),
    ("bi bi-rocket-takeoff", _("Запуск")),
    ("bi bi-stars", _("Выделение")),
    ("bi bi-lightning-charge", _("Активность")),
    ("bi bi-gear", _("Настройки")),
    ("bi bi-globe2", _("Глобально")),
    ("bi bi-pin-map", _("Карта")),
]


class IconPickerWidget(forms.Widget):
    template_name = "admin/widgets/icon_picker.html"

    def __init__(self, icon_choices=None, attrs=None):
        super().__init__(attrs)
        self.icon_choices = icon_choices or ICON_CHOICES

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        widget = context["widget"]
        value = (value or "").strip()
        element_id = widget["attrs"].get("id", f"id_{name}")

        choices = list(self.icon_choices)
        if value and all(
            (isinstance(choice, (list, tuple)) and choice[0] != value) or choice != value
            for choice in choices
        ):
            choices = choices + [(value, value)]

        icons = []
        for index, choice in enumerate(choices):
            if isinstance(choice, (list, tuple)):
                icon_value, icon_label = choice
            else:
                icon_value = icon_label = choice
            icon_id = f"{element_id}_{index}"
            icons.append(
                {
                    "id": icon_id,
                    "value": icon_value,
                    "label": icon_label,
                    "selected": icon_value == value,
                }
            )

        widget["icons"] = icons
        return context

    class Media:
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
                "test_indepo/admin/icon-picker.css",
            )
        }
        js = ("test_indepo/admin/icon-picker.js",)


class NavigationIconForm(forms.ModelForm):
    icon_class = forms.ChoiceField(
        label=_("Иконка"),
        required=False,
        choices=ICON_CHOICES,
        widget=IconPickerWidget(icon_choices=ICON_CHOICES),
        help_text=_("Выберите подходящую иконку из набора Bootstrap Icons."),
    )

    class Meta:
        model = NavigationIcon
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_value = self.initial.get("icon_class") or getattr(self.instance, "icon_class", "")
        if current_value and all(choice[0] != current_value for choice in self.fields["icon_class"].choices):
            extra_choices = list(self.fields["icon_class"].choices) + [(current_value, current_value)]
            self.fields["icon_class"].choices = extra_choices
            self.fields["icon_class"].widget.icon_choices = extra_choices


@admin.register(NavigationIcon)
class NavigationIconAdmin(admin.ModelAdmin):
    form = NavigationIconForm
    list_display = ("page", "icon_preview", "icon_class")
    list_display_links = ("page", "icon_preview")
    search_fields = ("page__title", "icon_class")

    @admin.display(description=_("Иконка"))
    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html('<i class="{}" style="font-size: 1.4rem;"></i>', obj.icon_class)
        return _("(нет)")
