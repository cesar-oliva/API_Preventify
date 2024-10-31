from rest_framework import serializers
from preventify.models.models_event import Event

class SerializerEvent(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'