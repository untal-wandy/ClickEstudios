from django.urls import path
from . import views, views_ajax

app_name = 'citas'
urlpatterns = [
    path('', views.DashboardCitas.as_view(), name='dashboard-citas' ),
    path('create-customer/<int:pk>', views.CustomerCreateView.as_view(), name='create-customer'),

    path('appointment-create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('customer-detail/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),  
    path('gallery-moment-select/<int:pk>', views.GalleryMomentSelect.as_view(), name='gallery-moment-select'),  
    path('service-select/<int:pk>', views.ServiceSelect.as_view(), name='service-select'),
    path('all-plans/', views.Plans.as_view(), name='all-plans'),
    
    path('admin-click-estudios', views.Admin.as_view(), name='admin-click-estudios'),
    path('create-user/', views.CreateUser.as_view(), name='create-user'),
    path('list-user', views.ListUser.as_view(), name='list-user'),
    path('actualizaciones', views.Actualizaciones.as_view(), name='actualizaciones'),


    # Administrative views
    path('administrations-citas', views.CitasAdministrations.as_view(), 
        name='administrations-citas' ),  
    
    path('logins/', views.Logins, name='logins'),
    
    path('customer-update/<int:pk>', views.CustomerUpdate.as_view(), 
         name='customer-update'),

    path('userA-update/<int:pk>', views.UserUpdate.as_view(), name='userA-update'),
    
    
    path('service-update/<int:pk>', views.ServiceUpdateView.as_view(), name='service-update'),
    
    path('service-create/', views.ServiceCreateView.as_view(), name='service-create'),
    
    path('moment-image-create/', views.MomentImgeCreate.as_view(), name='moment-image-create'),
    path('moment-image-update/<int:pk>', views.MomentImgeUpdate.as_view(), name='moment-image-update'),

    path('plans-create/', views.PlansCreate.as_view(), name='plans-create'),
    path('plans-update/<int:pk>', views.PlansUpdate.as_view(), name='plans-update'),
    path('histori-sale/', views.HistoriSale.as_view(), name='histori-sale'),
    path('create-rele/', views.CreateRole.as_view(), name='create-role'),
    path('Facebook/Histori/1213232', views.Facebook, name='facebook'),
    


    # Ajax views
    path('finished-cita/', views_ajax.FinishedCita, name='finished-cita'),
    path('delete-service/', views_ajax.DeleteService, name='delete-service'),
    path('delete-moment-image/', views_ajax.DeleteMomentImage, name='delete-moment-image'),
    path('delete-plans/', views_ajax.DeletePlans, name='delete-plans'),
    path('create-caract/', views_ajax.CreateCaract, name='create-caract'),
    path('delete-caract/', views_ajax.DeleteCaract, name='delete-caract'),
    path('reserver/', views_ajax.Reserver, name='reserver'),
    path('sale-service/', views_ajax.SaleService, name='sale-service'),
    path('sale-cancel/', views_ajax.SaleCancel, name='sale-cancel'),







]
