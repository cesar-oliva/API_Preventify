from rest_framework import serializers
from preventify.models.models_token_player import TokenPlayer

class SerializerTokenPlayer(serializers.ModelSerializer):
    class Meta:
        model = TokenPlayer
        fields = '__all__'