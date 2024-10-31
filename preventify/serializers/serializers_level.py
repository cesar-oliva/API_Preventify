from rest_framework import serializers
from preventify.models.models_level import Level

class SerializerLevel(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'