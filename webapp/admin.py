from django.contrib import admin
from . models import devices
from . models import data
from . models import real_time_data

admin.site.register(devices)
admin.site.register(data)
admin.site.register(real_time_data)