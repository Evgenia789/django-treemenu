from django.contrib import admin

from menu.models import Menu, Submenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    MenuAdmin class for editing Menu models
    in the admin zone interface.
    """
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Submenu)
class SubmenuAdmin(admin.ModelAdmin):
    """
    SubmenuAdmin class for editing Submenu models
    in the admin zone interface.
    """
    list_display = ("title", "menu", "parent")
    list_filter = ("menu", "parent")
    search_fields = ("menu__title", "parent__title")
    prepopulated_fields = {"slug": ("title", )}
    fieldsets = (("Add new submenu", {
            "description": "Select the parent for the submenu, if necessary",
            "fields": (("menu", "parent"), "title", "slug")
            }),)
