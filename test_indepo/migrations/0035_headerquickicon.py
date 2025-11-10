from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0034_navigationicon"),
    ]

    operations = [
        migrations.CreateModel(
            name="HeaderQuickIcon",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                (
                    "slot",
                    models.CharField(
                        choices=[("left", "Левая группа (контакты)"), ("right", "Правая группа (соцсети)")],
                        default="left",
                        max_length=10,
                        verbose_name="Slot",
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        help_text="Название иконки для скринридеров и CMS.",
                        max_length=150,
                        verbose_name="Label",
                    ),
                ),
                (
                    "tooltip",
                    models.CharField(
                        blank=True,
                        help_text="Отображается во всплывающем окошке (например, номер телефона или почта).",
                        max_length=255,
                        verbose_name="Tooltip text",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True,
                        help_text="Например: https://vk.com/..., mailto:info@example.com или tel:+74951234567",
                        max_length=255,
                        verbose_name="URL / action",
                    ),
                ),
                ("open_in_new_tab", models.BooleanField(default=False, verbose_name="Open in new tab")),
                (
                    "icon_class",
                    models.CharField(
                        default="bi bi-telegram",
                        help_text="Например: bi bi-telegram",
                        max_length=80,
                        verbose_name="Bootstrap icon class",
                    ),
                ),
                (
                    "background_color",
                    models.CharField(blank=True, default="#e0edff", max_length=40, verbose_name="Background color"),
                ),
                ("icon_color", models.CharField(blank=True, default="#1d4ed8", max_length=40, verbose_name="Icon color")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Display order")),
                (
                    "plugin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quick_icons",
                        to="test_indepo.headerpluginmodel",
                        verbose_name="Header plugin",
                    ),
                ),
            ],
            options={
                "ordering": ("slot", "order", "pk"),
                "verbose_name": "Header quick icon",
                "verbose_name_plural": "Header quick icons",
            },
        ),
    ]
