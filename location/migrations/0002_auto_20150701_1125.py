# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('name', 'latitude', 'longitude')]),
        ),
    ]
