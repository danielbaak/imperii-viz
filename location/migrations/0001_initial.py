# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('gnd_number', models.IntegerField(null=True)),
            ],
        ),
    ]
