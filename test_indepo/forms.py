from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.forms import TranslatableModelForm

from .models import (
    AboutItemPluginModel,
    AboutSectionPluginModel,
    ContactInfoPluginModel,
    DocumentItemPluginModel,
    FaqItemPluginModel,
    FaqSectionPluginModel,
    FeaturedServiceItem,
    FeaturedServicesSection,
    FooterPluginModel,
    HeroSectionPluginModel,
    HeaderPluginModel,
    HeaderQuickIcon,
    SocialInitiativesSectionPluginModel,
    SocialInitiativeCardPluginModel,
    AboutCardsSectionModel,
    AboutCardItemModel,
    LeadershipSectionModel,
    LeaderItemModel,
    ServiceItemPluginModel,
    ServicesSectionPluginModel,
    ServiceTilePluginModel,
    TeamContainer,
    TeamMember,
    TestimonialItemPluginModel,
    TestimonialsSectionPluginModel,
)


class ServiceTilePluginForm(TranslatableModelForm):
    class Meta:
        model = ServiceTilePluginModel
        fields = "__all__"


class AboutSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = AboutSectionPluginModel
        fields = "__all__"


class AboutItemPluginForm(TranslatableModelForm):
    class Meta:
        model = AboutItemPluginModel
        fields = "__all__"


class FaqSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = FaqSectionPluginModel
        fields = "__all__"


class FaqItemPluginForm(TranslatableModelForm):
    class Meta:
        model = FaqItemPluginModel
        fields = "__all__"


class HeroSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = HeroSectionPluginModel
        fields = "__all__"


class ServicesSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = ServicesSectionPluginModel
        fields = "__all__"


class ServiceItemPluginForm(TranslatableModelForm):
    class Meta:
        model = ServiceItemPluginModel
        fields = "__all__"


class TestimonialsSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = TestimonialsSectionPluginModel
        fields = "__all__"


class TestimonialItemPluginForm(TranslatableModelForm):
    class Meta:
        model = TestimonialItemPluginModel
        fields = "__all__"


class TeamContainerPluginForm(TranslatableModelForm):
    class Meta:
        model = TeamContainer
        fields = "__all__"


class TeamMemberPluginForm(TranslatableModelForm):
    class Meta:
        model = TeamMember
        fields = "__all__"


class ContactInfoPluginForm(TranslatableModelForm):
    class Meta:
        model = ContactInfoPluginModel
        fields = "__all__"


class FooterPluginForm(TranslatableModelForm):
    class Meta:
        model = FooterPluginModel
        fields = "__all__"


class DocumentItemPluginForm(forms.ModelForm):
    class Meta:
        model = DocumentItemPluginModel
        fields = "__all__"

    def clean(self):
        cleaned = super().clean()
        file = cleaned.get("file")
        url = (cleaned.get("url") or "").strip()
        if not file and not url:
            raise forms.ValidationError(_("Загрузите файл или укажите ссылку на документ."))
        if file:
            cleaned["url"] = ""
        else:
            cleaned["url"] = url
        return cleaned


class FeaturedServicesSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = FeaturedServicesSection
        fields = "__all__"


class FeaturedServiceItemPluginForm(TranslatableModelForm):
    class Meta:
        model = FeaturedServiceItem
        fields = "__all__"


class HeaderPluginForm(forms.ModelForm):
    class Meta:
        model = HeaderPluginModel
        fields = "__all__"


class AboutCardsSectionPluginForm(forms.ModelForm):
    class Meta:
        model = AboutCardsSectionModel
        fields = "__all__"


class AboutCardItemPluginForm(forms.ModelForm):
    class Meta:
        model = AboutCardItemModel
        fields = "__all__"


class LeadershipSectionPluginForm(forms.ModelForm):
    class Meta:
        model = LeadershipSectionModel
        fields = "__all__"


class LeaderItemPluginForm(forms.ModelForm):
    class Meta:
        model = LeaderItemModel
        fields = "__all__"


class HeaderQuickIconInlineForm(forms.ModelForm):
    ICON_CHOICES = [
        ("bi bi-telephone", _("Телефон")),
        ("bi bi-envelope", _("Почта")),
        ("bi bi-eyeglasses", _("Версия для слабовидящих")),
        ("bi bi-headset", _("Горячая линия")),
        ("bi bi-telegram", _("Telegram")),
        ("text:VK", _("VK (текст)")),
        ("text:OK", _("Одноклассники (текст)")),
        ("bi bi-people", _("Пользователи")),
        ("bi bi-whatsapp", _("WhatsApp")),
        ("bi bi-link-45deg", _("Ссылка")),
    ]
    CUSTOM_OPTION = "__custom__"

    custom_icon_class = forms.CharField(
        label=_("Своя иконка (CSS класс)"),
        required=False,
        help_text=_("Например: bi bi-shield-lock. Можно указать любой класс Bootstrap Icons."),
    )

    class Meta:
        model = HeaderQuickIcon
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rendered_choices = []
        for value, label in self.ICON_CHOICES:
            if value.startswith("text:"):
                text_value = value.split(":", 1)[1]
                html = mark_safe(
                    f'<span class="icon-choice icon-choice--text"><span class="icon-choice__text">{text_value}</span><span>{label}</span></span>'
                )
            else:
                html = mark_safe(f'<span class="icon-choice"><i class="{value}"></i><span>{label}</span></span>')
            rendered_choices.append((value, html))
        rendered_choices.append((self.CUSTOM_OPTION, _("Другая иконка")))

        self.fields["icon_class"] = forms.ChoiceField(
            label=_("Иконка"),
            choices=rendered_choices,
            widget=forms.RadioSelect(attrs={"class": "icon-choice__radios"}),
            required=True,
        )

        current_icon = self.instance.icon_class if self.instance.pk else None
        choice_values = {value for value, _ in self.ICON_CHOICES}
        if current_icon and current_icon not in choice_values:
            self.initial["icon_class"] = self.CUSTOM_OPTION
            self.initial["custom_icon_class"] = current_icon

        self.fields["background_color"].widget = forms.TextInput(
            attrs={"type": "color", "class": "vColorPicker"}
        )
        self.fields["icon_color"].widget = forms.TextInput(
            attrs={"type": "color", "class": "vColorPicker"}
        )
        self.fields["url"].widget.attrs.setdefault(
            "placeholder", "https://example.com или mailto:info@example.com"
        )
        self.order_fields(
            [
                "slot",
                "label",
                "icon_class",
                "custom_icon_class",
                "tooltip",
                "url",
                "open_in_new_tab",
                "background_color",
                "icon_color",
                "order",
            ]
        )

    def clean(self):
        cleaned_data = super().clean()
        icon_choice = cleaned_data.get("icon_class")
        custom_icon = cleaned_data.get("custom_icon_class")
        if icon_choice == self.CUSTOM_OPTION:
            if not custom_icon:
                self.add_error("custom_icon_class", _("Укажите CSS класс иконки"))
            else:
                cleaned_data["icon_class"] = custom_icon.strip()
        return cleaned_data


class SocialInitiativesSectionForm(forms.ModelForm):
    class Meta:
        model = SocialInitiativesSectionPluginModel
        fields = "__all__"


class SocialInitiativeCardForm(forms.ModelForm):
    class Meta:
        model = SocialInitiativeCardPluginModel
        exclude = ("section",)
