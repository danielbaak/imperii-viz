# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
