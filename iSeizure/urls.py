"""iSeizure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('webapp/', include('webapp.urls')),

    #home page
    path('', views.dashboard, name='index'),

    #REST API - devices
    #as_view method treat the deviceList class as a view function
    path('devices/', views.devicesList.as_view()),

    #REST API - File upload view
    path('fileupload/', views.FileUploadView.as_view()),

    #REST API - real time data 
    path('realtimedata/',views.realTimeDataView.as_view())
]



urlpatterns = format_suffix_patterns(urlpatterns) 

# settings.DEBUG defines the development mode - In production media files should be saved somewhere else on the server
if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)