from django.http import HttpResponse

#REST
from rest_framework.parsers import FileUploadParser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.template import loader
from . models import devices
from . models import real_time_data
from . serializers import devicesSerializer
from . serializers import FileUploadSerializer
from . serializers import realTimeDataSerializer

from rest_framework import viewsets
from . import serializers
from webapp import models

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import forms
from django.contrib.auth import login

#import SMSSender


#register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in 
            return redirect('display/')
    else:
        form = UserCreationForm()
    return render(request,'webapp/register.html',{'form':form})


#user login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid()==True:
            #log the user in 
            return redirect('display/')
    else:
        form = AuthenticationForm()
    return render(request,'webapp/login.html',{'form':form})



#DASHBOARD-To view data
def dashboard(request):
    #return render(request, 'webapp/dashboard.html')
    all_real_time_data = real_time_data.objects.all()
    template = loader.get_template('webapp/dashboard.html')
    context = {
        'all_real_time_data': all_real_time_data,
    }
    return HttpResponse(template.render(context, request))


#create a new device
def createdevice(request):
    form = forms.CreateDevice()
    return render(request,'webapp/create_device.html',{'form':form})

#displaying a device
def display(request):
    return render(request,'webapp/display.html')


#REST API for registering a device
class devicesList(APIView):

    #GET
    def get(self,request):
        stock = devices.objects.all()
        serializer = devicesSerializer(stock, many=True)
        return Response({"devices":serializer.data})
        

    #POST
    def post(self, request):
        #fetching JSON object
        new_device_data = request.data.get('devices')

        #serializing JSON object to a serializer object   
        new_device = devicesSerializer(data=new_device_data)    

        print (new_device.Meta)
        if new_device.is_valid(raise_exception=True):
            mac = new_device.save()

        sending_device_id = list(devices.objects.all().filter(mac_address=mac).values('id'))[0].get('id')
        #return Response({"success": "Device '{}' created successfully".format(new_device_saved.device_name)})
        response = HttpResponse( '%s%d%s' %("Device registered successfully!. Your device id is ", sending_device_id,"."))
        return response
   



#REST API for recieving real time data
class realTimeDataView(APIView):
        
    #POST
    def post(self, request):
        #fetching JSON object
        new_device_data = request.data.get('real_time_data')

        #serializing JSON object to a serializer object/django models
        new_data = realTimeDataSerializer(data=new_device_data)    

        if new_data.is_valid(raise_exception=True):
            new_data_saved = new_data.save()
        
        response = HttpResponse("Data recieved successfully")
        return response
   
        
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileUploadSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#class smsSenderView()