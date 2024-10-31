from rest_framework import serializers
from preventify.models.models_task import Task

class SerializerTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'