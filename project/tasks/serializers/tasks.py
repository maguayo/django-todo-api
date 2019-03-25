from rest_framework import serializers
from project.tasks.models import Task
from django.utils import timezone


class TasksodelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("__all__")

    def create(self, validated_data):
        pass
