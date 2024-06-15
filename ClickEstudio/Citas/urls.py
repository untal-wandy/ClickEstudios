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
    
    path('moment-image-create/', views.MomentImgeCreate.as_view(), name='moment-image-create'),
    path('moment-image-update/<int:pk>', views.MomentImgeUpdate.as_view(), name='moment-image-update'),

    path('plans-create/', views.PlansCreate.as_view(), name='plans-create'),
    path('plans-update/<int:pk>', views.PlansUpdate.as_view(), name='plans-update'),


    # Ajax views
    path('finished-cita/', views_ajax.FinishedCita, name='finished-cita'),
    path('delete-service/', views_ajax.DeleteService, name='delete-service'),
    path('delete-moment-image/', views_ajax.DeleteMomentImage, name='delete-moment-image'),
    path('delete-plans/', views_ajax.DeletePlans, name='delete-plans'),
    path('create-caract/', views_ajax.CreateCaract, name='create-caract'),



]
