from rest_framework import serializers
from .models import *

class CameraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Camera
		fields = '__all__'