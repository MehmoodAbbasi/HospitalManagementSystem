from django.db import models


# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    image = models.ImageField(width_field=None, height_field=None)
    phone = models.IntegerField()
    # is_deleted=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=25)
    value=models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.name
    

class Student(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name