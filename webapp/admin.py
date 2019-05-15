from django.contrib import admin
from . models import devices
from . models import data

admin.site.register(devices)
admin.site.register(data)