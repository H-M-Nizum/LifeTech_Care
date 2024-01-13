from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.AppiontmentModel.objects.all()
    serializer_class = serializers.AppointmentSerializers


    # # Custom query kortechi, particular Doctor ar jonne, id ke dore
    # def get_queryset(self):
    #     queryset = super().get_queryset()  ## parent ke inherit korlam
    #     doctor_id = self.request.query_params.get('doctor_id')  ## doctor id ke niye aslam
    #     if doctor_id:  ## if doctor id exist kore
    #         queryset = queryset.filter(doctor_id=doctor_id) ## queryset ke overwrite korlam
    #     return queryset  # finally return queryset

    # Custom query kortechi, particular patient ar jonne, id ke dore
    def get_queryset(self):
        queryset = super().get_queryset()  ## parent ke inherit korlam
        patient_id = self.request.query_params.get('patient_id')  ## patient id ke niye aslam
        if patient_id:  ## if patient id exist kore
            queryset = queryset.filter(patient_id=patient_id) ## queryset ke overwrite korlam
        return queryset  # finally return queryset

   