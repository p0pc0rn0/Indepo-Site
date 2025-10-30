import re

from django import template
from django.utils.text import slugify

register = template.Library()


@register.simple_tag
def resolve_nav_icon(icon_map, default_icons, page_id, title):
    """
    Pick the most suitable icon class for a menu node.

    Preference order:
    1. Explicit override from NavigationIcon objects (icon_map).
    2. Matching key inside the default icon dictionary. We try several
       normalized variants of the title to be resilient to locale changes.
    3. Graceful fallback icon.
    """

    if icon_map and page_id in icon_map:
        return icon_map[page_id]

    if not default_icons:
        return "bi bi-app-indicator"

    raw_title = (title or "").strip()
    if not raw_title:
        return default_icons.get("__fallback__", "bi bi-app-indicator")

    candidates = []
    ascii_slug = slugify(raw_title or "", allow_unicode=False)
    unicode_slug = slugify(raw_title or "", allow_unicode=True)
    collapsed_spaces = re.sub(r"\s+", " ", raw_title).casefold()
    dashed = collapsed_spaces.replace(" ", "-")
    compact = collapsed_spaces.replace(" ", "")

    candidates.extend(
        filter(
            None,
            {
                ascii_slug,
                unicode_slug,
                collapsed_spaces,
                dashed,
                compact,
            },
        )
    )

    for candidate in candidates:
        if candidate in default_icons:
            return default_icons[candidate]

    return default_icons.get("__fallback__", "bi bi-app-indicator")
