from django.urls import path,include
from api_v1.routers import router
from .views import *
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path(r'', include(router.urls)),
    path('',views.index,name='index'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',views.RegisterView,name='register'),
    path('logout/',views.logout,name='logout'),
    path('create/',ProductCreateView.as_view(),name = 'add_products'),
    path('add_students/',StudenttCreateView.as_view(),name = 'add_students'),
    path('create_user/',UserCreateView.as_view(),name = 'create_user'),
    path('update_student/<int:pk>/',StudentUpdateView.as_view(),name="update_student"),
    path('update_product/<int:pk>/',ProductUpdateView.as_view(),name="update_product"),
    # path('delete_student/<int:pk>/',StudentDeleteView.as_view(),name="delete_student"),

]
