from rest_framework import serializers
from preventify.models.models_player import Player

class SerializerPlayer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'