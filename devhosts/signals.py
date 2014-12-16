from django.db.models.signals import pre_save
from django.dispatch import receiver

from devhosts.models import RootCertificate, Server
from devhosts.ssl import *


@receiver(pre_save, sender=RootCertificate)
def generate_root_certificate(sender, instance, **kwargs):
    if not instance.private_key:
        pkey = create_key()
        instance.private_key = dump_key(pkey)
    if not instance.certificate:
        ca_cert = create_ca_cert(
            load_key(instance.private_key),
            instance.name
        )
        instance.certificate = dump_cert(ca_cert)


@receiver(pre_save, sender=Server)
def generate_server_certificate(sender, instance, **kwargs):
    if not instance.private_key:
        pkey = create_key()
        instance.private_key = dump_key(pkey)
    if not instance.certificate:
        cert = create_signed_cert(
            load_key(instance.private_key),
            instance.domain,
            load_key(instance.root_certificate.private_key),
            load_cert(instance.root_certificate.certificate)
        )
        instance.certificate = dump_cert(cert)
