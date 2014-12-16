from django.contrib import admin
from devhosts.models import Server, RootCertificate

admin.site.register(Server)
admin.site.register(RootCertificate)
