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
