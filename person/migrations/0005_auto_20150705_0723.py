# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20150701_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='summary',
        ),
        migrations.AlterField(
            model_name='person',
            name='gnd_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
