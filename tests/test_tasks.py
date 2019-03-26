import pytest
import json
from django.test import Client
from django.urls import reverse
from rest_framework import status
from project.tasks.models import Task


@pytest.mark.django_db
def test_task_create(create_user, login_user):
    token = "JWT " + login_user
    c = Client(HTTP_AUTHORIZATION=token)

    response = c.post(
        reverse("tasks-list"),
        content_type="application/json",
        data=json.dumps({"title": "Do some nerdy stuff!"}),
    )

    body = response.json()["data"]

    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(id=body["id"], title=body["title"]).exists()
    assert response.json()["success"] == True
    assert body["title"] == "Do some nerdy stuff!"
    assert body["slug"] == "do-some-nerdy-stuff"



@pytest.mark.django_db
def test_task_list(create_user, login_user):
    token = "JWT " + login_user
    c = Client(HTTP_AUTHORIZATION=token)

    response = c.post(
        reverse("tasks-list"),
        content_type="application/json",
        data=json.dumps({"title": "Do some nerdy stuff!"}),
    )

    task1 = response.json()["data"]

    response = c.post(
        reverse("tasks-list"),
        content_type="application/json",
        data=json.dumps({"title": "Buy Bitcoin"}),
    )

    task2 = response.json()["data"]

    response = c.get(
        reverse("tasks-list"),
        content_type="application/json",
    )

    body = response.json()["data"]

    assert response.status_code == status.HTTP_200_OK
    assert Task.objects.filter(user_id=task2["user"]).count() == len(body)
    assert response.json()["success"] == True
    assert body[0]["title"] == "Do some nerdy stuff!"
    assert body[0]["slug"] == "do-some-nerdy-stuff"
    assert body[1]["title"] == "Buy Bitcoin"
    assert body[1]["slug"] == "buy-bitcoin"
