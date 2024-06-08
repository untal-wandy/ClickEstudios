from django.db import models
from datetime import datetime
# Create your models here.

class Customer(models.Model):
      name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
      email = models.EmailField(default='example@gmail.com', blank= True, null=True)  
      number = models.CharField(max_length=20, blank=True, null=True)
      date_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"{self.name} {self.last_name}"
  
  
class Appointment(models.Model):
      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      date_created = models.DateTimeField(auto_now_add=True)
      date_remember = models.DateTimeField()  # Assuming date_remember is a reminder date
      date_remember_time = models.TimeField(default='10:00')  # Time part of the reminder date

      def __str__(self):
            return f"Cita para {self.customer.name} {self.date_remember} "