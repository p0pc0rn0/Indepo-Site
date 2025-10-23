from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0024_alter_documentitempluginmodel_cmsplugin_ptr_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TablePluginModel",
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
                        verbose_name="Table title",
                    ),
                ),
                (
                    "table_html",
                    djangocms_text_ckeditor.fields.HTMLField(verbose_name="Table content"),
                ),
                (
                    "footnote",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="Footnote",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
