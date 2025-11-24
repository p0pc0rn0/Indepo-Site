from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0045_header_search_placeholder_and_chip_opacity"),
    ]

    operations = [
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_background",
            field=models.CharField(blank=True, default="#ffffff", max_length=40, verbose_name="Цвет фона поиска"),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_border",
            field=models.CharField(
                blank=True, default="rgba(15, 23, 42, 0.18)", max_length=40, verbose_name="Цвет рамки поиска"
            ),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_input_background",
            field=models.CharField(blank=True, default="#ffffff", max_length=40, verbose_name="Цвет поля поиска"),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_text_color",
            field=models.CharField(blank=True, default="#0f172a", max_length=40, verbose_name="Цвет текста поиска"),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="search_placeholder_color",
            field=models.CharField(
                blank=True, default="#6b7280", max_length=40, verbose_name="Цвет плейсхолдера поиска"
            ),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="accessibility_background",
            field=models.CharField(blank=True, default="#ffffff", max_length=40, verbose_name="Фон кнопки доступности"),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="accessibility_border",
            field=models.CharField(
                blank=True,
                default="rgba(15, 23, 42, 0.2)",
                max_length=40,
                verbose_name="Рамка кнопки доступности",
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
            name="chip_hover_opacity",
            field=models.PositiveIntegerField(
                default=25, help_text="0-100, фон при hover", verbose_name="Прозрачность плашек при наведении (%)"
            ),
        ),
    ]
