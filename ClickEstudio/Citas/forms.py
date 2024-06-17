from django import forms
from .  import models

class CustomerForm(forms.ModelForm):
      class Meta:
            model = models.Customer
            fields = '__all__'  # Include all fields
            
            widgets = {
            'date_choice': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_time_choice': forms.TimeInput(attrs={'type': 'time'}),
        }


      def __init__(self, *args, **kwargs):
            super(CustomerForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
            # Add placeholders to form fields
            # self.fields['name'].widget.attrs['placeholder'] = 'Nombre y Apellidos'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
            self.fields['dni'].widget.attrs['placeholder'] = 'Cedula'
            # self.fields['email'].widget.attrs['placeholder'] = 'Correo electronico'
            # self.fields['number'].widget.attrs['placeholder'] = 'Numero de celular'
            


class AppointmentForm(forms.ModelForm):
      class Meta:
            model = models.Appointment
            fields = ['customer', 'date_remember', 'date_remember_time']  # Especifica los campos que quieres mostrar en el formulario
            
            widgets = {
            'date_remember': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_remember_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

      def __init__(self, *args, **kwargs):
            super(AppointmentForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
                  
                  
                  
class ServiceImageForm(forms.ModelForm):
      class Meta:
            model = models.ServiceImage
            fields = '__all__'  # Include all fields

      def __init__(self, *args, **kwargs):
            super(ServiceImageForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
            # Add placeholders to form fields
            self.fields['image'].widget.attrs['placeholder'] = 'Image URL'
            # self.fields['description'].widget.attrs['placeholder'] = 'Description'
                  
            widgets = {
                        'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})
                  }

                  
                  
class MomentImageForm(forms.ModelForm):
            class Meta:
                  model = models.MomentImage
                  fields = ['name', 'image', ]
                  widgets = {
                        'name': forms.TextInput(attrs={'class': 'form-control'}),
                        'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                  }
                  
                  
class PlansForm(forms.ModelForm):
    class Meta:
        model = models.Plans
        fields = ['name', 'description', 'img', 'price', 'service', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }