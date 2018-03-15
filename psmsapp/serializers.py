from rest_framework import serializers
from .models import *

class CameraSerializer(serializers.ModelSerializer):
	class Meta:
		model = CameraDetail
		fields = '__all__'