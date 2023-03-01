from django.views.generic import TemplateView


class MenuView(TemplateView):
    """
    A view that renders the index page of the menu app.
    The index page displays the main menu of the application.
    The menu items are retrieved from the database using the
    `draw_menu` template tag.
    """
    template_name = "menu/index.html"
