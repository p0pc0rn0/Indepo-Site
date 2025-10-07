from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from parler.models import TranslatableModelMixin, TranslatedFields


def default_swiper_config():
    """Return default swiper configuration."""
    return {
        "loop": True,
        "speed": 600,
        "autoplay": {"delay": 5000},
        "slidesPerView": "auto",
        "pagination": {
            "el": ".swiper-pagination",
            "type": "bullets",
            "clickable": True,
        },
    }


class TranslatableCMSPlugin(TranslatableModelMixin, CMSPlugin):
    """Base class to combine django CMS plugins with parler translations."""

    class Meta:
        abstract = True


class TopBarPluginModel(CMSPlugin):
    email = models.EmailField(default="contact@example.com", verbose_name="Email")
    phone = models.CharField(max_length=50, default="+1 5589 55488 55", verbose_name="Телефон")
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")
    vk = models.URLField(blank=True, null=True, verbose_name="ВКонтакте")
    odnoklassniki = models.URLField(blank=True, null=True, verbose_name="Одноклассники")

    def __str__(self):
        return f"TopBar ({self.email}, {self.phone})"


class ServicesSectionPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200, default="Services"),
        subtitle=models.CharField(_("Subtitle"), max_length=200, blank=True, default="Check Our Services"),
    )

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Services Section"


class ServiceItemPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        description=models.TextField(_("Description"), blank=True),
    )
    icon_class = models.CharField(
        _("Icon CSS class"), max_length=100, default="bi bi-activity", help_text="Например: 'bi bi-activity'"
    )
    link = models.URLField(_("Link"), blank=True)
    aos_delay = models.PositiveIntegerField(_("AOS delay (ms)"), default=100)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Service"


class TestimonialsSectionPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200, default="Testimonials"),
        subtitle=models.CharField(_("Subtitle"), max_length=200, blank=True, default=""),
    )
    background = models.CharField(
        _("Background image (static path)"), max_length=255, blank=True, default="assets/img/testimonials-bg.jpg"
    )
    swiper_config = models.JSONField(_("Swiper JSON config"), blank=True, default=default_swiper_config)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Testimonials Section"


class TestimonialItemPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        author_name=models.CharField(_("Author name"), max_length=200),
        author_role=models.CharField(_("Author role"), max_length=200, blank=True),
        quote=models.TextField(_("Quote")),
    )
    image = models.CharField(
        _("Image (static path)"), max_length=255, blank=True, help_text="например: assets/img/testimonials/testimonials-1.jpg"
    )

    def __str__(self):
        return self.safe_translation_getter("author_name", any_language=True) or "Testimonial"


class TeamContainer(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, default="Team"),
        description=models.CharField(max_length=300, blank=True, null=True),
    )

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Team"


class TeamMember(TranslatableCMSPlugin):
    photo = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        role=models.CharField(max_length=200),
        subtitle=models.CharField(max_length=150, blank=True, null=True),
    )

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or "Team member"


class ContactInfoPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(max_length=100, default="Contact"),
        subtitle=models.CharField(max_length=255, default="<span>Need Help?</span> <span class='description-title'>Contact Us</span>"),
        address=models.CharField(max_length=255, default="A108 Adam Street, New York, NY 535022"),
    )
    phone = models.CharField(max_length=50, default="+1 5589 55488 55")
    email = models.EmailField(default="info@example.com")
    map_iframe = models.TextField(
        default='<iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A..." width="100%" height="400" frameborder="0"></iframe>',
        help_text="Вставьте iframe карты Яндекс",
    )

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Contact"


class FooterPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        copyright_text=models.CharField(max_length=255, default="All Rights Reserved", verbose_name="Текст копирайта"),
        site_name=models.CharField(max_length=100, default="BizLand", verbose_name="Название сайта"),
        designed_by=models.CharField(max_length=100, default="BootstrapMade", verbose_name="Кем разработан"),
    )
    designed_by_url = models.URLField(default="https://bootstrapmade.com/", verbose_name="Ссылка на разработчика")

    def __str__(self):
        return self.safe_translation_getter("site_name", any_language=True) or "Footer"


class FeaturedServicesSection(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField("Заголовок", max_length=200, blank=True, null=True),
        description=models.TextField("Описание", blank=True, null=True),
    )

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Featured Services Section"


class FeaturedServiceItem(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(max_length=100, verbose_name="Заголовок"),
        description=models.TextField(verbose_name="Описание"),
    )
    icon = models.CharField(max_length=50, default="bi bi-activity", verbose_name="Bootstrap Icon класс")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    delay = models.PositiveIntegerField(default=100, verbose_name="Анимация (delay в ms)")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Service Item"
