from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
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

    def copy_relations(self, oldinstance):
        """
        Ensure parler translations are copied when duplicating plugins
        (e.g. при создании новой версии страницы).
        """
        for translation in oldinstance.translations.all():
            translation.pk = None
            translation.master = self
            translation.save()


class ServiceTilePluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        body=HTMLField(_("Body"), blank=True, null=True),
    )
    icon_class = models.CharField(
        _("Bootstrap icon class"), max_length=100, default="bi bi-calendar4-week"
    )
    aos_delay = models.PositiveIntegerField(_("AOS delay (ms)"), default=300)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Service Tile"


class AboutSectionPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Section title"), max_length=200, default="About"),
        subtitle_part1=models.CharField(_("Subtitle part 1"), max_length=200, default="Find Out More"),
        subtitle_part2=models.CharField(_("Subtitle part 2"), max_length=200, default="About Us"),
    )

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "About section"


class AboutItemPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        main_heading=models.CharField(_("Main heading"), max_length=300),
        italic_text=HTMLField(_("Intro text"), blank=True, null=True),
    )
    image = FilerImageField(
        verbose_name=_("Image"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    aos_delay_image = models.PositiveIntegerField(_("AOS delay for image (ms)"), default=100)
    aos_delay_content = models.PositiveIntegerField(_("AOS delay for content (ms)"), default=200)

    def __str__(self):
        return self.safe_translation_getter("main_heading", any_language=True) or "About item"


class FaqSectionPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200, default="Часто задаваемые вопросы"),
        subtitle_part1=models.CharField(_("Subtitle part 1"), max_length=200, default="Имеются вопросы?"),
        subtitle_part2=models.CharField(
            _("Subtitle part 2"), max_length=200, default="Ознакомьтесь с нашими FAQ"
        ),
    )
    aos_delay = models.PositiveIntegerField(_("AOS delay (ms)"), default=100)

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "FAQ section"


class FaqItemPluginModel(TranslatableCMSPlugin):
    translations = TranslatedFields(
        question=models.CharField(_("Question"), max_length=200, default="Вопрос"),
        answer=HTMLField(_("Answer"), blank=True, null=True),
    )
    is_active = models.BooleanField(_("Is active"), default=False)

    def __str__(self):
        return self.safe_translation_getter("question", any_language=True) or "FAQ item"


class HeroSectionPluginModel(TranslatableCMSPlugin):
    background_image = FilerImageField(
        verbose_name=_("Background image"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    translations = TranslatedFields(
        title_part1=models.CharField(_("Title part 1"), max_length=200, default="Приветствуем в"),
        title_part2=models.CharField(_("Title part 2"), max_length=200, default='ФБГУ НИИ "Интеграл"'),
        description=HTMLField(
            _("Description"),
            blank=True,
            null=True,
            default=(
                "Ведомственная принадлежность: ФГБУ НИИ «Интеграл» находится в ведении Министерства цифрового "
                "развития, связи и массовых коммуникаций Российской Федерации"
            ),
        ),
        get_started_text=models.CharField(_("Primary button text"), max_length=100, default="Get Started"),
    )
    get_started_url = models.CharField(_("Primary button URL"), max_length=200, default="#about", blank=True)
    aos_animation = models.CharField(_("AOS animation"), max_length=50, default="zoom-out", blank=True)

    def __str__(self):
        title = self.safe_translation_getter("title_part2", any_language=True)
        return f"Hero: {title}" if title else "Hero Section"


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
    ICON_SIZE_CHOICES = [
        ("sm", _("Small")),
        ("md", _("Medium")),
        ("lg", _("Large")),
    ]
    LAYOUT_VARIANT_CHOICES = [
        ("vertical", _("Vertical")),
        ("inline", _("Inline")),
    ]

    translations = TranslatedFields(
        title=models.CharField(max_length=100, default="Contact"),
        subtitle=models.CharField(
            max_length=255,
            blank=True,
            default="<span>Need Help?</span> <span class='description-title'>Contact Us</span>",
        ),
        address=models.CharField(max_length=255, default="A108 Adam Street, New York, NY 535022"),
    )
    phone = models.CharField(max_length=50, default="+1 5589 55488 55")
    email = models.EmailField(default="info@example.com")
    map_iframe = models.TextField(
        default='<iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A..." width="100%" height="400" frameborder="0"></iframe>',
        help_text="Вставьте iframe карты Яндекс",
    )
    work_hours_title = models.CharField(
        _("Work hours title"), max_length=120, blank=True, default="Время работы"
    )
    work_hours_text = models.TextField(_("Work hours"), blank=True, default="")
    vk_url = models.URLField(_("VK URL"), blank=True, default="")
    tg_url = models.URLField(
        _("Telegram URL"),
        blank=True,
        default="",
        help_text=_("Например: https://t.me/your_channel или tg://resolve?domain=your_channel"),
    )
    ok_url = models.URLField(_("Odnoklassniki URL"), blank=True, default="")
    show_labels = models.BooleanField(_("Show labels near icons"), default=False)
    icon_size = models.CharField(
        _("Icon size"), max_length=2, choices=ICON_SIZE_CHOICES, default="md"
    )
    layout_variant = models.CharField(
        _("Layout variant"),
        max_length=8,
        choices=LAYOUT_VARIANT_CHOICES,
        default="vertical",
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


class DocumentsSectionPluginModel(CMSPlugin):
    LAYOUT_CHOICES = [
        ("list", _("List")),
        ("accordion", _("Accordion")),
    ]

    title = models.CharField(_("Title"), max_length=200, blank=True, default="")
    show_search = models.BooleanField(_("Show search field"), default=True)
    show_empty_sections = models.BooleanField(_("Show empty subsections"), default=True)
    layout_variant = models.CharField(
        _("Layout variant"), max_length=20, choices=LAYOUT_CHOICES, default="list"
    )

    def __str__(self):
        return self.title or str(_("Documents section"))


class DocumentSubsectionPluginModel(CMSPlugin):
    title = models.CharField(_("Subsection title"), max_length=200, blank=True, default="")
    description = HTMLField(_("Description"), blank=True, default="")

    def __str__(self):
        return self.title or str(_("Documents subsection"))


class DocumentItemPluginModel(CMSPlugin):
    name = models.CharField(_("Document name"), max_length=255)
    url = models.URLField(_("Document URL"))
    description = models.TextField(_("Short description"), blank=True, default="")

    def __str__(self):
        return self.name


class TablePluginModel(CMSPlugin):
    title = models.CharField(_("Table title"), max_length=200, blank=True, default="")
    table_html = HTMLField(_("Table content"))
    footnote = models.CharField(_("Footnote"), max_length=255, blank=True, default="")

    def __str__(self):
        return self.title or str(_("Table"))


class AboutCardsSectionModel(CMSPlugin):
    LAYOUT_CHOICES = [
        ("list", _("List")),
        ("accordion", _("Accordion")),
    ]

    title = models.CharField(_("Section title"), max_length=200, blank=True, default="")
    layout_variant = models.CharField(
        _("Layout variant"), max_length=20, choices=LAYOUT_CHOICES, default="list"
    )

    def __str__(self):
        return self.title or str(_("About section"))


class AboutCardItemModel(CMSPlugin):
    title = models.CharField(_("Card title"), max_length=200)
    body = HTMLField(_("Card description"), blank=True, default="")
    initially_open = models.BooleanField(_("Open by default (accordion)"), default=False)

    def __str__(self):
        return self.title


class HeaderPluginModel(CMSPlugin):
    show_avatar = models.BooleanField(default=True, verbose_name=_("Show avatar"))
    avatar = FilerImageField(
        verbose_name=_("Avatar"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    def __str__(self):
        return "Header navigation"
