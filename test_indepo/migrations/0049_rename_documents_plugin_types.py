from django.db import migrations

forward_mapping = (
    ("ExpandableHighlightsSectionPlugin", "DocumentsShowcaseSectionPlugin"),
    ("ExpandableHighlightCardPlugin", "DocumentsShowcaseCardPlugin"),
)

def rename_plugins(apps, schema_editor, mapping=forward_mapping):
    CMSPlugin = apps.get_model("cms", "CMSPlugin")
    for old, new in mapping:
        CMSPlugin.objects.filter(plugin_type=old).update(plugin_type=new)

def reverse_rename_plugins(apps, schema_editor):
    reverse_map = tuple((new, old) for old, new in forward_mapping)
    rename_plugins(apps, schema_editor, mapping=reverse_map)


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0048_documentsshowcasepluginmodel_and_more"),
    ]

    operations = [
        migrations.RunPython(rename_plugins, reverse_rename_plugins),
    ]
