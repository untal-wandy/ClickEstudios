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
      
      def __str__(self):
            return f"{self.name} {self.last_name}"
  
  
class Appointment(models.Model):
      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      date_created = models.DateTimeField(auto_now_add=True)
      date_remember = models.DateTimeField()  # Assuming date_remember is a reminder date
      date_remember_time = models.TimeField(default='10:00')  # Time part of the reminder date

      def __str__(self):
            return f"Cita para {self.customer.name} {self.date_remember} "
      
      
      
      
class ServiceImage(models.Model):
      name = models.CharField(max_length=255, default='Servicio')
      image = models.ImageField(upload_to='service_images/')
      date_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name



class MomentImage(models.Model):
      name = models.CharField(max_length=255, default='Momento')
      image = models.ImageField(upload_to='moment_images/')
      date_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name
