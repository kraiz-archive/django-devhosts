from dnslib import DNSRecord,RR,QTYPE,RCODE,parse_time
from dnslib.server import BaseResolver

from devhosts.models import Server


class InterceptingResolver(BaseResolver):
    """
    For A queries check if the domain matches one of the server's in db.
    If it matches the server's ip is replied directly.
    If not the query is proxied to the default upstream dns server.
    """
    def resolve(self, request, handler):
        reply = request.reply()

        # we handle A queries only
        if QTYPE[request.q.qtype] == 'A':
            # filter db for this domain
            domain = str(request.q.qname).rstrip('.')
            server = Server.objects.get_for_dns_or_none(domain=domain)
            if server:
                # add the answer to the request
                reply.add_answer(*RR.fromZone(
                    '{domain} {ttl} A {ip}'.format(
                        domain=domain,
                        ttl=300,
                        ip=server.ip
                    )
                ))

        # if there's no anser already, send query upstream
        if not reply.rr:
            proxy_r = request.send('8.8.8.8', 53)
            reply = DNSRecord.parse(proxy_r)

        return reply
