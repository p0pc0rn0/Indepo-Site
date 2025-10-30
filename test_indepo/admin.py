from django.contrib import admin
from .models import NavigationIcon

@admin.register(NavigationIcon)
class NavigationIconAdmin(admin.ModelAdmin):
    list_display = ("page", "icon_class")
    search_fields = ("page__title", "icon_class")
