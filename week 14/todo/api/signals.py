from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.api.models import TaskList, Task


@receiver(post_save, sender=TaskList)
def task_created(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(name='Task List without tasks', task_list=instance)



