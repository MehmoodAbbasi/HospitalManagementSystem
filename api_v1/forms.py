from django import forms
from api_v1.models import *
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields= ('__all__')

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields= ('__all__')


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields= ('__all__')
