from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, View, UpdateView
from . import forms, models
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .Options import Mail, Options
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

class DashboardCitas(TemplateView, Mail):
      template_name = 'citas/inicio.html'
                  
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['moment'] = models.MomentImage.objects.all()
            context['service'] = models.ServiceImage.objects.all()
            context['setting'] = models.Setting.objects.get(name='icon')
            context['plans'] = models.Plans.objects.all()

            # print(self.SendGmail('untal.wandy@gmail.com', 'Prueba', 'Esto es una prueba de correo'))
            return context
      

class CitasAdministrations(TemplateView, Mail):
      template_name = 'citas/administration/aministrations.html'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['c'] = models.Customer.objects.filter(finished=False)
            context['setting'] = models.Setting.objects.get(name='icon')
            context['plans'] = models.Plans.objects.all()
            return context
      


      
class CustomerCreateView(CreateView, Mail):
      model = models.Customer
      form_class = forms.CustomerForm
      template_name = 'citas/create-customer.html'  

      def form_valid(self, form):
            if form.is_valid():
                  form.instance.plan_choice = int(self.request.POST.get('plan_choice'))
                  form.instance.plans = models.Plans.objects.get(id=self.kwargs.get('pk'))
                  form.save() 
                  return HttpResponseRedirect(reverse('citas:customer-detail', kwargs={'pk': form.instance.id}))

      def form_invalid(self, form):
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
            context['plans'] = self.model.objects.get(id=self.kwargs.get('pk')).services.all()

            
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
            context['plans'] = models.Plans.objects.all()

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
            context['plans'] = models.Plans.objects.all()

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
      
      
class MomentImgeCreate(CreateView):
      model = models.MomentImage
      form_class = forms.MomentImageForm
      template_name = 'citas/moment-image-create.html'
      success_url = reverse_lazy('citas:moment-image-create')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['moment'] = models.MomentImage.objects.all()
            context['service_admin'] = True
            context['plans'] = models.Plans.objects.all()

            # context['service'] = self.model.objects.get(id=self.kwargs.get('pk'))
            return context
      
      
      def form_valid(self, form):
            print(self.request.POST, self.request.FILES)
            
            # Guarda el formulario y luego llama a super().form_valid(form) para redirigir
            # response = super().form_valid(form)
            return super().form_valid(form)

      def form_invalid(self, form):
            # Imprime los errores del formulario para depuración
            print(form.errors)
            return super().form_invalid(form)
      
      
      
class MomentImgeUpdate(UpdateView):
      model = models.MomentImage
      form_class = forms.MomentImageForm
      template_name = 'citas/moment-image-update.html'
      success_url = reverse_lazy('citas:moment-image-create')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['moment'] = models.MomentImage.objects.all()
            context['service_admin'] = True
            context['plans'] = models.Plans.objects.all()

            # context['service'] = self.model.objects.get(id=self.kwargs.get('pk'))
            return context
      
      
      def form_valid(self, form):
            print(self.request.POST, self.request.FILES)
            
            # Guarda el formulario y luego llama a super().form_valid(form) para redirigir
            # response = super().form_valid(form)
            return super().form_valid(form)

      def form_invalid(self, form):
            # Imprime los errores del formulario para depuración
            print(form.errors)
            return super().form_invalid(form)
      
      
      
      
class PlansCreate(CreateView):
      model = models.Plans
      form_class = forms.PlansForm
      template_name = 'citas/plans-create.html'
      success_url = reverse_lazy('citas:plans-create')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['plans'] = models.Plans.objects.all()

            # context['moment'] = models.MomentImage.objects.all()
            context['service_admin'] = True
            return context
      
      def form_valid(self, form):
            return super().form_valid(form)

      def form_invalid(self, form):
            return super().form_invalid(form)
      
      
 
class PlansUpdate(UpdateView):
      model = models.Plans
      form_class = forms.PlansForm
      template_name = 'citas/plans-update.html'
      success_url = reverse_lazy('citas:plans-create')
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['img'] = self.model.objects.get(id=self.kwargs.get('pk')).img.url
            # context['moment'] = models.MomentImage.objects.all()
            context['service_admin'] = True
            context['plans'] = models.Plans.objects.all()
            context['edit'] = True

            return context
      
      def form_valid(self, form):
            return super().form_valid(form)

      def form_invalid(self, form):
            return super().form_invalid(form)



class CustomerUpdate(UpdateView, Options):
      model = models.Customer
      form_class = forms.CustomerForm2
      template_name = 'citas/customer-update.html'
      success_url = reverse_lazy('citas:administrations-citas'  )

      def get_context_data(self, **kwargs):
            c = self.model.objects.get(id=self.kwargs.get('pk'))
            context = super().get_context_data(**kwargs)
            context['service_admin'] = True
            context['plans'] = models.Plans.objects.all()
            context['plans_choice'] = c.plans if hasattr(c, 'plans') else None
            return context

      def form_valid(self, form):
            if self.request.POST.get('select') != None:
                  form.instance.plans =  models.Plans.objects.get(id=self.request.POST.get('select'))
                  form.save()
            return self.RedirectReverse('citas:customer-update', self.kwargs.get('pk') )

      def form_invalid(self, form):
            print(form.errors)
            return super().form_invalid(form)

      
"""
Manera de obtimizar es que la funcion se active cada 5 horas para verificar cuales usuarios estaran hoy, para enviar un correo de recordatorio
"""