# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devhosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='root_certificate',
            field=models.ForeignKey(default=1, to='devhosts.RootCertificate'),
            preserve_default=False,
        ),
    ]
