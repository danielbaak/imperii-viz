# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regeste', '0004_auto_20150701_1605'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='regesteunimainz',
            unique_together=set([('uri', 'exchange')]),
        ),
    ]
