from rest_framework import serializers
from . import models

# convert model object to JSON
class AppointmentSerializers(serializers.ModelSerializer):
    # OneToOne, ManyToMany, Forigenkey relational model ar id ar poriborte name show korar jonne use kora hoy.
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.AppiontmentModel
        fields = '__all__'