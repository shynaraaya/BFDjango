from django.core.management.base import BaseCommand
import datetime
from todo.api.models import TaskList, Task
from todo.auth_.models import MyUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        TaskList.objects.all().delete()
        for i in range(5):
            task = TaskList.objects.create(name=f'Task List {i}', created_by_id=1)
        self.stdout.write(f'Task {task.id} was created')
