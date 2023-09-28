from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from api_v1.views import *
from api_v1 import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api_v1.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)