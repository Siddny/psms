from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import ( generics, status)
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from datetime import date

from .models import *
from .serializers import ( CameraDetailSerializer, CameraTypesSerializer )


### show camera details
class CameraDetailView(generics.ListAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraDetailSerializer(queryset, many = True)
    return Response(serializer.data)

  # def options(self, *args, **kwargs):
  #   self.response.headers['Access-Control-Allow-Origin'] = '*'
  #   self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
  #   self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

#### create camera details
class AddCameraDetailView(generics.CreateAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer
  def post(self, request, format=None):
    camera_type = CameraTypes.objects.get(id=request.data['camera_type'])

    cameradetail = CameraDetail.objects.create(
                  name = request.data['name'],
                  model = request.data['model'],
                      # status = request.data['status'],
                      camera_type= camera_type)
    return Response(status=status.HTTP_201_CREATED)

  # def options(self, *args, **kwargs):
  #   self.response.headers['Access-Control-Allow-Origin'] = '*'
  #   self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
  #   self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

### show types of cameras
class CameraTypeView(generics.ListAPIView):
  queryset = CameraTypes.objects.all()
  serializer_class = CameraTypesSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraTypesSerializer(queryset, many=True)
    return Response(serializer.data)

  # def options(self, *args, **kwargs):
  #   self.response.headers['Access-Control-Allow-Origin'] = '*'
  #   self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
  #   self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

### create new type of camera
class NewCameraType(generics.CreateAPIView):
  queryset = CameraTypes.objects.all()
  serializer_class = CameraTypesSerializer
  
  def post(self, request):
    cameratype = CameraTypes.objects.create(name = request.data['name'])
    return Response(status=status.HTTP_201_CREATED)

  # def options(self, *args, **kwargs):
  #   self.response.headers['Access-Control-Allow-Origin'] = '*'
  #   self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
  #   self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

# ya keegan
class AddCameraType(generics.CreateAPIView):
    serializer_class = CameraTypesSerializer
    queryset = CameraTypes.objects.all()

    def post(self, request, format=None):
        cameradetail = request.data.pop('cameradetail')
        try:
            camera_type = CameraTypes.objects.create(
              name=request.data['name'])

            for item in cameradetail:
                CameraDetail.objects.create(
                  camera_type=camera_type,
                  status = item['status'],
                  name = item['name'],
                  model = item['model'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    # def options(self, *args, **kwargs):
    #   self.response.headers['Access-Control-Allow-Origin'] = '*'
    #   self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    #   self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

# {
# "cameradetail":[{
#     "name": "infinix",
#     "model": "cannon",
#     "status": null,
#     "camera_type": null
# },{
#     "name": "Kodak",
#     "model": "4567",
#     "status": null,
#     "camera_type": null
# }],
#     "name": "HD"
# }