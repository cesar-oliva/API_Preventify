from rest_framework import viewsets
from preventify.models.models_token_player import TokenPlayer
from preventify.serializers.serializers_token_player import SerializerTokenPlayer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TokenPlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TokenPlayer.objects.all()
    serializer_class = SerializerTokenPlayer