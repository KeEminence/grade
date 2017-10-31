# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_id', models.CharField(max_length=50)),
                ('emp_ll_id', models.CharField(max_length=50)),
                ('mane_id', models.CharField(max_length=50)),
                ('emp_beha_grade', models.FloatField()),
                ('emp_gtime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leader_id', models.CharField(max_length=50)),
                ('mane_id', models.CharField(max_length=50)),
                ('leader_con_grade', models.FloatField()),
                ('leader_beha_grade', models.FloatField()),
                ('leader_gtime', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mane_id_active', models.CharField(max_length=50)),
                ('mane_id_passive', models.CharField(max_length=50)),
                ('mane_con_grade', models.FloatField()),
                ('mane_gtime', models.DateField(auto_now=True)),
            ],
        ),
    ]
