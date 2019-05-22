from django import forms
from django.forms import ModelForm
from . import models

class CreateDevice(forms.ModelForm):
    class Meta:
        model = models.devices
        fields = ['device_name','user_name','user_email','local_ip','mac_address']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = models.data
        fields = ['values']
        