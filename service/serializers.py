from rest_framework import serializers
from . import models

# convert model object to JSON
class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceModel
        fields = '__all__'