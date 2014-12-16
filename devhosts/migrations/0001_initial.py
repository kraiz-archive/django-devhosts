# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RootCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('private_key', models.TextField(blank=True, help_text='Keep empty to auto generate')),
                ('certificate', models.TextField(blank=True, help_text='Keep empty to auto generate')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('private_key', models.TextField(blank=True, help_text='Keep empty to auto generate')),
                ('certificate', models.TextField(blank=True, help_text='Keep empty to auto generate')),
                ('domain', models.CharField(max_length=255, db_index=True)),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
