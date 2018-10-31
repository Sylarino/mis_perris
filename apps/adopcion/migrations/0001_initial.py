# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-31 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('run', models.CharField(max_length=10)),
                ('fNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('tipoVivienda', models.CharField(max_length=50)),
            ],
        ),
    ]