from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter() # amader router

router.register('list', views.PatientViewset) # router ar antena

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.PatientRegisterViewsset.as_view(), name='register'),
    path('login/', views.UserLoginApiview.as_view(), name='login'),
    path('active/<uid64>/<token>/', views.activate, name='activate')
]
