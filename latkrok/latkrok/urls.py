from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

'''i18n_urls = (
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
)'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('main.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
