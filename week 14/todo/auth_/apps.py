from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'todo.auth_'

    def ready(self):
        import todo.auth_.signals
