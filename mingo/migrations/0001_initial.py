# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('fin_type', models.CharField(max_length=50)),
                ('whale_type', models.CharField(max_length=50)),
                ('blow_type', models.CharField(max_length=50)),
                ('wave_type', models.CharField(max_length=50)),
            ],
        ),
    ]
