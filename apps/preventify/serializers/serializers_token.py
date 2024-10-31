from rest_framework import serializers
from preventify.models.models_token import Token

class SerializerToken(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'