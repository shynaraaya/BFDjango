from django.db import models
from datetime import datetime

from todo.api.validators import validate_file_size, validate_extension
from todo.auth_.models import MyUser


class TaskBoard(models.Model):
    name = models.CharField(max_length=200)

    @property
    def short_name(self):
        raise NotImplementedError()

    class Meta:
        abstract = True


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class TaskList(TaskBoard):
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='todo_images', null=True, blank=True, validators=[validate_file_size,
                                                                                         validate_extension, ])
    objects = TaskListManager()

    @property
    def short_name(self):
        return self.name[:10]

    def __str__(self):
        return self.name


class Task(TaskBoard):
    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=50)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    objects = TaskListManager()

    @property
    def short_name(self):
        return self.name[:5]

    def __str__(self):
        return '{}: {}'.format(self.due_on, self.name)
