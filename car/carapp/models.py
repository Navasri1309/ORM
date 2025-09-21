from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=50)
    year=models.IntegerField()
    
class CarAdmin(admin.ModelAdmin):
    list_display=('car_name','brand','model','year')
# Create your models here.
