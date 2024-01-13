from rest_framework import serializers
from . import models

# convert model object to JSON
class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SpecializationModel
        fields = '__all__'

        
class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DesignationModel
        fields = '__all__'

class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTimeModel
        fields = '__all__'

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DoctorModel
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'

