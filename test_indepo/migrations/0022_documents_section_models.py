from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("test_indepo", "0021_remove_hero_secondary_button"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentsSectionPluginModel",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="Title",
                    ),
                ),
                (
                    "show_search",
                    models.BooleanField(
                        default=True,
                        verbose_name="Show search field",
                    ),
                ),
                (
                    "show_empty_sections",
                    models.BooleanField(
                        default=True,
                        verbose_name="Show empty subsections",
                    ),
                ),
                (
                    "layout_variant",
                    models.CharField(
                        choices=[("list", "List"), ("accordion", "Accordion")],
                        default="list",
                        max_length=20,
                        verbose_name="Layout variant",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="DocumentSubsectionPluginModel",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=200,
                        verbose_name="Subsection title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        verbose_name="Description",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="DocumentItemPluginModel",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        verbose_name="Document name",
                    ),
                ),
                (
                    "url",
                    models.URLField(verbose_name="Document URL"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="",
                        verbose_name="Short description",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
