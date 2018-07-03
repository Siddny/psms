from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from psmsapp.views import *

urlpatterns = [    
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
    url(r'^delete_cam_type/(?P<pk>\d+)', DelCameraType.as_view()),

    url(r'^employees/', EmployeesView.as_view()),
    url(r'^equipments/', EquipmentView.as_view()),
    url(r'^assign_tool/', AssignToolsView.as_view()),
    # url(r'^book_tool/', BookingToolsView.as_view()),

]