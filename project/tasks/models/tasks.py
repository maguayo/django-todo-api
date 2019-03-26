from django.utils.text import slugify
from django.db import models
from project.users.models.users import User
from project.models import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)
    content = models.CharField(max_length=254, blank=True)
    due = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        User, related_name="owner", on_delete=models.CASCADE
    )
    shared = models.ManyToManyField(
        User, related_name="users_shared_task", blank=True, null=True
    )
    completed = models.BooleanField(default=False)
    completed_by = models.ForeignKey(
        User,
        related_name="user_completed",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    modified_by = models.ForeignKey(
        User,
        related_name="user_modified",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "tasks"
        get_latest_by = "created"
        ordering = ["created"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)
