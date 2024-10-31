from rest_framework import viewsets
from preventify.models.models_level import Level
from preventify.serializers.serializers_level import SerializerLevel
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LevelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Level.objects.all()
    serializer_class = SerializerLevel