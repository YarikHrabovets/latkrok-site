from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('tinymce/', include('tinymce.urls'))
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
)


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ] + urlpatterns

handler404 = 'main.views.page_not_found_view'
