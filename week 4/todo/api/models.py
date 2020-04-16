from django.db import models
from datetime import datetime
from todo.auth_.models import MyUser


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = TaskListManager()

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    due_on = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=50)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    objects = TaskListManager()

    def __str__(self):
        return '{}: {}'.format(self.due_on, self.name)
