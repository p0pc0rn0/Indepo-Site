from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0022_documents_section_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documentsubsectionpluginmodel",
            name="description",
            field=djangocms_text_ckeditor.fields.HTMLField(
                blank=True,
                default="",
                verbose_name="Description",
            ),
        ),
    ]
