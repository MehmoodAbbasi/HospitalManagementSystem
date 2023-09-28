from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Doctor(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    dob = models.DateField()
    phone = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    adress = models.TextField()
    specialization  = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='images/')

    created_on = models.DateTimeField( auto_now_add=True)
    updated_on = models.DateTimeField( auto_now=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural ="Doctors"
        
class Staff(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),

    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    dob = models.DateField()
    phone = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    adress = models.TextField()
    job_title  = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='images/')

    created_on = models.DateTimeField( auto_now_add=True)
    updated_on = models.DateTimeField( auto_now=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural ="Staff"

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),

    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    dob = models.DateField()
    phone = models.CharField( max_length=50)
    email = models.EmailField(unique=True)
    adress = models.TextField()
    current_medication   = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='images/')

    created_on = models.DateTimeField( auto_now_add=True)
    updated_on = models.DateTimeField( auto_now=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural ="Patient"



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)       
    appointment_date = models.DateField()

    def __str__(self):
        return  f"Appointment on {self.appointment_date} with Dr. {self.doctor}"
    

class MedicalReocrd(models.Model):
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=250)
    date = models.DateField()
    def __str__(self):
        return self.remarks
    
class Inventory(models.Model):
    item_name = models.CharField(max_length=250)    
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.item_name

class Billing(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)   
    item_name = models.ForeignKey(Inventory, verbose_name='item name', on_delete=models.CASCADE, related_name='billings_with_item_name')
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    invoice_date = models.DateField()
    def __str__(self):
        return  f"Billing on {self.invoice_date} of Mr. {self.patient_name}"  