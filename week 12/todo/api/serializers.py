from rest_framework import serializers

from todo.api.validators import validate_name
from todo.auth_.serializers import MyUserSerializer
from todo.api.models import Task, TaskList


class TaskListSerializer(serializers.ModelSerializer):
    created_by = MyUserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'photo')


class TaskSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list',)


class TaskShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status',)


class TaskFullSerializer(TaskShortSerializer):
    task_list = TaskListSerializer(read_only=True)

    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('task_list',)
