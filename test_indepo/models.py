from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class TopBarPluginModel(CMSPlugin):
    email = models.EmailField(default="contact@example.com", verbose_name="Email")
    phone = models.CharField(max_length=50, default="+1 5589 55488 55", verbose_name="Телефон")

    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")
    vk = models.URLField(blank=True, null=True, verbose_name="ВКонтакте")
    odnoklassniki = models.URLField(blank=True, null=True, verbose_name="Одноклассники")

    def __str__(self):
        return f"TopBar ({self.email}, {self.phone})"

class ServicesSectionPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, default="Services")
    subtitle = models.CharField(_("Subtitle"), max_length=200, blank=True, default="Check Our Services")

    def __str__(self):
        return f"ServicesSection: {self.title}"

class ServiceItemPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"), blank=True)
    icon_class = models.CharField(_("Icon CSS class"), max_length=100, default="bi bi-activity", help_text="Например: 'bi bi-activity'")
    link = models.URLField(_("Link"), blank=True)
    # delay в миллисекундах для data-aos-delay (удобно настраивать)
    aos_delay = models.PositiveIntegerField(_("AOS delay (ms)"), default=100)

    def __str__(self):
        return f"Service: {self.title}"

class TestimonialsSectionPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=200, default="Testimonials")
    subtitle = models.CharField(_("Subtitle"), max_length=200, blank=True, default="")
    # путь к картинке фона (static). Можно оставить дефолтный путь к статике шаблона.
    background = models.CharField(_("Background image (static path)"), max_length=255, blank=True, default="assets/img/testimonials-bg.jpg")
    # JSON конфиг для слайдера (храним как текст, но вставляем в <script type="application/json">)
    swiper_config = models.TextField(_("Swiper JSON config"), blank=True, default='{"loop": true, "speed": 600, "autoplay": {"delay": 5000}, "slidesPerView": "auto", "pagination": {"el": ".swiper-pagination", "type": "bullets", "clickable": true}}')

    def __str__(self):
        return f"TestimonialsSection: {self.title}"

class TestimonialItemPluginModel(CMSPlugin):
    author_name = models.CharField(_("Author name"), max_length=200)
    author_role = models.CharField(_("Author role"), max_length=200, blank=True)
    quote = models.TextField(_("Quote"))
    # Путь до изображения в static (можно оставить пустым)
    image = models.CharField(_("Image (static path)"), max_length=255, blank=True, help_text="например: assets/img/testimonials/testimonials-1.jpg")

    def __str__(self):
        return f"Testimonial: {self.author_name}"


class TeamContainer(CMSPlugin):
    title = models.CharField(max_length=200, default="Team")
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title


class TeamMember(CMSPlugin):
    plugin = models.ForeignKey(
        TeamContainer, on_delete=models.CASCADE, related_name="teammember_set"
    )
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo = FilerImageField(
        null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    subtitle = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class ContactInfoPluginModel(CMSPlugin):
    title = models.CharField(max_length=100, default="Contact")
    subtitle = models.CharField(max_length=255, default="<span>Need Help?</span> <span class='description-title'>Contact Us</span>")

    address = models.CharField(max_length=255, default="A108 Adam Street, New York, NY 535022")
    phone = models.CharField(max_length=50, default="+1 5589 55488 55")
    email = models.EmailField(default="info@example.com")
    map_iframe = models.TextField(
        default='<iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A..." width="100%" height="400" frameborder="0"></iframe>',
        help_text="Вставьте iframe карты Яндекс"
    )

    def __str__(self):
        return f"{self.title}"

class FooterPluginModel(CMSPlugin):
    copyright_text = models.CharField(
        max_length=255,
        default="All Rights Reserved",
        verbose_name="Текст копирайта"
    )
    site_name = models.CharField(
        max_length=100,
        default="BizLand",
        verbose_name="Название сайта"
    )
    designed_by = models.CharField(
        max_length=100,
        default="BootstrapMade",
        verbose_name="Кем разработан"
    )
    designed_by_url = models.URLField(
        default="https://bootstrapmade.com/",
        verbose_name="Ссылка на разработчика"
    )

    def __str__(self):
        return f"Footer: {self.site_name}"

class FeaturedServicesSection(CMSPlugin):
    title = models.CharField("Заголовок", max_length=200, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)

    def __str__(self):
        return self.title or "Featured Services Section"

class FeaturedServiceItem(CMSPlugin):
    icon = models.CharField(
        max_length=50,
        default="bi bi-activity",
        verbose_name="Bootstrap Icon класс"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    link = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    delay = models.PositiveIntegerField(
        default=100,
        verbose_name="Анимация (delay в ms)"
    )

    def __str__(self):
        return self.title
