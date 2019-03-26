from rest_framework import serializers
from project.tasks.models import Task
from django.utils import timezone


class TasksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
