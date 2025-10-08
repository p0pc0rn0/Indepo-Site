from django.utils.translation import gettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import (
    ServiceTilePluginModel,
    AboutSectionPluginModel,
    AboutItemPluginModel,
    FaqSectionPluginModel,
    FaqItemPluginModel,
    HeroSectionPluginModel,
    TopBarPluginModel,
    ServicesSectionPluginModel,
    ServiceItemPluginModel,
    TestimonialsSectionPluginModel,
    TestimonialItemPluginModel,
)


@plugin_pool.register_plugin
class ServiceTilePlugin(CMSPluginBase):
    model = ServiceTilePluginModel
    name = _("Service Tile")
    render_template = "cms/plugins/service_tile.html"
    cache = False
    module = "Sections"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class AboutSectionPlugin(CMSPluginBase):
    model = AboutSectionPluginModel
    name = _("About Section")
    render_template = "cms/plugins/about_section.html"
    cache = False
    module = "Sections"
    allow_children = True
    child_classes = ['AboutItemPlugin']


@plugin_pool.register_plugin
class AboutItemPlugin(CMSPluginBase):
    model = AboutItemPluginModel
    name = _("About Item")
    render_template = "cms/plugins/about_item.html"
    cache = False
    module = "Sections"
    require_parent = True
    parent_classes = ['AboutSectionPlugin']


@plugin_pool.register_plugin
class FaqSectionPlugin(CMSPluginBase):
    model = FaqSectionPluginModel
    name = _("FAQ Section")
    render_template = "cms/plugins/faq_section.html"
    cache = False
    module = "Sections"
    allow_children = True
    child_classes = ['FaqItemPlugin']


@plugin_pool.register_plugin
class FaqItemPlugin(CMSPluginBase):
    model = FaqItemPluginModel
    name = _("FAQ Item")
    render_template = "cms/plugins/faq_item.html"
    cache = False
    module = "Sections"
    require_parent = True
    parent_classes = ['FaqSectionPlugin']


@plugin_pool.register_plugin
class HeroSectionPlugin(CMSPluginBase):
    model = HeroSectionPluginModel
    name = _("Hero Section")
    render_template = "cms/plugins/hero_section.html"
    cache = False
    module = "Sections"


@plugin_pool.register_plugin
class TopBarPlugin(CMSPluginBase):
    model = TopBarPluginModel
    name = _("Top Bar")
    render_template = "cms/plugins/topbar.html"
    cache = False
    module = "Sections"


@plugin_pool.register_plugin
class ServicesSectionPlugin(CMSPluginBase):
    model = ServicesSectionPluginModel
    name = _("Services Section")
    render_template = "cms/plugins/services_section.html"
    cache = False
    module = "Sections"
    allow_children = True
    child_classes = ['ServiceItemPlugin']


@plugin_pool.register_plugin
class ServiceItemPlugin(CMSPluginBase):
    model = ServiceItemPluginModel
    name = _("Service Item")
    render_template = "cms/plugins/service_item.html"
    cache = False
    module = "Sections"
    require_parent = True
    parent_classes = ['ServicesSectionPlugin']


@plugin_pool.register_plugin
class TestimonialsSectionPlugin(CMSPluginBase):
    model = TestimonialsSectionPluginModel
    name = _("Testimonials Section")
    render_template = "cms/plugins/testimonials_section.html"
    cache = False
    module = "Sections"
    allow_children = True
    child_classes = ['TestimonialItemPlugin']


@plugin_pool.register_plugin
class TestimonialItemPlugin(CMSPluginBase):
    model = TestimonialItemPluginModel
    name = _("Testimonial Item")
    render_template = "cms/plugins/testimonial_item.html"
    cache = False
    module = "Sections"
    require_parent = True
    parent_classes = ['TestimonialsSectionPlugin']

