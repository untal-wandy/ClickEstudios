from django.urls import path
from . import views

app_name = 'citas'
urlpatterns = [
    path('', views.DashboardCitas.as_view(), name='dashboard-citas' ),
    path('create-customer/<str:id>', views.CustomerCreateView.as_view(), name='create-customer'),
      path('appointment-create/', views.AppointmentCreateView.as_view(), name='appointment-create'),

]
