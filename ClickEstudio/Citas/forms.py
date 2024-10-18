from django import forms
from .  import models
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
      class Meta:
            model = models.Customer
            fields = '__all__'  # Include all fields
            


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
            
            
            
class CustomerForm2(forms.ModelForm):
      class Meta:
            model = models.Customer
            fields = '__all__'  # Include all fields
            
            widgets = {
            'date_choice': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_time_choice': forms.TimeInput(attrs={'type': 'time'}),
        }
            
      def __init__(self, *args, **kwargs):
            super(CustomerForm2, self).__init__(*args, **kwargs)
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
                  fields = ['name', 'image', 'service']
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
        
        
class MomentRelatedImageForm(forms.ModelForm):
      class Meta:
            model = models.MomentRelatedImage
            fields = ['moment', 'image', 'service', ]
            widgets = {
                  'moment': forms.Select(attrs={'class': 'form-control'}),
                  'service': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                  'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }
            
            
            
class RoleForm(forms.ModelForm):
      class Meta:
            model = models.Role
            fields = ['name', 'description'] 
            widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
            
class UserAForm(forms.ModelForm):
      class Meta:
            model = models.UserA
            fields = ['user', 'role', 'img', 'name', 'last_name', 'number', 'birthday',  'active', 'email']
            widgets = {
                  'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            }

      def __init__(self, *args, **kwargs):
            super(UserAForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'




class Gastos(forms.ModelForm):
      class Meta:
            model = models.Gastos
            fields = ['name', 'description', 'price']
            widgets = {
             "description":  forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ingrese una descripción detallada'})
                  
            }
            # You can exclude fields here if needed:
            # exclude = ['plans', 'adicionales', 'date']

      def __init__(self, *args, **kwargs):
            super(Gastos, self).__init__(*args, **kwargs)
            for field in self.fields:
                        self.fields[field].widget.attrs['class'] = 'form-control'

      # You can customize form fields here (e.g., add widgets, set labels)
            self.fields['name'].label = 'Nombre del Gasto'  # Change label for 'name' field


class ImageServiceImgForm(forms.ModelForm):
    class Meta:
        model = models.ImageServiceImg
        fields = ['img_service', 'name', 'moment']  # Los campos que se incluirán en el formulario
        widgets = {
                  'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
                  'img_service': forms.Select(attrs={'class': 'form-control'}),
                  'moment': forms.Select(attrs={'class': 'form-control'}),
        }
        
        


class OpenCashForm(forms.Form):
    opening_balance = forms.DecimalField(max_digits=10, decimal_places=2, label='Monto de Apertura')

class CloseCashForm(forms.Form):
    closing_balance = forms.DecimalField(max_digits=10, decimal_places=2, label='Monto de Cierre')
    
    
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']  # Campos del formulario
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'password': 'Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}) ,
        }
        
        

class IngresoForm(forms.ModelForm):
      class Meta:
            model = models.Ingreso
            fields = ['descripcion', 'cantidad']
      
      def __init__(self, *args, **kwargs):
            super(IngresoForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
            # Add placeholders to form fields
            self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripción'
            self.fields['cantidad'].widget.attrs['placeholder'] = 'Cantidad'