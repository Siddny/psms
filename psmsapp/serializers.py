from rest_framework import serializers
from .models import *

class CameraDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraDetail
		fields = '__all__'


class CameraTypesSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraTypes
		fields = '__all__'

class LolSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraTypes
		fields = '__all__'
