# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiguaUserApacheNotMacUntil2015',
            fields=[
            ],
            options={
                'db_table': 'digua_user_apache_not_mac_until_2015',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imeidata',
            fields=[
            ],
            options={
                'db_table': 'imeidata',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImeiDistinct',
            fields=[
            ],
            options={
                'db_table': 'imei_distinct',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
