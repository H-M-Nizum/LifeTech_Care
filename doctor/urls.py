from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('specialization', views.SpecializationViewset) # router ar antena
router.register('designation', views.DesignationViewset) # router ar antena
router.register('list', views.DoctorViewset) # router ar antena
router.register('availabletime', views.AvailableTimeViewset) # router ar antena
router.register('review', views.ReviewViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),
]
