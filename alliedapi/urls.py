from django.contrib import admin
from django.urls import path,include
from api_v1.routers import router
from django.conf import settings
from django.conf.urls.static import static
from api_v1.views import *
from api_v1 import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/',include('api_v1.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)