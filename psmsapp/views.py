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

from django.db import transaction

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import Group

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
                  serial_number = request.data['serial_number'],
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
                  serial_number = request.data['serial_number'],
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
        except Exception as e:
            return Response(data={"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

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
    """
    {
    "cameradetail":[{
        "name": "infinix",
        "model": "cannon",
        "status": null,
        "camera_type": null
    },{
        "name": "Kodak",
        "model": "4567",
        "status": null,
        "camera_type": null
    }],
        "name": "HD"
    }
    """

class EmployeesView(APIView):
  def get(self, request, format=None):
    try:
      employee = User.objects.all()
    except Exception as e:
      return Response(data={"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    return Response(data=employee.values(), status = status.HTTP_200_OK)

  def post(self, request, format=None):
    """
    {
      "name"" "",
      "id_number"" "",
      "email"" "",
      "department"" "",
      "designation"" ""
    }
    """
    try:
      employee = User.objects.create(
        first_name = request.data['first_name'],
        last_name = request.data['last_name'],
        id_number = request.data['id_number'],
        phone_number = request.data['phone_number'],
        email = request.data['email'],
        department = request.data['department'],
        designation = request.data['designation']
        )
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

class EquipmentView(APIView):

  def get(self, request, format=None):
    try:
      equipment = Equipment.objects.all()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(data=equipment.values(), status = status.HTTP_200_OK)

  def post(self, request, format=None):
    """
    {
      "label": "",
      "model": "",
      "serial_number": "",
      "status": "",
      "equipment_type": "",
      "brand": ""
    }
    """
    print(request.data)
    try:
      equipment = Equipment.objects.create(
        label = request.data['label'],
        model = request.data['model'], 
        serial_number = request.data['serial_number'],
        status = request.data['status'],
        equipment_type = request.data['equipment_type'],
        brand = request.data['brand'],
        # availability = request.data['availability']
        )
      equipment.save()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

  def put(self, request, format=None):
    """
    when tool is returned or booked
    {
      "availability": free or book,
      "in_use": false
    }
    OR
    when tool is assigned
    {
      "availability": assign,
      "in_use": true
    }
    NB: only marked as in_use=true if availability=assign
    """
    # print(type(request.data))
    try:
      equipment_instance = Equipment.objects.get(pk=request.data["id"])
      equipment_instance.availability = request.data['availability']
      equipment_instance.in_use = request.data['in_use']

      equipment_instance.save()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)


# class AssignToolsView(APIView):

#   def get(self, request, format=None):
#     try:
#       assign_instances = AssignTools.objects.all()
#     except Exception as e:
#       return Response(e, status = status.HTTP_400_BAD_REQUEST)
#     return Response(data=assign_instances.values(
#       # "employee__first_name",
#       # "employee__last_name",
#       # "employee__id_number",
#       # "employee__phone_number",
#       # "employee__email",
#       # "employee__department",
#       # "employee__designation",
#       # "equipments__label",
#       # "equipments___type",
#       # "equipments__brand",
#       # "equipments__model",
#       # "equipments__serial_number",
#       # "equipments__status",
#       # "equipments__date_added",
#       # "equipments__availability"
#       ), status = status.HTTP_200_OK)

#   def post(self, request, format=None):
#     """
#     {
#         "availability": "assign",
#         "employee": 1,
#         "tools": [1, 2,3]
#     }
#     """
#     print(request.data)
#     try:
#       employee = User.objects.get(id=request.data['employee'])

#       for y in request.data['tools']:
#         print(y)
#         tools = Equipment.objects.get(id=y)

#         assign_tool = AssignTools.objects.create(
#           employee = employee,
#           equipments = tools,
#           )
#     except Exception as e:
#       return Response(e, status = status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_201_CREATED)


class DepartmentView(APIView):
  """
  {
    "name": "lighting dept",
    "HOD": 1
  }
  """
  def post(self, request, format=None):
    try:
      department = Department.objects.create(
        name=request.data['name'],
        HOD=User.objects.get(id=request.data['HOD'])
        )
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

  def get(self, request, format=None):
    try:
      departments = Department.objects.all()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(data= departments.values(), status=status.HTTP_200_OK)


class ProjectView(APIView):

  """
  {
    "name": "Projo Kubwa",
    "client": "Clients name or brand",
    "location": "Town",
    "producer": 2
  }
  """
  def post(self, request, format=None):
    try:
      Project.objects.create(
        name=request.data['name'],
        client=request.data['client'],
        location=request.data['location'],
        producer=User.objects.get(id=request.data['producer'])
        )
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

  def get(self, request, format=None):
    try:
      projects = Project.objects.all()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(data= projects.values(), status=status.HTTP_200_OK)

class DispatchToUser(APIView):

  """
  {
    "Employee":1
    "equipments":[
      {
        "equipment":2,
        "condition_ontake":"okay"
        "condition_onreturn":"okay"
      }
    ]
  }
  """
  def post(self, request, format=None):
    try:
      dispatch = DispatchToolsToUsers.objects.create(
        employee=User.objects.get(id=request.data['Employee']),
        )
    except Exception as e:
      return Response(data={"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    try:
      for item in request.data['equipments']:
        eq = DispatchToolsToDept.objects.get(id=item["equipment"])
        DispatchToolsToDept.create(
          user_dispatch = dispatch,
          equipment = eq,
          condition_ontake = item["condition_ontake"],
          # FIXME:
          # will be set on return
          # condition_onreturn = item["condition_onreturn"] 
          )

    except Exception as e:
      return Response(data = {"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)

  def get(self, request, format=None):
    try:
      to_dispatch = DispatchToolsToUsers.objects.all()
    except Exception as e:
      return Response(data={"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    return Response(data= to_dispatch.values(), status=status.HTTP_200_OK)


class DispatchToolsToDeptView(APIView):
  """
  {
    "Dept":1,
    "Project":1,
    "Equipment":[1,2,6,3,5,9]
  }
  """
  def post(self, request, format=None):
    try:
      project = Project.objects.get(id=request.data["Project"])
      dept = Department.objects.get(id=request.data["Dept"])
      dispatch = DispatchToDept.objects.create(
        department = dept,
        project = project
      )
      for item in request.data["Equipment"]:
        eq = Equipment.objects.get(id=item)
        DispatchToolsToDept.objects.create(
          dispatch=dispatch,
          equipments=eq
          )
    except Exception as e:
      return Response(data ={"Error":str(e)}, status = status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)

  def get(self, request, format=None):
    try:
      to_dispatch = DispatchToDept.objects.all()
    except Exception as e:
      return Response(data ={"Error":str(e)},status = status.HTTP_400_BAD_REQUEST)
    return Response(data= to_dispatch.values(), status=status.HTTP_200_OK)


    # def get(self, request, pk, format=None):
    #     try:
    #         disp = PurchaseOrders.objects.filter(id=pk, organization=get_auth(request)).values(
    #             'purchase_order_no', 'purchase_order_date')
    #         disp = disp[0]
    #         disp["order_items"] = PurchaseOrderItems.objects.filter(purchase_order=pk, organization = get_auth(request)).values('id','product','product__name','unit_cost','unit_of_measurement','description',"qty")
    #     except Exception as err:
    #         return Response(data={"Error": str(err)}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(data=disp, status=status.HTTP_200_OK)
    ########################################################################################################
    ################################### views #############################################################
    #######################################################################################################
class AssignEmployeesToProject(APIView):
  def post(self, request, format=None):
    """    
    data = {
      "project_id":1,
      "users":[2,4,5,6,7]
    }
    """
    try:   
      project = Project.objects.get(id=request.data["project_id"])
      for item in request.data["users"]:
        user = User.objects.get(id=item)
        project.user_set.add(user)
    except Exception as e:
      return Response(data={"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)
  
  def get(self, request, format=None):
    try:  
      query_set = Project.objects.filter(user = request.user).values()
    except Exception as e:
      return Response(data={"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=query_set,status=status.HTTP_200_OK)

# class RequestedItemsDetailView(APIView):
#   def get(self, request, pk, format=None):
#     Dis



