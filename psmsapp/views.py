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
from .serializers import ( CameraSerializer )

class CameraDetailView(generics.ListCreateAPIView):
	queryset = CameraDetail.objects.all()
	serializer_class = CameraSerializer

	def list(self, request):
		queryset = self.get_queryset()
		serializer = CameraSerializer(queryset, many = True)
		return Response(serializer.data)