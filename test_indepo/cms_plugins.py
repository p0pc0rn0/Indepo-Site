from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import (
    TopBarPluginModel,
    ServicesSectionPluginModel,
    ServiceItemPluginModel,
    TestimonialsSectionPluginModel,
    TestimonialItemPluginModel,
    TeamContainer,
    TeamMember,
    ContactInfoPluginModel,
    FooterPluginModel,
    FeaturedServicesSection,
    FeaturedServiceItem
)

@plugin_pool.register_plugin
class TopBarPlugin(CMSPluginBase):
    model = TopBarPluginModel
    name = _("Top Bar")
    render_template = "cms/plugins/topbar.html"
    cache = False

@plugin_pool.register_plugin
class ServicesSectionPlugin(CMSPluginBase):
    model = ServicesSectionPluginModel
    name = _("Services Section")
    render_template = "cms/plugins/services_section.html"
    cache = False
    allow_children = True
    child_classes = ['ServiceItemPlugin']
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        # передаём детей для рендера в шаблон
        context['instance'] = instance
        context['children'] = instance.get_children()
        return context

@plugin_pool.register_plugin
class ServiceItemPlugin(CMSPluginBase):
    model = ServiceItemPluginModel
    name = _("Service Item")
    render_template = "cms/plugins/service_item.html"
    require_parent = True
    parent_classes = ['ServicesSectionPlugin']
    cache = False
    module = _("Sections")

@plugin_pool.register_plugin
class TestimonialsSectionPlugin(CMSPluginBase):
    model = TestimonialsSectionPluginModel
    name = _("Testimonials Section")
    render_template = "cms/plugins/testimonials_section.html"
    cache = False
    allow_children = True
    child_classes = ['TestimonialItemPlugin']
    module = _("Sections")

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        context['children'] = instance.get_children()
        return context

@plugin_pool.register_plugin
class TestimonialItemPlugin(CMSPluginBase):
    model = TestimonialItemPluginModel
    name = _("Testimonial Item")
    render_template = "cms/plugins/testimonial_item.html"
    require_parent = True
    parent_classes = ['TestimonialsSectionPlugin']
    cache = False
    module = _("Sections")


@plugin_pool.register_plugin
class TeamContainerPlugin(CMSPluginBase):
    model = TeamContainer
    name = _("Team Section")
    render_template = "cms/plugins/team_section.html"
    cache = False
    allow_children = True
    child_classes = ['TeamMemberPlugin']


@plugin_pool.register_plugin
class TeamMemberPlugin(CMSPluginBase):
    model = TeamMember
    name = _("Team Member")
    render_template = "cms/plugins/team_member.html"
    cache = False
    require_parent = True
    parent_classes = ['TeamContainerPlugin']

@plugin_pool.register_plugin
class ContactInfoPlugin(CMSPluginBase):
    model = ContactInfoPluginModel
    module = _("Sections")
    name = _("Contact Info")
    render_template = "cms/plugins/contact_info.html"
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = FooterPluginModel
    name = _("Footer Section")
    render_template = "cms/plugins/footer.html"
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
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["instance"] = instance
        return context

@plugin_pool.register_plugin
class FeaturedServiceItemPlugin(CMSPluginBase):
    model = FeaturedServiceItem
    name = _("Service Item")
    render_template = "cms/plugins/service_item2.html"
    require_parent = True
    parent_classes = ["FeaturedServicesSectionPlugin"]
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
