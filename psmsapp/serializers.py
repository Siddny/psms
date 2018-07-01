from rest_framework import serializers
from .models import *

class CameraDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraDetail
		fields = '__all__'
		# e = CameraTypes.objects.select_related('name').get(id=1)



class CameraTypesSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraTypes
		fields = '__all__'

class LolSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraTypes
		fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Equipment
		fields = '__all__'

class AssignToolsSerializer(serializers.ModelSerializer):
	employee = EmployeeSerializer(read_only=True)
	equipments = EquipmentSerializer(read_only=True)
	class Meta:
		model = AssignTools
		fields = '__all__'