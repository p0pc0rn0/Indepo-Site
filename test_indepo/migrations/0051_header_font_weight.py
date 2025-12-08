from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0050_copy_expandable_documents_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="headerpluginmodel",
            name="chip_font_weight",
            field=models.CharField(
                blank=True,
                default="500",
                help_text="Например: 400, 500, 600",
                max_length=10,
                verbose_name="Толщина шрифта плашек",
            ),
        ),
        migrations.AddField(
            model_name="headerpluginmodel",
            name="chip_hover_font_weight",
            field=models.CharField(
                blank=True,
                default="600",
                help_text="Например: 500 или 600",
                max_length=10,
                verbose_name="Толщина шрифта при наведении",
            ),
        ),
    ]
