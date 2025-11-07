"""
URL configuration for test_indepo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from .views import GlobalSearchView

# filer лучше вынести сюда, вне i18n, чтобы не было /ru/filer/

from .views import GlobalSearchView  # импорт из origin/main

# filer — вне i18n, чтобы не было /ru/filer/
urlpatterns = [
    path('filer/', include('filer.urls')),
]

urlpatterns += i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('search/', GlobalSearchView.as_view(), name='site-search'),
    path('search/', GlobalSearchView.as_view(), name='site-search'),  # добавлено из origin/main
    path('', include('cms.urls')),
)

# медиафайлы вне i18n — правильно
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

