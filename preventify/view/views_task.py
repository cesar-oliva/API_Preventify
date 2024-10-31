from rest_framework import viewsets
from preventify.models.models_task import Task
from preventify.serializers.serializers_task import SerializerTask
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = SerializerTask