from django.db import models


class ServerManager(models.Manager):

    def get_for_dns_or_none(self, domain):
        return self.get_queryset().filter(domain=domain).first()
