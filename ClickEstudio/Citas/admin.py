from django.contrib import admin
from .models import Customer, MomentImage, ServiceImage, Appointment, MomentRelatedImage,Setting,Plans,CaratPlanes, UserA, Role
# Register your models here.

admin.site.register(Customer)
admin.site.register(MomentImage)
admin.site.register(ServiceImage)
admin.site.register(Appointment)
admin.site.register(MomentRelatedImage)
admin.site.register(Setting)
admin.site.register(Plans)
admin.site.register(CaratPlanes)
admin.site.register(UserA)
admin.site.register(Role)