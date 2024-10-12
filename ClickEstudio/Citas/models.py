from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
      name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255, default='', blank=True, null=True)
      dni = models.CharField(max_length=20, unique=True, blank=True, null=True)
      email = models.EmailField(default='', blank= True, null=True)  
      number = models.CharField(max_length=20, blank=True, null=True)
      date_created = models.DateTimeField(auto_now_add=True)
      date_choice = models.DateTimeField(default=datetime.now, blank=True, null=True)
      date_time_choice = models.TimeField(default='10:00') 
      plan_choice = models.IntegerField(default=2, blank=True, null=True)
      finished = models.BooleanField(default=False)
      reserve = models.BooleanField(default=False)
      reserver_mount = models.IntegerField(default=500, blank=True, null=True)
      plans = models.ForeignKey('Plans', related_name='plans_customer', on_delete=models.CASCADE, 
                                blank=True, null=True)
      plans_more = models.ManyToManyField('Plans', related_name='plans_more', blank=True)
      saled = models.BooleanField(default=False, blank=True, null=True)
      saled_mount = models.IntegerField(default=0, blank=True, null=True)
      price_reserved = models.IntegerField(default=500, blank=True, null=True)

      
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
    moment = models.ForeignKey(MomentImage, related_name='moment_img', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    img_url = models.URLField(default='', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.moment.name} - {"Related Image"}'
  
  
      
# Nuestros planes
class Plans(models.Model):
      name = models.CharField(max_length=255, default='Plan')
      description = models.TextField(default='Descripción del plan', blank=True, null=True)
      service = models.ForeignKey(ServiceImage, related_name='services', on_delete=models.CASCADE, blank=True, null=True)
      img = models.ImageField(upload_to='media/')
      price = models.IntegerField(default=0)
      final_price = models.IntegerField(default=0)
      date_created = models.DateTimeField(auto_now_add=True)
      is_activate = models.BooleanField(default=True)
      
      def __str__(self):
            return self.name
      
# Carateristicas de los planes
class CaratPlanes(models.Model):
      plans = models.ForeignKey(Plans, related_name='plans', on_delete=models.CASCADE, blank=True, null=True)
      name = models.CharField(max_length=255, default='Plan o Servicio')
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name
      
      
class Adicionales(models.Model):
      plans = models.ForeignKey(Plans, related_name='adicionales', on_delete=models.CASCADE, blank=True, null=True)
      description = models.TextField(default='...')
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.description
      
      
class Role(models.Model):
      name = models.CharField(max_length=255, default='Indefinido')
      description = models.TextField(default="Un rol indefinodo podría tener la capacidad de ver ciertos contenidos que no requieran permisos especiales, como páginas informativas o recursos de ayuda y mas")
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name
      
      
class UserA(models.Model):
      user = models.ForeignKey(User, related_name='userA',  on_delete=models.CASCADE, blank=True, null=True)
      role = models.ForeignKey(Role, related_name='role', on_delete=models.CASCADE, blank=True, null=True)
      img = models.ImageField(upload_to='media/', blank=True, null=True)

      name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      number = models.CharField(max_length=20,  blank=True, null=True)
      birthday = models.DateField(default=timezone.now)
      date_created = models.DateTimeField(auto_now_add=True,  blank=True, null=True)
      active = models.BooleanField(default=True)
      email = models.EmailField()

      def __str__(self):
            return self.name
      

class Permisons(models.Model):
      role = models.ForeignKey(Role, related_name='role_permisons', blank=True, null=True,
                               on_delete=models.CASCADE)
      user = models.ForeignKey(User, related_name='permisons', blank=True, null=True,
                               on_delete=models.CASCADE)
      priori = models.IntegerField(blank=True, null=True, default=0)
      active = models.BooleanField(default=True)
      date_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.role.name
      

class Tweet(models.Model):
      img = models.ImageField(upload_to='media/', blank=True, null=True)
      title = models.CharField(max_length=280)  # Límite de caracteres similar a Twitter
      sub = models.CharField(max_length=280, default='')  # Límite de caracteres similar a Twitter
      p = models.CharField(max_length=280, default='')  # Límite de caracteres similar a Twitter
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      is_activate = models.BooleanField(default=True)

      def __str__(self):
            return self.sub
      


class ImgTweet(models.Model):
      img = models.ForeignKey(Tweet, related_name='img_tweet', blank=True, null=True,
                               on_delete=models.CASCADE)
      img_tweet = models.ImageField(upload_to='media/', blank=True, null=True)
      is_activate = models.BooleanField(default=True)
      
      
class Gastos(models.Model):
      plans = models.ForeignKey(Plans, related_name='gastos_plan', 
                                on_delete=models.CASCADE,  blank=True, null=True)
      service = models.ForeignKey(ServiceImage, related_name='gastos_service', 
                                on_delete=models.CASCADE,  blank=True, null=True)
      adicionales = models.ForeignKey(Plans, related_name='gastos_adicionales', 
                                on_delete=models.CASCADE,  blank=True, null=True)
      name = models.CharField(max_length=100, default='...')
      description = models.TextField(default='...')
      price = models.IntegerField(default=0)
      date = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.name
      