# Generated by Django 2.1.7 on 2019-03-25 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('content', models.CharField(blank=True, max_length=254)),
                ('completed', models.BooleanField(default=False)),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_completed', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified', to=settings.AUTH_USER_MODEL)),
                ('shared', models.ManyToManyField(blank=True, null=True, related_name='users_shared_task', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tasks',
                'ordering': ['created'],
                'get_latest_by': 'created',
            },
        ),
    ]
