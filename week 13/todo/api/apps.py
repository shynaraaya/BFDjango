from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'todo.api'

    def ready(self):
        import todo.api.signals