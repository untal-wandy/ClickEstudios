from django.urls import path
from . import views, views_ajax

app_name = 'citas'
urlpatterns = [
    path('', views.DashboardCitas.as_view(), name='dashboard-citas' ),
    
    path('create-customer/<int:id>', views.CustomerCreateView.as_view(), name='create-customer'),
    path('appointment-create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),  

    path('gallery-moment-select/<int:pk>', views.GalleryMomentSelect.as_view(), name='gallery-moment-select'),  

    path('service-select/<int:pk>', views.ServiceSelect.as_view(), name='service-select'),  


    # Administrative views
    path('administrations-citas', views.CitasAdministrations.as_view(), 
        name='administrations-citas' ),  
    
    path('service-update/<int:pk>', views.ServiceUpdateView.as_view(), name='service-update'),
    
    path('service-create/', views.ServiceCreateView.as_view(), name='service-create'),


    # Ajax views
    path('finished-cita/', views_ajax.FinishedCita, name='finished-cita'),
    path('delete-service/', views_ajax.DeleteService, name='delete-service'),

]
