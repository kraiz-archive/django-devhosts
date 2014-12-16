from django.db import models

from devhosts.managers import ServerManager


class RootCertificate(models.Model):
    name = models.CharField(max_length=255)

    private_key = models.TextField(
        blank=True,
        help_text='Keep empty to auto generate'
    )

    certificate = models.TextField(
        blank=True,
        help_text='Keep empty to auto generate'
    )


class Server(models.Model):
    domain = models.CharField(max_length=255, db_index=True)
    ip = models.GenericIPAddressField()

    root_certificate = models.ForeignKey(RootCertificate)

    private_key = models.TextField(
        blank=True,
        help_text='Keep empty to auto generate'
    )

    certificate = models.TextField(
        blank=True,
        help_text='Keep empty to auto generate'
    )

    objects = ServerManager()
