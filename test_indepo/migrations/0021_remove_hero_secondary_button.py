from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0020_alter_contactinfopluginmodel_translation_subtitle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="herosectionpluginmodeltranslation",
            name="telegram_text",
        ),
        migrations.RemoveField(
            model_name="herosectionpluginmodel",
            name="telegram_url",
        ),
    ]
