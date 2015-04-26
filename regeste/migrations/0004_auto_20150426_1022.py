# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regeste', '0003_auto_20150426_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regeste',
            name='addenda',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='regeste',
            name='analysis',
            field=models.TextField(null=True),
        ),
    ]
