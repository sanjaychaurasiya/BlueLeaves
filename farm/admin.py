from django.contrib import admin
from .models import Sensor, FarmBlock, AddSensor, FarmModule


# Register your models here.
admin.site.register(Sensor)
admin.site.register(FarmBlock)
admin.site.register(AddSensor)
admin.site.register(FarmModule)
