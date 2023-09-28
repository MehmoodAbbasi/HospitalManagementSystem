from django.shortcuts import redirect , render
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404

from api_v1.models import *
from api_v1.forms import *
from django.contrib.auth.decorators import login_required




def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
          
        return redirect('login')



def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the actual URL or view name
    else:
        form = CreateUserForm()

    context = {
        'form': form,
    }
    return render(request, 'user_register.html', context)
def login(request):
        return  render(request,'login.html')

def logout(request):
        auth_logout(request)
        return  redirect('login')

def add_doctor(request):
    users = User.objects.all()

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()    
            # Redirect or do something else upon successful form submission
    else:
        form = DoctorForm()

    context = {
        'form': form,
        'users': users,
        'gender_choices': Doctor.GENDER_CHOICES,
    }

    return render(request, 'add_doctor.html', context)

def doctor_list(request):
        doctor = Doctor.objects.all()
        context = {
              'doctor':doctor
    }
        return  render(request,'doctor_list.html', context)

def add_staff(request):
        return  render(request,'add_staff.html')

def staff_list(request):
        return  render(request,'staff_list.html')

def add_patient(request):
        return  render(request,'add_patient.html')

def patient_list(request):
        return  render(request,'patient_list.html')

def add_appointment(request):
        return  render(request,'add_appointment.html')


def appointment_list(request):
        return  render(request,'appointment_list.html')

def billing(request):
        return  render(request,'billings.html')
def view_bill(request):
        return  render(request,'view_bill.html')

def add_medical_record(request):
        return  render(request,'add_medical_record.html')

def medical_records(request):
        return  render(request,'medical_record_list.html')

def add_inventory(request):
        return  render(request,'add_inventory.html')

def inventory_list(request):
        return  render(request,'inventory_list.html')
