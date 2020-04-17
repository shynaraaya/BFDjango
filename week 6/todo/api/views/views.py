from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo.api.models import Task, TaskList
from todo.api.serializers import TaskSerializer, TaskListSerializer


class TaskListsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class TaskListView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user).filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskListSerializer


class TasksView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(task_list=self.kwargs.get('pk'))

    def get_serializer_class(self):
        return TaskSerializer

    def perform_create(self, serializer):
        task_list_id = self.kwargs.get('pk')
        serializer.save(task_list=TaskList.objects.get(id=task_list_id))


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs.get('pk'), task_list=self.kwargs.get('pk2'))

    def get_serializer_class(self):
        return TaskSerializer
