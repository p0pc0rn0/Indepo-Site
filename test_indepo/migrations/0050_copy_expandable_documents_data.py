from django.db import migrations

def copy_to_documents(apps, schema_editor):
    connection = schema_editor.connection
    tables = connection.introspection.table_names()
    old_section = "test_indepo_expandablehighlightssectionpluginmodel"
    old_card = "test_indepo_expandablehighlightcardpluginmodel"
    new_section = "test_indepo_documentsshowcasesectionpluginmodel"
    new_card = "test_indepo_documentsshowcasecardpluginmodel"

    with connection.cursor() as cursor:
        if old_section in tables:
            cursor.execute(
                f"""
                INSERT INTO {new_section} (cmsplugin_ptr_id, title, subtitle)
                SELECT old.cmsplugin_ptr_id, old.title, old.subtitle
                FROM {old_section} AS old
                WHERE NOT EXISTS (
                    SELECT 1 FROM {new_section} AS new
                    WHERE new.cmsplugin_ptr_id = old.cmsplugin_ptr_id
                )
                """
            )
        if old_card in tables:
            cursor.execute(
                f"""
                INSERT INTO {new_card} (cmsplugin_ptr_id, title, teaser, full_text, button_label, image_id, section_id)
                SELECT old.cmsplugin_ptr_id, old.title, old.teaser, old.full_text, old.button_label, old.image_id, old.section_id
                FROM {old_card} AS old
                WHERE NOT EXISTS (
                    SELECT 1 FROM {new_card} AS new
                    WHERE new.cmsplugin_ptr_id = old.cmsplugin_ptr_id
                )
                """
            )

def copy_back_to_expandable(apps, schema_editor):
    connection = schema_editor.connection
    tables = connection.introspection.table_names()
    old_section = "test_indepo_expandablehighlightssectionpluginmodel"
    old_card = "test_indepo_expandablehighlightcardpluginmodel"
    new_section = "test_indepo_documentsshowcasesectionpluginmodel"
    new_card = "test_indepo_documentsshowcasecardpluginmodel"

    with connection.cursor() as cursor:
        if old_section in tables:
            cursor.execute(
                f"""
                INSERT INTO {old_section} (cmsplugin_ptr_id, title, subtitle)
                SELECT new.cmsplugin_ptr_id, new.title, new.subtitle
                FROM {new_section} AS new
                WHERE NOT EXISTS (
                    SELECT 1 FROM {old_section} AS old
                    WHERE old.cmsplugin_ptr_id = new.cmsplugin_ptr_id
                )
                """
            )
        if old_card in tables:
            cursor.execute(
                f"""
                INSERT INTO {old_card} (cmsplugin_ptr_id, title, teaser, full_text, button_label, image_id, section_id)
                SELECT new.cmsplugin_ptr_id, new.title, new.teaser, new.full_text, new.button_label, new.image_id, new.section_id
                FROM {new_card} AS new
                WHERE NOT EXISTS (
                    SELECT 1 FROM {old_card} AS old
                    WHERE old.cmsplugin_ptr_id = new.cmsplugin_ptr_id
                )
                """
            )


class Migration(migrations.Migration):

    dependencies = [
        ("test_indepo", "0049_rename_documents_plugin_types"),
    ]

    operations = [
        migrations.RunPython(copy_to_documents, copy_back_to_expandable),
    ]
