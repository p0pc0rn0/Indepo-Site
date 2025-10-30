from datetime import datetime, time as datetime_time

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


from .forms import (
    AboutItemPluginForm,
    AboutSectionPluginForm,
    ContactInfoPluginForm,
    FaqItemPluginForm,
    FaqSectionPluginForm,
    FeaturedServiceItemPluginForm,
    FeaturedServicesSectionPluginForm,
    FooterPluginForm,
    HeroSectionPluginForm,
    HeaderPluginForm,
    AboutCardsSectionPluginForm,
    AboutCardItemPluginForm,
    LeadershipSectionPluginForm,
    LeaderItemPluginForm,
    ServiceItemPluginForm,
    ServicesSectionPluginForm,
    ServiceTilePluginForm,
    TeamContainerPluginForm,
    TeamMemberPluginForm,
    TestimonialItemPluginForm,
    TestimonialsSectionPluginForm,
)
from .models import (
    AboutItemPluginModel,
    AboutSectionPluginModel,
    ContactInfoPluginModel,
    FaqItemPluginModel,
    FaqSectionPluginModel,
    FeaturedServiceItem,
    FeaturedServicesSection,
    FooterPluginModel,
    HeroSectionPluginModel,
    HeaderPluginModel,
    NavigationIcon,
    DocumentItemPluginModel,
    DocumentSubsectionPluginModel,
    DocumentsSectionPluginModel,
    AboutCardsSectionModel,
    AboutCardItemModel,
    LeadershipSectionModel,
    LeaderItemModel,
    NewsItemPluginModel,
    NewsSectionPluginModel,
    TablePluginModel,
    ServiceItemPluginModel,
    ServicesSectionPluginModel,
    ServiceTilePluginModel,
    TeamContainer,
    TeamMember,
    TestimonialItemPluginModel,
    TestimonialsSectionPluginModel,
    TopBarPluginModel,
)


@plugin_pool.register_plugin
class ServiceTilePlugin(CMSPluginBase):
    model = ServiceTilePluginModel
    name = _("Service Tile")
    render_template = "cms/plugins/service_tile.html"
    form = ServiceTilePluginForm
    cache = False
    module = _("Sections")


@plugin_pool.register_plugin
class AboutSectionPlugin(CMSPluginBase):
    model = AboutSectionPluginModel
    name = _("About Section")
    render_template = "cms/plugins/about_section.html"
    form = AboutSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ["AboutItemPlugin"]
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["children"] = list(instance.child_plugin_instances)
        return context


@plugin_pool.register_plugin
class AboutItemPlugin(CMSPluginBase):
    model = AboutItemPluginModel
    name = _("About Item")
    render_template = "cms/plugins/about_item.html"
    form = AboutItemPluginForm
    cache = False
    require_parent = True
    parent_classes = ["AboutSectionPlugin"]
    module = _("Sections")


@plugin_pool.register_plugin
class FaqSectionPlugin(CMSPluginBase):
    model = FaqSectionPluginModel
    name = _("FAQ Section")
    render_template = "cms/plugins/faq_section.html"
    form = FaqSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ["FaqItemPlugin"]
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["children"] = list(instance.child_plugin_instances)
        return context


@plugin_pool.register_plugin
class FaqItemPlugin(CMSPluginBase):
    model = FaqItemPluginModel
    name = _("FAQ Item")
    render_template = "cms/plugins/faq_item.html"
    form = FaqItemPluginForm
    cache = False
    require_parent = True
    parent_classes = ["FaqSectionPlugin"]
    module = _("Sections")

    def render(self, context, instance, placeholder):
        return super().render(context, instance, placeholder)


@plugin_pool.register_plugin
class HeroSectionPlugin(CMSPluginBase):
    model = HeroSectionPluginModel
    name = _("Hero Section")
    render_template = "cms/plugins/hero_section.html"
    form = HeroSectionPluginForm
    cache = False
    module = _("Sections")


@plugin_pool.register_plugin
class TopBarPlugin(CMSPluginBase):
    model = TopBarPluginModel
    name = _("Top Bar")
    render_template = "cms/plugins/topbar.html"
    cache = False
    module = _("Header")


@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = HeaderPluginModel
    name = _("Header")
    render_template = "cms/plugins/header.html"
    form = HeaderPluginForm
    cache = False
    module = _("Header")

    DEFAULT_ICON_SEEDS = {
        "Главная": "bi bi-house",
        "Регистрация программ": "bi bi-journal-check",
        "Правовое обеспечение": "bi bi-folder2",
        "Документы": "bi bi-folder2",
        "Образование": "bi bi-mortarboard",
        "ИС Антифишинг": "bi bi-shield-exclamation",
        "Антифишинг": "bi bi-shield-exclamation",
        "Передать сообщение о фишинги": "bi bi-shield-exclamation",
        "Передать сообщение о фишинге": "bi bi-shield-exclamation",
        "#МЫВМЕСТЕ": "bi bi-megaphone",
        "Мы вместе": "bi bi-megaphone",
        "Конкурс вместе против коррупции": "bi bi-award",
    }
    FALLBACK_ICON = "bi bi-app-indicator"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        icon_map = {
            icon.page_id: icon.icon_class
            for icon in NavigationIcon.objects.select_related("page")
        }
        normalized_defaults = {"__fallback__": self.FALLBACK_ICON}
        for title_seed, icon_class in self.DEFAULT_ICON_SEEDS.items():
            if not title_seed:
                continue
            stripped = title_seed.strip()
            casefolded = stripped.casefold()
            ascii_slug = slugify(stripped, allow_unicode=False)
            unicode_slug = slugify(stripped, allow_unicode=True)
            dashed = casefolded.replace(" ", "-")
            compact = casefolded.replace(" ", "")

            for key in {
                casefolded,
                ascii_slug,
                unicode_slug,
                dashed,
                compact,
            }:
                if key:
                    normalized_defaults[key] = icon_class

        context["icon_map"] = icon_map
        context["default_icons"] = normalized_defaults
        return context


@plugin_pool.register_plugin
class DocumentsSectionPlugin(CMSPluginBase):
    model = DocumentsSectionPluginModel
    name = _("Documents Section")
    render_template = "cms/plugins/documents_section.html"
    cache = False
    allow_children = True
    child_classes = ["DocumentSubsectionPlugin"]
    module = _("Documents")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        children = getattr(instance, "child_plugin_instances", []) or []
        visible_children = []
        has_documents = False

        for child in children:
            if isinstance(child, DocumentSubsectionPluginModel):
                documents = [
                    doc
                    for doc in (getattr(child, "child_plugin_instances", []) or [])
                    if isinstance(doc, DocumentItemPluginModel)
                ]
                section_has_docs = bool(documents)
                if section_has_docs:
                    has_documents = True
                if section_has_docs or instance.show_empty_sections:
                    visible_children.append(child)

        context["children"] = visible_children
        context["has_documents"] = has_documents
        context["layout_variant"] = instance.layout_variant
        context["show_empty_sections"] = instance.show_empty_sections
        return context


@plugin_pool.register_plugin
class DocumentSubsectionPlugin(CMSPluginBase):
    model = DocumentSubsectionPluginModel
    name = _("Document Subsection")
    render_template = "cms/plugins/document_subsection.html"
    cache = False
    allow_children = True
    child_classes = ["DocumentItemPlugin"]
    parent_classes = ["DocumentsSectionPlugin"]
    module = _("Documents")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        documents = [
            doc
            for doc in (getattr(instance, "child_plugin_instances", []) or [])
            if isinstance(doc, DocumentItemPluginModel)
        ]
        parent_model = None
        if instance.parent:
            parent_model, _plugin = instance.parent.get_plugin_instance()

        context["documents"] = documents
        context["has_documents"] = bool(documents)
        context["layout_variant"] = getattr(parent_model, "layout_variant", "list")
        context["show_empty_sections"] = getattr(parent_model, "show_empty_sections", True)
        context["section_dom_id"] = f"docs-subsection-{instance.pk}"
        return context


@plugin_pool.register_plugin
class DocumentItemPlugin(CMSPluginBase):
    model = DocumentItemPluginModel
    name = _("Document Item")
    render_template = "cms/plugins/document_item.html"
    cache = False
    require_parent = True
    parent_classes = ["DocumentSubsectionPlugin"]
    module = _("Documents")


@plugin_pool.register_plugin
class NewsSectionPlugin(CMSPluginBase):
    model = NewsSectionPluginModel
    name = _("News Section")
    render_template = "cms/plugins/news_section.html"
    cache = False
    allow_children = True
    child_classes = ["NewsItemPlugin"]
    module = _("News")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        children = list(getattr(instance, "child_plugin_instances", []) or [])
        items = [
            child
            for child in children
            if isinstance(child, NewsItemPluginModel) and getattr(child, "is_active", True)
        ]

        current_tz = timezone.get_current_timezone()

        def sort_key(item):
            if item.date:
                dt = datetime.combine(item.date, datetime_time.min)
                if timezone.is_naive(dt):
                    dt = timezone.make_aware(dt, current_tz)
                return dt
            value = getattr(item, "creation_date", None)
            return value or timezone.now()

        items.sort(key=sort_key, reverse=True)

        if instance.count and instance.count > 0:
            items = items[: instance.count]

        context["instance"] = instance
        context["items"] = items
        context["layout_variant"] = instance.layout_variant
        context["section_dom_id"] = f"news-section-{instance.pk}"
        context["has_items"] = bool(items)
        context["display_mode"] = instance.display_mode
        context["items_per_page"] = instance.items_per_page
        return context


@plugin_pool.register_plugin
class NewsItemPlugin(CMSPluginBase):
    model = NewsItemPluginModel
    name = _("News Item")
    render_template = "cms/plugins/news_item.html"
    cache = False
    require_parent = True
    parent_classes = ["NewsSectionPlugin"]
    module = _("News")

    PLACEHOLDER_STATIC_PATH = "assets/img/news/news-placeholder.jpg"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        context["placeholder_image"] = self.PLACEHOLDER_STATIC_PATH
        return context


@plugin_pool.register_plugin
class TablePlugin(CMSPluginBase):
    model = TablePluginModel
    name = _("Tables")
    render_template = "cms/plugins/table.html"
    cache = False
    module = _("Content")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        return context







@plugin_pool.register_plugin
class AboutCardsSectionPlugin(CMSPluginBase):
    model = AboutCardsSectionModel
    name = _("About")
    render_template = "cms/plugins/about_cards_section.html"
    form = AboutCardsSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ["AboutCardItemPlugin"]
    module = _("About")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["children"] = list(getattr(instance, "child_plugin_instances", []) or [])
        context["layout_variant"] = instance.layout_variant
        context["instance"] = instance
        context["section_dom_id"] = f"about-section-{instance.pk}"
        return context


@plugin_pool.register_plugin
class AboutCardItemPlugin(CMSPluginBase):
    model = AboutCardItemModel
    name = _("About card")
    render_template = "cms/plugins/about_card_item.html"
    form = AboutCardItemPluginForm
    cache = False
    require_parent = True
    parent_classes = ["AboutCardsSectionPlugin"]
    module = _("About")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        parent_model = None
        if instance.parent:
            parent_model, _plugin = instance.parent.get_plugin_instance()
        layout_variant = getattr(parent_model, "layout_variant", "list")
        context["layout_variant"] = layout_variant
        context["card_dom_id"] = f"about-card-{instance.pk}"
        context["is_initially_open"] = bool(instance.initially_open)
        return context


@plugin_pool.register_plugin
class LeadershipSectionPlugin(CMSPluginBase):
    model = LeadershipSectionModel
    name = _("Leadership")
    render_template = "cms/plugins/leadership_section.html"
    form = LeadershipSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ["LeaderItemPlugin"]
    module = _("About")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        context["leaders"] = list(getattr(instance, "child_plugin_instances", []) or [])
        return context


@plugin_pool.register_plugin
class LeaderItemPlugin(CMSPluginBase):
    model = LeaderItemModel
    name = _("Leader")
    render_template = "cms/plugins/leader_item.html"
    form = LeaderItemPluginForm
    cache = False
    require_parent = True
    parent_classes = ["LeadershipSectionPlugin"]
    module = _("About")

    PLACEHOLDER_STATIC_PATH = "assets/img/leadership/leader-placeholder.jpg"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        context["placeholder_image"] = self.PLACEHOLDER_STATIC_PATH
        return context


@plugin_pool.register_plugin
class ServicesSectionPlugin(CMSPluginBase):
    model = ServicesSectionPluginModel
    name = _("Services Section")
    render_template = "cms/plugins/services_section.html"
    form = ServicesSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ['ServiceItemPlugin']
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        context['children'] = list(instance.child_plugin_instances)
        return context

@plugin_pool.register_plugin
class ServiceItemPlugin(CMSPluginBase):
    model = ServiceItemPluginModel
    name = _("Service Item")
    render_template = "cms/plugins/service_item.html"
    require_parent = True
    parent_classes = ['ServicesSectionPlugin']
    form = ServiceItemPluginForm
    cache = False
    module = _("Sections")

@plugin_pool.register_plugin
class TestimonialsSectionPlugin(CMSPluginBase):
    model = TestimonialsSectionPluginModel
    name = _("Testimonials Section")
    render_template = "cms/plugins/testimonials_section.html"
    form = TestimonialsSectionPluginForm
    cache = False
    allow_children = True
    child_classes = ['TestimonialItemPlugin']
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        context['children'] = list(instance.child_plugin_instances)
        return context

@plugin_pool.register_plugin
class TestimonialItemPlugin(CMSPluginBase):
    model = TestimonialItemPluginModel
    name = _("Testimonial Item")
    render_template = "cms/plugins/testimonial_item.html"
    require_parent = True
    parent_classes = ['TestimonialsSectionPlugin']
    form = TestimonialItemPluginForm
    cache = False
    module = _("Sections")


@plugin_pool.register_plugin
class TeamContainerPlugin(CMSPluginBase):
    model = TeamContainer
    name = _("Team Section")
    render_template = "cms/plugins/team_section.html"
    form = TeamContainerPluginForm
    cache = False
    allow_children = True
    child_classes = ['TeamMemberPlugin']
    module = _("Sections")


@plugin_pool.register_plugin
class TeamMemberPlugin(CMSPluginBase):
    model = TeamMember
    name = _("Team Member")
    render_template = "cms/plugins/team_member.html"
    cache = False
    require_parent = True
    parent_classes = ['TeamContainerPlugin']
    form = TeamMemberPluginForm
    module = _("Sections")

@plugin_pool.register_plugin
class ContactInfoPlugin(CMSPluginBase):
    model = ContactInfoPluginModel
    module = _("Sections")
    name = _("Contact Info")
    render_template = "cms/plugins/contact_info.html"
    form = ContactInfoPluginForm
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context
@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = FooterPluginModel
    name = _("Footer Section")
    render_template = "cms/plugins/footer.html"
    form = FooterPluginForm
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FeaturedServicesSectionPlugin(CMSPluginBase):
    model = FeaturedServicesSection
    name = _("Featured Services Section")
    render_template = "cms/plugins/featured_services_section.html"
    allow_children = True
    child_classes = ["FeaturedServicesItemPlugin"]  # если у тебя есть элементы
    form = FeaturedServicesSectionPluginForm
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FeaturedServiceItemPlugin(CMSPluginBase):
    model = FeaturedServiceItem
    name = _("Featured Service Item")
    render_template = "cms/plugins/service_item2.html"
    require_parent = True
    parent_classes = ["FeaturedServicesSectionPlugin"]
    form = FeaturedServiceItemPluginForm
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
