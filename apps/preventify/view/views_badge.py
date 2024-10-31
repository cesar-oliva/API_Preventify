from rest_framework import viewsets
from preventify.models.models_badge import Badge
from preventify.serializers.serializers_badge import SerializerBadge
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BadgeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Badge.objects.all()
    serializer_class = SerializerBadge