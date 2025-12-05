from django.utils.cache import patch_cache_control


class BrowserCacheControlMiddleware:
    """
    Sets short-lived cache headers for HTML/JSON while disabling caching for staff / CMS toolbar.
    Keeps static/media unaffected so they can use long cache lifetimes and hashing.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        content_type = response.get("Content-Type", "")

        has_toolbar = request.COOKIES.get("cms-toolbar") or request.COOKIES.get("cms-toolbar-collapsed")
        is_staff = getattr(request.user, "is_staff", False)

        if is_staff or has_toolbar:
            patch_cache_control(
                response,
                no_cache=True,
                no_store=True,
                must_revalidate=True,
                max_age=0,
            )
        elif content_type.startswith(("text/html", "application/json")):
            patch_cache_control(
                response,
                private=True,
                max_age=300,
                stale_while_revalidate=30,
            )

        return response
