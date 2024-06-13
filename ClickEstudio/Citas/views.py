from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, View, UpdateView
from . import forms, models
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .Options import Mail 
from django.urls import reverse_lazy


class DashboardCitas(TemplateView, Mail):
      template_name = 'citas/inicio.html'
                  
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['moment'] = models.MomentImage.objects.all()
            context['service'] = models.ServiceImage.objects.all()
            context['setting'] = models.Setting.objects.get(name='icon')
            # print(self.SendGmail('untal.wandy@gmail.com', 'Prueba', 'Esto es una prueba de correo'))
            return context
      

class CitasAdministrations(TemplateView, Mail):
      template_name = 'citas/administration/aministrations.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['c'] = models.Customer.objects.filter(finished=False)
            context['setting'] = models.Setting.objects.get(name='icon')

            return context
      


      
class CustomerCreateView(CreateView, Mail):
      model = models.Customer
      form_class = forms.CustomerForm
      template_name = 'citas/create-customer.html'  

      def form_valid(self, form):
            print(self.request.POST)
            if form.is_valid():
                  form.instance.plan_choice = int(self.request.POST.get('plan_choice'))
                  instance = form.save() 
                  
                  # self.SendGmail(form.instance.email, 'Confirmacion', 
                  #             'Esta es la confirmacion de tu cita, gracias por elegirnos.')
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
      
      
class ServiceCreateView(CreateView):
      model = models.ServiceImage
      form_class = forms.ServiceImageForm
      template_name = 'citas/create-service.html'
      success_url = reverse_lazy('citas:service-create')

      def form_valid(self, form):
            # Imprime los datos POST para depuración
            print(self.request.POST)
            # Guarda el formulario y luego llama a super().form_valid(form) para redirigir
            # response = super().form_valid(form)
            return super().form_valid(form)

      def form_invalid(self, form):
            # Imprime los errores del formulario para depuración
            print(form.errors)
            return super().form_invalid(form)
      
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['service'] = models.ServiceImage.objects.all()
            context['service_admin'] = True
            # context['service'] = self.model.objects.get(id=self.kwargs.get('pk'))
            return context
      
      
class ServiceUpdateView(UpdateView):
      model = models.ServiceImage
      form_class = forms.ServiceImageForm
      template_name = 'citas/update-service.html'
      success_url = reverse_lazy('citas:service-create')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['img'] = self.model.objects.get(id=self.kwargs.get('pk')).image.url
            context['service_admin'] = True
            # context['service'] = self.model.objects.get(id=self.kwargs.get('pk'))
            return context
      
      
      
      def form_valid(self, form):
            print(self.request.POST)
            # Guarda el formulario y luego llama a super().form_valid(form) para redirigir
            # response = super().form_valid(form)
            return super().form_valid(form)

      def form_invalid(self, form):
            # Imprime los errores del formulario para depuración
            print(form.errors)
            return super().form_invalid(form)

      
"""
Manera de obtimizar es que la funcion se active cada 5 horas para verificar cuales usuarios estaran hoy, para enviar un correo de recordatorio
"""