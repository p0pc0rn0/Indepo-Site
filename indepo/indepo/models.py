from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import gettext_lazy as _

class ServiceTilePluginModel(CMSPlugin):
    title = models.CharField(max_length=200, verbose_name="Title")
    icon_class = models.CharField(max_length=100, verbose_name="Bootstrap Icon Class", default="bi bi-calendar4-week")
    aos_delay = models.CharField(max_length=10, verbose_name="AOS Delay", default="300")

    def __str__(self):
        return self.title

class AboutSectionPluginModel(CMSPlugin):
    title = models.CharField(max_length=200, verbose_name="Section Title", default="About")
    subtitle_part1 = models.CharField(max_length=200, verbose_name="Subtitle Part 1", default="Find Out More")
    subtitle_part2 = models.CharField(max_length=200, verbose_name="Subtitle Part 2", default="About Us")

    def __str__(self):
        return self.title


class AboutItemPluginModel(CMSPlugin):
    main_heading = models.CharField(max_length=300, verbose_name="Main Heading")
    italic_text = models.TextField(verbose_name="Italic Text", blank=True, null=True)
    image = FilerImageField(
        verbose_name="Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="about_item_image"
    )
    aos_delay_image = models.CharField(max_length=10, verbose_name="AOS Delay for Image", default="100")
    aos_delay_content = models.CharField(max_length=10, verbose_name="AOS Delay for Content", default="200")

    def __str__(self):
        return self.main_heading

class FaqSectionPluginModel(CMSPlugin):
    title = models.CharField(
        max_length=200,
        verbose_name="Title",
        default="Часто задаваемые вопросы"
    )
    subtitle_part1 = models.CharField(
        max_length=200,
        verbose_name="Subtitle Part 1",
        default="Имеются вопросы?"
    )
    subtitle_part2 = models.CharField(
        max_length=200,
        verbose_name="Subtitle Part 2",
        default="Ознакомьтесь с нашими FAQ"
    )
    aos_delay = models.PositiveIntegerField(
        verbose_name="AOS Delay",
        default=100
    )

    def __str__(self):
        return self.title

class FaqItemPluginModel(CMSPlugin):
    question = models.CharField(
        max_length=200,
        verbose_name="Question",
        default="Вопрос"
    )
    answer = HTMLField(
        verbose_name="Answer",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name="Is Active",
        default=False
    )

    def __str__(self):
        return self.question

class HeroSectionPluginModel(CMSPlugin):
    background_image = FilerImageField(
        verbose_name="Background Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="hero_background_image"
    )
    title_part1 = models.CharField(
        max_length=200,
        verbose_name="Title Part 1",
        default="Приветствуем в"
    )
    title_part2 = models.CharField(
        max_length=200,
        verbose_name="Title Part 2 (Highlighted)",
        default='ФБГУ НИИ "Интеграл"'
    )
    description = HTMLField(
        verbose_name="Description Text",
        blank=True,
        null=True,
        default="Ведомственная принадлежность: ФГБУ НИИ «Интеграл» находится в ведении Министерства цифрового развития, связи и массовых коммуникаций Российской Федерации"
    )
    get_started_text = models.CharField(
        max_length=100,
        verbose_name="Get Started Button Text",
        default="Get Started"
    )
    get_started_url = models.CharField(
        max_length=200,
        verbose_name="Get Started Button URL",
        default="#about",
        blank=True
    )
    telegram_text = models.CharField(
        max_length=100,
        verbose_name="Telegram Button Text",
        default="Телеграмм канал",
        blank=True
    )
    telegram_url = models.CharField(
        max_length=200,
        verbose_name="Telegram Button URL",
        default="https://t.me/integral_security",
        blank=True
    )
    aos_animation = models.CharField(
        max_length=50,
        verbose_name="AOS Animation",
        default="zoom-out",
        blank=True
    )

    def __str__(self):
        return f"Hero: {self.title_part1} {self.title_part2}"

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
