# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('department_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('issue_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Regeste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('issue_date', models.IntegerField()),
                ('abstract', models.TextField(null=True)),
                ('analysis', models.TextField(null=True)),
                ('addenda', models.TextField(null=True)),
                ('issue', models.ForeignKey(to='regeste.Issue')),
                ('issuer', models.ForeignKey(to='person.Person', related_name='regesten')),
                ('place_of_issue', models.ForeignKey(to='location.Location', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegesteUniMainz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uri', models.CharField(max_length=100)),
                ('exchange', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('volume_id', models.IntegerField()),
                ('editor', models.CharField(max_length=200)),
                ('department', models.ForeignKey(to='regeste.Department')),
            ],
        ),
        migrations.AddField(
            model_name='regeste',
            name='uni_mainz',
            field=models.ForeignKey(to='regeste.RegesteUniMainz'),
        ),
        migrations.AddField(
            model_name='issue',
            name='volume',
            field=models.ForeignKey(to='regeste.Volume'),
        ),
        migrations.AlterUniqueTogether(
            name='volume',
            unique_together=set([('volume_id', 'department')]),
        ),
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together=set([('issue_id', 'volume')]),
        ),
    ]
