from django.db import models
from datetime import datetime
from todo.auth_.models import MyUser


class TaskBoard(models.Model):
    name = models.CharField(max_length=200)

    def short_name(self):
        raise NotImplementedError()

    class Meta:
        abstract = True


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class TaskList(TaskBoard):
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = TaskListManager()

    def short_name(self):
        return self.name[:10]

    def __str__(self):
        return self.name


class Task(TaskBoard):
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    due_on = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=50)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    objects = TaskListManager()

    def short_name(self):
        return self.name[:5]

    def __str__(self):
        return '{}: {}'.format(self.due_on, self.name)
