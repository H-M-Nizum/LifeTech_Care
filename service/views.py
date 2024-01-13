from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

class ServicesViewset(viewsets.ModelViewSet):
    queryset = models.ServiceModel.objects.all()
    serializer_class = serializers.ServicesSerializers
