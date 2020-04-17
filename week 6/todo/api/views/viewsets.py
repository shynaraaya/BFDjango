from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_extensions import mixins

from todo.api.models import Task, TaskList
from todo.api.serializers import TaskSerializer, TaskListSerializer


class TaskListsViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class TasksViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs.get('parent_lookup_list'))

    def perform_create(self, serializer):
        task_list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(task_list=TaskList.objects.get(id=task_list_id))
