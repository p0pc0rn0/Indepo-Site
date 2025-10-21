from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0018_headerpluginmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="icon_size",
            field=models.CharField(
                choices=[("sm", "Small"), ("md", "Medium"), ("lg", "Large")],
                default="md",
                max_length=2,
                verbose_name="Icon size",
            ),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="layout_variant",
            field=models.CharField(
                choices=[("vertical", "Vertical"), ("inline", "Inline")],
                default="vertical",
                max_length=8,
                verbose_name="Layout variant",
            ),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="ok_url",
            field=models.URLField(blank=True, default="", verbose_name="Odnoklassniki URL"),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="show_labels",
            field=models.BooleanField(default=False, verbose_name="Show labels near icons"),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="tg_url",
            field=models.URLField(
                blank=True,
                default="",
                help_text="Например: https://t.me/your_channel или tg://resolve?domain=your_channel",
                verbose_name="Telegram URL",
            ),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="vk_url",
            field=models.URLField(blank=True, default="", verbose_name="VK URL"),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="work_hours_text",
            field=models.TextField(blank=True, default="", verbose_name="Work hours"),
        ),
        migrations.AddField(
            model_name="contactinfopluginmodel",
            name="work_hours_title",
            field=models.CharField(
                blank=True,
                default="Время работы",
                max_length=120,
                verbose_name="Work hours title",
            ),
        ),
    ]
