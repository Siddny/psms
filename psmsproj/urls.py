"""psmsproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from psmsapp.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # ya keegan
    url(r'^camera_detail_add/', AddCameraType.as_view()),
    # create new type of camera
    url(r'^new_type/', NewCameraType.as_view()),
    # show types of cameras
    url(r'^camera_types/', CameraTypeView.as_view()),
    # create camera details
    url(r'^camera_detail_create/', AddCameraDetailView.as_view()),
    # show camera details
    url(r'^camera_detail/', CameraDetailView.as_view()),
    url(r'^createlist/', CreateListCameraDetailView.as_view()),
    url(r'^up/(?P<pk>\d+)', UpCameraDetailView.as_view()),
    url(r'^del/(?P<pk>\d+)', DelCameraDetailView.as_view()),
    url(r'^charts/', chartView.as_view()),
]
