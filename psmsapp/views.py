from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import ( generics, status)
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from datetime import date

from rest_framework.views import APIView

from .models import *
from .serializers import *


### show camera details
class CameraDetailView(generics.ListAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraDetailSerializer(queryset, many = True)
    return Response(serializer.data)


class CreateListCameraDetailView(generics.ListCreateAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer

  def post(self, request, format=None):
    camera_type = CameraTypes.objects.get(id=request.data['camera_type'])

    cameradetail = CameraDetail.objects.create(
                  name = request.data['name'],
                  model = request.data['model'],
                  p_serial_number = request.data['p_serial_number'],
                  status = request.data['status'],
                  camera_type= camera_type)
    return Response(status=status.HTTP_201_CREATED)

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraDetailSerializer(queryset, many = True)
    return Response(serializer.data)

class UpCameraDetailView(generics.RetrieveUpdateAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer

  def put(self, request, pk, format=None):
      try:
          updated_camera = CameraDetail.objects.get(pk=pk)
          serializer = CameraDetailSerializer(
              updated_camera, data=request.data)
          if serializer.is_valid():
              serializer.save()
          else:
              return Response({"response": "data not valid"})
          return Response(serializer.data)
      except Exception as e:
          raise e

class DelCameraDetailView(generics.RetrieveDestroyAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer

  def delete(self, request, pk, format=None):
      try:
          updated_camera = CameraDetail.objects.get(pk=pk)
          updated_camera.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
          raise e


#### create camera details
class AddCameraDetailView(generics.ListCreateAPIView):
  queryset = CameraDetail.objects.all()
  serializer_class = CameraDetailSerializer
  def post(self, request, format=None):
    camera_type = CameraTypes.objects.get(id=request.data['camera_type'])

    cameradetail = CameraDetail.objects.create(
                  name = request.data['name'],
                  model = request.data['model'],
                  p_serial_number = request.data['p_serial_number'],
                  status = request.data['status'],
                  camera_type= camera_type)
    return Response(status=status.HTTP_201_CREATED)



### show types of cameras
class CameraTypeView(generics.ListAPIView):
  queryset = CameraTypes.objects.all()
  serializer_class = CameraTypesSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraTypesSerializer(queryset, many=True)
    return Response(serializer.data)



### create new type of camera
class NewCameraType(generics.CreateAPIView):
  queryset = CameraTypes.objects.all()
  serializer_class = CameraTypesSerializer
  
  def post(self, request):
    cameratype = CameraTypes.objects.create(name = request.data['name'])
    return Response(status=status.HTTP_201_CREATED)

### delete type of camera
class DelCameraType(generics.RetrieveDestroyAPIView):
  queryset = CameraTypes.objects.all()
  serializer_class = CameraTypesSerializer

  def delete(self, request, pk, format=None):
      try:
          updated_camera_type = CameraTypes.objects.get(pk=pk)
          updated_camera_type.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      except Exception as e:
          raise e


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

class chartView(generics.ListAPIView):
  queryset = CameraDetail.objects.filter(status="Bad")
  # queryset2 = CameraDetail.objects.filter(status="Fair")
  # queryset3 = CameraDetail.objects.filter(status="Bad")
  serializer_class = CameraDetailSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = CameraTypesSerializer(queryset, many=True)
    return Response(serializer.data)
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

class EmployeesView(generics.ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

  # def get(self, request, format=None):
  #   try:
  #     employee = queryset
  #   except Exception as e:
  #     return Response(e, status = status.HTTP_400_BAD_REQUEST)
  #   return Response(data=employee, status = status.HTTP_200_OK)

  def post(self, request, format=None):
    print(request.data)
    try:
      employee = Employee.objects.create(
        name = request.data['name'],
        id_number = request.data['id_number'],
        email = request.data['email'],
        department = request.data['department'],
        designation = request.data['designation']
        )
    except Exception as e:
      return Response(e,status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

class EquipmentView(generics.ListCreateAPIView):
  queryset = Equipment.objects.all()
  serializer_class = EquipmentSerializer

  # def get(self, request, format=None):
  #   try:
  #     equipment = queryset
  #   except Exception as e:
  #     return Response(status = status.HTTP_400_BAD_REQUEST)
  #   return Response(data=equipment, status = status.HTTP_200_OK)

  def post(self, request, format=None):
    try:
      equipment = Equipment.objects.create(
        name = request.data['name'],
        model = request.data['model'], 
        p_serial_number = request.data['p_serial_number'],
        status = request.data['status'],
        _type = request.data['_type'],
        brand = request.data['brand']
        )
    except Exception as e:
      return Response(status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

class AssignToolsView(generics.ListCreateAPIView):
  queryset = AssignTools.objects.all()
  serializer_class = AssignToolsSerializer

# {
#     "availability": "book",
#     "employee": 1,
#     "equipments": 1  
# }

  def post(self, request, format=None):
    print(request.data)
    employee = Employee.objects.get(id=request.data['employee'])
    equipments = Equipment.objects.get(id=request.data['equipments'])
    try:
      assign_tool = AssignTools.objects.create(
        availability = request.data['availability'],
        employee = employee,
        equipments = equipments,
        )
    except Exception as e:
      return Response(e, status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)
