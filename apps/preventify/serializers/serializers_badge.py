from rest_framework import serializers
from preventify.models.models_badge import Badge

class SerializerBadge(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'