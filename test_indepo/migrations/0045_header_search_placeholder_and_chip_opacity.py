from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0040_alter_socialinitiativecardpluginmodel_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="headerpluginmodel",
            name="chip_hover_opacity",
            field=models.PositiveIntegerField(
                default=25,
                help_text="0-100, фон при hover",
                verbose_name="Прозрачность плашек при наведении (%)",
            ),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="chip_opacity",
            field=models.PositiveIntegerField(
                default=12, help_text="0-100, фон быстрых иконок", verbose_name="Прозрачность плашек (%)"
            ),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_placeholder_color",
            field=models.CharField(
                blank=True, default="#6b7280", max_length=40, verbose_name="Цвет плейсхолдера поиска"
            ),
        ),
    ]
