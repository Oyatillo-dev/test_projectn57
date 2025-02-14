#from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from common.views import home_page
from Main_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)