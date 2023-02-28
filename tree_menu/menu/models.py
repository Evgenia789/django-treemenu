from django.db import models


class Menu(models.Model):
    """A class representing a menu object."""
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Title"
    )
    slug = models.SlugField(max_length=255, verbose_name="Slug")

    class Meta:
        ordering = ("title",)
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return str(self.title)


class Submenu(models.Model):
    """A class representing a submenu object."""
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name="submenus",
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="childrens",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Submenu"
        verbose_name_plural = "Submenus"

    def __str__(self):
        return self.title
