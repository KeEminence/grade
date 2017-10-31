# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.CharField(max_length=50)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_dept', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leader_id', models.CharField(max_length=50)),
                ('leader_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mane_id', models.CharField(max_length=50)),
                ('mane_name', models.CharField(max_length=50)),
                ('mane_level', models.CharField(max_length=50)),
                ('mane_dept', models.CharField(max_length=50)),
            ],
        ),
    ]
