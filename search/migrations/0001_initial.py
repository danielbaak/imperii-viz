# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.TextField()),
                ('birth_date', models.DateField(null=True)),
                ('death_date', models.DateField(null=True)),
                ('gnd_number', models.IntegerField(null=True)),
            ],
        ),
    ]
