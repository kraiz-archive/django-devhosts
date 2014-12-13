# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('domain', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
