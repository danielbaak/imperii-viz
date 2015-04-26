# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regeste', '0002_auto_20150426_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regeste',
            name='issue_date',
            field=models.BigIntegerField(null=True),
        ),
    ]
