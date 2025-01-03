from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path("", include('meteo.urls')),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)