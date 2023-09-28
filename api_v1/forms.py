from django import forms  # Import forms from django, not django.forms
from .models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input'}))
    email = forms.EmailField(error_messages={'required': 'Please enter your email address.'})
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class DoctorForm(forms.ModelForm):  # Change forms.Form to forms.ModelForm

    class Meta:
        model = Doctor
        fields = '__all__'
