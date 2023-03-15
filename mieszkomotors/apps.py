from django.apps import AppConfig


class MieszkomotorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mieszkomotors'

    def ready(self):
        import mieszkomotors.signals