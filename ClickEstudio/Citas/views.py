from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, View
from . import forms, models
from django.urls import reverse 
from django.http import HttpResponseRedirect

class DashboardCitas(TemplateView):
      template_name = 'citas/inicio.html'
                  
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['moment'] = models.MomentImage.objects.all()
            context['service'] = models.ServiceImage.objects.all()

            return context

      
class CustomerCreateView(CreateView):
      model = models.Customer
      form_class = forms.CustomerForm
      template_name = 'citas/create-customer.html'  

      def form_valid(self, form):
            print(self.request.POST)
            if form.is_valid():
                  form.instance.plan_choice = int(self.request.POST.get('plan_choice'))
                  instance = form.save() 
                  return HttpResponseRedirect(reverse('citas:customer-detail', kwargs={'pk': instance.id}))
            else:
                  print(form.errors)
                  return super().form_invalid(form) 

            
      # def post(self, request, *args, **kwargs):
      #   f = self.form_class(request.POST)
      #   if f.is_valid():
      #       f.save()
      #   else:
      #       print(f)
      #       return super().get(request, *args, **kwargs)
      
class AppointmentCreateView(CreateView):
      model = models.Appointment
      form_class = forms.AppointmentForm
      template_name = 'citas/create-appointment.html'  

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context

      def form_valid(self, form):
            form.save() 
            return super().form_valid(form)
      
class CustomerDetailView(DetailView):
      model = models.Customer
      form_class = forms.CustomerForm
      template_name = 'citas/customer-detail.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
            return context
      
      
class GalleryMomentSelect(DetailView):
      model = models.MomentImage
      template_name = 'citas/gallery-moment-select.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['img'] = self.model.objects.get(id=self.kwargs.get('pk')).moment_img.all()
            context['moment'] = self.model.objects.get(id=self.kwargs.get('pk'))

            
            return context
      
      
class ServiceSelect(DetailView):
      model = models.ServiceImage
      template_name = 'citas/service-select.html'

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['img'] = self.model.objects.get(id=self.kwargs.get('pk')).service_img.all()
            context['service'] = self.model.objects.get(id=self.kwargs.get('pk'))

            
            return context
      
      

      
"""
Manera de obtimizar es que la funcion se active cada 5 horas para verificar cuales usuarios estaran hoy, para enviar un correo de recordatorio
"""