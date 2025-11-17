from __future__ import annotations

from typing import List

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.utils.text import Truncator
from django.utils.translation import gettext as _
from django.views import View

from cms.models import PageContent, CMSPlugin
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

        contents = base_qs.filter(pk__in=published_ids).order_by("title")

        results = []
        term = query.casefold()
        for content in contents:
            haystack = " ".join(
                filter(
                    None,
                    [
                        content.title or "",
                        content.page_title or "",
                        content.menu_title or "",
                        content.meta_description or "",
                    ],
                )
            ).casefold()
            if not term or term not in haystack:
                continue
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
            if len(results) >= self.page_limit:
                break
        return results

    def _search_documents(self, request, query: str) -> List[dict]:
        term = query.casefold()
        seen = set()
        results = []

        language = getattr(request, "LANGUAGE_CODE", settings.LANGUAGE_CODE)

        pagecontent_ct = ContentType.objects.get_for_model(PageContent)
        published_pagecontent_ids = set(
            Version.objects.filter(content_type=pagecontent_ct, state=PUBLISHED).values_list("object_id", flat=True)
        )

        documents = (
            DocumentItemPluginModel.objects.select_related(
                "cmsplugin_ptr",
                "cmsplugin_ptr__placeholder",
                "cmsplugin_ptr__placeholder__page",
            )
            .filter(cmsplugin_ptr__language=language)
            .order_by("-cmsplugin_ptr__changed_date", "-pk")
            .iterator()
        )

        latest_by_plugin = {}
        for document in documents:
            plugin = document.cmsplugin_ptr
            # ensure placeholder's page (if any) is published
            placeholder = getattr(plugin, "placeholder", None)
            if placeholder is None:
                continue
            page = getattr(placeholder, "page", None)
            if page and getattr(page, "publisher_is_draft", False):
                continue
            source = getattr(placeholder, "source", None)
            if source and source.pk not in published_pagecontent_ids:
                continue
            key = getattr(plugin, "publisher_public_id", None) or plugin.pk
            current = latest_by_plugin.get(key)
            if not current or document.cmsplugin_ptr.changed_date > current.cmsplugin_ptr.changed_date:
                latest_by_plugin[key] = document

        seen_names = set()

        for document in latest_by_plugin.values():
            normalized_name = (document.name or "").strip().casefold()
            if normalized_name in seen_names:
                continue
            haystack = " ".join(filter(None, [document.name, document.description])).casefold()
            if term not in haystack:
                continue
            normalized_url = document.get_absolute_link(request)
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
                    "external": document.is_external,
                }
            )
            if len(results) >= self.document_limit * 2:
                break
        return results
