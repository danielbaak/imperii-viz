# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20150701_1125'),
        ('person', '0003_person_summary'),
        ('regeste', '0003_auto_20150426_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='regeste',
            name='locations',
            field=models.ManyToManyField(to='location.Location', related_name='locations'),
        ),
        migrations.AddField(
            model_name='regeste',
            name='people',
            field=models.ManyToManyField(to='person.Person', related_name='people'),
        ),
        migrations.AlterField(
            model_name='regeste',
            name='place_of_issue',
            field=models.ForeignKey(null=True, related_name='place_of_issue', to='location.Location'),
        ),
    ]
