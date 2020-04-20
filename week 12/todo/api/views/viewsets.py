import logging

from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_extensions import mixins

from todo.api.models import Task, TaskList
from todo.api.serializers import TaskSerializer, TaskListSerializer, TaskShortSerializer, TaskFullSerializer

logger = logging.getLogger(__name__)


class TaskListsViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
        logger.info(f'Task List created: {serializer.instance}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'Task List updated: {serializer.instance}')

    def perform_destroy(self, instance):
        instance.delete()
        logger.info(f'Task List deleted: {instance}')


class TasksViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs.get('parent_lookup_list'))

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskFullSerializer
        return TaskShortSerializer

    def perform_create(self, serializer):
        task_list_id = self.kwargs.get('parent_lookup_list')
        serializer.save(task_list=TaskList.objects.get(id=task_list_id))
        logger.info(f'Task object created: {serializer.instance}')
