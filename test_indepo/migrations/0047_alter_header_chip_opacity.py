from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_indepo", "0046_header_theme_colors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="headerpluginmodel",
            name="chip_opacity",
            field=models.PositiveIntegerField(
                blank=True, null=True, default=12, help_text="0-100, фон быстрых иконок", verbose_name="Прозрачность плашек (%)"
            ),
        ),
        migrations.AlterField(
            model_name="headerpluginmodel",
            name="chip_hover_opacity",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                default=25,
                help_text="0-100, фон при hover",
                verbose_name="Прозрачность плашек при наведении (%)",
            ),
        ),
    ]
