from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models
from . import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


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

            token = default_token_generator.make_token(user)
            print('token', token)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)

            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

            email_subject = 'Çonfirm your email'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response(" Check Your mail for confirmation")
        return Response(serializer.errors)