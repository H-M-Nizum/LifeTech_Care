from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.PatientModel.objects.all()
    serializer_class = serializers.PatientSerializers


class PatientRegisterViewsset(APIView):
    serializer_class = serializers.PatientRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)

            return Response("Submisssion done")
        return Response(serializer.errors)