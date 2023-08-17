from django.contrib import admin
from django.urls import path,include
from api_v1.routers import router
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/',include('api_v1.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)