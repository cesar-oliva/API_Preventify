from rest_framework import viewsets
from preventify.models.models_player import Player
from preventify.serializers.serializers_player import SerializerPlayer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = SerializerPlayer