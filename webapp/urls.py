from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [

    #register new user
    path('register/',views.register,name='register'),

    #login new user
    path('login/',views.login,name='login'),


    #create new device
    path('register/createdevice/',views.createdevice,name='createdevice'),

    #diplay device data
    path('login/display/',views.display,name='display'),

    path('register/display/',views.display,name='display'),

    #/devices/
    #path('', views.index, name='index'),

    #/devices/id
    #re_path(r'^(?P<device_id>[0-9]+)/$',views.deviceDetails, name="deviceDetails"),
]