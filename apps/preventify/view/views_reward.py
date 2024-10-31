from rest_framework import viewsets
from preventify.models.models_reward import Reward
from preventify.serializers.serializers_reward import SerializerReward
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RewardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reward.objects.all()
    serializer_class = SerializerReward