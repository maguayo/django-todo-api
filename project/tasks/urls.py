from django.urls import include, path
from project.users.views.tasks import TasksList, TasksDetail

urlpatterns = [
    path("tasks/", view=TasksList.as_view(), name="tasks-list"),
    path(
        "tasks/<uuid:task_id>/",
        view=TasksDetail.as_view(),
        name="tasks-detail",
    ),
]
