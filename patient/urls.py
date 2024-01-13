from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('list', views.PatientViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.PatientRegisterViewsset.as_view(), name='register'),
]
