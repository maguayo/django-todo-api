from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from project.tasks.models import Task
from project.tasks.serializers import TasksModelSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from project.functions import response_wrapper


class TasksList(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serialiser = TasksModelSerializer(tasks, many=True)
        return Response(response_wrapper(data=serialiser.data, success=True))

    def post(self, request):
        data = request.data
        data["user"] = request.user.id

        serialiser = TasksModelSerializer(data=data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response(
            response_wrapper(data=serialiser.data, success=True),
            status=status.HTTP_201_CREATED,
        )


class TasksDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, task_id):
        task = Task.objects.get(id=task_id, user=request.user)
        return Response({})

    def patch(self, request):
        return Response({})
