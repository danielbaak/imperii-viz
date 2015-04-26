# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('term', models.CharField(max_length=200)),
                ('regest', models.CharField(max_length=200)),
                ('occurences', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
