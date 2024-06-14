from django.db import models
from datetime import datetime
import os

# Create your models here.

class Customer(models.Model):
      name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255, default='', blank=True, null=True)
      dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
      email = models.EmailField(default='', blank= True, null=True)  
      number = models.CharField(max_length=20, blank=True, null=True)
      date_created = models.DateTimeField(auto_now_add=True)
      date_choice = models.DateTimeField(default=datetime.now)
      date_time_choice = models.TimeField(default='10:00') 
      plan_choice = models.IntegerField(default=2)
      finished = models.BooleanField(default=False)
      
      def __str__(self):
            return f"{self.name} {self.last_name}"
  
  
class Appointment(models.Model):
      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      date_created = models.DateTimeField(auto_now_add=True)
      date_remember = models.DateTimeField()  # Assuming date_remember is a reminder date
      date_remember_time = models.TimeField(default='10:00')  # Time part of the reminder 

      def __str__(self):
            return f"Cita para {self.customer.name} {self.date_remember} "
      
      
      
class ServiceImage(models.Model):
      name = models.CharField(max_length=255, default='Servicio')
      image = models.ImageField(upload_to='media/')
      date_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name
      
      
class ServiceRelatedImage(models.Model):
    service = models.ForeignKey(ServiceImage, related_name='service_img', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    img_url = models.URLField(default='', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.moment.name} - {"Related Image"}'



class MomentImage(models.Model):
      name = models.CharField(max_length=255, default='Momento')
      image = models.ImageField(upload_to='media/')
      date_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name


class MomentRelatedImage(models.Model):
    moment = models.ForeignKey(MomentImage, related_name='moment_img', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    img_url = models.URLField(default='', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.moment.name} - {"Related Image"}'
  
  
class Setting(models.Model):
      name = models.CharField(max_length=255, default='Setting')
      icon = models.ImageField(upload_to='media/')
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name
      
# Nuestros planes
class Plans(models.Model):
      name = models.CharField(max_length=255, default='Plan')
      description = models.TextField(default='Descripción del plan')
      img = models.ImageField(upload_to='media/')
      price = models.IntegerField(default=0)
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name
      
# Carateristicas de los planes
class CaratPlanes(models.Model):
      plans = models.ForeignKey(Plans, related_name='plans', on_delete=models.CASCADE)
      name = models.CharField(max_length=255, default='Plan')
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name