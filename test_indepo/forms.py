from parler.forms import TranslatableModelForm

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


class FeaturedServicesSectionPluginForm(TranslatableModelForm):
    class Meta:
        model = FeaturedServicesSection
        fields = "__all__"


class FeaturedServiceItemPluginForm(TranslatableModelForm):
    class Meta:
        model = FeaturedServiceItem
        fields = "__all__"
