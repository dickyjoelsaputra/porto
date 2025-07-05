from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail import hooks
from personal.models import Portfolio


@register_snippet
class PortfolioAdmin(SnippetViewSet):
    add_to_admin_menu = True
    model = Portfolio
    icon = "tasks"
    menu_label = "Portfolio"
    menu_order = 10
    list_display = ["modal_id", "category", "title", "project_link"]
    search_fields = ["modal_id", "category", "title", "description"]