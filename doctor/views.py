from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.SpecializationModel.objects.all()
    serializer_class = serializers.SpecializationSerializers

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.DesignationModel.objects.all()
    serializer_class = serializers.DesignationSerializers

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.DoctorModel.objects.all()
    serializer_class = serializers.DoctorSerializers

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTimeModel.objects.all()
    serializer_class = serializers.AvailableTimeSerializers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializers

