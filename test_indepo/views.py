from __future__ import annotations

from typing import List

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.http import JsonResponse
from django.utils.text import Truncator
from django.utils.translation import gettext as _
from django.views import View

from cms.models import PageContent
from djangocms_versioning.constants import PUBLISHED
from djangocms_versioning.models import Version

from .models import DocumentItemPluginModel


class GlobalSearchView(View):
    """
    Return JSON with search results across published CMS pages and document plugins.
    Intended for AJAX/Fetch consumption by the floating navigation search overlay.
    """

    page_limit = 8
    document_limit = 6
    total_limit = 14

    def get(self, request, *args, **kwargs):
        query = (request.GET.get("q") or "").strip()
        if not query:
            return JsonResponse({"results": []})

        language = getattr(request, "LANGUAGE_CODE", settings.LANGUAGE_CODE)
        site = get_current_site(request)

        page_results = self._search_pages(request, query, language, site_id=site.id)
        document_results = self._search_documents(request, query)

        combined: List[dict] = []
        combined.extend(page_results[: self.page_limit])
        combined.extend(document_results[: self.document_limit])

        return JsonResponse({"results": combined[: self.total_limit]})

    def _search_pages(self, request, query: str, language: str, site_id: int) -> List[dict]:
        pagecontent_ct = ContentType.objects.get_for_model(PageContent)
        base_qs = PageContent.objects.filter(
            language=language,
            page__site_id=site_id,
            page__is_page_type=False,
        ).select_related("page")

        published_ids = Version.objects.filter(
            content_type=pagecontent_ct,
            state=PUBLISHED,
            object_id__in=base_qs.values_list("pk", flat=True),
        ).values_list("object_id", flat=True)

        contents = (
            base_qs.filter(pk__in=published_ids)
            .filter(
                Q(title__icontains=query)
                | Q(page_title__icontains=query)
                | Q(menu_title__icontains=query)
                | Q(meta_description__icontains=query)
            )
            .order_by("title")[: self.page_limit]
        )

        results = []
        for content in contents:
            page = content.page
            url = page.get_absolute_url(language=language)
            results.append(
                {
                    "type": "page",
                    "title": content.title or content.page_title or page.get_title(language) or "",
                    "url": request.build_absolute_uri(url),
                    "label": _("Страница"),
                    "description": Truncator(content.meta_description or "").chars(160),
                    "icon": "bi bi-collection-play",
                }
            )
        return results

    def _search_documents(self, request, query: str) -> List[dict]:
        term = query.casefold()
        seen = set()
        results = []
        documents = (
            DocumentItemPluginModel.objects.select_related("cmsplugin_ptr")
            .order_by("-cmsplugin_ptr__changed_date", "-pk")
            .iterator()
        )

        seen_names = set()

        for document in documents:
            normalized_name = (document.name or "").strip().casefold()
            if normalized_name in seen_names:
                continue
            haystack = " ".join(filter(None, [document.name, document.description])).casefold()
            if term not in haystack:
                continue
            normalized_url = self._build_absolute_document_url(request, document.url)
            if not normalized_url:
                continue
            key = normalized_url
            if key in seen:
                continue
            seen.add(key)
            seen_names.add(normalized_name)
            results.append(
                {
                    "type": "document",
                    "title": document.name,
                    "url": normalized_url,
                    "label": _("Документ"),
                    "description": Truncator(document.description or "").chars(160),
                    "icon": "bi bi-file-earmark-text",
                    "external": normalized_url.startswith(("http://", "https://")),
                }
            )
            if len(results) >= self.document_limit * 2:
                break
        return results

    def _build_absolute_document_url(self, request, url: str) -> str:
        if not url:
            return ""
        if url.startswith(("http://", "https://", "mailto:", "tel:")):
            return url
        if url.startswith("//"):
            scheme = "https:" if request.is_secure() else "http:"
            return f"{scheme}{url}"
        if not url.startswith("/"):
            url = f"/{url}"
        return request.build_absolute_uri(url)
