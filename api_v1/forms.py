from django import forms
from api_v1.models import *

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
        model = Users
        fields= ('__all__')
