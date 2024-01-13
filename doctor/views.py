from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework import filters, pagination
from . import models
from . import serializers


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.SpecializationModel.objects.all()
    serializer_class = serializers.SpecializationSerializers

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.DesignationModel.objects.all()
    serializer_class = serializers.DesignationSerializers

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100



class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.DoctorModel.objects.all()
    serializer_class = serializers.DoctorSerializers
    filter_backends = [filters.SearchFilter]

    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']



class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctormodel = doctor_id)
        return query_set


class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTimeModel.objects.all()
    serializer_class = serializers.AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]


class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializers

