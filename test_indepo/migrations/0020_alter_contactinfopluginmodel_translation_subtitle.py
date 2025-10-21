from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0019_contactinfopluginmodel_extra_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactinfopluginmodeltranslation",
            name="subtitle",
            field=models.CharField(
                blank=True,
                default="<span>Need Help?</span> <span class='description-title'>Contact Us</span>",
                max_length=255,
            ),
        ),
    ]
