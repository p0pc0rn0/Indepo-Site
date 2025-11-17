from django.db import migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0039_socialinitiativessectionpluginmodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialinitiativecardpluginmodel",
            name="description",
            field=djangocms_text_ckeditor.fields.HTMLField(
                blank=True,
                default="",
                verbose_name="Description",
            ),
        ),
    ]
