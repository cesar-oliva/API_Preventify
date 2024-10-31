from rest_framework import serializers
from preventify.models.models_reward import Reward

class SerializerReward(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'