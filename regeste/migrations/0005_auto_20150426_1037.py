# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regeste', '0004_auto_20150426_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regeste',
            name='abstract',
            field=models.TextField(null=True),
        ),
    ]
