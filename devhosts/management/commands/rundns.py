import time
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from dnslib.server import DNSServer, DNSHandler, DNSLogger

from devhosts.dns import InterceptingResolver
from devhosts.models import Server


class Command(BaseCommand):
    help = ''
    option_list = (
        make_option('-a', '--address',
            default='0.0.0.0',
            help='Address to bind to.',
        ),
        make_option('-p', '--port',
            default=53,
            type='int',
            help='Port to bind to.',
        )
    ) + BaseCommand.option_list

    def handle(self, *args, **options):
        udp_server = DNSServer(
            resolver=InterceptingResolver(),
            address=options['address'],
            port=options['port'],
            logger=DNSLogger(log={
                '0': '-request,-reply,-truncated,-error',
                '1': '',
                '2': '+recv,+send',
                '3': '+recv,+send,+data'
            }[options['verbosity']])
        )
        udp_server.start_thread()

        try:
            while udp_server.isAlive():
                time.sleep(1)
        except KeyboardInterrupt:
            udp_server.stop()

