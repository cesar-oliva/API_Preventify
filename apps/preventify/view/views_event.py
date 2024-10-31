from rest_framework import viewsets
from preventify.models.models_event import Event
from preventify.serializers.serializers_event import SerializerEvent
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = SerializerEvent