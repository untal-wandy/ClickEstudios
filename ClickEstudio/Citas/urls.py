from django.urls import path
from . import views

app_name = 'citas'
urlpatterns = [
    path('', views.DashboardCitas.as_view(), name='dashboard-citas' ),
    path('create-customer/<int:id>', views.CustomerCreateView.as_view(), name='create-customer'),
    path('appointment-create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),  
    
    path('gallery-moment-select/<int:pk>', views.GalleryMomentSelect.as_view(), name='gallery-moment-select'),  

    path('service-select/<int:pk>', views.ServiceSelect.as_view(), name='service-select'),  


]
