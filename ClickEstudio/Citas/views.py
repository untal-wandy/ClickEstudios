from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from . import forms, models


class DashboardCitas(TemplateView):
      template_name = 'citas/inicio.html'

      
class CustomerCreateView(CreateView):
      model = models.Customer
      form_class = forms.CustomerForm
      template_name = 'citas/create-customer.html'  

      def form_valid(self, form):
            form.save() 
            return super().get(request, *args, **kwargs)
      
      
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
      
      
"""
Manera de obtimizar es que la funcion se active cada 5 horas para verificar cuales usuarios estaran hoy, para enviar un correo de recordatorio
"""