from typing import Dict, List

from django import template
from django.db.models.query import QuerySet
from django.utils.datastructures import MultiValueDictKeyError

from menu.models import Submenu

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: Dict[str, any], menu: str) -> Dict[str, any]:
    """
    Generates a dictionary of menu items for the specified menu.
    """
    result_dict = {'menu': menu}

    try:
        items = Submenu.objects.filter(menu__title=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_slug = context['request'].GET[menu]
        selected_item = items.get(slug=selected_item_slug)
        selected_item_ids = get_selected_item_ids(selected_item)
        for item in primary_item:
            if item['id'] in selected_item_ids:
                item['child_items'] = get_child_items(
                    items=items_values,
                    parent_id=item['id'],
                    selected_item_ids=selected_item_ids
                )

    except MultiValueDictKeyError:
        pass

    result_dict['items'] = primary_item

    return result_dict


def get_child_items(items: QuerySet, parent_id: int,
                    selected_item_ids: List[int]) -> List[Dict]:
    """
    Recursively retrieves a list of child items
    for a given parent item ID from a queryset of items.
    """
    child_items = []
    for item in items.filter(parent_id=parent_id):
        if item['id'] in selected_item_ids:
            item['child_items'] = get_child_items(
                items=items,
                parent_id=item['id'],
                selected_item_ids=selected_item_ids
            )
        child_items.append(item)

    return child_items


def get_selected_item_ids(parent: Submenu) -> List[int]:
    """
    Retrieves a list of IDs for the given parent item
    and all of its ancestors.
    """
    selected_item_ids = []

    while parent is not None:
        selected_item_ids.append(parent.id)
        parent = parent.parent

    return selected_item_ids
