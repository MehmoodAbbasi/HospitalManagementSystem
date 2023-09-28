from django.urls import path,include

from .views import *
from . import views
from django.contrib.auth import views as aut_views
urlpatterns = [
    # path(r'', include(router.urls)),
    path('',views.index,name='index'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('patient_list/',views.patient_list,name='patient_list'),
    path('add_staff/',views.add_staff,name='add_staff'),
    path('staff_list/',views.staff_list,name='staff_list'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('doctor_list/',views.doctor_list,name='doctor_list'),
    path('add_appointment/',views.add_appointment,name='add_appointment'),
    path('appointment_list/',views.appointment_list,name='appointment_list'),
    path('add_medical_record/',views.add_medical_record,name='add_medical_record'),
    path('medical_records/',views.medical_records,name='medical_records'),
    path('add_inventory/',views.add_inventory,name='add_inventory'),
    path('inventory_list/',views.inventory_list,name='inventory_list'),
    path('billing/',views.billing,name='billing'),
    path('view_bill/',views.view_bill,name='view_bill'),










    path('user_register/',views.register,name='user_register'),
    path('login/',aut_views.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',views.logout,name='logout'),
    

]