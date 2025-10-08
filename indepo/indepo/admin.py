from django.contrib import admin
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from .models import HeroSectionPluginModel, FaqSectionPluginModel, FaqItemPluginModel

# Кастомный виджет для CKEditor
class CKEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'djangocms-ckeditor'
        rendered = super().render(name, value, attrs, renderer)
        return mark_safe(
            rendered + '''
            <script src="/static/djangocms_text_ckeditor/ckeditor/ckeditor.js"></script>
            <script>
                CKEDITOR.replace('{}', {{
                    toolbar: 'CMS',
                    skin: 'moono-lisa',
                    language: 'ru'
                }});
            </script>
            '''.format(name)
        )

class HeroSectionPluginModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

class FaqItemPluginModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(HeroSectionPluginModel, HeroSectionPluginModelAdmin)
admin.site.register(FaqSectionPluginModel)
admin.site.register(FaqItemPluginModel, FaqItemPluginModelAdmin)
