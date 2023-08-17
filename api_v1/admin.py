from django.contrib import admin
from api_v1.models import *
# Register your models here.


class UserAccountModel(admin.ModelAdmin):
    list_display=('id','name','father_name','city_name','email','adress','image','phone')


admin.site.register(Users,UserAccountModel)
class ProductAccountModel(admin.ModelAdmin):
    list_display = ('id','name','value','date')

admin.site.register(Product,ProductAccountModel)


class StudentModel(admin.ModelAdmin):
    list_display = ('id','name','father_name','group','roll_no','subject_name')
admin.site.register(Student,StudentModel)