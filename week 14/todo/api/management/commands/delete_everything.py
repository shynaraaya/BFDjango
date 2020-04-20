from django.core.management import BaseCommand

from todo.api.models import TaskList, Task


class Command(BaseCommand):

    def handle(self, *args, **options):
        TaskList.objects.all().delete()
        Task.objects.all().delete()

        self.stdout.write('All objects were deleted')
