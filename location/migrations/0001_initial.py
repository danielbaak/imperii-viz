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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=10)),
                ('gnd_number', models.IntegerField(null=True)),
            ],
        ),
    ]
