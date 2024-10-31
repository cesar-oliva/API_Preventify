from rest_framework import viewsets
from preventify.models.models_token import Token
from preventify.serializers.serializers_token import SerializerToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TokenViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Token.objects.all()
    serializer_class = SerializerToken