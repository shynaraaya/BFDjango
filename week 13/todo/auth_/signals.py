from django.db.models.signals import post_save
from django.dispatch import receiver
from todo.auth_.models import MyUser
from todo.api.models import TaskList


@receiver(post_save, sender=MyUser)
def user_created_task_list(sender, instance, created, **kwargs):
    if created:
        TaskList.objects.create(name='Task List created by user', created_by=instance)