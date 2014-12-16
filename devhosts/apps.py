from django.apps import AppConfig


class DevHostsConfig(AppConfig):
    name = 'devhosts'
    verbose_name = 'DevHosts'

    def ready(self):
        import devhosts.signals
