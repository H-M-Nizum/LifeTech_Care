from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SpecializationModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
class DesignationModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class AvailableTimeModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class DoctorModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/')
    designation = models.ManyToManyField(DesignationModel)
    specialization = models.ManyToManyField(SpecializationModel)
    available_time = models.ManyToManyField(AvailableTimeModel)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    