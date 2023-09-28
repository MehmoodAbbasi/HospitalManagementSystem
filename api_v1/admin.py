from django.contrib import admin
from api_v1.models import *
# Register your models here.


class DoctorAccountModel(admin.ModelAdmin):
    list_display=('id','user','first_name','last_name','adress','phone','email','specialization','profile_image')
admin.site.register(Doctor,DoctorAccountModel)


class PatientAccountModel(admin.ModelAdmin):
    list_display=('id','first_name','last_name','adress','phone','email',
'current_medication','profile_image')
admin.site.register(Patient,PatientAccountModel)

class StaffAccountModel(admin.ModelAdmin):
    list_display=('id','first_name','last_name','phone','email',
'job_title','profile_image')
admin.site.register(Staff,StaffAccountModel)

class AppointmentAccountModel(admin.ModelAdmin):
    list_display=('id','doctor','patient','appointment_date')
admin.site.register(Appointment,AppointmentAccountModel)

class MedicalRecordAccountModel(admin.ModelAdmin):
    list_display=('id','doctor_name','patient_name','remarks')
admin.site.register(MedicalReocrd,MedicalRecordAccountModel)


class inventryAccountModel(admin.ModelAdmin):
    list_display=('id','item_name','quantity','unit_price')
admin.site.register(Inventory,inventryAccountModel)

class BillingAccountModel(admin.ModelAdmin):
    list_display=('id','patient_name','item_name','total_amount','invoice_date')
admin.site.register(Billing,BillingAccountModel)

