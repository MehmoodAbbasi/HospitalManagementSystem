from django.urls import path,include
from api_v1.routers import router
from .views import *
from . import views
urlpatterns = [
    # path(r'', include(router.urls)),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('create/',ProductCreateView.as_view(),name = 'add_products'),
    path('add_students/',StudenttCreateView.as_view(),name = 'add_students'),
    path('create_user/',UserCreateView.as_view(),name = 'create_user'),
    path('update_student/<int:pk>/',StudentUpdateView.as_view(),name="update_student"),
    path('update_product/<int:pk>/',ProductUpdateView.as_view(),name="update_product"),
    # path('delete_student/<int:pk>/',StudentDeleteView.as_view(),name="delete_student"),

]
